import bpy

from multiprocessing import context
from bpy.types import Operator

from .gz_pivot_main import *



'''''''''''''''''''''''''''''''''''''''''''''''''''''
    
                     OPERATORS
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''

class cornerBtn(Operator):
    bl_idname = 'object.corner_btn'
    bl_label = 'Corner Button'
    bl_description = 'Set origin to BBox corner'
    
    btn_id: bpy.props.StringProperty(name="sample")
 
    def execute(self, context):
        myCorners = bboxCorners(self)
        setPivotCorners(self, self.btn_id, myCorners)
        return {'FINISHED'}


class centerBtn(Operator):
    bl_idname = 'object.center_btn'
    bl_label = 'Center Button'
    bl_description = 'Set origin to BBox face center'
    
    btn_id: bpy.props.StringProperty(name="sample")
 
    def execute(self, context):
        myFaceCenters = bboxFaceCenters(self)
        setPivotCenters(self, self.btn_id, myFaceCenters)
        return {'FINISHED'}

    
class CenterBounds(Operator):
    bl_idname = 'object.centerbounds'
    bl_label = 'CenterBounds'
    bl_description = 'Set origin to center bounds'
    btn_id = 'centerBounds'

    def execute(self, context):
        setPivotCenter(self, self.btn_id)
        return {'FINISHED'}

  
class CenterMass(Operator):
    bl_idname = 'object.centermass'
    bl_label = 'CenterMass'
    bl_description = 'Set origin to center mass'
    btn_id = 'centerMass'

    def execute(self, context):
        setPivotCenter(self, self.btn_id)
        return {'FINISHED'}


class Cursor(Operator):
    bl_idname = 'object.cursor'
    bl_label = '3D Cursor'
    bl_description = 'Set origin to 3D cursor'
    btn_id = 'cursor'

    def execute(self, context):
        setPivotCenter(self, self.btn_id)
        return {'FINISHED'}
    

class ClearSRL(Operator):
    bl_idname = 'object.clearsrl'
    bl_label = 'Clear SRL'
    bl_description = 'Reset Location and Rotation to 0,0,0. Reset Scale to 1'
    btn_id = 'clear_srl'

    def execute(self, context):
        clearSRL(self, self.btn_id)
        return {'FINISHED'}


class showBBoxBtn(Operator):
    bl_idname = 'object.show_bbox_btn'
    bl_label = 'Bounding Box'
    bl_description = 'Show Bounding box'

    def execute(self, context):
        showBBox(self)
        return {'FINISHED'}


class showCornerPointsBtn(Operator):
    bl_idname = 'object.show_cornerpoints_btn'
    bl_label = 'Corner Points ID'
    bl_description = 'Show Corner Points ID'

    def execute(self, context):
        showCornerPointsId(self, context)
        return {'FINISHED'}


class showCenterPointsBtn(Operator):
    bl_idname = 'object.show_centerpoints_btn'
    bl_label = 'Center Points ID'
    bl_description = 'Show Center Points ID'

    def execute(self, context):
        showFaceCenterPointsId(self, context)
        return {'FINISHED'}