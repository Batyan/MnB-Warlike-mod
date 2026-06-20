from header_common import *
from header_operations import *
from module_constants import *

scripts_presentation = [
    # script_presentation_generate_select_lord_card
        # input:
        #   arg1: troop_no
        #   arg2: x
        #   arg3: values_x
        #   arg4: values2_x
        #   arg5: cur_y
        # output: none
    ("presentation_generate_select_lord_card",
        [
            (store_script_param, ":lord_no", 1),

            (store_script_param, ":x", 2),
            (store_script_param, ":values_x", 3),
            (store_script_param, ":values2_x", 4),
            (store_script_param, ":cur_y", 5),

            (assign, ":line_height", 30),

            (create_mesh_overlay, reg0, "mesh_mp_ingame_menu"),
            (position_set_x, pos1, ":x"),
            (position_set_y, pos1, ":cur_y"),
            (overlay_set_position, reg0, pos1),
            (position_set_x, pos1, 800),
            (position_set_y, pos1, 225),
            (overlay_set_size, reg0, pos1),

            (store_add, ":line_text_y", ":cur_y", 10),

            (store_add, ":checkbox_y", ":line_text_y", 45),
            (store_add, ":checkbox_x", ":x", 25),
            (create_check_box_overlay, reg0, "mesh_checkbox_off", "mesh_checkbox_on"),
            (position_set_x, pos1, ":checkbox_x"),
            (position_set_y, pos1, ":checkbox_y"),
            (overlay_set_position, reg0, pos1),
            (troop_set_slot, ":lord_no", slot_troop_temp_slot, reg0),

            (store_add, ":picture_x", ":x", 35),
            (store_add, ":picture_y", ":line_text_y", 5),
            (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_troop_note_mesh", ":lord_no"),
            (position_set_x, pos1, ":picture_x"),
            (position_set_y, pos1, ":picture_y"),
            (overlay_set_position, reg0, pos1),
            (position_set_x, pos1, 380),
            (position_set_y, pos1, 380),
            (overlay_set_size, reg0, pos1),

            (call_script, "script_troop_get_banner", ":lord_no"),
            (assign, ":banner_spr", reg0),
            (try_begin),
                (is_between, ":banner_spr", banner_scene_props_begin, banner_scene_props_end),
                (store_sub, ":banner_mesh", ":banner_spr", banner_scene_props_begin),
                (val_add, ":banner_mesh", banner_meshes_begin),

                (store_sub, ":banner_x", ":values_x", 25),
                (store_add, ":banner_y", ":line_text_y", 100),
                (create_mesh_overlay, reg0, ":banner_mesh"),
                (position_set_x, pos1, ":banner_x"),
                (position_set_y, pos1, ":banner_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 45),
                (position_set_y, pos1, 45),
                (overlay_set_size, reg0, pos1),
                (overlay_set_additional_render_height, reg0, 100),
            (try_end),

            (troop_get_slot, ":culture", ":lord_no", slot_troop_culture),
            (str_store_faction_name, s10, ":culture"),
            (call_script, "script_presentation_create_text_overlay", 0, ":values_x", ":line_text_y", 1000, 1000),
            (overlay_set_color, reg0, text_color_white),

            (val_add, ":line_text_y", ":line_height"),

            (call_script, "script_troop_get_relation_with_troop", ":lord_no", "$g_player_troop"),
            (assign, reg10, reg0),
            (str_store_string, s10, "@{reg10} relation"),
            (call_script, "script_presentation_create_text_overlay", 0, ":values_x", ":line_text_y", 1000, 1000),
            (overlay_set_color, reg0, text_color_white),

            (troop_get_slot, reg10, ":lord_no", slot_troop_renown),
            (str_store_string, s10, "@{reg10} renown"),
            (call_script, "script_presentation_create_text_overlay", 0, ":values2_x", ":line_text_y", 1000, 1000),
            (overlay_set_color, reg0, text_color_white),

            (val_add, ":line_text_y", ":line_height"),

            (troop_get_slot, reg10, ":lord_no", slot_troop_num_vassal),
            (str_store_string, s10, "@{reg10} vassals"),
            (call_script, "script_presentation_create_text_overlay", 0, ":values_x", ":line_text_y", 1000, 1000),
            (overlay_set_color, reg0, text_color_white),

            (assign, ":num_fiefs", 0),
            (try_for_range, ":center_no", centers_begin, centers_end),
                (party_slot_eq, ":center_no", slot_party_lord, ":lord_no"),
                (val_add, ":num_fiefs", 1),
            (try_end),
            (assign, reg10, ":num_fiefs"),
            (str_store_string, s10, "@{reg10} fiefs"),
            (call_script, "script_presentation_create_text_overlay", 0, ":values2_x", ":line_text_y", 1000, 1000),
            (overlay_set_color, reg0, text_color_white),

            (val_add, ":line_text_y", ":line_height"),

            (str_store_troop_name, s10, ":lord_no"),
            (call_script, "script_presentation_create_text_overlay", 0, ":values_x", ":line_text_y", 1000, 1000),
            (overlay_set_color, reg0, text_color_white),
        ]),

    # script_presentation_create_text_overlay
        # input:
        #   s10: text_string_register
        #   arg1: text_overlay_options
        #   arg2: x_position
        #   arg3: y_position
        #   arg4: x_size
        #   arg5: y_size
        # output:
        #   reg0: overlay_id
    ("presentation_create_text_overlay",
        [
            (store_script_param, ":options", 1),
            (store_script_param, ":x_pos", 2),
            (store_script_param, ":y_pos", 3),
            (store_script_param, ":x_size", 4),
            (store_script_param, ":y_size", 5),

            (create_text_overlay, reg0, s10, ":options"),
            (position_set_x, pos1, ":x_pos"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, reg0, pos1),
            (position_set_x, pos1, ":x_size"),
            (position_set_y, pos1, ":y_size"),
            (overlay_set_size, reg0, pos1),
        ]),

    # script_presentation_create_combo_button_overlay
        # input:
        #   arg1: x_position
        #   arg2: y_position
        #   arg3: x_size
        #   arg4: y_size
        # output:
        #   reg0: overlay_id
    ("presentation_create_combo_button_overlay",
        [
            (store_script_param, ":x_pos", 1),
            (store_script_param, ":y_pos", 2),
            (store_script_param, ":x_size", 3),
            (store_script_param, ":y_size", 4),

            (create_combo_button_overlay, reg0),
            (position_set_x, pos1, ":x_pos"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, reg0, pos1),
            (position_set_x, pos1, ":x_size"),
            (position_set_y, pos1, ":y_size"),
            (overlay_set_size, reg0, pos1),
        ]),

    # script_presentation_create_check_box_overlay
        # input:
        #   arg1: x_position
        #   arg2: y_position
        #   arg3: value
        # output:
        #   reg0: overlay_id
    ("presentation_create_check_box_overlay",
        [
            (store_script_param, ":x_pos", 1),
            (store_script_param, ":y_pos", 2),
            (store_script_param, ":value", 3),

            (create_check_box_overlay, reg0,  "mesh_checkbox_off", "mesh_checkbox_on"),
            (position_set_x, pos1, ":x_pos"),
            (position_set_y, pos1, ":y_pos"),
            (overlay_set_position, reg0, pos1),
            (overlay_set_val, reg0, ":value"),
        ]),
]