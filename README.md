# Free-Solidworks-OBJ-Exporter

Free SolidWorks .OBJ Exporter v2.0 published 1/4/2012


## DISCLAIMER:

This software is free for use and to distribute. It is NOT to be sold as is, nor in modified
form,nor incorporated in other software for sale.
This software and the accompanying files are provided as is.
The macro will act upon the current SolidWorks document.
As a precaution be sure you have a current back up your data before using this macro.
There are no warranties, expressed or implied, that this macro will perform without fault.
Use at your own risk. 
This macro has been tested with Win XP Pro 32 bit using SW2005 and SW2009 and with Blender 2.62
and Octane beta 2.57 but not exhaustively.
 
 
## INTRODUCTION:

The purpose of this macro is to export meshes in Alias|Wavefront .obj format from SolidWorks.
The materials details are also exported as a standard Alias|Wavefront .mtl file.
These may be subsequently automatically loaded into Blender or Octane for rendering purposes.
The .obj and .mtl are also suitable for use in other cg applications.
All files produced during export are placed in a new folder created in the same directory as the
current document. eg D:\surfboard.sldpart --> D:\surfboard OBJ\surfboard.obj
When you export again from the same SolidWorks document any existing OBJ directory and the
contained files will be overwritten without warning.
The macro UI provides the user with an opportunity to set custom tessellation parameters and other
useful options. The macro should work as intended with SolidWorks version 2005 and up.


## INSTALLATION:

The SW macro can go anywhere but conveniently where you keep your other SW macros. You will need
to use the provided toolbar button to launch the macro from SW. See the SW Help>Macros>customise
buttons to find out how to set this up. See also the included picture of the custom button
showing to select the modSWtoOBJ.InitialUI as the 'Method' to start.

NOTE: The macro will not run from the menu Tools/Macro/Run> or from the toolbar Macro>Run.
 
The macro included was authored in SW2009. Different SW versions will require you to open the
macro in the SW MS VBA window, reselect the Reference Libraries appropriate to that version, and
then save the macro. See the included 'References' picture of SW2009. Opening in another version
may show the References as being 'MISSING'. Look down the list and find equivalent entries but
for the year of your SW install. Sometimes SW will find these references itself.

The Blender helper script is required to load the finished .obj into Blender automatically.
It should work with Blender 2.5 and up. Make sure it goes in the same folder as the Blender.exe
The path to Blender is assumed to be C:\Program Files\Blender Foundation\Blender\blender.exe

The path to Octane is assumed to be C:\Program Files\Refractive Software\OctaneRender\Octane.exe

You can change these paths if necessary in the vba module code by going to lines 627 & 632
respectively.


## FURTHER USEAGE NOTES not covered in the 'About':

### CONFIGURATIONS:

The macro should correctly traverse complex configuations and all forms of patterns correctly
including exploded views. Assembly Features like holes and cuts are only considered if they are
propogated to the parts.
If your assembly has instances of the same subassy or part but in different configurations
it is necessary for the macro to force rebuilds as it progresses. This takes extra time and does
leave open the possibility that some rebuild errors may be discovered in the model while that is
underway. The macro will stop with an error, but no harm is done. You will however need to fix
the issue in the problem part or assy before you can successfully run the macro through entirely
when rerunning the macro again.
After running the macro you should NOT accept the SW prompt to save your models when closing a
document because they have changed. There is no change. It is only flagged so because of the
harmless rebuild. This also minimises the risk of some unintended change occuring by accident.


### COMPLEX PARTS AND ASSEMBLIES:

The tessellation from complex parts and assemblies is liable to take several minutes to complete
particularly those with numerous configurations to traverse. The files can also be quite large.
Be wary of tackling too much at once and creating a .obj that is too big to handle in other
applications. Because the macro only exports visible objects you can break the mission down
into convenient bites and then combine those .obj manually later in, say, Blender. The origin
will be consistant across the files. It also means you can avoid having to redo the whole mission
again if something changes.

You will find it hard to handle more than about 12m tris in any cg application presently. Such an
.obj file out of this script would amount to something in the order of 2gb and take about 35 mins.
A practical maximum size is probably 5 m tris. Note that 64 bit Windows is required for dealing
with such large files. To give an idea of what a large model means the Mach5 model shown in
some of the pictures is about 450,000 tris and the .obj is 87mb, so 11 of these would be enough.
The number of tris produced isnt so much to do with the size or number of objects as the need to
capture fine details with sufficient tessellation not to appear faceted. 


### TEXTURES:

You are not limited to the colour textures supplied with SolidWorks. You can substitute others
individually in the SW Appearances Property Manager or add a folder in the SW Task Pane for the
usual drag and drop application. The exporter should find these and copy them to the same
directory as the .obj at the end of the export process. You could also substitute other textures
for the exported ones when the .obj has been loaded into another cg application.

You can nominate to export 'spec' and 'bump' maps(textures) on the basis of the colour map
(texture) used in SW. The requirement for this is that these need to have the same basic name and
be in the same location as the colour map(texture). For example -
D:\myplace\mytexture.jpg, D:\myplace\mytexture spec.jpg, D:\myplace\mytexture bump.jpg

If you want to change the ' spec' and ' bump' labels to suit your own texture collection go to
lines 592,593,596,597,605,611 in the vba module code.

If you nominate to use spec and/or bump maps in the UI the texture name will appear in the .mtl
even if the images dont actually exist. The macro will skip any textures it cannot find. In the
case of a missing texture Octane will prompt you for one as the .obj loads. Blender will load
the file unhindered but you will need to source a substitute image afterward in the material's
texture panel. In some later Sw versions some materials do have bump maps (of a sort) supplied,
as well as the colour map(texture).


### SCENE COMPOSITION:

You can set up a studio scene in a SW part and use that with your model. For example, it might
include a floor/backdrop and rectangular surfaces to use as area lights. The part can either be
inserted into your model part or used as a component in an assembly. You can use mates to position
your studio or props exactly or just leave them floating. Of course you can use a number of parts
for individual elements of your scene. See the included simple example of a studio made in SW09.
Going through a cg app like Blender allows you to incorporate different props like trees or
people that are hard to produce in SW and to reposition or duplicate them easily. You can also
make use of other models like those of cars and trucks obtained from many sources and of different
file types. The SW exporter does not handle mesh instances.
Incidentally the green side of a SW sketch plane is the direction of the normal. 


### TESSELLATION:

The pictures accompanying this README show a mesh in Blender illustrating the standard SW
tessellation and another where the max face length has been set to 0.15m. This control is handy
to ensure the triangles are not too long and thin which is bad for use with render engines.
With finer tessellation settings intricate shapes are reproduced well, particularly 3d curved
surfaces, and it also allows for effective subdivision so normal maps can work effectively if
applied later.

Smaller diameter parts need lower deviation settings to ensure that the tessellation presents
sufficient roundness or smoothness when seen in a render. If you have an assembly that has
both large and very small detailed parts use the SW Image Quality settings in each document
rather than the custom settings in the macro UI - check the Disable option in the macro UI panel.
Another way around this is to export just the large items in one .obj by making only them visible
and then follow up with the smaller items in another .obj making only them visible, with custom
settings for each as appropriate.

I suggest you try your export with the custom tessellation disabled in the first instance and
if necessary use custom ones. The provided default custom numbers are a good starting point but
will require some experimentation/familiarisation to get the best results in each case.
To make sure very small parts are captured faithfully be sure to set the Max Chord Width small
enough. Try 1/10th of the minimum radius of the smallest feature. You might need to set the Min
Face Width to be almost as small if the objects are tiny.


## KNOWN ISSUES:

### SOLIDWORKS:

SolidWorks is pretty poor at texture unwrapping. You will probably want to open the .obj in
another application like Blender to tweak the unwrap and other aspects of materials.
In the 'SW unwrap errors' folder included with this macro you can see examples of how poor the
native unwrapping is. Even a stock std Blender Smart UV Project unwrap is a vast improvement.
 
The UV mapping styles in SW like spherical or cylindrical and the scaling, rotation etc do not
actually make any difference to the unwrap that comes out of the SW API despite the change
apparent in the 3d view looking at SW Realview. Do your alterations in other cg applications. 
If your model is mostly 'boxy' or prismatic and the texture has nondescript detail you may not
notice poor unwraps too much in the render but in other cases the odd unwraps can be glaring or
otherwise unsatisfactory. In simple cases you might get away with just changing the X & Y texture
scale in Blender or Octane to suit rather than redo the unwrap.

There is an issue in SW2009 and probably later versions where the unwrap of cylindrical faces
is especially bad. You can sort of fix this in Blender in the Texture>Image Mapping panel by
using a Repeat of Y = 16x. It will still have other issues but this puts it back in the ballpark.
This can be similarly fixed in Octane by scaling 16x in the textures Y axis.

--->  All in all I suggest you redo anything other than basic texture mapping in Blender or
another cg app if you want to end up with quality renders.


### BLENDER:

While working on this project I discovered that the Blender 2.6 .obj import script has some
small deficiencies in how it translates materials which will generate unnecessary work for the
user to fix for each imported material. I hope to have this remedied officially but in the interum
I have included a modified IO script to get around these niggles. This is a direct substitute for
the one in the Blender.../Scripts/io_scen_obj folder. Rename the existing one first as __.py.old
to preserve it. This modified script may not be compatible with Blender 2.63 because of the
extent of changes made for bmesh.


**HAPPY RENDERING!! :)**
