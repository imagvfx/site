# encoding: utf-8

import os
import bpy

scene = os.environ["SCENE"]

bpy.ops.wm.save_as_mainfile(filepath=scene)
