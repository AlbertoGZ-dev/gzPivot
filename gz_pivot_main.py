
from sre_parse import State
import bpy
import functools
import re

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

from bpy.types import ( Panel,
                        AddonPreferences,
                        Operator,
                        PropertyGroup,
                      )
                      
from mathutils import ( Vector,
                        Matrix
                        )

from bpy_extras.io_utils import axis_conversion





# this must match the addon name, use '__package__'
# when defining this in a submodule of a python package.
#addon_name = __name__       # when single file 
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
            name='Tab Label',
            description='Choose a label-name for the panel tab',
            default='New Addon',
            update=_update_panel_fnc
    )

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        col = row.column()
        col.label(text='Tab Label:')
        col.prop(self, 'tab_label', text='')
'''





'''''''''''''''''''''''''''''''''''''''''''''''''''''
    
                    FUNCTIONS
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''

class GlobalsMain():
    bbox_btn_depress = False
    cornerpoints_btn_depress = False
    centerpoints_btn_depress = False
    white = (1.0, 1.0, 1.0)
    red = (1.0, 0.1, 0.2)
    green = (0.0, 1.0, 0.0)
    blue = (0.1, 0.3, 1.0)
    cyan = (0.0, 1.0, 1.0)
    magenta = (1.0, 0.0, 1.0)
    yellow = (1.0, 1.0, 0.0)



def bboxCorners(self):
    sel = bpy.context.selected_objects
    
    for obj in sel:

        posx = obj.location.x
        posy = obj.location.y
        posz = obj.location.z

        ### Multiply World Matrix by BBox corners
        bbox = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        corners = {
                    # Corners World
                    'CW0': (bbox[0].x - posx, bbox[0].y - posy, bbox[0].z - posz),
                    'CW1': (bbox[4].x - posx, bbox[4].y - posy, bbox[4].z - posz),
                    'CW2': (bbox[7].x - posx, bbox[7].y - posy, bbox[7].z - posz),
                    'CW3': (bbox[3].x - posx, bbox[3].y - posy, bbox[3].z - posz),
                    'CW4': (bbox[1].x - posx, bbox[1].y - posy, bbox[1].z - posz),
                    'CW5': (bbox[5].x - posx, bbox[5].y - posy, bbox[5].z - posz),
                    'CW6': (bbox[6].x - posx, bbox[6].y - posy, bbox[6].z - posz),
                    'CW7': (bbox[2].x - posx, bbox[2].y - posy, bbox[2].z - posz),
                    # Corners Local
                    'CL0': (bbox[0].x, bbox[0].y, bbox[0].z),
                    'CL1': (bbox[4].x, bbox[4].y, bbox[4].z),
                    'CL2': (bbox[7].x, bbox[7].y, bbox[7].z),
                    'CL3': (bbox[3].x, bbox[3].y, bbox[3].z),
                    'CL4': (bbox[1].x, bbox[1].y, bbox[1].z),
                    'CL5': (bbox[5].x, bbox[5].y, bbox[5].z),
                    'CL6': (bbox[6].x, bbox[6].y, bbox[6].z),
                    'CL7': (bbox[2].x, bbox[2].y, bbox[2].z)
                     
        }
        return corners




def bboxFaceCenters(self):
    sel = bpy.context.selected_objects
    
    for obj in sel:

        posx = obj.location.x
        posy = obj.location.y
        posz = obj.location.z

        ### Multiply World Matrix by BBox corners
        bbox = [obj.matrix_world @ Vector(corner) for corner in obj.bound_box]
        
        faceCenters = {
                        # Face Centers World
                        'FCW0': ( (bbox[0].x + bbox[2].x) / 2 - posx, (bbox[0].y + bbox[2].y) / 2 - posy, (bbox[0].z + bbox[2].z) / 2 - posz ),
                        'FCW1': ( (bbox[4].x + bbox[1].x) / 2 - posx, (bbox[4].y + bbox[1].y) / 2 - posy, (bbox[4].z + bbox[1].z) / 2 - posz ),
                        'FCW2': ( (bbox[7].x + bbox[0].x) / 2 - posx, (bbox[7].y + bbox[0].y) / 2 - posy, (bbox[7].z + bbox[0].z) / 2 - posz ),
                        'FCW3': ( (bbox[4].x + bbox[6].x) / 2 - posx, (bbox[4].y + bbox[6].y) / 2 - posy, (bbox[4].z + bbox[6].z) / 2 - posz ),
                        'FCW4': ( (bbox[3].x + bbox[6].x) / 2 - posx, (bbox[3].y + bbox[6].y) / 2 - posy, (bbox[3].z + bbox[6].z) / 2 - posz ),
                        'FCW5': ( (bbox[5].x + bbox[2].x) / 2 - posx, (bbox[5].y + bbox[2].y) / 2 - posy, (bbox[5].z + bbox[2].z) / 2 - posz ),
                        # Face Centers Local
                        'FCL0': ( (bbox[0].x + bbox[2].x) / 2, (bbox[0].y + bbox[2].y) / 2, (bbox[0].z + bbox[2].z) / 2 ),
                        'FCL1': ( (bbox[4].x + bbox[1].x) / 2, (bbox[4].y + bbox[1].y) / 2, (bbox[4].z + bbox[1].z) / 2 ),
                        'FCL2': ( (bbox[7].x + bbox[0].x) / 2, (bbox[7].y + bbox[0].y) / 2, (bbox[7].z + bbox[0].z) / 2 ),
                        'FCL3': ( (bbox[4].x + bbox[6].x) / 2, (bbox[4].y + bbox[6].y) / 2, (bbox[4].z + bbox[6].z) / 2 ),
                        'FCL4': ( (bbox[3].x + bbox[6].x) / 2, (bbox[3].y + bbox[6].y) / 2, (bbox[3].z + bbox[6].z) / 2 ),
                        'FCL5': ( (bbox[5].x + bbox[2].x) / 2, (bbox[5].y + bbox[2].y) / 2, (bbox[5].z + bbox[2].z) / 2 )
                    
        }
        return faceCenters




def checkSelected(self):
    sel = bpy.context.selected_objects
    
    if len(sel) == 0:
        self.report({'ERROR'}, 'No objects selected')
        state = 'NONE' 
    
    elif len(sel) >= 2:
        self.report({'ERROR'}, 'You have selected ' + str(len(sel)) + ' items. ' + 'Maybe works with only 1 object')
        state = 'LOCK' 

    elif len(sel) == 1:
        state = 'VALID' 
    
    return state 




def setOriginToPivotPos(pivotPos):
    transformOri = bpy.context.scene.my_tool.transformOri

    bpy.context.scene.transform_orientation_slots[0].type = 'GLOBAL'
    bpy.context.scene.tool_settings.use_transform_data_origin = True
    bpy.ops.transform.translate(value=pivotPos)
    bpy.context.scene.tool_settings.use_transform_data_origin = False 
    
    if transformOri == 'local':
            bpy.context.scene.transform_orientation_slots[0].type = 'LOCAL'
    else:
            bpy.context.scene.transform_orientation_slots[0].type = 'GLOBAL'




def setPivotCorners(self, btn_id, corners): 

    if checkSelected(self) == 'VALID':

        ### Select 'pivotPos' from button
        if btn_id == 'btn_c0':
            pivotPos = corners['CW0']

        if btn_id == 'btn_c1':
            pivotPos = corners['CW1']
           
        if btn_id == 'btn_c2':
            pivotPos = corners['CW2']
            
        if btn_id == 'btn_c3':
            pivotPos = corners['CW3']
            
        if btn_id == 'btn_c4':
            pivotPos = corners['CW4']
        
        if btn_id == 'btn_c5':
            pivotPos = corners['CW5']
        
        if btn_id == 'btn_c6':
            pivotPos = corners['CW6']
        
        if btn_id == 'btn_c7':
            pivotPos = corners['CW7']

        ### Set origin with pivotPos
        if GlobalsMain.cornerpoints_btn_depress == True:
            deleteCornerPointsId(self)
            setOriginToPivotPos(pivotPos)
            createCornerPointsId(self)
        else:
            setOriginToPivotPos(pivotPos)
        
        if GlobalsMain.centerpoints_btn_depress == True:
            deleteFaceCenterPointsId(self)
            createFaceCenterPointsId(self)
        
        ### Show BBox during a short time
        if GlobalsMain.bbox_btn_depress == False:
            showBBoxTemp()
        if GlobalsMain.bbox_btn_depress == False:
            pivotMarker(x=0, color=(GlobalsMain.red[0],GlobalsMain.red[1],GlobalsMain.red[2]))
        else:
            pivotMarker(x=0, color=(GlobalsMain.red[0],GlobalsMain.red[1],GlobalsMain.red[2]))

        ### Hightlight the pivot marker
            pivotMarker(x=0, color=(GlobalsMain.red[0],GlobalsMain.red[1],GlobalsMain.red[2]))
    
        return self, pivotPos
 



def setPivotCenters(self, btn_id, faceCenters):

    if checkSelected(self) == 'VALID':

        ### Select 'pivotPos' from button
        if btn_id == 'btn_fc0':
            pivotPos = faceCenters['FCW0']

        if btn_id == 'btn_fc1':
            pivotPos = faceCenters['FCW1']
        
        if btn_id == 'btn_fc2':
            pivotPos = faceCenters['FCW2']
        
        if btn_id == 'btn_fc3':
            pivotPos = faceCenters['FCW3']
            
        if btn_id == 'btn_fc4':
            pivotPos = faceCenters['FCW4']
        
        if btn_id == 'btn_fc5':
            pivotPos = faceCenters['FCW5']
        
        ### Set origin with pivotPos
        if GlobalsMain.centerpoints_btn_depress == True:
            deleteFaceCenterPointsId(self)
            setOriginToPivotPos(pivotPos)
            createFaceCenterPointsId(self)
        else:
            setOriginToPivotPos(pivotPos)

        if GlobalsMain.cornerpoints_btn_depress == True:
            deleteCornerPointsId(self)
            createCornerPointsId(self)
        

        ### Show BBox during a short time
        if GlobalsMain.bbox_btn_depress == False:
            showBBoxTemp()
        if GlobalsMain.bbox_btn_depress == False:
            pivotMarker(x=0, color=(GlobalsMain.blue[0],GlobalsMain.blue[1],GlobalsMain.blue[2]))
        else:
            pivotMarker(x=0, color=(GlobalsMain.blue[0],GlobalsMain.blue[1],GlobalsMain.blue[2]))

        ### Hightlight the pivot marker
            pivotMarker(x=0, color=(GlobalsMain.blue[0],GlobalsMain.blue[1],GlobalsMain.blue[2]))
        
        

def setPivotCenter(self, btn_id): 
    sel = bpy.context.selected_objects

    if checkSelected(self) == 'VALID':

        ### Show BBox during a few time
        if GlobalsMain.bbox_btn_depress == False:
            showBBoxTemp()
        
        if GlobalsMain.bbox_btn_depress == False:
            pivotMarker(x=0, color=(GlobalsMain.blue[0],GlobalsMain.blue[1],GlobalsMain.blue[2]))
        else:
            pivotMarker(x=0, color=(GlobalsMain.blue[0],GlobalsMain.blue[1],GlobalsMain.blue[2]))
        

        for obj in sel:
            obj.show_bounds = True
            if btn_id == 'centerBounds':
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
            
            if btn_id == 'centerMass':
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            
            if btn_id == 'cursor':
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='BOUNDS')




def transformsOri(self, context):
    transformOri = bpy.context.scene.my_tool.transformOri
    
    if transformOri == 'global':
        bpy.context.scene.transform_orientation_slots[0].type = 'GLOBAL'

    if transformOri == 'local':
        bpy.context.scene.transform_orientation_slots[0].type = 'LOCAL'




def clearSRL(self, btn_id):
    sel = bpy.context.selected_objects
    
    if checkSelected(self) != 'NONE':
        
        for obj in sel:
            obj.location = (0,0,0)
            obj.rotation_euler = (0,0,0)
            obj.scale = (1,1,1)



def showBBox(self):
    sel = bpy.context.selected_objects
  
    if checkSelected(self) == 'VALID':

        for obj in sel:
            if obj.show_bounds == False:
                obj.show_bounds = True
                GlobalsMain.bbox_btn_depress = True
            else:          
                obj.show_bounds = False
                GlobalsMain.bbox_btn_depress = False
   


def showBBoxTemp(x=0):
    bpy.context.object.show_bounds = False
    x += 1
    if(x < 2): # Run after 1 second
        bpy.app.timers.register(functools.partial(showBBoxTemp,x), first_interval=1)
        bpy.context.object.show_bounds = True


    
def pivotMarker(x, color):
    x = x
    color = color
    bpy.context.preferences.themes[0].view_3d.object_origin_size = 5
    bpy.context.preferences.themes[0].view_3d.object_active = (1.0, 0.5, 0.0)

    x += 1
    if(x < 2): # Run after 1 second
        bpy.app.timers.register(functools.partial(pivotMarker,x, color), first_interval=1)
        bpy.context.preferences.themes[0].view_3d.object_origin_size = 10
        bpy.context.preferences.themes[0].view_3d.object_active = (color[0], color[1], color[2])
      
    


def createCornerPointsId(self):
    active_obj = bpy.context.active_object
    myCorners = bboxCorners(self)

    # Create collection for empties
    collection = bpy.data.collections.new('CornersColl')
    bpy.context.scene.collection.children.link(collection)
    
    for i in range(0, 8):
        name = ('CL'+str(i))
        loc = myCorners['CL'+str(i)]
        # Template for Empty 
        name = bpy.data.objects.new(' '+str(i), None) #Name of empty obj
        bpy.data.collections['CornersColl'].objects.link( name )
        name.empty_display_size = 0.005
        name.empty_display_type = 'SPHERE'
        name.show_in_front = True
        name.show_name = True
        name.location = loc
        name.parent = active_obj
        name.matrix_parent_inverse = active_obj.matrix_world.inverted()

    # Set wirecolor to custom color
    bpy.context.preferences.themes[0].view_3d.empty = (0.0, 1.0, 1.0)

    # Hide relationship lines
    bpy.context.space_data.overlay.show_relationship_lines = False



def deleteCornerPointsId(self):

    #pattern = re.compile('CornersColl*')

    for colls in bpy.data.collections:
        if colls.name == 'CornersColl':

            # Remove collection and children items
            collection = bpy.data.collections.get('CornersColl')
            for obj in collection.objects:
                bpy.data.objects.remove(obj, do_unlink=True)
            bpy.data.collections.remove(collection)
    
    # Set wirecolor to default color
    bpy.context.preferences.themes[0].view_3d.empty = (0.0, 0.0, 0.0)




def showCornerPointsId(self, context):
    sel = bpy.context.selected_objects

    if checkSelected(self) == 'VALID':

        if GlobalsMain.cornerpoints_btn_depress == False:
            createCornerPointsId(self)
            GlobalsMain.cornerpoints_btn_depress = True
            
        elif GlobalsMain.cornerpoints_btn_depress == True:
            deleteCornerPointsId(self)
            GlobalsMain.cornerpoints_btn_depress = False

            


def createFaceCenterPointsId(self):
    active_obj = bpy.context.active_object
    myFaceCenters = bboxFaceCenters(self)

    # Create collection for empties 
    collection = bpy.data.collections.new('FaceCentersColl')
    bpy.context.scene.collection.children.link(collection)
    
    for i in range(0, 6):
        name = ('FCL'+str(i))
        loc = myFaceCenters['FCL'+str(i)]
        # Template for Empty 
        name = bpy.data.objects.new('C'+str(i), None) #Name of empty obj
        bpy.data.collections['FaceCentersColl'].objects.link( name )
        name.empty_display_size = 0.005
        name.empty_display_type = 'SPHERE'
        name.show_in_front = True
        name.show_name = True
        name.location = loc
        name.parent = active_obj
        name.matrix_parent_inverse = active_obj.matrix_world.inverted()
    
    # Set wirecolor to custom color
    bpy.context.preferences.themes[0].view_3d.empty = (0.0, 1.0, 1.0)

    # Hide relationship lines
    bpy.context.space_data.overlay.show_relationship_lines = False




def deleteFaceCenterPointsId(self):
    # Remove collection and children items
    collection = bpy.data.collections.get('FaceCentersColl')
    for obj in collection.objects:
        bpy.data.objects.remove(obj, do_unlink=True)
    bpy.data.collections.remove(collection)
    
    # Set wirecolor to default color
    bpy.context.preferences.themes[0].view_3d.empty = (0.0, 0.0, 0.0)
    



def showFaceCenterPointsId(self, context):
    sel = bpy.context.selected_objects
 
    if checkSelected(self) == 'VALID':

        if GlobalsMain.centerpoints_btn_depress == False:
            createFaceCenterPointsId(self)
            GlobalsMain.centerpoints_btn_depress = True
            
        elif GlobalsMain.centerpoints_btn_depress == True:
            deleteFaceCenterPointsId(self)
            GlobalsMain.centerpoints_btn_depress = False

            




    





'''''''''''''''''''''''''''''''''''''''''''''''''''''
    
        PROPERTIES VISIBLE IN THE ADDON-PANEL
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''

class PG_MyProperties (bpy.types.PropertyGroup):
    
    transformOri : bpy.props.EnumProperty(
        items=[
            ('global', 'Global', '', '', 0),
            ('local', 'Local', '', '', 1)
        ],
        default = 'global',
        description = 'Set transforms orientation to',
        update = transformsOri
    )

    '''
    showBBox : BoolProperty(
        name = 'Bounding Box',
        description = 'Show/Hide bounding box for all selected objects',
        default = False,
        update = showBBox
    )
    

    showCornerPointsId : BoolProperty(
        name = 'Corner Points ID',
        description = 'Show/Hide Corner Points IDs for active object',
        default = False,
        update = showCornerPointsId
        #update = lambda s, c: showCornerPointsId(s, c, 'VALID'),
    )
    
    showFaceCentersPointsId : BoolProperty(
        name = 'Face Center Points ID',
        description = 'Show/Hide Face Center Points IDs for active object',
        default = False,
        update = showFaceCenterPointsId
    )
    '''
    
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