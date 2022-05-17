import bpy
import textwrap

from ast import Global
from ctypes import alignment
from bpy.types import Panel
from .gz_pivot_ops import *



'''''''''''''''''''''''''''''''''''''''''''''''''''''
    
        ADDON-PANEL-VISIBLE IN OBJECT CONTEXT
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''


class OBJECT_PT_MyPanel (Panel):
    bl_idname = 'OBJECT_PT_MyPanel'
    bl_label = 'GZ Pivot'
    bl_space_type = 'VIEW_3D'   
    bl_region_type = 'UI'
    bl_category = 'GZ Pivot'  # note: replaced by preferences-setting in register function 
    bl_context = 'objectmode'
   
    

    '''
    def __init(self):
        super( self, Panel ).__init__()
        bl_category = bpy.context.preferences.addons[__name__].preferences.category 
    '''
    
    
    
    @classmethod
    def poll(self,context):
        return context.object is not None

    
        
    def draw(self, context):
        layout = self.layout
        layout.scale_x = 10
        scene = context.scene
        mytool = scene.my_tool

        row1 = layout.grid_flow(columns=2, row_major=True, align=True)
        row1.scale_y = 1.5
        row1.prop(mytool, 'transformOri', expand=True)
        
        row2 = layout.grid_flow(columns=1, row_major=True, align=True)
        row2.operator(ClearSRL.bl_idname, text='Center to World')

        row3 = layout.row()
        row3.label(text='Show:')

        row4 = layout.grid_flow(columns=1, row_major=True, align=True)
        row4.operator(showBBoxBtn.bl_idname, text='Bounding Box', depress=GlobalsMain.bbox_btn_depress)

        row5 = layout.grid_flow(columns=1, row_major=True, align=True)
        row5.operator(showCornerPointsBtn.bl_idname, text='Corner Points ID', depress=GlobalsMain.cornerpoints_btn_depress)

        row6 = layout.grid_flow(columns=1, row_major=True, align=True)
        row6.operator(showCenterPointsBtn.bl_idname, text='Center Points ID', depress=GlobalsMain.centerpoints_btn_depress)
        

 
        
class SUBPANEL_PT_PivotToCorners (Panel):
    bl_idname = 'SUBPANEL_PT_PivotToCorners'
    bl_label = 'Pivot to Corners'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'OBJECT_PT_MyPanel'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        pcoll = preview_collections['main']
        
        ### Icons collection
        corner_0 = pcoll['corner_0']
        corner_1 = pcoll['corner_1']
        corner_2 = pcoll['corner_2']
        corner_3 = pcoll['corner_3']
        corner_4 = pcoll['corner_4']
        corner_5 = pcoll['corner_5']
        corner_6 = pcoll['corner_6']
        corner_7 = pcoll['corner_7']          
              
        ### Pivot to Corners (Layout Items)
        row11 = layout.grid_flow(columns=4, row_major=True, align=True)
        row11.scale_y = 1.0
        row11.template_icon(icon_value=corner_4.icon_id, scale=3)
        row11.template_icon(icon_value=corner_5.icon_id, scale=3)
        row11.template_icon(icon_value=corner_6.icon_id, scale=3)
        row11.template_icon(icon_value=corner_7.icon_id, scale=3)
        
        row12 = layout.grid_flow(columns=4, row_major=True, align=True)
        row12.scale_y = 1.0
        row12.operator(C4.bl_idname, text='4', emboss=True)
        row12.operator(C5.bl_idname, text='5', emboss=True)
        row12.operator(C6.bl_idname, text='6', emboss=True)
        row12.operator(C7.bl_idname, text='7', emboss=True)
        row12.operator(C0.bl_idname, text='0', emboss=True)
        row12.operator(C1.bl_idname, text='1', emboss=True)
        row12.operator(C2.bl_idname, text='2', emboss=True)
        row12.operator(C3.bl_idname, text='3', emboss=True)
        
        row13 = layout.grid_flow(columns=4, row_major=True, align=True)
        row13.scale_y = 1.0
        row13.template_icon(icon_value=corner_0.icon_id, scale=3)
        row13.template_icon(icon_value=corner_1.icon_id, scale=3)
        row13.template_icon(icon_value=corner_2.icon_id, scale=3)
        row13.template_icon(icon_value=corner_3.icon_id, scale=3)
           
        
preview_collections = {}        
        


                  
class SUBPANEL_PT_PivotToCenters (Panel):
    bl_idname = 'SUBPANEL_PT_PivotToCenters'
    bl_label = 'Pivot to Centers'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'OBJECT_PT_MyPanel'
    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        pcoll = preview_collections['main']
        
        ### Icons collection
        face_center_0 = pcoll['face_center_0']
        face_center_1 = pcoll['face_center_1']
        face_center_2 = pcoll['face_center_2']
        face_center_3 = pcoll['face_center_3']
        face_center_4 = pcoll['face_center_4']
        face_center_5 = pcoll['face_center_5']
    
        ### Pivot to Centers (Layout Items)
        row22 = layout.grid_flow(columns=4, row_major=True, align=True)
        row22.scale_y = 1.0
        row22.template_icon(icon_value=face_center_3.icon_id, scale=2.5)
        row22.template_icon(icon_value=face_center_4.icon_id, scale=2.5)
        row22.template_icon(icon_value=face_center_5.icon_id, scale=2.5)

        row21 = layout.grid_flow(columns=4, row_major=True, align=True)
        row21.scale_y = 1.0
        row21.operator(FC3.bl_idname, text='3')
        row21.operator(FC4.bl_idname, text='4')
        row21.operator(FC5.bl_idname, text='5')
        row21.operator(FC0.bl_idname, text='0')
        row21.operator(FC1.bl_idname, text='1')
        row21.operator(FC2.bl_idname, text='2')

        row23 = layout.row(align=True)
        row23.scale_y = 1.0
        row23.template_icon(icon_value=face_center_0.icon_id, scale=2.5)
        row23.template_icon(icon_value=face_center_1.icon_id, scale=2.5)
        row23.template_icon(icon_value=face_center_2.icon_id, scale=2.5)   
        
        row25 = layout.grid_flow(columns=2, row_major=True, align=True)
        row25.scale_y = 1.0
        row25.operator(CenterBounds.bl_idname, text='Center (bounds)')
        row25.operator(CenterMass.bl_idname, text='Center (mass)')


        

class SUBPANEL_PT_PivotTo3Dcursor (Panel):
    bl_idname = 'SUBPANEL_PT_PivotTo3Dcursor'
    bl_label = 'Pivot to 3D Cursor'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'OBJECT_PT_MyPanel'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        ### Pivot to 3D Cursor
        row41 = layout.grid_flow(columns=4, row_major=True)
        row41.operator(Cursor.bl_idname, text='3D Cursor')
        
        


class SUBPANEL_PT_About (Panel):
    bl_idname = 'SUBPANEL_PT_About'
    bl_label = 'About'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = 'OBJECT_PT_MyPanel'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        ### About
        row90 = layout.row(align=True)
        row90.alignment = 'CENTER'
        row90.label(text='GZ Pivot v0.1.1')

        row91 = layout.row(align=True)
        row91.alignment = 'CENTER'
        row91.label(text='by Alberto GZ')
        row91.separator()
        #
        row92 = layout.row(align=True)
        text = 'GZ Privot helps to set origin on objects in easy and quick way'      
        
        def label_multiline(context, text, parent):
            chars = int(context.region.width / 13)
            wrapper = textwrap.TextWrapper(width=chars)
            text_lines = wrapper.wrap(text=text)
            for text_line in text_lines:
                parent.label(text=text_line)

        label_multiline(
            context=context,
            text=text,
            parent=layout
        )