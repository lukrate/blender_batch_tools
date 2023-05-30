import bpy
import math

class Simplify_OT_Simplify(bpy.types.Operator):
    bl_label = "Simplify Selected Objects"
    bl_idname = "wm.simplify_object_operator"
    bl_description = "Apply all operators" 
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        obj = context.selected_objects
        if len(obj) >= 1:
            return True

        return False
    
    def ui_update_custom_props(self, obj, name, value):
        ui = obj.id_properties_ui(name)
        ui.update(description = name)
        ui.update(default = value) 
    
    def execute(self, context):
        active_objs = context.selected_objects
        mat_list = []

        if context.scene.simplify_use_tri_to_quad or \
            context.scene.simplify_use_merge or \
            context.scene.simplify_use_recalulate_outside or \
            context.scene.simplify_use_seam or \
            context.scene.simplify_use_sharp or \
            context.scene.simplify_use_bevel or \
            context.scene.simplify_clear_seam or \
            context.scene.simplify_clear_sharp or \
            context.scene.simplify_clear_bevel:

            if(context.object.mode == "OBJECT"):
                bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='SELECT')
            if context.scene.simplify_use_tri_to_quad:
                bpy.ops.mesh.tris_convert_to_quads()
            if context.scene.simplify_use_merge:
                bpy.ops.mesh.remove_doubles()
            if context.scene.simplify_use_recalulate_outside:
                bpy.ops.mesh.normals_make_consistent(inside=False)
            if context.scene.simplify_clear_seam:
                bpy.ops.mesh.mark_seam(clear=True)
            if context.scene.simplify_clear_sharp:
                bpy.ops.mesh.mark_sharp(clear=True)
            if context.scene.simplify_clear_bevel:
                bpy.ops.mesh.customdata_bevel_weight_edge_clear()

            ## SELECT SHARP
            bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='EDGE')
            bpy.ops.mesh.edges_select_sharp(sharpness=math.pi / 180 * context.scene.simplify_auto_select_sharp_value)
            if context.scene.simplify_use_sharp:
                bpy.ops.mesh.mark_sharp(clear=False)
            if context.scene.simplify_use_seam:
                bpy.ops.mesh.mark_seam(clear=False)
            if context.scene.simplify_use_bevel:
                ##bpy.ops.mesh.customdata_bevel_weight_edge_clear()
                bpy.ops.mesh.customdata_bevel_weight_edge_add()
                bpy.ops.object.editmode_toggle()
                for obj in active_objs:
                    edges = [e for e in obj.data.edges if e.select]
                    for edge in edges:
                        edge.bevel_weight=1
                bpy.ops.object.editmode_toggle()
            
            if context.scene.simplify_use_uv_unwrap:
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)


            #bpy.ops.mesh.select_all(action='DESELECT')
            bpy.ops.object.editmode_toggle()

        if context.scene.simplify_use_replace_duplicate_materials:
            for obj in active_objs:
                for mat in obj.material_slots:
                    if not mat.name in mat_list:
                        mat_list.append(mat.name)
            for obj in active_objs:
                if obj.type == "MESH":
                    cur_obj = bpy.data.objects[obj.name]
                    for mat in cur_obj.material_slots:
                        if mat.name.split(".")[0] in mat_list:
                            mat.material = bpy.data.materials.get(mat.name.split(".")[0])

        for obj in active_objs:
            if obj.type == "MESH":
                context.view_layer.objects.active = obj

                if context.scene.simplify_use_bevel:
                    pass

                if obj.data.has_custom_normals and context.scene.simplify_use_clear_custom_data:
                    bpy.ops.mesh.customdata_custom_splitnormals_clear()
                
                if context.scene.simplify_use_apply_scale_rotate:
                    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

                if context.scene.simplify_use_auto_smooth:
                    #bpy.ops.object.shade_smooth()
                    bpy.data.objects[obj.name].data.use_auto_smooth = True
                    obj.data.auto_smooth_angle = math.pi / 180 * context.scene.simplify_auto_smooth_value
                
                ## Modifiers

                if context.scene.simplify_use_decimate:
                    bpy.ops.mesh.customdata_custom_splitnormals_clear()
                    dec = obj.modifiers.new("Simplify Decimate", type="DECIMATE")
                    dec.ratio = context.scene.simplify_decimate_value
                
                if context.scene.simplify_use_auto_mirror:
                    bpy.ops.object.automirror()
                
                if context.scene.simplify_use_bevel_modifier:
                    bpy.ops.mesh.customdata_custom_splitnormals_clear()
                    bev = obj.modifiers.new("Simplify Bevel", type="BEVEL")
                    bev.width = 0.01
                    bev.segments = 3
                    bev.limit_method = "WEIGHT"


                if context.scene.simplify_use_apply_all_modifiers:
                    for name in [m.name for m in obj.modifiers]:
                        bpy.ops.object.modifier_apply( modifier = name )

                if context.scene.simplify_use_remove_unused_materials:
                    bpy.ops.object.material_slot_remove_unused()

                if context.scene.simplify_use_objName_to_meshName:
                    if not context.scene.simplify_reverse_objName_to_meshName:
                        bpy.data.objects[obj.name].data.name = bpy.data.objects[obj.name].name
                    else:
                        bpy.data.objects[obj.name].name = bpy.data.objects[obj.name].data.name

                if context.scene.simplify_add_custom_props:
                    if context.scene.simplify_add_custom_props_cast_shadow:
                        name = "cast_shadow"
                        value = context.scene.simplify_add_custom_props_cast_shadow_value
                        obj[name] = value
                        self.ui_update_custom_props(obj, name, value)
                    if context.scene.simplify_add_custom_props_receive_shadow:
                        name = "receive_shadow"
                        value = context.scene.simplify_add_custom_props_receive_shadow_value
                        obj[name] = value
                        self.ui_update_custom_props(obj, name, value)

                    
                    

        

        return {"FINISHED"}