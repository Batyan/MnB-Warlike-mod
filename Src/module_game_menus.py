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
					(assign, "$g_test_player_troop", -1),
					
					(jump_to_menu, "mnu_start_phase_2"),
				]),
			
			("start_female", 
				[
					(troop_get_type, ":player_gender", player_troop),
					(try_begin),
						(eq, ":player_gender", tf_female),
						(disable_menu_option),
					(try_end),
				], "Start as female character",
				[
					(troop_set_type, player_troop, tf_female),
					(troop_set_type, "trp_player", tf_female),
					(display_message, "@Player is female"),
					(jump_to_menu, "mnu_start_game_0"),
				]),
			
			("start_male", 
				[
					(troop_get_type, ":player_gender", player_troop),
					(try_begin),
						(eq, ":player_gender", tf_male),
						(disable_menu_option),
					(try_end),
				], "Start as male character",
				[
					(troop_set_type, player_troop, tf_male),
					(troop_set_type, "trp_player", tf_female),
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
					(jump_to_menu, "mnu_start_game_3"),
				]),
		]),
	
	("start_game_3", mnf_disable_all_keys,
		"Start Game 3",
		"none",
		[],
		[
			("continue", [], "Continue",
				[
					(change_screen_return),
					(try_begin),
						(eq, "$g_test_player_troop", -1),
						(assign, "$g_test_player_troop", "trp_swadian_light_cavalry"),

						(store_random_in_range, ":banner", banner_scene_props_begin, banner_scene_props_end),
						(troop_set_slot, player_troop, slot_troop_banner_scene_prop, ":banner"),
					(else_try),
						(neg|is_between, "$g_test_player_faction", kingdoms_begin, kingdoms_end),
						(assign, "$g_test_player_faction", "fac_kingdom_1"),
						(start_presentation, "prsnt_intro_select_kingdom"),

						# (call_script, "script_troop_copy_face_code_from_troop", player_troop, "trp_player"),
						# (set_player_troop, player_troop),
					(try_end),
				]),
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
			## General reports - displays a large amount of general informations
			# Global report shows party speed, current party size, max party size, prisoners, max prisoners, current morale, party wages
			("report_global", [(disable_menu_option),], "Global report", []),
			# Personal report shows player traits, player stat boosts, current gold, current renown, current honor rating
			("report_personal", [(disable_menu_option),], "Personal report", []),

			## Detailed reports - displays specific informations about a particular topic
			# Displays informations about party size
			("report_party_size",[],"Party size report",[(jump_to_menu, "mnu_report_party_size"),]),
			# Displays morale report
			("report_morale",[(disable_menu_option),],"Morale report",[]),
			# Displays wages for the current party (not fiefs)
			("report_wages",[(disable_menu_option),],"Party wages report",[]),

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
			("camp_settings", [], "Customize game settings",
				[(jump_to_menu, "mnu_settings"),]),
			("camp_debug_settings", [(call_script, "script_cf_debug", debug_all),], "Debug settings",
				[
					(jump_to_menu, "mnu_debug_settings"),
				]),
			("camp_debug_menu", [(call_script, "script_cf_debug", debug_all),], "Debug menu",
				[
					(jump_to_menu, "mnu_debug_menu"),
				]),
			("camp_siege_battle", [(call_script, "script_cf_debug", debug_all),], "Start a siege battle",
				[
					(jump_to_menu, "mnu_siege_battle_select"),
				]),
			
			("camp_test_face_keys", [(call_script, "script_cf_debug", debug_all),], "Test Face Keys",
				[
					(call_script, "script_troop_get_face_code", player_troop),
					(troop_set_face_keys, player_troop, s0),
					(display_message, "@Face key: {s0}"),
				]),
			
			("camp_test_battle_plain", [(call_script, "script_cf_debug", debug_all),], "Go to plain battle test",
				[
					(store_random_in_range, ":scene", "scn_test_battle_plain", castle_scene_begin),
					(assign, "$g_player_team", 0),
					(set_jump_mission, "mt_battle_test_plain"),
					(jump_to_scene, ":scene"),
					(change_screen_mission),
				]),
			
			("camp_wait_here", [], "Rest",
				[
					(rest_for_hours_interactive, 24 * 365, 5, 1),
					(change_screen_return),
					(change_screen_map),
				]),
			
			("camp_test_faction_relations", [(call_script, "script_cf_debug", debug_all),], "Modify faction relations",
				[
					(jump_to_menu, "mnu_test_faction_relations"),
				]),
				
			("camp_test_join_faction", [(call_script, "script_cf_debug", debug_all),], "Join a faction",
				[
					(store_faction_of_party, "$g_test_player_faction", "p_main_party"),
					(jump_to_menu, "mnu_test_faction_join"),
				]),
			
			("camp_train_levies", [(disable_menu_option),], "Initiate a training session",
				[
					# ToDo: training
					# Training allows player to duel his companions/troops
					# Also allows to train recruits if player/companion has at least 1 point in trainer
					# Trained recruits will most likely end up being the troop type trained by the different trainings
					# Available trainings:
					# 	horseback
					# 	lancing
					# 	spear cavalry (only rhodoks, swadians-iven and nords-rizi)
					# 	ranged (bow or crossbow depending on faction)
					# 	horse archery
					# 	melee fights (shield and sword)
					# 	melee fights (shield and spear)
					# 	melee fights (two handed swords)
					# 	skirmishing (throwing weapons)
					# 	mounted skirmishing (throwing weapons)
					# (jump_to_menu, "mnu_levy_train"),
				]),
			
			("resume_travelling",[], "Dismantle camp",
				[
					(change_screen_return),
				]),
		]),
	
	###########
	## Other ##
	###########

	("settings", 0,
		"Change the settings",
		"none",
		[],
		[
			("setting_shield",
				[], "Shield painting",
				[(start_presentation, "prsnt_setting_shield_painting"),]),
			("setting_weather",
				[], "Weather",
				[(start_presentation, "prsnt_setting_weather"),]),
			("setting_morale",
				[], "Morale",
				[(start_presentation, "prsnt_setting_morale"),]),
			("setting_death",
				[], "Death",
				[(start_presentation, "prsnt_setting_death"),]),
			("setting_losing",
				[], "Losing",
				[(start_presentation, "prsnt_setting_losing"),]),
			("setting_difficulty",
				[], "Difficulty",
				[(start_presentation, "prsnt_setting_difficulty"),]),
			("setting_misc",
				[], "Misc. settings",
				[(start_presentation, "prsnt_setting_misc"),]),
		]),

	("debug_settings", 0,
		"Change the debug settings",
		"none",
		[],
		[
			("debug_simple",
				[(try_begin),(eq, "$debug", debug_simple),(disable_menu_option),(try_end),
				], "Set debug level to simple",
				[(assign, "$debug", debug_simple),(jump_to_menu, "mnu_debug_settings"),]),
			("debug_economy",
				[(try_begin),(eq, "$debug", debug_economy),(disable_menu_option),(try_end),
				],"Set debug level to economy",
				[(assign, "$debug", debug_economy),(jump_to_menu, "mnu_debug_settings"),]),
			("debug_ai",
				[(try_begin),(eq, "$debug", debug_ai),(disable_menu_option),(try_end),
				],"Set debug level to ai",
				[(assign, "$debug", debug_ai),(jump_to_menu, "mnu_debug_settings"),]),
			("debug_war",
				[(try_begin),(eq, "$debug", debug_war),(disable_menu_option),(try_end),
				],"Set debug level to war",
				[(assign, "$debug", debug_war),(jump_to_menu, "mnu_debug_settings"),]),
			("debug_faction",
				[(try_begin),(eq, "$debug", debug_faction),(disable_menu_option),(try_end),
				],"Set debug level to faction",
				[(assign, "$debug", debug_faction),(jump_to_menu, "mnu_debug_settings"),]),
			("debug_trade",
				[(try_begin),(eq, "$debug", debug_trade),(disable_menu_option),(try_end),
				],"Set debug level to trade",
				[(assign, "$debug", debug_trade),(jump_to_menu, "mnu_debug_settings"),]),
			("debug_all",
				[(try_begin),(eq, "$debug", debug_all),(disable_menu_option),(try_end),
				],"Set debug level to all",
				[(assign, "$debug", debug_all),(jump_to_menu, "mnu_debug_settings"),]),
			("debug_disable",
				[(try_begin),(eq, "$debug", 0),(disable_menu_option),(try_end),
				],"Disable debug mode",
				[(assign, "$debug", 0),(jump_to_menu, "mnu_debug_settings"),]),
			("debug_return",
				[], "Go back",
				[(jump_to_menu, "mnu_camp"),]),
		]),

	("debug_menu", 0,
		"Debug commands",
		"none",
		[],
		[
			("debug_disable_ai",
				[(neq, "$g_disable_ai", 1)],"Disable ais",
				[(assign, "$g_disable_ai", 1),(jump_to_menu, "mnu_debug_menu"),]),
			("debug_enable_ai",
				[(eq, "$g_disable_ai", 1)],"Enable ais",
				[(assign, "$g_disable_ai", 0),(jump_to_menu, "mnu_debug_menu"),]),


			("debug_increase_haze",
				[(assign, reg10, "$g_global_haze_amount"),],"Increase Haze ({reg10})",
				[
					(val_add, "$g_global_haze_amount", 10),
					(val_min, "$g_global_haze_amount", 100),
					(assign, reg10, "$g_global_haze_amount"),
					(display_message, "@Global haze: {reg10}"),
					(jump_to_menu, "mnu_debug_menu"),
				]),
			("debug_decrease_haze",
				[(assign, reg10, "$g_global_haze_amount"),],"Decrease Haze ({reg10})",
				[
					(val_add, "$g_global_haze_amount", -10),
					(val_max, "$g_global_haze_amount", 0),
					(assign, reg10, "$g_global_haze_amount"),
					(display_message, "@Global haze: {reg10}"),
					(jump_to_menu, "mnu_debug_menu"),
				]),
			("debug_increase_cloud",
				[(assign, reg10, "$g_global_cloud_amount"),],"Increase Cloud ({reg10})",
				[
					(val_add, "$g_global_cloud_amount", 10),
					(val_min, "$g_global_cloud_amount", 100),
					(assign, reg10, "$g_global_cloud_amount"),
					(display_message, "@Global cloud: {reg10}"),
					(jump_to_menu, "mnu_debug_menu"),
				]),
			("debug_decrease_cloud",
				[(assign, reg10, "$g_global_cloud_amount"),],"Decrease Cloud ({reg10})",
				[
					(val_add, "$g_global_cloud_amount", -10),
					(val_max, "$g_global_cloud_amount", 0),
					(assign, reg10, "$g_global_cloud_amount"),
					(display_message, "@Global cloud: {reg10}"),
					(jump_to_menu, "mnu_debug_menu"),
				]),
			("debug_return",
				[], "Go back",
				[(jump_to_menu, "mnu_camp"),]),
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
						(le, ":relation", relation_war),
						(str_store_string, s14, "@Cannot make allies out of enemies"),
						(disable_menu_option),
					(else_try),
						(store_relation, ":relation", "$test_faction_1", "$test_faction_2"),
						(ge, ":relation", relation_allies),
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
			
			("camp_test_battle", [], "Jump to battle",
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
					(party_add_leader, "p_main_party", player_troop),
					(call_script, "script_troop_use_template_troop", player_troop, "$g_test_player_troop"),
					(party_set_faction, "p_main_party", "$g_test_player_faction"),
					(try_for_range, ":unused", 0, 50),
						(call_script, "script_party_get_companion_limit", "p_main_party"),
						(assign, ":limit", reg0),
						(party_get_num_companions, ":num_troops", "p_main_party"),
						(lt, ":num_troops", ":limit"),
						(call_script, "script_party_add_reinforcements", "p_main_party"),
					(try_end),
					(troop_set_faction, player_troop, "$g_test_player_faction"),
					
					(store_random_in_range, ":banner", banner_scene_props_begin, banner_scene_props_end),
					(troop_set_slot, player_troop, slot_troop_banner_scene_prop, ":banner"),
			
					(display_message, "@Joined!"),
					(jump_to_menu, "mnu_test_faction_join"),
				]),
			("join_accept_no_change", [], "Join (no player change)",
				[
					(party_set_faction, "p_main_party", "$g_test_player_faction"),
					(troop_set_faction, player_troop, "$g_test_player_faction"),
			
					(display_message, "@Joined!"),
					(jump_to_menu, "mnu_test_faction_join"),
				]),
			
			("join_era", [(faction_get_slot, reg10, "fac_kingdom_1", slot_faction_era),], "Increase era (current era: {reg10})",
				[
					(faction_get_slot, ":era", "fac_kingdom_1", slot_faction_era),
					(val_add, ":era", 1),
					(try_begin),
						(gt, ":era", 10),
						(assign, ":era", 0),
					(try_end),
					(try_for_range, ":faction", kingdoms_begin, kingdoms_end),
						(faction_set_slot, ":faction", slot_faction_era, ":era"),
					(try_end),
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


			(try_begin),
                (call_script, "script_cf_debug", debug_economy|debug_simple),
				(party_get_slot, reg1, "$g_encountered_party", slot_party_population),
				(party_get_slot, reg2, "$g_encountered_party", slot_party_wealth),
				(display_message, "@Town population : {reg1}^Town wealth : {reg2}."),

				(party_get_slot, ":total_res", "$g_encountered_party", slot_party_total_resources),
	            (str_store_party_name, s12, "$g_encountered_party"),
	            (try_begin),
                	(call_script, "script_cf_debug", debug_economy),
					(try_for_range, ":ressource", slot_party_ressources_begin, slot_party_ressources_end),
		                (party_get_slot, reg10, "$g_encountered_party", ":ressource"),
		                (gt, reg10, 0),
		                (str_store_item_name, s11, ":ressource"),
		                (display_log_message, "@Center {s12} has ressource {s11}: {reg10}."),
		            (try_end),
	            (try_end),
	            (assign, reg11, ":total_res"),
	            (display_log_message, "@{s12} has {reg11} resources."),
			(try_end),
		],
		[
			("center_enter", [], "Ask permition to enter",
				[
					(jump_to_menu,"mnu_town_center"),
				]),
			
			("center_meet_leader", [(disable_menu_option),], "Ask for an audience with the leader of the garrison",
				[
					#TODO: meet leader
				]),
			
			("center_besiege", [], "Besiege the center",
				[
					(call_script, "script_party_besiege_party", "p_main_party", "$g_encountered_party"),
					(jump_to_menu, "mnu_town_siege"),
				]),
			
			#ToDo: attack the guards (if villages)
			
			("center_leave", [], "Leave center",
				[
					# (leave_encounter),
					(change_screen_return),
					(change_screen_map),
				]),
		]),
	
	("town_center", mnf_scale_picture,
		"{s10}",
		"none",
		[
			(set_background_mesh, "mesh_pic_camp"),
			
			(str_store_string, s10, "@You are inside the walls of the city of {s11}. The streets are busy with merchants and the townsfolk seem well fed."),
			(str_store_party_name, s11,"$g_encountered_party"),
		],
		[
			("center_keep", [], "Head to the keep",
				[
					(jump_to_menu,"mnu_town_keep"),
				]),
			
			("center_guildmaster", 
				[(disable_menu_option),
					(party_slot_eq,"$g_encountered_party", slot_party_type, spt_town),
				], "Speak to the guildmaster",
				[
					#ToDo: guildmaster
				]),
			
			("center_elder", [(disable_menu_option),], "Speak to the village elder",
				[
					#ToDo: elder
				]),
			
			("center_market", [], "Go to the marketplace",
				[
					(jump_to_menu, "mnu_town_market"),
				]),
			
			("center_bank", [(disable_menu_option),], "Go to the bank",
				[
					# (jump_to_menu, "mnu_town_bank"),
				]),
			
			("center_inn", 
				[(disable_menu_option),
					(neg|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
				], "Go to the inn",
				[
					#ToDo: inn
				]),
			
			("center_tavern", 
				[(disable_menu_option),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
				], "Go to the tavern",
				[
					#ToDo: tavern
				]),
			
			("center_leave", [], "Leave center",
				[
					# (leave_encounter),
					(change_screen_return),
					(change_screen_map),
				]),
		]),
	
	("town_keep", mnf_scale_picture,
		"You are in the military section of the center",
		"none",
		[
			(set_background_mesh, "mesh_pic_camp"),
			
		],
		[
			("center_manage", [(party_slot_eq, "$g_encountered_party", slot_party_leader, player_troop),], "Manage the center",
				[
					(jump_to_menu, "mnu_town_manage"),
				]),
			
			("center_hall", [(disable_menu_option),], "Go to the main hall",
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
					# (leave_encounter),
					(change_screen_return),
					(change_screen_map),
				]),
		]),
	
	("town_market", mnf_scale_picture,
		"You see all sorts of shops around you^What do you wish to buy?",
		"none",
		[
			(set_background_mesh, "mesh_pic_camp"),
			(call_script, "script_party_update_merchants", "$g_encountered_party"),
			(assign, "$g_trading", 0),
		],
		[
			("center_buy_goods", [(disable_menu_option),], "Buy goods",
				[
					#ToDo: buy goods
					(assign, "$g_trading", 1),
				]),
			
			("center_buy_weapons", 
				[
					# (call_script, "script_party_has_building", "$g_encountered_party", "itm_building_smithy"),
					# (assign, ":has_building", reg0),
					
					# (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
					# (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
					(is_between, "$g_encountered_party", towns_begin, towns_end),
					# (ge, ":has_building", 1),
				], "Buy weapons",
				[
					#ToDo: buy weapons
					# (party_get_slot, ":party_type", "$g_encountered_party", slot_party_type),
					# (eq, ":party_type", spt_town),
					(store_sub, ":offset", "$g_encountered_party", towns_begin),
					(store_add, ":merchant", merchants_weapons_begin, ":offset"),
					# (assign, "$current_trader", ":merchant"),
					(assign, "$g_trading", 1),
					(change_screen_trade, ":merchant"),
					# (assign, "$current_trader", -1),
				]),
			
			("center_buy_smith", 
				[
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
				], "Buy gear",
				[
					(store_sub, ":offset", "$g_encountered_party", castles_begin),
					(store_add, ":merchant", merchants_smiths_begin, ":offset"),
					# (assign, "$current_trader", ":merchant"),
					(assign, "$g_trading", 1),
					(change_screen_trade, ":merchant"),
					# (assign, "$current_trader", -1),
				]),
			
			("center_buy_armors", 
				[
					# (call_script, "script_party_has_building", "$g_encountered_party", "itm_building_smithy"),
					# (assign, ":has_building", reg0),
					
					# (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
					# (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
					(is_between, "$g_encountered_party", towns_begin, towns_end),
					# (ge, ":has_building", 1),
				], "Buy armors",
				[
					# ToDo: buy armors
					(store_sub, ":offset", "$g_encountered_party", towns_begin),
					(store_add, ":merchant", merchants_armors_begin, ":offset"),
					# (assign, "$current_trader", ":merchant"),
					(assign, "$g_trading", 1),
					(change_screen_trade, ":merchant"),
					# (assign, "$current_trader", -1),
				]),
			
			("center_buy_horses", 
				[(disable_menu_option),
					(call_script, "script_party_has_building", "$g_encountered_party", "itm_building_stables"),
					(assign, ":has_building", reg0),
					
					(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
					(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
					(ge, ":has_building", 1),
				], "Buy horses",
				[
					#ToDo: buy horses
					(assign, "$g_trading", 1),
				]),
			
			("center_buy_general", 
				[
					# (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
					(this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
					(party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
				], "Go to the general store",
				[
					#ToDo: pawnbroker
					(store_sub, ":offset", "$g_encountered_party", towns_begin),
					(store_add, ":merchant", merchants_general_begin, ":offset"),
					# (assign, "$current_trader", ":merchant"),
					(assign, "$g_trading", 1),
					(change_screen_trade, ":merchant"),
					# (assign, "$current_trader", -1),
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
					# (store_mul, reg11, "$g_num_levies", train_levies_cost),

					(store_faction_of_party, ":faction", "$g_encountered_party"),
					(faction_get_slot, ":culture", ":faction", slot_faction_culture),
					(faction_get_slot, ":peasant_begin", ":culture", slot_faction_peasant_begin),
					(faction_get_slot, ":common_begin", ":culture", slot_faction_common_begin),

					(party_clear, "p_temp_party"),
					(party_set_faction, "p_temp_party", ":faction"),

					(call_script, "script_party_add_troops", "p_temp_party", ":peasant_begin", ":common_begin", "$g_num_levies"),
					(store_div, ":cost", reg1, 2),
					(call_script, "script_game_get_money_text", ":cost"),
					(str_store_string_reg, s10, s0),

					(party_set_faction, "p_temp_party", fac_commoners),
					
					(store_div, ":min_hours", "$g_num_levies", 10),
					(val_add, ":min_hours", 1),
					
					(store_mul, ":num_levies_5", "$g_num_levies", 5),
					
					(store_skill_level, ":trainer", skl_trainer, player_troop),
					(store_add, ":div", 20, ":trainer"),
					
					(store_mul, ":sub", ":num_levies_5", ":div"),
					(store_div, ":sub", ":num_levies_5", 40),
					(store_sub, ":rest_time", ":num_levies_5", ":sub"),
					(val_div, ":rest_time", 3),
					
					(val_max, ":rest_time", ":min_hours"),
					(assign, reg12, ":rest_time"),
				], "Recruit {reg10} levies : {s10} ({reg12} hours)",
				[
					(try_begin),
						(gt, "$g_num_levies", 0),
						(store_troop_gold, ":total_gold", player_troop),
						# (store_mul, ":total_cost", "$g_num_levies", train_levies_cost),
						(assign, ":total_cost", reg11),
						(try_begin),
							(gt, ":total_gold", ":total_cost"),
							
							(distribute_party_among_party_group, "p_temp_party", "p_main_party"),
							(troop_remove_gold, player_troop, ":total_cost"),
							
							(party_clear, "p_temp_party"),
							
							(store_div, ":min_hours", "$g_num_levies", 10),
							(val_add, ":min_hours", 1),
							
							(store_mul, ":num_levies_5", "$g_num_levies", 5),
							
							(store_skill_level, ":trainer", skl_trainer, player_troop),
							(store_add, ":div", 20, ":trainer"),
							
							(store_mul, ":sub", ":num_levies_5", ":div"),
							(store_div, ":sub", ":num_levies_5", 40),
							(store_sub, ":rest_time", ":num_levies_5", ":sub"),
							(val_div, ":rest_time", 3),
							
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

	("town_manage", mnf_scale_picture,
		"Here you can manage your center.",
		"none",
		[],
		[
			("manage_report", # Gives a report of current situation of town
				[(disable_menu_option),], "Center report", []),

			("manage_tax", # 
				[(disable_menu_option),], "Manage taxes", []),

			("manage_buildings", # View currently built buildings, their conditions, their upkeep
				[(disable_menu_option),], "Manage constructions", []),

			("manage_events", # Organize tournaments, festivals, plan special events
				[(disable_menu_option),], "Manage events", []),

			("manage_troops", # Allows automatic training, automatic reinforcements (both ways), set maximum garrison (up to real max)
				[(disable_menu_option),], "Manage garrison", []),

			("manage_return",
				[], "Go back", [(jump_to_menu, "mnu_town_keep"),]),
		]),
	
	("town_siege", mnf_scale_picture,
		"You are surrounding the walls of {s10}.^You can see the garrison making preparations on the battlements.",
		"none",
		[
			(str_store_party_name, s10, "$g_encountered_party"),
			(try_for_parties, ":party_no"),
				(call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "p_main_party"),
				(assign, ":continue", reg0),
				(try_begin),
					(eq, ":continue", 1),
					(str_store_party_name, s20, ":party_no"),
					(display_message, "@{s20} joins the battle on the enemy side"),
				(else_try),
					(eq, ":continue", 2),
					(str_store_party_name, s20, ":party_no"),
					(display_message, "@{s20} joins the battle on your side"),
				(try_end),
			(try_end),
		],
		[
			("siege_meeting",
				[ (disable_menu_option),], "Call for a meeting with the commander of the garrison",
				[
					# ToDo: meeting
					# Meeting will take place with player and companions/soldiers and garrison commander
					#	Can chose the number of men to bring
					#	Bringing high number of men may intimidate but can be considered dishomourable
					#	Bringing a low number (one) of men show your sincerity and honour
					# Player can chose to attack the commander
					# 	lose relation with faction, owner of center, family of commander
					# 	lose renown
					# 	lose reputation
					# 	gain morale if at war
					# 	gain relation with member of faction (not honourable ones)
					# Or to talk
				]),
			
			("siege_attack",
				[ ], "Launch the attack",
				[
					(assign, "$g_enemy", "$g_encountered_party"),
					(try_for_parties, ":party_no"),
						(call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "p_main_party"),
						(assign, ":continue", reg0),
						(try_begin),
							(eq, ":continue", 1),
							# (str_store_party_name, s20, ":party_no"),
							(party_quick_attach_to_current_battle, ":party_no", 1),
						(else_try),
							(eq, ":continue", 2),
							# (str_store_party_name, s20, ":party_no"),
							(party_quick_attach_to_current_battle, ":party_no", 0),
						(try_end),
					(try_end),
					(jump_to_menu, "mnu_encounter_battle_siege"),
				]),
			
			("siege_build_equipement",
				[ (disable_menu_option),], "Build siege equipment",
				[
					# ToDo: build ladders-siege tower
				]),
			
			("siege_cheat_capture",
				[(call_script, "script_cf_debug", debug_simple|debug_war), ], "|Cheat| Capture center",
				[
					(call_script, "script_party_group_defeat_party_group", "p_main_party", "$g_encountered_party"),
				]),
			
			("siege_wait",
				[ ], "Wait for some time",
				[
					(display_message, "@You need to stay close to the besieged center if you wish to keep it besieged."),
					(change_screen_return),
				]),
			
			("siege_leave_army",
				[ (disable_menu_option),], "Leave your army to besiege the center",
				[
					# ToDo: leave army
					# Leave most of your army (select a few troops/companions to follow you)
					# The army will stay around the center to maintain the siege
					# It will not attack the center by itself
					# If the army is not big enough, the defenders might sally out and fight the besiegers
					# 	When player arrives, the defenders will go back inside if player army+besieger is too large
					# 	else fight on the field
					# 	If besieging army is defeated in battle, player lose renown (for using bad strategies)
				]),
			
			("siege_abandon",
				[ ], "Abandon the siege",
				[
					(call_script, "script_party_lift_siege", "$g_encountered_party"),
					(change_screen_return),
				]),
		]),
	
	("siege_camp", mnf_scale_picture,
		"You spot the camp of {s10} surrounding the town of {s11}, you decide to...",
		"none",
		[
			(str_store_party_name, s11, "$g_encountered_party"),
			(party_get_slot, ":leader", "$g_encountered_party_2", slot_party_leader),
			(str_store_troop_name, s10, ":leader"),
		],
		[
			("join_defenders",
				[
				# (str_store_party_name, s11, "$g_encountered_party_2"),
				], "Sneak past the besieger and help the defenders of {s11}",
				[
					(select_enemy, 1),
					(assign, "$g_enemy", "$g_encountered_party_2"),
					(jump_to_menu, "mnu_encounter_battle_siege"),
				]),
			
			("join_attackers",
				[
				], "Join the besiegers attacking the walls",
				[
					(select_enemy, 0),
					(assign, "$g_enemy", "$g_encountered_party"),
					(jump_to_menu, "mnu_encounter_battle_siege"),
				]),
			
			("leave", [], "Leave", 
				[
					(leave_encounter),
					(change_screen_return),
				]),
		]),
	
	("simple_encounter", mnf_scale_picture,
		"Simple encounter",
		"none",
		[
			# (set_background_mesh, "mesh_pic_camp"),
			(try_for_parties, ":party_no"),
				(call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "p_main_party"),
				(assign, ":continue", reg0),
				(try_begin),
					(eq, ":continue", 1),
					(str_store_party_name, s20, ":party_no"),
					(display_message, "@{s20} joins the battle on the enemy side"),
				(else_try),
					(eq, ":continue", 2),
					(str_store_party_name, s20, ":party_no"),
					(display_message, "@{s20} joins the battle on your side"),
				(try_end),
			(try_end),
		],
		[
			("encounter_meet_leader", 
				[
					(party_stack_get_troop_id, ":troop_no", "$g_encountered_party", 0),
					(str_store_troop_name, s10, ":troop_no"),
					(party_slot_eq, "$g_encountered_party", slot_party_speak_allowed, 1),], "Meet {s10}",
				[
					(assign, "$g_talk_party", "$g_encountered_party"),
					(call_script, "script_setup_party_meeting", "$g_encountered_party"),
				]),
			
			("encounter_attack", 
				[
					(str_store_party_name, s10, "$g_encountered_party"),
					(store_faction_of_party, ":faction", "$g_encountered_party"),
					(str_store_faction_name, s11, ":faction"),], "Attack {s10} ({s11})",
				[
					# Preparation
					
					# (try_begin),
						# (encountered_party_is_attacker),
						# (assign, "$g_player_team", 1),
					# (else_try),
						(assign, "$g_player_team", 1),
					# (try_end),
					# (store_sub, ":enemy_team", 1, "$g_player_team"),
					(assign, "$g_enemy", "$g_encountered_party"),
					(try_for_parties, ":party_no"),
						(call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "p_main_party"),
						(assign, ":continue", reg0),
						(try_begin),
							(eq, ":continue", 1),
							# (str_store_party_name, s20, ":party_no"),
							(party_quick_attach_to_current_battle, ":party_no", 1),
						(else_try),
							(eq, ":continue", 2),
							# (str_store_party_name, s20, ":party_no"),
							(party_quick_attach_to_current_battle, ":party_no", 0),
						(try_end),
					(try_end),
					(jump_to_menu, "mnu_encounter_battle"),
				]),
			
			("encounter_surrender",
				[ (disable_menu_option),
				], "Surrender", []),
			
			("encounter_leave", 
				[
					(try_begin),
						(encountered_party_is_attacker),
						(disable_menu_option),
					(try_end),
				], "Leave",
				[
					(leave_encounter),
					(change_screen_return),
				]),
		]),
	
	("double_encounter", mnf_scale_picture,
		"Double encounter, not supposed to work yet",
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
					(assign, "$g_talk_party", "$g_encountered_party"),
					(call_script, "script_setup_party_meeting", "$g_encountered_party"),
				]),
			
			("encounter_meet_leader_2", 
				[
					(party_stack_get_troop_id, ":troop_no", "$g_encountered_party_2", 0),
					(str_store_troop_name, s10, ":troop_no"),], "Meet {s10}",
				[
					(assign, "$g_talk_party", "$g_encountered_party_2"),
					(call_script, "script_setup_party_meeting", "$g_encountered_party_2"),
				]),
			
			("encounter_attack", 
				[
					(str_store_party_name, s10, "$g_encountered_party"),
					(str_store_party_name, s12, "$g_encountered_party_2"),
					(store_faction_of_party, ":faction", "$g_encountered_party"),
					(store_faction_of_party, ":faction_2", "$g_encountered_party_2"),
					(str_store_faction_name, s11, ":faction"),
					(str_store_faction_name, s13, ":faction_2"),
					], "Help {s12} ({s13}) against {s10} ({s11})",
				[
					# Preparation
					(assign, "$g_enemy", "$g_encountered_party"),
					(assign, "$g_player_team", 1),
					(select_enemy, 0),
					
					(try_for_parties, ":party_no"),
						(call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "$g_encountered_party_2"),
						(assign, ":continue", reg0),
						(try_begin),
							(eq, ":continue", 1),
							# (str_store_party_name, s20, ":party_no"),
							(party_quick_attach_to_current_battle, ":party_no", 0),
						(else_try),
							(eq, ":continue", 2),
							# (str_store_party_name, s20, ":party_no"),
							(party_quick_attach_to_current_battle, ":party_no", 1),
						(try_end),
					(try_end),
					
					(jump_to_menu, "mnu_encounter_battle"),
				]),
			
			("encounter_attack_2", 
				[
					(str_store_party_name, s10, "$g_encountered_party_2"),
					(str_store_party_name, s12, "$g_encountered_party"),
					(store_faction_of_party, ":faction", "$g_encountered_party"),
					(store_faction_of_party, ":faction_2", "$g_encountered_party_2"),
					(str_store_faction_name, s11, ":faction_2"),
					(str_store_faction_name, s13, ":faction"),
					], "Join {s12} ({s13}) against {s10} ({s11})",
				[
					# Preparation
					(assign, "$g_enemy", "$g_encountered_party_2"),
					(assign, "$g_player_team", 0),
					(select_enemy, 1),
					
					(try_for_parties, ":party_no"),
						(call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "$g_encountered_party_2"),
						(assign, ":continue", reg0),
						(try_begin),
							(eq, ":continue", 1),
							# (str_store_party_name, s20, ":party_no"),
							(party_quick_attach_to_current_battle, ":party_no", 1),
						(else_try),
							(eq, ":continue", 2),
							# (str_store_party_name, s20, ":party_no"),
							(party_quick_attach_to_current_battle, ":party_no", 0),
						(try_end),
					(try_end),
					
					(jump_to_menu, "mnu_encounter_battle"),
				]),
			
			("encounter_leave", [], "Leave",
				[
					(leave_encounter),
					(change_screen_return),
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
					# (encounter_attack),
					(set_battle_advantage, 0),
					
					(call_script, "script_get_battle_scene"),
					(assign, ":scene", reg0),
					
					(set_jump_mission, "mt_battle_field"),
					(jump_to_scene, ":scene"),
					
					(assign, "$g_looted_enemies", 0),
					(jump_to_menu, "mnu_battle_casualties"),

					(change_screen_mission),
				]),
		]),
	
	("encounter_battle_siege", mnf_scale_picture,
		"Encounter",
		"none",
		[
		],
		[
			("battle_charge", [], "Charge the enemy",
				[
					(set_party_battle_mode),
					# (encounter_attack),
					(set_battle_advantage, 0),
					
					(party_get_slot, ":scene", "$g_encountered_party", slot_party_siege_scene),
					
					(set_jump_mission, "mt_battle_siege"),
					(jump_to_scene, ":scene"),
					
					(assign, "$g_looted_enemies", 0),
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

			(try_begin),
				(eq, "$g_battle_result", -1),
				(store_random_in_range, reg20, 0, 2), # outcome of the defeat
			(try_end),
		],
		[
			("defeat_taken_prisoner", [(eq, "$g_battle_result", -1),(eq, reg20, 0),],
				"You are taken prisoner by your oppenents", [(change_screen_return),]),

			("defeat_left_for_dead", [(eq, "$g_battle_result", -1),(eq, reg20, 1),],
				"Your enemies believe you dead and leave you lying on the ground", [(change_screen_return),]),

			("loot_enemies", [(eq, "$g_battle_result", 1),(neq, "$g_looted_enemies", 1),], "Loot the fallen enemies",
				[
					(call_script, "script_get_party_looted_gold", "p_enemy_casualties"),
					(assign, ":gold", reg0),
					(call_script, "script_party_group_distribute_gold", "p_main_party", ":gold"),
					(call_script, "script_party_group_defeat_party_group", "p_main_party", "$g_enemy"),

					(call_script, "script_party_get_loot", "p_enemy_casualties", 1, -1),
					(assign, ":loot_troop", reg0),
					(assign, "$g_looted_enemies", 1),
					(change_screen_loot, ":loot_troop"),

					# (change_screen_return),
				]),
			
			("loot_enemies_no_player", [(eq, "$g_battle_result", 1),(neq, "$g_looted_enemies", 1),], "Allow your men to loot the fallen enemies",
				[
					(call_script, "script_get_party_looted_gold", "p_enemy_casualties"),
					(assign, ":gold", reg0),
					(store_sqrt, ":morale", ":gold"),
					(val_div, ":morale", 50),
					(val_add, ":morale", 1),
					(call_script, "script_party_change_morale", "p_main_party", ":morale"),
					(call_script, "script_troop_change_relation_with_party_heroes", player_troop, "p_enemy_casualties", -1),
					# ToDo: reduce relation with faction and slightly with looted lords
					(call_script, "script_party_group_defeat_party_group", "p_main_party", "$g_enemy"),

					(change_screen_return),
				]),
			
			("loot_all", [(eq, "$g_battle_result", 1),(neq, "$g_looted_enemies", 1),], "Loot every fallen soldier",
				[
					(call_script, "script_get_party_looted_gold", "p_enemy_casualties"),
					(assign, ":gold", reg0),
					(call_script, "script_get_party_looted_gold", "p_ally_casualties"),
					(val_add, ":gold", reg0),
					(call_script, "script_get_party_looted_gold", "p_player_casualties"),
					(val_add, ":gold", reg0),
					(call_script, "script_party_group_distribute_gold", "p_main_party", ":gold"),

					(call_script, "script_troop_change_honor", player_troop, -1),
					(call_script, "script_party_change_morale", "p_main_party", -5),
					# ToDo: reduce relation with faction and with looted lords (includes allies at a reduced rate)
					(call_script, "script_troop_change_relation_with_party_heroes", player_troop, "p_enemy_casualties", -2),
					(call_script, "script_troop_change_relation_with_party_heroes", player_troop, "p_ally_casualties", -1),
					
					(call_script, "script_party_get_loot", "p_enemy_casualties", 1, -1),
					(assign, ":loot_troop", reg0),
					(call_script, "script_party_get_loot", "p_ally_casualties", 0, ":loot_troop"),
					(call_script, "script_party_get_loot", "p_player_casualties", 0, ":loot_troop"),
					(assign, "$g_looted_enemies", 1),
					(change_screen_loot, ":loot_troop"),
					# (change_screen_return),
				]),
			
			("leave_no_loot", [(eq, "$g_battle_result", 1),(neq, "$g_looted_enemies", 1),], "Leave the battlefield without looting",
				[
					(call_script, "script_get_party_looted_gold", "p_enemy_casualties"),
					(assign, ":gold", reg0),
					(troop_add_gold, player_troop, ":gold"),
					(call_script, "script_troop_change_honor", player_troop, 1),
					# ToDo: slightly increase relation with faction
					(call_script, "script_party_group_defeat_party_group", "p_main_party", "$g_enemy"),

					(change_screen_return),
				]),
			("leave", [(eq, "$g_battle_result", 1), (eq, "$g_looted_enemies", 1),], "Leave the battlefield",
				[
					(call_script, "script_party_group_defeat_party_group", "p_main_party", "$g_enemy"),

					(change_screen_return),
				]),
			("error_leave", [(neq, "$g_battle_result", 1),(neq, "$g_battle_result", -1),], "Error! Leave the battle",
				[
					(change_screen_return),
				]),
		]),
	
	("after_battle", mnf_scale_picture,
		"You should not be reading this",
		"none",
		[
			(change_screen_map),
		],
		[ ]),
	
	# ("visit_place", mnf_scale_picture,
		# "Visit the monument?",
		# "none", [],
		# [ 
			# ("visit_yes", [], "Yes",
			# [
				# (store_sub, ":offset", "$g_encountered_party", "p_places_stone_obelisk"),
				# (store_add, ":scene", ":offset", "scn_places_plain_stone_obelisk"),
				# (set_jump_mission, "mt_visit_place"),
				# (jump_to_scene, ":scene"),
				# (change_screen_mission),
			# ]),
			
			# ("visit_no", [], "No",
			# [
				# (change_screen_return),
			# ]),
		# ]),

	("report_party_size", mnf_scale_picture,
		"Party size report :^^Current max party size: {reg10}^Modifiers:^  - Base party size: {reg11}^  - Charisma bonus: +{reg12}^  - Leadership multiplier: {reg13}% = +{reg14}^  - Faction modifiers: {s10}{reg15}% = {s10}{reg16}",
		"none",
		[
			(call_script, "script_party_get_companion_limit", "p_main_party"),
			(assign, ":companion_limit", reg0),

			(troop_get_slot, ":rank", player_troop, slot_troop_rank),
			(store_faction_of_party, ":player_faction", "p_main_party"),

            (try_begin),
                (assign, ":base_limit", base_party_size_rank_7),
            (else_try),
                (eq, ":rank", 0),
                (assign, ":base_limit", base_party_size_rank_0),
            (else_try),
                (eq, ":rank", 1),
                (assign, ":base_limit", base_party_size_rank_1),
            (else_try),
                (eq, ":rank", 2),
                (assign, ":base_limit", base_party_size_rank_2),
            (else_try),
                (eq, ":rank", 3),
                (assign, ":base_limit", base_party_size_rank_3),
            (else_try),
                (eq, ":rank", 4),
                (assign, ":base_limit", base_party_size_rank_4),
            (else_try),
                (eq, ":rank", 5),
                (assign, ":base_limit", base_party_size_rank_5),
            (else_try),
                (eq, ":rank", 6),
                (assign, ":base_limit", base_party_size_rank_6),
            (else_try),
                (eq, ":rank", 7),
                (assign, ":base_limit", base_party_size_rank_7),
            (try_end),

            (store_attribute_level, ":charisma_bonus", player_troop, ca_charisma),

            (store_add, ":party_limit", ":base_limit", ":charisma_bonus"),

            (store_skill_level, ":leadership", skl_leadership, player_troop),
            (val_mul, ":leadership", 5),
            
            (store_mul, ":leadership_bonus", ":party_limit", ":leadership"),
            (val_div, ":leadership_bonus", 100),

            (call_script, "script_faction_get_party_size_modifier", ":player_faction"),
            (assign, ":modifier", reg0),

            (val_add, ":party_limit", ":leadership_bonus"),
            (store_sub, ":faction_bonus", ":companion_limit", ":party_limit"),

            (try_begin),
            	(gt, ":faction_bonus", 0),
            	(str_store_string, s10, "@+"),
            (else_try),
            	(str_clear, s10),
            (try_end),

            (assign, reg10, ":companion_limit"),
            (assign, reg11, ":base_limit"),
            (assign, reg12, ":charisma_bonus"),
            (assign, reg13, ":leadership"),
            (assign, reg14, ":leadership_bonus"),
            (assign, reg15, ":modifier"),
            (assign, reg16, ":faction_bonus"),
		],
		[
			("report_go_back", [], "Go back", [(change_screen_return),]),
		]),

	("player_prisoner_take_action", mnf_scale_picture, 
		"{s10} holds you prisoner, chains holding your arms and legs in place.^^You can see two guards playing cards glancing at you from time to time.^You guess that they are your jailers.",
		"none",
		[
			(troop_get_slot, ":captor", player_troop, slot_troop_prisoner_of),
			(try_begin),
				(is_between, ":captor", lords_begin, lords_end),
				(str_store_troop_name, s10, ":captor"),
			(else_try),
				(str_store_string, s10, "@Someone"),
			(try_end),
		],
		[
			("action_call_guards", [], "Call the guards", [(jump_to_menu, "mnu_player_prisoner_call_guards"),]),
			("action_insult_guards", [], "Yell insults at the guards", [(jump_to_menu, "mnu_player_prisoner_insult_guards"),]),
			("action_escape", [], "Try to find a way to escape", [(jump_to_menu, "mnu_player_prisoner_escape"),]),
			("action_do_nothing", [], "Do nothing", [(change_screen_return),]),
		]),

	("player_prisoner_call_guards", mnf_scale_picture, 
		"When you call for them, one of them turns to you, the other sighing.",
		"none",
		[],
		[
			("action_talk", [], "Talk to the guards", [(jump_to_menu, "mnu_player_prisoner_talk_guards"),]),
			("action_order_release", [], "Order your release", [(jump_to_menu, "mnu_player_prisoner_order_release"),]),
			("action_do_nothing", [], "Nevermind", [(jump_to_menu, "mnu_player_prisoner_take_action"),]),
		]),

	("player_prisoner_talk_guards", mnf_scale_picture, 
		"They both do not seem interested in talking to you, they tell you to shut up, and they go back to their game.",
		"none",
		[],
		[
			("action_insult_guards", [], "Yell insults at the guards", [(jump_to_menu, "mnu_player_prisoner_insult_guards"),]),
			("action_go_back", [], "Nevermind", [(jump_to_menu, "mnu_player_prisoner_take_action"),]),
		]),
	("player_prisoner_order_release", mnf_scale_picture, 
		"You order them to release you, but in your current state you cannot do more than.",
		"none",
		[],
		[
			("action_insult_more", [], "Keep going", [(jump_to_menu, "mnu_player_prisoner_insult_guards_more"),]),
			("action_go_back", [], "Calm down and stop", [(jump_to_menu, "mnu_player_prisoner_take_action"),]),
		]),

	("player_prisoner_insult_guards", mnf_scale_picture, 
		"You yell all sorts of insults at your jailers. They try to ignore you.",
		"none",
		[],
		[
			("action_insult_more", [], "Keep going", [(jump_to_menu, "mnu_player_prisoner_insult_guards_more"),]),
			("action_go_back", [], "Calm down and stop", [(jump_to_menu, "mnu_player_prisoner_take_action"),]),
		]),

	("player_prisoner_insult_guards_more", mnf_scale_picture, 
		"You keep yelling insults, you seem to find insults that are worst every time a new one comes out of your mouth.^After a while, you can see your jailers gritting their teeth.^A feeling of success is felt in you and it only increases the amount and the loudness of your insults.^^One of them turns at you with a cold stare.",
		"none",
		[],
		[
			("action_insult_more_and_more", [], "Personaly insult him", [(jump_to_menu, "mnu_player_prisoner_insult_guards_more_and_more"),]),
			("action_go_back", [], "Calm down and stop", [(jump_to_menu, "mnu_player_prisoner_take_action"),]),
		]),

	("player_prisoner_insult_guards_more_and_more", mnf_scale_picture, 
		"You smile, and insult him where it hurts, he gets up his chair, his friend not trying to hold him.^He pauses and seeing the smile on your face he comes to teach you a lesson.",
		"none",
		[],
		[
			("action_defy_him", [], "Keep smiling, and dare him to come", [(jump_to_menu, "mnu_player_prisoner_guard_teach_lesson"),]),
			("action_apologise", [], "Try to apologise", [(jump_to_menu, "mnu_player_prisoner_guard_teach_lesson"),]),
		]),

	("player_prisoner_guard_teach_lesson", mnf_scale_picture, 
		"He doesn't mind you anymore, you pushed him too much, now you will have to pay the price.",
		"none",
		[],
		[
			("action_hit_him_first", [], "Try to hit him first", [(jump_to_menu, "mnu_player_prisoner_guard_beating"),]),
			("action_call_for_help", [], "Call for help as you as you can", [(jump_to_menu, "mnu_player_prisoner_guard_beating"),]),
			("action_plead_mercy", [], "Plead for mercy", [(jump_to_menu, "mnu_player_prisoner_guard_beating"),]),
		]),

	("player_prisoner_guard_beating", mnf_scale_picture, 
		"Your newly found friend unleashes all his anger on you, kicking, punching, in your face, in your stomach, the force is so great you have trouble breathing.^You try to block the hits with your arms, but your chains prevent you from moving.^You try to plead him to stop, but words barely come out of your mouth.^Your strength is drained from your body, you cannot move anymore.",
		"none",
		[],
		[
			("action_blackout", [], "You feel like you are dying, you close your eyes and all becomes dark", [(troop_set_health, player_troop, 5),(jump_to_menu, "mnu_player_prisoner_guard_beating_end"),]),
		]),

	("player_prisoner_guard_beating_end", mnf_scale_picture, 
		"After a while, you regain consciousness. Your body hurts, but you manage to open your eyes.^You can see the two guards are no longer playing cards, the one that administered your punishment is leaning against a wall, you can see he is still angered but has managed to calm a little.^The other is still sat on the chair, he seems a bit concerned, but it doesn't seem to be about you, he probably had to stop him from killing you.^He stare at his friend in silence.^^You will try to remember to be a bit more careful next time.^You eyes are heavy, you feel like resting a little more...",
		"none",
		[],
		[
			("action_go_back", [], "Go back", [(change_screen_return),]),
		]),

	("player_prisoner_escape", mnf_scale_picture, 
		"In your current conditon you don't think you will be able to move at all, let alone escape.",
		"none",
		[],
		[
			("action_go_back", [], "Perhaps later...", [(jump_to_menu, "mnu_player_prisoner_take_action"),]),
		]),
 ]
