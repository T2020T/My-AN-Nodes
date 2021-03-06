import bpy
from bpy.props import *
from ... base_types import AnimationNode

class GetBoneNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_GetBoneNode"
    bl_label = "Bone From Armature Object"
    bl_width_default = 220

    Search = StringProperty(name = "Search String")
    message1 = StringProperty()

    def draw(self, layout):
        layout.prop(self, "Search")
        if (self.message1 != ""):
            layout.label(self.message1, icon = "INFO")

    def create(self):
        self.newInput("Object", "Armature", "arm")
        self.newOutput("Bone", "Single Bone", "bone_ob")

    def execute(self, arm):
        if arm is None:
            return

        if arm.type == "ARMATURE":
            if self.Search != "":
                boneList = [item for item in arm.pose.bones if item.name.startswith(self.Search)]
            else:
                boneList = arm.pose.bones
            self.message1 = "First Bone of " + str(len(boneList)) + " match(es)"
            if boneList:
                bone_ob = boneList[0]
            else:
                bone_ob = None
                self.message1 = "No Matches"
            return bone_ob
