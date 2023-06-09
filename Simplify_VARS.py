import bpy

def registerDataTypes():
    ## SHARP TOOLS

    bpy.types.Scene.simplify_clear_sharp = bpy.props.BoolProperty(name="Clear Sharp", description="Clear Sharp to the Sharp Edges", default=False)
    bpy.types.Scene.simplify_clear_seam = bpy.props.BoolProperty(name="Clear Seam", description="Clear Seam to the Sharp Edges", default=False)
    bpy.types.Scene.simplify_clear_bevel = bpy.props.BoolProperty(name="Clear Bevel Weight", description="Clear Bevel Weight to the Sharp Edges", default=False)

    bpy.types.Scene.simplify_use_sharp = bpy.props.BoolProperty(name="Add Sharp", description="Add Sharp to the Sharp Edges", default=False)
    bpy.types.Scene.simplify_use_seam = bpy.props.BoolProperty(name="Add Seam", description="Add Seam to the Sharp Edges", default=False)
    bpy.types.Scene.simplify_use_bevel = bpy.props.BoolProperty(name="Add Bevel Weight", description="Add Bevel Weight to the Sharp Edges", default=False)
    bpy.types.Scene.simplify_auto_select_sharp_value = bpy.props.FloatProperty(name="Sharpness Value", description="Sharpness Value (min: 0.00, max: 180.00)", default=30.00, min=0.00, max=180.00, step=5)

    ## UV unwrap
    bpy.types.Scene.simplify_use_uv_unwrap = bpy.props.BoolProperty(name="UV unwrap", description="Unwrap UV", default=False)
    
    bpy.types.Scene.simplify_add_auto_smooth = bpy.props.BoolProperty(name="Add", description="Add Auto Smooth", default=False)
    bpy.types.Scene.simplify_remove_auto_smooth = bpy.props.BoolProperty(name="Remove", description="Remove Auto Smooth", default=False)
    bpy.types.Scene.simplify_auto_smooth_value = bpy.props.FloatProperty(name="Auto Smooth Value", description="Auto Smooth Value (min: 0.00, max: 180.00)", default=80.00, min=0.00, max=180.00, step=5)
    bpy.types.Scene.simplify_use_recalulate_outside = bpy.props.BoolProperty(name="Recalculate outside", description="Recalculate normal outside", default=False)
    bpy.types.Scene.simplify_use_clear_custom_data = bpy.props.BoolProperty(name="Clear custom data", description="Clear custom split normals data", default=False)
    bpy.types.Scene.simplify_use_tri_to_quad = bpy.props.BoolProperty(name="Triangles to Quad", description="Triangles to Quad", default=False)
    bpy.types.Scene.simplify_use_merge = bpy.props.BoolProperty(name="Remove doubles", description="Merge Vertices", default=False)
    
    ##Modifiers
    bpy.types.Scene.simplify_use_decimate = bpy.props.BoolProperty(name="Decimate mesh", description="Decimate the mesh", default=False)
    bpy.types.Scene.simplify_decimate_value = bpy.props.FloatProperty(name="Decimate Value", description="Decimate Value (min: 0.01, max: 0.95)", default=0.5, min=0.01, max=0.95, step=10)
    bpy.types.Scene.simplify_use_auto_mirror = bpy.props.BoolProperty(name="Add Auto Mirror", description="Add automirror", default=False)
    bpy.types.Scene.simplify_use_bevel_modifier_weight = bpy.props.BoolProperty(name="Add Bevel Modifier (Weight)", description="Add Bevel Modifier", default=False)
    bpy.types.Scene.simplify_use_bevel_modifier = bpy.props.BoolProperty(name="Add Bevel Modifier (Angle)", description="Add Bevel Modifier", default=False)
    bpy.types.Scene.simplify_bevel_modifier_angle = bpy.props.FloatProperty(name="Angle Value", description="Angle Value (min: 0.00, max: 180.00)", default=30.00, min=0.00, max=180.00, step=5)
    bpy.types.Scene.simplify_use_apply_all_modifiers = bpy.props.BoolProperty(name="Apply all modifiers", description="Apply all modifiers", default=False)
    
    bpy.types.Scene.simplify_use_remove_unused_materials = bpy.props.BoolProperty(name="Remove unused materials", description="Remove all unused materials", default=False)
    bpy.types.Scene.simplify_use_replace_duplicate_materials = bpy.props.BoolProperty(name="Replace duplicate materials", description="Replace duplicate materials, for exemple (Material.001, Material.002 --- by --- Material) NEED MATERIAL NAME WITHOUT ' . ' (point)", default=False)
    bpy.types.Scene.simplify_use_apply_scale_rotate = bpy.props.BoolProperty(name="Apply Rotate-Scale", description="Apply rotate and scale", default=False)
    
    #Properties
    bpy.types.Scene.simplify_use_objName_to_meshName = bpy.props.BoolProperty(name="Objects Name to Meshes Name", description="Change the name of the mesh by the name of the object", default=False)
    bpy.types.Scene.simplify_reverse_objName_to_meshName = bpy.props.BoolProperty(name="Reverse", description="Meshes name to Objects name", default=False)


    #ADD CUSTOM PROPERIES
    bpy.types.Scene.simplify_add_custom_props = bpy.props.BoolProperty(name="Add Custom Properties", description="Add Custom Properies", default=False)
    bpy.types.Scene.simplify_add_custom_props_receive_shadow = bpy.props.BoolProperty(name="Add Receive Shadow", description="Add Custom Properies - Receive Shadow", default=False)
    bpy.types.Scene.simplify_add_custom_props_cast_shadow = bpy.props.BoolProperty(name="Add Cast Shadow", description="Add Custom Properies - Cast Shadow", default=False)
    bpy.types.Scene.simplify_add_custom_props_receive_shadow_value = bpy.props.BoolProperty(name="Set Receive Shadow Value", description="Set Custom Properies - Receive Shadow", default=False)
    bpy.types.Scene.simplify_add_custom_props_cast_shadow_value = bpy.props.BoolProperty(name="Set Cast Shadow Value", description="Set Custom Properies - Cast Shadow", default=False)

def unregisterDataTypes():
    del bpy.types.Scene.simplify_clear_sharp
    del bpy.types.Scene.simplify_clear_seam
    del bpy.types.Scene.simplify_clear_bevel

    del bpy.types.Scene.simplify_use_sharp
    del bpy.types.Scene.simplify_use_seam
    del bpy.types.Scene.simplify_use_bevel
    del bpy.types.Scene.simplify_auto_select_sharp_value

    del bpy.types.Scene.simplify_use_uv_unwrap

    del bpy.types.Scene.simplify_add_auto_smooth
    del bpy.types.Scene.simplify_remove_auto_smooth
    del bpy.types.Scene.simplify_auto_smooth_value
    del bpy.types.Scene.simplify_use_recalulate_outside
    del bpy.types.Scene.simplify_use_clear_custom_data

    del bpy.types.Scene.simplify_use_tri_to_quad
    del bpy.types.Scene.simplify_use_merge
    
    del bpy.types.Scene.simplify_use_decimate
    del bpy.types.Scene.simplify_decimate_value
    del bpy.types.Scene.simplify_use_auto_mirror
    del bpy.types.Scene.simplify_use_bevel_modifier_weight
    del bpy.types.Scene.simplify_use_bevel_modifier
    del bpy.types.Scene.simplify_bevel_modifier_angle
    del bpy.types.Scene.simplify_use_apply_all_modifiers

    del bpy.types.Scene.simplify_use_remove_unused_materials
    del bpy.types.Scene.simplify_use_replace_duplicate_materials
    del bpy.types.Scene.simplify_use_apply_scale_rotate
    
    del bpy.types.Scene.simplify_use_objName_to_meshName
    del bpy.types.Scene.simplify_reverse_objName_to_meshName


    del bpy.types.Scene.simplify_add_custom_props
    del bpy.types.Scene.simplify_add_custom_props_receive_shadow
    del bpy.types.Scene.simplify_add_custom_props_cast_shadow
    del bpy.types.Scene.simplify_add_custom_props_receive_shadow_value
    del bpy.types.Scene.simplify_add_custom_props_cast_shadow_value