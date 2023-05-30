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

import bpy

bl_info = {
    "name" : "Simplify - Batch Tools",
    "author" : "Boris",
    "description" : "Batch/stackable tools for lot of repetitive manipulation",
    "blender" : (3, 5, 1),
    "version" : (0, 0, 8),
    "location" : "3D View",
    "category" : "Mesh"
}

# VARS
from . Simplify_VARS import registerDataTypes
from . Simplify_VARS import unregisterDataTypes

# OPERATORS
from .Simplify_OP import Simplify_OT_Simplify
from .Simplify_PNL import SIMPLIFY_PT_main
from .Simplify_PNL import SIMPLIFY_PT_mesh
from .Simplify_PNL import SIMPLIFY_PT_modifiers
from .Simplify_PNL import SIMPLIFY_PT_materials
from .Simplify_PNL import SIMPLIFY_PT_props
from .Simplify_PNL import SIMPLIFY_PT_customProps
from .Simplify_PNL import SIMPLIFY_PT_selected

classes = (
    Simplify_OT_Simplify,
    SIMPLIFY_PT_main,
    SIMPLIFY_PT_mesh,
    SIMPLIFY_PT_modifiers,
    SIMPLIFY_PT_materials,
    SIMPLIFY_PT_props,
    SIMPLIFY_PT_customProps,
    SIMPLIFY_PT_selected,
)

def register():
    for c in classes:
        bpy.utils.register_class(c)
    registerDataTypes()

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    unregisterDataTypes()
