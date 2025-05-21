# pylint: disable=import-error
##################################################
bl_info = {
    "name":
        "Kingdom Hearts Re:Chain of Memories",
    "author":
        "Murugo",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "location":
        "File -> Import-Export",
    "description":
        "Import-Export Kingdom Hearts Re:Chain of Memories (PS2) models, Import models from KH Re:COM file formats.",
    "category":
        "Import-Export"
}

if "bpy" in locals():
  # pylint: disable=undefined-variable
  import importlib
  if "import_azf" in locals():
    importlib.reload(import_azf)# type: ignore
  if "import_gsd" in locals():
    importlib.reload(import_gsd)# type: ignore
  if "import_mdl" in locals():
    importlib.reload(import_mdl)# type: ignore


import os
import bpy
from bpy.props import (BoolProperty,StringProperty,EnumProperty)
from bpy_extras.io_utils import (ImportHelper, ExportHelper)
from bpy.types import Operator
##A Bunch of imports of the other files
##############################################








class ImportKhReComAzf(bpy.types.Operator, ImportHelper):
  """Load a Kingdom Hearts Re:Chain of Memories AZF file"""
  bl_idname = "import_khrecom.azf"
  bl_label = "Import Kingdom Hearts Re:COM (PS2) Stage (AZF)"
  bl_options = {'PRESET', 'UNDO'}

  filename_ext = ".azf"
  filter_glob: StringProperty(default="*.azf", options={'HIDDEN'})# type: ignore

  import_skybox: BoolProperty(
      name="Import Skybox",
      description="Import skybox objects and textures.",
      default=True,
  )# type: ignore

  ignore_placeholders: BoolProperty(
      name="Ignore Placeholders",
      description=
      "Skip importing placeholder meshes used to mark particle effects.",
      default=True,
  )# type: ignore

  use_vertex_color_materials: BoolProperty(
      name="Use Vertex Color in Materials",
      description=
      "Automatically connect baked vertex colors in Blender materials if present. If unchecked, vertex color layers will still be imported for objects.",
      default=True,
  )# type: ignore

  def execute(self, context):
    from . import import_azf

    keywords = self.as_keywords(ignore=("filter_glob",))
    status, msg = import_azf.load(context, **keywords)
    if msg:
      self.report({'ERROR'}, msg)
    return {status}

  def draw(self, context):
    pass


class AZF_PT_import_options(bpy.types.Panel):
  bl_space_type = 'FILE_BROWSER'
  bl_region_type = 'TOOL_PROPS'
  bl_label = "Import AZF"
  bl_parent_id = "FILE_PT_operator"

  @classmethod
  def poll(cls, context):
    sfile = context.space_data
    operator = sfile.active_operator

    return operator.bl_idname == "IMPORT_KHRECOM_OT_azf"

  def draw(self, context):
    layout = self.layout
    layout.use_property_split = True
    layout.use_property_decorate = False

    sfile = context.space_data
    operator = sfile.active_operator

    layout.prop(operator, 'import_skybox')
    layout.prop(operator, 'ignore_placeholders')
    layout.prop(operator, 'use_vertex_color_materials')


class ImportKhReComGsd(bpy.types.Operator, ImportHelper):
  """Load a Kingdom Hearts Re:Chain of Memories GSD file"""
  bl_idname = "import_khrecom.gsd"
  bl_label = "Import Kingdom Hearts Re:COM (PS2) Stage Gimmicks (GSD)"
  bl_options = {'PRESET', 'UNDO'}

  filename_ext = ".gsd"
  filter_glob: StringProperty(default="*.gsd", options={'HIDDEN'})# type: ignore

  import_shadow_model: BoolProperty(
      name="Import Shadow Models",
      description="Import models used for shadows.",
      default=False,
  )# type: ignore

  use_vertex_color_materials: BoolProperty(
      name="Use Vertex Color in Materials",
      description=
      "Automatically connect baked vertex colors in Blender materials if present. If unchecked, vertex color layers will still be imported for objects.",
      default=True,
  )# type: ignore

  def execute(self, context):
    from . import import_gsd

    keywords = self.as_keywords(ignore=("filter_glob",))
    status, msg = import_gsd.load(context, **keywords)
    if msg:
      self.report({'ERROR'}, msg)
    return {status}

  def draw(self, context):
    pass


class GSD_PT_import_options(bpy.types.Panel):
  bl_space_type = 'FILE_BROWSER'
  bl_region_type = 'TOOL_PROPS'
  bl_label = "Import GSD"
  bl_parent_id = "FILE_PT_operator"

  @classmethod
  def poll(cls, context):
    sfile = context.space_data
    operator = sfile.active_operator

    return operator.bl_idname == "IMPORT_KHRECOM_OT_gsd"

  def draw(self, context):
    layout = self.layout
    layout.use_property_split = True
    layout.use_property_decorate = False

    sfile = context.space_data
    operator = sfile.active_operator

    layout.prop(operator, 'import_shadow_model')
    layout.prop(operator, 'use_vertex_color_materials')















######################################################################################################
############
class ImportKhReComMdl(bpy.types.Operator, ImportHelper):
  """Load a Kingdom Hearts Re:Chain of Memories MDL file"""
  bl_idname = "import_khrecom.mdl"
  bl_label = "Import Kingdom Hearts Re:COM (PS2) Model (MDL)"
  bl_options = {'PRESET', 'UNDO'}

  filename_ext = ".mdl"
  filter_glob: StringProperty(default="*.mdl", options={'HIDDEN'})# type: ignore

  import_shadow_model: BoolProperty(
      name="Import Shadow Models",
      description="Import models used for shadows.",
      default=False,
  )# type: ignore

  use_vertex_color_materials: BoolProperty(
      name="Use Vertex Color in Materials",
      description=
      "Automatically connect baked vertex colors in Blender materials if present. If unchecked, vertex color layers will still be imported for objects.",
      default=True,
  )# type: ignore

  def execute(self, context):
    from . import import_mdl

    keywords = self.as_keywords(ignore=("filter_glob",))
    status, msg = import_mdl.load(context, **keywords)
    if msg:
      self.report({'ERROR'}, msg)
    return {status}

  def draw(self, context):
    pass
#################

#################
class MDL_PT_import_options(bpy.types.Panel):
  bl_space_type = 'FILE_BROWSER'
  bl_region_type = 'TOOL_PROPS'
  bl_label = "Import MDL"
  bl_parent_id = "FILE_PT_operator"

  @classmethod
  def poll(cls, context):
    sfile = context.space_data
    operator = sfile.active_operator

    return operator.bl_idname == "IMPORT_KHRECOM_OT_mdl"

  def draw(self, context):
    layout = self.layout
    layout.use_property_split = True
    layout.use_property_decorate = False

    sfile = context.space_data
    operator = sfile.active_operator

    layout.prop(operator, 'import_shadow_model')
    layout.prop(operator, 'use_vertex_color_materials')
#################

######################################################################################

from . import readutil
import binascii
import struct
import mathutils
import numpy as np
def write_mdl_data2(context, filepath, use_some_setting):
  
  #Step 1: Need to determine how many models are there, and which ones are shadow models
  #The models in blender are made in the order they are read in, so the model offsets at the begining of the file should be in the same order
  #Models that have multiple textures to them make seperate models, the textures are read from their texture table. The model in blender will have their model number, followed by their mat number
  #Using the same logic as in the parser script we can find the relevant offsets for the models

  #The offsets for model offs need to be updated to adjusted locations
  #If at model offset + 12 (The texture table count) it is 0, then it is a shadow model. The begining to the end of that model will be copied without change, need to determine exact start. Only change will be its model offset
  #At exactly model offset is bone count in 2 bytes, then ?? ??, then is bone_table_offs(Needs to be added to model offset)in 4 bytes, then transform_table_offs(Needs to be added to model offset) in 4 bytes. All of these will not change. After is the texture table offsets
  #After the model offset +12 is the texture tabel count, texture table offset(Needs to be added to model offset),vif_opaque_offs (Needs to be added to model offset),vif_translucent_offs (Needs to be added to model offset),then bone data. 
  #After the bone data i belive it starts with the first texture table names list, which is a list of strings of length 32 read a texture table count number of times
  #After that is the location of model off+ vif_opaque_offs , which lands directly on the first DMAtag

  #A VIF packet is consisted of a DmaTag (a calculation for offset to the next DMATag consisting of 1 byte QWC and 2 bytes 00 and one byte 10. Or if its the last DMATAG it will be 00 00 00 60), 
  #QWC can be found as ((V_count*48)/16) + 3 
  # STCYCL and UNPACK commands(Skipped in blender)(Needed in game) [00 00 00 00 04 04 00 01 00 80 ?? ?? ?? 00 00 00] it seems the 3 ?? can be made 0 without issue , then a vertex tabel consisting of [vertex_table_count, _, vertex_count, (Value unique to model), mode][5 int16, Vertex table count, 01 00, Vertex count, ??, mode]. 
    # The entire begining part of the packet is from DMATag to the end of the vertex tabel variables(and at the end of a vertex table are the bytes 00 9C XX 80 00 00 00 40 3E 30 12 04 00 00 00 00 00 00 Where XX is the vertex count) is 48 bytes
  
    #Finally the rest of the packet is vertex data, starting imediatley after at offset modelOffs + vif_opaque/transparent_offs +48
    #Vertecies start and end imediatley after one another
    '''
    A mdl vertex is 48 bytes
    Offset start
    Bytes 1-2: Flag int, it is checked if the value is either 0 or 32. Other values seen include -1. This is the face orientation of the triangle formed. 0 and 32 switches it, -1 is for no triangle. 
    Bytes 3-4 are skipped
    Bytes 5-8 vtx_weight float
    Bytes 9-12 00 00 00 00
    Bytes 13-16 ?? No clue but 00ing it does not change anything Values seen are for normal  00 20 00 00 and for -1 flags 00A00000
    Bytes 17-20 X position float
    Bytes 21-24 Y position float
    Bytes 25-28 Z position float
    Bytes 29-30 Parent bone int X 4 (No clue why)
    Bytes 31-32 Parent bone int
    Bytes 33-36 UV X float
    Bytes 37-40 UV Y float
    Bytes 41-44 Float 1
    Bytes 45-46 Texture index int16
    Bytes 47-48

    '''
    #After the last vertex in a table add values 00 00 00 17 00 00 00 00 00 00 00 00 00 00 00 00 before next DMAtag
    # The data between the last DMATag 1610612736 and the new one is 12 bytes, 00 00 00 00 00 00 00 00 00 00 00 00. After will 60 if its the end of the model, or a new DMATAG for the transparent model
    #If its before a new model then everything from that point till the next model offset should be coppied


  #When the importer is parsing VIF packets it checks to see if the texture index of the current packet is in the submesh, if it is then the packet is assigned to an existing submesh, if not it makes a new submesh for those vertecies and all that come after.
  #The order in blender may not be accurate as the transparent texture model may show up before the second texture submesh
  #In general, there will be a ending for models, transparent models, and shadow models

  #Things that will need updating:
    '''''
    Model offsets for each model in the mdl file, read at the begining of the file
    Bone and texture data should stay the same so that shouldnt need changing
    vif_translucent_offs, since opaque size will be different any new translucent offs will need to be recalculated. 
    '''''


  #-------------------Pseudo code

    #Open old and new mdl files
    mdl_dirname = os.path.dirname(filepath)
    mdl_basename = os.path.splitext(os.path.basename(filepath))[0]
    
    NEWfilepath = mdl_dirname + '\\'+ mdl_basename + 'NEW.mdl'
    Oldmdl = readutil.BinaryFileReader(filepath)
    Newmdl = open(NEWfilepath, 'wb')

    #Read Uint32 at begining of oldmdl until reads 00s and store all the mdl offsets found into oldOffsetList list
    oldOffsetList = []
    mainModelCount = 0
    for i in range(0x100):#reads the beginign of file for every model offset. Stops when it reads 00000000 in uint32
      
      Oldmdl.seek(i * 4)
      
      model_offs = Oldmdl.read_uint32() #Determines the model offest for all the parsing
      if not model_offs:
        break    
      oldOffsetList.append(model_offs)
      #Get a count of how many models there should be. For the models in blender this should be the first _# after the basename, transparent textures will be grouped with their respective model, shadows are by their selves
      mainModelCount +=1 
        
      
      print("Model offset read offset:", Oldmdl.tell()-4)
      print("Model offset", model_offs)




    #Make a empty list called newOffsetList. This list will be appended in the writing loop
    newOffsetList = []

    #Copy everything from byte 0 to the first model offset read at 0. We will come back and edit the offsets later
    i = 0
    Oldmdl.seek(0)    
    model_offs = Oldmdl.read_uint32()    
    while i < model_offs: #Copies all the data before the first model offset
      Oldmdl.seek(i)      
      Newmdl.write(struct.pack('<h', Oldmdl.read_int16()))#< for little endian ! for big endian
      i+= 2


    oldReturnOffset=0
    newReturnOffset=0
    #For i=0<oldOffsetList.length (one big write loop for each model)
    for i in range (len(oldOffsetList)):
      
      #newOffsetlist append current offset
      newOffsetList.append(Newmdl.tell())
      #If at model offset + 12 (The texture table count) it is 0, copy everything from old mdl to new mdl from current offset to the next mdl offset because this is a shadow mdl  
      oldReturnOffset = Oldmdl.tell()
      Oldmdl.seek(oldOffsetList[i]+12)      
      texture_table_count = Oldmdl.read_uint32() 
      Oldmdl.seek(oldReturnOffset)
      
      

      if texture_table_count ==0:
        if i == len(oldOffsetList)-1:#If last model is a shadow model
          print("Shadow model last,copying the rest of the file ")
          LoopOffset = Oldmdl.tell()          
          while LoopOffset < Oldmdl.filesize:
            Oldmdl.seek(LoopOffset)      
            Newmdl.write(struct.pack('<h', Oldmdl.read_int16()))#< for little endian ! for big endian
            LoopOffset+= 2  
        else:
          print("Shadow model,copying and skipping to next model offset: ",oldOffsetList[i+1])
          shadowLoopOffset = Oldmdl.tell()
          while shadowLoopOffset < oldOffsetList[i+1]:
            Oldmdl.seek(shadowLoopOffset)      
            Newmdl.write(struct.pack('<h', Oldmdl.read_int16()))#< for little endian ! for big endian
            shadowLoopOffset+= 2
      #Else(Here we start parsing code)
      else:
        
        #Copy the next 12 bytes from old mdl to new mdl as this is bone data
        oldReturnOffset = Oldmdl.tell()
        bone_count = Oldmdl.read_uint16()
        Oldmdl.seek(oldReturnOffset)
        Newmdl.write(struct.pack('<I', Oldmdl.read_uint32())) #Bone count
        bone_table_offs = Oldmdl.read_uint32()
        Newmdl.write(struct.pack('<I', bone_table_offs))
        transform_table_offs = Oldmdl.read_uint32()
        Newmdl.write(struct.pack('<I', transform_table_offs))
        
        #Copy the texture table count,texture table offset,and vif_opaque_offs from old to new, all uint 32. these offsets are just added to model offset and dont need to change
        Newmdl.write(struct.pack('<I', Oldmdl.read_uint32()))
        Newmdl.write(struct.pack('<I', Oldmdl.read_uint32()))
        vif_opaque_offs = Oldmdl.read_uint32()
        Newmdl.write(struct.pack('<I', vif_opaque_offs))
    
        #Set bool hastransparent to false
        hastransparent = False
        #Set int vif_translucent_offs_off to current offset in new
        vif_translucent_offs_off = Newmdl.tell()

        #If vif_translucent_offs in oldmdl is != 0 
        oldReturnOffset = Oldmdl.tell()
        vif_translucent_offs = Oldmdl.read_uint32() 
        Oldmdl.seek(oldReturnOffset)
        if vif_translucent_offs !=0:            
          # Set bool hastransparent to true
          hastransparent =True
    
        #Copy vif_translucent_offs from old to new for now, we have the bool saying if we need to update it later
        Newmdl.write(struct.pack('<I', Oldmdl.read_uint32()))
    
        #Copy everything from here to model off+ vif_opaque_offs, the first VIF packet, from old to new
        LoopOffset = Oldmdl.tell()
        #print("Before copy:", Newmdl.tell())
        #print("Model offset:", oldOffsetList[i])
        while LoopOffset < oldOffsetList[i]+vif_opaque_offs:
          Oldmdl.seek(LoopOffset)      
          Newmdl.write(struct.pack('<h', Oldmdl.read_int16()))#< for little endian ! for big endian
          LoopOffset+= 2
        #print("After copy:", Newmdl.tell())

        #Make a list of bone names in blender called boneList
        bone_names = []        
        for armature in [ob for ob in bpy.data.objects if ob.type == 'ARMATURE']:
          for bone in armature.data.bones:           
            bone_names.append(bone.name)

        
        
        #Retreive a list of bone matracies from oldmdl (Since a model will use the same bones for all of it we only need the first copy). The matracies can be found at transform_table_offs
        boneMatrix = []
        oldReturnOffset = Oldmdl.tell()     
        
        for boneloopnumber in range(bone_count):
          Oldmdl.seek(bone_table_offs +oldOffsetList[i] + boneloopnumber * 0x14)
          bone_name = Oldmdl.read_string(0x10)
          parent_index = Oldmdl.read_int16()
          Oldmdl.seek(transform_table_offs+ oldOffsetList[i] + boneloopnumber * 0x40)
          local_matrix = mathutils.Matrix([Oldmdl.read_nfloat32(4) for _ in range(4)]) 
          local_matrix.transpose()         

          if parent_index >= 0:
            global_matrix = boneMatrix[parent_index] @ local_matrix
          else:
            global_matrix = local_matrix

                    
          boneMatrix.append(global_matrix)
          #print("Bone #", boneloopnumber, local_matrix)
        Oldmdl.seek(oldReturnOffset)
        #count = 0
        #for rix in boneMatrix:
          #print("Bone #", count, rix)
          #count +=1
        

        #Find vertex table model unique value
        
        Oldmdl.seek((oldOffsetList[i] + vif_opaque_offs)+16+6)
        uniqueValue = Oldmdl.read_int16()
        #Now, we need to find the models that correspond to our loop variable i, and are not transparent, and pull their mesh info.
        #Assuming that a model can only have 1 texture in it be transparent

        #Set list models to corresponding models to i WITH _t at end as transModel
        transModel = []
        transModelNames = []
        #Set list models to corresponding models to i without _t at end as submodelslist
        submodelslist = []
        submodelslistNames = []

        lastAddModelNameCorrection =0
        for obj in bpy.data.objects:
          print(obj.name) 
          last_chars = obj.name[-4:]
          if obj.name + '_mesh_data' in bpy.data.meshes:
            
            if "_"+str(i) in obj.name:
                
              if '_t' in obj.name:
                transModel.append(obj.data)
                transModelNames.append(obj.name)
              else:                  
                           
                
                submodelslist.append(obj.data)
                submodelslistNames.append(obj.name)
          #Merge the loose subobjects into their main one          
          
          if obj.name[:-4] + '_mesh_data' +last_chars in bpy.data.meshes:
              
              if "_"+str(i) in obj.name:             
                bpy.ops.object.select_all(action='DESELECT')   
                lastAddModelNameCorrection = len(submodelslistNames)-1
                
                bpy.data.objects[obj.name].select_set(True)  
                bpy.data.objects[submodelslistNames[lastAddModelNameCorrection]].select_set(True)
                bpy.context.view_layer.objects.active = bpy.data.objects[submodelslistNames[lastAddModelNameCorrection]]
                bpy.ops.object.join()   
                bpy.context.active_object.name = submodelslistNames[lastAddModelNameCorrection]
                submodelslist[lastAddModelNameCorrection] = bpy.context.active_object.data
                bpy.ops.object.select_all(action='DESELECT')
              
              
                         
        
        #need to combine the sub meshes into one big mesh
        #the flag order of a single lone triangle is 0 -1 -1 Highest ver to smallest
        #Try getting a int extra vertex count of the extra mesh

        
        #for each model in submodelslist (Its here we are gonna write the VIF packets for opauqe)
        submodelslistloop = 0
        for model in submodelslist:
          submodelslistloop +=1
          
          
          #Get vertex count
          vertex_count = 0
          subModelVertexList = []
          for vertexies in model.vertices:
            vertex_count +=1
            subModelVertexList.append(vertexies)
          #print(vertex_count)
          UVList =[mathutils.Vector((0, 0))]*vertex_count  #To store the UVs without having to search 
          print("UVLIST: ", len(UVList))



          triangleList = []

          
          
          normalvert = True
          addedVertTriOffset =-1
          largestVertOffset= -1
          FlagaddedVertTriOffset =-1
          FlaglargestVertOffset= -1
          for fa, face in enumerate(model.polygons):
                
              triangleList.append(face.vertices[:])               
              
              print("mesh[{fa}].SetTriangle {v_i};".format(fa=fa, v_i=triangleList[fa]))
              for ver in face.vertices[:]:
                
                if ver == face.vertices[:][0]:
                  

                  if abs(ver - face.vertices[:][1]) >2 or abs(ver - face.vertices[:][2]) >2 or use_some_setting == True: #if vert 1 and 2 are within 2 range of 0 then its a normal vert and should be ordered lowest to heighest
                    normalvert = False

                if normalvert == True and ver >largestVertOffset:
                  largestVertOffset = ver +1
                  FlaglargestVertOffset = ver +1
              
                if addedVertTriOffset == -1  and normalvert == False: #As the for loop continues triangle list is getting larger, as soon as a non normal triangle is spotted addedVertTriOffset is set                  
                    addedVertTriOffset = len(triangleList)-1
                    FlagaddedVertTriOffset = len(triangleList)-1


                    
          
                        

          #for all the non normal verts, reorder them
          print("AddedVertTriOffset (First edited triangle)", addedVertTriOffset)
          print("LargestVertOffset (First edited vertex)",largestVertOffset)
          #For every non normal triangle, order it into a new form of largestVertOffset+2 largestVertOffset+1 largestVertOffset, copying the vertecies data from 
          #the original tri to the new tris and swap them, swaping the verts in the triangle list too

          print("Generating Uv List...") 
          vertLoopDict = {} #structure vertexID : loopID, lets uvs find the correct vert it needs. Need the blender loop the vertex is in.
          for face in model.polygons:
            for vert_idx, loop_idx in zip(face.vertices, face.loop_indices):
              uv_coords = model.uv_layers.active.data[loop_idx].uv
                    
              UVList[vert_idx]= uv_coords 
              vertLoopDict [vert_idx] = loop_idx

          
          vertex_Dict = {} #structure vertexID : [tri#, position in tri]
          for index, tri in enumerate(triangleList):
                for tri_index, tri_vert in enumerate(tri):   
                  vertex_Dict[tri_vert] = [index, tri_index] 

          if addedVertTriOffset > -1 :
            if largestVertOffset == -1:
              largestVertOffset = 0
            while addedVertTriOffset < len(triangleList):
                  original_tri = list(triangleList[addedVertTriOffset])              
                  #print("Original triangle",triangleList[addedVertTriOffset], "Tri ",addedVertTriOffset )
                  #Each original tri vert needs to be set after the search for the last one incase they are changed in the previous search 
              
                  
              
                  orgi_triVert1 = list(triangleList[addedVertTriOffset])[0]
                  replacementTri = vertex_Dict[largestVertOffset+2][0]
                  replacementTriVertIndex = vertex_Dict[largestVertOffset+2][1]
                  tri_vert = largestVertOffset+2
                               
                  if tri_vert == largestVertOffset+2:

                    originalLoop = -1
                    foundLoop = -1
                    orgi_uv_coordsX = -1
                    orgi_uv_coordsY = -1
                    originalLoop = vertLoopDict.get(orgi_triVert1)  
                    foundLoop = vertLoopDict.get(tri_vert)     
                    if originalLoop != foundLoop:                   
                      orgi_uv_coordsX = model.uv_layers.active.data[originalLoop].uv.x
                      orgi_uv_coordsY = model.uv_layers.active.data[originalLoop].uv.y
                      found_uv_coords =model.uv_layers.active.data[foundLoop].uv
                      model.uv_layers.active.data[originalLoop].uv = found_uv_coords                    
                            
                      model.uv_layers.active.data[foundLoop].uv.x = orgi_uv_coordsX
                      model.uv_layers.active.data[foundLoop].uv.y = orgi_uv_coordsY 
                      
                      UVList[tri_vert] = model.uv_layers.active.data[foundLoop].uv
                      
                      
                    
                    if replacementTri ==  addedVertTriOffset: #already on same triangle 
                      if replacementTriVertIndex == 0:
                        print("Vert 0 already in correct tirangle and correct position")
                      else:
                        print("Vert 0 already in correct tirangle but incorrect position")  
                        temp_triVert = list(triangleList[addedVertTriOffset])[0] 
                        temp_listVert = subModelVertexList[temp_triVert]
                        subModelVertexList[temp_triVert] = subModelVertexList[largestVertOffset+2] #copy the vertex data from found vertex to original
                        subModelVertexList[largestVertOffset+2] = temp_listVert
                        original_tri[0] = original_tri[replacementTriVertIndex]
                        original_tri[replacementTriVertIndex] = temp_triVert
                        

                    else:#Not on the same triangle
                      tempVert1 = subModelVertexList[orgi_triVert1] #Vertex data of original tri vert 1
                      subModelVertexList[orgi_triVert1] = subModelVertexList[largestVertOffset+2] #copy the vertex data from found vertex to original
                      subModelVertexList[largestVertOffset+2] = tempVert1 #copy the vertex data from original to found vertex
                      temp_tri1 = list(triangleList[replacementTri]) #Triangle of found triangle
                      temp_tri1[replacementTriVertIndex] = original_tri[0]#Copy the original vert int to where the repalcement was found 
                      original_tri[0] = largestVertOffset+2 #Write the new vert to original tri
                      new_tri1 = tuple(temp_tri1)
                      triangleList[replacementTri] = new_tri1 #Overwrite the found tri with temp one

                    #Swap the values in dictionary
                    vertex_Dict[orgi_triVert1], vertex_Dict[largestVertOffset+2] = vertex_Dict[largestVertOffset+2], vertex_Dict[orgi_triVert1]

                    new_new_tri = tuple(original_tri)
                    triangleList[addedVertTriOffset] = new_new_tri 
                  #
                  orgi_triVert2 = list(triangleList[addedVertTriOffset])[1]
                  replacementTri = vertex_Dict[largestVertOffset+1][0]
                  replacementTriVertIndex = vertex_Dict[largestVertOffset+1][1]
                  tri_vert = largestVertOffset+1 
                  if tri_vert == largestVertOffset+1:
                    originalLoop = -1
                    foundLoop = -1
                    orgi_uv_coordsX = -1
                    orgi_uv_coordsY = -1
                    originalLoop = vertLoopDict.get(orgi_triVert2)  
                    foundLoop = vertLoopDict.get(tri_vert)   
                    if originalLoop != foundLoop:                   
                      orgi_uv_coordsX = model.uv_layers.active.data[originalLoop].uv.x
                      orgi_uv_coordsY = model.uv_layers.active.data[originalLoop].uv.y
                      found_uv_coords =model.uv_layers.active.data[foundLoop].uv
                      model.uv_layers.active.data[originalLoop].uv = found_uv_coords                    
                            
                      model.uv_layers.active.data[foundLoop].uv.x = orgi_uv_coordsX
                      model.uv_layers.active.data[foundLoop].uv.y = orgi_uv_coordsY 
                      UVList[tri_vert] = model.uv_layers.active.data[foundLoop].uv
                      
                    if replacementTri ==  addedVertTriOffset: #already on same triangle 
                      if replacementTriVertIndex == 1:
                        print("Vert 1 already in correct tirangle and correct position")
                      else:
                        print("Vert 1 already in correct tirangle but incorrect position")  
                        temp_triVert = list(triangleList[addedVertTriOffset])[1] 
                        temp_listVert = subModelVertexList[temp_triVert]
                        subModelVertexList[temp_triVert] = subModelVertexList[largestVertOffset+1] #copy the vertex data from found vertex to original
                        subModelVertexList[largestVertOffset+1] = temp_listVert
                        original_tri[1] = original_tri[replacementTriVertIndex]
                        original_tri[replacementTriVertIndex] = temp_triVert
                    else:
                      tempVert2 = subModelVertexList[orgi_triVert2] #Vertex data of original tri vert 2
                      subModelVertexList[orgi_triVert2] = subModelVertexList[largestVertOffset+1] #copy the vertex data from found vertex to original
                      subModelVertexList[largestVertOffset+1] = tempVert2 #copy the vertex data from original to found vertex
                      temp_tri2 = list(triangleList[replacementTri]) #Triangle of found triangle
                      temp_tri2[replacementTriVertIndex] = original_tri[1]#Copy the original vert int to where the repalcement was found 
                      original_tri[1] = largestVertOffset+1 #Write the new vert to original tri
                      new_tri2 = tuple(temp_tri2)
                      triangleList[replacementTri] = new_tri2 #Overwrite the found tri with temp one
                    #Swap the values in dictionary
                    vertex_Dict[orgi_triVert2], vertex_Dict[largestVertOffset+1] = vertex_Dict[largestVertOffset+1], vertex_Dict[orgi_triVert2]
                    new_new_tri = tuple(original_tri)
                    triangleList[addedVertTriOffset] = new_new_tri 
                  #
                  orgi_triVert3 = list(triangleList[addedVertTriOffset])[2]
                  replacementTri = vertex_Dict[largestVertOffset][0]
                  replacementTriVertIndex = vertex_Dict[largestVertOffset][1]
                  tri_vert = largestVertOffset
                  if tri_vert == largestVertOffset:
                    originalLoop = -1
                    foundLoop = -1
                    orgi_uv_coordsX = -1
                    orgi_uv_coordsY = -1
                    originalLoop = vertLoopDict.get(orgi_triVert3)  
                    foundLoop = vertLoopDict.get(tri_vert)   
                    if originalLoop != foundLoop:                   
                      orgi_uv_coordsX = model.uv_layers.active.data[originalLoop].uv.x
                      orgi_uv_coordsY = model.uv_layers.active.data[originalLoop].uv.y
                      found_uv_coords =model.uv_layers.active.data[foundLoop].uv
                      model.uv_layers.active.data[originalLoop].uv = found_uv_coords                    
                            
                      model.uv_layers.active.data[foundLoop].uv.x = orgi_uv_coordsX
                      model.uv_layers.active.data[foundLoop].uv.y = orgi_uv_coordsY 
                      UVList[tri_vert] = model.uv_layers.active.data[foundLoop].uv
                      
                    if replacementTri ==  addedVertTriOffset: #already on same triangle 
                      if replacementTriVertIndex == 2:
                        print("Vert 2 already in correct tirangle and correct position")
                      else:
                        print("Vert 2 already in correct tirangle but incorrect position")  
                        temp_triVert = list(triangleList[addedVertTriOffset])[2] 
                        temp_listVert = subModelVertexList[temp_triVert]
                        subModelVertexList[temp_triVert] = subModelVertexList[largestVertOffset] #copy the vertex data from found vertex to original
                        subModelVertexList[largestVertOffset] = temp_listVert
                        original_tri[2] = original_tri[replacementTriVertIndex]
                        original_tri[replacementTriVertIndex] = temp_triVert
                    else:
                      tempVert3 = subModelVertexList[orgi_triVert3] #Vertex data of original tri vert 3
                      subModelVertexList[orgi_triVert3] = subModelVertexList[largestVertOffset] #copy the vertex data from found vertex to original
                      subModelVertexList[largestVertOffset] = tempVert3 #copy the vertex data from original to found vertex
                      temp_tri3 = list(triangleList[replacementTri]) #Triangle of found triangle
                      temp_tri3[replacementTriVertIndex] = original_tri[2]#Copy the original vert int to where the repalcement was found 
                      original_tri[2] = largestVertOffset #Write the new vert to original tri
                      new_tri3 = tuple(temp_tri3)
                      triangleList[replacementTri] = new_tri3 #Overwrite the found tri with temp one
                    #Swap the values in dictionary
                    vertex_Dict[orgi_triVert3], vertex_Dict[largestVertOffset] = vertex_Dict[largestVertOffset], vertex_Dict[orgi_triVert3]
                    new_new_tri = tuple(original_tri)
                    triangleList[addedVertTriOffset] = new_new_tri 


                  largestVertOffset+=3
                  new_new_tri = tuple(original_tri)
                  triangleList[addedVertTriOffset] = new_new_tri
                  print(submodelslistNames[submodelslistloop-1], "   New triangle",triangleList[addedVertTriOffset], "Tri ",addedVertTriOffset," /", len(triangleList) )
                  addedVertTriOffset+=1

          print("Generating flag list for each vertex..." )
          flagList =[] #To store the flags of a dmatag without having to search      
          flagvert = 0
          if(FlagaddedVertTriOffset == -1):
            FlagaddedVertTriOffset = len(triangleList)
           
          while flagvert < FlaglargestVertOffset:  
              if(flagvert%100 == 0 ):  
                print(submodelslistNames[submodelslistloop-1], "Vert Flag: ",  flagvert, " / ", vertex_count ) 

              flag = -1
              vertInNextTri = False
              sawAFellowVert = False
              #make triangle loop = to the tri# of a flagvert in vertDictionary vertex_Dict[flagvert][0]
              triangleLoop = 0

              
              while triangleLoop < FlagaddedVertTriOffset:
                    
                    if triangleLoop+1 == FlagaddedVertTriOffset:                    
                      if vertInNextTri == False: 
                        if sawAFellowVert == True:               
                          flag = -1
                          
                      if flagvert == vertex_count-1:
                        flag = 32
                    elif flagvert == triangleList[triangleLoop][0]:
                      for nextTriVerts in triangleList[triangleLoop+1]:
                        if flagvert == nextTriVerts:                                                 
                            vertInNextTri = True

                      if vertInNextTri == True:                                            
                        flag = 0  
                      else:                      
                        for currenttris in triangleList[triangleLoop]:
                          for nexttris in triangleList[triangleLoop+1]:
                            if currenttris == nexttris:                            
                              sawAFellowVert = True
                        
                        if sawAFellowVert == False:                        
                          flag = 0 
                    elif flagvert == triangleList[triangleLoop][1]: 
                      for nextTriVerts in triangleList[triangleLoop+1]:
                        if flagvert == nextTriVerts:                          
                          vertInNextTri = True
                      if vertInNextTri == True:
                        flag = -1  
                    
                    elif flagvert == triangleList[triangleLoop][2]:
                      for nextTriVerts in triangleList[triangleLoop+1]:
                          if flagvert == nextTriVerts:                          
                            vertInNextTri = True

                      if vertInNextTri == True:
                        flag = 32 
                      else:                     
                        
                        for currenttris in triangleList[triangleLoop]:
                          for nexttris in triangleList[triangleLoop+1]:
                            if currenttris == nexttris:                            
                              sawAFellowVert = True
                        if sawAFellowVert == False:
                          
                          if triangleList[triangleLoop][2]< triangleList[triangleLoop][1]:
                            if triangleList[triangleLoop][2]< triangleList[triangleLoop][0]:
                              flag = -1
                          else:
                            flag = 32 
                          
                    
                    
                    triangleLoop +=1                  
                    if vertInNextTri == True:
                      triangleLoop = FlagaddedVertTriOffset
              flagList.append(flag)
              flagvert+=1

          while flagvert < vertex_count:  
              if(flagvert%100 == 0 ):  
                print(submodelslistNames[submodelslistloop-1], "Vert Flag: ",  flagvert, " / ", vertex_count ) 

              flag = -1
              vertInNextTri = False
              sawAFellowVert = False
              #make triangle loop = to the tri# of a flagvert in vertDictionary vertex_Dict[flagvert][0]
              triangleLoop = vertex_Dict[flagvert][0]

                  
              if triangleLoop+1 == len(triangleList):                    
                      if vertInNextTri == False: 
                        if sawAFellowVert == True:               
                          flag = -1
                          
                      if flagvert == vertex_count-1:
                        flag = 32
              elif flagvert == triangleList[triangleLoop][0]:
                      for nextTriVerts in triangleList[triangleLoop+1]:
                        if flagvert == nextTriVerts:                                                 
                            vertInNextTri = True

                      if vertInNextTri == True:                                            
                        flag = 0  
                      else:                      
                        for currenttris in triangleList[triangleLoop]:
                          for nexttris in triangleList[triangleLoop+1]:
                            if currenttris == nexttris:                            
                              sawAFellowVert = True
                        
                        if sawAFellowVert == False:                        
                          flag = 0 
              elif flagvert == triangleList[triangleLoop][1]: 
                      for nextTriVerts in triangleList[triangleLoop+1]:
                        if flagvert == nextTriVerts:                          
                          vertInNextTri = True
                      if vertInNextTri == True:
                        flag = -1  
                    
              elif flagvert == triangleList[triangleLoop][2]:
                      for nextTriVerts in triangleList[triangleLoop+1]:
                          if flagvert == nextTriVerts:                          
                            vertInNextTri = True

                      if vertInNextTri == True:
                        flag = 32 
                      else:                     
                        
                        for currenttris in triangleList[triangleLoop]:
                          for nexttris in triangleList[triangleLoop+1]:
                            if currenttris == nexttris:                            
                              sawAFellowVert = True
                        if sawAFellowVert == False:
                          
                          if triangleList[triangleLoop][2]< triangleList[triangleLoop][1]:
                            if triangleList[triangleLoop][2]< triangleList[triangleLoop][0]:
                              flag = -1
                          else:
                            flag = 32 
                          
                    
                    
                    
              flagList.append(flag)
              flagvert+=1
              
               
            
            
            
            
                
          

          #Int vertecies processed = 0
          vertecies_processed = 0
          #bool lastVIF = false
          lastVIF = False
          #While vertecies processed < vertex count (Until all the vertecies in the model are processed)
          print("Generating dmaTags (Groups of vertexies and their data)" )
          while vertecies_processed < vertex_count:
            #int vertexset = 0
            vertexset = 0
            #if vertexcount - vertecies processed > 74
            if vertex_count - vertecies_processed > 74:
              #vertexset = 74
              vertexset = 74
            #else
            else:
              #vertexset = vertexcount - vertecies processed  (If at the end of the list of vertecies to process)
              vertexset = vertex_count - vertecies_processed
              #if last submodel in submodel list
              if submodelslistloop == len(submodelslist):
                  #lastVIF = true
                  lastVIF = True
            if lastVIF == False:
              #Check here to see if the next dmatag will start with 2 -1 flags and if not add or subtract to vertexset as needed
              if vertecies_processed+vertexset+1 < len(flagList):                
                  
                if flagList[vertecies_processed+vertexset] == -1 and flagList[vertecies_processed+vertexset+1] == -1:                
                    print("all good, ", vertecies_processed, "/ ", vertex_count," processed")                    
                else:
                  while flagList[vertecies_processed+vertexset] != -1 and vertexset > 0 or flagList[vertecies_processed+vertexset+1] != -1 and vertexset > 0:
                    vertexset-=1
                  if vertexset <= 0 and flagList[vertecies_processed+vertexset] != -1 or vertexset <= 0 and flagList[vertecies_processed+vertexset+1] != -1 :
                    while flagList[vertecies_processed+vertexset] != -1  or flagList[vertecies_processed+vertexset+1] != -1 :
                      vertexset+=1
                  print("fixed, new vertex count:", vertexset," ",  vertecies_processed, "/ ", vertex_count, "processed")  
                
                

                  
      
            #Wrtie a DmaTag to new
            #The first byte will be ((vertexset*48)/16) + 3 , then 00 00 10
            DmaTagHead = int(((vertexset*48)/16) + 3)
            #print(DmaTagHead)
            Newmdl.write(struct.pack('<B', DmaTagHead) +bytes.fromhex('000010'))

            #Wrtie STCYCL and UNPACK commands(Skipped in blender)(Needed in game) [00 00 00 00 04 04 00 01 00 80 ?? ?? ?? 00 00 00] it seems the 3 ?? can be made 0 without issue to new C86CC8
            Newmdl.write(bytes.fromhex('00000000040400010080C86CC8000000'))
            #Wrtie vertex table count as vertexset to new as int16
            Newmdl.write(struct.pack('<h', vertexset))
            #Write 01 00 to new mdl
            Newmdl.write(bytes.fromhex('0100'))
            #Write vertex count as vertexset to new as int 16
            Newmdl.write(struct.pack('<h', vertexset))
            # int unique value = Goto old mdl model off+ vif_opaque_offs + 16 to skip the unpack commands, + 6 to skip the begining of the vertex table to get to the unique value read as a int16
            Newmdl.write(struct.pack('<h', uniqueValue))

            #Write mode as 06 00 to new. Shadow modles use mode 16 but since they are getting copied as is we can assume mode 6 for custom models
            Newmdl.write(bytes.fromhex('0600'))
            #Write 00 9C XX 80 00 00 00 40 3E 30 12 04 00 00 00 00 00 00 to new where XX is vertexset as hex (struct.pack('<B', vertexset))
            Newmdl.write(bytes.fromhex('009C')+ struct.pack('<B', vertexset) +bytes.fromhex('80000000403E301204000000000000'))

            #For i < vertexset (each vertex in table)
            vert = 0
            while vert < vertexset:
              
              #print("Vert:", vert + vertecies_processed, "Start offset:" , Newmdl.tell())
              #Get face orientation of vertex
              #Write flag to new to bytes 1 and 2. 
              #Need to pull the vertex triangle data
              
              
              #print("Vertex ", vert+vertecies_processed, "flag ", flagList[vert+vertecies_processed])
              Newmdl.write(struct.pack('<h', flagList[vert+vertecies_processed]))
              
              #Write 00 00 to bytes 3 and 4
              Newmdl.write(bytes.fromhex('0000'))
              #Get vertex weight for current vertex bone group
              #Write vertex weigh(should just be 1 so try just that first) to bytes 5-8 as a float
              Newmdl.write(struct.pack('<f', 1))
             
              #Write 00 00 to bytes 9-12
              Newmdl.write(bytes.fromhex('00000000'))
              #For bytes 13 - 16 i am not sure what it is for, 0ing it dosent seem to change anything but the normal values seen are seen are 00200000 for normal vertex and 00A00000 for -1 flags
              
              Newmdl.write(bytes.fromhex('00200000'))
              #For bytes 17-20 calculate the mdl x position from the bone matrix, using the bone name the vertex is attached to find a index in the bone name list and then
              #it should be the same index in the oldmdl bone matracies list
              #print(subModelVertexList[vert+vertecies_processed].groups)
              
              ob = bpy.data.objects[submodelslistNames[submodelslistloop-1]]
              boneIndex = -1 #This will be the index to the parent bone in the mdl
              groupName= ""
              vertexToUse =mathutils.Vector((0, 0, 0))
              vertexToUse = subModelVertexList[vertecies_processed+vert]
              for ran in range(0, len(ob.vertex_groups)): #For every vertex group in the submodel model
                group = ob.vertex_groups[ran]
                for g in subModelVertexList[vertecies_processed+vert].groups:
                  if ran == g.group:                   
                    groupName = group.name
                    
                    #print("Vert", vertecies_processed+vert, model.vertices[vertecies_processed+vert].co, "Group:" , group.name)
              
              v_mixed = mathutils.Vector((vertexToUse.co.x, vertexToUse.co.y,vertexToUse.co.z, 1))              
              #print("updated vertex:", v_mixed)
              for boneloop in range(0, len(bone_names)):
                if groupName == bone_names[boneloop]:
                  boneIndex = boneloop
                  
              #print("Matrix:", boneMatrix[boneIndex], "Bone:", boneIndex)
              x = np.dot(np.linalg.inv(boneMatrix[boneIndex]), v_mixed) 
              #np.linalg.inv(A)  is simply the inverse of A, np.dot is the dot product

              #print("Vert", vertecies_processed+vert,"Original?:",x)
              
              
              Newmdl.write(struct.pack('<f', x[0]))
              

              #For bytes 21-24 calculate mdl y position
              Newmdl.write(struct.pack('<f', x[1]))
              #For bytes 25-28 calculate mdl z position
              Newmdl.write(struct.pack('<f', x[2]))
              
              #For bytes 29-30 write the bone index *4
              #print(boneIndex)
              Newmdl.write(struct.pack('<h', boneIndex*4))
              #For bytes 31-32 write the bone index
              Newmdl.write(struct.pack('<h', boneIndex))
              
              my_uv =UVList[vertecies_processed+vert] 
                
              UVx = my_uv.x
              Newmdl.write(struct.pack('<f', UVx))
              #For bytes 37-40 write UV y to new
              UVy =1 - my_uv.y
              Newmdl.write(struct.pack('<f', UVy))
              #For bytes 41-44 write float 1
              Newmdl.write(struct.pack('<f', 1))
              #For bytes 45-46 write the texture index float to new              
              Newmdl.write(struct.pack('<H', submodelslistloop-1))
              #Bytes 47-48
              Newmdl.write(bytes.fromhex('0000'))
              #Temp empty vertex data
              #Newmdl.write(bytes.fromhex('00000000000000000000000000000000'))
              #Newmdl.write(bytes.fromhex(''))
              vert +=1

            #After writing all the vertecies in the table:
            #Write 00 00 00 17 00 00 00 00 00 00 00 00 00 00 00 00 before next DMAtag
            Newmdl.write(bytes.fromhex('00000017000000000000000000000000'))
            vertecies_processed +=vertexset
            #print("Vertecies processed:",vertecies_processed, " out of ", vertex_count  )
            
          #print(lastVIF)
          #If lastVIF
          if lastVIF:
            #DmaTag = 1610612736
            #write DMATag to new
            Newmdl.write(struct.pack('<I',1610612736 ))
            #write 12 bytes, 00 00 00 00 00 00 00 00 00 00 00 00 to new
            Newmdl.write(bytes.fromhex('000000000000000000000000'))       
                   
              
          
        
    
        
        #If hastransparent == true
        if hastransparent == True:
          #Get current offset - mdl offset and save as newTransOff
          newTransOff = Newmdl.tell()- newOffsetList[i]          
          #Go back to vif_translucent_offs_off and update it with newTransOff then come back
          newReturnOffset = Newmdl.tell()
          Newmdl.seek(vif_translucent_offs_off)          
          Newmdl.write(struct.pack('<I', newTransOff))
          Newmdl.seek(newReturnOffset)
          #do another VIF packet loop but this time for transModel
          #-------------------------------------------------------------------  Change for transparent
          #for each model in submodelslist (Its here we are gonna write the VIF packets for transparent)
          transModelloop = 0
          for model2 in transModel:
            transModelloop +=1
            #Get vertex count
            vertex_count = 0
            transModelVertexList = []
            for vertexies in model2.vertices:
              vertex_count +=1
              transModelVertexList.append(vertexies)
            #print(vertex_count)
            UVList =[mathutils.Vector((0, 0))]*vertex_count  #To store the UVs without having to search 
            print("UVLIST: ", len(UVList))
            triangleList = []
            normalvert = True
            addedVertTriOffset =-1
            largestVertOffset= -1
            FlagaddedVertTriOffset =-1
            FlaglargestVertOffset= -1
            for fa, face in enumerate(model2.polygons):
                  
                triangleList.append(face.vertices[:])               
                
                #print("mesh[{fa}].SetTriangle {v_i};".format(fa=fa, v_i=triangleList[fa]))
                for ver in face.vertices[:]:
                  
                  if ver == face.vertices[:][0]:
                    

                    if abs(ver - face.vertices[:][1]) >2 or abs(ver - face.vertices[:][2]) >2 or use_some_setting == True: #if vert 1 and 2 are within 2 range of 0 then its a normal vert and should be ordered lowest to heighest
                      normalvert = False

                  if normalvert == True and ver >largestVertOffset:
                    largestVertOffset = ver +1
                    FlaglargestVertOffset = ver +1
              
                  if addedVertTriOffset == -1  and normalvert == False: #As the for loop continues triangle list is getting larger, as soon as a non normal triangle is spotted addedVertTriOffset is set                  
                      addedVertTriOffset = len(triangleList)-1
                      FlagaddedVertTriOffset = len(triangleList)-1


                    
            
                 

            #for all the non normal verts, reorder them
            print("AddedVertTriOffset (First edited triangle)", addedVertTriOffset)
            print("LargestVertOffset (First edited vertex)",largestVertOffset)
            #For every non normal triangle, order it into a new form of largestVertOffset+2 largestVertOffset+1 largestVertOffset, copying the vertecies data from 
            #the original tri to the new tris and swap them, swaping the verts in the triangle list too
            print("Generating Uv List...")
            vertLoopDict = {}#structure vertexID : loopID, lets uvs find the correct vert it needs. Need the blender loop the vertex is in.
            for face in model2.polygons:
              for vert_idx, loop_idx in zip(face.vertices, face.loop_indices):
                vertLoopDict [vert_idx] = loop_idx
                uv_coords = model2.uv_layers.active.data[loop_idx].uv                    
                UVList[vert_idx]= uv_coords

            vertex_Dict = {} #structure vertexID : [tri#, position in tri]
            for index, tri in enumerate(triangleList):
                  for tri_index, tri_vert in enumerate(tri):
                    vertex_Dict[tri_vert] = [index, tri_index] 
            #For every non normal triangle, order it into a new form of largestVertOffset+2 largestVertOffset+1 largestVertOffset, copying the vertecies data from 
            #the original tri to the new tris and swap them, swaping the verts in the triangle list too
            if addedVertTriOffset > -1:
              if largestVertOffset == -1:
                largestVertOffset = 0
              while addedVertTriOffset < len(triangleList):
                    original_tri = list(triangleList[addedVertTriOffset])              
                    #print("Original triangle",triangleList[addedVertTriOffset], "Tri ",addedVertTriOffset )
                    
                    
                      
                    
                    
                    orgi_triVert1 = list(triangleList[addedVertTriOffset])[0]
                    replacementTri = vertex_Dict[largestVertOffset+2][0]
                    replacementTriVertIndex = vertex_Dict[largestVertOffset+2][1]
                    tri_vert = largestVertOffset+2                    
                    if tri_vert == largestVertOffset+2:
                      originalLoop = -1
                      foundLoop = -1
                      orgi_uv_coordsX = -1
                      orgi_uv_coordsY = -1
                      originalLoop = vertLoopDict.get(orgi_triVert1)  
                      foundLoop = vertLoopDict.get(tri_vert) 
                      if originalLoop != foundLoop:                   
                        orgi_uv_coordsX = model2.uv_layers.active.data[originalLoop].uv.x
                        orgi_uv_coordsY = model2.uv_layers.active.data[originalLoop].uv.y
                        found_uv_coords =model2.uv_layers.active.data[foundLoop].uv
                        model2.uv_layers.active.data[originalLoop].uv = found_uv_coords       
                        model2.uv_layers.active.data[foundLoop].uv.x = orgi_uv_coordsX
                        model2.uv_layers.active.data[foundLoop].uv.y = orgi_uv_coordsY 
                        UVList[tri_vert] = model2.uv_layers.active.data[foundLoop].uv
                      if replacementTri ==  addedVertTriOffset: #already on same triangle
                        if replacementTriVertIndex == 0:
                          print("Vert 0 already in correct tirangle and correct position")
                        else:
                          print("Vert 0 already in correct tirangle but incorrect position")  
                          temp_triVert = list(triangleList[addedVertTriOffset])[0] 
                          temp_listVert = transModelVertexList[temp_triVert]
                          transModelVertexList[temp_triVert] = transModelVertexList[largestVertOffset+2] #copy the vertex data from found vertex to original
                          transModelVertexList[largestVertOffset+2] = temp_listVert
                          original_tri[0] = original_tri[replacementTriVertIndex]

                          original_tri[replacementTriVertIndex] = temp_triVert

                      else:
                        tempVert1 = transModelVertexList[orgi_triVert1] #Vertex data of original tri vert 1
                        transModelVertexList[orgi_triVert1] = transModelVertexList[largestVertOffset+2] #copy the vertex data from found vertex to original
                        transModelVertexList[largestVertOffset+2] = tempVert1 #copy the vertex data from original to found vertex
                        temp_tri1 = list(triangleList[replacementTri]) #Triangle of found triangle
                        temp_tri1[replacementTriVertIndex] = original_tri[0]#Copy the original vert int to where the repalcement was found 
                        original_tri[0] = largestVertOffset+2 #Write the new vert to original tri
                        new_tri1 = tuple(temp_tri1)
                        triangleList[replacementTri] = new_tri1 #Overwrite the found tri with temp one
                      #Swap the values in dictionary
                      vertex_Dict[orgi_triVert1], vertex_Dict[largestVertOffset+2] = vertex_Dict[largestVertOffset+2], vertex_Dict[orgi_triVert1]  
                      new_new_tri = tuple(original_tri)
                      triangleList[addedVertTriOffset] = new_new_tri 


                    orgi_triVert2 = list(triangleList[addedVertTriOffset])[1]
                    replacementTri = vertex_Dict[largestVertOffset+1][0]
                    replacementTriVertIndex = vertex_Dict[largestVertOffset+1][1]
                    tri_vert = largestVertOffset+1   
                    if tri_vert == largestVertOffset+1:
                      originalLoop = -1
                      foundLoop = -1
                      orgi_uv_coordsX = -1
                      orgi_uv_coordsY = -1
                      originalLoop = vertLoopDict.get(orgi_triVert2)  
                      foundLoop = vertLoopDict.get(tri_vert) 
                      if originalLoop != foundLoop:                   
                        orgi_uv_coordsX = model2.uv_layers.active.data[originalLoop].uv.x
                        orgi_uv_coordsY = model2.uv_layers.active.data[originalLoop].uv.y
                        found_uv_coords =model2.uv_layers.active.data[foundLoop].uv
                        model2.uv_layers.active.data[originalLoop].uv = found_uv_coords   
                        model2.uv_layers.active.data[foundLoop].uv.x = orgi_uv_coordsX
                        model2.uv_layers.active.data[foundLoop].uv.y = orgi_uv_coordsY 
                        UVList[tri_vert] = model2.uv_layers.active.data[foundLoop].uv
                      if replacementTri ==  addedVertTriOffset: #already on same triangle
                        if replacementTriVertIndex == 1:
                          print("Vert 1 already in correct tirangle and correct position")
                        else:
                          print("Vert 1 already in correct tirangle but incorrect position")  
                          temp_triVert = list(triangleList[addedVertTriOffset])[1] 
                          temp_listVert = transModelVertexList[temp_triVert]
                          transModelVertexList[temp_triVert] = transModelVertexList[largestVertOffset+1] #copy the vertex data from found vertex to original
                          transModelVertexList[largestVertOffset+1] = temp_listVert
                          original_tri[1] = original_tri[replacementTriVertIndex]
                          original_tri[replacementTriVertIndex] = temp_triVert
                      else:
                        tempVert2 = transModelVertexList[orgi_triVert2] #Vertex data of original tri vert 2
                        transModelVertexList[orgi_triVert2] = transModelVertexList[largestVertOffset+1] #copy the vertex data from found vertex to original
                        transModelVertexList[largestVertOffset+1] = tempVert2 #copy the vertex data from original to found vertex
                        temp_tri2 = list(triangleList[replacementTri]) #Triangle of found triangle
                        temp_tri2[replacementTriVertIndex] = original_tri[1]#Copy the original vert int to where the repalcement was found 
                        original_tri[1] = largestVertOffset+1 #Write the new vert to original tri
                        new_tri2 = tuple(temp_tri2)
                        triangleList[replacementTri] = new_tri2 #Overwrite the found tri with temp one
                        #Swap the values in dictionary
                      vertex_Dict[orgi_triVert2], vertex_Dict[largestVertOffset+1] = vertex_Dict[largestVertOffset+1], vertex_Dict[orgi_triVert2]
                      new_new_tri = tuple(original_tri)
                      triangleList[addedVertTriOffset] = new_new_tri 
                    


                    orgi_triVert3 = list(triangleList[addedVertTriOffset])[2]
                    replacementTri = vertex_Dict[largestVertOffset][0]
                    replacementTriVertIndex = vertex_Dict[largestVertOffset][1]
                    tri_vert = largestVertOffset
                    if tri_vert == largestVertOffset:
                      originalLoop = -1
                      foundLoop = -1
                      orgi_uv_coordsX = -1
                      orgi_uv_coordsY = -1
                      originalLoop = vertLoopDict.get(orgi_triVert3)  
                      foundLoop = vertLoopDict.get(tri_vert) 
                      if originalLoop != foundLoop:                   
                        orgi_uv_coordsX = model2.uv_layers.active.data[originalLoop].uv.x
                        orgi_uv_coordsY = model2.uv_layers.active.data[originalLoop].uv.y
                        found_uv_coords =model2.uv_layers.active.data[foundLoop].uv
                        model2.uv_layers.active.data[originalLoop].uv = found_uv_coords                    
                              
                        model2.uv_layers.active.data[foundLoop].uv.x = orgi_uv_coordsX
                        model2.uv_layers.active.data[foundLoop].uv.y = orgi_uv_coordsY 
                        UVList[tri_vert] = model2.uv_layers.active.data[foundLoop].uv
                        
                      if replacementTri ==  addedVertTriOffset: #already on same triangle
                        if replacementTriVertIndex == 2:
                          print("Vert 2 already in correct tirangle and correct position")
                        else:
                          print("Vert 2 already in correct tirangle but incorrect position")  
                          temp_triVert = list(triangleList[addedVertTriOffset])[2] 
                          temp_listVert = transModelVertexList[temp_triVert]
                          transModelVertexList[temp_triVert] = transModelVertexList[largestVertOffset] #copy the vertex data from found vertex to original
                          transModelVertexList[largestVertOffset] = temp_listVert
                          original_tri[2] = original_tri[replacementTriVertIndex]
                          original_tri[replacementTriVertIndex] = temp_triVert
                      else:
                        tempVert3 = transModelVertexList[orgi_triVert3] #Vertex data of original tri vert 3
                        transModelVertexList[orgi_triVert3] = transModelVertexList[largestVertOffset] #copy the vertex data from found vertex to original
                        transModelVertexList[largestVertOffset] = tempVert3 #copy the vertex data from original to found vertex
                        temp_tri3 = list(triangleList[replacementTri]) #Triangle of found triangle
                        temp_tri3[replacementTriVertIndex] = original_tri[2]#Copy the original vert int to where the repalcement was found 
                        original_tri[2] = largestVertOffset #Write the new vert to original tri
                        new_tri3 = tuple(temp_tri3)
                        triangleList[replacementTri] = new_tri3 #Overwrite the found tri with temp one
                      
                      vertex_Dict[orgi_triVert3], vertex_Dict[largestVertOffset] = vertex_Dict[largestVertOffset], vertex_Dict[orgi_triVert3]
                      new_new_tri = tuple(original_tri)
                      triangleList[addedVertTriOffset] = new_new_tri 
                    


                
                    

                
                  
                    largestVertOffset+=3
                    


                  
                    new_new_tri = tuple(original_tri)
                    triangleList[addedVertTriOffset] = new_new_tri
                    print(transModelNames[transModelloop-1],"  New triangle",triangleList[addedVertTriOffset], "Tri ",addedVertTriOffset," /", len(triangleList)  )
                    addedVertTriOffset+=1

            print("Generating flag list for each vertex..." )
            flagList =[] #To store the flags of a dmatag without having to search      
            flagvert = 0
            if(FlagaddedVertTriOffset == -1):
              FlagaddedVertTriOffset = len(triangleList)
            while flagvert < FlaglargestVertOffset:  
              if(flagvert%100 == 0 ):  
                print(submodelslistNames[submodelslistloop-1], "Vert Flag: ",  flagvert, " / ", vertex_count ) 

              flag = -1
              vertInNextTri = False
              sawAFellowVert = False
              #make triangle loop = to the tri# of a flagvert in vertDictionary vertex_Dict[flagvert][0]
              triangleLoop = 0

              
              while triangleLoop < FlagaddedVertTriOffset:
                    
                    if triangleLoop+1 == FlagaddedVertTriOffset:                    
                      if vertInNextTri == False: 
                        if sawAFellowVert == True:               
                          flag = -1
                          
                      if flagvert == vertex_count-1:
                        flag = 32
                    elif flagvert == triangleList[triangleLoop][0]:
                      for nextTriVerts in triangleList[triangleLoop+1]:
                        if flagvert == nextTriVerts:                                                 
                            vertInNextTri = True

                      if vertInNextTri == True:                                            
                        flag = 0  
                      else:                      
                        for currenttris in triangleList[triangleLoop]:
                          for nexttris in triangleList[triangleLoop+1]:
                            if currenttris == nexttris:                            
                              sawAFellowVert = True
                        
                        if sawAFellowVert == False:                        
                          flag = 0 
                    elif flagvert == triangleList[triangleLoop][1]: 
                      for nextTriVerts in triangleList[triangleLoop+1]:
                        if flagvert == nextTriVerts:                          
                          vertInNextTri = True
                      if vertInNextTri == True:
                        flag = -1  
                    
                    elif flagvert == triangleList[triangleLoop][2]:
                      for nextTriVerts in triangleList[triangleLoop+1]:
                          if flagvert == nextTriVerts:                          
                            vertInNextTri = True

                      if vertInNextTri == True:
                        flag = 32 
                      else:                     
                        
                        for currenttris in triangleList[triangleLoop]:
                          for nexttris in triangleList[triangleLoop+1]:
                            if currenttris == nexttris:                            
                              sawAFellowVert = True
                        if sawAFellowVert == False:
                          
                          if triangleList[triangleLoop][2]< triangleList[triangleLoop][1]:
                            if triangleList[triangleLoop][2]< triangleList[triangleLoop][0]:
                              flag = -1
                          else:
                            flag = 32 
                          
                    
                    
                    triangleLoop +=1                  
                    if vertInNextTri == True:
                      triangleLoop = FlagaddedVertTriOffset
              flagList.append(flag)
              flagvert+=1

            while flagvert < vertex_count:  
              if(flagvert%100 == 0 ):  
                print(submodelslistNames[submodelslistloop-1], "Vert Flag: ",  flagvert, " / ", vertex_count ) 

              flag = -1
              vertInNextTri = False
              sawAFellowVert = False
              #make triangle loop = to the tri# of a flagvert in vertDictionary vertex_Dict[flagvert][0]
              triangleLoop = vertex_Dict[flagvert][0]

                  
              if triangleLoop+1 == len(triangleList):                    
                      if vertInNextTri == False: 
                        if sawAFellowVert == True:               
                          flag = -1
                          
                      if flagvert == vertex_count-1:
                        flag = 32
              elif flagvert == triangleList[triangleLoop][0]:
                      for nextTriVerts in triangleList[triangleLoop+1]:
                        if flagvert == nextTriVerts:                                                 
                            vertInNextTri = True

                      if vertInNextTri == True:                                            
                        flag = 0  
                      else:                      
                        for currenttris in triangleList[triangleLoop]:
                          for nexttris in triangleList[triangleLoop+1]:
                            if currenttris == nexttris:                            
                              sawAFellowVert = True
                        
                        if sawAFellowVert == False:                        
                          flag = 0 
              elif flagvert == triangleList[triangleLoop][1]: 
                      for nextTriVerts in triangleList[triangleLoop+1]:
                        if flagvert == nextTriVerts:                          
                          vertInNextTri = True
                      if vertInNextTri == True:
                        flag = -1  
                    
              elif flagvert == triangleList[triangleLoop][2]:
                      for nextTriVerts in triangleList[triangleLoop+1]:
                          if flagvert == nextTriVerts:                          
                            vertInNextTri = True

                      if vertInNextTri == True:
                        flag = 32 
                      else:                     
                        
                        for currenttris in triangleList[triangleLoop]:
                          for nexttris in triangleList[triangleLoop+1]:
                            if currenttris == nexttris:                            
                              sawAFellowVert = True
                        if sawAFellowVert == False:
                          
                          if triangleList[triangleLoop][2]< triangleList[triangleLoop][1]:
                            if triangleList[triangleLoop][2]< triangleList[triangleLoop][0]:
                              flag = -1
                          else:
                            flag = 32 
                          
                    
                    
                    
              flagList.append(flag)
              flagvert+=1
            
            

            #Int vertecies processed = 0
            vertecies_processed = 0
            #bool lastVIF = false
            lastVIF = False
            #While vertecies processed < vertex count (Until all the vertecies in the model are processed)
            print("Generating dmaTags (Groups of vertexies and their data)" )
            while vertecies_processed < vertex_count:
              #int vertexset = 0
              vertexset = 0
              #if vertexcount - vertecies processed > 74
              if vertex_count - vertecies_processed > 74:
                #vertexset = 74
                vertexset = 74
              #else
              else:
                #vertexset = vertexcount - vertecies processed  (If at the end of the list of vertecies to process)
                vertexset = vertex_count - vertecies_processed
                #if last submodel in submodel list
                if transModelloop == len(transModel):
                    #lastVIF = true
                    lastVIF = True
              if lastVIF == False:
              #Check here to see if the next dmatag will start with 2 -1 flags and if not add or subtract to vertexset as needed
                if vertecies_processed+vertexset+1 < len(flagList):                
                    
                  if flagList[vertecies_processed+vertexset] == -1 and flagList[vertecies_processed+vertexset+1] == -1:                
                       print("all good, ", vertecies_processed, "/ ", vertex_count," processed")                   
                  else:
                    while flagList[vertecies_processed+vertexset] != -1 and vertexset > 0 or flagList[vertecies_processed+vertexset+1] != -1 and vertexset > 0:
                      vertexset-=1
                    if vertexset <= 0 and flagList[vertecies_processed+vertexset] != -1 or vertexset <= 0 and flagList[vertecies_processed+vertexset+1] != -1 :
                      while flagList[vertecies_processed+vertexset] != -1  or flagList[vertecies_processed+vertexset+1] != -1 :
                        vertexset+=1
                    print("fixed, new vertex count:", vertexset," ",  vertecies_processed, "/ ", vertex_count, "processed")   
      
              #Wrtie a DmaTag to new
              #The first byte will be ((vertexset*48)/16) + 3 , then 00 00 10
              DmaTagHead = int(((vertexset*48)/16) + 3)
              #print(DmaTagHead)
              Newmdl.write(struct.pack('<B', DmaTagHead) +bytes.fromhex('000010'))

              #Wrtie STCYCL and UNPACK commands(Skipped in blender)(Needed in game) [00 00 00 00 04 04 00 01 00 80 ?? ?? ?? 00 00 00] it seems the 3 ?? CANNOT be made 0 without issue to new
              Newmdl.write(bytes.fromhex('00000000040400010080C86CC8000000'))
              #Wrtie vertex table count as vertexset to new as int16
              Newmdl.write(struct.pack('<h', vertexset))
              #Write 01 00 to new mdl
              Newmdl.write(bytes.fromhex('0100'))
              #Write vertex count as vertexset to new as int 16
              Newmdl.write(struct.pack('<h', vertexset))
              # int unique value = Goto old mdl model off+ vif_opaque_offs + 16 to skip the unpack commands, + 6 to skip the begining of the vertex table to get to the unique value read as a int16
              Newmdl.write(struct.pack('<h', uniqueValue))

              #Write mode as 06 00 to new. Shadow modles use mode 16 but since they are getting copied as is we can assume mode 6 for custom models
              Newmdl.write(bytes.fromhex('0600'))
              #Write 00 9C XX 80 00 00 00 40 3E 30 12 04 00 00 00 00 00 00 to new where XX is vertexset as hex (struct.pack('<B', vertexset))
              Newmdl.write(bytes.fromhex('009C')+ struct.pack('<B', vertexset) +bytes.fromhex('80000000403E301204000000000000'))

              #For i < vertexset (each vertex in table)
              vert = 0
              while vert < vertexset:                

                #print("Vert:", vert + vertecies_processed, "Start offset:" , Newmdl.tell())
                #Get face orientation of vertex
                #Write flag to new to bytes 1 and 2. This is the face orientation of the triangle formed. 0 and 32 switches it, -1 is for no triangle. 
                #Flag reverse solve rules: If the vertex first apperance is on the left side of tri and has atleast 1 more appearance then it is flag 0, if on right its flag 32, 
                # if in middle or only has one appearance it is -1, but if only one appearance and
                # none of the other vertexies in the triangle show up in the next triangle then its the rules for 0 and 32 unless the value is on right side and is lowest in triangle, then its -1
                #A dmatag needs to start with 2 -1
                
                #print("Vertex ", vert+vertecies_processed, "flag ", flag)
                Newmdl.write(struct.pack('<h', flagList[vert+vertecies_processed]))
                #Newmdl.write(bytes.fromhex('0200'))#Temp 32
                
                #Write 00 00 to bytes 3 and 4
                Newmdl.write(bytes.fromhex('0000'))
                #Get vertex weight for current vertex bone group
                #Write vertex weigh(should just be 1 so try just that first) to bytes 5-8 as a float
                Newmdl.write(struct.pack('<f', 1))
              
                #Write 00 00 to bytes 9-12
                Newmdl.write(bytes.fromhex('00000000'))
                #For bytes 13 - 16 i am not sure what it is for, 0ing it dosent seem to change anything but the normal values seen are seen are 00200000 for normal vertex and 00A00000 for -1 flags
                if flag == -1:
                  Newmdl.write(bytes.fromhex('00A00000'))
                else:
                  Newmdl.write(bytes.fromhex('00200000'))
                #For bytes 17-20 calculate the mdl x position from the bone matrix, using the bone name the vertex is attached to find a index in the bone name list and then
                #it should be the same index in the oldmdl bone matracies list
                #print(subModelVertexList[vert+vertecies_processed].groups)
                
                ob = bpy.data.objects[transModelNames[transModelloop-1]]
                boneIndex = -1 #This will be the index to the parent bone in the mdl
                groupName= ""
                vertexToUse =mathutils.Vector((0, 0, 0))
                for ran in range(0, len(ob.vertex_groups)): #For every vertex group in the submodel model
                  group = ob.vertex_groups[ran]
                  
                  for g in transModelVertexList[vertecies_processed+vert].groups:
                    if ran == g.group:                   
                      groupName = group.name
                      vertexToUse = transModelVertexList[vertecies_processed+vert]
                      #print("Vert", vertecies_processed+vert, model.vertices[vertecies_processed+vert].co, "Group:" , group.name)
                
                v_mixed = mathutils.Vector((vertexToUse.co.x, vertexToUse.co.y,vertexToUse.co.z, 1))              
                #print("updated vertex:", v_mixed)
                for boneloop in range(0, len(bone_names)):
                  if groupName == bone_names[boneloop]:
                    boneIndex = boneloop
                
                #print("Matrix:", boneMatrix[boneIndex], "Bone:", boneIndex)
                x = np.dot(np.linalg.inv(boneMatrix[boneIndex]), v_mixed) 
                #np.linalg.inv(A)  is simply the inverse of A, np.dot is the dot product

                #print("Vert", vertecies_processed+vert,"Original?:",x)
                
                
                Newmdl.write(struct.pack('<f', x[0]))
                

                #For bytes 21-24 calculate mdl y position
                Newmdl.write(struct.pack('<f', x[1]))
                #For bytes 25-28 calculate mdl z position
                Newmdl.write(struct.pack('<f', x[2]))
                
                #For bytes 29-30 write the bone index *4
                #print(boneIndex)
                Newmdl.write(struct.pack('<h', boneIndex*4))
                #For bytes 31-32 write the bone index
                Newmdl.write(struct.pack('<h', boneIndex))
                
                #For bytes 33-36 write UV x to new
                my_uv =UVList[vertecies_processed+vert] 
                        

                UVx = my_uv.x
                Newmdl.write(struct.pack('<f', UVx))
                #For bytes 37-40 write UV y to new
                UVy =1 - my_uv.y
                #print("Vertex:", vert+ vertecies_processed, "UVx", UVx, "UVy", UVy)
                Newmdl.write(struct.pack('<f', UVy))
                #For bytes 41-44 write float 1
                Newmdl.write(struct.pack('<f', 1))
                #For bytes 45-46 write the texture index float to new  
                #Need to find the correct texture for the transparent model
                NeededName = transModelNames[transModelloop-1]  
                third_to_last_char = NeededName[-3]#This char should be the material number          
                Newmdl.write(struct.pack('<H', int(third_to_last_char)))
                #Bytes 47-48
                Newmdl.write(bytes.fromhex('0000'))
                
                #Temp empty vertex data
                #Newmdl.write(bytes.fromhex('00000000000000000000000000000000'))
                #Newmdl.write(bytes.fromhex(''))
                vert +=1

              #After writing all the vertecies in the table:
              #Write 00 00 00 17 00 00 00 00 00 00 00 00 00 00 00 00 before next DMAtag
              Newmdl.write(bytes.fromhex('00000017000000000000000000000000'))
              vertecies_processed +=vertexset
              #print("Vertecies processed:",vertecies_processed, " out of ", vertex_count  )
              
            #print(lastVIF)
            #If lastVIF
            if lastVIF:
              #DmaTag = 1610612736
              #write DMATag to new
              Newmdl.write(struct.pack('<I',1610612736 ))
              #write 12 bytes, 00 00 00 00 00 00 00 00 00 00 00 00 to new
              Newmdl.write(bytes.fromhex('000000000000000000000000'))    
      

        #Find the last dmaTag in current loop
        lastDMAtagOffset = 0
        #go to first dmaTag
        Oldmdl.seek(oldOffsetList[i]+vif_opaque_offs)
        #print("QWC Offset to next dmatag?:", (qwc + 1) * 16)
        currentDMAtag = 0
        #while currentDMAtag !=1610612736
        while currentDMAtag != 1610612736:
          #keep going to the next dmatag
          oldReturnOffset = Oldmdl.tell()          
          #currentDmatag = oldmdl.read
          currentDMAtag = Oldmdl.read_uint32()
          Oldmdl.seek(oldReturnOffset)

          #if currentDMAtag == 1610612736
          if currentDMAtag == 1610612736:            
            #lastDMAtagOffset = oldmdl.tell
            lastDMAtagOffset = Oldmdl.tell()
          else:
            qwc = currentDMAtag & 0xFF
            offsetToNextDMAtag = int((qwc + 1) * 16)
            Oldmdl.seek(Oldmdl.tell()+offsetToNextDMAtag)

            
            
        print("Last DMATag if no transparent:", lastDMAtagOffset)  
        #if hastransparent
        if hastransparent == True:          
          #skip 16 bytes to skip the last dmatag and the 12 00s
          Oldmdl.skip(16)
          lastDMAtagOffset = 0
          currentDMAtag = 0
          while currentDMAtag != 1610612736:
          #keep going to the next dmatag
            oldReturnOffset = Oldmdl.tell()          
            #currentDmatag = oldmdl.read
            print("Transparent DMAtag offset:", Oldmdl.tell())
            currentDMAtag = Oldmdl.read_uint32()
            Oldmdl.seek(oldReturnOffset)

            #if currentDMAtag == 1610612736
            if currentDMAtag == 1610612736:            
              #lastDMAtagOffset = oldmdl.tell
              lastDMAtagOffset = Oldmdl.tell()
            else:
              qwc = currentDMAtag & 0xFF
              offsetToNextDMAtag = int((qwc + 1) * 16)
              Oldmdl.seek(Oldmdl.tell()+offsetToNextDMAtag)

        print("lastDMATag:", lastDMAtagOffset)
        #Since we already wrote the 12 empty bytes after the last offset in newmdl we can skip those while copying from old after last DMA 
        Oldmdl.seek(lastDMAtagOffset+16)      
        
        #If this is the last model offset copy the rest of the file.
        if i == len(oldOffsetList)-1:
          LoopOffset = Oldmdl.tell()          
          while LoopOffset < Oldmdl.filesize:
            Oldmdl.seek(LoopOffset)      
            Newmdl.write(struct.pack('<h', Oldmdl.read_int16()))#< for little endian ! for big endian
            LoopOffset+= 2     
        #Else copy everything from last DmaTag of current model in oldmdl to the next model offset
        else:
          LoopOffset = Oldmdl.tell()          
          while LoopOffset < oldOffsetList[i+1]:
            Oldmdl.seek(LoopOffset)      
            Newmdl.write(struct.pack('<h', Oldmdl.read_int16()))#< for little endian ! for big endian
            LoopOffset+= 2
    
    #Go back to begining of new file and update model offsets with newOffsetlist
    
    Newmdl.seek(0)
    for newOffsetCountLoop in range(0, len(newOffsetList)):
      Newmdl.write(struct.pack('<I', newOffsetList[newOffsetCountLoop])) 

  
  

    return {'FINISHED'}


class ExportKhReComMdl(Operator, ExportHelper):
    """Exports the object to become a RECOM MDL file"""
    bl_idname = "export_test.some_data"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Export MDL model"

    # ExportHelper mixin class uses this
    filename_ext = ".mdl"

    filter_glob: StringProperty(
        default="*.mdl",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )# type: ignore


    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    use_setting: BoolProperty(
        name="All Custom Fast export",
        description="If the entire model is made up custom mesh and there is no original that is needed this will speed up the export.",
        default=False,
    ) # type: ignore

    type: EnumProperty(
        name="Example Enum",
        description="Choose between two items",
        items=(
            ('OPT_A', "First Option", "Description one"),
            ('OPT_B', "Second Option", "Description two"),
        ),
        default='OPT_A',
    ) # type: ignore

    def execute(self, context):
        return write_mdl_data2(context, self.filepath, self.use_setting)





def menu_func_import(self, context):
  self.layout.operator(ImportKhReComAzf.bl_idname,text="Kingdom Hearts Re:COM Stage (.azf)")
  self.layout.operator(ImportKhReComGsd.bl_idname,text="Kingdom Hearts Re:COM Stage Gimmicks (.gsd)")
  self.layout.operator(ImportKhReComMdl.bl_idname,text="Kingdom Hearts Re:COM Model (.mdl)")

def menu_func_export(self, context):
    self.layout.operator(ExportKhReComMdl.bl_idname,text="Kingdom Hearts Re:COM Model (.mdl)")



classes = (ImportKhReComAzf,ImportKhReComGsd,ImportKhReComMdl,AZF_PT_import_options,GSD_PT_import_options,MDL_PT_import_options ,ExportKhReComMdl)


def register():
  for cls in classes:
    bpy.utils.register_class(cls)

  bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
  bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
  for cls in classes:
    bpy.utils.unregister_class(cls)

  bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
  bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
  register()

