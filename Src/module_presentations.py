from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
from header_terrain_types import *
import string

###############################
## Presentation informations ##
###############################
## screen start :
## x:0 y:0
## bottom left
##
## main screen size:
## x:960 y:700
## 
##

numberbox_padding = 5
numberbox_size = 65
checkbox_size = 20

button_padding = 12
button_size = 80

line_height = 30
line_small_height = 20
category_height = line_height + 20

presentations = [

    ###############
    ## Hardcoded ##
    ###############
    ("game_profile_banner_selection", 0, mesh_load_window,
        [
            (ti_on_presentation_load, [
                (set_fixed_point_multiplier, 1000),
                (presentation_set_duration, 999999),
            ]),

            (ti_on_presentation_run,
            [
                (presentation_set_duration, 0),
            ]),
        ]),

    ###########
    ## Other ##
    ###########
    # prsnt_recruit_from_town_garrison
        # Requires $temp set to the center where the player is recruiting
    ("recruit_from_town_garrison", 0, mesh_load_window, 
        [
        	(ti_on_presentation_load,
        	[
        		(set_fixed_point_multiplier, 1000),
        		
        		(assign, ":current_city", "$temp"),
        		# (party_get_num_companions, ":garrison_size", ":current_city"),
        		# (store_div, ":garrison_size_div_2", ":garrison_size", 10),
        		# Company free capacity textBox
        		(create_text_overlay, reg0, s11, tf_left_align),
        		(position_set_x, pos1, 50),
        		(position_set_y, pos1, 800),
        		(overlay_set_position, reg0, pos1),
        		(position_set_x, pos1, 1000),
        		(position_set_y, pos1, 1000),
        		(overlay_set_size, reg0, pos1),
        		
        		# (party_get_free_companions_capacity, reg11, "$g_player_party"),
        		# (str_store_string, s11, "@{reg11}"),
        		# (create_text_overlay, "$g_hire_soldiers_free_capacity", s11, tf_left_align),
        		# (position_set_x, pos1, 120),
        		# (position_set_y, pos1, 800),
        		# (overlay_set_position, "$g_hire_soldiers_free_capacity", pos1),
        		# (position_set_x, pos1, 1000),
        		# (position_set_y, pos1, 1000),
        		# (overlay_set_size, "$g_hire_soldiers_free_capacity", pos1),
        		
        		(try_begin),
        			
        			(str_clear, s0),
        			(create_text_overlay, reg0, s0, tf_scrollable),
        			(position_set_x, pos1, 60),
        			(position_set_y, pos1, 200),
        			(overlay_set_position, reg0, pos1),
        			(position_set_x, pos1, 520),
        			(position_set_y, pos1, 500),
        			
        			(overlay_set_area_size, reg0, pos1),
        			
        			(set_container_overlay, reg0),
        			
        			(store_add, "$g_hire_soldiers_center_troops_begin", reg0, 1),
        			
        			(assign, ":names_x", 0),
        			(assign, ":numberbox_x", 440),
        			(assign, ":cur_y", 20),
        			(party_get_num_companion_stacks, ":num_stacks", ":current_city"),
        			(try_for_range, ":stack_no", 0, ":num_stacks"),
        				(party_stack_get_troop_id, ":troop_no", ":current_city", ":stack_no"),
                        # (neg|troop_is_hero, ":troop_no"),
        				(party_stack_get_size, ":stack_size", ":current_city", ":stack_no"),
        				(assign, reg1, ":stack_size"),
        				
        				(str_store_troop_name, s1, ":troop_no"),
        				
                        (try_begin),
                            (troop_is_hero, ":troop_no"),
                        
                            (create_text_overlay, reg0, "@{s1}", tf_left_align),
                        (else_try),
            				(call_script, "script_troop_get_cost", ":troop_no"),
            				(assign, ":troop_cost", reg0),
            				
            				(call_script, "script_troop_get_cost_modifier", ":troop_no", ":current_city", "$g_player_troop"),
            				(assign, ":cost_modifier", reg0),
            				(val_mul, ":troop_cost", ":cost_modifier"),
            				(val_div, ":troop_cost", 100),
            				
            				(assign, reg2, ":troop_cost"),
                        
                            (create_text_overlay, reg0, "@{s1}: {reg2} denars ({reg1})", tf_left_align),
                        (try_end),
        				
        				(position_set_x, pos1, ":names_x"),
        				(position_set_y, pos1, ":cur_y"),
        				(overlay_set_position, reg0, pos1),
        				(position_set_x, pos1, 1000),
        				(position_set_y, pos1, 1000),
        				(overlay_set_size, reg0, pos1),
        				
                        (assign, ":pos_x", ":numberbox_x"),
        				(store_add, ":max_taken", ":stack_size", 1),
        				(try_begin),
        					(troop_is_hero, ":troop_no"),
        					(assign, ":max_taken", 0),
                            (create_text_overlay, reg0, "@ ", tf_left_align),
                        (else_try),
                            (call_script, "script_cf_troop_available_for_recruit", ":troop_no", ":current_city", "$g_player_troop"),
        				    (create_number_box_overlay, reg0, 0, ":max_taken"),
                        (else_try),
                            (create_text_overlay, reg0, "@Unavailable", tf_left_align),
                            (overlay_set_color, reg0, text_color_light),
                            (val_add, ":pos_x", -25),
        				(try_end),
        				
        				(position_set_x, pos1, ":pos_x"),
        				(position_set_y, pos1, ":cur_y"),
        				(overlay_set_position, reg0, pos1),
        				(position_set_x, pos1, 1000),
        				(position_set_y, pos1, 1000),
        				(overlay_set_size, reg0, pos1),
        				
        				(val_add, ":cur_y", 40),
        				
        				# This is to reset the number of men the player is hiring
        				(troop_set_slot, ":troop_no", slot_troop_temp_hire_number, 0),
        			(try_end),
        			(store_add, "$g_hire_soldiers_center_troops_end", reg0, 1),
        			
        			(set_container_overlay, -1),
        		(try_end),
        		
        		# Total cost
        		(str_store_string, s10, "@Total cost: 0 denars"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, 250, 140, 1000, 1000),
                (assign, "$g_hire_soldiers_total_cost", reg0),
        		# Current money
        		(store_troop_gold, reg0, "$g_player_troop"),
        		(str_store_string, s10, "@Current money: {reg0} denars"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, 250, 110, 1000, 1000),
        		
        		# Party size
        		(party_get_num_companions, reg11, "$g_player_party"),
        		(str_store_string, s10, "@Party size: {reg11}"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, 250, 80, 1000, 1000),
                (assign, "$g_hire_soldiers_free_capacity", reg0),
                
                # Min Center Party size
                (call_script, "script_party_get_prefered_wages_limit", ":current_city"),
                (assign, reg10, reg1),
                (call_script, "script_party_get_wages", ":current_city"),
                (assign, reg11, reg0),
                (str_store_string, s10, "@Center recruitment limit: {reg11}/{reg10}"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, 250, 50, 1000, 1000),
                (assign, "$g_hire_soldiers_min_capacity", reg0),
                (try_begin),
                    (gt, reg10, reg11),
                    (overlay_set_color, "$g_hire_soldiers_min_capacity", text_color_impossible),
                (try_end),
        		
        		(store_add, "$g_hide_soldiers_portrait_begin", "$g_hire_soldiers_min_capacity", 1),
        		# Troop picture
        		(party_get_num_companion_stacks, ":num_stacks", ":current_city"),
        		(try_for_range, ":stack_no", 0, ":num_stacks"),
        			(party_stack_get_troop_id, ":troop_no", ":current_city", ":stack_no"),
                    # (neg|troop_is_hero, ":troop_no"),
        			(val_mul, ":troop_no", 2),
        			(create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_game_party_window", ":troop_no"),
        			# (position_set_x, pos1, 600),
        			(position_set_x, pos1, 520),
        			(position_set_y, pos1, 220),
        			(overlay_set_position, reg0, pos1),
        			(position_set_x, pos1, 1200),
        			(position_set_y, pos1, 1200),
        			(overlay_set_size, reg0, pos1),
        			(overlay_set_display, reg0, 0),
        		(try_end),
        		(assign, "$last", -1),
        		
        		# Troop informations
        		(str_clear, s0),
        		(create_text_overlay, "$g_hire_soldiers_troop_information", s0, tf_left_align),
        		# (position_set_x, pos1, 820),
        		# (position_set_y, pos1, 200),
        		# (overlay_set_position, "$g_hire_soldiers_troop_information", pos1),
        		# (position_set_x, pos1, 1000),
        		# (position_set_y, pos1, 1000),
        		# (overlay_set_size, "$g_hire_soldiers_troop_information", pos1),
        		
        		# Troop type
        		(str_clear, s0),
        		(create_text_overlay, "$g_hire_soldiers_troop_type", s0, tf_left_align),
        		# (position_set_x, pos1, 630),
        		# (position_set_y, pos1, 400),
        		# (overlay_set_position, "$g_hire_soldiers_troop_type", pos1),
        		# (position_set_x, pos1, 1000),
        		# (position_set_y, pos1, 1000),
        		# (overlay_set_size, "$g_hire_soldiers_troop_type", pos1),
        		
        		# Buy button
                (create_game_button_overlay, "$g_presentation_ok", "@Buy"),
                (position_set_x, pos1, 150),
                (position_set_y, pos1, 100),
                (overlay_set_position, "$g_presentation_ok", pos1),
        		
        		# Cancel button
        		(create_game_button_overlay, "$g_presentation_cancel", "@Cancel"),
        		(position_set_x, pos1, 150),
        		(position_set_y, pos1, 50),
        		(overlay_set_position, "$g_presentation_cancel", pos1),
        		
        		(presentation_set_duration, 999999),
        	]),
        	
        	(ti_on_presentation_mouse_enter_leave,
        	[
        		(store_trigger_param_1, ":object"),
        		(store_trigger_param_2, ":value"),
        		
        		(set_fixed_point_multiplier, 1000),
        		(is_between, ":object", "$g_hire_soldiers_center_troops_begin", "$g_hire_soldiers_center_troops_end"),
        		
        		(store_sub, ":stack_no", ":object", "$g_hire_soldiers_center_troops_begin"),
        		(val_div, ":stack_no", 2),

                # (try_for_range, ":cur_stack", 0, ":stack_no"),
                #     (party_stack_get_troop_id, ":troop_no", "$temp", ":cur_stack"),
                #     (troop_is_hero, ":troop_no"),
                #     (val_add, ":stack_no", 1),
                # (try_end),
        		
        		(store_add, ":portrait", ":stack_no", "$g_hide_soldiers_portrait_begin"),
        		
        		(try_begin),
        			(eq, ":value", 0),
        			(neq, "$last", ":portrait"),
        			(try_begin),
        				(ge, "$last", 0),
        				(overlay_set_display, "$last", 0),
        			(try_end),
        			(overlay_set_display, ":portrait", 1),
        			(assign, "$last", ":portrait"),
        			
        			(party_stack_get_troop_id, ":troop_no", "$temp", ":stack_no"),
        			(call_script, "script_troop_get_info", ":troop_no"),
        			(assign, ":num_lines", reg0),
        			(val_mul, ":num_lines", 18),
        			(store_sub, ":pos_y", 520, ":num_lines"),
        			(init_position, pos1),
        			(position_set_x, pos1, 820),
        			(position_set_y, pos1, ":pos_y"),
        			(overlay_set_position, "$g_hire_soldiers_troop_information", pos1),
        			(position_set_x, pos1, 1000),
        			(position_set_y, pos1, 1000),
        			(overlay_set_size, "$g_hire_soldiers_troop_information", pos1),
        			
        			(overlay_set_text, "$g_hire_soldiers_troop_information", s0),
        			
        			(call_script, "script_troop_get_description", ":troop_no"),
        			(assign, ":num_lines", reg0),
        			(val_mul, ":num_lines", 18),
        			(store_sub, ":pos_y", 700, ":num_lines"),
        			(init_position, pos1),
        			(position_set_x, pos1, 630),
        			(position_set_y, pos1, ":pos_y"),
        			(overlay_set_position, "$g_hire_soldiers_troop_type", pos1),
        			(position_set_x, pos1, 1000),
        			(position_set_y, pos1, 1000),
        			(overlay_set_size, "$g_hire_soldiers_troop_type", pos1),
        			
        			(overlay_set_text, "$g_hire_soldiers_troop_type", s0),
        			
        		(try_end),
        	]),
        	
        	(ti_on_presentation_event_state_change,
        	[
        		(store_trigger_param_1, ":object"),
        		(store_trigger_param_2, ":value"),
        		
        		(assign, ":current_city", "$temp"),
        		
        		(try_begin),
        			(eq, ":object", "$g_presentation_cancel"),
        			(presentation_set_duration, 1),
        		(else_try),
        			(eq, ":object", "$g_presentation_ok"),
        			
        			(call_script, "script_calculate_hire_troop_cost", ":current_city", "$g_player_troop"),
        			(assign, ":total_cost", reg0),
        			(assign, ":total_num_troops", reg1),
        			(party_get_free_companions_capacity, ":free_slots", "$g_player_party"),
        			
        			(store_troop_gold, ":player_gold", "$g_player_troop"),
        			(try_begin),
        				(gt, ":total_cost", ":player_gold"),
        				(assign, reg2, ":player_gold"),
        				(display_message, "@You do not have enough gold! You currently possess {reg2} denars.", text_color_impossible),
        			(else_try),
        				(gt, ":total_num_troops", ":free_slots"),
        				(assign, reg2, ":free_slots"),
        				(display_message, "@Party size not big enough! You can only hold up to {reg2} more troops", text_color_impossible),
                    (else_try),
                        (call_script, "script_party_get_prefered_wages_limit", ":current_city"),
                        (assign, ":limit", reg1),
                        (call_script, "script_party_get_wages", ":current_city"),
                        (assign, ":current_wages", reg0),
                        (assign, ":temp_wages", 0),
                        (party_get_num_companion_stacks, ":num_stacks", ":current_city"),
                        (try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
                            (party_stack_get_troop_id, ":troop_no", ":current_city", ":stack_no"),
                            (troop_get_slot, ":num_troops", ":troop_no", slot_troop_temp_hire_number),
                            (call_script, "script_troop_get_wages", ":troop_no"),
                            (store_mul, ":stack_wages", reg0, ":num_troops"),
                            (val_add, ":temp_wages", ":stack_wages"),
                        (try_end),

                        (call_script, "script_party_get_wages_modifier", ":current_city"),
                        (assign, ":modifier", reg0),

                        (val_mul, ":temp_wages", ":modifier"),
                        (val_div, ":temp_wages", 100),

                        (val_sub, ":current_wages", ":temp_wages"),

                        (gt, ":limit", ":current_wages"),
                        (display_message, "@Center cannot give out this many troops", text_color_impossible),
        			(else_try),
        				(party_get_num_companion_stacks, ":num_stacks", ":current_city"),
        				(try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
        					(party_stack_get_troop_id, ":troop_no", ":current_city", ":stack_no"),
        					(troop_get_slot, ":num_troops", ":troop_no", slot_troop_temp_hire_number),
        					(gt, ":num_troops", 0),
        					(party_add_members, "$g_player_party", ":troop_no", ":num_troops"),
        					(assign, ":really_removed", reg0),
        					(try_begin),
        						# We added the correct number of troops
        						(eq, ":num_troops", ":really_removed"),
        						(party_remove_members, ":current_city", ":troop_no", ":num_troops"),
        					(else_try),
        						(store_sub, ":num_troops_not_added", ":num_troops", ":really_removed"),
        						(party_remove_members, ":current_city", ":troop_no", ":really_removed"),
        						
        						(str_store_troop_name, s10, ":troop_no"),
        						(display_message, "@Impossible to add all troops of type {s10}, {reg0} have been added.", 0xbb0000),
        						(call_script, "script_troop_get_cost", ":troop_no"),
        						(val_mul, ":num_troops_not_added", reg0),
        						
        						(call_script, "script_troop_get_cost_modifier", ":troop_no", ":current_city", "$g_player_troop"),
        						(assign, ":cost_modifier", reg0),
        						(val_mul, ":num_troops_not_added", ":cost_modifier"),
        						(val_div, ":num_troops_not_added", 100),
        						
        						(val_sub, ":total_cost", ":num_troops_not_added"),
        						(display_message, "@Total cost has been adjusted.", 0xbb0000),
        					(try_end),
        				(try_end),

                        (call_script, "script_party_add_accumulated_taxes", ":current_city", ":total_cost", tax_type_troops_selling),
                        (store_mul, ":player_cost", ":total_cost", -1),
                        (call_script, "script_party_modify_wealth", "$g_player_party", ":player_cost"),
        				# Restart the presentation
        				(assign, "$temp", ":current_city"),
        				(start_presentation, "prsnt_recruit_from_town_garrison"),
        			(try_end),
        		(else_try),
        			(is_between, ":object", "$g_hire_soldiers_center_troops_begin", "$g_hire_soldiers_center_troops_end"),
        			
        			# (party_get_num_companion_stacks, ":num_stacks", ":current_city"),
        			(store_sub, ":troop_stack", ":object", "$g_hire_soldiers_center_troops_begin"),
        			(val_div, ":troop_stack", 2),

                    # (try_for_range, ":cur_stack", 0, ":troop_stack"),
                    #     (party_stack_get_troop_id, ":troop_no", "$temp", ":cur_stack"),
                    #     (troop_is_hero, ":troop_no"),
                    #     (val_sub, ":troop_stack", 1),
                    # (try_end),

        			(party_stack_get_troop_id, ":troop_no", ":current_city", ":troop_stack"),
        			(troop_set_slot, ":troop_no", slot_troop_temp_hire_number, ":value"),
        			(overlay_set_val, ":object", ":value"),
        			
        			(call_script, "script_calculate_hire_troop_cost", ":current_city", "$g_player_troop"),
        			(assign, ":total_cost", reg0),
        			(assign, ":num_troops", reg1),
        			(overlay_set_text, "$g_hire_soldiers_total_cost", "@Total cost: {reg0} denars"),
        			
        			(party_get_num_companions, ":total", "$g_player_party"),
        			(val_add, ":total", ":num_troops"),
        			(assign, reg11, ":total"),
        			(overlay_set_text, "$g_hire_soldiers_free_capacity", "@Party size: {reg11}"),
        			(try_begin),
        				(store_troop_gold, ":player_gold", "$g_player_troop"),
        				(gt, ":total_cost", ":player_gold"),
        				(overlay_set_color, "$g_hire_soldiers_total_cost", text_color_impossible),
        			(else_try),
        				(overlay_set_color, "$g_hire_soldiers_total_cost", text_color_default),
        			(try_end),

                    (call_script, "script_party_get_prefered_wages_limit", ":current_city"),
                    (assign, ":limit", reg1),
                    (call_script, "script_party_get_wages", ":current_city"),
                    (assign, ":current_wages", reg0),
                    (assign, ":temp_wages", 0),
                    (party_get_num_companion_stacks, ":num_stacks", ":current_city"),
                    (try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
                        (party_stack_get_troop_id, ":troop_no", ":current_city", ":stack_no"),
                        (troop_get_slot, ":num_troops", ":troop_no", slot_troop_temp_hire_number),
                        (call_script, "script_troop_get_wages", ":troop_no"),
                        (store_mul, ":stack_wages", reg0, ":num_troops"),
                        (val_add, ":temp_wages", ":stack_wages"),
                    (try_end),

                    (call_script, "script_party_get_wages_modifier", ":current_city"),
                    (assign, ":modifier", reg0),

                    (val_mul, ":temp_wages", ":modifier"),
                    (val_div, ":temp_wages", 100),

                    (val_sub, ":current_wages", ":temp_wages"),

                    (assign, reg10, ":limit"),
                    (assign, reg11, ":current_wages"),
                    (overlay_set_text, "$g_hire_soldiers_min_capacity", "@Center recruitment limit: {reg11}/{reg10}"),

                    (try_begin),
                        (gt, ":limit", ":current_wages"),
                        (overlay_set_color, "$g_hire_soldiers_min_capacity", text_color_impossible),
                    (else_try),
                        (overlay_set_color, "$g_hire_soldiers_min_capacity", text_color_default),
                    (try_end),
        		# (else_try),
        			# (display_message, "@Event change, not a known object."),
        		(try_end),
        	]),
        ]),

    ("intro_select_kingdom", 0, mesh_load_window, 
        [
        	(ti_on_presentation_load,
        	[
        		(set_fixed_point_multiplier, 1000),
        		
        		# Culture selection
        		(str_store_string, s10, "@Select a culture you wish to start as"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, 50, 550, 1000, 1000),
        		
        		(create_combo_button_overlay, "$g_presentation_culture_choice"),
        		(position_set_x, pos1, 240),
        		(position_set_y, pos1, 500),
        		(overlay_set_position, "$g_presentation_culture_choice", pos1),
        		(position_set_x, pos1, 1000),
        		(position_set_y, pos1, 1000),
        		(overlay_set_size, "$g_presentation_culture_choice", pos1),
        		
        		(try_for_range_backwards, ":culture", cultures_begin, cultures_end),
        			(str_store_faction_name, s10, ":culture"),
        			(overlay_add_item, "$g_presentation_culture_choice", s10),
        		(try_end),
        		(overlay_set_val, "$g_presentation_culture_choice", 6),

                (assign, "$g_presentation_culture", cultures_begin),
        		
        		# Accept button
        		(create_game_button_overlay, "$g_presentation_ok", "@Accept"),
        		(position_set_x, pos1, 150),
        		(position_set_y, pos1, 120),
        		(overlay_set_position, "$g_presentation_ok", pos1),
        		
        		# Cancel button
        		# (create_button_overlay, "$g_presentation_cancel", "@Cancel"),
        		# (position_set_x, pos1, 50),
        		# (position_set_y, pos1, 90),
        		# (overlay_set_position, "$g_presentation_cancel", pos1),
        		
        		(presentation_set_duration, 999999),
        	]),
        	
        	(ti_on_presentation_event_state_change,
        	[
        		(store_trigger_param_1, ":object"),
        		(store_trigger_param_2, ":value"),
        		
        		(try_begin),
        			(eq, ":object", "$g_presentation_ok"),
        			

                    (troop_set_slot, "$g_player_troop", slot_troop_culture, "$g_presentation_culture"),
                    (troop_set_slot, "$g_player_troop", slot_troop_original_faction, "$g_test_player_faction"),

        			(assign, reg10, "$g_test_player_faction"),
        			(str_store_faction_name, s10, "$g_test_player_faction"),
        			(display_message, "@Faction is {reg10}: {s10}"),
        			
        			(presentation_set_duration, 1),
        		(else_try),
        			(eq, ":object", "$g_presentation_culture_choice"),
        			
        			(store_sub, ":num_cultures", cultures_end, cultures_begin),
        			
        			(assign, ":faction", 0),
        			
        			(store_sub, ":culture", ":num_cultures", ":value"),
        			(val_sub, ":culture", 1),
        			(val_add, ":culture", cultures_begin),

                    (assign, "$g_presentation_culture", ":culture"),
        			        			
        			(assign, ":end", kingdoms_end),
        			(try_for_range, ":faction_no", kingdoms_begin, ":end"),
        				(faction_slot_eq, ":faction_no", slot_faction_culture, ":culture"),
        				(assign, ":faction", ":faction_no"),
        				(assign, ":end", 0),
        			(try_end),
        			(assign, "$g_test_player_faction", ":faction"),
        			
        			(assign, reg10, "$g_test_player_faction"),
        			(str_store_faction_name, s10, "$g_test_player_faction"),
        			(display_message, "@Faction is {reg10}: {s10}"),
        		(try_end),
        	]),
        ]),

    # prsnt_budget_report
        # Presentation detailing budget management
        # Requires g_process_effects set to 1/0
        #   toggle processing of current effects (owned center taxes, party wages...)
    ("budget_report", 0, mesh_load_window,
        [
            (ti_on_presentation_load,
            [
                (set_fixed_point_multiplier, 1000),

                # Current state panel
                (str_store_string, s10, "@Current state"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, 50, 680, 1000, 1000),
                (assign, ":current_state_x", 0),
                (assign, ":current_state_values_x", 255),

                # Current effects panel
                (str_store_string, s10, "@Current effects"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, 355, 680, 1000, 1000),
                (assign, ":current_effects_x", 305),
                (assign, ":current_effects_values_x", 565),

                # Future state panel
                (str_store_string, s10, "@Future state"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, 665, 680, 1000, 1000),
                (assign, ":future_state_x", 615),
                (assign, ":future_state_values_x", 870),

                (str_clear, s0),
                (create_text_overlay, reg0, s0, tf_scrollable),
                (position_set_x, pos1, 50),
                (position_set_y, pos1, 100),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 880),
                (position_set_y, pos1, 550),
                (overlay_set_area_size, reg0, pos1),
                
                (set_container_overlay, reg0),

                (assign, ":cur_y", 10),
                (assign, ":line_height", line_height),
                (assign, ":category_height", category_height),
                (assign, ":num_lines", 3),
                (store_mul, ":center_line_height", ":line_height", ":num_lines"),
                (val_add, ":center_line_height", 10),
                (try_for_range_backwards, ":center", centers_begin, centers_end),
                    (assign, ":display_name", 0),
                    (assign, ":go_back", 1),
                    (try_begin),
                        (call_script, "script_cf_party_has_building", ":center", "itm_building_bank"),

                        (party_get_slot, ":bank_amount", ":center", slot_party_bank_amount),
                        (gt, ":bank_amount", 0),

                        (str_store_string, s10, "@Bank funds:"),
                        (call_script, "script_presentation_create_text_overlay", tf_left_align, ":current_state_x", ":cur_y", 1000, 1000),
                        (overlay_set_color, reg0, text_color_budget_neutral),

                        (assign, reg10, ":bank_amount"),
                        (str_store_string, s10, "@{reg10}"),
                        (call_script, "script_presentation_create_text_overlay", tf_right_align, ":current_state_values_x", ":cur_y", 1000, 1000),
                        (overlay_set_color, reg0, text_color_budget_neutral),

                        (assign, ":bank_interests", 0),
                        (try_begin),
                            (eq, "$g_process_effects", 1),
                            (call_script, "script_party_get_bank_interests", ":center", ":bank_amount"),
                            (assign, ":bank_interests", reg0),

                            (set_fixed_point_multiplier, 1000),

                            (str_store_string, s10, "@Bank interests:"),
                            (call_script, "script_presentation_create_text_overlay", tf_left_align, ":current_effects_x", ":cur_y", 1000, 1000),
                            (overlay_set_color, reg0, text_color_budget_neutral),

                            (assign, reg10, ":bank_interests"),
                            (str_store_string, s10, "@+{reg10}"),
                            (call_script, "script_presentation_create_text_overlay", tf_right_align, ":current_effects_values_x", ":cur_y", 1000, 1000),
                            (overlay_set_color, reg0, text_color_budget_info),
                        (try_end),

                        (str_store_string, s10, "@Bank funds total:"),
                        (call_script, "script_presentation_create_text_overlay", tf_left_align, ":future_state_x", ":cur_y", 1000, 1000),
                        (overlay_set_color, reg0, text_color_budget_neutral),
                        
                        (store_add, reg10, ":bank_amount", ":bank_interests"),
                        (str_store_string, s10, "@{reg10}"),
                        (call_script, "script_presentation_create_text_overlay", tf_right_align, ":future_state_values_x", ":cur_y", 1000, 1000),
                        (overlay_set_color, reg0, text_color_budget_neutral),
                        
                        (assign, ":go_back", 0),
                        (assign, ":display_name", 1),
                    (try_end),

                    (party_get_slot, ":leader", ":center", slot_party_leader),
                    (try_begin),
                        (eq, ":leader", "$g_player_troop"),
                        (try_begin),
                            (eq, ":display_name", 1),
                            (val_add, ":cur_y", ":category_height"),
                        (try_end),
                        (assign, ":display_name", 1),

                        (party_get_slot, ":last_wealth", ":center", slot_party_budget_last_wealth),
                        (party_get_slot, ":current_wealth", ":center", slot_party_wealth),
                        # (is_between, ":center", towns_begin, towns_end),

                        # (call_script, "script_party_get_wages", ":center"),
                        # (store_mul, ":center_wages", reg0, -1),

                        (assign, ":total_budget", 0),
                        (try_for_range_backwards, ":tax_slot", slot_party_buget_taxes_begin, slot_party_buget_taxes_end),
                            (store_sub, ":offset", ":tax_slot", slot_party_buget_taxes_begin),
                            (store_add, ":tax_description", ":offset", "str_party_tax_description_taxes"),

                            (party_get_slot, ":amount", ":center", ":tax_slot"),
                            (neq, ":amount", 0),

                            (str_store_string, s11, ":tax_description"),
                            (create_text_overlay, reg0, "@{s11}:", tf_left_align),
                            (position_set_x, pos1, ":current_effects_x"),
                            (position_set_y, pos1, ":cur_y"),
                            (overlay_set_position, reg0, pos1),
                            (position_set_x, pos1, 1000),
                            (position_set_y, pos1, 1000),
                            (overlay_set_size, reg0, pos1),
                            (overlay_set_color, reg0, text_color_budget_neutral),

                            (assign, reg10, ":amount"),
                            (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                            (position_set_x, pos1, ":current_effects_values_x"),
                            (position_set_y, pos1, ":cur_y"),
                            (overlay_set_position, reg0, pos1),
                            (position_set_x, pos1, 1000),
                            (position_set_y, pos1, 1000),
                            (overlay_set_size, reg0, pos1),
                            (try_begin),
                                (gt, ":amount", 0),
                                (overlay_set_color, reg0, text_color_budget_positive),
                            (else_try),
                                (overlay_set_color, reg0, text_color_budget_negative),
                            (try_end),
                            (val_add, ":total_budget", ":amount"),

                            (val_add, ":cur_y", ":line_height"),
                            (assign, ":go_back", 1),
                        (try_end),

                        (store_add, ":total", ":last_wealth", ":total_budget"),
                        (store_sub, ":missing", ":current_wealth", ":total"),

                        (try_begin),
                            (neq, ":missing", 0),
                            (create_text_overlay, reg0, "@Other spendings:", tf_left_align),
                            (position_set_x, pos1, ":current_effects_x"),
                            (position_set_y, pos1, ":cur_y"),
                            (overlay_set_position, reg0, pos1),
                            (position_set_x, pos1, 1000),
                            (position_set_y, pos1, 1000),
                            (overlay_set_size, reg0, pos1),
                            (overlay_set_color, reg0, text_color_budget_neutral),

                            (assign, reg10, ":missing"),
                            (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                            (position_set_x, pos1, ":current_effects_values_x"),
                            (position_set_y, pos1, ":cur_y"),
                            (overlay_set_position, reg0, pos1),
                            (position_set_x, pos1, 1000),
                            (position_set_y, pos1, 1000),
                            (overlay_set_size, reg0, pos1),
                            (try_begin),
                                (gt, ":missing", 0),
                                (overlay_set_color, reg0, text_color_budget_positive),
                            (else_try),
                                (overlay_set_color, reg0, text_color_budget_negative),
                            (try_end),
                            (val_add, ":cur_y", ":line_height"),
                            (assign, ":go_back", 1),
                        (try_end),

                        # We need to go back one row
                        (try_begin),
                            (eq, ":go_back", 1),
                            (val_sub, ":cur_y", ":line_height"),
                        (try_end),

                        (create_text_overlay, reg0, "@Past wealth:", tf_left_align),
                        (position_set_x, pos1, ":current_state_x"),
                        (position_set_y, pos1, ":cur_y"),
                        (overlay_set_position, reg0, pos1),
                        (position_set_x, pos1, 1000),
                        (position_set_y, pos1, 1000),
                        (overlay_set_size, reg0, pos1),
                        (overlay_set_color, reg0, text_color_budget_neutral),

                        (assign, reg10, ":last_wealth"),
                        (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                        (position_set_x, pos1, ":current_state_values_x"),
                        (position_set_y, pos1, ":cur_y"),
                        (overlay_set_position, reg0, pos1),
                        (position_set_x, pos1, 1000),
                        (position_set_y, pos1, 1000),
                        (overlay_set_size, reg0, pos1),
                        (overlay_set_color, reg0, text_color_budget_neutral),
                        
                        (try_begin),
                            (eq, "$g_process_effects", 1),
                        
                            (create_text_overlay, reg0, "@Total change:", tf_left_align),
                            (position_set_x, pos1, ":future_state_x"),
                            (position_set_y, pos1, ":cur_y"),
                            (overlay_set_position, reg0, pos1),
                            (position_set_x, pos1, 1000),
                            (position_set_y, pos1, 1000),
                            (overlay_set_size, reg0, pos1),
                            (overlay_set_color, reg0, text_color_budget_neutral),

                            (store_add, reg10, ":total_budget", ":missing"),
                            (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                            (position_set_x, pos1, ":future_state_values_x"),
                            (position_set_y, pos1, ":cur_y"),
                            (overlay_set_position, reg0, pos1),
                            (position_set_x, pos1, 1000),
                            (position_set_y, pos1, 1000),
                            (overlay_set_size, reg0, pos1),
                            (try_begin),
                                (ge, reg10, 0),
                                (overlay_set_color, reg0, text_color_budget_positive),
                            (else_try),
                                (overlay_set_color, reg0, text_color_budget_negative),
                            (try_end),

                            # We need to go back one row
                            (val_sub, ":cur_y", ":line_height"),

                            (create_text_overlay, reg0, "@Wealth:", tf_left_align),
                            (position_set_x, pos1, ":future_state_x"),
                            (position_set_y, pos1, ":cur_y"),
                            (overlay_set_position, reg0, pos1),
                            (position_set_x, pos1, 1000),
                            (position_set_y, pos1, 1000),
                            (overlay_set_size, reg0, pos1),
                            (overlay_set_color, reg0, text_color_budget_neutral),

                            (assign, reg10, ":current_wealth"),
                            (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                            (position_set_x, pos1, ":future_state_values_x"),
                            (position_set_y, pos1, ":cur_y"),
                            (overlay_set_position, reg0, pos1),
                            (position_set_x, pos1, 1000),
                            (position_set_y, pos1, 1000),
                            (overlay_set_size, reg0, pos1),
                            (try_begin),
                                (ge, ":current_wealth", 0),
                                (overlay_set_color, reg0, text_color_budget_neutral),
                            (else_try),
                                (overlay_set_color, reg0, text_color_budget_negative),
                            (try_end),

                            # Rollback previous line changes
                            (val_add, ":cur_y", ":line_height"),
                        (try_end),
                        (val_add, ":cur_y", ":line_height"),
                    (else_try),
                        (eq, ":display_name", 1),
                        (val_add, ":cur_y", ":line_height"),
                    (try_end),

                    (try_begin),
                        (eq, ":display_name", 1),
                        (str_store_party_name, s10, ":center"),

                        (create_text_overlay, reg0, "@{s10}", tf_left_align),
                        (position_set_x, pos1, ":current_state_x"),
                        (position_set_y, pos1, ":cur_y"),
                        (overlay_set_position, reg0, pos1),
                        (position_set_x, pos1, 1100),
                        (position_set_y, pos1, 1100),
                        (overlay_set_size, reg0, pos1),

                        (val_add, ":cur_y", ":category_height"),
                    (try_end),
                (try_end),

                (troop_get_slot, ":vassal_taxes", "$g_player_troop", slot_troop_budget_vassal_taxes),
                (troop_get_slot, ":member_taxes", "$g_player_troop", slot_troop_budget_faction_member_taxes),
                (troop_get_slot, ":faction_taxes", "$g_player_troop", slot_troop_budget_faction_funds),

                (party_get_slot, ":debt_interests", "$g_player_party", slot_party_budget_debts),

                (store_add, ":total_recieving", ":faction_taxes", ":member_taxes"),
                (val_add, ":total_recieving", ":vassal_taxes"),

                (store_troop_gold, ":player_gold", "$g_player_troop"),

                (call_script, "script_party_get_wages", "$g_player_party"),
                (store_mul, ":player_party_wages", reg0, -1),

                (store_add, ":player_party_remaining", ":player_gold", 0),

                (party_get_slot, ":player_party_debt", "$g_player_party", slot_party_unpaid_wages),

                (store_add, ":total_change", ":total_recieving", ":player_party_wages"),
                (val_add, ":total_change", ":debt_interests"),
                (val_sub, ":total_change", ":player_party_debt"),

                (store_mul, ":remaining_debt", ":total_change", -1),

                (assign, "$g_presentation_wages_amount_unpaid", ":remaining_debt"),

                (try_begin),
                    (lt, ":remaining_debt", 0),
                    (val_sub, ":player_party_remaining", ":remaining_debt"),
                    (assign, ":remaining_debt", 0),
                (try_end),

                (create_text_overlay, reg0, "@Remaining debt:", tf_left_align),
                (position_set_x, pos1, ":future_state_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (store_mul, reg10, ":remaining_debt", -1),
                (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                (position_set_x, pos1, ":future_state_values_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (try_begin),
                    (eq, ":remaining_debt", 0),
                    (overlay_set_color, reg0, text_color_budget_neutral),
                (else_try),
                    (overlay_set_color, reg0, text_color_budget_negative),
                (try_end),
                (assign, "$g_presentation_wages_remaining_unpaid", reg0),
                (try_begin),
                    (lt, ":debt_interests", 0),

                    (str_store_string, s10, "@Debt interests:"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":current_effects_x", ":cur_y", 1000, 1000),
                    (overlay_set_color, reg0, text_color_budget_neutral),

                    (assign, reg10, ":debt_interests"),
                    (str_store_string, s10, "@{reg10}"),
                    (call_script, "script_presentation_create_text_overlay", tf_right_align, ":current_effects_values_x", ":cur_y", 1000, 1000),
                    (overlay_set_color, reg0, text_color_budget_negative),
                (try_end),

                (str_store_string, s10, "@Current debt:"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":current_state_x", ":cur_y", 1000, 1000),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (store_mul, reg10, ":player_party_debt", -1),
                (str_store_string, s10, "@{reg10}"),
                (call_script, "script_presentation_create_text_overlay", tf_right_align, ":current_state_values_x", ":cur_y", 1000, 1000),
                (try_begin),
                    (eq, ":player_party_debt", 0),
                    (overlay_set_color, reg0, text_color_budget_neutral),
                (else_try),
                    (overlay_set_color, reg0, text_color_budget_negative),
                (try_end),

                (val_add, ":cur_y", ":line_height"),
                
                (str_store_string, s10, "@Remaining gold:"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":future_state_x", ":cur_y", 1000, 1000),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (assign, reg10, ":player_party_remaining"),
                (str_store_string, s10, "@{reg10}"),
                (call_script, "script_presentation_create_text_overlay", tf_right_align, ":future_state_values_x", ":cur_y", 1000, 1000),
                (overlay_set_color, reg0, text_color_budget_neutral),
                (assign, "$g_presentation_wages_remaining_gold", reg0),

                (assign, ":added_taxes", 0),

                (try_begin),
                    (neq, ":vassal_taxes", 0),
                    
                    (val_add, ":cur_y", ":line_height"),

                    (str_store_string, s10, "str_party_tax_description_vassal"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":current_effects_x", ":cur_y", 1000, 1000),
                    (overlay_set_color, reg0, text_color_budget_neutral),
                    (assign, reg10, ":vassal_taxes"),
                    (str_store_string, s10, "@{reg10}"),
                    (call_script, "script_presentation_create_text_overlay", tf_right_align, ":current_effects_values_x", ":cur_y", 1000, 1000),
                    
                    (assign, ":added_taxes", 1),
                    (try_begin),
                        (gt, ":vassal_taxes", 0),
                        (overlay_set_color, reg0, text_color_budget_positive),
                    (else_try),
                        (overlay_set_color, reg0, text_color_budget_negative),
                    (try_end),
                (try_end),

                (try_begin),
                    (neq, ":member_taxes", 0),

                    (val_add, ":cur_y", ":line_height"),

                    (str_store_string, s10, "str_party_tax_description_member"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":current_effects_x", ":cur_y", 1000, 1000),
                    (overlay_set_color, reg0, text_color_budget_neutral),
                    (assign, reg10, ":member_taxes"),
                    (str_store_string, s10, "@{reg10}"),
                    (call_script, "script_presentation_create_text_overlay", tf_right_align, ":current_effects_values_x", ":cur_y", 1000, 1000),
                    
                    (assign, ":added_taxes", 1),
                    (try_begin),
                        (gt, ":member_taxes", 0),
                        (overlay_set_color, reg0, text_color_budget_positive),
                    (else_try),
                        (overlay_set_color, reg0, text_color_budget_negative),
                    (try_end),
                (try_end),

                (try_begin),
                    (neq, ":faction_taxes", 0),

                    (val_add, ":cur_y", ":line_height"),

                    (str_store_string, s10, "str_party_tax_description_funds"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":current_effects_x", ":cur_y", 1000, 1000),
                    (overlay_set_color, reg0, text_color_budget_neutral),
                    (assign, reg10, ":faction_taxes"),
                    (str_store_string, s10, "@{reg10}"),
                    (call_script, "script_presentation_create_text_overlay", tf_right_align, ":current_effects_values_x", ":cur_y", 1000, 1000),
                    
                    (assign, ":added_taxes", 1),
                    (try_begin),
                        (gt, ":faction_taxes", 0),
                        (overlay_set_color, reg0, text_color_budget_positive),
                    (else_try),
                        (overlay_set_color, reg0, text_color_budget_negative),
                    (try_end),
                (try_end),

                (try_begin),
                    (eq, ":added_taxes", 0),
                    (val_add, ":cur_y", ":line_height"),
                (try_end),

                (str_store_string, s10, "@Amount to pay:"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":future_state_x", ":cur_y", 1000, 1000),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (assign, "$g_presentation_wages_amount_paying", 0),

                (try_begin),
                    (eq, "$g_process_effects", 1),
                    (store_add, ":max_wage_payment", ":player_gold", 1),
                    (assign, ":max_debt_payment", ":remaining_debt"),
                    (val_add, ":max_debt_payment", 1),
                    (val_min, ":max_wage_payment", ":max_debt_payment"),
                    (val_max, ":max_wage_payment", 0),
                    (create_number_box_overlay, reg0, 0, ":max_wage_payment"),
                    (store_add, ":position_x", ":future_state_x", 190),
                    (position_set_x, pos1, ":position_x"),
                (else_try),
                    (assign, reg10, 0),
                    (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                    (overlay_set_color, reg0, text_color_budget_neutral),
                    (position_set_x, pos1, ":future_state_values_x"),
                (try_end),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (assign, "$g_presentation_wages_pay_slider", reg0),

                (try_begin),
                    (eq, "$g_process_effects", 2),
                    (create_button_overlay, reg0, "@Pay all"),
                    (store_add, ":position_x", ":future_state_x", 215),
                    (position_set_x, pos1, ":position_x"),
                    (position_set_y, pos1, ":cur_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1000),
                    (position_set_y, pos1, 1000),
                    (overlay_set_size, reg0, pos1),
                    (assign, "$g_presentation_wages_pay_all", reg0),
                (try_end),

                (val_add, ":cur_y", ":line_height"),

                (str_store_string, s10, "@Wealth:"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":current_state_x", ":cur_y", 1000, 1000),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (assign, reg10, ":player_gold"),
                (str_store_string, s10, "@{reg10}"),
                (call_script, "script_presentation_create_text_overlay", tf_right_align, ":current_state_values_x", ":cur_y", 1000, 1000),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (str_store_string, s10, "@Wages:"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":current_effects_x", ":cur_y", 1000, 1000),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (assign, reg10, ":player_party_wages"),
                (str_store_string, s10, "@{reg10}"),
                (call_script, "script_presentation_create_text_overlay", tf_right_align, ":current_effects_values_x", ":cur_y", 1000, 1000),
                (overlay_set_color, reg0, text_color_budget_negative),

                (str_store_string, s10, "@Total change:"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":future_state_x", ":cur_y", 1000, 1000),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (assign, reg10, ":total_change"),
                (str_store_string, s10, "@{reg10}"),
                (call_script, "script_presentation_create_text_overlay", tf_right_align, ":future_state_values_x", ":cur_y", 1000, 1000),
                (try_begin),
                    (lt, ":total_change", 0),
                    (overlay_set_color, reg0, text_color_budget_negative),
                (else_try),
                    (gt, ":total_change", 0),
                    (overlay_set_color, reg0, text_color_budget_positive),
                (else_try),
                    (overlay_set_color, reg0, text_color_budget_neutral),
                (try_end),

                (val_add, ":cur_y", ":line_height"),

                (create_text_overlay, reg0, "@Main party", tf_left_align),
                (position_set_x, pos1, ":current_state_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1100),
                (position_set_y, pos1, 1100),
                (overlay_set_size, reg0, pos1),

                (set_container_overlay, -1),

                # Actions panel
                (create_game_button_overlay, "$g_presentation_ok", "@Continue"),
                (position_set_x, pos1, 150),
                (position_set_y, pos1, 50),
                (overlay_set_position, "$g_presentation_ok", pos1),

                (presentation_set_duration, 999999),
            ]),

            (ti_on_presentation_event_state_change,
            [
                (store_trigger_param_1, ":object"),
                (store_trigger_param_2, ":value"),

                (try_begin),
                    (eq, ":object", "$g_presentation_ok"),

                    (try_begin),
                        (eq, "$g_process_effects", 1),
                        (call_script, "script_party_pay_wages", "$g_player_party", "$g_presentation_wages_amount_paying"),

                        (try_begin),
                            (gt, "$g_presentation_wages_amount_unpaid", 0),
                            (party_set_slot, "$g_player_party", slot_party_unpaid_wages, "$g_presentation_wages_amount_unpaid"),
                            (call_script, "script_party_unpaid_wages_penalties", "$g_player_party"),
                        (else_try),
                            (party_set_slot, "$g_player_party", slot_party_unpaid_wages, 0),
                            (store_mul, ":change", "$g_presentation_wages_amount_unpaid", -1),
                            (gt, ":change", 0),
                            (call_script, "script_troop_change_wealth", "$g_player_troop", ":change"),
                        (try_end),

                        (call_script, "script_process_bank_interests"),

                        (call_script, "script_clean_budgets"),
                        (assign, "$g_process_effects", 0),
                    (try_end),
                    (presentation_set_duration, 0),
                (else_try),
                    (eq, ":object", "$g_presentation_wages_pay_slider"),

                    (assign, "$g_presentation_wages_amount_paying", ":value"),

                    (store_troop_gold, ":player_gold", "$g_player_troop"),
                    (store_sub, ":player_party_remaining", ":player_gold", ":value"),

                    (call_script, "script_party_get_wages", "$g_player_party"),
                    (assign, ":player_party_wages", reg0),
                    (store_sub, ":remaining_wages", ":player_party_wages", ":value"),
                    (party_get_slot, ":unpaid_wages", "$g_player_party", slot_party_unpaid_wages),

                    (troop_get_slot, ":vassal_taxes", "$g_player_troop", slot_troop_budget_vassal_taxes),
                    (troop_get_slot, ":member_taxes", "$g_player_troop", slot_troop_budget_faction_member_taxes),
                    (troop_get_slot, ":faction_taxes", "$g_player_troop", slot_troop_budget_faction_funds),

                    (party_get_slot, ":debt_interests", "$g_player_party", slot_party_budget_debts),

                    (try_begin),
                        (lt, ":remaining_wages", 0),
                        (val_add, ":unpaid_wages", ":remaining_wages"),
                    (else_try),
                        (val_add, ":player_party_remaining", ":remaining_wages"),
                    (try_end),
                    (val_sub, ":unpaid_wages", ":debt_interests"),
                    (val_sub, ":unpaid_wages", ":vassal_taxes"),
                    (val_sub, ":unpaid_wages", ":member_taxes"),
                    (val_sub, ":unpaid_wages", ":faction_taxes"),

                    (assign, reg10, ":player_party_remaining"),
                    (overlay_set_text, "$g_presentation_wages_remaining_gold", "@{reg10}"),

                    (store_mul, reg10, ":unpaid_wages", -1),
                    (overlay_set_text, "$g_presentation_wages_remaining_unpaid", "@{reg10}"),
                    (try_begin),
                        (eq, ":unpaid_wages", 0),
                        (overlay_set_color, "$g_presentation_wages_remaining_unpaid", text_color_budget_neutral),
                    (else_try),
                        (overlay_set_color, "$g_presentation_wages_remaining_unpaid", text_color_budget_negative),
                    (try_end),

                    (assign, "$g_presentation_wages_amount_unpaid", ":unpaid_wages"),
                (else_try),
                    (eq, ":object", "$g_presentation_wages_pay_all"),
                    (store_troop_gold, ":player_gold", "$g_player_troop"),

                    (call_script, "script_party_get_wages", "$g_player_party"),
                    (assign, ":player_party_wages", reg0),
                    (party_get_slot, ":unpaid_wages", "$g_player_party", slot_party_unpaid_wages),
                    (val_add, ":unpaid_wages", ":player_party_wages"),

                    (assign, ":amount_paid", ":player_gold"),
                    (val_min, ":amount_paid", ":unpaid_wages"),

                    (assign, "$g_presentation_wages_amount_paying", ":amount_paid"),

                    (overlay_set_val, "$g_presentation_wages_pay_slider", ":amount_paid"),

                    (store_sub, ":remaining_gold", ":player_gold", ":amount_paid"),
                    (assign, reg10, ":remaining_gold"),
                    (overlay_set_text, "$g_presentation_wages_remaining_gold", "@{reg10}"),

                    (store_sub, ":remaining_unpaid", ":unpaid_wages", ":amount_paid"),
                    (store_mul, reg10, ":remaining_unpaid", -1),
                    (overlay_set_text, "$g_presentation_wages_remaining_unpaid", "@{reg10}"),
                    (try_begin),
                        (eq, ":remaining_unpaid", 0),
                        (overlay_set_color, "$g_presentation_wages_remaining_unpaid", text_color_budget_neutral),
                    (else_try),
                        (overlay_set_color, "$g_presentation_wages_remaining_unpaid", text_color_budget_negative),
                    (try_end),

                (try_end),
            ]),
        ]),

    # prsnt_center_administration
        # Requires temp set to center id
    ("center_administration", 0, mesh_load_window,
        [
            (ti_on_presentation_load,
            [
                (assign, ":current_center", "$temp"),

                (set_fixed_point_multiplier, 1000),

                (str_store_party_name, s10, ":current_center"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, 50, 680, 1200, 1200),

                (str_clear, s0),
                (create_text_overlay, reg0, s0, tf_scrollable),
                (position_set_x, pos1, 50),
                (position_set_y, pos1, 100),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 880),
                (position_set_y, pos1, 550),
                (overlay_set_area_size, reg0, pos1),
                
                (set_container_overlay, reg0),
                (assign, ":cur_y", 10),
                (assign, ":line_height", line_height),
                (assign, ":category_height", category_height),
                (assign, ":left_panel_x", 0),
                (assign, ":left_panel_values_x", 385),
                (assign, ":right_panel_x", 435),
                (assign, ":right_panel_values_x", 870),

                (party_get_slot, ":lord", ":current_center", slot_party_lord),
                (try_begin),
                    (eq, ":lord", "$g_player_troop"),
                    (assign, "$g_presentation_readonly", 0),
                (else_try),
                    (assign, "$g_presentation_readonly", 1),
                (try_end),

                (party_get_slot, ":prisoner_outcome", ":current_center", slot_party_max_prisoner_outcome),

                (str_store_string, s10, "@Allow ransoming prisoners"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":left_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":left_panel_values_x", checkbox_size),
                (store_and, ":value", ":prisoner_outcome", mpo_ransom),
                (call_script, "script_presentation_create_check_box_overlay", ":x", ":cur_y", ":value"),
                (assign, "$g_presentation_center_prisoner_outcome_flags_ransom", reg0),

                (str_store_string, s10, "@Allow enslaving prisoners"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":right_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":right_panel_values_x", checkbox_size),
                (store_and, ":value", ":prisoner_outcome", mpo_slave),
                (call_script, "script_presentation_create_check_box_overlay", ":x", ":cur_y", ":value"),
                (assign, "$g_presentation_center_prisoner_outcome_flags_enslave", reg0),

                (val_add, ":cur_y", ":line_height"),

                (str_store_string, s10, "@Allow releasing prisoners"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":left_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":left_panel_values_x", checkbox_size),
                (store_and, ":value", ":prisoner_outcome", mpo_release),
                (call_script, "script_presentation_create_check_box_overlay", ":x", ":cur_y", ":value"),
                (assign, "$g_presentation_center_prisoner_outcome_flags_release", reg0),

                (str_store_string, s10, "@Allow recruiting prisoners"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":right_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":right_panel_values_x", checkbox_size),
                (store_and, ":value", ":prisoner_outcome", mpo_recruit),
                (call_script, "script_presentation_create_check_box_overlay", ":x", ":cur_y", ":value"),
                (assign, "$g_presentation_center_prisoner_outcome_flags_recruit", reg0),

                (val_add, ":cur_y", ":line_height"),

                (party_get_slot, reg10, ":current_center", slot_party_max_prisoner_ratio),
                (str_store_string, s10, "@Prisoners handled when above {reg10}% of party size"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":right_panel_x", ":cur_y", 1000, 1000),

                (str_store_string, s10, "@Prisoners management"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":left_panel_x", ":cur_y", 1000, 1000),

                (val_add, ":cur_y", ":category_height"),
                
                ## CENTER GARRISON
                # Center garrison sending
                (party_get_slot, ":garrison_masks", ":current_center", slot_party_player_garrison_flags),

                (str_store_string, s10, "@Noble troops"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":left_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":left_panel_values_x", 20),
                (call_script, "script_presentation_create_combo_button_overlay", ":x", ":cur_y", 550, 700),

                (overlay_add_item, reg0, "@Disabled"),
                (overlay_add_item, reg0, "@Allowed"),

                (assign, "$g_presentation_center_garrison_flags_send_noble", reg0),

                (try_begin),
                    (store_and, ":noble_flags", ":garrison_masks", pgf_send_noble),
                    (gt, ":noble_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_send_noble", 1),
                (else_try),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_send_noble", 0),
                (try_end),

                (val_add, ":cur_y", ":line_height"),

                (str_store_string, s10, "@Elite troops"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":right_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":right_panel_values_x", 20),
                (call_script, "script_presentation_create_combo_button_overlay", ":x", ":cur_y", 550, 700),

                (overlay_add_item, reg0, "@Disabled"),
                (overlay_add_item, reg0, "@Allowed"),

                (assign, "$g_presentation_center_garrison_flags_send_elite", reg0),

                (try_begin),
                    (store_and, ":elite_flags", ":garrison_masks", pgf_send_elite),
                    (gt, ":elite_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_send_elite", 1),
                (else_try),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_send_elite", 0),
                (try_end),

                (str_store_string, s10, "@Veteran troops"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":left_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":left_panel_values_x", 20),
                (call_script, "script_presentation_create_combo_button_overlay", ":x", ":cur_y", 550, 700),

                (overlay_add_item, reg0, "@Disabled"),
                (overlay_add_item, reg0, "@Allowed"),

                (assign, "$g_presentation_center_garrison_flags_send_veteran", reg0),

                (try_begin),
                    (store_and, ":veteran_flags", ":garrison_masks", pgf_send_veteran),
                    (gt, ":veteran_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_send_veteran", 1),
                (else_try),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_send_veteran", 0),
                (try_end),

                (val_add, ":cur_y", ":line_height"),

                (str_store_string, s10, "@Common troops"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":right_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":right_panel_values_x", 20),
                (call_script, "script_presentation_create_combo_button_overlay", ":x", ":cur_y", 550, 700),

                (overlay_add_item, reg0, "@Disabled"),
                (overlay_add_item, reg0, "@Allowed"),

                (assign, "$g_presentation_center_garrison_flags_send_common", reg0),

                (try_begin),
                    (store_and, ":common_flags", ":garrison_masks", pgf_send_common),
                    (gt, ":common_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_send_common", 1),
                (else_try),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_send_common", 0),
                (try_end),

                (str_store_string, s10, "@Levy troops"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":left_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":left_panel_values_x", 20),
                (call_script, "script_presentation_create_combo_button_overlay", ":x", ":cur_y", 550, 700),

                (overlay_add_item, reg0, "@Disabled"),
                (overlay_add_item, reg0, "@Allowed"),

                (assign, "$g_presentation_center_garrison_flags_send_levy", reg0),

                (try_begin),
                    (store_and, ":levy_flags", ":garrison_masks", pgf_send_levy),
                    (gt, ":levy_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_send_levy", 1),
                (else_try),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_send_levy", 0),
                (try_end),

                (val_add, ":cur_y", ":line_height"),

                (str_store_string, s10, "@Allow sending troops to other centers from garrison"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":left_panel_x", ":cur_y", 1000, 1000),

                (val_add, ":cur_y", ":category_height"),

                # Center garrison selling

                (str_store_string, s10, "@Noble troops"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":left_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":left_panel_values_x", 20),
                (call_script, "script_presentation_create_combo_button_overlay", ":x", ":cur_y", 550, 700),

                (overlay_add_item, reg0, "@Disabled"),
                (overlay_add_item, reg0, "@Allow vassals"),
                (overlay_add_item, reg0, "@Allow faction members"),
                (overlay_add_item, reg0, "@Allow anyone"),
                (assign, "$g_presentation_center_garrison_flags_noble", reg0),

                (try_begin),
                    (store_and, ":noble_flags", ":garrison_masks", pgf_sell_noble_unknown),
                    (gt, ":noble_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_noble", 3),
                (else_try),
                    (store_and, ":noble_flags", ":garrison_masks", pgf_sell_noble_faction),
                    (gt, ":noble_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_noble", 2),
                (else_try),
                    (store_and, ":noble_flags", ":garrison_masks", pgf_sell_noble_vassals),
                    (gt, ":noble_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_noble", 1),
                (try_end),

                (val_add, ":cur_y", ":line_height"),

                (str_store_string, s10, "@Elite troops"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":right_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":right_panel_values_x", 20),
                (call_script, "script_presentation_create_combo_button_overlay", ":x", ":cur_y", 550, 700),

                (overlay_add_item, reg0, "@Disabled"),
                (overlay_add_item, reg0, "@Allow vassals"),
                (overlay_add_item, reg0, "@Allow faction members"),
                (overlay_add_item, reg0, "@Allow anyone"),
                (assign, "$g_presentation_center_garrison_flags_elite", reg0),

                (try_begin),
                    (store_and, ":elite_flags", ":garrison_masks", pgf_sell_elite_unknown),
                    (gt, ":elite_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_elite", 3),
                (else_try),
                    (store_and, ":elite_flags", ":garrison_masks", pgf_sell_elite_faction),
                    (gt, ":elite_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_elite", 2),
                (else_try),
                    (store_and, ":elite_flags", ":garrison_masks", pgf_sell_elite_vassals),
                    (gt, ":elite_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_elite", 1),
                (try_end),

                (str_store_string, s10, "@Veteran troops"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":left_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":left_panel_values_x", 20),
                (call_script, "script_presentation_create_combo_button_overlay", ":x", ":cur_y", 550, 700),

                (overlay_add_item, reg0, "@Disabled"),
                (overlay_add_item, reg0, "@Allow vassals"),
                (overlay_add_item, reg0, "@Allow faction members"),
                (overlay_add_item, reg0, "@Allow anyone"),
                (assign, "$g_presentation_center_garrison_flags_veteran", reg0),

                (try_begin),
                    (store_and, ":veteran_flags", ":garrison_masks", pgf_sell_veteran_unknown),
                    (gt, ":veteran_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_veteran", 3),
                (else_try),
                    (store_and, ":veteran_flags", ":garrison_masks", pgf_sell_veteran_faction),
                    (gt, ":veteran_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_veteran", 2),
                (else_try),
                    (store_and, ":veteran_flags", ":garrison_masks", pgf_sell_veteran_vassals),
                    (gt, ":veteran_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_veteran", 1),
                (try_end),

                (val_add, ":cur_y", ":line_height"),

                (str_store_string, s10, "@Common troops"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":right_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":right_panel_values_x", 20),
                (call_script, "script_presentation_create_combo_button_overlay", ":x", ":cur_y", 550, 700),

                (overlay_add_item, reg0, "@Disabled"),
                (overlay_add_item, reg0, "@Allow vassals"),
                (overlay_add_item, reg0, "@Allow faction members"),
                (overlay_add_item, reg0, "@Allow anyone"),
                (assign, "$g_presentation_center_garrison_flags_common", reg0),

                (try_begin),
                    (store_and, ":common_flags", ":garrison_masks", pgf_sell_common_unknown),
                    (gt, ":common_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_common", 3),
                (else_try),
                    (store_and, ":common_flags", ":garrison_masks", pgf_sell_common_faction),
                    (gt, ":common_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_common", 2),
                (else_try),
                    (store_and, ":common_flags", ":garrison_masks", pgf_sell_common_vassals),
                    (gt, ":common_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_common", 1),
                (try_end),

                (str_store_string, s10, "@Levies"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":left_panel_x", ":cur_y", 1000, 1000),

                (store_sub, ":x", ":left_panel_values_x", 20),
                (call_script, "script_presentation_create_combo_button_overlay", ":x", ":cur_y", 550, 700),

                (overlay_add_item, reg0, "@Disabled"),
                (overlay_add_item, reg0, "@Allow vassals"),
                (overlay_add_item, reg0, "@Allow faction members"),
                (overlay_add_item, reg0, "@Allow anyone"),
                (assign, "$g_presentation_center_garrison_flags_levy", reg0),

                (try_begin),
                    (store_and, ":levy_flags", ":garrison_masks", pgf_sell_levy_unknown),
                    (gt, ":levy_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_levy", 3),
                (else_try),
                    (store_and, ":levy_flags", ":garrison_masks", pgf_sell_levy_faction),
                    (gt, ":levy_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_levy", 2),
                (else_try),
                    (store_and, ":levy_flags", ":garrison_masks", pgf_sell_levy_vassals),
                    (gt, ":levy_flags", 0),
                    (overlay_set_val, "$g_presentation_center_garrison_flags_levy", 1),
                (try_end),

                (val_add, ":cur_y", ":line_height"),

                (str_store_string, s10, "@Allow selling troops from garrison"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":left_panel_x", ":cur_y", 1000, 1000),

                (val_add, ":cur_y", ":category_height"),

                # Center garrison size
                (call_script, "script_party_get_expected_taxes", ":current_center"),
                (assign, ":expected_taxes", reg0),
                (val_mul, ":expected_taxes", 12),

                (try_begin),
                    (eq, "$g_presentation_readonly", 0),

                    (party_get_slot, ":wages_limit", ":current_center", slot_party_player_wages_limit),

                    (assign, ":enable_garrison_management", 0),
                    (try_begin),
                        (ge, ":wages_limit", 0),
                        (assign, ":enable_garrison_management", 1),
                    (try_end),

                    (str_store_string, s10, "@Percentage of expected taxes"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":right_panel_x", ":cur_y", 1000, 1000),
                    (try_begin),
                        (eq, ":enable_garrison_management", 0),
                        (overlay_set_display, reg0, 0),
                    (try_end),
                    (assign, "$g_presentation_center_wages_percent_label", reg0),

                    (try_begin),
                        (eq, ":enable_garrison_management", 1),
                        (store_mul, reg10, ":wages_limit", 100),
                        (val_div, reg10, ":expected_taxes"),
                        (str_store_string, s10, "@{reg10}%"),
                    (else_try),
                        (str_store_string, s10, "@-"),
                    (try_end),
                    (call_script, "script_presentation_create_text_overlay", tf_right_align, ":right_panel_values_x", ":cur_y", 1000, 1000),
                    (try_begin),
                        (eq, ":enable_garrison_management", 0),
                        (overlay_set_display, reg0, 0),
                    (try_end),
                    (assign, "$g_presentation_center_wages_percent", reg0),

                    (val_add, ":cur_y", ":line_height"),

                    (str_store_string, s10, "@Automatic garrison size manager"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":left_panel_x", ":cur_y", 1000, 1000),
                    (overlay_set_size, reg0, pos1),

                    (store_sub, ":pos", ":left_panel_values_x", checkbox_size),
                    (store_sub, ":value", 1, ":enable_garrison_management"),
                    (call_script, "script_presentation_create_check_box_overlay", ":pos", ":cur_y", ":value"),
                    (assign, "$g_presentation_center_garrison_manager", reg0),

                    (str_store_string, s10, "@Wanted garrison wages"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":right_panel_x", ":cur_y", 1000, 1000),
                    (try_begin),
                        (eq, ":enable_garrison_management", 0),
                        (overlay_set_display, reg0, 0),
                    (try_end),
                    (assign, "$g_presentation_center_garrison_wages_label", reg0),

                    (store_mul, ":max", ":expected_taxes", 100),
                    (val_add, ":max", 1),
                    (create_number_box_overlay, reg0, 0, ":max"),
                    (store_sub, ":pos", ":right_panel_values_x", numberbox_size),
                    (position_set_x, pos1, ":pos"),
                    (position_set_y, pos1, ":cur_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1500),
                    (position_set_y, pos1, 1000),
                    (overlay_set_size, reg0, pos1),
                    (try_begin),
                        (eq, ":enable_garrison_management", 1),
                        (overlay_set_val, reg0, ":wages_limit"),
                    (else_try),
                        (overlay_set_display, reg0, 0),
                    (try_end),
                    (assign, "$g_presentation_center_garrison_wages", reg0),

                    (val_add, ":cur_y", ":category_height"),
                (try_end),

                ## CENTER POLICIES
                # Center taxes

                (str_store_string, s10, "@Buying tax rate"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":left_panel_x", ":cur_y", 1000, 1000),

                (party_get_slot, ":buy_rate", ":current_center", slot_party_taxes_buy),
                (try_begin),
                    (eq, "$g_presentation_readonly", 0),
                    (assign, ":max", 100),
                    (create_number_box_overlay, reg0, 0, ":max"),
                    (store_sub, ":pos", ":left_panel_values_x", numberbox_size),
                (else_try),
                    (assign, reg10, ":buy_rate"),
                    (create_text_overlay, reg0, "@{reg10}"),
                    (assign, ":pos", ":left_panel_values_x"),
                (try_end),
                (position_set_x, pos1, ":pos"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (overlay_set_val, reg0, ":buy_rate"),
                (assign, "$g_presentation_center_tax_rate_buy_select", reg0),

                (create_text_overlay, reg0, "@Selling tax rate", tf_left_align),
                (position_set_x, pos1, ":right_panel_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),

                (party_get_slot, ":sell_rate", ":current_center", slot_party_taxes_sell),
                (try_begin),
                    (eq, "$g_presentation_readonly", 0),
                    (assign, ":max", 100),
                    (create_number_box_overlay, reg0, 0, ":max"),
                    (store_sub, ":pos", ":right_panel_values_x", numberbox_size),
                (else_try),
                    (assign, reg10, ":sell_rate"),
                    (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                    (assign, ":pos", ":right_panel_values_x"),
                (try_end),
                (position_set_x, pos1, ":pos"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (overlay_set_val, reg0, ":sell_rate"),
                (assign, "$g_presentation_center_tax_rate_sell_select", reg0),

                (val_add, ":cur_y", ":line_height"),

                (create_text_overlay, reg0, "@Tax rate", tf_left_align),
                (position_set_x, pos1, ":left_panel_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),

                (party_get_slot, ":tax_rate", ":current_center", slot_party_taxes_fixed),
                (try_begin),
                    (eq, "$g_presentation_readonly", 0),
                    (assign, ":max", 100),
                    (create_number_box_overlay, reg0, 0, ":max"),
                    (store_sub, ":pos", ":left_panel_values_x", numberbox_size),
                (else_try),
                    (assign, reg10, ":tax_rate"),
                    (create_text_overlay, reg0, "@{reg10}"),
                    (assign, ":pos", ":left_panel_values_x"),
                (try_end),
                (position_set_x, pos1, ":pos"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (overlay_set_val, reg0, ":tax_rate"),
                (assign, "$g_presentation_center_tax_rate_fixed_select", reg0),

                (str_store_string, s10, "@Estimated yearly taxes: "),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":right_panel_x", ":cur_y", 1000, 1000),

                (assign, ":max", 100),

                (assign, reg10, ":expected_taxes"),
                (str_store_string, s10, "@{reg10}"),
                (call_script, "script_presentation_create_text_overlay", tf_right_align, ":right_panel_values_x", ":cur_y", 1000, 1000),
                (assign, "$g_presentation_center_tax_rate_fixed_estimation", reg0),

                (val_add, ":cur_y", ":category_height"),

                ## CENTER WEALTH
                # Center treasury
                (try_begin),
                    (eq, "$g_presentation_readonly", 0),

                    (party_get_slot, ":center_wealth", ":current_center", slot_party_wealth),
                    (store_troop_gold, ":player_wealth", "$g_player_troop"),

                    (store_add, ":max", ":center_wealth", 1),
                    (create_number_box_overlay, reg0, 0, ":max"),
                    (store_add, ":pos", ":left_panel_x", numberbox_padding),
                    (position_set_x, pos1, ":pos"),
                    (position_set_y, pos1, ":cur_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1000),
                    (position_set_y, pos1, 1000),
                    (overlay_set_size, reg0, pos1),
                    (assign, "$g_presentation_center_wealth_select", reg0),

                    (assign, reg10, ":center_wealth"),
                    (create_button_overlay, reg0, "@Withdraw", tf_right_align),
                    (store_add, ":pos", ":left_panel_values_x", button_padding),
                    (position_set_x, pos1, ":pos"),
                    (position_set_y, pos1, ":cur_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1000),
                    (position_set_y, pos1, 1000),
                    (overlay_set_size, reg0, pos1),
                    (assign, "$g_presentation_withdraw", reg0),

                    (store_add, ":max", ":player_wealth", 1),
                    (create_number_box_overlay, reg0, 0, ":max"),
                    (store_add, ":pos", ":right_panel_x", numberbox_padding),
                    (position_set_x, pos1, ":pos"),
                    (position_set_y, pos1, ":cur_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1000),
                    (position_set_y, pos1, 1000),
                    (overlay_set_size, reg0, pos1),
                    (assign, "$g_presentation_player_wealth_select", reg0),

                    (assign, reg11, ":player_wealth"),
                    (create_button_overlay, reg0, "@Deposit", tf_right_align),
                    (store_add, ":pos", ":right_panel_values_x", button_padding),
                    (position_set_x, pos1, ":pos"),
                    (position_set_y, pos1, ":cur_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1000),
                    (position_set_y, pos1, 1000),
                    (overlay_set_size, reg0, pos1),
                    (assign, "$g_presentation_deposit", reg0),

                    (val_add, ":cur_y", ":line_height"),

                    (str_store_party_name, s11, ":current_center"),
                    (create_text_overlay, reg0, "@{s11} treasury:", tf_left_align),
                    (position_set_x, pos1, ":left_panel_x"),
                    (position_set_y, pos1, ":cur_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1000),
                    (position_set_y, pos1, 1000),
                    (overlay_set_size, reg0, pos1),

                    (assign, reg10, ":center_wealth"),
                    (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                    (position_set_x, pos1, ":left_panel_values_x"),
                    (position_set_y, pos1, ":cur_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1000),
                    (position_set_y, pos1, 1000),
                    (overlay_set_size, reg0, pos1),
                    (assign, "$g_presentation_center_wealth", reg0),

                    (str_store_troop_name, s12, "$g_player_troop"),
                    (create_text_overlay, reg0, "@{s12} wealth:", tf_left_align),
                    (position_set_x, pos1, ":right_panel_x"),
                    (position_set_y, pos1, ":cur_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1000),
                    (position_set_y, pos1, 1000),
                    (overlay_set_size, reg0, pos1),

                    (assign, reg11, ":player_wealth"),
                    (create_text_overlay, reg0, "@{reg11}", tf_right_align),
                    (position_set_x, pos1, ":right_panel_values_x"),
                    (position_set_y, pos1, ":cur_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1000),
                    (position_set_y, pos1, 1000),
                    (overlay_set_size, reg0, pos1),
                    (assign, "$g_presentation_player_wealth", reg0),

                    (val_add, ":cur_y", ":category_height"),
                (try_end),

                (assign, "$g_withdraw_select", 0),
                (assign, "$g_deposit_select", 0),

                ## CENTER INFORMATIONS
                # Citizen's wealth
                # Population

                ## CENTER ADMINISTRATION
                # Assign governor
                # Grant fief

                (try_begin),
                    (ge, ":lord", 0),

                    (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_troop_note_mesh", ":lord"),
                    (store_sub, ":x", ":right_panel_values_x", 100),
                    (position_set_x, pos1, ":x"),
                    (position_set_y, pos1, ":cur_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 380),
                    (position_set_y, pos1, 380),
                    (overlay_set_size, reg0, pos1),
                (try_end),

                (try_begin),
                    (ge, ":lord", 0),
                    (try_begin),
                        (troop_slot_eq, ":lord", slot_troop_home, ":current_center"),
                        (str_store_troop_name, s10, ":lord"),

                        (str_store_string, s10, "@Court of {s10}"),
                        (call_script, "script_presentation_create_text_overlay", tf_left_align, ":right_panel_x", ":cur_y", 1000, 1000),
                    (else_try),
                        (eq, ":lord", "$g_player_troop"),
                        (neg|troop_slot_eq, "$g_player_troop", slot_troop_home, ":current_center"),

                        (create_game_button_overlay, reg0, "@Set as court"),
                        (store_add, ":x", ":left_panel_x", 100),
                        (position_set_x, pos1, ":x"),
                        (position_set_y, pos1, ":cur_y"),
                        (overlay_set_position, reg0, pos1),
                        (assign, "$g_presentation_center_set_court", reg0),

                        (assign, reg10, court_movement_cost),
                        (str_store_string, s10, "@Costs {reg10} denars"),
                        (call_script, "script_presentation_create_text_overlay", tf_right_align, ":left_panel_values_x", ":cur_y", 1000, 1000),
                        (overlay_set_color, reg0, text_color_light),
                    (try_end),
                (try_end),

                (try_begin),
                    (this_or_next|eq, ":lord", "$g_player_troop"),
                    (lt, ":lord", 0),

                    (try_begin),
                        (neg|troop_slot_eq, "$g_player_troop", slot_troop_home, ":current_center"),
                        (create_game_button_overlay, reg0, "@Change owner"),
                        (store_add, ":x", ":right_panel_x", 100),
                        (position_set_x, pos1, ":x"),
                        (position_set_y, pos1, ":cur_y"),
                        (overlay_set_position, reg0, pos1),
                        (val_add, ":cur_y", ":line_height"),
                        (assign, "$g_presentation_center_change_lord", reg0),
                    (try_end),
                (try_end),
                (val_add, ":cur_y", ":line_height"),

                (try_begin),
                    (ge, ":lord", 0),
                    (str_store_troop_name, s10, ":lord"),
                (else_try),
                    (str_store_string, s10, "@unassigned"),
                (try_end),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":right_panel_x", ":cur_y", 1000, 1000),
                (val_add, ":cur_y", ":line_height"),

                (str_store_string, s10, "@Current lord:"),
                (call_script, "script_presentation_create_text_overlay", tf_left_align, ":right_panel_x", ":cur_y", 1000, 1000),
                (val_add, ":cur_y", ":line_height"),

                (set_container_overlay, -1),

                (create_game_button_overlay, "$g_presentation_ok", "@Continue"),
                (position_set_x, pos1, 150),
                (position_set_y, pos1, 50),
                (overlay_set_position, "$g_presentation_ok", pos1),

                (presentation_set_duration, 999999),
            ]),

            (ti_on_presentation_event_state_change,
            [
                (store_trigger_param_1, ":object"),
                (store_trigger_param_2, ":value"),

                (assign, ":current_center", "$temp"),

                (try_begin),
                    (eq, ":object", "$g_presentation_ok"),

                    (presentation_set_duration, 0),
                (else_try),
                    (eq, ":object", "$g_presentation_deposit"),
                    (call_script, "script_party_transfer_wealth", "$g_player_party", ":current_center", "$g_deposit_select", tax_type_private_expenses, tax_type_none),
                    (overlay_set_val, "$g_presentation_player_wealth_select", 0),
                    (assign, "$g_deposit_select", 0),
                (else_try),
                    (eq, ":object", "$g_presentation_withdraw"),
                    (call_script, "script_party_transfer_wealth", ":current_center", "$g_player_party", "$g_withdraw_select", tax_type_none, tax_type_private_expenses),
                    (overlay_set_val, "$g_presentation_center_wealth_select", 0),
                    (assign, "$g_withdraw_select", 0),
                (else_try),
                    (eq, ":object", "$g_presentation_center_wealth_select"),
                    (assign, "$g_withdraw_select", ":value"),
                (else_try),
                    (eq, ":object", "$g_presentation_player_wealth_select"),
                    (assign, "$g_deposit_select", ":value"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_tax_rate_fixed_select"),
                    (party_set_slot, ":current_center", slot_party_taxes_fixed, ":value"),

                    (call_script, "script_party_get_expected_taxes", ":current_center"),
                    (assign, reg10, reg0),
                    (overlay_set_text, "$g_presentation_center_tax_rate_fixed_estimation", "@{reg10}"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_tax_rate_buy_select"),
                    (party_set_slot, ":current_center", slot_party_taxes_buy, ":value"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_tax_rate_sell_select"),
                    (party_set_slot, ":current_center", slot_party_taxes_sell, ":value"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_change_lord"),
                    (assign, "$callback", "script_assign_selected_lord"),
                    (assign, "$temp", ":current_center"),
                    (assign, "$filter_method", "script_filter_lord_vassal_grant"),

                    (start_presentation, "prsnt_select_lord"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_set_court"),
                    (troop_set_slot, "$g_player_troop", slot_troop_home, ":current_center"),

                    (store_mul, ":amount", court_movement_cost, -1),
                    (call_script, "script_party_add_accumulated_taxes", ":current_center", ":amount", tax_type_expenses),

                    (assign, reg10, court_movement_cost),
                    (display_message, "@{reg10} denars have been removed from the center treasury"),
                    (start_presentation, "prsnt_center_administration"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_garrison_manager"),
                    (try_begin),
                        (eq, ":value", 1),

                        (overlay_set_display, "$g_presentation_center_wages_percent", 0),
                        (overlay_set_display, "$g_presentation_center_garrison_wages_label", 0),
                        (overlay_set_display, "$g_presentation_center_garrison_wages", 0),
                        (overlay_set_display, "$g_presentation_center_wages_percent_label", 0),

                        (party_set_slot, ":current_center", slot_party_player_wages_limit, -1),
                    (else_try),
                        (overlay_set_display, "$g_presentation_center_wages_percent", 1),
                        (overlay_set_display, "$g_presentation_center_garrison_wages_label", 1),
                        (overlay_set_display, "$g_presentation_center_garrison_wages", 1),
                        (overlay_set_display, "$g_presentation_center_wages_percent_label", 1),

                        (party_set_slot, ":current_center", slot_party_player_wages_limit, 0),
                        (overlay_set_val, "$g_presentation_center_garrison_wages", 0),
                        (overlay_set_text, "$g_presentation_center_wages_percent", "@0%"),
                    (try_end),
                (else_try),
                    (eq, ":object", "$g_presentation_center_garrison_wages"),

                    (party_set_slot, ":current_center", slot_party_player_wages_limit, ":value"),

                    (call_script, "script_party_get_expected_taxes", ":current_center"),
                    (assign, ":expected_taxes", reg0),
                    (val_mul, ":expected_taxes", 12),

                    (store_mul, reg10, ":value", 100),
                    (val_div, reg10, ":expected_taxes"),

                    (overlay_set_text, "$g_presentation_center_wages_percent", "@{reg10}%"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_garrison_flags_noble"),

                    (party_get_slot, ":flags", ":current_center", slot_party_player_garrison_flags),
                    (val_and, ":flags", pgf_sell_noble_clean),
                    (assign, ":new_flags", 0),
                    (try_begin),
                        (eq, ":value", 0),
                    (else_try),
                        (eq, ":value", 1),
                        (assign, ":new_flags", pgf_sell_noble_vassals),
                    (else_try),
                        (eq, ":value", 2),
                        (assign, ":new_flags", pgf_sell_noble_vassals|pgf_sell_noble_faction),
                    (else_try),
                        (eq, ":value", 3),
                        (assign, ":new_flags", pgf_sell_noble_vassals|pgf_sell_noble_faction|pgf_sell_noble_unknown),
                    (try_end),
                    (val_or, ":flags", ":new_flags"),
                    (party_set_slot, ":current_center", slot_party_player_garrison_flags, ":flags"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_garrison_flags_elite"),

                    (party_get_slot, ":flags", ":current_center", slot_party_player_garrison_flags),
                    (val_and, ":flags", pgf_sell_elite_clean),
                    (assign, ":new_flags", 0),
                    (try_begin),
                        (eq, ":value", 0),
                    (else_try),
                        (eq, ":value", 1),
                        (assign, ":new_flags", pgf_sell_elite_vassals),
                    (else_try),
                        (eq, ":value", 2),
                        (assign, ":new_flags", pgf_sell_elite_vassals|pgf_sell_elite_faction),
                    (else_try),
                        (eq, ":value", 3),
                        (assign, ":new_flags", pgf_sell_elite_vassals|pgf_sell_elite_faction|pgf_sell_elite_unknown),
                    (try_end),
                    (val_or, ":flags", ":new_flags"),
                    (party_set_slot, ":current_center", slot_party_player_garrison_flags, ":flags"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_garrison_flags_veteran"),

                    (party_get_slot, ":flags", ":current_center", slot_party_player_garrison_flags),
                    (val_and, ":flags", pgf_sell_veteran_clean),
                    (assign, ":new_flags", 0),
                    (try_begin),
                        (eq, ":value", 0),
                    (else_try),
                        (eq, ":value", 1),
                        (assign, ":new_flags", pgf_sell_veteran_vassals),
                    (else_try),
                        (eq, ":value", 2),
                        (assign, ":new_flags", pgf_sell_veteran_vassals|pgf_sell_veteran_faction),
                    (else_try),
                        (eq, ":value", 3),
                        (assign, ":new_flags", pgf_sell_veteran_vassals|pgf_sell_veteran_faction|pgf_sell_veteran_unknown),
                    (try_end),
                    (val_or, ":flags", ":new_flags"),
                    (party_set_slot, ":current_center", slot_party_player_garrison_flags, ":flags"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_garrison_flags_common"),

                    (party_get_slot, ":flags", ":current_center", slot_party_player_garrison_flags),
                    (val_and, ":flags", pgf_sell_common_clean),
                    (assign, ":new_flags", 0),
                    (try_begin),
                        (eq, ":value", 0),
                    (else_try),
                        (eq, ":value", 1),
                        (assign, ":new_flags", pgf_sell_common_vassals),
                    (else_try),
                        (eq, ":value", 2),
                        (assign, ":new_flags", pgf_sell_common_vassals|pgf_sell_common_faction),
                    (else_try),
                        (eq, ":value", 3),
                        (assign, ":new_flags", pgf_sell_common_vassals|pgf_sell_common_faction|pgf_sell_common_unknown),
                    (try_end),
                    (val_or, ":flags", ":new_flags"),
                    (party_set_slot, ":current_center", slot_party_player_garrison_flags, ":flags"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_garrison_flags_levy"),

                    (party_get_slot, ":flags", ":current_center", slot_party_player_garrison_flags),
                    (val_and, ":flags", pgf_sell_levy_clean),
                    (assign, ":new_flags", 0),
                    (try_begin),
                        (eq, ":value", 0),
                    (else_try),
                        (eq, ":value", 1),
                        (assign, ":new_flags", pgf_sell_levy_vassals),
                    (else_try),
                        (eq, ":value", 2),
                        (assign, ":new_flags", pgf_sell_levy_vassals|pgf_sell_levy_faction),
                    (else_try),
                        (eq, ":value", 3),
                        (assign, ":new_flags", pgf_sell_levy_vassals|pgf_sell_levy_faction|pgf_sell_levy_unknown),
                    (try_end),
                    (val_or, ":flags", ":new_flags"),
                    (party_set_slot, ":current_center", slot_party_player_garrison_flags, ":flags"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_garrison_flags_send_noble"),

                    (party_get_slot, ":flags", ":current_center", slot_party_player_garrison_flags),
                    (try_begin),
                        (eq, ":value", 0),
                        (val_and, ":flags", pgf_send_noble_clean),
                    (else_try),
                        (val_or, ":flags", pgf_send_noble),
                    (try_end),
                    (party_set_slot, ":current_center", slot_party_player_garrison_flags, ":flags"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_garrison_flags_send_elite"),

                    (party_get_slot, ":flags", ":current_center", slot_party_player_garrison_flags),
                    (try_begin),
                        (eq, ":value", 0),
                        (val_and, ":flags", pgf_send_elite_clean),
                    (else_try),
                        (val_or, ":flags", pgf_send_elite),
                    (try_end),
                    (party_set_slot, ":current_center", slot_party_player_garrison_flags, ":flags"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_garrison_flags_send_veteran"),

                    (party_get_slot, ":flags", ":current_center", slot_party_player_garrison_flags),
                    (try_begin),
                        (eq, ":value", 0),
                        (val_and, ":flags", pgf_send_veteran_clean),
                    (else_try),
                        (val_or, ":flags", pgf_send_veteran),
                    (try_end),
                    (party_set_slot, ":current_center", slot_party_player_garrison_flags, ":flags"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_garrison_flags_send_common"),

                    (party_get_slot, ":flags", ":current_center", slot_party_player_garrison_flags),
                    (try_begin),
                        (eq, ":value", 0),
                        (val_and, ":flags", pgf_send_common_clean),
                    (else_try),
                        (val_or, ":flags", pgf_send_common),
                    (try_end),
                    (party_set_slot, ":current_center", slot_party_player_garrison_flags, ":flags"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_garrison_flags_send_levy"),

                    (party_get_slot, ":flags", ":current_center", slot_party_player_garrison_flags),
                    (try_begin),
                        (eq, ":value", 0),
                        (val_and, ":flags", pgf_send_levy_clean),
                    (else_try),
                        (val_or, ":flags", pgf_send_levy),
                    (try_end),
                    (party_set_slot, ":current_center", slot_party_player_garrison_flags, ":flags"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_prisoner_outcome_flags_ransom"),

                    (party_get_slot, ":outcome", ":current_center", slot_party_max_prisoner_outcome),
                    (try_begin),
                        (eq, ":value", 0),
                        (val_and, ":outcome", mpo_ransom_clear),
                    (else_try),
                        (val_or, ":outcome", mpo_ransom),
                    (try_end),
                    (party_set_slot, ":current_center", slot_party_max_prisoner_outcome, ":outcome"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_prisoner_outcome_flags_release"),

                    (party_get_slot, ":outcome", ":current_center", slot_party_max_prisoner_outcome),
                    (try_begin),
                        (eq, ":value", 0),
                        (val_and, ":outcome", mpo_release_clear),
                    (else_try),
                        (val_or, ":outcome", mpo_release),
                    (try_end),
                    (party_set_slot, ":current_center", slot_party_max_prisoner_outcome, ":outcome"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_prisoner_outcome_flags_enslave"),

                    (party_get_slot, ":outcome", ":current_center", slot_party_max_prisoner_outcome),
                    (try_begin),
                        (eq, ":value", 0),
                        (val_and, ":outcome", mpo_slave_clear),
                    (else_try),
                        (val_or, ":outcome", mpo_slave),
                    (try_end),
                    (party_set_slot, ":current_center", slot_party_max_prisoner_outcome, ":outcome"),
                (else_try),
                    (eq, ":object", "$g_presentation_center_prisoner_outcome_flags_recruit"),

                    (party_get_slot, ":outcome", ":current_center", slot_party_max_prisoner_outcome),
                    (try_begin),
                        (eq, ":value", 0),
                        (val_and, ":outcome", mpo_recruit_clear),
                    (else_try),
                        (val_or, ":outcome", mpo_recruit),
                    (try_end),
                    (party_set_slot, ":current_center", slot_party_max_prisoner_outcome, ":outcome"),
                (try_end),

                (try_begin),
                    (eq, "$g_presentation_readonly", 0),
                    (party_get_slot, ":center_wealth", ":current_center", slot_party_wealth),
                    (store_troop_gold, ":player_wealth", "$g_player_troop"),

                    (assign, reg10, ":center_wealth"),
                    (assign, reg11, ":player_wealth"),
                    (overlay_set_text, "$g_presentation_center_wealth", "@{reg10}"),
                    (overlay_set_text, "$g_presentation_player_wealth", "@{reg11}"),

                    (store_add, ":max", ":center_wealth", 1),
                    (overlay_set_boundaries, "$g_presentation_center_wealth_select", 0, ":max"),
                    (store_add, ":max", ":player_wealth", 1),
                    (overlay_set_boundaries, "$g_presentation_player_wealth_select", 0, ":max"),
                (try_end),
            ]),
        ]),

    # prsnt_clan_management
    ("clan_management", 0, mesh_load_window,
        [
            (ti_on_presentation_load,
                [
                    (set_fixed_point_multiplier, 1000),

                    (assign, ":picture_height", 100),
                    (assign, ":center_name_x", 50),
                    (assign, ":mesh_pic_x", 0),
                    (assign, ":current_lord_x", 230),
                    (assign, ":current_governor_x", 430),
                    (assign, ":actions_x", 700),
                    (assign, ":container_x", 50),
                    (assign, ":container_y", 100),
                    (assign, ":container_size_x", 880),
                    (assign, ":container_size_y", 550),

                    (store_add, ":header_y", ":container_y", ":container_size_y"),
                    (val_add, ":header_y", 30),

                    (store_add, ":header_x", ":center_name_x", ":container_x"),
                    (create_text_overlay, reg0, "@Center"),
                    (position_set_x, pos1, ":header_x"),
                    (position_set_y, pos1, ":header_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1200),
                    (position_set_y, pos1, 1200),
                    (overlay_set_size, reg0, pos1),

                    (store_add, ":header_x", ":current_lord_x", ":container_x"),
                    (create_text_overlay, reg0, "@Lord"),
                    (position_set_x, pos1, ":header_x"),
                    (position_set_y, pos1, ":header_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1200),
                    (position_set_y, pos1, 1200),
                    (overlay_set_size, reg0, pos1),

                    (store_add, ":header_x", ":current_governor_x", ":container_x"),
                    (create_text_overlay, reg0, "@Governor"),
                    (position_set_x, pos1, ":header_x"),
                    (position_set_y, pos1, ":header_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1200),
                    (position_set_y, pos1, 1200),
                    (overlay_set_size, reg0, pos1),

                    (store_add, ":header_x", ":actions_x", ":container_x"),
                    (create_text_overlay, reg0, "@Actions"),
                    (position_set_x, pos1, ":header_x"),
                    (position_set_y, pos1, ":header_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1200),
                    (position_set_y, pos1, 1200),
                    (overlay_set_size, reg0, pos1),

                    (str_clear, s0),
                    (create_text_overlay, reg0, s0, tf_scrollable),
                    (position_set_x, pos1, ":container_x"),
                    (position_set_y, pos1, ":container_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, ":container_size_x"),
                    (position_set_y, pos1, ":container_size_y"),
                    (overlay_set_area_size, reg0, pos1),
                    
                    (set_container_overlay, reg0),

                    (assign, ":cur_y", 10),

                    (store_add, ":line_height", ":picture_height", line_height),

                    (try_for_range_backwards, ":cur_center", centers_begin, centers_end),
                        (party_set_slot, ":cur_center", slot_party_temp, -1),
                        (call_script, "script_cf_clan_management_can_display_center", ":cur_center"),

                        (assign, ":center_y", ":cur_y"),

                        (call_script, "script_party_get_picture_mesh", ":cur_center"),
                        (assign, ":mesh", reg0),

                        (store_div, ":offset", ":picture_height", 3),
                        (store_sub, ":mesh_pic_y", ":center_y", ":offset"),

                        (create_mesh_overlay, reg0, ":mesh"),
                        (position_set_x, pos1, ":mesh_pic_x"),
                        (position_set_y, pos1, ":mesh_pic_y"),
                        (overlay_set_position, reg0, pos1),
                        (position_set_x, pos1, 200),
                        (position_set_y, pos1, 200),
                        (overlay_set_size, reg0, pos1),

                        (val_add, ":center_y", ":picture_height"),

                        (str_store_party_name, s10, ":cur_center"),
                        (create_text_overlay, reg0, "@{s10}"),
                        (position_set_x, pos1, ":center_name_x"),
                        (position_set_y, pos1, ":center_y"),
                        (overlay_set_position, reg0, pos1),
                        (position_set_x, pos1, 1000),
                        (position_set_y, pos1, 1000),
                        (overlay_set_size, reg0, pos1),
                        (overlay_set_color, reg0, text_color_light),

                        (val_add, ":center_y", line_height),

                        (assign, ":center_y", ":cur_y"),

                        (party_get_slot, ":lord", ":cur_center", slot_party_lord),
                        (try_begin),
                            (ge, ":lord", 0),
                            (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_troop_note_mesh", ":lord"),
                            (position_set_x, pos1, ":current_lord_x"),
                            (position_set_y, pos1, ":center_y"),
                            (overlay_set_position, reg0, pos1),
                            (position_set_x, pos1, 380),
                            (position_set_y, pos1, 380),
                            (overlay_set_size, reg0, pos1),
                        (try_end),

                        (val_add, ":center_y", ":picture_height"),

                        (str_store_party_name, s10, ":cur_center"),
                        (try_begin),
                            (ge, ":lord", 0),
                            (str_store_troop_name, s10, ":lord"),
                        (else_try),
                            (str_store_string, s10, "@unassigned"),
                        (try_end),
                        (create_text_overlay, reg0, "@{s10}"),
                        (position_set_x, pos1, ":current_lord_x"),
                        (position_set_y, pos1, ":center_y"),
                        (overlay_set_position, reg0, pos1),
                        (position_set_x, pos1, 1000),
                        (position_set_y, pos1, 1000),
                        (overlay_set_size, reg0, pos1),
                        (overlay_set_color, reg0, text_color_light),

                        (assign, ":center_y", ":cur_y"),

                        (party_get_slot, ":governor", ":cur_center", slot_party_governor),
                        (try_begin),
                            (ge, ":governor", 0),
                            (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_troop_note_mesh", ":governor"),
                            (position_set_x, pos1, ":current_governor_x"),
                            (position_set_y, pos1, ":center_y"),
                            (overlay_set_position, reg0, pos1),
                            (position_set_x, pos1, 380),
                            (position_set_y, pos1, 380),
                            (overlay_set_size, reg0, pos1),
                        (try_end),

                        (val_add, ":center_y", ":picture_height"),

                        (str_store_party_name, s10, ":cur_center"),
                        (try_begin),
                            (ge, ":governor", 0),
                            (str_store_troop_name, s10, ":governor"),
                        (else_try),
                            (str_store_string, s10, "@unassigned"),
                        (try_end),
                        (create_text_overlay, reg0, "@{s10}"),
                        (position_set_x, pos1, ":current_governor_x"),
                        (position_set_y, pos1, ":center_y"),
                        (overlay_set_position, reg0, pos1),
                        (position_set_x, pos1, 1000),
                        (position_set_y, pos1, 1000),
                        (overlay_set_size, reg0, pos1),
                        (overlay_set_color, reg0, text_color_light),

                        (assign, ":center_y", ":cur_y"),

                        # (create_game_button_overlay, reg0, "@Manage"),
                        # (position_set_x, pos1, ":actions_x"),
                        # (position_set_y, pos1, ":center_y"),
                        # (overlay_set_position, reg0, pos1),
                        # (position_set_x, pos1, 100),
                        # (position_set_y, pos1, 100),
                        # (overlay_set_size, reg0, pos1),

                        (val_add, ":center_y", line_height),

                        (create_game_button_overlay, reg0, "@Manage"),
                        (store_add, ":x", ":actions_x", 50),
                        (position_set_x, pos1, ":x"),
                        (position_set_y, pos1, ":center_y"),
                        (overlay_set_position, reg0, pos1),
                        # (position_set_x, pos1, 1000),
                        # (position_set_y, pos1, 1000),
                        # (overlay_set_size, reg0, pos1),

                        (party_set_slot, ":cur_center", slot_party_temp, reg0),

                        (val_add, ":cur_y", ":line_height"),
                    (try_end),

                    (set_container_overlay, -1),

                    # Actions panel
                    (create_game_button_overlay, "$g_presentation_ok", "@Continue"),
                    (position_set_x, pos1, 150),
                    (position_set_y, pos1, 50),
                    (overlay_set_position, "$g_presentation_ok", pos1),

                    (presentation_set_duration, 999999),

                ]),

            (ti_on_presentation_event_state_change,
                [
                    (store_trigger_param_1, ":object"),
                    # (store_trigger_param_2, ":value"),

                    (assign, ":manage_center", -1),
                    (try_for_range, ":cur_center", centers_begin, centers_end),
                        (party_slot_eq, ":cur_center", slot_party_temp, ":object"),
                        (assign, ":manage_center", ":cur_center"),
                    (try_end),

                    (try_begin),
                        (eq, ":object", "$g_presentation_ok"),

                        (presentation_set_duration, 0),
                    (else_try),
                        (is_between, ":manage_center", centers_begin, centers_end),
                        (assign, "$temp", ":manage_center"),
                        (start_presentation, "prsnt_center_administration"),
                    (try_end),
                ]),
        ]),

    # prsnt_select_lord
        # Requires temp set to center id
        # Requires callback set to callback script (arg1: selected lord)
        # Requires filter_method set to script for filtering troop (arg1: selected lord)
    ("select_lord", 0, mesh_load_window,
        [
            (ti_on_presentation_load,
                [
                    (set_fixed_point_multiplier, 1000),

                    (str_clear, s0),
                    (create_text_overlay, reg0, s0, tf_scrollable),
                    (position_set_x, pos1, 50),
                    (position_set_y, pos1, 150),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 880),
                    (position_set_y, pos1, 550),
                    (overlay_set_area_size, reg0, pos1),

                    (assign, "$g_presentation_selected_lord", -1),
                    
                    (set_container_overlay, reg0),

                    (assign, ":cur_y", 10),

                    (assign, ":left_panel_x", 10),
                    (assign, ":left_panel_values_x", 190),
                    (assign, ":left_panel_values2_x", 290),
                    (assign, ":right_panel_x", 445),
                    (assign, ":right_panel_values_x", 625),
                    (assign, ":right_panel_values2_x", 725),

                    (try_for_range, ":lord_no", lords_begin, lords_end),
                        (troop_set_slot, ":lord_no", slot_troop_temp_slot, -1),
                    (try_end),

                    (store_troop_faction, ":player_faction", "$g_player_troop"),

                    (call_script, "script_faction_get_notables", ":player_faction"),
                    (assign, ":num_constables", reg0),
                    (store_add, ":end", slot_troop_temp_array_begin, ":num_constables"),

                    (assign, ":i", 0),

                    (try_for_range, ":slot", slot_troop_temp_array_begin, ":end"),
                        (troop_get_slot, ":lord_no", "trp_temp_troop", ":slot"),

                        (try_begin),
                            (eq, ":i", 0),
                            (assign, ":x", ":left_panel_x"),
                            (assign, ":values_x", ":left_panel_values_x"),
                            (assign, ":values2_x", ":left_panel_values2_x"),
                        (else_try),
                            (assign, ":x", ":right_panel_x"),
                            (assign, ":values_x", ":right_panel_values_x"),
                            (assign, ":values2_x", ":right_panel_values2_x"),
                        (try_end),

                        (call_script, "script_presentation_generate_select_lord_card", ":lord_no", ":x", ":values_x", ":values2_x", ":cur_y"),

                        (try_begin),
                            (eq, ":i", 1),
                            (val_add, ":cur_y", 140),
                        (try_end),
                        (val_add, ":i", 1),
                        (val_mod, ":i", 2),
                    (try_end),

                    (try_begin),
                        (eq, ":i", 1),
                        (val_add, ":cur_y", 140),
                    (try_end),

                    (create_text_overlay, reg0, "@Notables"),
                    (position_set_x, pos1, ":left_panel_x"),
                    (position_set_y, pos1, ":cur_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1000),
                    (position_set_y, pos1, 1000),
                    (overlay_set_size, reg0, pos1),

                    (val_add, ":cur_y", line_height),

                    (assign, ":i", 0),

                    (try_for_range, ":lord_no", lords_begin, lords_end),
                        (call_script, "$filter_method", ":lord_no"),
                        (eq, reg0, 0),

                        (try_begin),
                            (eq, ":i", 0),
                            (assign, ":x", ":left_panel_x"),
                            (assign, ":values_x", ":left_panel_values_x"),
                            (assign, ":values2_x", ":left_panel_values2_x"),
                        (else_try),
                            (assign, ":x", ":right_panel_x"),
                            (assign, ":values_x", ":right_panel_values_x"),
                            (assign, ":values2_x", ":right_panel_values2_x"),
                        (try_end),

                        (call_script, "script_presentation_generate_select_lord_card", ":lord_no", ":x", ":values_x", ":values2_x", ":cur_y"),

                        (try_begin),
                            (eq, ":i", 1),
                            (val_add, ":cur_y", 140),
                        (try_end),
                        (val_add, ":i", 1),
                        (val_mod, ":i", 2),
                    (try_end),

                    (try_begin),
                        (eq, ":i", 1),
                        (val_add, ":cur_y", 140),
                    (try_end),

                    (str_store_troop_name, s10, "$g_player_troop"),
                    (create_text_overlay, reg0, "@{s10}'s vassals"),
                    (position_set_x, pos1, ":left_panel_x"),
                    (position_set_y, pos1, ":cur_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1000),
                    (position_set_y, pos1, 1000),
                    (overlay_set_size, reg0, pos1),

                    (val_add, ":cur_y", line_height),

                    (set_container_overlay, -1),

                    # Actions panel
                    (create_game_button_overlay, "$g_presentation_ok", "@Continue"),
                    (position_set_x, pos1, 150),
                    (position_set_y, pos1, 100),
                    (overlay_set_position, "$g_presentation_ok", pos1),

                    (create_game_button_overlay, "$g_presentation_cancel", "@Cancel"),
                    (position_set_x, pos1, 150),
                    (position_set_y, pos1, 50),
                    (overlay_set_position, "$g_presentation_cancel", pos1),

                    (presentation_set_duration, 999999),
                ]),

            (ti_on_presentation_event_state_change,
                [
                    (store_trigger_param_1, ":object"),
                    (store_trigger_param_2, ":value"),

                    (try_begin),
                        (eq, ":object", "$g_presentation_ok"),

                        (try_begin),
                            (ge, "$g_presentation_selected_lord", 0),
                            (call_script, "$callback", "$g_presentation_selected_lord"),
                        (try_end),

                        (presentation_set_duration, 0),
                    (else_try),
                        (eq, ":object", "$g_presentation_cancel"),

                        (presentation_set_duration, 0),
                    (else_try),
                        (assign, ":selected_lord", -1),
                        (try_for_range, ":lord_no", lords_begin, lords_end),
                            (troop_slot_eq, ":lord_no", slot_troop_temp_slot, ":object"),
                            (assign, ":selected_lord", ":lord_no"),
                            (try_begin),
                                (eq, ":value", 1),
                                (assign, "$g_presentation_selected_lord", ":selected_lord"),
                            (else_try),
                                (assign, "$g_presentation_selected_lord", -1),
                            (try_end),
                        (try_end),
                        (ge, ":selected_lord", 0),
                        
                        (try_for_range, ":lord_no", lords_begin, lords_end),
                            (troop_get_slot, ":overlay_id", ":lord_no", slot_troop_temp_slot),
                            (neq, ":overlay_id", ":object"),
                            (ge, ":overlay_id", 0),
                            (overlay_set_val, ":overlay_id", 0),
                        (try_end),
                    (try_end),
                ]),
        ]),

    ("center_constructions", 0, mesh_load_window,
        [
            (ti_on_presentation_load,
                [
                    (set_fixed_point_multiplier, 1000),

                    (assign, ":current_center", "$temp"),
                    (party_get_slot, ":current_center_type", ":current_center", slot_party_type),

                    (assign, ":num_currently_building", 0),

                    (assign, ":num_buildings", 0),
                    (try_for_range_backwards, ":building", center_buildings_begin, center_buildings_end),
                        (item_get_slot, ":enabled", ":building", slot_building_enabled),
                        (store_sub, ":offset", ":building", center_buildings_begin),
                        (store_add, ":building_slot", ":offset", slot_party_building_slot_begin),
                        (party_get_slot, ":building_state", ":current_center", ":building_slot"),

                        (try_begin),
                            (lt, ":building_state", 0),
                            (val_add, ":num_currently_building", 1),
                        (try_end),

                        (eq, ":enabled", 1),

                        (item_get_slot, ":building_types", ":building", slot_building_center_types),
                        (store_mod, ":allowed", ":building_types", ":current_center_type"),
                        (eq, ":allowed", 0),
                        (val_add, ":num_buildings", 1),
                    (try_end),

                    (assign, ":columns", 3),

                    (val_mod, ":num_buildings", ":columns"),
                    (store_sub, ":mod", ":num_buildings", 1),
                    (try_begin),
                        (eq, ":mod", -1),
                        (store_sub, ":mod", ":columns", 1),
                    (try_end),

                    (call_script, "script_party_get_building_slots", ":current_center"),
                    (assign, ":num_slots", reg0),

                    (assign, ":container_x", 50),
                    (assign, ":container_y", 100),
                    (assign, ":container_size_x", 605),
                    (assign, ":container_size_y", 550),

                    (assign, ":header_x", 50),
                    (assign, ":header_y", 680),
                    (str_store_party_name, s10, ":current_center"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":header_x", ":header_y", 1200, 1200),

                    (store_add, ":queue_x", ":container_x", ":container_size_x"),
                    (assign, reg10, ":num_currently_building"),
                    (assign, reg11, ":num_slots"),
                    (str_store_string, s10, "@Construction slots: {reg10}/{reg11}"),
                    (call_script, "script_presentation_create_text_overlay", tf_right_align, ":queue_x", ":header_y", 850, 850),

                    (str_clear, s0),
                    (create_text_overlay, reg0, s0, tf_scrollable),
                    (position_set_x, pos1, ":container_x"),
                    (position_set_y, pos1, ":container_y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, ":container_size_x"),
                    (position_set_y, pos1, ":container_size_y"),
                    (overlay_set_area_size, reg0, pos1),
                    
                    (assign, ":container", reg0),

                    (str_clear, s0),
                    (create_text_overlay, reg0, s0, tf_scrollable),
                    (store_add, ":x", ":container_x", ":container_size_x"),
                    (position_set_x, pos1, ":x"),
                    (position_set_y, pos1, ":container_y"),
                    (overlay_set_position, reg0, pos1),
                    (store_sub, ":size_x", 980, ":x"),
                    (position_set_x, pos1, ":size_x"),
                    (position_set_y, pos1, ":container_size_y"),
                    (overlay_set_area_size, reg0, pos1),
                    (assign, ":side_panel", reg0),

                    (set_container_overlay, ":container"),

                    (assign, ":padding_x", 10),
                    (assign, ":y", 10),

                    (assign, ":column_size", ":container_size_x"),

                    (val_div, ":column_size", ":columns"),
                    (assign, ":card_size", 100),

                    (try_for_range_backwards, ":building", center_buildings_begin, center_buildings_end),
                        (item_get_slot, ":enabled", ":building", slot_building_enabled),
                        (item_set_slot, ":building", slot_building_presentation_card, -1),
                        (item_set_slot, ":building", slot_building_presentation_button, -1),
                        (eq, ":enabled", 1),

                        (item_get_slot, ":building_types", ":building", slot_building_center_types),
                        (store_mod, ":allowed", ":building_types", ":current_center_type"),
                        (eq, ":allowed", 0),

                        (store_mul, ":row_x", ":mod", ":column_size"),
                        (store_add, ":cur_x", ":padding_x", ":row_x"),

                        (store_add, ":cur_y", ":y", 5),

                        (store_sub, ":offset", ":building", center_buildings_begin),
                        (store_add, ":building_slot", ":offset", slot_party_building_slot_begin),
                        (party_get_slot, ":building_state", ":current_center", ":building_slot"),

                        (create_mesh_overlay, reg0, "mesh_mp_ui_command_panel"),
                        (position_set_x, pos1, ":cur_x"),
                        (position_set_y, pos1, ":cur_y"),
                        (overlay_set_position, reg0, pos1),
                        (position_set_x, pos1, 2000),
                        (position_set_y, pos1, 1000),
                        (overlay_set_size, reg0, pos1),
                        (overlay_set_alpha, reg0, 0x7F),

                        (item_set_slot, ":building", slot_building_presentation_card, reg0),

                        (val_add, ":cur_y", 10),

                        (try_begin),
                            # efficiency
                            (gt, ":building_state", 0),
                            (call_script, "script_party_get_building_efficiency", ":current_center", ":building"),
                            (str_store_string, s10, "@{reg0}% efficiency"),

                            (call_script, "script_presentation_create_text_overlay", tf_left_align, ":cur_x", ":cur_y", 850, 850),
                            (overlay_set_color, reg0, text_color_light),
                        (else_try),
                            (lt, ":building_state", 0),

                            (call_script, "script_party_get_building_creation_time", ":current_center", ":building"),
                            (assign, ":build_time", reg0),

                            (store_mul, ":time_left", ":building_state", -100),
                            (val_div, ":time_left", ":build_time"),
                            (val_min, ":time_left", 100),
                            (val_max, ":time_left", 0),
                            (store_sub, ":progress", 100, ":time_left"),
                            (assign, reg10, ":progress"),
                            (str_store_string, s10, "@Building in progress: {reg10}%"),

                            (call_script, "script_presentation_create_text_overlay", tf_left_align, ":cur_x", ":cur_y", 850, 850),
                            (overlay_set_color, reg0, text_color_light),
                        (else_try),
                            (ge, ":num_currently_building", ":num_slots"),
                            (str_store_string, s10, "@Too many constructions"),

                            (call_script, "script_presentation_create_text_overlay", tf_left_align, ":cur_x", ":cur_y", 850, 850),
                            (overlay_set_color, reg0, text_color_light),
                        (else_try),
                            (create_game_button_overlay, reg0, "@Build"),
                            (store_add, ":x", ":cur_x", button_padding),
                            (val_add, ":x", button_size),
                            (position_set_x, pos1, ":x"),
                            (position_set_y, pos1, ":cur_y"),
                            (overlay_set_position, reg0, pos1),
                            (item_set_slot, ":building", slot_building_presentation_button, reg0),
                        (try_end),

                        (val_add, ":cur_y", 50),

                        (str_store_item_name, s10, ":building"),
                        (call_script, "script_presentation_create_text_overlay", tf_left_align, ":cur_x", ":cur_y", 900, 900),
                        # (overlay_set_color, reg0, text_color_white),

                        (val_add, ":cur_y", 25),

                        (try_begin),
                            (le, ":mod", 0),
                            (val_add, ":y", ":card_size"),
                            (assign, ":mod", ":columns"),
                        (try_end),

                        (val_sub, ":mod", 1),
                    (try_end),

                    (set_container_overlay, ":side_panel"),

                    (assign, ":cur_y", 0),
                    (assign, ":cur_x", 25),

                    (str_store_string, s10, "@ _^ ^ ^ ^ ^"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":cur_x", ":cur_y", 800, 800),
                    (assign, "$g_presentation_building_description", reg0),

                    (val_add, ":cur_y", 100),

                    (str_store_string, s10, "@ _"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":cur_x", ":cur_y", 800, 800),
                    (assign, "$g_presentation_building_requirements", reg0),

                    (val_add, ":cur_y", line_small_height),

                    (str_store_string, s10, "@ _"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":cur_x", ":cur_y", 800, 800),
                    (assign, "$g_presentation_building_create_time", reg0),

                    (val_add, ":cur_y", line_small_height),

                    (str_store_string, s10, "@ _"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":cur_x", ":cur_y", 800, 800),
                    (assign, "$g_presentation_building_create_maintenance", reg0),

                    (val_add, ":cur_y", line_small_height),

                    (str_store_string, s10, "@ _"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":cur_x", ":cur_y", 800, 800),
                    (assign, "$g_presentation_building_create_cost", reg0),

                    (val_add, ":cur_y", line_height),

                    (str_store_string, s10, "@ _"),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, ":cur_x", ":cur_y", 1000, 1000),
                    (assign, "$g_presentation_building_name", reg0),

                    (set_container_overlay, -1),

                    # Actions panel
                    (create_game_button_overlay, "$g_presentation_ok", "@Continue"),
                    (position_set_x, pos1, 150),
                    (position_set_y, pos1, 50),
                    (overlay_set_position, "$g_presentation_ok", pos1),

                    (presentation_set_duration, 999999),
                ]),

            (ti_on_presentation_event_state_change,
                [
                    (store_trigger_param_1, ":object"),
                    # (store_trigger_param_2, ":value"),

                    (assign, ":current_center", "$temp"),

                    (assign, ":building_button", -1),
                    (try_for_range, ":building", center_buildings_begin, center_buildings_end),
                        (item_get_slot, ":button", ":building", slot_building_presentation_button),
                        (eq, ":button", ":object"),
                        (assign, ":building_button", ":building"),
                    (try_end),

                    (try_begin),
                        (is_between, ":building_button", center_buildings_begin, center_buildings_end),

                        (call_script, "script_party_create_building", ":current_center", ":building_button"),

                        (start_presentation, "prsnt_center_constructions"),
                    (else_try),
                        (eq, ":object", "$g_presentation_ok"),

                        (presentation_set_duration, 0),
                    (try_end),
                ]),

            
            (ti_on_presentation_mouse_enter_leave,
            [
                (store_trigger_param_1, ":object"),
                (store_trigger_param_2, ":value"),
                
                (set_fixed_point_multiplier, 1000),

                (try_begin),
                    (eq, ":value", 0),

                    (assign, ":current_center", "$temp"),

                    (assign, ":building_card", -1),
                    (try_for_range, ":building", center_buildings_begin, center_buildings_end),
                        (item_get_slot, ":card", ":building", slot_building_presentation_card),
                        (eq, ":card", ":object"),
                        (assign, ":building_card", ":building"),
                    (try_end),
                        
                    (try_begin),
                        (is_between, ":building_card", center_buildings_begin, center_buildings_end),
                        (str_store_item_name, s10, ":building_card"),

                        (store_sub, ":offset", ":building_card", center_buildings_begin),
                        (store_add, ":building_description", ":offset", center_buildings_description_begin),

                        (call_script, "script_party_get_building_creation_time", ":current_center", ":building_card"),
                        (assign, ":creation_time", reg0),
                        (call_script, "script_party_get_building_creation_cost", ":current_center", ":building_card"),
                        (assign, ":cost", reg0),
                        (item_get_slot, ":requirements", ":building_card", slot_building_required_building),
                        (item_get_slot, ":maintenance", ":building_card", slot_building_cost_maintenance),

                        (overlay_set_text, "$g_presentation_building_description", ":building_description"),

                        (assign, reg10, ":creation_time"),
                        (str_store_string, s10, "@{reg10} days"),
                        (overlay_set_text, "$g_presentation_building_create_time", s10),

                        (try_begin),
                            (is_between, ":requirements", center_buildings_begin, center_buildings_end),
                            (str_store_item_name, s10, ":requirements"),
                            (overlay_set_text, "$g_presentation_building_requirements", "@Requires {s10}"),
                        (else_try),
                            (overlay_set_text, "$g_presentation_building_requirements", "@ _"),
                        (try_end),

                        (call_script, "script_game_get_money_text", ":cost"),
                        (overlay_set_text, "$g_presentation_building_create_cost", s0),

                        (call_script, "script_game_get_money_text", ":maintenance"),
                        (str_store_string, s10, "@{s0} per month"),
                        (overlay_set_text, "$g_presentation_building_create_maintenance", s10),

                        (str_store_item_name, s10, ":building_card"),
                        (overlay_set_text, "$g_presentation_building_name", s10),
                    (try_end),
                (try_end),
            ]),
        ]),

    ("banner_selection", 0, mesh_load_window,
        [
            (ti_on_presentation_load,
                [
                    (set_fixed_point_multiplier, 1000),

                    (str_clear, s0),
                    (create_text_overlay, reg0, s0, tf_scrollable),
                    (position_set_x, pos1, 50),
                    (position_set_y, pos1, 100),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 620),
                    (position_set_y, pos1, 550),
                    (overlay_set_area_size, reg0, pos1),

                    (set_container_overlay, reg0),

                    (assign, ":x_pos", 10),
                    (assign, ":y_pos", 230),
                    (assign, ":num_rows", 5),

                    (assign, "$g_presentation_selected_banner_begin", -1),

                    (store_sub, ":num_banners", banner_meshes_end, banner_meshes_begin),
                    (val_mod, ":num_banners", ":num_rows"),
                    (store_sub, ":i", ":num_rows", ":num_banners"),
                    (val_mod, ":i", ":num_rows"),

                    (try_for_range, ":banner", banner_meshes_begin, banner_meshes_end),
                        (create_image_button_overlay, reg1, ":banner", ":banner"),

                        (store_sub, ":pos", ":num_rows", ":i"),
                        (val_sub, ":pos", 1),

                        (store_mul, ":x_pos", ":pos", 125),
                        (val_add, ":x_pos", 60),
                        (position_set_x, pos1, ":x_pos"),
                        (position_set_y, pos1, ":y_pos"),
                        (overlay_set_position, reg1, pos1),
                        (position_set_x, pos1, 100),
                        (position_set_y, pos1, 100),
                        (overlay_set_size, reg1, pos1),

                        (try_begin),
                            (eq, "$g_presentation_selected_banner_begin", -1),
                            (assign, "$g_presentation_selected_banner_begin", reg1),
                        (try_end),

                        (val_add, ":i", 1),
                        (try_begin),
                            (ge, ":i", ":num_rows"),
                            (val_mod, ":i", ":num_rows"),
                            (val_add, ":y_pos", 230),
                        (try_end),
                    (try_end),

                    (set_container_overlay, -1),

                    (troop_get_slot, ":selected_banner", "$g_player_troop", slot_troop_banner_scene_prop),

                    (try_begin),
                        (is_between, ":selected_banner", banner_scene_props_begin, banner_scene_props_end),

                        (store_sub, ":offset", ":selected_banner", banner_scene_props_begin),
                        (store_add, ":selected_arms_mesh", ":offset", arms_meshes_begin),
                        (assign, "$g_override_troop_banner_mesh", ":selected_arms_mesh"),

                        (store_add, ":selected_banner_mesh", ":offset", banner_meshes_begin),
                        (create_mesh_overlay, reg0, ":selected_banner_mesh"),
                        (position_set_x, pos1, 770),
                        (position_set_y, pos1, 650),
                        (overlay_set_position, reg0, pos1),
                        (position_set_x, pos1, 100),
                        (position_set_y, pos1, 100),
                        (overlay_set_size, reg0, pos1),
                    (else_try),
                        (assign, "$g_override_troop_banner_mesh", -1),
                    (try_end),

                    (try_begin),
                        (eq, "$g_presentation_preview_selected_culture", -1),
                        (troop_get_slot, ":culture", "$g_player_troop", slot_troop_culture),
                    (else_try),
                        (assign, ":culture", "$g_presentation_preview_selected_culture"),
                    (try_end),
                    (try_begin),
                        (eq, ":culture", "fac_culture_1"),
                        (assign, ":troop_1", "trp_swadian_light_infantry"),
                        (assign, ":troop_2", "trp_swadian_man_at_arms"),
                        (assign, ":troop_3", "trp_swadian_noble"),
                    (else_try),
                        (eq, ":culture", "fac_culture_2"),
                        (assign, ":troop_1", "trp_vaegir_light_bowman"),
                        (assign, ":troop_2", "trp_vaegir_heavy_infantry"),
                        (assign, ":troop_3", "trp_vaegir_royal_hussar"),
                    (else_try),
                        (eq, ":culture", "fac_culture_3"),
                        (assign, ":troop_1", "trp_khergit_skirmisher"),
                        (assign, ":troop_2", "trp_khergit_heavy_spearman"),
                        (assign, ":troop_3", "trp_khergit_noble"),
                    (else_try),
                        (eq, ":culture", "fac_culture_4"),
                        (assign, ":troop_1", "trp_nord_light_infantry"),
                        (assign, ":troop_2", "trp_nord_medium_infantry"),
                        (assign, ":troop_3", "trp_nord_noble_infantry"),
                    (else_try),
                        (eq, ":culture", "fac_culture_5"),
                        (assign, ":troop_1", "trp_rhodok_light_crossbowman"),
                        (assign, ":troop_2", "trp_rhodok_spearman"),
                        (assign, ":troop_3", "trp_rhodok_noble"),
                    (else_try),
                        (eq, ":culture", "fac_culture_6"),
                        (assign, ":troop_1", "trp_sarranid_light_skirmisher"),
                        (assign, ":troop_2", "trp_sarranid_guard"),
                        (assign, ":troop_3", "trp_sarranid_noble_horse_archer"),
                    (else_try),
                        (assign, ":troop_1", "trp_mercenary_light_infantry"),
                        (assign, ":troop_2", "trp_mercenary_infantry"),
                        (assign, ":troop_3", "trp_mercenary_knight"),
                    (try_end),

                    (assign, ":y", 80),

                    (store_mul, ":troop_no", ":troop_1", 2),
                    (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_game_party_window", ":troop_no"),
                    (position_set_x, pos1, 560),
                    (position_set_y, pos1, ":y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1200),
                    (position_set_y, pos1, 1200),
                    (overlay_set_size, reg0, pos1),

                    (store_mul, ":troop_no", ":troop_2", 2),
                    (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_game_party_window", ":troop_no"),
                    (position_set_x, pos1, 650),
                    (position_set_y, pos1, ":y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1200),
                    (position_set_y, pos1, 1200),
                    (overlay_set_size, reg0, pos1),

                    (store_mul, ":troop_no", ":troop_3", 2),
                    (create_mesh_overlay_with_tableau_material, reg0, -1, "tableau_game_party_window", ":troop_no"),
                    (position_set_x, pos1, 740),
                    (position_set_y, pos1, ":y"),
                    (overlay_set_position, reg0, pos1),
                    (position_set_x, pos1, 1200),
                    (position_set_y, pos1, 1200),
                    (overlay_set_size, reg0, pos1),

                    (str_store_string, s10, "@You have been granted a banner to represent your lineage."),
                    (call_script, "script_presentation_create_text_overlay", tf_left_align, 50, 700, 1000, 1000),

                    # Actions panel
                    (try_begin),
                        (create_game_button_overlay, "$g_presentation_switch_preview", "@Change preview"),
                        (position_set_x, pos1, 820),
                        (position_set_y, pos1, 50),
                        (overlay_set_position, "$g_presentation_switch_preview", pos1),
                    (try_end),

                    (create_game_button_overlay, "$g_presentation_ok", "@Accept banner"),
                    (position_set_x, pos1, 150),
                    (position_set_y, pos1, 50),
                    (overlay_set_position, "$g_presentation_ok", pos1),
                    (try_begin),
                        (eq, ":selected_banner", -1),
                        (overlay_set_display, "$g_presentation_ok", 0),
                    (try_end),

                    (presentation_set_duration, 999999),
                ]),

            (ti_on_presentation_event_state_change,
                [
                    (store_trigger_param_1, ":object"),

                    (try_begin),
                        (eq, ":object", "$g_presentation_ok"),
                        (assign, "$g_override_troop_banner_mesh", -1),
                        (presentation_set_duration, 0),
                    (else_try),
                        (eq, ":object", "$g_presentation_switch_preview"),
                        (val_add, "$g_presentation_preview_selected_culture", 1),
                        (try_begin),
                            (neg|is_between, "$g_presentation_preview_selected_culture", cultures_begin, cultures_end),
                            (assign, "$g_presentation_preview_selected_culture", cultures_begin),
                        (try_end),
                        (start_presentation, "prsnt_banner_selection"),
                    (else_try),
                        (store_sub, ":offset", ":object", "$g_presentation_selected_banner_begin"),
                        (store_add, ":selected_banner", ":offset", banner_scene_props_begin),

                        (troop_set_slot, "$g_player_troop", slot_troop_banner_scene_prop, ":selected_banner"),
                        (start_presentation, "prsnt_banner_selection"),
                        # (overlay_set_display, "$g_presentation_ok", 1),
                    (try_end),
                ]),
        ]),

    ("setting_shield_painting", 0, mesh_load_window,
        [
            (ti_on_presentation_load,
                [
                    (set_fixed_point_multiplier, 1000),
                    (presentation_set_duration, 999999),
                ]),

            (ti_on_presentation_run,
                [
                    (presentation_set_duration, 0),
                ]),
        ]),

    ("setting_weather", 0, mesh_load_window, [
        (ti_on_presentation_load,
            [
                (set_fixed_point_multiplier, 1000),
                (presentation_set_duration, 999999),
            ]),

        (ti_on_presentation_run,
            [
    	       (presentation_set_duration, 0),
            ]),
        ]),

    ("setting_morale", 0, mesh_load_window, [
        (ti_on_presentation_load,
            [
                (set_fixed_point_multiplier, 1000),
                (presentation_set_duration, 999999),
            ]),

        (ti_on_presentation_run,
            [
                (presentation_set_duration, 0),
            ]),
        ]),

    ("setting_death", 0, mesh_load_window, [
        (ti_on_presentation_load,
            [
                (set_fixed_point_multiplier, 1000),
                (presentation_set_duration, 999999),
            ]),

        (ti_on_presentation_run,
            [
                (presentation_set_duration, 0),
            ]),
        ]),

    ("setting_losing", 0, mesh_load_window, [
        (ti_on_presentation_load,
            [
                (set_fixed_point_multiplier, 1000),
                (presentation_set_duration, 999999),
            ]),

        (ti_on_presentation_run,
            [
                (presentation_set_duration, 0),
            ]),
        ]),

    ("setting_difficulty", 0, mesh_load_window, [
        (ti_on_presentation_load,
            [
                (set_fixed_point_multiplier, 1000),
                (presentation_set_duration, 999999),
            ]),

        (ti_on_presentation_run,
            [
                (presentation_set_duration, 0),
            ]),
        ]),

    ("setting_misc", 0, mesh_load_window,
        [
            (ti_on_presentation_load,
            [
                (set_fixed_point_multiplier, 1000),
                (presentation_set_duration, 999999),
            ]),

            (ti_on_presentation_run,
            [
        	    (presentation_set_duration, 0),
            ]),
        ]),
]
