from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
import string





presentations = [

    ###############
    ## Hardcoded ##
	###############
  ("game_profile_banner_selection", 0, mesh_load_window, [
    (ti_on_presentation_load,
     [(set_fixed_point_multiplier, 1000),
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
			
			# (party_get_free_companions_capacity, reg11, "p_main_party"),
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
					(party_stack_get_size, ":stack_size", ":current_city", ":stack_no"),
					(assign, reg1, ":stack_size"),
					
					(str_store_troop_name, s1, ":troop_no"),
					
					(call_script, "script_troop_get_cost", ":troop_no"),
					(assign, ":troop_cost", reg0),
					
					(call_script, "script_troop_get_cost_modifier", ":troop_no", ":current_city", "trp_player"),
					(assign, ":cost_modifier", reg0),
					(val_mul, ":troop_cost", ":cost_modifier"),
					(val_div, ":troop_cost", 100),
					
					(assign, reg2, ":troop_cost"),
					
					(create_text_overlay, reg0, "@{s1}: {reg2} denars ({reg1})", tf_left_align),
					
					(position_set_x, pos1, ":names_x"),
					(position_set_y, pos1, ":cur_y"),
					(overlay_set_position, reg0, pos1),
					(position_set_x, pos1, 1000),
					(position_set_y, pos1, 1000),
					(overlay_set_size, reg0, pos1),
					
					(store_add, ":max_taken", ":stack_size", 1),
					(try_begin),
						(troop_is_hero, ":troop_no"),
						(assign, ":max_taken", 0),
					(try_end),
					(create_number_box_overlay, reg0, 0, ":max_taken"),
					
					(position_set_x, pos1, ":numberbox_x"),
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
			(position_set_y, pos1, 120),
			(overlay_set_position, "$g_hire_soldiers_total_cost", pos1),
			(position_set_x, pos1, 1000),
			(position_set_y, pos1, 1000),
			(overlay_set_size, "$g_hire_soldiers_total_cost", pos1),
			# Current money
			(store_troop_gold, reg0, "trp_player"),
			(str_store_string, s0, "@Current money: {reg0} denars"),
			(create_text_overlay, reg0, s0, tf_left_align),
			(position_set_x, pos1, 200),
			(position_set_y, pos1, 90),
			(overlay_set_position, reg0, pos1),
			(position_set_x, pos1, 1000),
			(position_set_y, pos1, 1000),
			(overlay_set_size, reg0, pos1),
			
			# Party size
			(call_script, "script_party_get_companion_limit", "p_main_party"),
			(assign, reg10, reg0),
			(party_get_num_companions, reg11, "p_main_party"),
			(str_store_string, s0, "@Party size: {reg11}/{reg10}"),
			(create_text_overlay, "$g_hire_soldiers_free_capacity", s0, tf_left_align),
			(position_set_x, pos1, 200),
			(position_set_y, pos1, 60),
			(overlay_set_position, "$g_hire_soldiers_free_capacity", pos1),
			(position_set_x, pos1, 1000),
			(position_set_y, pos1, 1000),
			(overlay_set_size, "$g_hire_soldiers_free_capacity", pos1),
			
			(store_add, "$g_hide_soldiers_portrait_begin", "$g_hire_soldiers_free_capacity", 1),
			# Troop picture
			(party_get_num_companion_stacks, ":num_stacks", ":current_city"),
			(try_for_range, ":stack_no", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":troop_no", ":current_city", ":stack_no"),
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
			(position_set_y, pos1, 120),
			(overlay_set_position, "$g_presentation_ok", pos1),
			
			# Cancel button
			(create_button_overlay, "$g_presentation_cancel", "@Cancel"),
			(position_set_x, pos1, 50),
			(position_set_y, pos1, 90),
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
				
				(call_script, "script_calculate_hire_troop_cost", ":current_city", "trp_player"),
				(assign, ":total_cost", reg0),
				(assign, ":total_num_troops", reg1),
				(party_get_free_companions_capacity, ":free_slots", "p_main_party"),
				
				(store_troop_gold, ":player_gold", "trp_player"),
				(try_begin),
					(gt, ":total_cost", ":player_gold"),
					(assign, reg2, ":player_gold"),
					(display_message, "@You do not have enough gold! You currently possess {reg2} denars.", text_color_impossible),
				(else_try),
					(gt, ":total_num_troops", ":free_slots"),
					(assign, reg2, ":free_slots"),
					(display_message, "@Party size not big enough! You can only hold up to {reg2} more troops", text_color_impossible),
				(else_try),
					(party_get_num_companion_stacks, ":num_stacks", ":current_city"),
					(try_for_range_backwards, ":stack_no", 0, ":num_stacks"),
						(party_stack_get_troop_id, ":troop_no", ":current_city", ":stack_no"),
						(troop_get_slot, ":num_troops", ":troop_no", slot_troop_temp_hire_number),
						(gt, ":num_troops", 0),
						(party_add_members, "p_main_party", ":troop_no", ":num_troops"),
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
							
							(call_script, "script_troop_get_cost_modifier", ":troop_no", ":current_city", "trp_player"),
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
					
					(troop_remove_gold, "trp_player", ":total_cost"),
					# Restart the presentation
					(assign, "$temp", ":current_city"),
					(start_presentation, "prsnt_recruit_from_town_garrison"),
				(try_end),
			(else_try),
				(is_between, ":object", "$g_hire_soldiers_center_troops_begin", "$g_hire_soldiers_center_troops_end"),
				
				# (party_get_num_companion_stacks, ":num_stacks", ":current_city"),
				(store_sub, ":troop_stack", ":object", "$g_hire_soldiers_center_troops_begin"),
				(val_div, ":troop_stack", 2),
				(party_stack_get_troop_id, ":troop_no", ":current_city", ":troop_stack"),
				(troop_set_slot, ":troop_no", slot_troop_temp_hire_number, ":value"),
				(overlay_set_val, ":object", ":value"),
				
				(call_script, "script_calculate_hire_troop_cost", ":current_city", "trp_player"),
				(assign, ":total_cost", reg0),
				(assign, ":num_troops", reg1),
				(overlay_set_text, "$g_hire_soldiers_total_cost", "@Total cost: {reg0} denars"),
				
				(call_script, "script_party_get_companion_limit", "p_main_party"),
				(assign, ":limit", reg0),
				(assign, reg10, ":limit"),
				(party_get_num_companions, ":total", "p_main_party"),
				(val_add, ":total", ":num_troops"),
				(assign, reg11, ":total"),
				(overlay_set_text, "$g_hire_soldiers_free_capacity", "@Party size: {reg11}/{reg10}"),
				(try_begin),
					(store_troop_gold, ":player_gold", "trp_player"),
					(gt, ":total_cost", ":player_gold"),
					(overlay_set_color, "$g_hire_soldiers_total_cost", text_color_impossible),
				(else_try),
					(overlay_set_color, "$g_hire_soldiers_total_cost", 0x000000),
				(try_end),
				(try_begin),
					(gt, ":total", ":limit"),
					(overlay_set_color, "$g_hire_soldiers_free_capacity", text_color_impossible),
				(else_try),
					(overlay_set_color, "$g_hire_soldiers_free_capacity", 0x000000),
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
			
			(create_combo_button_overlay, "$g_culture_choice"),
			(position_set_x, pos1, 240),
			(position_set_y, pos1, 500),
			(overlay_set_position, "$g_culture_choice", pos1),
			(position_set_x, pos1, 1000),
			(position_set_y, pos1, 1000),
			(overlay_set_size, "$g_culture_choice", pos1),
			
			(try_for_range_backwards, ":culture", cultures_begin, cultures_end),
				(str_store_faction_name, s10, ":culture"),
				(overlay_add_item, "$g_culture_choice", s10),
				
				# Faction selection
				(create_combo_button_overlay, reg0),
				(position_set_x, pos1, 240),
				(position_set_y, pos1, 400),
				(overlay_set_position, reg0, pos1),
				(position_set_x, pos1, 1000),
				(position_set_y, pos1, 1000),
				(overlay_set_size, reg0, pos1),
				(assign, ":num_factions", -1),
				(try_for_range_backwards, ":faction", kingdoms_begin, kingdoms_end),
					(faction_slot_eq, ":faction", slot_faction_culture, ":culture"),
					(str_store_faction_name, s10, ":faction"),
					(overlay_add_item, reg0, s10),
					(val_add, ":num_factions", 1),
				(try_end),
				(overlay_set_val, reg0, ":num_factions"),
				(overlay_set_display, reg0, 0),
			(try_end),
			
			(store_add, reg0, "$g_culture_choice", 6),
			(overlay_set_display, reg0, 1),
			(overlay_set_val, "$g_culture_choice", 5),
			
			(str_store_string, s0, "@Select the faction you wish to join"),
			(create_text_overlay, reg0, s0, tf_left_align),
			(position_set_x, pos1, 50),
			(position_set_y, pos1, 450),
			(overlay_set_position, reg0, pos1),
			(position_set_x, pos1, 1000),
			(position_set_y, pos1, 1000),
			(overlay_set_size, reg0, pos1),
			
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
				
				(troop_set_faction, "trp_player", "$g_test_player_faction"),
				
				(party_set_faction, "p_main_party", "$g_test_player_faction"),
				(try_for_range, ":unused", 0, 30),
					(call_script, "script_party_get_companion_limit", "p_main_party"),
					(assign, ":limit", reg0),
					(party_get_num_companions, ":num_troops", "p_main_party"),
					(lt, ":num_troops", ":limit"),
					(call_script, "script_party_add_reinforcements", "p_main_party"),
				(try_end),
				
				(assign, reg10, "$g_test_player_faction"),
				(str_store_faction_name, s10, "$g_test_player_faction"),
				(display_message, "@Faction is {reg10}: {s10}"),
				
				(presentation_set_duration, 1),
			(else_try),
				(eq, ":object", "$g_culture_choice"),
				(store_add, ":faction_choice", "$g_culture_choice", 1),
				
				(store_sub, ":num_cultures", cultures_end, cultures_begin),
				(try_for_range, ":overlay", 0, ":num_cultures"),
					(val_add, ":overlay", ":faction_choice"),
					(overlay_set_display, ":overlay", 0),
				(try_end),
				
				(val_add, ":faction_choice", ":value"),
				(overlay_set_display, ":faction_choice", 1),
				(assign, ":faction", 0),
				
				(store_sub, ":culture", ":num_cultures", ":value"),
				(val_sub, ":culture", 1),
				(val_add, ":culture", cultures_begin),
				
				(assign, ":num_factions", 0),
				(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
					(faction_slot_eq, ":faction_no", slot_faction_culture, ":culture"),
					(val_add, ":num_factions", 1),
				(try_end),
				(val_sub, ":num_factions", 1),
				(overlay_set_val, ":faction_choice", ":num_factions"),
				
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
			(else_try),
				(store_sub, ":num_cultures", cultures_end, cultures_begin),
				(store_add, ":bot", "$g_culture_choice", 1),
				(store_add, ":top", ":bot", ":num_cultures"),
				(is_between, ":object", ":bot", ":top"),
				
				(store_sub, ":offset", ":object", ":bot"),
				(store_sub, ":culture", ":num_cultures", ":offset"),
				(val_sub, ":culture", 1),
				(val_add, ":culture", cultures_begin),
				
				(assign, ":num_factions", 0),
				(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
					(faction_slot_eq, ":faction_no", slot_faction_culture, ":culture"),
					(val_add, ":num_factions", 1),
				(try_end),
				(store_sub, ":count", ":num_factions", ":value"),
				(val_sub, ":count", 1),
				
				(assign, ":end", kingdoms_end),
				
				(try_for_range, ":faction", kingdoms_begin, ":end"),
					(faction_slot_eq, ":faction", slot_faction_culture, ":culture"),
					(try_begin),
						(eq, ":count", 0),
						(assign, ":end", 0),
						(assign, "$g_test_player_faction", ":faction"),
					(else_try),
						(val_sub, ":count", 1),
					(try_end),
				(try_end),
				
				(assign, reg10, "$g_test_player_faction"),
				(str_store_faction_name, s10, "$g_test_player_faction"),
				(display_message, "@Faction is {reg10}: {s10}"),
			(try_end),
		]),
	]),
]
