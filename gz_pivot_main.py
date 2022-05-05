import bpy
import os
import math
import mathutils

from bpy.utils import ( register_class, 
                        unregister_class
                        )
                        
from bpy.props import ( StringProperty,
                        BoolProperty,
                        IntProperty,
                        FloatProperty,
                        FloatVectorProperty,
                        EnumProperty,
                        PointerProperty,
                       )

from bpy.types import ( #Panel,
                        AddonPreferences,
                        #Operator,
                        PropertyGroup,
                      )
                      
from mathutils import ( Vector )


# this must match the addon name, use '__package__'
# when defining this in a submodule of a python package.
addon_name = __name__       # when single file 
#addon_name = __package__   # when file in package 



'''''''''''''''''''''''''''''''''''''''''''''''''''''
    
        SETTINGS IN ADDON-PREFERENCES PANEL
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
# panel update function for PREFS_PT_MyPrefs panel 
def _update_panel_fnc (self, context):
    #
    # load addon custom-preferences 
    print( addon_name, ': update pref.panel function called' )
    #
    main_panel =  OBJECT_PT_MyPanel
    #
    main_panel .bl_category = context .preferences.addons[addon_name] .preferences.tab_label
    # re-register for update 
    unregister_class( main_panel )
    register_class( main_panel )


class PREFS_PT_MyPrefs( AddonPreferences ):
    
    #Custom Addon Preferences Panel - in addon activation panel - menu / edit / preferences / add-ons  

    bl_idname = addon_name

    tab_label: StringProperty(
            name="Tab Label",
            description="Choose a label-name for the panel tab",
            default="New Addon",
            update=_update_panel_fnc
    )

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        col = row.column()
        col.label(text="Tab Label:")
        col.prop(self, "tab_label", text="")

'''



'''''''''''''''''''''''''''''''''''''''''''''''''''''
    
                    FUNCTIONS
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''

def setPivotCorners(self, btn_id): 
    
    sel = bpy.context.selected_objects
    obj = bpy.context.active_object
    posx = obj.location.x
    posy = obj.location.y
    posz = obj.location.z
    pivotPos = (0,0,0)
    
    msg2 = "You have selected " + str(len(sel)) + " items. " + "Please select only 1 object"     
    
    if len(sel) >= 2:
        print(msg2)
        self.report({"ERROR"}, msg2)
    
    else:

        ### Multiply World Matrix by BBox corners
        bbox = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        ### Sort points by index 
        '''
        C0 = ( bbox[0].x - posx, bbox[0].y - posy, bbox[0].z - posz )
        C1 = ( bbox[1].x - posx, bbox[1].y - posy, bbox[1].z - posz )
        C2 = ( bbox[2].x - posx, bbox[2].y - posy, bbox[2].z - posz )
        C3 = ( bbox[3].x - posx, bbox[3].y - posy, bbox[3].z - posz )
        C4 = ( bbox[4].x - posx, bbox[4].y - posy, bbox[4].z - posz )
        C5 = ( bbox[5].x - posx, bbox[5].y - posy, bbox[5].z - posz )
        C6 = ( bbox[6].x - posx, bbox[6].y - posy, bbox[6].z - posz )
        C7 = ( bbox[7].x - posx, bbox[7].y - posy, bbox[7].z - posz )
        '''
        ### Sort points by face location
        C0 = ( bbox[0].x - posx, bbox[0].y - posy, bbox[0].z - posz )
        C1 = ( bbox[4].x - posx, bbox[4].y - posy, bbox[4].z - posz )
        C2 = ( bbox[7].x - posx, bbox[7].y - posy, bbox[7].z - posz )
        C3 = ( bbox[3].x - posx, bbox[3].y - posy, bbox[3].z - posz )
        C4 = ( bbox[1].x - posx, bbox[1].y - posy, bbox[1].z - posz )
        C5 = ( bbox[5].x - posx, bbox[5].y - posy, bbox[5].z - posz )
        C6 = ( bbox[6].x - posx, bbox[6].y - posy, bbox[6].z - posz )
        C7 = ( bbox[2].x - posx, bbox[2].y - posy, bbox[2].z - posz )
               
        ### Selection pivotPos from button
        if btn_id == "btn_c0":
            pivotPos = C0

        if btn_id == "btn_c1":
            pivotPos = C1
        
        if btn_id == "btn_c2":
            pivotPos = C2
            
        if btn_id == "btn_c3":
            pivotPos = C3
            
        if btn_id == "btn_c4":
            pivotPos = C4
        
        if btn_id == "btn_c5":
            pivotPos = C5
        
        if btn_id == "btn_c6":
            pivotPos = C6
        
        if btn_id == "btn_c7":
            pivotPos = C7
            
        ### Set origin with pivotPos
        bpy.context.scene.tool_settings.use_transform_data_origin = True
        bpy.ops.transform.translate(value=pivotPos)
        bpy.context.scene.tool_settings.use_transform_data_origin = False
        



def setPivotCenters(self, btn_id): 
    
    sel = bpy.context.selected_objects
    obj = bpy.context.active_object
    posx = obj.location.x
    posy = obj.location.y
    posz = obj.location.z
    pivotPos = (0,0,0)
    
    msg2 = "You have selected " + str(len(sel)) + " items. " + "Please select only 1 object"     
    
    if len(sel) >= 2:
        print(msg2)
        self.report({"ERROR"}, msg2)
    
    else:

        ### Multiply World Matrix by BBox corners
        bbox = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        ### Find center for each BBox face
        FC0 = ( (bbox[0].x + bbox[2].x) / 2 - posx, (bbox[0].y + bbox[2].y) / 2 - posy, (bbox[0].z + bbox[2].z) / 2 - posz )
        FC1 = ( (bbox[4].x + bbox[1].x) / 2 - posx, (bbox[4].y + bbox[1].y) / 2 - posy, (bbox[4].z + bbox[1].z) / 2 - posz )
        FC2 = ( (bbox[7].x + bbox[0].x) / 2 - posx, (bbox[7].y + bbox[0].y) / 2 - posy, (bbox[7].z + bbox[0].z) / 2 - posz )
        FC3 = ( (bbox[3].x + bbox[6].x) / 2 - posx, (bbox[3].y + bbox[6].y) / 2 - posy, (bbox[3].z + bbox[6].z) / 2 - posz )
        FC4 = ( (bbox[1].x + bbox[3].x) / 2 - posx, (bbox[1].y + bbox[3].y) / 2 - posy, (bbox[1].z + bbox[3].z) / 2 - posz )
        FC5 = ( (bbox[5].x + bbox[2].x) / 2 - posx, (bbox[5].y + bbox[2].y) / 2 - posy, (bbox[5].z + bbox[2].z) / 2 - posz )
    
        ### Selection pivotPos from button
        if btn_id == "btn_fc0":
            print(btn_id)
            pivotPos = FC0

        if btn_id == "btn_fc1":
            print(btn_id)
            pivotPos = FC1
        
        if btn_id == "btn_fc2":
            print(btn_id)
            pivotPos = FC2
           
        if btn_id == "btn_fc3":
            print(btn_id)
            pivotPos = FC3
            
        if btn_id == "btn_fc4":
            print(btn_id)
            pivotPos = FC4
        
        if btn_id == "btn_fc5":
            print(btn_id)
            pivotPos = FC5
          
        ### Set origin with pivotPos
        bpy.context.scene.tool_settings.use_transform_data_origin = True
        bpy.ops.transform.translate(value=pivotPos)
        bpy.context.scene.tool_settings.use_transform_data_origin = False
        
        


def setPivotCenter(btn_id): 
    
    sel = bpy.context.selected_objects
    
    for obj in sel:
        if btn_id == "centerBounds":
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
        
        if btn_id == "centerMass":
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
        
        if btn_id == "cursor":
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='BOUNDS')
 



def checkSelected(self, context):
    
    sel = bpy.context.selected_objects
    
    if not sel:
        self.report({"ERROR"}, "No objects selected")




def transformsOri(self, context):

    transformOri = bpy.context.scene.my_tool.transformOri
    
    if transformOri == "global":
        bpy.context.scene.transform_orientation_slots[0].type = 'GLOBAL'

    if transformOri == "local":
        bpy.context.scene.transform_orientation_slots[0].type = 'LOCAL'
        


def clearSRL(btn_id):
    sel = bpy.context.selected_objects
    for obj in sel:
        obj.location = (0,0,0)
        obj.rotation_euler = (0,0,0)
        obj.scale = (1,1,1)




'''''''''''''''''''''''''''''''''''''''''''''''''''''
    
        PROPERTIES VISIBLE IN THE ADDON-PANEL
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''

class PG_MyProperties (PropertyGroup):
     
    transformOri : bpy.props.EnumProperty(
        items=[
            ('global', 'Global', '', '', 0),
            ('local', 'Local', '', '', 1)
        ],
        default = 'global',
        description = "Set transforms orientation to",
        update = transformsOri
    )
    
    
    pivotToCenters1 : bpy.props.EnumProperty(
        items=[
            ('0', '0', '', '', 0),
            ('1', '1', '', '', 1),
            ('2', '2', '', '', 2)
        ],
    )
    
    pivotToCenters2 : bpy.props.EnumProperty(
        items=[
            ('3', '3', '', '', 0),
            ('4', '4', '', '', 1),
            ('5', '5', '', '', 2)
        ],
    )