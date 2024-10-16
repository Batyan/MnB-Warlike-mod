from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
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

button_padding = 12

line_height = 30
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
        		(str_store_string, s0, "@Total cost: 0 denars"),
        		(create_text_overlay, "$g_hire_soldiers_total_cost", s0, tf_left_align),
        		(position_set_x, pos1, 200),
        		(position_set_y, pos1, 140),
        		(overlay_set_position, "$g_hire_soldiers_total_cost", pos1),
        		(position_set_x, pos1, 1000),
        		(position_set_y, pos1, 1000),
        		(overlay_set_size, "$g_hire_soldiers_total_cost", pos1),
        		# Current money
        		(store_troop_gold, reg0, "$g_player_troop"),
        		(str_store_string, s0, "@Current money: {reg0} denars"),
        		(create_text_overlay, reg0, s0, tf_left_align),
        		(position_set_x, pos1, 200),
        		(position_set_y, pos1, 110),
        		(overlay_set_position, reg0, pos1),
        		(position_set_x, pos1, 1000),
        		(position_set_y, pos1, 1000),
        		(overlay_set_size, reg0, pos1),
        		
        		# Party size
        		(party_get_num_companions, reg11, "$g_player_party"),
        		(str_store_string, s0, "@Party size: {reg11}"),
        		(create_text_overlay, "$g_hire_soldiers_free_capacity", s0, tf_left_align),
        		(position_set_x, pos1, 200),
        		(position_set_y, pos1, 80),
        		(overlay_set_position, "$g_hire_soldiers_free_capacity", pos1),
        		(position_set_x, pos1, 1000),
        		(position_set_y, pos1, 1000),
        		(overlay_set_size, "$g_hire_soldiers_free_capacity", pos1),
                
                # Min Center Party size
                (call_script, "script_party_get_prefered_wages_limit", ":current_city"),
                (assign, reg10, reg1),
                (call_script, "script_party_get_wages", ":current_city"),
                (assign, reg11, reg0),
                (str_store_string, s0, "@Center recruitment limit: {reg11}/{reg10}"),
                (create_text_overlay, "$g_hire_soldiers_min_capacity", s0, tf_left_align),
                (position_set_x, pos1, 200),
                (position_set_y, pos1, 50),
                (overlay_set_position, "$g_hire_soldiers_min_capacity", pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, "$g_hire_soldiers_min_capacity", pos1),
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
        		(create_button_overlay, "$g_presentation_ok", "@Buy"),
        		(position_set_x, pos1, 50),
        		(position_set_y, pos1, 80),
        		(overlay_set_position, "$g_presentation_ok", pos1),
        		
        		# Cancel button
        		(create_button_overlay, "$g_presentation_cancel", "@Cancel"),
        		(position_set_x, pos1, 50),
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
        				(party_get_slot, ":center_wealth", ":current_city", slot_party_wealth),
        				(val_add, ":center_wealth", ":total_cost"),
        				(party_set_slot, ":current_city", slot_party_wealth, ":center_wealth"),
        				
        				(troop_remove_gold, "$g_player_troop", ":total_cost"),
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
        		(str_store_string, s0, "@Select a culture you wish to start as"),
        		(create_text_overlay, reg0, s0, tf_left_align),
        		(position_set_x, pos1, 50),
        		(position_set_y, pos1, 550),
        		(overlay_set_position, reg0, pos1),
        		(position_set_x, pos1, 1000),
        		(position_set_y, pos1, 1000),
        		(overlay_set_size, reg0, pos1),
        		
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
        		(create_button_overlay, "$g_presentation_ok", "@Accept"),
        		(position_set_x, pos1, 50),
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

                    (call_script, "script_player_add_starting_items"),
        			
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
                (create_text_overlay, reg0, "@Current state", tf_left_align),
                (position_set_x, pos1, 50),
                (position_set_y, pos1, 680),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (assign, ":current_state_x", 0),
                (assign, ":current_state_values_x", 255),

                # Current effects panel
                (create_text_overlay, reg0, "@Current effects", tf_left_align),
                (position_set_x, pos1, 355),
                (position_set_y, pos1, 680),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (assign, ":current_effects_x", 305),
                (assign, ":current_effects_values_x", 565),

                # Future state panel
                (create_text_overlay, reg0, "@Future state", tf_left_align),
                (position_set_x, pos1, 665),
                (position_set_y, pos1, 680),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
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
                    (party_get_slot, ":last_wealth", ":center", slot_party_budget_last_wealth),
                    (party_get_slot, ":current_wealth", ":center", slot_party_wealth),
                    
                    (party_get_slot, ":leader", ":center", slot_party_leader),
                    (eq, ":leader", "$g_player_troop"),
                    # (is_between, ":center", towns_begin, towns_end),

                    # (call_script, "script_party_get_wages", ":center"),
                    # (store_mul, ":center_wages", reg0, -1),

                    (assign, ":total_budget", 0),
                    (try_for_range, ":tax_slot", slot_party_buget_taxes_begin, slot_party_buget_taxes_end),
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
                    (try_end),

                    # We need to go back one row
                    (val_sub, ":cur_y", ":line_height"),

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
                    (try_end),

                    (val_add, ":cur_y", ":line_height"),

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

                (store_troop_gold, ":player_gold", "$g_player_troop"),

                (call_script, "script_party_get_wages", "$g_player_party"),
                (store_mul, ":player_party_wages", reg0, -1),

                (store_add, ":player_party_remaining", ":player_gold", 0),

                (party_get_slot, ":player_party_debt", "$g_player_party", slot_party_unpaid_wages),
                (store_sub, ":remaining_debt", ":player_party_debt", ":player_party_wages"),

                (assign, "$g_presentation_wages_amount_unpaid", ":remaining_debt"),

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

                (create_text_overlay, reg0, "@Current debt:", tf_left_align),
                (position_set_x, pos1, ":current_state_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (store_mul, reg10, ":player_party_debt", -1),
                (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                (position_set_x, pos1, ":current_state_values_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (try_begin),
                    (eq, ":player_party_debt", 0),
                    (overlay_set_color, reg0, text_color_budget_neutral),
                (else_try),
                    (overlay_set_color, reg0, text_color_budget_negative),
                (try_end),

                (val_add, ":cur_y", ":line_height"),
                
                (create_text_overlay, reg0, "@Remaining gold:", tf_left_align),
                (position_set_x, pos1, ":future_state_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (assign, reg10, ":player_party_remaining"),
                (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                (position_set_x, pos1, ":future_state_values_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (overlay_set_color, reg0, text_color_budget_neutral),
                (assign, "$g_presentation_wages_remaining_gold", reg0),

                (val_add, ":cur_y", ":line_height"),

                (create_text_overlay, reg0, "@Wealth:", tf_left_align),
                (position_set_x, pos1, ":current_state_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (assign, reg10, ":player_gold"),
                (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                (position_set_x, pos1, ":current_state_values_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (create_text_overlay, reg0, "@Wages:", tf_left_align),
                (position_set_x, pos1, ":current_effects_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (assign, reg10, ":player_party_wages"),
                (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                (position_set_x, pos1, ":current_effects_values_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (overlay_set_color, reg0, text_color_budget_negative),

                (create_text_overlay, reg0, "@Amount to pay:", tf_left_align),
                (position_set_x, pos1, ":future_state_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (overlay_set_color, reg0, text_color_budget_neutral),

                (assign, "$g_presentation_wages_amount_paying", 0),

                (try_begin),
                    (eq, "$g_process_effects", 1),
                    (store_add, ":max_wage_payment", ":player_gold", 1),
                    (store_add, ":max_debt_payment", ":remaining_debt", 1),
                    (val_min, ":max_wage_payment", ":max_debt_payment"),
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

                (create_text_overlay, reg0, "@Main party", tf_left_align),
                (position_set_x, pos1, ":current_state_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1100),
                (position_set_y, pos1, 1100),
                (overlay_set_size, reg0, pos1),

                (set_container_overlay, -1),

                # Actions panel
                (create_button_overlay, "$g_presentation_ok", "@Continue"),
                (position_set_x, pos1, 50),
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
                        (party_set_slot, "$g_player_party", slot_party_unpaid_wages, "$g_presentation_wages_amount_unpaid"),

                        (call_script, "script_clean_budgets"),
                        (assign, "$g_process_effects", 0),
                    (try_end),
                    (presentation_set_duration, 0),
                (else_try),
                    (eq, ":object", "$g_presentation_wages_pay_slider"),

                    (assign, "$g_presentation_wages_amount_paying", ":value"),

                    (store_troop_gold, ":player_gold", "$g_player_troop"),
                    (store_sub, ":player_party_remaining", ":player_gold", ":value"),
                    (assign, reg10, ":player_party_remaining"),
                    (overlay_set_text, "$g_presentation_wages_remaining_gold", "@{reg10}"),

                    (call_script, "script_party_get_wages", "$g_player_party"),
                    (assign, ":player_party_wages", reg0),
                    (store_sub, ":remaining_wages", ":player_party_wages", ":value"),
                    (party_get_slot, ":unpaid_wages", "$g_player_party", slot_party_unpaid_wages),
                    (val_add, ":unpaid_wages", ":remaining_wages"),
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

                (str_store_party_name, s11, ":current_center"),
                (create_text_overlay, reg0, s11, tf_left_align),
                (position_set_x, pos1, 50),
                (position_set_y, pos1, 680),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),

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
                
                ## CENTER POLICIES
                # Center taxes

                (create_text_overlay, reg0, "@Buying tax rate", tf_left_align),
                (position_set_x, pos1, ":left_panel_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),

                (party_get_slot, ":buy_rate", ":current_center", slot_party_taxes_buy),
                (assign, ":max", 100),
                (create_number_box_overlay, reg0, 0, ":max"),
                (store_sub, ":pos", ":left_panel_values_x", numberbox_size),
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
                (assign, ":max", 100),
                (create_number_box_overlay, reg0, 0, ":max"),
                (store_sub, ":pos", ":right_panel_values_x", numberbox_size),
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
                (assign, ":max", 100),
                (create_number_box_overlay, reg0, 0, ":max"),
                (store_sub, ":pos", ":left_panel_values_x", numberbox_size),
                (position_set_x, pos1, ":pos"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (overlay_set_val, reg0, ":tax_rate"),
                (assign, "$g_presentation_center_tax_rate_fixed_select", reg0),

                (create_text_overlay, reg0, "@Estimated monthly taxes: ", tf_left_align),
                (position_set_x, pos1, ":right_panel_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),

                (call_script, "script_party_get_expected_taxes", ":current_center"),
                (assign, reg10, reg0),

                (assign, ":max", 100),
                (create_text_overlay, reg0, "@{reg10}", tf_right_align),
                (position_set_x, pos1, ":right_panel_values_x"),
                (position_set_y, pos1, ":cur_y"),
                (overlay_set_position, reg0, pos1),
                (position_set_x, pos1, 1000),
                (position_set_y, pos1, 1000),
                (overlay_set_size, reg0, pos1),
                (assign, "$g_presentation_center_tax_rate_fixed_estimation", reg0),

                (val_add, ":cur_y", ":category_height"),

                ## CENTER WEALTH
                # Center treasury
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

                (assign, "$g_withdraw_select", 0),
                (assign, "$g_deposit_select", 0),

                ## CENTER GARRISON
                # Center garrison selling
                # Center garrison sending
                # Center garrison size

                (set_container_overlay, -1),

                (create_button_overlay, "$g_presentation_ok", "@Continue"),
                (position_set_x, pos1, 50),
                (position_set_y, pos1, 50),
                (overlay_set_position, "$g_presentation_ok", pos1),


                (presentation_set_duration, 999999),
            ]),

            (ti_on_presentation_run,
            [
                # (presentation_set_duration, 0),
            ]),


            (ti_on_presentation_event_state_change,
            [
                (store_trigger_param_1, ":object"),
                (store_trigger_param_2, ":value"),

                (assign, ":current_center", "$temp"),

                (try_begin),
                    (eq, ":object", "$g_presentation_deposit"),
                    (call_script, "script_party_transfer_wealth", "$g_player_party", ":current_center", "$g_deposit_select", tax_type_none),
                    (overlay_set_val, "$g_presentation_player_wealth_select", 0),
                    (assign, "$g_deposit_select", 0),
                (else_try),
                    (eq, ":object", "$g_presentation_withdraw"),
                    (call_script, "script_party_transfer_wealth", ":current_center", "$g_player_party", "$g_withdraw_select", tax_type_none),
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
                    (eq, ":object", "$g_presentation_ok"),

                    (presentation_set_duration, 0),
                (try_end),

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
         [(set_fixed_point_multiplier, 1000),
          (presentation_set_duration, 999999),
          ]),

        (ti_on_presentation_run,
         [
    	    (presentation_set_duration, 0),
          ]),
        ]),

    ("setting_morale", 0, mesh_load_window, [
        (ti_on_presentation_load,
         [(set_fixed_point_multiplier, 1000),
          (presentation_set_duration, 999999),
          ]),

        (ti_on_presentation_run,
         [
    	    (presentation_set_duration, 0),
          ]),
        ]),

    ("setting_death", 0, mesh_load_window, [
        (ti_on_presentation_load,
         [(set_fixed_point_multiplier, 1000),
          (presentation_set_duration, 999999),
          ]),

        (ti_on_presentation_run,
         [
    	    (presentation_set_duration, 0),
          ]),
        ]),

    ("setting_losing", 0, mesh_load_window, [
        (ti_on_presentation_load,
         [(set_fixed_point_multiplier, 1000),
          (presentation_set_duration, 999999),
          ]),

        (ti_on_presentation_run,
         [
    	    (presentation_set_duration, 0),
          ]),
        ]),

    ("setting_difficulty", 0, mesh_load_window, [
        (ti_on_presentation_load,
         [(set_fixed_point_multiplier, 1000),
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
