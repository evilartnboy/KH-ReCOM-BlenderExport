# pylint: disable=import-error

import bpy
import math
import mathutils
import logging
import numpy as np

class MeshImportError(Exception):
  pass


class Armature:
  def __init__(self, basename, skip_armature_creation=False):
    if not skip_armature_creation:
      self.armature_data = bpy.data.armatures.new('%s_Armature' % basename)
      self.armature_obj = bpy.data.objects.new(basename,self.armature_data)

      bpy.context.scene.collection.objects.link(self.armature_obj)
      bpy.context.view_layer.objects.active = self.armature_obj

    self.bone_matrices = []
    self.bone_names = []


class Submesh:
  def __init__(self, object_name, armature, invert_normals=False):
    self._armature = armature
    self.invert_normals = invert_normals

    self.vtx = []
    self.vn = []
    self.uv = []
    self.vcol = []
    self.tri = []
    self.bone_vertex_list = [[] for _ in range(len(armature.bone_names))]

    self.mesh_data = bpy.data.meshes.new(object_name + '_mesh_data')
    self.mesh_obj = bpy.data.objects.new(object_name, self.mesh_data)

  def update(self, skip_vertex_groups=False):
    self.mesh_data.from_pydata(self.vtx, [], self.tri)
    self.mesh_data.update()

    if self.vcol:
      self.mesh_data.vertex_colors.new()
      self.mesh_data.vertex_colors[-1].data.foreach_set('color', [
          rgba for col in
          [self.vcol[loop.vertex_index] for loop in self.mesh_data.loops]
          for rgba in col
      ])

    if self.uv:
      self.mesh_data.uv_layers.new(do_init=False)
      self.mesh_data.uv_layers[-1].data.foreach_set('uv', [
          vt for pair in
          [self.uv[loop.vertex_index] for loop in self.mesh_data.loops]
          for vt in pair
      ])

    if self.invert_normals:
      self.mesh_data.flip_normals()

    if skip_vertex_groups:
      return
    for i, v_list in enumerate(self.bone_vertex_list):
      if not v_list:
        continue
      group = self.mesh_obj.vertex_groups.new(name=self._armature.bone_names[i])
      for v, weight in v_list:
        group.add([v], weight, 'ADD')

  def update_normals(self):
    if not self.vn:
      return

    vn_loop = []
    for face in self.mesh_data.polygons:
      for vertex_index in face.vertices:
        vn_loop.append(self.vn[vertex_index])
      face.use_smooth = True
    self.mesh_data.use_auto_smooth = True
    self.mesh_data.normals_split_custom_set(vn_loop)


class MeshParser:
  def __init__(self,mat_manager,armature=None,skip_armature_creation=False,skip_textureless_meshes=False):

    self._mat_manager = mat_manager
    self._armature = armature
    self._skip_armature_creation = skip_armature_creation
    self._skip_textureless_meshes = skip_textureless_meshes
    self._texture_names = []

  def parse(self, f, model_offs, basename):
    #The way seek and read works is seek sets the pointer to that location
    #Read returns what it atempts to read in the format called and then moves the pointer to one after the end of it

    #Will go to the model offset of each submodel in the mdl file
    f.seek(model_offs + 0xC) #At offset 28 a int lists the number of textures
    texture_table_count = f.read_uint32() 
    texture_table_offs = model_offs + f.read_uint32() #Reading at offset 32, is the value read + model offset so the value read at offset 0, 16 for sora    
    vif_opaque_offs = f.read_uint32() #offset 36
    print("vif_opaque_offs",vif_opaque_offs+model_offs)
    vif_translucent_offs = f.read_uint32() #offset 40
    print("vif_translucent_offs",vif_translucent_offs+model_offs)
    if texture_table_count == 0 and self._skip_textureless_meshes:
      return [], self._armature

    if not self._armature:
      self._armature = self._parse_armature(f, model_offs, basename)
    
    self.texture_names = self._parse_texture_table(f, texture_table_offs,texture_table_count)
    
    objects = []
    if vif_opaque_offs:#For all normal textured messhes
      objects += self._parse_vif_packets(f, model_offs + vif_opaque_offs,basename, False)
    if vif_translucent_offs:#For all transparent meshes
      objects += self._parse_vif_packets(f, model_offs + vif_translucent_offs,basename, True)

    return objects, self._armature

  def _parse_armature(self, f, model_offs, armature_basename):
    armature = Armature(armature_basename, self._skip_armature_creation)

    f.seek(model_offs) #Offsets read at 0
    bone_count = f.read_uint16() #Offset read from offset 0 has the bone count read in unint
    
    if bone_count <= 0:
      return
    armature.bone_matrices = [None] * bone_count
    armature.bone_names = [None] * bone_count
    f.skip(2) #Since uint16 reads only 2 bytes 2 more need to be skipped
    bone_table_offs = model_offs + f.read_uint32() #Adds the model offset to the value read at offset 20  
    transform_table_offs = model_offs + f.read_uint32() # Adds the model offset (probably 16) to the value read at offset 24 (This will be a different number depending on model size)
   

    if not self._skip_armature_creation:
      current_mode = bpy.context.object.mode
      bpy.ops.object.mode_set(mode='EDIT', toggle=False)

    ###############################################################################################
    for i in range(bone_count): #for each bone in the model, probably offset 64
      print("----------------------------------------------------------------------Bone#", i)
      
      f.seek(bone_table_offs + i * 0x14) # Read bone_table offest + i * certian ammount (+20 when converted from hex)
      #print("Bone name/parent data offset:", f.tell())
      bone_name = f.read_string(0x10) ## Reads 16 bytes for the name
     # print("Bone Name:", bone_name)
      
      parent_index = f.read_int16() ##The last 2 bytes of the bone
     # print("Parent bone:", parent_index)
      bone_index = i 
      
      f.seek(transform_table_offs + i * 0x40) #Gets the position data of the bone  from the transform table off + I * 64
      #print("Bone matrix start offset:", f.tell())
      local_matrix = mathutils.Matrix([f.read_nfloat32(4) for _ in range(4)]) 
      ##Structure: Inherit roll?, Roll left?, Roll Right?, Roll up?
      #            Rotation up?, Rotation down?, Parent rotation bool?, Rotation?/Roll?
      #            -off_z, off_x , -off_y, apply off of parent bone bool
      ## 

      #print("---------------------------------------------Bone matrix end offset:", f.tell() - 0x1)
      #Bone Name, location and data in the mdl file
      print(bone_name)
      #print(transform_table_offs + i * 0x40)
      
      
      
      local_matrix.transpose()
      #print(local_matrix)
      
      if parent_index >= 0:
        global_matrix = armature.armature_data.edit_bones[parent_index].matrix @ local_matrix
      else:
        global_matrix = local_matrix

      armature.bone_matrices[bone_index] = global_matrix
      armature.bone_names[bone_index] = bone_name
      
      if not self._skip_armature_creation:
        bone = armature.armature_data.edit_bones.new(bone_name)
        bone.tail = (0.025, 0, 0) #Tail bone location
        bone.use_inherit_rotation = True 
        bone.use_local_location = True
        bone.matrix = global_matrix
        if parent_index >= 0:
          bone.parent = armature.armature_data.edit_bones[parent_index]
      
      ##############################################################################################

    
    if not self._skip_armature_creation:
      armature.armature_obj.rotation_euler = (math.pi / 2, 0, 0) #Blender rotation
      bpy.ops.object.mode_set(mode=current_mode, toggle=False)
      armature.armature_obj.select_set(state=True)
    
    return armature

  def _parse_texture_table(self, f, texture_table_offs, texture_table_count):
    f.seek(texture_table_offs) #Reading at offset 32, is the value read + model offset so the value read at offset 0, 16 for sora 
    print("Texture table offset start:", f.tell(), " Reads strings of length 32", texture_table_count, " times. The first vertex determines the texture file used. Ends at offset", f.tell()+ (texture_table_count*32))
    return [f.read_string(0x20) for i in range(texture_table_count)] #For sora it is the string starting from offset 1072

  def _parse_vif_packets(self, f, offs, basename, is_translucent):
    # {material index -> Submesh}
    #This def is called twice, once for opauqe models, once for transparent ones. Is seperated by the is_translucent bool
    #The offset is the values read at either offset 36 or 40, + the model offset (probably 16)
    submesh_dict = dict() #Submesh dictionary
    mesh_index = 0
    
    while offs < f.filesize:
      f.seek(offs) #This while loop increases offset by a yet unknown method       
      dmatag = f.read_uint32() #268435681 for keyblade opauqe
      print("-----------------------------------------------------------------------------------------------------Dmatag :", dmatag, "-----------Dmatag offset:", f.tell()-4,"Is translucent?:",is_translucent)
      
      if dmatag == 0x60000000:  # ret 1,610,612,736
        
        break
      qwc = dmatag & 0xFF # 0xFF =255, Also it seems the qwc is at the offs location as a int16
      #print("QWC:", qwc)
      #print("QWC Offset to next dmatag?:", (qwc + 1) * 16)
      ''''
      if is_translucent == False:
        print("Opauqe")
        print("Offs:", offs)
        print("Datamg:", dmatag)
        print("qwc", qwc)
      else:
        print("Translucent")
        print("Offs:", offs)
        print("Datamg:", dmatag)
        print("qwc", qwc)
      '''
      
      #print("------------------------------------------------------------STCYCL and UNPACK commands(Skipped in blender) offset start:", f.tell(), " Offset end:", f.tell()+16)
      # Skip STCYCL and UNPACK commands and go straight to compressed vertex
      # data since these are not critical for parsing.
      f.skip(0x10) #so offs + 4 from datamag read + 16
      #print("------------------------------------------------------------------------------------------------vertex_table_count, _, vertex_count, _, mode offset start:", f.tell())
      vertex_table_count, _, vertex_count, _, mode = f.read_nuint16(5) #From what i can tell, the table count and vertex count are the same, mode for player mdl is 6
      
      
      print("vertex_table_count:", vertex_table_count)
      #print("vertex_count:", vertex_count)
      #print("mode:", mode)      
      #print("---------------------------------------------------------------------------------------------------vertex_table_count, _, vertex_count, _, mode offset end:", f.tell())

      # TODO: These are known render modes across .AZF and .MDL files, but their
      # exact distinctions are unknown. The render mode specifies which
      # microsubroutine to run in order to process vertex data and send draw
      # instructions to the GIF.
      has_vnormal = has_uv = has_vcol = has_uint_vcol = False
      invert_normals = False

      #The mode determines how large the vertex data in the file is
      if mode == 0x10:  # Pos, mode for shadow mdls
        vertex_byte_size = 0x20
      elif mode == 0x6:  # Pos, UV #Mode for MDL?
        vertex_byte_size = 0x30 #48
        has_uv = True
      elif mode in (0x2, 0x4005):  # Pos, Normal
        vertex_byte_size = 0x30
        has_vnormal = True
      elif mode == 0x4205:  # Pos, UV (Musashi reflective texture?)
        vertex_byte_size = 0x30
        has_uv = True
      elif mode == 0x4009:  # Pos, Color (Musashi inverse hull)
        vertex_byte_size = 0x30
        has_vcol = True
        invert_normals = True
      elif mode in (0x0, 0x5, 0x24, 0x200, 0x406, 0x400B):  # Pos, Color, UV
        vertex_byte_size = 0x40
        has_uv = True
        has_vcol = True
        has_uint_vcol = mode in (0x0, 0x5, 0x24, 0x200)
      elif mode in (0x406E, 0x40EE):  # Pos, Normal, Color, UV (Musashi stages)
        vertex_byte_size = 0x50
        has_vnormal = True
        has_uv = True
        has_vcol = True
      else:
        raise MeshImportError('Unrecognized render mode {} at offset {}'.format(
            hex(mode), hex(offs + 0x1C))) #0x1c = 28

      # Only the first vertex determines the texture to apply.
      if has_uv and mode != 0x4205: #if not mode 16,901
        f.seek(offs + vertex_byte_size + 0x2C) #so offs + 48 for mode 6 + 44        
        texture_index = f.read_uint16() 
        print("Texture index offset:", f.tell()-2, "Texture index: ", texture_index )
      else:
        texture_index = 0

      if texture_index in submesh_dict:
        submesh = submesh_dict[texture_index]
      else: #Assigns the submesh on first loop
        submesh = submesh_dict[texture_index] = Submesh('{}_mat{}{}'.format(basename, texture_index,'_t' if is_translucent else ''), self._armature,invert_normals) #Is the only use of is translucent
      
      v_start = len(submesh.vtx)
      
      v_offs = offs + 0x30 # 0x30 = 48
      #print("V_offs:", v_offs)
      vertex_table_index = 0
      

      #####Vertex search#####
      for v in range(vertex_count):
        # Scan forward for vertices that should be added together due to
        # multiple bone influences.
        #For keyblade v offs is 1152
        
        
        f.seek(v_offs + 0x8) # 0x8 = 8
        
        split_index = f.read_int16() #first offset is 1160 for keyblade. For both sora and keyblade all the split indexes seem to be 0
        
        split_count = 1
        if split_index > 0:
          # Assume max influence of 8 bones.
          for i in range(min(8, vertex_table_count - vertex_table_index - 1)):
            f.seek(v_offs + (i + 1) * vertex_byte_size + 0x8)
            
            print("Split index offset:" ,f.tell())
            next_split_index = f.read_int16()
            if next_split_index <= split_index:
              break
            split_index = next_split_index
            split_count += 1

        vtx = []
        # print(split_count)
        for i in range(split_count): #For both sora and the keyblade the split count is just 1, so this for loop executes once
          
          vertex_table_index += 1
          f.seek(v_offs) #V_offs is offs + 48 +
          #print("-------------------------------------------------------------------------Vertex #:", len(submesh.vtx)+1,"Offset start:", f.tell())
          
          
          flag = f.read_int16() #What is flag for? it is checked if the value is either 0 or 32. Other values seen include -1. I think it is for relations for triangles
          #print("Flag:", flag,"Offset location:", f.tell()-2)
          f.skip(2)#Skip 2 since int16 only reads 2 bytes
          
          vtx_weight = f.read_float32()
          #print("Vtx_weight:", vtx_weight, "Offset location:", f.tell()-4)
          #-0.115641 at 22232
          f.skip(8)
          #print("Vertex location offset:", f.tell())
          vtx_local = f.read_nfloat32(3) + (vtx_weight,) #reads 3 float 32s, I think these are the vertecies position data. Value 0.180951 at offset 1168 on keyblade
          #print("MDL Vertex location XYZ:", vtx_local)
          
          
          f.skip(2)
          bone_index = f.read_int16() #Lists what bone the vertex is attached to
          #print("Parent Bone: ", bone_index, "Offset", f.tell()-2)
          
          if bone_index < 0 or bone_index >= len(self._armature.bone_names):
            raise MeshImportError('Bad bone index {} at offset {}'.format(
                bone_index, hex(v_offs)))

          submesh.bone_vertex_list[bone_index].append((v_start + v, vtx_weight))
          
          #print(self._armature.bone_matrices[bone_index])
          #print(self._armature.bone_matrices[bone_index]@ mathutils.Vector(vtx_local))
          
         

          vtx.append(self._armature.bone_matrices[bone_index] @ mathutils.Vector(vtx_local)) 
          #vtx.append(mathutils.Vector(vtx_local))
          
          if has_vnormal: #Not true for sora or keyblade
            vn = f.read_nfloat32(4)[:3]

          if has_vcol: #Not true for sora or keyblade
            if has_uint_vcol:
              vcol = [
                  c / f for c, f in zip(f.read_nuint32(4), (0x100, 0x100, 0x100,
                                                            0x80))
              ]
            else:
              vcol = [
                  c / f for c, f in zip(f.read_nfloat32(4), (256.0, 256.0,
                                                             256.0, 128.0))
              ]
          if has_uv:#True for sora and keyblade. The UVs determine where on the uv texture map the vertex is
            uv = f.read_nfloat32(2) #Reads the x and y uv positions. Y is inverted with 1-y further down
            ##print("UV:", uv)
            
         # print("-------------------------------------Offset end:", f.tell()+8)
          v_offs += vertex_byte_size

        v_mixed = mathutils.Vector((0, 0, 0, 0))
        for v_elem in vtx:
          v_mixed += v_elem

     
        #----------------------------------------------------------Solve for unknown matrix, in this case original mdl xyz values, slightly off due to rounding
        x = np.dot(np.linalg.inv(self._armature.bone_matrices[bone_index]), v_mixed) 
        #np.linalg.inv(A)  is simply the inverse of A, np.dot is the dot product
        #print ("Vertex# :", len(submesh.vtx), "Flag:", flag)  
        #print("Vertex ", len(submesh.vtx), "UV ", uv[0],uv[1])
        #print("Vstart + v", v_start + v)
        #if(v ==vertex_count-1):
          #print("Matrix:", self._armature.bone_matrices[bone_index], "Bone:", bone_index)
        #print("Original?:",x)
        #--------------------------------------------------------------------------

        
        submesh.vtx.append(v_mixed.to_3d().to_tuple()) #I think this is where submesh.vtx is updated
        if has_vnormal:
          submesh.vn.append(vn)
        if has_vcol:
          submesh.vcol.append(vcol)
        if has_uv:
          submesh.uv.append((uv[0], 1.0 - uv[1]))#Inverts the uv Y position 
        #Flag reverse solve rules: If the vertex first apperance is on the left side of tri then it is flag 0, if on right its flag 32, if in middle or only has one appearance 
        #it is -1
        if v > 1:#Only 2 uses of flag
          if flag == 0x00: #if flag == 0
            submesh.tri.append((v_start + v, v_start + v - 1, v_start + v - 2))
          elif flag == 0x20: #if flag == 32
            submesh.tri.append((v_start + v - 2, v_start + v - 1, v_start + v))
        #################################

      
      
      mesh_index += 1
      offs += (qwc + 1) * 0x10 # 16, skipps over the hex values 00000017000000000000000000000000 to the next dmatag

    #print(len(submesh.vtx)) #Shows the vertex count of the groups
    objects = []
    for texture_index, mesh in submesh_dict.items():
      mesh.update(skip_vertex_groups=self._skip_armature_creation)
      # Objects such as placeholders for particle effects may have UVs, but no
      # textures.
      if has_uv and texture_index < len(self.texture_names):
        material = self._mat_manager.get_material(self.texture_names[texture_index], has_vcol)
        mesh.mesh_obj.data.materials.append(material)
      objects.append(mesh.mesh_obj)

      bpy.context.scene.collection.objects.link(mesh.mesh_obj)

      mesh.update_normals()
      mesh.mesh_obj.select_set(state=True)

    return objects
