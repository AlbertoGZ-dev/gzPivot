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
   
    # def __init(self):
    #     super( self, Panel ).__init__()
    #     bl_category = bpy.context.preferences.addons[__name__].preferences.category 
    
    # @classmethod
    # def poll(self,context):
    #     return context.object is not None
  
    def draw(self, context):
        layout = self.layout
        layout.scale_x = 10
        scene = context.scene
        mytool = scene.my_tool

        row1 = layout.grid_flow(columns=2, row_major=True, align=True)
        row1.scale_y = 1.5
        row1.prop(mytool, 'transformOri', expand=True)
        
        row2 = layout.grid_flow(columns=1, row_major=True, align=True)
        row2.operator('btn.reset_location', text='Center to World')

        row3 = layout.row()
        row3.label(text='Show:')

        row4 = layout.grid_flow(columns=1, row_major=True, align=True)
        row4.operator('btn.show_bbox', text='Bounding Box', depress=GlobalsMain.bbox_btn_depress)

        row5a = layout.row()
        row5a.label(text='Show Points ID:')

        row5 = layout.grid_flow(columns=1, row_major=True, align=True)
        row5.operator('btn.show_cornerpoints', text='Corners', depress=GlobalsMain.cornerpoints_btn_depress)

        row6 = layout.grid_flow(columns=1, row_major=True, align=True)
        row6.operator('btn.show_centerpoints', text='Face Centers', depress=GlobalsMain.centerpoints_btn_depress)

        row7 = layout.grid_flow(columns=1, row_major=True, align=True)
        row7.operator('btn.show_midpoints', text='Middle Edges', depress=GlobalsMain.midpoints_btn_depress)
        

 
        
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
        row12.operator('btn.corners', text='4').btn_id = 'btn_c4'
        row12.operator('btn.corners', text='5').btn_id = 'btn_c5'
        row12.operator('btn.corners', text='6').btn_id = 'btn_c6'
        row12.operator('btn.corners', text='7').btn_id = 'btn_c7'
        row12.operator('btn.corners', text='0').btn_id = 'btn_c0'
        row12.operator('btn.corners', text='1').btn_id = 'btn_c1'
        row12.operator('btn.corners', text='2').btn_id = 'btn_c2'
        row12.operator('btn.corners', text='3').btn_id = 'btn_c3'
        
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
        row21.operator('btn.centers', text='3').btn_id = 'btn_fc3'
        row21.operator('btn.centers', text='4').btn_id = 'btn_fc4'
        row21.operator('btn.centers', text='5').btn_id = 'btn_fc5'
        row21.operator('btn.centers', text='0').btn_id = 'btn_fc0'
        row21.operator('btn.centers', text='1').btn_id = 'btn_fc1'
        row21.operator('btn.centers', text='2').btn_id = 'btn_fc2'

        row23 = layout.row(align=True)
        row23.scale_y = 1.0
        row23.template_icon(icon_value=face_center_0.icon_id, scale=2.5)
        row23.template_icon(icon_value=face_center_1.icon_id, scale=2.5)
        row23.template_icon(icon_value=face_center_2.icon_id, scale=2.5)   
        
        row25 = layout.grid_flow(columns=2, row_major=True, align=True)
        row25.scale_y = 1.0
        row25.operator('btn.center_bounds', text='Center (bounds)')
        row25.operator('btn.center_mass', text='Center (mass)')




class SUBPANEL_PT_PivotToMidEdges(Panel):
    bl_idname = 'SUBPANEL_PT_PivotToMidEdges'
    bl_label = 'Pivot to Middle Edges'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_parent_id = 'OBJECT_PT_MyPanel'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        pcoll = preview_collections['main']

        ### Icons collection
        mid_edge_0 = pcoll['mid_edge_0']
        mid_edge_1 = pcoll['mid_edge_1']
        mid_edge_2 = pcoll['mid_edge_2']
        mid_edge_3 = pcoll['mid_edge_3']
        mid_edge_4 = pcoll['mid_edge_4']
        mid_edge_5 = pcoll['mid_edge_5']
        mid_edge_6 = pcoll['mid_edge_6']
        mid_edge_7 = pcoll['mid_edge_7']
        mid_edge_8 = pcoll['mid_edge_8']
        mid_edge_9 = pcoll['mid_edge_9']
        mid_edge_10 = pcoll['mid_edge_10']
        mid_edge_11 = pcoll['mid_edge_11']

        ### Pivot to Mid Edges (Layout Items)
        row35 = layout.grid_flow(columns=4, row_major=True, align=True)
        row35.scale_y = 1.0
        row35.template_icon(icon_value=mid_edge_8.icon_id, scale=2.5)
        row35.template_icon(icon_value=mid_edge_9.icon_id, scale=2.5)
        row35.template_icon(icon_value=mid_edge_10.icon_id, scale=2.5)
        row35.template_icon(icon_value=mid_edge_11.icon_id, scale=2.5)

        row34 = layout.grid_flow(columns=4, row_major=True, align=True)
        row34.scale_y = 1.0
        row34.operator('btn.mid_edges', text='8').btn_id = 'btn_mid8'
        row34.operator('btn.mid_edges', text='9').btn_id = 'btn_mid9'
        row34.operator('btn.mid_edges', text='10').btn_id = 'btn_mid10'
        row34.operator('btn.mid_edges', text='11').btn_id = 'btn_mid11'

        layout.separator(factor=2.0)
        row33 = layout.grid_flow(columns=4, row_major=True, align=True)
        row33.scale_y = 1.0
        row33.template_icon(icon_value=mid_edge_4.icon_id, scale=2.5)
        row33.template_icon(icon_value=mid_edge_5.icon_id, scale=2.5)
        row33.template_icon(icon_value=mid_edge_6.icon_id, scale=2.5)
        row33.template_icon(icon_value=mid_edge_7.icon_id, scale=2.5)

        row32 = layout.grid_flow(columns=4, row_major=True, align=True)
        row32.scale_y = 1.0
        row32.operator('btn.mid_edges', text='4').btn_id = 'btn_mid4'
        row32.operator('btn.mid_edges', text='5').btn_id = 'btn_mid5'
        row32.operator('btn.mid_edges', text='6').btn_id = 'btn_mid6'
        row32.operator('btn.mid_edges', text='7').btn_id = 'btn_mid7'
        
        layout.separator(factor=2.0)
        row31 = layout.grid_flow(columns=4, row_major=True, align=True)
        row31.scale_y = 1.0
        row31.template_icon(icon_value=mid_edge_0.icon_id, scale=2.5)
        row31.template_icon(icon_value=mid_edge_1.icon_id, scale=2.5)
        row31.template_icon(icon_value=mid_edge_2.icon_id, scale=2.5)
        row31.template_icon(icon_value=mid_edge_3.icon_id, scale=2.5)

        row30 = layout.grid_flow(columns=4, row_major=True, align=True)
        row30.scale_y = 1.0
        row30.operator('btn.mid_edges', text='0').btn_id = 'btn_mid0'
        row30.operator('btn.mid_edges', text='1').btn_id = 'btn_mid1'
        row30.operator('btn.mid_edges', text='2').btn_id = 'btn_mid2'
        row30.operator('btn.mid_edges', text='3').btn_id = 'btn_mid3'

        
      
        
       
        


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
        row41.operator('btn.cursor', text='3D Cursor')
        
        


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
        row90.label(text='GZ Pivot v0.1.2')

        row91 = layout.row(align=True)
        row91.alignment = 'CENTER'
        row91.label(text='by Alberto GZ')
        row91.separator()
        
        row92 = layout.row(align=True)
        row92.alignment = 'CENTER'
        text = 'GZ Privot helps to set origin on objects in easy and quick way'      
        
        def label_multiline(context, text, parent):
            chars = int(context.region.width / 8.5)
            wrapper = textwrap.TextWrapper(width=chars)
            text_lines = wrapper.wrap(text=text)
            for text_line in text_lines:
                parent.label(text=text_line)

        label_multiline(
            context=context,
            text=text,
            parent=layout
        )