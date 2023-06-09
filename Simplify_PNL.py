import bpy



class SIMPLIFY_PT_panel():
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Edit"
    bl_category = "Batch Tools"

class SIMPLIFY_PT_main(SIMPLIFY_PT_panel, bpy.types.Panel):
    bl_idname = "SIMPLYIFY_PT_main"
    bl_label = "Batch Tools"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.scale_y = 2
        row.operator("wm.simplify_object_operator")

class SIMPLIFY_PT_mesh(SIMPLIFY_PT_panel, bpy.types.Panel):
    bl_parent_id = "SIMPLYIFY_PT_main"
    bl_label = "MESHES"

    def draw(self, context):
        scn = context.scene
        
        layout = self.layout
        
        box_mesh = layout.box()        
        row = box_mesh.row()
        row.prop(scn, "simplify_use_clear_custom_data")
        row = box_mesh.row()
        row.prop(scn, "simplify_use_apply_scale_rotate")
        row = box_mesh.row()
        row.prop(scn, "simplify_use_tri_to_quad")
        row = box_mesh.row()
        row.prop(scn, "simplify_use_merge")
        row = box_mesh.row()
        row.prop(scn, "simplify_use_recalulate_outside")
        
        
        ## sharpness tools
        layout.label(text="Sharpness Edge Tools:")
        box_mesh = layout.box()
        row = box_mesh.row()
        row.prop(scn, "simplify_use_sharp")
        row.prop(scn, "simplify_clear_sharp")
        row = box_mesh.row()
        row.prop(scn, "simplify_use_seam")
        row.prop(scn, "simplify_clear_seam")
        row = box_mesh.row()
        row.prop(scn, "simplify_use_bevel")
        row.prop(scn, "simplify_clear_bevel")
        
        if context.scene.simplify_use_sharp or context.scene.simplify_use_seam or context.scene.simplify_use_bevel:
            row = box_mesh.row()
            row.scale_y = 2
            row.prop(scn, "simplify_auto_select_sharp_value")
            layout.separator(factor=1.0)
            row = box_mesh.row()
            row.prop(scn, "simplify_use_bevel_modifier_weight")
        
        ## uv unwrap
        row = box_mesh.row()
        row.prop(scn, "simplify_use_uv_unwrap")
        
        layout.label(text="Auto Smooth:")
        box_mesh = layout.box()
        row = box_mesh.row()
        row.prop(scn, "simplify_add_auto_smooth")
        row.prop(scn, "simplify_remove_auto_smooth")
        if context.scene.simplify_add_auto_smooth:
            row = box_mesh.row()
            row.scale_y = 2
            row.prop(scn, "simplify_auto_smooth_value")
            layout.separator(factor=1.0)
        

        

class SIMPLIFY_PT_modifiers(SIMPLIFY_PT_panel, bpy.types.Panel):
    bl_parent_id = "SIMPLYIFY_PT_main"
    bl_label = "MODIFIERS"

    def draw(self, context):
        scn = context.scene
        layout = self.layout
        box_modifiers = layout.box() 
        row = box_modifiers.row()
        row.prop(scn, "simplify_use_decimate")
        if context.scene.simplify_use_decimate:
            row = box_modifiers.row()
            row.scale_y = 2
            row.prop(scn, "simplify_decimate_value")
        row = box_modifiers.row()
        if hasattr(context.scene, 'automirror'):
            row.prop(scn, "simplify_use_auto_mirror")
        else:
            row.alert = True
            row.label(text="install auto mirror addon")
        
        row = box_modifiers.row()
        row.prop(scn, "simplify_use_bevel_modifier")
        if context.scene.simplify_use_bevel_modifier:
            row = box_modifiers.row()
            row.scale_y = 2
            row.prop(scn, "simplify_bevel_modifier_angle")
        
        row = box_modifiers.row()
        row.prop(scn, "simplify_use_apply_all_modifiers")



class SIMPLIFY_PT_materials(SIMPLIFY_PT_panel, bpy.types.Panel):
    bl_parent_id = "SIMPLYIFY_PT_main"
    bl_label = "MATERIALS"

    def draw(self, context):
        scn = context.scene
        
        layout = self.layout
        box_modifiers = layout.box()  
        row = box_modifiers.row()
        row.prop(scn, "simplify_use_remove_unused_materials")
        #simplify_use_replace_duplicate_materials
        row = box_modifiers.row()
        row.prop(scn, "simplify_use_replace_duplicate_materials")
        row.alert = True
        row.label(text="", icon="ERROR")


class SIMPLIFY_PT_props(SIMPLIFY_PT_panel, bpy.types.Panel):
    bl_parent_id = "SIMPLYIFY_PT_main"
    bl_label = "PROPERTIES"

    def draw(self, context):
        scn = context.scene

        layout = self.layout
        box = layout.box()
        row = box.row()
        row.prop(scn, "simplify_use_objName_to_meshName")
        if context.scene.simplify_use_objName_to_meshName:
            row.prop(scn, "simplify_reverse_objName_to_meshName")

class SIMPLIFY_PT_customProps(SIMPLIFY_PT_panel, bpy.types.Panel):
    bl_parent_id = "SIMPLYIFY_PT_main"
    bl_label = "CUSTOM PROPERTIES"

    def draw(self, context):
        scn = context.scene

        layout = self.layout
        box = layout.box()
        row = box.row()
        row.prop(scn, "simplify_add_custom_props")
        if context.scene.simplify_add_custom_props:
            row = box.row()
            row.prop(scn, "simplify_add_custom_props_cast_shadow")
            if context.scene.simplify_add_custom_props_cast_shadow:
                row = box.row()
                row.label(text = "value")
                row.prop(scn, "simplify_add_custom_props_cast_shadow_value", text=str(context.scene.simplify_add_custom_props_cast_shadow_value))
            row = box.row()
            row.prop(scn, "simplify_add_custom_props_receive_shadow")
            if context.scene.simplify_add_custom_props_receive_shadow:
                row = box.row()
                row.label(text = "value")
                row.prop(scn, "simplify_add_custom_props_receive_shadow_value", text=str(context.scene.simplify_add_custom_props_receive_shadow_value))
           

class SIMPLIFY_PT_selected(SIMPLIFY_PT_panel, bpy.types.Panel):
    bl_parent_id = "SIMPLYIFY_PT_main"
    bl_label = "Selected Objects"

    def draw(self, context):
        objs = context.selected_objects
        
        layout = self.layout
        for obj in objs:
            row = layout.row()
            if not obj.type == "MESH":
                row.alert = True
            row.label(text="" + obj.name)
        