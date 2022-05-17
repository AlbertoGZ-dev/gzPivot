from multiprocessing import context
import bpy

from bpy.types import Operator
from .gz_pivot_main import *



'''''''''''''''''''''''''''''''''''''''''''''''''''''
    
                     OPERATORS
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''

### Pivot To Corners OPs
class C0(Operator):
    bl_idname = 'object.c0'
    bl_label = 'C0'
    bl_description = 'Set origin to BBox corner'
    btn_id = 'btn_c0'

    def execute(self, context):
        myCorners = bboxCorners(self)
        setPivotCorners(self, self.btn_id, myCorners)
        return {'FINISHED'}


class C1(Operator):
    bl_idname = 'object.c1'
    bl_label = 'C1'
    bl_description = 'Set origin to BBox corner'
    btn_id = 'btn_c1'

    def execute(self, context):
        myCorners = bboxCorners(self)
        setPivotCorners(self, self.btn_id, myCorners)
        return {'FINISHED'}
       

class C2(Operator):
    bl_idname = 'object.c2'
    bl_label = 'C2'
    bl_description = 'Set origin to BBox corner'
    btn_id = 'btn_c2'

    def execute(self, context):
        myCorners = bboxCorners(self)
        setPivotCorners(self, self.btn_id, myCorners)
        return {'FINISHED'}
    

class C3(Operator):
    bl_idname = 'object.c3'
    bl_label = 'C3'
    bl_description = 'Set origin to BBox corner'
    btn_id = 'btn_c3'

    def execute(self, context):
        myCorners = bboxCorners(self)
        setPivotCorners(self, self.btn_id, myCorners)
        return {'FINISHED'}
    

class C4(Operator):
    bl_idname = 'object.c4'
    bl_label = 'C4'
    bl_description = 'Set origin to BBox corner'
    btn_id = 'btn_c4'

    def execute(self, context):
        myCorners = bboxCorners(self)
        setPivotCorners(self, self.btn_id, myCorners)
        return {'FINISHED'}


class C5(Operator):
    bl_idname = 'object.c5'
    bl_label = 'C5'
    bl_description = 'Set origin to BBox corner'
    btn_id = 'btn_c5'

    def execute(self, context):
        myCorners = bboxCorners(self)
        setPivotCorners(self, self.btn_id, myCorners)
        return {'FINISHED'}
    

class C6(Operator):
    bl_idname = 'object.c6'
    bl_label = 'C6'
    bl_description = 'Set origin to BBox corner'
    btn_id = 'btn_c6'

    def execute(self, context):
        myCorners = bboxCorners(self)
        setPivotCorners(self, self.btn_id, myCorners)
        return {'FINISHED'}
  
    
class C7(Operator):
    bl_idname = 'object.c7'
    bl_label = 'C7'
    bl_description = 'Set origin to BBox corner'
    btn_id = 'btn_c7'

    def execute(self, context):
        myCorners = bboxCorners(self)
        setPivotCorners(self, self.btn_id, myCorners)
        return {'FINISHED'}
    
    

### Pivot To Centers OPs
class FC0(Operator):
    bl_idname = 'object.fc0'
    bl_label = 'FC0'
    bl_description = 'Set origin to BBox face center'
    btn_id = 'btn_fc0'

    def execute(self, context):
        myFaceCenters = bboxFaceCenters(self)
        setPivotCenters(self, self.btn_id, myFaceCenters)
        return {'FINISHED'}
    

class FC1(Operator):
    bl_idname = 'object.fc1'
    bl_label = 'FC1'
    bl_description = 'Set origin to BBox face center'
    btn_id = 'btn_fc1'

    def execute(self, context):
        myFaceCenters = bboxFaceCenters(self)
        setPivotCenters(self, self.btn_id, myFaceCenters)
        return {'FINISHED'}
 
    
class FC2(Operator):
    bl_idname = 'object.fc2'
    bl_label = 'FC2'
    bl_description = 'Set origin to BBox face center'
    btn_id = 'btn_fc2'

    def execute(self, context):
        myFaceCenters = bboxFaceCenters(self)
        setPivotCenters(self, self.btn_id, myFaceCenters)
        return {'FINISHED'}


class FC3(Operator):
    bl_idname = 'object.fc3'
    bl_label = 'FC3'
    bl_description = 'Set origin to BBox face center'
    btn_id = 'btn_fc3'

    def execute(self, context):
        myFaceCenters = bboxFaceCenters(self)
        setPivotCenters(self, self.btn_id, myFaceCenters)
        return {'FINISHED'}


class FC4(Operator):
    bl_idname = 'object.fc4'
    bl_label = 'FC4'
    bl_description = 'Set origin to BBox face center'
    btn_id = 'btn_fc4'

    def execute(self, context):
        myFaceCenters = bboxFaceCenters(self)
        setPivotCenters(self, self.btn_id, myFaceCenters)
        return {'FINISHED'}


class FC5(Operator):
    bl_idname = 'object.fc5'
    bl_label = 'FC5'
    bl_description = 'Set origin to BBox face center'
    btn_id = 'btn_fc5'

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