import bpy

from multiprocessing import context
from bpy.types import Operator

from .gz_pivot_main import *



'''''''''''''''''''''''''''''''''''''''''''''''''''''
    
                     OPERATORS
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''

class CornersBtn(Operator):
    bl_idname = 'btn.corners'
    bl_label = 'Corners'
    bl_description = 'Set origin to BBox corner'
    btn_id: bpy.props.StringProperty(name='')
   
    def execute(self, context):
        setPivotCorners(self, self.btn_id)
        return {'FINISHED'}


class CentersBtn(Operator):
    bl_idname = 'btn.centers'
    bl_label = 'Centers'
    bl_description = 'Set origin to BBox face center'
    btn_id: bpy.props.StringProperty(name='')
 
    def execute(self, context):
        setPivotCenters(self, self.btn_id)
        return {'FINISHED'}


class MidEdgesBtn(Operator):
    bl_idname = 'btn.mid_edges'
    bl_label = 'Middle Edges'
    bl_description = 'Set origin to BBox middle edges'
    btn_id: bpy.props.StringProperty(name='')

    def execute(self, context):
        setPivotMidEdges(self, self.btn_id)
        return {'FINISHED'}

    
class CenterBoundsBtn(Operator):
    bl_idname = 'btn.center_bounds'
    bl_label = 'Center Bounds'
    bl_description = 'Set origin to center bounds'
    btn_id = 'center_bounds'

    def execute(self, context):
        setPivotCenter(self, self.btn_id)
        return {'FINISHED'}

  
class CenterMassBtn(Operator):
    bl_idname = 'btn.center_mass'
    bl_label = 'Center Mass'
    bl_description = 'Set origin to center mass'
    btn_id = 'center_mass'

    def execute(self, context):
        setPivotCenter(self, self.btn_id)
        return {'FINISHED'}


class CursorBtn(Operator):
    bl_idname = 'btn.cursor'
    bl_label = '3D Cursor'
    bl_description = 'Set origin to 3D cursor'
    btn_id = 'cursor'

    def execute(self, context):
        setPivotCenter(self, self.btn_id)
        return {'FINISHED'}
    

class ResetLocationBtn(Operator):
    bl_idname = 'btn.reset_location'
    bl_label = 'Reset Location'
    bl_description = 'Reset Location and Rotation to 0,0,0. Reset Scale to 1'
    btn_id = 'reset_location'

    def execute(self, context):
        resetLocation(self, self.btn_id)
        return {'FINISHED'}


class ShowBBoxBtn(Operator):
    bl_idname = 'btn.show_bbox'
    bl_label = 'Bounding Box'
    bl_description = 'Show Bounding box'

    def execute(self, context):
        showBBox(self)
        return {'FINISHED'}


class ShowCornerPointsBtn(Operator):
    bl_idname = 'btn.show_cornerpoints'
    bl_label = 'Corner Points ID'
    bl_description = 'Show Corner Points ID'

    def execute(self, context):
        showCornerPointsId(self, context)
        return {'FINISHED'}


class ShowCenterPointsBtn(Operator):
    bl_idname = 'btn.show_centerpoints'
    bl_label = 'Center Points ID'
    bl_description = 'Show Center Points ID'

    def execute(self, context):
        showFaceCenterPointsId(self, context)
        return {'FINISHED'}


class ShowMidEdgesBtn(Operator):
    bl_idname = 'btn.show_midpoints'
    bl_label = 'Middle Points ID'
    bl_description = 'Show Middle Edges Points ID'

    def execute(self, context):
        showMidEdgesPointsId(self, context)
        return {'FINISHED'}