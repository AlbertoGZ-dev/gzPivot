# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    'name' : 'GZ Pivot',
    'author' : 'AlbertoGZ',
    'description' : 'Set origin to objects in easy and quick way.',
    'blender' : (2, 80, 0),
    'version' : (0, 1, 1),
    'location' : 'View3D',
    'warning' : '',
    'category' : 'Object'
}


from multiprocessing import context
import bpy
import os

from bpy.utils import ( register_class, 
                        unregister_class
                        )

from .gz_pivot_main import *
from .gz_pivot_panels import *
from .gz_pivot_ops import CornersBtn


''''''''''''''''''''''''''''''''''''''''''''''''''''
    
            REGISTER AND UNREGISTER
    
'''''''''''''''''''''''''''''''''''''''''''''''''''''

classes = (
    PG_MyProperties,
    OBJECT_PT_MyPanel,
    SUBPANEL_PT_PivotToCorners,
    SUBPANEL_PT_PivotToCenters,
    SUBPANEL_PT_PivotToMidEdges,
    SUBPANEL_PT_PivotTo3Dcursor,
    SUBPANEL_PT_About,
    #PREFS_PT_MyPrefs    
)



def register():
    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()

    # Path to the folder where the icons are.
    # The path is calculated relative to this py file inside the addon folder
    script_path = os.path.abspath(__file__) 
    path_list = script_path.split(os.sep)
    script_directory = path_list[0:len(path_list)-1]
    rel_path = 'icons/'
    icons_dir = '/'.join(script_directory) + '/' + rel_path

    print('ICONS DIRECTORY = ' + icons_dir)
   
    # load a preview thumbnail of a file and store in the previews collection 
    pcoll.load('corner_0', os.path.join(icons_dir, 'corner_0.png'), 'IMAGE')
    pcoll.load('corner_1', os.path.join(icons_dir, 'corner_1.png'), 'IMAGE')
    pcoll.load('corner_2', os.path.join(icons_dir, 'corner_2.png'), 'IMAGE')
    pcoll.load('corner_3', os.path.join(icons_dir, 'corner_3.png'), 'IMAGE')
    pcoll.load('corner_4', os.path.join(icons_dir, 'corner_4.png'), 'IMAGE')
    pcoll.load('corner_5', os.path.join(icons_dir, 'corner_5.png'), 'IMAGE')
    pcoll.load('corner_6', os.path.join(icons_dir, 'corner_6.png'), 'IMAGE')
    pcoll.load('corner_7', os.path.join(icons_dir, 'corner_7.png'), 'IMAGE')
    
    pcoll.load('face_center_0', os.path.join(icons_dir, 'face_center_0.png'), 'IMAGE')
    pcoll.load('face_center_1', os.path.join(icons_dir, 'face_center_1.png'), 'IMAGE')
    pcoll.load('face_center_2', os.path.join(icons_dir, 'face_center_2.png'), 'IMAGE')
    pcoll.load('face_center_3', os.path.join(icons_dir, 'face_center_3.png'), 'IMAGE')
    pcoll.load('face_center_4', os.path.join(icons_dir, 'face_center_4.png'), 'IMAGE')
    pcoll.load('face_center_5', os.path.join(icons_dir, 'face_center_5.png'), 'IMAGE')
    
    preview_collections['main'] = pcoll
    
    #
    for cls in classes:
        register_class(cls)
    #
    bpy.types.Scene.my_tool = PointerProperty(type=PG_MyProperties)

    bpy.utils.register_class(CornersBtn)
    bpy.utils.register_class(CentersBtn)
    bpy.utils.register_class(MidEdgesBtn)
    bpy.utils.register_class(CenterBoundsBtn)
    bpy.utils.register_class(CenterMassBtn)
    
    bpy.utils.register_class(CursorBtn)
    bpy.utils.register_class(ResetLocationBtn)

    bpy.utils.register_class(ShowBBoxBtn)
    bpy.utils.register_class(ShowCornerPointsBtn)
    bpy.utils.register_class(ShowCenterPointsBtn)
    bpy.utils.register_class(ShowMidEdgesBtn)

   

def unregister():
    #
    for cls in reversed(classes):
        unregister_class(cls)
    #
    del bpy.types.Scene.my_tool  # remove PG_MyProperties

    bpy.utils.unregister_class(CornersBtn)
    bpy.utils.unregister_class(CentersBtn)
    bpy.utils.unregister_class(MidEdgesBtn)
    bpy.utils.unregister_class(CenterBoundsBtn)
    bpy.utils.unregister_class(CenterMassBtn)
    
    bpy.utils.unregister_class(CursorBtn)
    bpy.utils.unregister_class(ResetLocationBtn)

    bpy.utils.unregister_class(ShowBBoxBtn)
    bpy.utils.unregister_class(ShowCornerPointsBtn)
    bpy.utils.unregister_class(ShowCenterPointsBtn)
    bpy.utils.unregister_class(ShowMidEdgesBtn)



    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()
  

if __name__ == '__main__':
    pass
    register()

    bpy.ops.wm.modal_timer_operator()