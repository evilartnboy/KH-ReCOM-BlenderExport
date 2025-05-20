# KH Re:COM Tools
#-Evilartnboy: I have updated the blender addon to allow for exporting. My tutorial for it will be in the blender addon section.

A set of experimental tools for researching Kingdom Hearts Re:Chain of Memories for the PlayStation 2.

## Extractor

Extracts all files from a KH Re:COM disk image (.ISO). Supports both NA and JP releases.

Sample usage:

```khrecom-ps2-extractor.exe C:\path\to\game.iso -d C:\optional\extract\dir```

The default location for extracted files will be a folder named `extract/` in the working directory.

## Resource Unpacker

Extracts files from packed resource file types. To find these files, run the above extractor on the .ISO first. Supp![1](https://github.com/user-attachments/assets/6c411ac6-54fe-4c5d-ba73-1b1dc0cb1a03)
orted extensions are:

* .ABC, .BIN, .EPD, .PTD
* .CAP (Camera Data)
* .CTD (Cutscene Data)
* .EFF (Particle Effects)
* .ESD, .GSD (Enemy, Gimmick Stage Data)
* .RTM, .VTM (TIM2 Images/Textures)
* .SPR (Sprites)
* .TXA (Animated Textures)
* .SND, .RSD, .VSM (Sound Bank)

Sample usage:

```khrecom-ps2-rsrc-unpacker.exe C:\path\to\resou.rce -d C:\optional\extract\dir```

By default, the unpacker will create a new folder in the working directory with the same name as the original file.

## Blender Add-on

<img src="img/blender-preview-0.png" alt="alt text" width="75%">

An experimental Blender importer for both stages (.AZF) and models (.MDL). Compatible with Blender 2.8x.


Installation Method A:

1. Locate the add-ons folder for Blender. In Windows, this path is typically: `%appdata%\Blender Foundation\Blender\2.8x\scripts\addons\`
2. Copy the `io_kh_recom\` folder into `addons\`.
3. Open Blender, go to `Edit -> Preferences`, and select the `Add-ons` tab.
4. Ensure the `Community` filter is selected, and locate `Import-Export: Kingdom Hearts Re:Chain of Memories` in the list. Click the checkmark next to this add-on to load it. Close the preferences window.
5. Go to `File -> Import` and select either from the list of file formats:
    * `Kingdom Hearts Re:COM Stage (.azf)`
    * `Kingdom Hearts Re:COM Stage Gimmicks (.gsd)`
    * `Kingdom Hearts Re:COM Model (.mdl)`

Installation Method B:

1. Pack the contents of `io_kh_recom\` into a single ZIP file.
2. Open Blender, go to `Edit -> Preferences`, and select the `Add-ons` tab.
3. Click `Install...` and locate the ZIP you created in step 1.
4. Follow steps 4 and 5 in method A.

-----------Export Tutorial
This is a tutorial for model swapping for KH ReCom on the PC.
So, for setting up your work environment for modding recom I would first recommend decompiling your game with the OpenKH tools and install 
Murugo's Blender recom tools https://github.com/Murugo/KH-ReCOM-Tools that I built this exporter off of. Then you just want to download my 
version of it and overwrite the murugo addon.

The version of blender I am using is 3.4 with python 3.10.8 and I would recommend clearing out your scene of any objects and enable the terminal

The export tool is very quirky so I will walk you through a mod so you can understand the step by step

First we can either prepare a model to use or import a Recom model, lets import first.
![1](https://github.com/user-attachments/assets/17476d46-ea12-4050-b06d-190ac3dea6b2)


I would recommend making a copy of your export of recom so you dont accidentally mess it up. For making patches for recom,
put the files in a folder structure of MyPatch/Recom/, then your original and remastered folders from then export.

The mdl files we will be editing are under the original folder. I will be modding NPC 105, Aerith.
If you import the mdl file with its RTM file in the same folder it will import its original ps2 textures too and can be viewed if you 
enable viewport shading.

On the right you will see that a character model is made up of several sub models, each with its own texture denoted by _mat#.
The model with _t is a transparent model, meaning it will be transparent when the texture is black and visible everywhere else.
On aerith this is just her bracelet.
![2](https://github.com/user-attachments/assets/f94fd3b7-b315-4dc5-8ecb-4eda25f374f7)


The vertex groups correspond to the bones that the vertecies in each submodel are attached to. The great thing is that every submodel
has a copy of every bone so we can add new vertex groups to connect to a bone even if its not normaly in there, the game will just use it.
![3](https://github.com/user-attachments/assets/1f435cd0-554a-4c32-be38-e48a1b1c0fc8)

You will notice that there are only triangles in the model, no ngons. The exporter will get angry if you dont triangulate each mesh.
![4](https://github.com/user-attachments/assets/bfcc9542-a93c-4cae-bfc4-c5fed5f9470d)

Now that we have our target lets find what we want to do with her. We can edit the positions of any existing vertecies for a easy mod, 
maybe long fingers? But that would be boring. Lets go with captian keys from halo. 

This will do.
![5](https://github.com/user-attachments/assets/2c4d8def-f33e-49cf-bdcc-2e4721d26622)

Opening up a clean blender file we import out model, go into uv editing and open up his textures, then equipt those textues to the correct model as a base color
![6](https://github.com/user-attachments/assets/b55bcc11-7638-4614-9ec1-acd69a7bafd3)
![7](https://github.com/user-attachments/assets/29ce87e2-5e2d-4a90-9de5-886f8598c5cf)

After cleaning up out model we can see what we have to work with.
![8](https://github.com/user-attachments/assets/93da0f85-5253-4ef2-b2b3-f51c75bd99f8)

Keys is 1 model but has 4 textures, while aerith only has 3 textures. This is a issue because we cant add new textures. I think its possible but that feature
is beyond what I need the program for. Looking at his textues the decals and eyes can probably be put on his body texture, saving 2 texture slots, something we
will see is important later.

For now we need to tpose the captian.
![9](https://github.com/user-attachments/assets/43191fe3-b593-4828-9465-6bd054a06ca0)

A good tutorial for posing models in blender can be found here https://youtu.be/WMxNinivOvs?si=1b0zOpeeJfRcSuPF

His fingers could use more polygons but im not gonna bother with this mod. Ill just have his entire hand be attached to the hand bone.

Now that he is posed we can import aerith and begin modding

Id recommend going into edit mode and moving all of aeriths vertex's back to making work easier and to resize your mod model to the same porportions as 
the original character. Keys arms are too long so we have to shorten them.
I am also going to separate keys head from the rest of his model since it has its own texture.
![10](https://github.com/user-attachments/assets/9fb4d923-4fcf-4961-8fac-5af4472c138a)

Now that we have our characters in position we can begin combining them. You want to first select your new model and then the model you want to join it to
and join them with cntl j. Make sure not to delete the original mesh before joining.

Then you go to the materials tab and vertex group tabs and remove any materials and vertex groups that dont belong to your KH model.

Here i joined his head to the submodel with mat0 and his body to mat1 and his patch to mat1_t
![11](https://github.com/user-attachments/assets/41e5c102-4ebb-46af-96d4-197e7e67b15b)

You will notice your model is defaulted to the KH texture and looks wrong. This is ok. we will now go get the textures for the KH model from the remastered folder in the same directory as where the model would be. Under the RTM folder is your textures. Now we will simply load the texture into gimp and paste in the texture for your added model, then export. This will overwrite the texture with the added model texture in layer 1. I will also add the texture for keys badges to his body texture, adding alpha to the parts i want transparent. Assuming you dont change the size of the texture like i did with the body then the UVs will work fine after you import the texture into blender and then set it as the texture. If not then simply resize the uvs until it fits
![11](https://github.com/user-attachments/assets/e8662968-83d5-45db-a779-2bceabb9fe3c)


Now we can see that keys looks great and aerith is a freak. One key thing to note is that if we can avoid it we dont use a texture with a face. As you saw in the texture folder there is extra textures for blinking and speaking. These textures auto apply to the model texture in the spot where its UVs should be. Causing blinking skin if we have uvs in that area. 
![12](https://github.com/user-attachments/assets/9011f6b9-70c0-44ca-9f91-226a0423d969)

Now we will go through our import model and assign each vertex to a vertex group bone, making the corresponding group in the submodel if it isn't present. If each vertex isn't assigned then the model will throw a error when you try to import it.

After that we can begin removing the original kh mesh. Now each submodel needs at least 1 triangle in it for the game to work so for any models we did not add
a mesh too we will select a triangle, hit y and move it inside our model, also change the bones of that triangle to be the same as the mesh around it so it 
dosent come out. Edit: It seems like enemy models dont respond well to simple edits of vertex geometry, if you are just resizing something on a shadow or whatever split the mesh faces and edges by verts so the export thinks its a new mesh, NPC and player models seem to be fine with simple edits.
![13](https://github.com/user-attachments/assets/e1371b02-5cff-4ce0-8c68-2baa30f7ebb3)

After that there is just one last thing we need to do before exporting. We must split each triangle in the mesh away from each other into individual triangles. This is because
the mdl file is structured to use strips of tris and not entire meshes, likely a ps2 limitation. After divining the triangle rules for a week I was able to get the exporter to accept
a bunch of individual triangles pretending to be one big mesh, essentially tripling the vertex count. This shouldn't be a issue as long as the export function dosent need to search 
each vertex for its processing causing the process to take exponentially more and more time the more vertices there are (PS this is exactly how it works. I made a program that works
not one that is good. If you can figure out how to search for verts easier please do so).

Selecting the entire mesh we go to Mesh, split, faces and edges by verticies.

Finally we can export. Vertex count dosent have a major effect on export times anymore so get creative.

For exporting you go to export and select the original file. Make sure you are not in edit mode or exporting will not work. Blender will then create a new file with the same name but with NEW at the end. This is your exported model. If you have the terminal open you can watch the process of exporting.
![14](https://github.com/user-attachments/assets/e1d3e7d1-f8ea-4632-85bc-ebaa0cffa030)

After exporting the UVs of your model in blender will be messed up, just hit undo to fix it.
![15](https://github.com/user-attachments/assets/edf22d3c-c448-4eb7-90bf-6d8cf3f4697c)

Now we can import our exported mdl to blender. What did you think we were done? Now we got to fix the errors.
![16](https://github.com/user-attachments/assets/d7b4bbed-10f9-4338-9bde-b4c645605915)

Adding the textures to the new mdl we can see some errors. Mainly triangles stretched to other parts of the mdl and some messed up uvs. Im not sure exactly what causes this but I think
its something to do with how groups of vertecies are stored and the flags for each triangle is read. Regardless we can fix it here. For the stretched tris just go find the vertex and bring it back to around where it should be, it will be connected to other verts in a strip of meshes but thats ok, the program will export it fine now. The bone will have changed so you need to change it back. Ps each vertex can only have 1 bone. For missing triangles you can select three verts around it, hit f to make a new face, then hit y to split the triangle from them. For any messed up uvs just go into uv editing and fix them. Another common error is a flipped face orientation. You cant use the blender normal flip to fix this, you need to manually flip the vertecies on the mesh to correct it.


A quick tip for moving vertecies while keeping them separate is selecting one then the next, shift s and then selected to active.
I would also recommend fixing the model in a clean blender window or saving and loading the current one to clear out any other models.

After your fixes you can then export this new model over your previous export. Repeat these steps until the model comes out right.
![17](https://github.com/user-attachments/assets/91f4c390-e854-4629-a95c-a58679e905ca)
And after just a few attempts we got it to export with no errors. Now we can put it into the game!

Simply take your new MDL file and replace the original with it. Then take your new texture files and replace those too. Then you are going to make a patch by dragging the mypatch folder into KHPCPatchManager, then opening the exe to apply that patch to your game. If everything worked then the model should be in game. If you have a error with the model, like it being to small or too many triangles ontop of eachother the game will crash when you load the area with your model.

And just like that we have a brand new character!.
![18](https://github.com/user-attachments/assets/d0d13191-4569-45f4-b626-93a40936632b)

