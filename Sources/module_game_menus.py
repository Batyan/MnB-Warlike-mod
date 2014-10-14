from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
from module_constants import *





game_menus = [

    ###############
	## Hardcoded ##
	###############
    ("start_game_0", menu_text_color(0xFF000000)|mnf_disable_all_keys,
		"Start Game 0",
		"none",
		[],
		[		
			("continue", [], "Accept",
				[
					# (set_show_messages, 0),
					# (troop_raise_attribute, "trp_player", ca_strength, 11),
					# (troop_raise_attribute, "trp_player", ca_agility, 11),
					# (troop_raise_attribute, "trp_player", ca_intelligence, 8),
					# (troop_raise_attribute, "trp_player", ca_charisma, 8),
					
					# (troop_raise_skill,"trp_player", skl_ironflesh, 3),
					# (troop_raise_skill,"trp_player", skl_power_strike, 2),
					# (troop_raise_skill,"trp_player", skl_power_throw, 2),
					# (troop_raise_skill,"trp_player", skl_power_draw, 5),
					# (troop_raise_skill,"trp_player", skl_shield, 1),
					# (troop_raise_skill,"trp_player", skl_athletics, 4),
					# (troop_raise_skill,"trp_player", skl_riding, 5),
					# (troop_raise_skill,"trp_player", skl_horse_archery, 4),
					
					# (troop_raise_skill,"trp_player", skl_inventory_management, 10),
					
					# (troop_raise_skill,"trp_player", skl_leadership, 10),
					
					# (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 90),
					# (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 90),
					# (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 90),
					# (troop_raise_proficiency_linear, "trp_player", wpt_archery, 90),
					# (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 90),
					# (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 90),
					
					# (troop_add_item, "trp_player", "itm_leather_armor", 0),
					
					# (troop_add_item, "trp_player", "itm_leather_boots", 0),
					# (troop_add_item, "trp_player", "itm_leather_gloves", 0),
					# (troop_equip_items, "trp_player"),
					
					(call_script, "script_troop_use_template_troop", "trp_player", "trp_swadian_lord_template_4"),
					(assign, "$g_test_player_troop", "trp_swadian_lord_template_4"),
					(assign, "$g_test_player_faction", "fac_small_kingdom_17"),
					
					(party_set_faction, "p_main_party", "$g_test_player_faction"),
					(try_for_range, ":unused", 0, 30),
						(call_script, "script_party_get_companion_limit", "p_main_party"),
						(assign, ":limit", reg0),
						(party_get_num_companions, ":num_troops", "p_main_party"),
						(lt, ":num_troops", ":limit"),
						(call_script, "script_party_add_reinforcements", "p_main_party"),
					(try_end),
					# (party_set_faction, "p_main_party", "fac_player_faction"),
					
					# (set_show_messages, 1),
					# (change_screen_map),
					(jump_to_menu, "mnu_start_phase_2"),
				]),
			
			("start_female", 
				[
					(troop_get_type, ":player_gender", "trp_player"),
					(try_begin),
						(eq, ":player_gender", tf_female),
						(disable_menu_option),
					(try_end),
				], "Start as female character",
				[
					(troop_set_type, "trp_player", tf_female),
					(display_message, "@Player is female"),
					(jump_to_menu, "mnu_start_game_0"),
				]),
			
			("start_male", 
				[
					(troop_get_type, ":player_gender", "trp_player"),
					(try_begin),
						(eq, ":player_gender", tf_male),
						(disable_menu_option),
					(try_end),
				], "Start as male character",
				[
					(troop_set_type, "trp_player", tf_male),
					(display_message, "@Player is male"),
					(jump_to_menu, "mnu_start_game_0"),
				]),

			("go_back",[],"Go back",
				[
					(change_screen_quit),
				]),
		]),
	
	("start_phase_2", mnf_disable_all_keys,
		"Start Phase 2",
		"none",
		[],
		[
			("continue", [], "Continue",
				[
					(change_screen_return),
				]),
			("map", [], "Map",
				[
					(change_screen_map),
				]),
		]),
	
	("start_game_3", mnf_disable_all_keys,
		"Start Game 3",
		"none",
		[],
		[
		]),
	
	("tutorial", mnf_disable_all_keys,
		"Tutorial",
		"none",
		[],
		[
			("return", [], "Return",
				[
					(change_screen_quit),
				]),
		]),

    ("reports", 0,
		"Reports",
		"none",
		[],
		[
			("resume_travelling",[],"Resume travelling",
				[
					(change_screen_return),
				]),
		]),

    ("camp", mnf_scale_picture,
		"Camp",
		"none",
		[
			(set_background_mesh, "mesh_pic_camp"),
		],
		[
			("camp_siege_battle", [], "Start a siege battle",
				[
					(jump_to_menu, "mnu_siege_battle_select"),
				]),
			
			("camp_test_battle_plain", [], "Go to plain battle test",
				[
					(store_random_in_range, ":scene", "scn_test_battle_plain", "scn_castle_01_outside"),
					(set_jump_mission, "mt_battle_test_plain"),
					(jump_to_scene, ":scene"),
					(change_screen_mission),
				]),
			
			("camp_wait_here", [], "Rest",
				[
					(rest_for_hours_interactive, 24 * 365, 5, 1),
					(change_screen_map),
				]),
			
			("camp_test_faction_relations", [], "Modify faction relations",
				[
					(jump_to_menu, "mnu_test_faction_relations"),
				]),
				
			("camp_test_join_faction", [], "Join a faction",
				[
					(store_faction_of_party, "$g_test_player_faction", "p_main_party"),
					(jump_to_menu, "mnu_test_faction_join"),
				]),
			
			("resume_travelling",[], "Dismantle camp",
				[
					(change_screen_return),
				]),
		]),
	
	###########
	## Other ##
	###########
	
	("test_faction_relations", 0,
		"Modify the faction relations",
		"none",
		[],
		[
			("faction_1", 
				[
					(try_begin),
						(neg|is_between, "$test_faction_1", kingdoms_begin, kingdoms_end),
						(assign, "$test_faction_1", kingdoms_begin),
					(try_end),
					(str_store_faction_name, s10, "$test_faction_1"),
				], "Faction 1: {s10}",
				[
					(val_add, "$test_faction_1", 1),
					(try_begin),
						(ge, "$test_faction_1", kingdoms_end),
						(assign, "$test_faction_1", kingdoms_begin),
					(try_end),
				]),
			
			("faction_2", 
				[
					(try_begin),
						(neg|is_between, "$test_faction_2", kingdoms_begin, kingdoms_end),
						(assign, "$test_faction_2", kingdoms_begin),
					(try_end),
					(str_store_faction_name, s11, "$test_faction_2"),
				], "Faction 1: {s11}",
				[
					(val_add, "$test_faction_2", 1),
					(try_begin),
						(ge, "$test_faction_2", kingdoms_end),
						(assign, "$test_faction_2", kingdoms_begin),
					(try_end),
				]),
			
			("declare_war", 
				[
					(try_begin),
						(eq, "$test_faction_1", "$test_faction_2"),
						(str_store_string, s12, "@Factions are identical!"),
						(disable_menu_option),
					(else_try),
						(store_relation, ":relation", "$test_faction_1", "$test_faction_2"),
						(lt, ":relation", relation_war),
						(str_store_string, s12, "@Factions are already at war"),
						(disable_menu_option),
					(else_try),
						(str_store_string, s12, "@Declare war"),
					(try_end),
				], "{s12}", 
				[
					(call_script, "script_faction_declare_war_to_faction", "$test_faction_1", "$test_faction_2"),
				]),
			("make_peace", 
				[
					(try_begin),
						(eq, "$test_faction_1", "$test_faction_2"),
						(str_store_string, s13, "@Factions are identical!"),
						(disable_menu_option),
					(else_try),
						(store_relation, ":relation", "$test_faction_1", "$test_faction_2"),
						(lt, ":relation", relation_friendly),
						(gt, ":relation", relation_bad),
						(str_store_string, s13, "@Factions are already at peace"),
						(disable_menu_option),
					(else_try),
						(str_store_string, s13, "@Make peace"),
					(try_end),
				], "{s13}", 
				[
					(call_script, "script_faction_make_peace_to_faction", "$test_faction_1", "$test_faction_2"),
				]),
			("make_alliance", 
				[
					(try_begin),
						(eq, "$test_faction_1", "$test_faction_2"),
						(str_store_string, s14, "@Factions are identical!"),
						(disable_menu_option),
					(else_try),
						(store_relation, ":relation", "$test_faction_1", "$test_faction_2"),
						(lt, ":relation", relation_war),
						(str_store_string, s14, "@Cannot make allies out of enemies"),
						(disable_menu_option),
					(else_try),
						(store_relation, ":relation", "$test_faction_1", "$test_faction_2"),
						(gt, ":relation", relation_allies),
						(str_store_string, s14, "@Factions are already allies"),
						(disable_menu_option),
					(else_try),
						(str_store_string, s14, "@Make an alliance"),
					(try_end),
				], "{s14}", 
				[
					(call_script, "script_faction_set_random_relation_with_faction", "$test_faction_1", "$test_faction_2", 4), # Make allies
				]),
			
			("back",[], "Back to camp",
			[
				(jump_to_menu, "mnu_camp"),
			]),
		]),
	
	("siege_battle_select", mnf_scale_picture,
		"Select a siege scene, cur scene: scene {reg10}",
		"none",
		[
			(try_begin),
				(neg|is_between, "$g_cur_selected", castle_scene_begin, castle_scene_end),
				(assign, "$g_cur_selected", castle_scene_begin),
			(try_end),
			(store_sub, reg10, "$g_cur_selected", castle_scene_begin),],
		[
			("scene_select_plus", [], "Select next scene",
				[
					(val_add, "$g_cur_selected", 1),
					(try_begin),
						(ge, "$g_cur_selected", castle_scene_end),
						(assign, "$g_cur_selected", castle_scene_begin),
					(try_end),
					(store_sub, reg10, "$g_cur_selected", castle_scene_begin),
				]),
			
			("scene_select_minus", [], "Select previous scene",
				[
					(try_begin),
						(le, "$g_cur_selected", castle_scene_begin),
						(assign, "$g_cur_selected", castle_scene_end),
					(try_end),
					(val_add, "$g_cur_selected", -1),
					(store_sub, reg10, "$g_cur_selected", castle_scene_begin),
				]),
			
			("camp_test_battle_plain", [], "Jump to battle",
				[
					(try_begin),
						(is_between, "$g_cur_selected", castle_scene_begin, castle_scene_end),
						(set_jump_mission, "mt_battle_test_siege"),
						(jump_to_scene, "$g_cur_selected"),
						(change_screen_mission),
					(else_try),
						(display_message, "@Invalid scene ID!", 0xee0000),
					(try_end),
				]),
			
			("back",[], "Back to camp",
				[
					(jump_to_menu, "mnu_camp"),
				]),
		]),
	
	("test_faction_join", mnf_scale_picture,
		"You are lord of {s11}^Join the {s12} as a {s10}",
		"none",
		[
			(str_store_troop_name, s10, "$g_test_player_troop"),
			(store_faction_of_party, ":faction", "p_main_party"),
			(str_store_faction_name, s11, ":faction"),
			(str_store_faction_name, s12, "$g_test_player_faction"),
		],
		[
			("join_next_faction", [], "Next faction",
				[
					(val_add, "$g_test_player_faction", 1),
					(try_begin),
						(ge, "$g_test_player_faction", kingdoms_end),
						(assign, "$g_test_player_faction", kingdoms_begin),
					(try_end),
					(jump_to_menu, "mnu_test_faction_join"),
				]),
			("join_previous_faction", [], "Previous faction",
				[
					(try_begin),
						(le, "$g_test_player_faction", kingdoms_begin),
						(assign, "$g_test_player_faction", kingdoms_end),
					(try_end),
					(val_add, "$g_test_player_faction", -1),
					(jump_to_menu, "mnu_test_faction_join"),
				]),
			("join_increase_lord", 
				[
					(faction_get_slot, ":culture", "$g_test_player_faction", slot_faction_culture),
					(faction_get_slot, ":template_begin", ":culture", slot_faction_template_troops_begin),
					(store_add, ":template_end", ":template_begin", 7),
					(try_begin),
						(ge, "$g_test_player_troop", ":template_end"),
						(disable_menu_option),
					(try_end),
				], "Increase rank",
				[
					(faction_get_slot, ":culture", "$g_test_player_faction", slot_faction_culture),
					(faction_get_slot, ":template_begin", ":culture", slot_faction_template_troops_begin),
					(try_begin),
						(lt, "$g_test_player_troop", ":template_begin"),
						(assign, "$g_test_player_troop", ":template_begin"),
					(else_try),
						(val_add, "$g_test_player_troop", 1),
					(try_end),
					(jump_to_menu, "mnu_test_faction_join"),
				]),
			("join_decrease_lord", 
				[
					(faction_get_slot, ":culture", "$g_test_player_faction", slot_faction_culture),
					(faction_get_slot, ":template_begin", ":culture", slot_faction_template_troops_begin),
					# (store_add, ":template_end", ":template_begin", 7),
					(try_begin),
						(le, "$g_test_player_troop", ":template_begin"),
						(disable_menu_option),
					(try_end),
				], "Decrease rank",
				[
					(faction_get_slot, ":culture", "$g_test_player_faction", slot_faction_culture),
					(faction_get_slot, ":template_begin", ":culture", slot_faction_template_troops_begin),
					(store_add, ":template_end", ":template_begin", 7),
					(try_begin),
						(gt, "$g_test_player_troop", ":template_end"),
						(assign, "$g_test_player_troop", ":template_end"),
					(else_try),
						(val_add, "$g_test_player_troop", -1),
					(try_end),
					(jump_to_menu, "mnu_test_faction_join"),
				]),
			("join_accept", [], "Join",
				[
					(party_clear, "p_main_party"),
					(party_add_leader, "p_main_party", "trp_player"),
					(call_script, "script_troop_use_template_troop", "trp_player", "$g_test_player_troop"),
					(party_set_faction, "p_main_party", "$g_test_player_faction"),
					(try_for_range, ":unused", 0, 50),
						(call_script, "script_party_get_companion_limit", "p_main_party"),
						(assign, ":limit", reg0),
						(party_get_num_companions, ":num_troops", "p_main_party"),
						(lt, ":num_troops", ":limit"),
						(call_script, "script_party_add_reinforcements", "p_main_party"),
					(try_end),
					(display_message, "@Joined!"),
					(jump_to_menu, "mnu_test_faction_join"),
				]),
			
			("join_back", [], "Back to camp",
				[
					(jump_to_menu, "mnu_camp"),
				]),
		]),
	
	("town", mnf_scale_picture,
		"You come near the gates of {s10}^You see the guards looking at you carefully",
		"none",
		[
			(str_store_party_name, s10, "$g_encountered_party"),
			(set_background_mesh, "mesh_pic_camp"),
		],
		[
			("center_enter", [], "Ask permition to enter",
				[
					(jump_to_menu,"mnu_town_center"),
				]),
			
			("center_meet_leader", [], "Ask for an audience with the leader of the garrison",
				[
					#TODO: meet leader
				]),
			
			("center_besiege", [], "Besiege the center",
				[
					#TODO: besiege
				]),
			
			#ToDo: attack the guards (if villages)
			
			("center_leave", [], "Leave center",
				[
					(leave_encounter),
					(change_screen_map),
				]),
		]),
	
	("town_center", mnf_scale_picture,
		"{s10}^^Population: {reg1}^Wealth: {reg2}^You see the guards looking at you carefully",
		"none",
		[
			(set_background_mesh, "mesh_pic_camp"),
			
			(str_store_party_name, s10,"$g_encountered_party"),
			
			(party_get_slot, reg1, "$g_encountered_party", slot_party_population),
			(party_get_slot, reg2, "$g_encountered_party", slot_party_wealth),
		],
		[
			("center_keep", [], "Head to the keep",
				[
					(jump_to_menu,"mnu_town_keep"),
				]),
			
			("center_guildmaster", 
				[
					(party_slot_eq,"$g_encountered_party", slot_party_type, spt_town),
				], "Speak to the guildmaster",
				[
					#ToDo: guildmaster
				]),
			
			("center_elder", [], "Speak to the village elder",
				[
					#ToDo: elder
				]),
			
			("center_market", [], "Go to the marketplace",
				[
					(jump_to_menu, "mnu_town_market"),
				]),
			
			("center_bank", [], "Go to the bank",
				[
					# (jump_to_menu, "mnu_town_bank"),
				]),
			
			("center_inn", 
				[
					(neg|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
				], "Go to the inn",
				[
					#ToDo: inn
				]),
			
			("center_tavern", 
				[
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
				], "Go to the tavern",
				[
					#ToDo: tavern
				]),
			
			("center_leave", [], "Leave center",
				[
					(leave_encounter),
					(change_screen_map),
				]),
		]),
	
	("town_keep", mnf_scale_picture,
	"You are in the military party of the center",
	"none",
	[
		(set_background_mesh, "mesh_pic_camp"),
		
	],
	[
		("center_manage", [], "Manage the center",
		[
			#ToDo: manage center
		]),
		
		("center_hall", [], "Go to the main hall",
		[
			#ToDo: hall
		]),
		
		("center_recruit", [], "Recruit troops",
		[
			(assign, "$temp", "$g_encountered_party"),
			(start_presentation, "prsnt_recruit_from_town_garrison"),
		]),
		
		("center_raise_levies", [(neg|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),], "Raise levies",
		[
			(jump_to_menu, "mnu_town_raise_levies"),
		]),
		
		("center_back", [], "Head back to the center",
		[
			(jump_to_menu, "mnu_town_center"),
		]),
		
		("center_leave", [], "Leave center",
		[
			(leave_encounter),
			(change_screen_map),
		]),
	]),
	
	
	("town_market", mnf_scale_picture,
	"You see all sorts of shops around you^What do you wish to buy?",
	"none",
	[
		(set_background_mesh, "mesh_pic_camp"),
	],
	[
		("center_buy_goods", [], "Buy goods",
		[
			#ToDo: buy goods
		]),
		
		("center_buy_weapons", 
		[
			(call_script, "script_party_has_building", "$g_encountered_party", "itm_building_smithy"),
			(assign, ":has_building", reg0),
			
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
			(ge, ":has_building", 1),
		], "Buy weapons",
		[
			#ToDo: buy weapons
		]),
		
		("center_buy_armors", 
		[
			(call_script, "script_party_has_building", "$g_encountered_party", "itm_building_smithy"),
			(assign, ":has_building", reg0),
			
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
			(ge, ":has_building", 1),
		], "Buy armors",
		[
			#ToDo: buy armors
		]),
		
		("center_buy_horses", 
		[
			(call_script, "script_party_has_building", "$g_encountered_party", "itm_building_stables"),
			(assign, ":has_building", reg0),
			
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
			(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
			(ge, ":has_building", 1),
		], "Buy horses",
		[
			#ToDo: buy horses
		]),
		
		("center_pawnbroker", 
		[
			# (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
		], "Go see the pawnbroker",
		[
			#ToDo: pawnbroker
		]),
		
		("center_back", [], "Head back to the center",
		[
			(jump_to_menu, "mnu_town_center"),
		]),
	]),
	
	("town_raise_levies", mnf_scale_picture,
	"How many levies do you wish to raise?^^Available recruits:{s10}",
	"none",
	[
		# (val_max, "$g_num_levies", 0),
		# (assign, reg11, "$g_num_levies"),
		
		(str_clear, s10),
		
		(store_faction_of_party, ":faction", "$g_encountered_party"),
		(faction_get_slot, ":culture", ":faction", slot_faction_culture),
		(faction_get_slot, ":peasant_begin", ":culture", slot_faction_peasant_begin),
		(faction_get_slot, ":common_begin", ":culture", slot_faction_common_begin),
		
		(try_for_range, ":cur_troop", ":peasant_begin", ":common_begin"),
			(troop_get_slot, ":only_faction_1", ":cur_troop", slot_troop_faction_reserved_1),
			(troop_get_slot, ":only_faction_2", ":cur_troop", slot_troop_faction_reserved_2),
			(troop_get_slot, ":no_faction_1", ":cur_troop", slot_troop_faction_not_1),
			(troop_get_slot, ":no_faction_2", ":cur_troop", slot_troop_faction_not_2),
			(try_begin),
				(this_or_next|eq, ":only_faction_1", -1),
				(this_or_next|eq, ":only_faction_1", ":faction"),
				(eq, ":only_faction_2", ":faction"),
				(neq, ":no_faction_1", ":faction"),
				(neq, ":no_faction_2", ":faction"),
				(str_store_troop_name, s11, ":cur_troop"),
				(str_store_string, s10, "@{s10}^{s11}"),
			(try_end),
		(try_end),
	],
	[
		("recruit_increase", [], "Increase number of recruits",
		[
			(val_add, "$g_num_levies", 1),
			(jump_to_menu, "mnu_town_raise_levies"),
		]),
		
		("recruit_decrease", [], "Decrease number of recruits",
		[
			(val_add, "$g_num_levies", -1),
			(jump_to_menu, "mnu_town_raise_levies"),
		]),
		
		("recruit_raise", 
		[
			(val_max, "$g_num_levies", 0),
			(assign, reg10, "$g_num_levies"),
			(store_mul, reg11, "$g_num_levies", 50),
			
			(store_div, ":min_hours", "$g_num_levies", 5),
			(val_add, ":min_hours", 1),
			
			(store_mul, ":num_levies_5", "$g_num_levies", 5),
			
			(store_skill_level, ":trainer", skl_trainer, "trp_player"),
			(store_add, ":div", 10, ":trainer"),
			
			(store_div, ":sub", ":num_levies_5", ":div"),
			(store_sub, ":rest_time", ":num_levies_5", ":sub"),
			
			(val_max, ":rest_time", ":min_hours"),
			(assign, reg12, ":rest_time"),
		], "Recruit {reg10} levies : {reg11} denars ({reg12} hours)",
		[
			(try_begin),
				(gt, "$g_num_levies", 0),
				(store_troop_gold, ":total_gold", "trp_player"),
				(store_mul, ":total_cost", "$g_num_levies", 50),
				(try_begin),
					(gt, ":total_gold", ":total_cost"),
					
					(store_faction_of_party, ":faction", "$g_encountered_party"),
					(faction_get_slot, ":culture", ":faction", slot_faction_culture),
					(faction_get_slot, ":peasant_begin", ":culture", slot_faction_peasant_begin),
					(faction_get_slot, ":common_begin", ":culture", slot_faction_common_begin),
					
					(party_clear, "p_temp_party"),
					(party_set_faction, "p_temp_party", ":faction"),
					(call_script, "script_party_add_troops", "p_temp_party", ":peasant_begin", ":common_begin", "$g_num_levies"),
					(party_set_faction, "p_temp_party", fac_commoners),
					
					(distribute_party_among_party_group, "p_temp_party", "p_main_party"),
					(troop_remove_gold, "trp_player", ":total_cost"),
					
					(party_clear, "p_temp_party"),
					
					(store_div, ":min_hours", "$g_num_levies", 5),
					(val_add, ":min_hours", 1),
					
					(store_mul, ":num_levies_5", "$g_num_levies", 5),
					
					(store_skill_level, ":trainer", skl_trainer, "trp_player"),
					(store_add, ":div", 10, ":trainer"),
					
					(store_div, ":sub", ":num_levies_5", ":div"),
					(store_sub, ":rest_time", ":num_levies_5", ":sub"),
					
					(val_max, ":rest_time", ":min_hours"),
					(assign, reg12, ":rest_time"),
					(display_message, "@Rest time: {reg12}"),
					(rest_for_hours, ":rest_time"),
					
					(assign, "$g_num_levies", 0),
				(else_try),
					(display_message, "@Not enough gold!", text_color_impossible),
				(try_end),
			(try_end),
			(jump_to_menu, "mnu_town_raise_levies"),
		]),
		
		("center_back", [], "Head back to the keep",
		[
			(jump_to_menu, "mnu_town_keep"),
		]),
	]),
	
	
	
	
	("simple_encounter", mnf_scale_picture,
	"Simple encounter",
	"none",
	[
		# (set_background_mesh, "mesh_pic_camp"),
	],
	[
		("encounter_meet_leader", 
		[
			(party_stack_get_troop_id, ":troop_no", "$g_encountered_party", 0),
			(str_store_troop_name, s10, ":troop_no"),], "Meet {s10}",
		[
			(call_script, "script_setup_party_meeting", "$g_encountered_party"),
		]),
		
		("encounter_attack", 
		[
			(str_store_party_name, s10, "$g_encountered_party"),
			(store_faction_of_party, ":faction", "$g_encountered_party"),
			(str_store_faction_name, s11, ":faction"),], "Attack {s10} ({s11})",
		[
			# Preparation
			(try_begin),
				# Player attacked
				(assign, "$g_attacker", "$g_encountered_party"),
				(assign, "$g_defender", "p_main_party"),
			(else_try),
				# Player_attacking
				(assign, "$g_attacker", "p_main_party"),
				(assign, "$g_defender", "$g_encountered_party"),
			(try_end),
			(party_quick_attach_to_current_battle, "p_main_party", 0),
			(party_quick_attach_to_current_battle, "$g_encountered_party", 1),
			(jump_to_menu, "mnu_encounter_battle"),
		]),
		
		("encounter_leave", [], "Leave",
		[
			(leave_encounter),
			(change_screen_map),
		]),
	]),
	
	("double_encounter", mnf_scale_picture,
	"Double encounter",
	"none",
	[
		# (set_background_mesh, "mesh_pic_camp"),
	],
	[
		("encounter_meet_leader", [], "Meet with the leader",
		[
			(call_script, "script_setup_party_meeting", "$g_encountered_party"),
		]),
		
		("encounter_meet_leader_2", [], "Meet with the leader 2",
		[
			(call_script, "script_setup_party_meeting", "$g_encountered_party_2"),
		]),
		
		("encounter_attack", [], "Attack the enemy",
		[
			# Preparation
			(try_begin),
				# Player attacked
				(assign, "$g_attacker", "$g_encountered_party"),
				(assign, "$g_defender", "p_main_party"),
			(else_try),
				# Player_attacking
				(assign, "$g_attacker", "p_main_party"),
				(assign, "$g_defender", "$g_encountered_party"),
			(try_end),
			(party_quick_attach_to_current_battle, "p_main_party", 0),
			(party_quick_attach_to_current_battle, "$g_encountered_party", 1),
			(party_quick_attach_to_current_battle, "$g_encountered_party_2", 0),
			(jump_to_menu, "mnu_encounter_battle"),
		]),
		
		("encounter_attack_2", [], "Attack the enemy 2",
		[
			# Preparation
			(try_begin),
				# Player attacked
				(assign, "$g_attacker", "$g_encountered_party_2"),
				(assign, "$g_defender", "p_main_party"),
			(else_try),
				# Player_attacking
				(assign, "$g_attacker", "p_main_party"),
				(assign, "$g_defender", "$g_encountered_party_2"),
			(try_end),
			(party_quick_attach_to_current_battle, "p_main_party", 0),
			(party_quick_attach_to_current_battle, "$g_encountered_party", 0),
			(party_quick_attach_to_current_battle, "$g_encountered_party_2", 1),
			(jump_to_menu, "mnu_encounter_battle"),
		]),
		
		("encounter_leave", [], "Leave",
		[
			(leave_encounter),
			(change_screen_map),
		]),
	]),
	
	("encounter_battle", mnf_scale_picture,
	"Encounter",
	"none",
	[
	],
	[
		("battle_charge", [], "Charge the enemy",
		[
			(set_party_battle_mode),
			(set_battle_advantage, 0),
			
			(call_script, "script_get_battle_scene"),
			(assign, ":scene", reg0),
			
			(set_jump_mission, "mt_battle_field"),
			(jump_to_scene, ":scene"),
			
			(jump_to_menu, "mnu_battle_casualties"),
			
			(change_screen_mission),
		]),
	]),
	
	("battle_casualties", mnf_scale_picture,
	"{s10}",
	"none",
	[
		# (call_script, "script_get_victory_phrase"),
		# (str_store_string_reg, s10, s0),
		(str_store_string, s10, "@The battle is over:^Casualties:"),
		(party_get_num_companions, ":num_player", "p_player_casualties"),
		(try_begin),
			(gt, ":num_player", 0),
			(assign, ":total_dead", 0),
			(assign, ":total_wounded", 0),
			(str_store_string, s10, "@{s10}^^Player casualties:"),
			(party_get_num_companion_stacks, ":num_stacks", "p_player_casualties"),
			(try_for_range, ":cur_stack", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":cur_troop", "p_player_casualties", ":cur_stack"),
				(party_stack_get_size, ":stack_size", "p_player_casualties", ":cur_stack"),
				(party_stack_get_num_wounded, ":cur_wounded", "p_player_casualties", ":cur_stack"),
				(store_sub, ":cur_dead", ":stack_size", ":cur_wounded"),
				(val_add, ":total_dead", ":cur_dead"),
				(val_add, ":total_wounded", ":cur_wounded"),
				(str_store_troop_name_by_count, s11, ":cur_troop", ":stack_size"),
				(assign, reg10, ":cur_dead"),
				(assign, reg11, ":cur_wounded"),
				(str_store_string, s10, "@{s10}^    {s11}:{reg10? {reg10} dead:}{reg11? {reg11} wounded:}"),
			(try_end),
			(assign, reg12, ":total_dead"),
			(assign, reg13, ":total_wounded"),
			(str_store_string, s10, "@{s10}^  Total: {reg12} dead {reg13} wounded"),
		(try_end),
		
		(party_get_num_companions, ":num_ally", "p_ally_casualties"),
		(try_begin),
			(gt, ":num_ally", 0),
			(assign, ":total_dead", 0),
			(assign, ":total_wounded", 0),
			(str_store_string, s10, "@{s10}^^Ally casualties:"),
			(party_get_num_companion_stacks, ":num_stacks", "p_ally_casualties"),
			(try_for_range, ":cur_stack", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":cur_troop", "p_ally_casualties", ":cur_stack"),
				(party_stack_get_size, ":stack_size", "p_ally_casualties", ":cur_stack"),
				(party_stack_get_num_wounded, ":cur_wounded", "p_ally_casualties", ":cur_stack"),
				(store_sub, ":cur_dead", ":stack_size", ":cur_wounded"),
				(val_add, ":total_dead", ":cur_dead"),
				(val_add, ":total_wounded", ":cur_wounded"),
				(str_store_troop_name_by_count, s11, ":cur_troop", ":stack_size"),
				(assign, reg10, ":cur_dead"),
				(assign, reg11, ":cur_wounded"),
				(str_store_string, s10, "@{s10}^    {s11}:{reg10? {reg10} dead:}{reg11? {reg11} wounded:}"),
			(try_end),
			(assign, reg12, ":total_dead"),
			(assign, reg13, ":total_wounded"),
			(str_store_string, s10, "@{s10}^  Total: {reg12} dead {reg13} wounded"),
		(try_end),
		
		(party_get_num_companions, ":num_enemy", "p_enemy_casualties"),
		(try_begin),
			(gt, ":num_enemy", 0),
			(assign, ":total_dead", 0),
			(assign, ":total_wounded", 0),
			(str_store_string, s10, "@{s10}^^Enemy casualties:"),
			(party_get_num_companion_stacks, ":num_stacks", "p_enemy_casualties"),
			(try_for_range, ":cur_stack", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":cur_troop", "p_enemy_casualties", ":cur_stack"),
				(party_stack_get_size, ":stack_size", "p_enemy_casualties", ":cur_stack"),
				(party_stack_get_num_wounded, ":cur_wounded", "p_enemy_casualties", ":cur_stack"),
				(store_sub, ":cur_dead", ":stack_size", ":cur_wounded"),
				(val_add, ":total_dead", ":cur_dead"),
				(val_add, ":total_wounded", ":cur_wounded"),
				(str_store_troop_name_by_count, s11, ":cur_troop", ":stack_size"),
				(assign, reg10, ":cur_dead"),
				(assign, reg11, ":cur_wounded"),
				(str_store_string, s10, "@{s10}^    {s11}:{reg10? {reg10} dead:}{reg11? {reg11} wounded:}"),
			(try_end),
			(assign, reg12, ":total_dead"),
			(assign, reg13, ":total_wounded"),
			(str_store_string, s10, "@{s10}^  Total:{reg12? {reg12} dead:}{reg13? {reg13} wounded:}"),
		(try_end),
	],
	[
		("leave", [], "Leave the battlefield",
		[
			(leave_encounter),
			(change_screen_map),
		]),
	]),
 ]
