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
			("map", [], "Map",
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
					
					(call_script, "script_troop_use_template_troop", "trp_player", "trp_khergit_lord_template_7"),
					
					(try_for_range, ":troop_no", kingdom_3_troops_begin, kingdom_3_troops_end),
						(party_force_add_members, "p_main_party", ":troop_no", 2),
					(try_end),
					
					# (set_show_messages, 1),
					(change_screen_map),
				]),
			
			("start_female", [], "Start as female character.",
				[
					(troop_set_type, "trp_player", tf_female),
					(display_message, "@Player is female."),
				]),
			
			("start_male", [], "Start as male character.",
				[
					(troop_set_type, "trp_player", tf_male),
					(display_message, "@Player is male."),
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
			("resume_travelling",[],"Resume travelling.",
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
			("camp_siege_battle", [], "Start a siege battle.",
				[
					(jump_to_menu, "mnu_siege_battle_select"),
				]),
			
			("camp_test_battle_plain", [], "Go to plain battle test.",
				[
					(store_random_in_range, ":scene", "scn_test_battle_plain", "scn_castle_01_outside"),
					(set_jump_mission, "mt_battle_test_plain"),
					(jump_to_scene, ":scene"),
					(change_screen_mission),
				]),
			
			("camp_wait_here", [], "Rest.",
				[
					(rest_for_hours_interactive, 24 * 365, 5, 1),
					(change_screen_map),
				]),
			
			("camp_test_faction_relations", [], "Modify faction relations.",
				[
					(jump_to_menu, "mnu_test_faction_relations"),
				]),
			
			("resume_travelling",[], "Dismantle camp.",
				[
					(change_screen_return),
				]),
		]),
	
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
			
			("back",[], "Back to camp.",
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
			("scene_select_plus", [], "Select next scene.",
				[
					(val_add, "$g_cur_selected", 1),
					(try_begin),
						(ge, "$g_cur_selected", castle_scene_end),
						(assign, "$g_cur_selected", castle_scene_begin),
					(try_end),
					(store_sub, reg10, "$g_cur_selected", castle_scene_begin),
				]),
			
			("scene_select_minus", [], "Select previous scene.",
				[
					(try_begin),
						(le, "$g_cur_selected", castle_scene_begin),
						(assign, "$g_cur_selected", castle_scene_end),
					(try_end),
					(val_add, "$g_cur_selected", -1),
					(store_sub, reg10, "$g_cur_selected", castle_scene_begin),
				]),
			
			("camp_test_battle_plain", [], "Jump to battle.",
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
			
			("back",[], "Back to camp.",
				[
					(jump_to_menu, "mnu_camp"),
				]),
		]),
	
	
	
	
	
	###########
	## Other ##
	###########
	("town", mnf_scale_picture,
		"You come near the gates of {s10}.^You see the guards looking at you carefully.",
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
			
			("center_leave", [], "Leave center.",
				[
					(leave_encounter),
					(change_screen_map),
				]),
		]),
	
	("town_center", mnf_scale_picture,
		"{s10}^^Population: {reg1}^Wealth: {reg2}.^You see the guards looking at you carefully.",
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
			
			("center_leave", [], "Leave center.",
				[
					(leave_encounter),
					(change_screen_map),
				]),
		]),
	
	("town_keep", mnf_scale_picture,
	"You are in the military party of the center.",
	"none",
	[
		(set_background_mesh, "mesh_pic_camp"),
		
	],
	[
		("center_manage", [], "Manage the center.",
		[
			#ToDo: manage center
		]),
		
		("center_hall", [], "Go to the main hall.",
		[
			#ToDo: hall
		]),
		
		("center_recruit", [], "Recruit troops.",
		[
			(assign, "$temp", "$g_encountered_party"),
			(start_presentation, "prsnt_recruit_from_town_garrison"),
		]),
		
		("center_back", [], "Head back to the center.",
		[
			(jump_to_menu, "mnu_town_center"),
		]),
		
		("center_leave", [], "Leave center.",
		[
			(leave_encounter),
			(change_screen_map),
		]),
	]),
	
	
	("town_market", mnf_scale_picture,
	"You see all sorts of shop around you^What do you wish to buy?.",
	"none",
	[
		(set_background_mesh, "mesh_pic_camp"),
	],
	[
		("center_buy_goods", [], "Buy goods.",
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
		], "Buy weapons.",
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
		], "Buy armors.",
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
		], "Buy horses.",
		[
			#ToDo: buy horses
		]),
		
		("center_pawnbroker", 
		[
			# (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
		], "Go see the pawnbroker.",
		[
			#ToDo: pawnbroker
		]),
		
		("center_back", [], "Head back to the center.",
		[
			(jump_to_menu, "mnu_town_center"),
		]),
	]),
	
	
	
	
	("simple_encounter", mnf_scale_picture,
	"Simple encounter",
	"none",
	[
		# (set_background_mesh, "mesh_pic_camp"),
	],
	[
		("encounter_meet_leader", [], "Meet with the leader.",
		[
			(call_script, "script_setup_party_meeting", "$g_encountered_party"),
		]),
		
		("encounter_attack", [], "Attack the enemy.",
		[]),
		
		("encounter_leave", [], "Leave.",
		[
			(leave_encounter),
			(change_screen_map),
		]),
	]),
 ]
