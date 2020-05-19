# SolidWorks .OBJ Macro Version 2.0 ---> Blender 2.6
# a small script to load .obj from Blendercommand line after export from SW.

import bpy, sys

bpy.ops.import_scene.obj(filepath=sys.argv[-1])