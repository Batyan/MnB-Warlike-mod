from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from ID_animations import *


scripts = [	
	
	###############
	## Hardcoded ##
	###############

	# script_game_start:
	# This script is called when a new game is started
	# INPUT: none
	("game_start",
		[
			(set_player_troop, "trp_player"),
			
			# (party_set_slot, "p_main_party", slot_party_type, spt_war_party),
			
			(call_script, "script_init_factions"),
			(call_script, "script_init_cultures"),
			(call_script, "script_init_bandits"),
			(call_script, "script_init_mercenaries"),
			
			(call_script, "script_init_building_slots"),
			(call_script, "script_init_siege_scene_slots"),
			
			(call_script, "script_init_troops_types"),
			(call_script, "script_init_troops_factions"),
			
			(try_for_range, ":cur_center", towns_begin, towns_end),
				(party_set_slot, ":cur_center", slot_party_type, spt_town),
			(try_end),
			
			(try_for_range, ":cur_center", castles_begin, castles_end),
				(party_set_slot, ":cur_center", slot_party_type, spt_castle),
				(assign, ":best", -1),
				(assign, ":best_dist", 999),
				(try_for_range, ":village", villages_begin, villages_end),
					(store_distance_to_party_from_party, ":dist", ":cur_center", ":village"),
					(try_begin),
						(lt, ":dist", ":best_dist"),
						(assign, ":best_dist", ":dist"),
						(assign, ":best", ":village"),
					(try_end),
				(try_end),
				(party_set_slot, ":cur_center", slot_party_linked_party, ":best"),
				(party_set_slot, ":best", slot_party_linked_party, ":cur_center"),
			(try_end),
			
			(try_for_range, ":cur_center", villages_begin, villages_end),
				(party_set_slot, ":cur_center", slot_party_type, spt_village),
				(neg|party_slot_ge, ":cur_center", slot_party_linked_party, 1),
				(assign, ":best", -1),
				(assign, ":best_dist", 999),
				(try_for_range, ":town", towns_begin, towns_end),
					(store_distance_to_party_from_party, ":dist", ":cur_center", ":town"),
					(try_begin),
						(lt, ":dist", ":best_dist"),
						(assign, ":best_dist", ":dist"),
						(assign, ":best", ":town"),
					(try_end),
				(try_end),
				(party_set_slot, ":cur_center", slot_party_linked_party, ":best"),
			(try_end),
			
			(faction_set_slot, "fac_kingdom_1", slot_faction_leader, "trp_swadian_lord_1"),
			(faction_set_slot, "fac_kingdom_2", slot_faction_leader, "trp_vaegir_lord_1"),
			(faction_set_slot, "fac_kingdom_3", slot_faction_leader, "trp_khergit_lord_1"),
			(faction_set_slot, "fac_kingdom_4", slot_faction_leader, "trp_nord_lord_1"),
			(faction_set_slot, "fac_kingdom_5", slot_faction_leader, "trp_rhodok_lord_1"),
			(faction_set_slot, "fac_kingdom_6", slot_faction_leader, "trp_sarranid_lord_1"),
			(try_for_range, ":small_kingdom", small_kingdoms_begin, small_kingdoms_end),
				(faction_set_slot, ":small_kingdom", slot_faction_leader, -1),
			(try_end),
			# (faction_set_slot, "fac_small_kingdom_11", slot_faction_leader, "trp_swadian_lord_21"),
			# (faction_set_slot, "fac_small_kingdom_12", slot_faction_leader, "trp_swadian_lord_23"),
			# (faction_set_slot, "fac_small_kingdom_13", slot_faction_leader, "trp_swadian_lord_25"),
			# (faction_set_slot, "fac_small_kingdom_14", slot_faction_leader, "trp_swadian_lord_30"),
			# (faction_set_slot, "fac_small_kingdom_15", slot_faction_leader, "trp_swadian_lord_32"),
			# (faction_set_slot, "fac_small_kingdom_16", slot_faction_leader, "trp_swadian_lord_36"),
			# (faction_set_slot, "fac_small_kingdom_17", slot_faction_leader, "trp_swadian_lord_38"),
			# (faction_set_slot, "fac_small_kingdom_63", slot_faction_leader, "trp_sarranid_lord_27"),
			# (faction_set_slot, "fac_small_kingdom_53", slot_faction_leader, "trp_rhodok_lord_25"),
			
			(try_for_range, ":party_no", centers_begin, centers_end),
				(call_script, "script_party_init_center", ":party_no"),
			(try_end),
			
			(try_for_range, ":lord_no", lords_begin, lords_end),
				(store_troop_faction, ":original_faction", ":lord_no"),
				(troop_set_slot, ":lord_no", slot_troop_original_faction, ":original_faction"),
			(try_end),
			
			(try_for_range, ":lord_no", lords_begin, lords_end),
				(call_script, "script_init_lord", ":lord_no"),
			(try_end),
			
			(set_show_messages, 0),
			(try_for_range, ":center_no", centers_begin, centers_end),
				(store_faction_of_party, ":faction_no", ":center_no"),
				(call_script, "script_faction_get_best_candidate_for_center", ":faction_no", ":center_no"),
				(assign, ":troop_no", reg0),
				
				(gt, ":troop_no", -1),
				(call_script, "script_give_center_to_troop", ":center_no", ":troop_no"),
				
				(troop_get_slot, ":rank", ":troop_no", slot_troop_rank),
				(troop_get_slot, ":level", ":troop_no", slot_troop_level),
				(neq, ":rank", ":level"),
				(call_script, "script_troop_change_level", ":troop_no", ":rank"),
			(try_end),
			
			(try_for_range, ":party_no", centers_begin, centers_end),
				(party_get_slot, ":party_type", ":party_no", slot_party_type),
				(try_begin),
					(eq, ":party_type", spt_town),
					
					(party_set_slot, ":party_no", slot_party_population, 1000),
					(party_set_slot, ":party_no", slot_party_wealth, 5000),
					(try_for_range, ":unused", 0, 40),
						(call_script, "script_party_recruit_troops", ":party_no"),
					(try_end),
				(else_try),
					(eq, ":party_type", spt_castle),
					(party_set_slot, ":party_no", slot_party_population, 100),
					(party_set_slot, ":party_no", slot_party_wealth, 500),
					(try_for_range, ":unused", 0, 30),
						(call_script, "script_party_recruit_troops", ":party_no"),
					(try_end),
				(else_try),
					(eq, ":party_type", spt_village),
					(party_set_slot, ":party_no", slot_party_population, 100),
					(party_set_slot, ":party_no", slot_party_wealth, 250),
					(call_script, "script_party_recruit_troops", ":party_no"),
				(try_end),
				# (party_set_slot, ":party_no", slot_party_lord, -1),
			(try_end),
			
			(set_show_messages, 1),
		]),

	#script_game_quick_start
	# This script is called from the game engine for initializing the global variables for tutorial, multiplayer and custom battle modes.
	# INPUT:
	# none
	# OUTPUT:
	# none
	("game_quick_start",
		[
		]),

	#script_game_set_multiplayer_mission_end
	# This script is called from the game engine when a multiplayer map is ended in clients (not in server).
	# INPUT:
	# none
	# OUTPUT:
	# none
	("game_set_multiplayer_mission_end",
		[
			(assign, "$g_multiplayer_mission_end_screen", 1),
		]),
	
	#script_game_get_use_string
	# This script is called from the game engine for getting using information text
	# INPUT: used_scene_prop_id  
	# OUTPUT: s0
	("game_get_use_string",
		[
		]),
	
	#script_game_enable_cheat_menu
	# This script is called from the game engine when user enters "cheatmenu from command console (ctrl+~).
	# INPUT:
	# none
	# OUTPUT:
	# none
	("game_enable_cheat_menu",
		[
		]),  

	# script_game_event_party_encounter:
	# This script is called from the game engine whenever player party encounters another party or a battle on the world map
	# INPUT:
	# param1: encountered_party
	# param2: second encountered_party (if this was a battle
	("game_event_party_encounter",
		[
			(store_script_param_1, "$g_encountered_party"),
			(store_script_param_2, "$g_encountered_party_2"), #Negative if non-battle.
			
			(party_get_slot, ":party_type", "$g_encountered_party", slot_party_type),
			
			(try_begin),
				(lt, "$g_encountered_party_2", 0), #Non-battle.
				(try_begin),
					(eq, "$g_encountered_party", "p_camp_bandits"), #Camp.
					(jump_to_menu, "mnu_camp"),
				(else_try),
					(this_or_next|eq, ":party_type", spt_town),
					(this_or_next|eq, ":party_type", spt_village),
					(eq, ":party_type", spt_castle),
					(jump_to_menu, "mnu_town"),
				(else_try),
					(jump_to_menu, "mnu_simple_encounter"),
				(try_end),
			(else_try),
				# Battle between two parties
				(jump_to_menu, "mnu_double_encounter"),
			(try_end),
		]),

	# script_game_event_simulate_battle:
	# This script is called whenever the game simulates the battle between two parties on the map.
	# INPUT:
	# param1: Defender Party
	# param2: Attacker Party
	("game_event_simulate_battle",
		[
			(store_script_param, ":defender_party", 1),
			(store_script_param, ":attacker_party", 2),
			
			(assign, ":result", 0),
			
			(party_get_slot, ":party_type", ":defender_party", slot_party_type),
			
			(try_begin),
				(store_faction_of_party, ":defender_faction", ":defender_party"),
				(store_faction_of_party, ":attacker_faction", ":attacker_party"),
				
				(store_relation, ":relation", ":defender_faction", ":attacker_faction"),
				
				(this_or_next|eq, ":defender_faction", ":attacker_faction"),
				(ge, ":relation", 0),
				
				(assign, ":result", 1),
			(else_try),
				(party_collect_attachments_to_party, ":defender_party", "p_collective_defender"),
				(party_collect_attachments_to_party, ":attacker_party", "p_collective_attacker"),
				
				(call_script, "script_party_count_fit_for_battle", "p_collective_defender", 0),
				(assign, ":num_defenders", reg0),
				(call_script, "script_party_count_fit_for_battle", "p_collective_attacker", 0),
				(assign, ":num_attackers", reg0),
				(try_begin),
					(eq, ":num_defenders", 0),
					(assign, ":result", 1),
					(try_begin),
						(this_or_next|eq, ":party_type", spt_town),
						(this_or_next|eq, ":party_type", spt_castle),
						(eq, ":party_type", spt_village),
						(call_script, "script_party_group_defeat_party_group", ":attacker_party", ":defender_party"),
					(else_try),
						(call_script, "script_party_group_defeat_party_group", ":attacker_party", ":defender_party"),
					(try_end),
				(else_try),
					(eq, ":num_attackers", 0),
					(assign, ":result", 1),
					(call_script, "script_party_group_defeat_party_group", ":defender_party", ":attacker_party"),
				(else_try),
					# (inflict_casualties_to_party_group, ":defender_party", 20, "p_temp_casualties"),
					(call_script, "script_party_groups_simulate_battle", ":attacker_party", ":defender_party"),
				(try_end),
			(try_end),
			
			# ToDo: simulate battle
			(set_trigger_result, ":result"),
		]),
	
	# script_party_groups_simulate_battle
	# input:
	# 	arg1: attacker
	# 	arg2: defender
	# output: none
	("party_groups_simulate_battle",
		[
			(store_script_param, ":attacker", 1),
			(store_script_param, ":defender", 2),
			
			# (party_get_slot, ":attacker_type", ":attacker", slot_party_type),
			(party_get_slot, ":defender_type", ":defender", slot_party_type),
			
			(party_get_slot, ":stage", ":attacker", slot_party_battle_stage),
			(try_begin),
				(is_between, ":stage", bs_approach, bs_charge),
				# Approach
				(call_script, "script_party_groups_simulate_battle_approach", ":attacker", ":defender"),
				(assign, ":attacker_strength", reg0),
				(assign, ":defender_strength", reg1),
				
				(val_add, ":stage", 1),
				(party_set_slot, ":attacker", slot_party_battle_stage, ":stage"),
			(else_try),
				(is_between, ":stage", bs_charge, bs_melee),
				# Charge
				(call_script, "script_party_groups_simulate_battle_charge", ":attacker", ":defender"),
				(assign, ":attacker_strength", reg0),
				(assign, ":defender_strength", reg1),
				
				(val_add, ":stage", 1),
				(party_set_slot, ":attacker", slot_party_battle_stage, ":stage"),
			(else_try),
				(eq, ":stage", bs_melee),
				# Melee
				(call_script, "script_party_groups_simulate_battle_melee", ":attacker", ":defender"),
				(assign, ":attacker_strength", reg0),
				(assign, ":defender_strength", reg1),
			(else_try),
				(party_set_slot, ":attacker", slot_party_battle_stage, bs_approach),
				(assign, ":attacker_strength", 0),
				(assign, ":defender_strength", 0),
			(try_end),
			
			# Conclusion
			(try_begin),
				(this_or_next|eq, ":defender_type", spt_castle),
				(eq, ":defender_type", spt_town),
				(val_div, ":attacker_strength", 2),
				(val_add, ":defender_strength", 1500),
			(else_try),
				(eq, ":defender_type", spt_village),
				(val_add, ":defender_strength", 750),
				(val_mul, ":attacker_strength", 2),
				(val_div, ":attacker_strength", 3),
			(try_end),
			(try_begin),
				(val_div, ":attacker_strength", 150),
				(val_div, ":defender_strength", 150),
				(val_add, ":attacker_strength", 5),
				(val_add, ":defender_strength", 5),
				(try_begin),
					(this_or_next|eq, ":defender_type", spt_castle),
					(eq, ":defender_type", spt_town),
					(val_min, ":attacker_strength", 40),
					(val_min, ":defender_strength", 50),
				(else_try),
					(val_min, ":attacker_strength", 45),
					(val_min, ":defender_strength", 45),
				(try_end),
			(try_end),
			(try_begin),
				(assign, reg12, ":stage"),
				(str_store_party_name, s10, ":attacker"),
				(str_store_party_name, s11, ":defender"),
				(assign, reg10, ":attacker_strength"),
				(assign, reg11, ":defender_strength"),
				(display_message, "@Stage {reg12}^{s10}'s strength: {reg10}.^{s11}'s strength: {reg11}."),
			(try_end),
			(try_begin),
				(gt, ":attacker_strength", 0),
				(inflict_casualties_to_party_group, ":defender", ":attacker_strength", "p_temp_casualties"),
			(try_end),
			(try_begin),
				(gt, ":defender_strength", 0),
				(inflict_casualties_to_party_group, ":attacker", ":defender_strength", "p_temp_casualties"),
			(try_end),
		]),
	
	# script_party_groups_simulate_battle_approach
	# input:
	# 	arg1: attacker
	# 	arg2: defender
	# output:
	# 	reg0: attacker_strength
	# 	reg1: defender_strength
	("party_groups_simulate_battle_approach",
		[
			(store_script_param, ":attacker", 1),
			(store_script_param, ":defender", 2),
			
			(call_script, "script_party_group_calculate_strength_approach", ":attacker"),
			(assign, ":attacker_strength", reg0),
			(assign, ":attacker_defense", reg1),
			(call_script, "script_party_group_calculate_strength_approach", ":defender"),
			(assign, ":defender_strength", reg0),
			(assign, ":defender_defense", reg1),
			
			(val_mul, ":attacker_strength", ":defender_defense"),
			(val_div, ":attacker_strength", 100),
			(val_mul, ":defender_strength", ":attacker_defense"),
			(val_div, ":defender_strength", 100),
			
			# Defenders have a small bonus during the approach phase
			(val_mul, ":defender_strength", 125),
			(val_div, ":defender_strength", 100),
			
			(assign, reg0, ":attacker_strength"),
			(assign, reg1, ":defender_strength"),
		]),
	
	# script_party_groups_simulate_battle_charge
	# input:
	# 	arg1: attacker
	# 	arg2: defender
	# output:
	# 	reg0: attacker_strength
	# 	reg1: defender_strength
	("party_groups_simulate_battle_charge",
		[
			(store_script_param, ":attacker", 1),
			(store_script_param, ":defender", 2),
			
			(call_script, "script_party_group_calculate_strength_charge", ":attacker"),
			(assign, ":attacker_strength", reg0),
			# Defender does not benefit from charge bonus
			(call_script, "script_party_group_calculate_strength", ":defender"),
			(assign, ":defender_strength", reg0),
			
			(assign, reg0, ":attacker_strength"),
			(assign, reg1, ":defender_strength"),
		]),
	
	# script_party_groups_simulate_battle_melee
	# input:
	# 	arg1: attacker
	# 	arg2: defender
	# output:
	# 	reg0: attacker_strength
	# 	reg1: defender_strength
	("party_groups_simulate_battle_melee",
		[
			(store_script_param, ":attacker", 1),
			(store_script_param, ":defender", 2),
			
			(call_script, "script_party_group_calculate_strength", ":attacker"),
			(assign, ":attacker_strength", reg0),
			(call_script, "script_party_group_calculate_strength", ":defender"),
			(assign, ":defender_strength", reg0),
			
			(assign, reg0, ":attacker_strength"),
			(assign, reg1, ":defender_strength"),
		]),
	
	# script_party_group_calculate_strength
	# input:
	# 	arg1: party_group
	# output:
	# 	reg0: strength
	# 	reg1: defense
	("party_group_calculate_strength",
		[
			
			(store_script_param, ":party_no", 1),
			
			(assign, ":strength", 0),
			(assign, ":defense", 0),
			
			(party_get_num_companion_stacks, ":num_stacks", ":party_no"),
			(try_for_range, ":i_stack", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":troop_no", ":party_no", ":i_stack"),
				
				(party_stack_get_num_wounded, ":num_wounded", ":party_no", ":i_stack"),
				(party_stack_get_size, ":num_troops", ":party_no", ":i_stack"),
				(store_sub, ":num_ready", ":num_troops", ":num_wounded"),
				(gt, ":num_ready", 0),
				(store_random_in_range, ":rand", 0, 2),
				
				(call_script, "script_troop_calculate_strength", ":troop_no"),
				(assign, ":cur_strength", reg0),
				(assign, ":cur_defense", reg1),
				(assign, ":cur_ranged", reg2),
				(try_begin),
					(this_or_next|eq, ":rand", 0),
					(eq, ":cur_ranged", 0),
				(else_try),
					(assign, ":cur_strength", ":cur_ranged"),
				(try_end),
				
				(val_mul, ":cur_strength", ":num_ready"),
				(val_mul, ":cur_defense", ":num_ready"),
				
				(val_add, ":strength", ":cur_strength"),
				(val_add, ":defense", ":cur_defense"),
			(try_end),
			
			(party_get_num_attached_parties, ":num_attached", ":party_no"),
			(try_for_range, ":i", 0, ":num_attached"),
				(party_get_attached_party_with_rank, ":cur_party", ":party_no", ":i"),
				(call_script, "script_party_group_calculate_strength", ":cur_party"),
				(val_add, ":strength", reg0),
				(val_add, ":defense", reg1),
			(try_end),
			(assign, reg0, ":strength"),
			(assign, reg1, ":defense"),
		]),
	
	# script_party_group_calculate_strength_approach
	# input:
	# 	arg1: party_group
	# output:
	# 	reg0: strength
	# 	reg1: defense
	("party_group_calculate_strength_approach",
		[
			(store_script_param, ":party_no", 1),
			
			(assign, ":strength", 0),
			(assign, ":defense", 0),
			
			(party_get_num_companion_stacks, ":num_stacks", ":party_no"),
			(try_for_range, ":i_stack", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":troop_no", ":party_no", ":i_stack"),
				
				(party_stack_get_num_wounded, ":num_wounded", ":party_no", ":i_stack"),
				(party_stack_get_size, ":num_troops", ":party_no", ":i_stack"),
				(store_sub, ":num_ready", ":num_troops", ":num_wounded"),
				(gt, ":num_ready", 0),
				
				(call_script, "script_troop_calculate_strength", ":troop_no"),
				(assign, ":cur_strength", reg2), # We add ranged strength
				(assign, ":cur_defense", reg1),
				
				(val_mul, ":cur_strength", ":num_ready"),
				(val_mul, ":cur_defense", ":num_ready"),
				
				(val_add, ":strength", ":cur_strength"),
				(val_add, ":defense", ":cur_defense"),
			(try_end),
			
			(party_get_num_attached_parties, ":num_attached", ":party_no"),
			(try_for_range, ":i", 0, ":num_attached"),
				(party_get_attached_party_with_rank, ":cur_party", ":party_no", ":i"),
				(call_script, "script_party_group_calculate_strength_approach", ":cur_party"),
				(val_add, ":strength", reg0),
				(val_add, ":defense", reg1),
			(try_end),
			(assign, reg0, ":strength"),
			(assign, reg1, ":defense"),
		]),
	
	# script_party_group_calculate_strength_charge
	# input:
	# 	arg1: party_group
	# output:
	# 	reg0: strength
	# 	reg1: defense
	("party_group_calculate_strength_charge",
		[
			
			(store_script_param, ":party_no", 1),
			
			(assign, ":strength", 0),
			(assign, ":defense", 0),
			
			(party_get_num_companion_stacks, ":num_stacks", ":party_no"),
			(try_for_range, ":i_stack", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":troop_no", ":party_no", ":i_stack"),
				(party_stack_get_num_wounded, ":num_wounded", ":party_no", ":i_stack"),
				(party_stack_get_size, ":num_troops", ":party_no", ":i_stack"),
				(store_sub, ":num_ready", ":num_troops", ":num_wounded"),
				(gt, ":num_ready", 0),
				
				(troop_get_slot, ":type", ":troop_no", slot_troop_type),
				(call_script, "script_troop_calculate_strength", ":troop_no"),
				(assign, ":cur_strength", reg0),
				(assign, ":cur_defense", reg1),
				(assign, ":cur_ranged", reg2),
				
				(val_mul, ":cur_strength", ":num_ready"),
				(val_mul, ":cur_defense", ":num_ready"),
				(val_mul, ":cur_ranged", ":num_ready"),
				(try_begin),
					(this_or_next|eq, ":type", tt_shock_infantry),
					(eq, ":type", tt_spearman),
					(eq, ":type", tt_pikeman),
					(val_mul, ":cur_strength", 3),
					(val_div, ":cur_strength", 2),
					
					(val_add, ":strength", ":cur_strength"),
					(val_add, ":defense", ":cur_defense"),
				(else_try),
					(this_or_next|eq, ":type", tt_archer),
					(this_or_next|eq, ":type", tt_crossbow),
					(this_or_next|eq, ":type", tt_horse_archer),
					(val_add, ":strength", ":cur_ranged"),
					(val_add, ":defense", ":cur_defense"),
				(else_try),
					(eq, ":type", tt_lancer),
					(val_mul, ":cur_strength", 6),
					
					(val_add, ":strength", ":cur_strength"),
					(val_add, ":defense", ":cur_defense"),
				(else_try),
					(this_or_next|eq, ":type", tt_cavalry),
					(eq, ":type", tt_mounted_skirmisher),
					(val_mul, ":cur_strength", 2),
					
					(val_add, ":strength", ":cur_strength"),
					(val_add, ":defense", ":cur_defense"),
				(else_try),
					(val_add, ":strength", ":cur_strength"),
					(val_add, ":defense", ":cur_defense"),
				(try_end),
			(try_end),
			
			(party_get_num_attached_parties, ":num_attached", ":party_no"),
			(try_for_range, ":i", 0, ":num_attached"),
				(party_get_attached_party_with_rank, ":cur_party", ":party_no", ":i"),
				(call_script, "script_party_group_calculate_strength_charge", ":cur_party"),
				(val_add, ":strength", reg0),
				(val_add, ":defense", reg1),
			(try_end),
			(assign, reg0, ":strength"),
			(assign, reg1, ":defense"),
		]),
	
	# script_troop_calculate_strength
	# input:
	# 	arg1: troop
	# output:
	# 	reg0: strength
	# 	reg1: defense
	# 	reg2: ranged_strength
	("troop_calculate_strength",
		[
			(store_script_param, ":troop_no", 1),
			
			# (store_character_level, ":level", ":troop_no"),
			
			(troop_get_slot, ":type", ":troop_no", slot_troop_type),
			
			(store_skill_level, ":ironflesh", skl_ironflesh, ":troop_no"),
			(store_mul, ":defense", ":ironflesh", 2),
			
			(store_skill_level, ":ps", skl_power_strike, ":troop_no"),
			(val_mul, ":ps", 8),
			(store_attribute_level, ":str", ":troop_no", ca_strength),
			(store_div, ":strength", ":str", 2),
			(val_add, ":strength", ":ps"),
			
			(val_add, ":defense", ":str"),
			
			(troop_get_slot, ":armor_weight", ":troop_no", slot_troop_armor_weight),
			(troop_get_slot, ":weapon_weight", ":troop_no", slot_troop_ranged_weapon_weight),
			
			(val_mul, ":armor_weight", 3),
			(val_add, ":armor_weight", 2),
			(val_mul, ":defense", ":armor_weight"),
			(val_div, ":defense", 10),
			
			(assign, ":ranged_strength", 0),
			(try_begin),
				(ge, ":weapon_weight", 0),
				(store_mul, ":ranged_strength", ":weapon_weight", 12),
				(val_add, ":ranged_strength", 5),
				
				(assign, ":mult", 100),
				(try_begin),
					(this_or_next|eq, ":type", tt_archer),
					(eq, ":type", tt_horse_archer),
					(store_skill_level, ":pd", skl_power_draw, ":troop_no"),
					(val_mul, ":pd", 14),
					(val_add, ":mult", ":pd"),
				(else_try),
					(store_skill_level, ":pt", skl_power_throw, ":troop_no"),
					(val_mul, ":pt", 10),
					(val_add, ":mult", ":pt"),
				(try_end),
				(val_mul, ":ranged_strength", ":mult"),
				(val_div, ":ranged_strength", 100),
				
				(assign, ":p", 100),
				(try_begin),
					(eq, ":type", tt_archer),
					(store_proficiency_level, ":p", ":troop_no", wpt_archery),
				(else_try),
					(eq, ":type", tt_crossbow),
					(store_proficiency_level, ":p", ":troop_no", wpt_crossbow),
				(else_try),
					(eq, ":type", tt_horse_archer),
					(store_proficiency_level, ":p", ":troop_no", wpt_archery),
					(store_proficiency_level, ":c", ":troop_no", wpt_crossbow),
					(store_proficiency_level, ":t", ":troop_no", wpt_throwing),
					(val_max, ":p", ":c"),
					(val_max, ":p", ":t"),
				(else_try),
					(eq, ":type", tt_skirmisher),
					(store_proficiency_level, ":p", ":troop_no", wpt_throwing),
				(else_try),
					(eq, ":type", tt_mounted_skirmisher),
					(store_proficiency_level, ":p", ":troop_no", wpt_throwing),
				(else_try),
					(store_proficiency_level, ":p", ":troop_no", wpt_archery),
					(store_proficiency_level, ":c", ":troop_no", wpt_crossbow),
					(store_proficiency_level, ":t", ":troop_no", wpt_throwing),
					(val_max, ":p", ":c"),
					(val_max, ":p", ":t"),
				(try_end),
				(val_mul, ":ranged_strength", ":p"),
				(val_div, ":ranged_strength", 100),
			(try_end),
			
			(try_begin),
				(eq, ":type", tt_infantry),
				(val_mul, ":defense", 3),
				(val_div, ":defense", 2),
				
				(val_mul, ":strength", 4),
				(val_div, ":strength", 5),
			(else_try),
				(eq, ":type", tt_spearman),
				(val_mul, ":defense", 2),
				
				(val_mul, ":strength", 4),
				(val_div, ":strength", 5),
			(else_try),
				(eq, ":type", tt_pikeman),
				(val_mul, ":defense", 3),
				(val_div, ":defense", 2),
			(else_try),
				(eq, ":type", tt_shock_infantry),
				(val_mul, ":defense", 2),
				(val_div, ":defense", 3),
			(else_try),
				(eq, ":type", tt_archer),
				(val_div, ":defense", 2),
				(val_div, ":strength", 2),
			(else_try),
				(eq, ":type", tt_crossbow),
				(val_mul, ":defense", 2),
				(val_div, ":defense", 3),
				(val_mul, ":strength", 2),
				(val_div, ":strength", 3),
			(else_try),
				(eq, ":type", tt_horse_archer),
				(val_mul, ":strength", 9),
				(val_div, ":strength", 10),
				(val_div, ":defense", 2),
			(else_try),
				(eq, ":type", tt_lancer),
				(val_div, ":strength", 2),
				(val_mul, ":defense", 4),
				(val_div, ":defense", 5),
			(else_try),
				(this_or_next|eq, ":type", tt_cavalry),
				(eq, ":type", tt_mounted_skirmisher),
				(val_mul, ":strength", 9),
				(val_div, ":strength", 10),
				(val_mul, ":defense", 4),
				(val_div, ":defense", 5),
			(try_end),
			
			(assign, reg0, ":strength"),
			(assign, reg1, ":defense"),
			(assign, reg2, ":ranged_strength"),
		]),
	
	
	# script_party_group_defeat_party_group
	# input:
	# 	arg1: winner_party
	# 	arg2: defeated_party
	# output: none
	("party_group_defeat_party_group",
		[
			(store_script_param, ":winner_party", 1),
			(store_script_param, ":defeated_party", 2),
			
			(party_get_slot, ":party_type", ":defeated_party", slot_party_type),
			
			(call_script, "script_party_group_take_party_group_prisoner", ":winner_party", ":defeated_party"),
			(call_script, "script_party_group_defeated", ":defeated_party"),
			(call_script, "script_clear_party_group", ":defeated_party"),
			
			(party_set_slot, ":winner_party", slot_party_battle_stage, bs_approach),
			
			(try_begin),
				(is_between, ":party_type", spt_village, spt_fort + 1),
				# (call_script, "script_troop_get_home", ":leader", 1),
				# (assign, ":home", reg0),
				# (call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_party, ":home"),
				(party_get_slot, ":leader", ":winner_party", slot_party_leader),
				(troop_set_slot, ":leader", slot_troop_mission, -1),
				(call_script, "script_party_process_mission", ":winner_party"),
			(try_end),
		]),
	
	# script_party_group_defeated
	# input:
	# 	arg1: defeated_party
	# output: none
	("party_group_defeated",
		[
			(store_script_param, ":defeated_party", 1),
			
			(try_begin),
				(party_slot_eq, ":defeated_party", slot_party_type, spt_war_party),
				(party_get_slot, ":leader", ":defeated_party", slot_party_leader),
				(troop_set_slot, ":leader", slot_troop_leaded_party, -1),
				
				###
				(str_store_troop_name, s10, ":leader"),
				(display_message, "@{s10} has been defeated in battle."),
				###
			(try_end),
			
			(party_get_num_attached_parties, ":num_attached_parties", ":defeated_party"),
			(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
				(party_get_attached_party_with_rank, ":attached_party", ":defeated_party", ":attached_party_rank"),
				(call_script, "script_party_group_defeated", ":attached_party"),
			(try_end),
		]),
	
	# script_party_group_take_party_group_prisoner
	# input:
	# 	arg1: party_group_no
	# 	arg2: prisoner_party
	# output: none
	("party_group_take_party_group_prisoner",
		[
			# (store_script_param, ":party_group_no", 1),
			# (store_script_param, ":prisoner_party", 2),
			
			# (distribute_party_among_party_group, ":prisoner_party", ":party_group_no"),
			
			# (party_get_num_attached_parties, ":num_attached_parties", ":prisoner_party"),
			# (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
				# (party_get_attached_party_with_rank, ":attached_party", ":prisoner_party", ":attached_party_rank"),
				# (call_script, "script_party_group_take_party_group_prisoner", ":attached_party"),
			# (try_end),
		]),

	#script_game_event_battle_end:
	# This script is called whenever the game ends the battle between two parties on the map.
	# INPUT:
	# param1: Defender Party
	# param2: Attacker Party
	("game_event_battle_end",
		[
		]), 

	#script_game_get_item_buy_price_factor:
	# This script is called from the game engine for calculating the buying price of any item.
	# INPUT:
	# param1: item_kind_id
	# OUTPUT:
	# trigger_result and reg0 = price_factor
	("game_get_item_buy_price_factor",
		[
		]),
  
	#script_game_get_item_sell_price_factor:
	# This script is called from the game engine for calculating the selling price of any item.
	# INPUT:
	# param1: item_kind_id
	# OUTPUT:
	# trigger_result and reg0 = price_factor
	("game_get_item_sell_price_factor",
		[
		]),
  
	#script_game_event_buy_item:
	# This script is called from the game engine when player buys an item.
	# INPUT:
	# param1: item_kind_id
	("game_event_buy_item",
		[
		]),
  
	#script_game_event_sell_item:
	# This script is called from the game engine when player sells an item.
	# INPUT:
	# param1: item_kind_id
	("game_event_sell_item",
		[
		]),	
  
	# script_game_get_troop_wage
	# This script is called from the game engine for calculating troop wages.
	# Input:
	# param1: troop_id, param2: party-id
	# Output: reg0: weekly wage
	("game_get_troop_wage",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":party_no", 2),
			
			(store_character_level, ":troop_level", ":troop_no"),
			
			(store_add, ":divider", ":troop_level", 60),
			(val_add, ":troop_level", 8),
			(val_mul, ":troop_level", 2),
			(val_mul, ":troop_level", ":troop_level"),
			
			(val_div, ":troop_level", ":divider"),
			
			(try_begin), # Mercenaries are 50% more expensive to maintain
				(is_between, ":troop_no", mercenaries_begin, mercenaries_end),
				(val_mul, ":troop_level", 3),
				(val_div, ":troop_level", 2),
			(try_end),
			(try_begin), # Mounted units are 25% more expensive to maintain
				(troop_is_mounted, ":troop_no"),
				(val_mul, ":troop_level", 5),
				(val_div, ":troop_level", 4),
			(try_end),
			
			(party_get_slot, ":party_leader", ":party_no", slot_party_leader),
			(try_begin), # 5% less per leadership point
				(ge, ":party_leader", 0),
				(store_skill_level, ":leadership", skl_leadership, ":party_leader"),
				(val_add, ":leadership", 20),
				(val_mul, ":troop_level", 20),
				(val_div, ":troop_level", ":leadership"),
			(try_end),
			
			(assign, reg0, ":troop_level"),
			(set_trigger_result, reg0),
		]),

	# script_game_get_total_wage
	# This script is called from the game engine for calculating total wage of the player party which is shown at the party window.
	# Input: none
	# Output: 
	# 	reg0: weekly wage
	("game_get_total_wage",
		[
			(assign, ":total_cost", 0),
			
			(party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
			
			(try_for_range, ":cur_stack", 1, ":num_stacks"),
				(party_stack_get_troop_id, ":troop_id", "p_main_party", ":cur_stack"),
				(party_stack_get_size, ":num_troops", "p_main_party", ":cur_stack"),
				(call_script, "script_game_get_troop_wage", ":troop_id", "p_main_party"),
				(store_mul, ":stack_cost", ":num_troops", reg0),
				(val_add, ":total_cost", ":stack_cost"),
			(try_end),
			
			(assign, reg0, ":total_cost"),
			(set_trigger_result, reg0),
		]),
  
	# script_game_get_join_cost
	# This script is called from the game engine for calculating troop join cost.
	# Input:
	# param1: troop_id,
	# Output: reg0: join cost
	("game_get_join_cost",
		[
			(store_script_param, ":troop_no", 1),
			
			(call_script, "script_troop_get_cost", ":troop_no"),
			(assign, ":join_cost", reg0),
			
			(try_begin),
				(is_between, ":troop_no", mercenaries_begin, mercenaries_end),
				(val_mul, ":join_cost", 3),
				(val_div, ":join_cost", 2),
			(try_end),
			
			(assign, reg0, ":join_cost"),
			(set_trigger_result, reg0),
		]),
  
	# script_game_get_upgrade_xp
	# This script is called from game engine for calculating needed troop upgrade exp
	# Input:
	# param1: troop_id,
	# Output: reg0 = needed exp for upgrade 
	("game_get_upgrade_xp",
		[
		]),
  
	# script_game_get_upgrade_cost
	# This script is called from game engine for calculating needed troop upgrade exp
	# Input:
	# param1: troop_id,
	# Output: reg0 = needed cost for upgrade
	("game_get_upgrade_cost",
		[
		]),

	# script_game_get_prisoner_price
	# This script is called from the game engine for calculating prisoner price
	# Input:
	# param1: troop_id,
	# Output: reg0  
	("game_get_prisoner_price",
		[
		]),


	# script_game_check_prisoner_can_be_sold
	# This script is called from the game engine for checking if a given troop can be sold.
	# Input: 
	# param1: troop_id,
	# Output: reg0: 1= can be sold; 0= cannot be sold.
	("game_check_prisoner_can_be_sold",
		[
		]),
  
	# script_game_get_morale_of_troops_from_faction
	# This script is called from the game engine 
	# Input: 
	# param1: faction_no,
	# Output: reg0: extra morale x 100
	("game_get_morale_of_troops_from_faction",
		[
		]),
  
	#script_game_event_detect_party:
	# This script is called from the game engine when player party inspects another party.
	# INPUT:
	# param1: Party-id
	("game_event_detect_party",
		[
		]),

	#script_game_event_undetect_party:
	# This script is called from the game engine when player party inspects another party.
	# INPUT:
	# param1: Party-id
	("game_event_undetect_party",
		[
		]),

	#script_game_get_statistics_line:
	# This script is called from the game engine when statistics page is opened.
	# INPUT:
	# param1: line_no
	("game_get_statistics_line",
		[
			(store_script_param_1, ":line_no"),
			(try_begin),
				(eq, ":line_no", 0),
				(get_player_agent_kill_count, reg1),
				(str_store_string, s1, "str_number_of_troops_killed_reg1"),
				(set_result_string, s1),
			(else_try),
				(eq, ":line_no", 1),
				(get_player_agent_kill_count, reg1, 1),
				(str_store_string, s1, "str_number_of_troops_wounded_reg1"),
				(set_result_string, s1),
			(else_try),
				(eq, ":line_no", 2),
				(get_player_agent_own_troop_kill_count, reg1),
				(str_store_string, s1, "str_number_of_own_troops_killed_reg1"),
				(set_result_string, s1),
			(else_try),
				(eq, ":line_no", 3),
				(get_player_agent_own_troop_kill_count, reg1, 1),
				(str_store_string, s1, "str_number_of_own_troops_wounded_reg1"),
				(set_result_string, s1),
			(try_end),
		]),

	#script_game_get_date_text:
	# This script is called from the game engine when the date needs to be displayed.
	# INPUT: arg1 = number of days passed since the beginning of the game
	# OUTPUT: result string = date
	("game_get_date_text",
		[
			(store_script_param_2, ":num_hours"),
			
			(store_div, ":num_days", ":num_hours", 24),
			(store_add, ":cur_day", ":num_days", 23),
			(assign, ":cur_month", 1),
			(assign, ":cur_year", 533),
			(assign, ":try_range", 99999),
			(try_for_range, ":unused", 0, ":try_range"),
				(try_begin),
					(this_or_next|eq, ":cur_month", 1),
					(this_or_next|eq, ":cur_month", 3),
					(this_or_next|eq, ":cur_month", 5),
					(this_or_next|eq, ":cur_month", 7),
					(this_or_next|eq, ":cur_month", 8),
					(this_or_next|eq, ":cur_month", 10),
					(eq, ":cur_month", 12),
					(assign, ":month_day_limit", 31),
				(else_try),
					(this_or_next|eq, ":cur_month", 4),
					(this_or_next|eq, ":cur_month", 6),
					(this_or_next|eq, ":cur_month", 9),
					(eq, ":cur_month", 11),
					(assign, ":month_day_limit", 30),
				(else_try),
					(try_begin),
						(store_div, ":cur_year_div_4", ":cur_year", 4),
						(val_mul, ":cur_year_div_4", 4),
						(eq, ":cur_year_div_4", ":cur_year"),
						(assign, ":month_day_limit", 29),
					(else_try),
						(assign, ":month_day_limit", 28),      
					(try_end),
				(try_end),
				(try_begin),
					(gt, ":cur_day", ":month_day_limit"),
					(val_sub, ":cur_day", ":month_day_limit"),
					(val_add, ":cur_month", 1),
					(try_begin),
						(gt, ":cur_month", 12),
						(val_sub, ":cur_month", 12),
						(val_add, ":cur_year", 1),
					(try_end),
				(else_try),
					(assign, ":try_range", 0),
				(try_end),
			(try_end),
			(assign, reg1, ":cur_day"),
			(assign, reg2, ":cur_year"),
			(try_begin),
				(eq, ":cur_month", 1),
				(str_store_string, s1, "str_january_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 2),
				(str_store_string, s1, "str_february_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 3),
				(str_store_string, s1, "str_march_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 4),
				(str_store_string, s1, "str_april_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 5),
				(str_store_string, s1, "str_may_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 6),
				(str_store_string, s1, "str_june_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 7),
				(str_store_string, s1, "str_july_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 8),
				(str_store_string, s1, "str_august_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 9),
				(str_store_string, s1, "str_september_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 10),
				(str_store_string, s1, "str_october_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 11),
				(str_store_string, s1, "str_november_reg1_reg2"),
			(else_try),
				(eq, ":cur_month", 12),
				(str_store_string, s1, "str_december_reg1_reg2"),
			(try_end),
			(set_result_string, s1),
		]),
  
	#script_game_get_money_text:
	# This script is called from the game engine when an amount of money needs to be displayed.
	# INPUT: arg1 = amount in units
	# OUTPUT: result string = money in text
	("game_get_money_text",
		[
			(store_script_param, ":amount", 1),
			(str_clear, s0),
			
			(try_begin),
				(eq, ":amount", 1),
				(str_store_string, s0, "str_1_denar"),
			(else_try),
				(assign, reg1, ":amount"),
				(str_store_string, s0, "str_reg1_denars"),
			(try_end),
			
			(set_result_string, s0),
		]),

	# script_game_get_party_companion_limit:
	# This script is called from the game engine when the companion limit is needed for a party.
	# INPUT: arg1 = none
	# OUTPUT: reg0 = companion_limit
	("game_get_party_companion_limit",
		[
			(call_script, "script_party_get_companion_limit", "p_main_party"),
			(set_trigger_result, reg0),
		]),


	#script_game_reset_player_party_name:
	# This script is called from the game engine when the player name is changed.
	# INPUT: none
	# OUTPUT: none
	("game_reset_player_party_name",
		[
			# (str_store_troop_name, s10, "trp_player"),
			# (troop_set_plural_name, "trp_player", s10),
			# (call_script, "script_troop_update_rank", "trp_player"),
			# (call_script, "script_troop_update_name", "trp_player"),
		]),

	#script_game_get_troop_note
	# This script is called from the game engine when the notes of a troop is needed.
	# INPUT: arg1 = troop_no, arg2 = note_index
	# OUTPUT: s0 = note
	("game_get_troop_note",
		[
		]),
  
	#script_game_get_center_note
	# This script is called from the game engine when the notes of a center is needed.
	# INPUT: arg1 = center_no, arg2 = note_index
	# OUTPUT: s0 = note
	("game_get_center_note",
		[
		]),

	#script_game_get_faction_note
	# This script is called from the game engine when the notes of a faction is needed.
	# INPUT: arg1 = faction_no, arg2 = note_index
	# OUTPUT: s0 = note
	("game_get_faction_note",
		[
		]),

	#script_game_get_quest_note
	# This script is called from the game engine when the notes of a quest is needed.
	# INPUT: arg1 = quest_no, arg2 = note_index
	# OUTPUT: s0 = note
	("game_get_quest_note",
		[
		]),

	#script_game_get_info_page_note
	# This script is called from the game engine when the notes of a info_page is needed.
	# INPUT: arg1 = info_page_no, arg2 = note_index
	# OUTPUT: s0 = note
	("game_get_info_page_note",
		[
		]),

	#script_game_get_scene_name
	# This script is called from the game engine when a name for the scene is needed.
	# INPUT: arg1 = scene_no
	# OUTPUT: s0 = name
	("game_get_scene_name",
		[
		]),
  
	#script_game_get_mission_template_name
	# This script is called from the game engine when a name for the mission template is needed.
	# INPUT: arg1 = mission_template_no
	# OUTPUT: s0 = name
	("game_get_mission_template_name",
		[
		]),

	#script_game_receive_url_response
	#response format should be like this:
	#  [a number or a string]|[another number or a string]|[yet another number or a string] ...
	# here is an example response:
	# 12|Player|100|another string|142|323542|34454|yet another string
	# INPUT: arg1 = num_integers, arg2 = num_strings
	# reg0, reg1, reg2, ... up to 128 registers contain the integer values
	# s0, s1, s2, ... up to 128 strings contain the string values
	("game_receive_url_response",
		[
		]),
      
	("game_get_cheat_mode",
		[
		]),    
  
	#script_game_receive_network_message
	# This script is called from the game engine when a new network message is received.
	# INPUT: arg1 = player_no, arg2 = event_type, arg3 = value, arg4 = value_2, arg5 = value_3, arg6 = value_4
	("game_receive_network_message",
		[
		]),

	# script_game_get_multiplayer_server_option_for_mission_template
	# Input: arg1 = mission_template_id, arg2 = option_index
	# Output: trigger_result = 1 for option available, 0 for not available
	# reg0 = option_value
	("game_get_multiplayer_server_option_for_mission_template",
		[
		]),

	# script_game_multiplayer_server_option_for_mission_template_to_string
	# Input: arg1 = mission_template_id, arg2 = option_index, arg3 = option_value
	# Output: s0 = option_text
	("game_multiplayer_server_option_for_mission_template_to_string",
		[
		]),

	# script_game_multiplayer_event_duel_offered
	# Input: arg1 = agent_no
	# Output: none
	("game_multiplayer_event_duel_offered",
		[
		]),
	 
	# script_game_get_multiplayer_game_type_enum
	# Input: none
	# Output: reg0:first type, reg1:type count
	("game_get_multiplayer_game_type_enum",
		[
		]),

	# script_game_multiplayer_get_game_type_mission_template
	# Input: arg1 = game_type
	# Output: mission_template 
	("game_multiplayer_get_game_type_mission_template",
		[
		]),

	#script_game_get_party_prisoner_limit:
	# This script is called from the game engine when the prisoner limit is needed for a party.
	# INPUT: arg1 = party_no
	# OUTPUT: reg0 = prisoner_limit
	("game_get_party_prisoner_limit",
		[
		]),

	#script_game_get_item_extra_text:
	# This script is called from the game engine when an item's properties are displayed.
	# INPUT: arg1 = item_no, arg2 = extra_text_id (this can be between 0-7 (7 included)), arg3 = item_modifier
	# OUTPUT: result_string = item extra text, trigger_result = text color (0 for default)
	("game_get_item_extra_text",
		[
			(store_script_param, ":item_no", 1),
			(store_script_param, ":extra_text_id", 2),
			# (store_script_param, ":item_modifier", 3),
			
			(try_begin),
				(this_or_next|eq, ":item_no", "itm_javelin"),
				(this_or_next|eq, ":item_no", "itm_jarid"),
				(eq, ":item_no", "itm_throwing_spears"),
				(eq, ":extra_text_id", 0),
				(set_result_string, "@Bonus against armor"),
				(set_trigger_result, 0xFFF022),
			(try_end),
		]),

	#script_game_on_disembark:
	# This script is called from the game engine when the player reaches the shore with a ship.
	# INPUT: pos0 = disembark position
	# OUTPUT: none
	("game_on_disembark",
		[
		]),


	#script_game_context_menu_get_buttons:
	# This script is called from the game engine when the player clicks the right mouse button over a party on the map.
	# INPUT: arg1 = party_no
	# OUTPUT: none, fills the menu buttons
	("game_context_menu_get_buttons",
		[
		]),

	#script_game_event_context_menu_button_clicked:
	# This script is called from the game engine when the player clicks on a button at the right mouse menu.
	# INPUT: arg1 = party_no, arg2 = button_value
	# OUTPUT: none
	("game_event_context_menu_button_clicked",
		[
		]),

	#script_game_get_skill_modifier_for_troop
	# This script is called from the game engine when a skill's modifiers are needed
	# INPUT: arg1 = troop_no, arg2 = skill_no
	# OUTPUT: trigger_result = modifier_value
	("game_get_skill_modifier_for_troop",
		[
		]),
  
	# script_game_check_party_sees_party
	# This script is called from the game engine when a party is inside the range of another party
	# input: arg1 = party_no_seer, arg2 = party_no_seen
	# output: trigger_result = true or false (1 = true, 0 = false)
	("game_check_party_sees_party",
		[
			(store_script_param, ":party_no_seer", 1),
			(store_script_param, ":party_no_seen", 2),
			
			(try_begin),
				(eq, ":party_no_seer", "p_main_party"),
				(party_get_slot, ":party_type", ":party_no_seen", slot_party_type),
				(is_between, ":party_type", spt_village, spt_fort + 1),
				(party_set_flags, ":party_no_seen", pf_always_visible, 1),
			(try_end),
			(set_trigger_result, 1),
		]),
##
##  #script_game_get_party_speed_multiplier
##  # This script is called from the game engine when a skill's modifiers are needed
##  # INPUT: arg1 = party_no
##  # OUTPUT: trigger_result = multiplier (scaled by 100, meaning that giving 100 as the trigger result does not change the party speed)
##  ("game_get_party_speed_multiplier",
##   [
##     (store_script_param, ":party_no", 1),
##     (set_trigger_result, 100),
##    ]),

	#script_game_get_console_command
	# This script is called from the game engine when a console command is entered from the dedicated server.
	# INPUT: anything
	# OUTPUT: s0 = result text
	("game_get_console_command",
		[
		]),
	
	# script_clear_party_group:
	# input:
	# 	arg1: Party-id of the root of the group.
	# This script will clear the root party and all parties attached to it recursively.
	("clear_party_group",
		[
			(store_script_param_1, ":root_party"),
		
			(party_clear, ":root_party"),
			(party_get_num_attached_parties, ":num_attached_parties", ":root_party"),
			(try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
				(party_get_attached_party_with_rank, ":attached_party", ":root_party", ":attached_party_rank"),
				(call_script, "script_clear_party_group", ":attached_party"),
			(try_end),
		]),
	
	#script_add_troop_to_cur_tableau
	# INPUT: troop_no
	# OUTPUT: none
	("add_troop_to_cur_tableau",
		[
			(store_script_param, ":troop_no",1),

			(set_fixed_point_multiplier, 100),
			(assign, ":banner_mesh", -1),
			# (troop_get_slot, ":banner_spr", ":troop_no", slot_troop_banner_scene_prop),
			# (store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
			# (try_begin),
				# (is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
				# (val_sub, ":banner_spr", banner_scene_props_begin),
				# (store_add, ":banner_mesh", ":banner_spr", banner_meshes_begin),
			# (try_end),

			(cur_tableau_clear_override_items),
		   
			(cur_tableau_set_override_flags, af_override_fullhelm),
			(cur_tableau_set_override_flags, af_override_head|af_override_weapons),
		   
			(init_position, pos2),
			(cur_tableau_set_camera_parameters, 1, 6, 6, 10, 10000),

			(init_position, pos5),
			(assign, ":eye_height", 162),
			(store_mul, ":camera_distance", ":troop_no", 87323),
			# (val_mod, ":camera_distance", 5),
			(assign, ":camera_distance", 139),
			(store_mul, ":camera_yaw", ":troop_no", 124337),
			(val_mod, ":camera_yaw", 50),
			(val_add, ":camera_yaw", -25),
			(store_mul, ":camera_pitch", ":troop_no", 98123),
			(val_mod, ":camera_pitch", 20),
			(val_add, ":camera_pitch", -14),
			(assign, ":animation", "anim_stand_man"),
		   
	##       (troop_get_inventory_slot, ":horse_item", ":troop_no", ek_horse),
	##       (try_begin),
	##         (gt, ":horse_item", 0),
	##         (assign, ":eye_height", 210),
	##         (cur_tableau_add_horse, ":horse_item", pos2, anim_horse_stand, 0),
	##         (assign, ":animation", anim_ride_0),
	##         (position_set_z, pos5, 125),
	##         (try_begin),
	##           (is_between, ":camera_yaw", -10, 10), #make sure horse head doesn't obstruct face.
	##           (val_min, ":camera_pitch", -5),
	##         (try_end),
	##       (try_end),
			(position_set_z, pos5, ":eye_height"),
	
			# camera looks towards -z axis
			(position_rotate_x, pos5, -90),
			(position_rotate_z, pos5, 180),
	
			# now apply yaw and pitch
			(position_rotate_y, pos5, ":camera_yaw"),
			(position_rotate_x, pos5, ":camera_pitch"),
			(position_move_z, pos5, ":camera_distance", 0),
			(position_move_x, pos5, 5, 0),
	
			(try_begin),
				(ge, ":banner_mesh", 0),
	
				(init_position, pos1),
				(position_set_z, pos1, -1500),
				(position_set_x, pos1, 265),
				(position_set_y, pos1, 400),
				(position_transform_position_to_parent, pos3, pos5, pos1),
				(cur_tableau_add_mesh, ":banner_mesh", pos3, 400, 0),
			(try_end),
			(cur_tableau_add_troop, ":troop_no", pos2, ":animation" , 0),
	
			(cur_tableau_set_camera_position, pos5),
	
			(copy_position, pos8, pos5),
			(position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
			(position_rotate_z, pos8, 30), 
			(position_rotate_x, pos8, -60), 
			(cur_tableau_add_sun_light, pos8, 175,150,125),
		]),

	#script_add_troop_to_cur_tableau_for_character
	# INPUT: troop_no
	# OUTPUT: none
	("add_troop_to_cur_tableau_for_character",
		[
			(store_script_param, ":troop_no",1),
	
			(set_fixed_point_multiplier, 100),
	
			(cur_tableau_clear_override_items),
			(cur_tableau_set_override_flags, af_override_fullhelm),
	##    	   (cur_tableau_set_override_flags, af_override_head|af_override_weapons),
			
			(init_position, pos2),
			(cur_tableau_set_camera_parameters, 1, 4, 8, 10, 10000),
	
			(init_position, pos5),
			(assign, ":cam_height", 150),
	#     	  (val_mod, ":camera_distance", 5),
			(assign, ":camera_distance", 360),
			(assign, ":camera_yaw", -15),
			(assign, ":camera_pitch", -18),
			(assign, ":animation", anim_stand_man),
			
			(position_set_z, pos5, ":cam_height"),
	
			# camera looks towards -z axis
			(position_rotate_x, pos5, -90),
			(position_rotate_z, pos5, 180),
	
			# now apply yaw and pitch
			(position_rotate_y, pos5, ":camera_yaw"),
			(position_rotate_x, pos5, ":camera_pitch"),
			(position_move_z, pos5, ":camera_distance", 0),
			(position_move_x, pos5, 5, 0),
	
			(try_begin),
				(troop_is_hero, ":troop_no"),
				(cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
			(else_try),
				(store_mul, ":random_seed", ":troop_no", 126233),
				(val_mod, ":random_seed", 1000),
				(val_add, ":random_seed", 1),
				(cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
			(try_end),
			(cur_tableau_set_camera_position, pos5),
	
			(copy_position, pos8, pos5),
			(position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
			(position_rotate_z, pos8, 30), 
			(position_rotate_x, pos8, -60), 
			(cur_tableau_add_sun_light, pos8, 175,150,125),
		]),

	#script_add_troop_to_cur_tableau_for_inventory
	# INPUT: troop_no
	# OUTPUT: none
	("add_troop_to_cur_tableau_for_inventory",
		[
			(store_script_param, ":troop_no",1),
			(store_mod, ":side", ":troop_no", 4), #side flag is inside troop_no value
			(val_div, ":troop_no", 4), #removing the flag bit
			(val_mul, ":side", 90), #to degrees
	
			(set_fixed_point_multiplier, 100),
	
			(cur_tableau_clear_override_items),
			
			(init_position, pos2),
			(position_rotate_z, pos2, ":side"),
			(cur_tableau_set_camera_parameters, 1, 4, 6, 10, 10000),
	
			(init_position, pos5),
			(assign, ":cam_height", 105),
	#     	  (val_mod, ":camera_distance", 5),
			(assign, ":camera_distance", 380),
			(assign, ":camera_yaw", -15),
			(assign, ":camera_pitch", -18),
			(assign, ":animation", anim_stand_man),
			
			(position_set_z, pos5, ":cam_height"),
	
			# camera looks towards -z axis
			(position_rotate_x, pos5, -90),
			(position_rotate_z, pos5, 180),
	
			# now apply yaw and pitch
			(position_rotate_y, pos5, ":camera_yaw"),
			(position_rotate_x, pos5, ":camera_pitch"),
			(position_move_z, pos5, ":camera_distance", 0),
			(position_move_x, pos5, 5, 0),
	
			(try_begin),
				(troop_is_hero, ":troop_no"),
				(cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
			(else_try),
				(store_mul, ":random_seed", ":troop_no", 126233),
				(val_mod, ":random_seed", 1000),
				(val_add, ":random_seed", 1),
				(cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
			(try_end),
			(cur_tableau_set_camera_position, pos5),
	
			(copy_position, pos8, pos5),
			(position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
			(position_rotate_z, pos8, 30), 
			(position_rotate_x, pos8, -60), 
			(cur_tableau_add_sun_light, pos8, 175,150,125),
		]),

	#script_add_troop_to_cur_tableau_for_profile
	# INPUT: troop_no
	# OUTPUT: none
	("add_troop_to_cur_tableau_for_profile",
		[
			(store_script_param, ":troop_no",1),
	
			(set_fixed_point_multiplier, 100),
	
			(cur_tableau_clear_override_items),
			
			(cur_tableau_set_camera_parameters, 1, 4, 6, 10, 10000),
	
			(init_position, pos5),
			(assign, ":cam_height", 105),
	#     	  (val_mod, ":camera_distance", 5),
			(assign, ":camera_distance", 380),
			(assign, ":camera_yaw", -15),
			(assign, ":camera_pitch", -18),
			(assign, ":animation", anim_stand_man),
			
			(position_set_z, pos5, ":cam_height"),
	
			# camera looks towards -z axis
			(position_rotate_x, pos5, -90),
			(position_rotate_z, pos5, 180),
	
			# now apply yaw and pitch
			(position_rotate_y, pos5, ":camera_yaw"),
			(position_rotate_x, pos5, ":camera_pitch"),
			(position_move_z, pos5, ":camera_distance", 0),
			(position_move_x, pos5, 5, 0),
	
			# (profile_get_banner_id, ":profile_banner"),
			# (try_begin),
				# (ge, ":profile_banner", 0),
				# (init_position, pos2),
				# (val_add, ":profile_banner", banner_meshes_begin),
				# (position_set_x, pos2, -175),
				# (position_set_y, pos2, -300),
				# (position_set_z, pos2, 180),
				# (position_rotate_x, pos2, 90),
				# (position_rotate_y, pos2, -15),
				# (cur_tableau_add_mesh, ":profile_banner", pos2, 0, 0),
			# (try_end),

			(init_position, pos2),
			(try_begin),
				(troop_is_hero, ":troop_no"),
				(cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
			(else_try),
				(store_mul, ":random_seed", ":troop_no", 126233),
				(val_mod, ":random_seed", 1000),
				(val_add, ":random_seed", 1),
				(cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
			(try_end),
			(cur_tableau_set_camera_position, pos5),

			(copy_position, pos8, pos5),
			(position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
			(position_rotate_z, pos8, 30), 
			(position_rotate_x, pos8, -60), 
			(cur_tableau_add_sun_light, pos8, 175,150,125),
		]),

	#script_add_troop_to_cur_tableau_for_retirement
	# INPUT: type
	# OUTPUT: none
	("add_troop_to_cur_tableau_for_retirement", 
		[
			(store_script_param, ":type", 1),
			(cur_tableau_set_override_flags, af_override_everything),

			(try_begin),
				(eq, ":type", 0),
				# (cur_tableau_add_override_item, "itm_pilgrim_hood"),
				# (cur_tableau_add_override_item, "itm_pilgrim_disguise"),
				# (cur_tableau_add_override_item, "itm_wrapping_boots"),
				(assign, ":animation", "anim_pose_1"),
			(else_try),
				(eq, ":type", 1),
				# (cur_tableau_add_override_item, "itm_pilgrim_hood"),
				# (cur_tableau_add_override_item, "itm_red_tunic"),
				# (cur_tableau_add_override_item, "itm_wrapping_boots"),
				# (cur_tableau_add_override_item, "itm_dagger"),
				(assign, ":animation", "anim_pose_1"),
			(else_try),
				(eq, ":type", 2),
				# (cur_tableau_add_override_item, "itm_linen_tunic"),
				# (cur_tableau_add_override_item, "itm_wrapping_boots"),
				(assign, ":animation", "anim_pose_2"),
			(else_try),
				(eq, ":type", 3),
				# (cur_tableau_add_override_item, "itm_nomad_vest"),
				# (cur_tableau_add_override_item, "itm_nomad_boots"),
				(assign, ":animation", "anim_pose_2"),
			(else_try),
				(eq, ":type", 4),
				# (cur_tableau_add_override_item, "itm_leather_apron"),
				# (cur_tableau_add_override_item, "itm_leather_boots"),
				(assign, ":animation", "anim_pose_3"),
			(else_try),
				(eq, ":type", 5),
				# (cur_tableau_add_override_item, "itm_red_shirt"),
				# (cur_tableau_add_override_item, "itm_woolen_hose"),
				# (cur_tableau_add_override_item, "itm_fur_hat"),
				(assign, ":animation", "anim_pose_3"),
			(else_try),
				(eq, ":type", 6),
				# (cur_tableau_add_override_item, "itm_red_gambeson"),
				# (cur_tableau_add_override_item, "itm_leather_boots"),
				# (cur_tableau_add_override_item, "itm_sword_medieval_c"),
				(assign, ":animation", "anim_pose_4"),
			(else_try),
				(eq, ":type", 7),
				# (cur_tableau_add_override_item, "itm_nobleman_outfit"),
				# (cur_tableau_add_override_item, "itm_blue_hose"),
				# (cur_tableau_add_override_item, "itm_sword_medieval_c"),
				(assign, ":animation", "anim_pose_4"),
			(else_try),
				(eq, ":type", 8),
				# (cur_tableau_add_override_item, "itm_courtly_outfit"),
				# (cur_tableau_add_override_item, "itm_woolen_hose"),
				# (cur_tableau_add_override_item, "itm_sword_medieval_c"),
				(assign, ":animation", "anim_pose_4"),
			(else_try),
				# (eq, ":type", 9),
				# (cur_tableau_add_override_item, "itm_heraldic_mail_with_surcoat_for_tableau"),
				# (cur_tableau_add_override_item, "itm_mail_boots_for_tableau"),
				# (cur_tableau_add_override_item, "itm_sword_medieval_c"),
				(assign, ":animation", "anim_pose_5"),
		##    	(else_try), #not used
		##    	  (cur_tableau_add_override_item, "itm_heraldic_mail_with_tabard"),
		##    	  (cur_tableau_add_override_item, "itm_iron_greaves"),
		##    	  (cur_tableau_add_override_item, "itm_sword_medieval_c"),
		##    	  (assign, ":animation", "anim_pose_5"),
			(try_end),

		##    (set_fixed_point_multiplier, 100),
		##    (cur_tableau_set_background_color, 0x00000000),
		##    (cur_tableau_set_ambient_light, 10,11,15),

		##     (init_position, pos8),
		##     (position_set_x, pos8, -210),
		##     (position_set_y, pos8, 200),
		##     (position_set_z, pos8, 300),
		##     (cur_tableau_add_point_light, pos8, 550,500,450),


			(set_fixed_point_multiplier, 100),
			(cur_tableau_set_camera_parameters, 1, 6, 6, 10, 10000),
			(assign, ":cam_height", 155),
			(assign, ":camera_distance", 575),
			(assign, ":camera_yaw", -5),
			(assign, ":camera_pitch", 10),

			(init_position, pos5),
			(position_set_z, pos5, ":cam_height"),
			# camera looks towards -z axis
			(position_rotate_x, pos5, -90),
			(position_rotate_z, pos5, 180),
			# now apply yaw and pitch
			(position_rotate_y, pos5, ":camera_yaw"),
			(position_rotate_x, pos5, ":camera_pitch"),
			(position_move_z, pos5, ":camera_distance", 0),
			(position_move_x, pos5, 60, 0),

			(init_position, pos2),
			(cur_tableau_add_troop, "trp_player", pos2, ":animation", 0),
			(cur_tableau_set_camera_position, pos5),

			(copy_position, pos8, pos5),
			(position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
			(position_rotate_z, pos8, 30),
			(position_rotate_x, pos8, -60),
			(cur_tableau_add_sun_light, pos8, 175,150,125),
		]),
  
	#script_add_troop_to_cur_tableau_for_party
	# INPUT: troop_no
	# OUTPUT: none
	("add_troop_to_cur_tableau_for_party",
		[
			(store_script_param, ":troop_no",1),
			(store_mod, ":hide_weapons", ":troop_no", 2), #hide_weapons flag is inside troop_no value
			(val_div, ":troop_no", 2), #removing the flag bit
			
			(set_fixed_point_multiplier, 100),
			
			(cur_tableau_clear_override_items),
			(try_begin),
				(eq, ":hide_weapons", 1),
				(cur_tableau_set_override_flags, af_override_fullhelm|af_override_head|af_override_weapons),
			(try_end),
			
			(init_position, pos2),
			(cur_tableau_set_camera_parameters, 1, 6, 6, 10, 10000),
			
			(init_position, pos5),
			(assign, ":cam_height", 105),
			# (val_mod, ":camera_distance", 5),
			(assign, ":camera_distance", 450),
			(assign, ":camera_yaw", 15),
			(assign, ":camera_pitch", -18),
			(assign, ":animation", anim_stand_man),
			
			(troop_get_inventory_slot, ":horse_item", ":troop_no", ek_horse),
			(try_begin),
				(gt, ":horse_item", 0),
				(eq, ":hide_weapons", 0),
				(cur_tableau_add_horse, ":horse_item", pos2, "anim_horse_stand", 0),
				(assign, ":animation", "anim_ride_0"),
				(assign, ":camera_yaw", 23),
				(assign, ":cam_height", 150),
				(assign, ":camera_distance", 550),
			(try_end),
			(position_set_z, pos5, ":cam_height"),
			
			# camera looks towards -z axis
			(position_rotate_x, pos5, -90),
			(position_rotate_z, pos5, 180),
			
			# now apply yaw and pitch
			(position_rotate_y, pos5, ":camera_yaw"),
			(position_rotate_x, pos5, ":camera_pitch"),
			(position_move_z, pos5, ":camera_distance", 0),
			(position_move_x, pos5, 5, 0),
			
			(try_begin),
				(troop_is_hero, ":troop_no"),
				(cur_tableau_add_troop, ":troop_no", pos2, ":animation", -1),
			(else_try),
				(store_mul, ":random_seed", ":troop_no", 126233),
				(val_mod, ":random_seed", 1000),
				(val_add, ":random_seed", 1),
				(cur_tableau_add_troop, ":troop_no", pos2, ":animation", ":random_seed"),
			(try_end),
			(cur_tableau_set_camera_position, pos5),
			
			(copy_position, pos8, pos5),
			(position_rotate_x, pos8, -90), #y axis aligned with camera now. z is up
			(position_rotate_z, pos8, 30), 
			(position_rotate_x, pos8, -60), 
			(cur_tableau_add_sun_light, pos8, 175,150,125),
		]),
	 
	 
	 
	 
	 
	########### 
	## Other ##
	###########
	#script_agent_troop_get_banner_mesh
	# INPUT: agent_no, troop_no
	# OUTPUT: banner_mesh
	("agent_troop_get_banner_mesh",
		[
			(store_script_param, ":agent_no", 1),
			(store_script_param, ":troop_no", 2),
			(assign, ":banner_troop", -1),
			(assign, ":banner_mesh", "mesh_banners_default_b"),
			(try_begin),
				(lt, ":agent_no", 0),
				(try_begin),
					(ge, ":troop_no", 0),
					(this_or_next|troop_slot_ge, ":troop_no", slot_troop_banner_scene_prop, 1),
					(eq, ":troop_no", "trp_player"),
					(assign, ":banner_troop", ":troop_no"),
				(else_try),
					(is_between, ":troop_no", companions_begin, companions_end),
					(assign, ":banner_troop", "trp_player"),
				(else_try),
					(assign, ":banner_mesh", "mesh_banners_default_a"),
				(try_end),
			(else_try),
				(agent_get_troop_id, ":troop_id", ":agent_no"),
				(this_or_next|troop_slot_ge,  ":troop_id", slot_troop_banner_scene_prop, 1),
				(eq, ":troop_no", "trp_player"),
				(assign, ":banner_troop", ":troop_id"),
			(else_try),
				(agent_get_party_id, ":agent_party", ":agent_no"),
				(try_begin),
					(lt, ":agent_party", 0),
					(is_between, ":troop_id", companions_begin, companions_end),
					(main_party_has_troop, ":troop_id"),
					(assign, ":agent_party", "p_main_party"),
				(try_end),
				(ge, ":agent_party", 0),
				(try_begin),
					(is_between, ":agent_party", centers_begin, centers_end),
					(party_get_slot, ":town_lord", "$g_encountered_party", slot_party_leader),
					(ge, ":town_lord", 0),
					(assign, ":banner_troop", ":town_lord"),
				(else_try),
					(this_or_next|party_slot_eq, ":agent_party", slot_party_type, spt_war_party),
					(eq, ":agent_party", "p_main_party"),
					(party_get_num_companion_stacks, ":num_stacks", ":agent_party"),
					(gt, ":num_stacks", 0),
					(party_stack_get_troop_id, ":leader_troop_id", ":agent_party", 0),
					(this_or_next|troop_slot_ge,  ":leader_troop_id", slot_troop_banner_scene_prop, 1),
					(eq, ":leader_troop_id", "trp_player"),
					(assign, ":banner_troop", ":leader_troop_id"),
				(try_end),
			(try_end),
			(try_begin),
				(ge, ":banner_troop", 0),
				(try_begin),
					(neg|troop_slot_ge, ":banner_troop", slot_troop_banner_scene_prop, 1),
					(assign, ":banner_mesh", "mesh_banners_default_b"),
				(else_try), 
					(troop_get_slot, ":banner_spr", ":banner_troop", slot_troop_banner_scene_prop),
					(store_add, ":banner_scene_props_end", banner_scene_props_end_minus_one, 1),
					(is_between, ":banner_spr", banner_scene_props_begin, ":banner_scene_props_end"),
					(val_sub, ":banner_spr", banner_scene_props_begin),
					(store_add, ":banner_mesh", ":banner_spr", arms_meshes_begin),
				(try_end),
			(try_end),
			(assign, reg0, ":banner_mesh"),
		]),
	
	#script_shield_item_set_banner
	# INPUT: agent_no
	# OUTPUT: none
	("shield_item_set_banner",
		[
			(store_script_param, ":tableau_no",1),
			(store_script_param, ":agent_no", 2),
			(store_script_param, ":troop_no", 3),
			(call_script, "script_agent_troop_get_banner_mesh", ":agent_no", ":troop_no"),
			(cur_item_set_tableau_material, ":tableau_no", reg0),
		 ]),
	  
	#script_troop_agent_set_banner
	# INPUT: agent_no
	# OUTPUT: none
	("troop_agent_set_banner",
		[
			(store_script_param, ":tableau_no",1),
			(store_script_param, ":agent_no", 2),
			(store_script_param, ":troop_no", 3),
			(call_script, "script_agent_troop_get_banner_mesh", ":agent_no", ":troop_no"),
			(cur_agent_set_banner_tableau_material, ":tableau_no", reg0),
		]),
	
	# script_test_spawn_team_members
	# input: 
	# 	arg1: team
	# 	arg2: spawn_point
	# output: none
	("test_spawn_team_members",
		[
			(store_script_param, ":team_no", 1),
			(store_script_param, ":spawn_point", 2),
			
			(call_script, "script_test_spawn_team_members_siege", ":team_no", ":spawn_point"),
		]),
	
	# script_test_spawn_team_members_siege
	# input:
	# 	arg1: team
	# 	arg2: spawn_point
	# output: none
	("test_spawn_team_members_siege",
		[
			(store_script_param, ":team_no", 1),
			(store_script_param, ":spawn_point", 2),
			
			(store_current_scene, ":cur_scene"),
			(modify_visitors_at_site, ":cur_scene"),
			
			(team_get_slot, ":faction_strength_bonus", ":team_no", slot_team_test_strength),
			(try_begin),
				(gt, ":faction_strength_bonus", -10),
				(team_get_slot, ":faction", ":team_no", slot_team_test_faction),
				(party_clear, "p_temp_party"),
				(party_set_faction, "p_temp_party", ":faction"),
				# (call_script, "script_party_add_reinforcements", "p_temp_party"),
				(call_script, "script_party_add_reinforcements", "p_temp_party"),
				
				(party_get_num_companion_stacks, ":num_stacks", "p_temp_party"),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":troop_id", "p_temp_party", ":i_stack"),
					(party_stack_get_size, ":num_troops", "p_temp_party", ":i_stack"),
					(add_visitors_to_current_scene, ":spawn_point", ":troop_id", ":num_troops"),
				(try_end),
				
				(party_set_faction, "p_temp_party", "fac_commoners"),
			
				(try_begin),
					(store_random_in_range, ":rand", 0, 2),
					(eq, ":rand", 0),
					(assign, ":num_tries", 10),
					(try_for_range, ":unused", 0, ":num_tries"),
						(store_random_in_range, ":lord", lords_begin, lords_end),
						(troop_slot_eq, ":lord", slot_troop_original_faction, ":faction"),
						
						(call_script, "script_troop_get_rank", ":lord"),
						(assign, ":real_rank", reg0),
						(call_script, "script_troop_change_level", ":lord", ":real_rank"),
						
						# (call_script, "script_troop_set_equip_type", ":lord"),
						
						# (store_random_in_range, ":new_rank", 0, 8),
						# (call_script, "script_troop_change_level", ":lord", ":new_rank"),
						# (troop_set_slot, ":lord", slot_troop_rank, ":new_rank"),
						# (call_script, "script_troop_update_name", ":lord"),
						
						# (modify_visitors_at_site, ":cur_scene"),
						(add_visitors_to_current_scene, ":spawn_point", ":lord", 1),
						(display_message, "@Spawning lord!"),
						(assign, ":num_tries", 0),
					(try_end),
				(try_end),
			(try_end),
		]),
	
	# script_agent_reassign_division
	# input:
	# 	agr1: agent_no
	# output:
	#	reg0: division
	("agent_reassign_division",
		[
			(store_script_param, ":agent_no", 1),
			
			(assign, ":new_div", -1),
			
			(agent_get_team, ":team", ":agent_no"),
			(try_begin),
				(agent_slot_eq, ":agent_no", slot_agent_charge, 1),
				(assign, ":new_div", 4),
			(else_try),
				(agent_get_horse, ":horse", ":agent_no"),
				(agent_get_ammo, ":ammo", ":agent_no", 0),
				
				(assign, ":has_ranged", 0),
				(assign, ":has_shield", 0),
				# 2 Is xbow/bow 1 is throwing
				(try_for_range, ":i_slot", ek_item_0, ek_head),
					(agent_get_item_slot, ":item", ":agent_no", ":i_slot"),
					(gt, ":item", 0),
					(item_get_type, ":item_type", ":item"),
					(try_begin),
						(is_between, ":item", "itm_darts", "itm_hunting_bow"),
						(lt, ":has_ranged", 1),
						(assign, ":has_ranged", 1),
					(else_try),
						(is_between, ":item", "itm_hunting_bow", "itm_items_end"),
						(try_begin),
							# Long bow not usable on horse
							(this_or_next|is_between, ":item", "itm_long_bow", "itm_khergit_bow"),
							# Heavy crossbows not usable on horse
							(is_between, ":item", "itm_crossbow", "itm_items_end"),
							(lt, ":has_ranged", 2),
							(assign, ":has_ranged", 2),
						(else_try),
							(lt, ":has_ranged", 3),
							(assign, ":has_ranged", 3),
						(try_end),
					(else_try),
						(is_between, ":item", shields_begin, shields_end),
						(val_add, ":has_shield", 4),
					(else_try),
						(this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
						(this_or_next|eq, ":item_type", itp_type_polearm), # We consider all polearms to be usable with a shield, even if it's false
						# Following is because 1h/2h weapons are considered 2h weapons and would not enter the previous check
						(this_or_next|eq, ":item", "itm_morningstar"),
						(this_or_next|eq, ":item", "itm_fighting_axe"),
						(this_or_next|eq, ":item", "itm_club_with_spike_head"),
						(is_between, ":item", "itm_bastard_sword_a", "itm_sword_of_war"), # Bastard swords
						(val_add, ":has_shield", 1),
					(try_end),
				(try_end),
				
				(try_begin),
					(gt, ":horse", 0),
					(assign, ":break", 0),
					(try_begin),
						# Horse archer
						(this_or_next|eq, ":has_ranged", 1), # Throw
						(eq, ":has_ranged", 3), # Bows/Light xbows
						(gt, ":ammo", 0),
						(assign, ":break", 1),
						(team_get_slot, ":harcher_division", ":team", slot_team_harcher_division),
						(ge, ":harcher_division", 0),
						(assign, ":new_div", ":harcher_division"),
					(else_try),
						# Horseman
						(assign, ":break", 1),
						(team_get_slot, ":horse_division", ":team", slot_team_horse_division),
						(ge, ":horse_division", 0),
						(assign, ":new_div", ":horse_division"),
					(try_end),
					(eq, ":break", 1),
				(else_try),
					(gt, ":ammo", 0),
					(assign, ":break", 0),
					(try_begin),
						(ge, ":has_ranged", 2),
						(assign, ":break", 1),
						(team_get_slot, ":archer_division", ":team", slot_team_archer_division),
						(ge, ":archer_division", 0),
						(assign, ":new_div", ":archer_division"),
					(else_try),
						(eq, ":has_ranged", 1),
						(assign, ":break", 1),
						(team_get_slot, ":throw_division", ":team", slot_team_throw_division),
						(ge, ":throw_division", 0),
						(assign, ":new_div", ":throw_division"),
					(try_end),
					(eq, ":break", 1),
					# Division assigned, break
				(else_try),
					(ge, ":has_shield", 5), # Needs a shield (4) plus a 1h weapon/polearm (1)
					(team_get_slot, ":shield_division", ":team", slot_team_shield_division),
					(ge, ":shield_division", 0),
					(assign, ":new_div", ":shield_division"),
				(else_try),
					(team_get_slot, ":rest_division", ":team", slot_team_rest_division),
					(assign, ":new_div", ":rest_division"),
				(try_end),
			(try_end),
			
			(try_begin),
				(is_between, ":new_div", 0, 9),
				(agent_get_division, ":old_div", ":agent_no"),
				(neq, ":new_div", ":old_div"),
				(agent_set_division, ":agent_no", ":new_div"),
				(agent_set_slot, ":agent_no", slot_agent_new_division, ":new_div"),
			(try_end),
			(assign, reg0, ":new_div"),
		]),
	
	# script_agent_reassign_division_siege
	# input:
	#	arg1: agent_no
	# output: none
	("agent_reassign_division_siege",
		[
			(store_script_param, ":agent_no", 1),
			
			(agent_get_team, ":team", ":agent_no"),
			(try_begin),
				(eq, ":team", 0),
				(agent_get_division, ":division", ":agent_no"),
				(agent_get_ammo, ":ammo", ":agent_no", 0),
				
				(try_begin),
					(eq, ":division", grc_archers),
					(le, ":ammo", 1),
					(call_script, "script_scene_get_defend_points_range"),
					(assign, ":begin", reg0),
					(assign, ":end", reg1),
					(store_random_in_range, ":rand", ":begin", ":end"),
					(store_sub, ":division", ":rand", ":begin"),
					(val_add, ":division", 2),
					(agent_set_slot, ":agent_no", slot_agent_new_division, ":division"),
					(agent_set_division, ":agent_no", ":division"),
				(else_try),
					(neq, ":division", grc_archers),
					(gt, ":ammo", 1),
					
					(call_script, "script_agent_reassign_division", ":agent_no"),
					(try_begin),
						(eq, reg0, grc_infantry),
						(agent_set_slot, ":agent_no", slot_agent_new_division, ":division"),
						(agent_set_division, ":agent_no", ":division"),
					(try_end),
					# (agent_set_slot, ":agent_no", slot_agent_new_division, grc_archers),
					# (agent_set_division, ":agent_no", grc_archers),
					
					(agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 0),
					(agent_set_slot, ":agent_no", slot_agent_target_entry_point, 0),
					(agent_set_slot, ":agent_no", slot_agent_is_in_scripted_mode, 0),
				(try_end),
			(else_try),
				(call_script, "script_agent_reassign_division", ":agent_no"),
			(try_end),
		]),
	
	# script_spawn_new_center_around_party
	# input:
	# 	arg1: party_no
	# 	arg2: spawn_type
	# Last argument is referring to what has caused the center to spawn
	# is it a revolted group of peasant, or is it an overpopulated center that sent them to make a village for raw materials
	# output: new_party_id
	("spawn_new_center_around_party",
		[
			(store_script_param, ":party_no", 1),
			# (store_script_parma, ":spawn_type", 2),
			
			(store_faction_of_party, ":faction_no", ":party_no"),
			
			(assign, ":template", "pt_village_template"),
			# (faction_get_slot, ":template", ":faction_no", slot_faction_village_template),
			
			(spawn_around_party, ":party_no", ":template"),
			(assign, ":new_party_id", reg0),
			
			(party_set_faction, ":new_party_id", ":faction_no"),
			
			(party_set_slot, ":new_party_id", slot_party_type, spt_village),
			
			(call_script, "script_party_init_center", ":new_party_id"),
			
			(call_script, "script_party_transfer_to_party", ":party_no", ":new_party_id"),
			
		]),
	
	# script_party_init_center
	# input:
	# 	arg1: party_no
	# output; none
	("party_init_center",
		[
			(store_script_param, ":party_no", 1),
			
			(store_faction_of_party, ":original_faction", ":party_no"),
			(party_set_slot, ":party_no", slot_party_original_faction, ":original_faction"),
			
			(party_set_slot, ":party_no", slot_party_ressource_radius, 3),
			
			(try_for_range, ":ressource", slot_party_ressources_begin, slot_party_ressources_end),
				(party_set_slot, ":party_no", ":ressource", 0),
			(try_end),
			
			(call_script, "script_party_update_nearby_resources", ":party_no"),
			(call_script, "script_center_init_productions", ":party_no"),
			
			(party_set_slot, ":party_no", slot_party_population, 0),
			(party_set_slot, ":party_no", slot_party_wealth, 0),
			
			(party_set_slot, ":party_no", slot_party_lord, -1),
			
			(party_set_slot, ":party_no", slot_party_besieged_by, -1),
			
			# ToDo:
			# (call_script, "script_party_set_siege_scene", ":party_no"),
			(store_random_in_range, ":siege_scene", castle_scene_begin, castle_scene_end),
			(party_set_slot, ":party_no", slot_party_siege_scene, ":siege_scene"),
		]),
	
	# script_party_update_nearby_resources
	# input:
	# 	arg1: party_no
	# output: none
	("party_update_nearby_resources",
		[
			(store_script_param, ":party_no", 1),
			
			(party_get_position, pos10, ":party_no"),
			(copy_position, pos11, pos10),
			
			(position_get_x, ":pos_init_x", pos10),
			(position_get_y, ":pos_init_y", pos10),
			# (position_get_z, ":pos_init_z", pos10),
			
			(call_script, "script_party_get_resources_radius", ":party_no"),
			(assign, ":radius", reg0),
			
			(try_for_range, ":range", 0, ":radius"),
				(store_add, ":effective_range", ":range", 1),
				(try_for_range, ":mult1", -1, 2),
					(try_for_range, ":mult2", -1, 2),
						(copy_position, pos11, pos10),
						
						(store_mul, ":x_offset", ":mult1", ressource_gathering_pace),
						(store_mul, ":y_offset", ":mult2", ressource_gathering_pace),
						(val_mul, ":x_offset", ":effective_range"),
						(val_mul, ":y_offset", ":effective_range"),
						(store_add, ":pos_x", ":x_offset", ":pos_init_x"),
						(store_add, ":pos_y", ":y_offset", ":pos_init_y"),
						
						(position_set_x, pos11, ":pos_x"),
						(position_set_y, pos11, ":pos_y"),
						
						(party_set_position, "p_resources_party", pos11),
						
						(party_get_current_terrain, ":terrain_type", "p_resources_party"),
						
						(party_get_position, pos11, "p_resources_party"),
						(position_get_z, ":height", pos11),
						
						(call_script, "script_party_update_resources_slot_with_terrain_and_height", ":party_no", ":terrain_type", ":height"),
					(try_end),
				(try_end),
			(try_end),
			
			# (try_for_range, ":ressource", slot_party_ressources_begin, slot_party_ressources_end),
				# (party_get_slot, reg10, ":party_no", ":ressource"),
				# (gt, reg10, 0),
				# (str_store_item_name, s10, ":ressource"),
				# (str_store_party_name, s11, ":party_no"),
				# (display_message, "@Center {s11} has ressource {s10}: {reg10}."),
			# (try_end),
		]),
	
	# script_party_get_resources_radius
	# input:
	# 	arg1: party_no
	# output:
	# 	reg0: resources_radius
	("party_get_resources_radius",
		[
			(store_script_param, ":party_no", 1),
			
			(party_get_slot, ":party_type", ":party_no", slot_party_type),
			
			(assign, ":radius", 1),
			
			(try_begin),
				(eq, ":party_type", spt_town),
				(assign, ":radius", 3),
			(else_try),
				(eq, ":party_type", spt_scout),
				(assign, ":radius", 1),
			(else_try),
				(assign, ":radius", 1),
			(try_end),
			
			(assign, reg0, ":radius"),
		]),
	
	# script_party_update_resources_slot_with_terrain_and_height
	# input:
	# 	arg1: party_no
	# 	arg2: terrain_type
	# 	arg3: height
	# output: none
	("party_update_resources_slot_with_terrain_and_height",
		[
			(store_script_param, ":party_no", 1),
			(store_script_param, ":terrain_type", 2),
			# (store_script_param, ":height", 3),
			
			# ToDo : raw_date_fruit
			
			(try_begin),
				(eq, ":terrain_type", rt_water),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_smoked_fish", 10),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_salt", 10),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_oil", 1),
				
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, 5),
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -1),
			(else_try),
				(eq, ":terrain_type", rt_mountain),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_iron", 10),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_stone", 10),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_salt", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_pottery", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wool", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_dyes", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_furs", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_cheese", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_sausages", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_dried_meat", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_apples", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_grapes", 6),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_olives", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_butter", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_cattle_meat", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_pork", 2),
				# (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
				
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, -2),
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -2),
			(else_try),
				(eq, ":terrain_type", rt_steppe),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_spice", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_stone", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_pottery", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_oil", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_flax", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wool", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_cheese", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_cabbages", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_grain", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_cattle_meat", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_chicken", 2),
				# (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
				
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, -5),
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -1),
			(else_try),
				(eq, ":terrain_type", rt_plain),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_flax", 3),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_oil", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wool", 3),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_stone", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_cheese", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_honey", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_sausages", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_cabbages", 3),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_dried_meat", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_apples", 5),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_grain", 6),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_butter", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_cattle_meat", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_chicken", 4),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_pork", 1),
				# (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
				
				# (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, 0),
				# (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, 0),
			(else_try),
				(eq, ":terrain_type", rt_snow),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_pottery", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wool", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_furs", 5),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_stone", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_cabbages", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_dried_meat", 5),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_grain", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_butter", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_chicken", 1),
				# (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
				
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, -2),
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -10),
			(else_try),
				(eq, ":terrain_type", rt_desert),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_pottery", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_dyes", 3),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_iron", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_date_fruit", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_olives", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_chicken", 1),
				# (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
				
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, -10),
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, 10),
			(else_try),
				(this_or_next|eq, ":terrain_type", rt_bridge),
				(eq, ":terrain_type", rt_river),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_smoked_fish", 4),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_cabbages", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_apples", 1),
				# (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
				
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, 10),
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -1),
			(else_try),
				(eq, ":terrain_type", rt_mountain_forest),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_iron", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_stone", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_salt", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wool", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_dyes", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_silk", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_furs", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 3),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_sausages", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_dried_meat", 3),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_grapes", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_butter", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_pork", 2),
				# (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
				
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, -5),
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -5),
			(else_try),
				(eq, ":terrain_type", rt_steppe_forest),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_spice", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_oil", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_flax", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_silk", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_furs", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 4),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_sausages", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_dried_meat", 3),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_apples", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_pork", 1),
				# (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
				
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, -3),
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -1),
			(else_try),
				(eq, ":terrain_type", rt_forest),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_flax", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_oil", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wool", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_silk", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 3),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_furs", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 6),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_sausages", 4),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_dried_meat", 5),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_apples", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_butter", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_pork", 4),
				# (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
				
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, 1),
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, 2),
			(else_try),
				(eq, ":terrain_type", rt_snow_forest),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wool", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_silk", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 3),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_furs", 8),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 8),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_dried_meat", 11),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_butter", 5),
				# (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
				
				# (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, 0),
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -8),
			(else_try),
				(eq, ":terrain_type", rt_desert_forest),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_dyes", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_silk", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_date_fruit", 10),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_dried_meat", 1),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_grapes", 2),
				(call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_olives", 2),
				# (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
				
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, 2),
				(call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, 8),
			(try_end),
		]),
	
	# script_party_update_resources_slot
	# input:
	# 	arg1: party_no
	# 	arg2: resource
	# 	arg3: value
	# output: none
	("party_update_resources_slot",
		[
			(store_script_param, ":party_no", 1),
			(store_script_param, ":resource", 2),
			(store_script_param, ":value", 3),
			
			(assign, ":resource_slot", ":resource"),
			(party_get_slot, ":current_resources", ":party_no", ":resource_slot"),
			(val_add, ":current_resources", ":value"),
			(party_set_slot, ":party_no", ":resource_slot", ":current_resources"),
		]),
	
	# script_party_update_weather_slot
	# input:
	# 	arg1: party_no
	# 	arg2: slot
	# 	arg3: value
	# output: none
	("party_update_weather_slot",
		[
			(store_script_param, ":party_no", 1),
			(store_script_param, ":slot", 2),
			(store_script_param, ":value", 3),
			
			(party_get_slot, ":current_weather", ":party_no", ":slot"),
			(val_add, ":current_weather", ":value"),
			(party_set_slot, ":party_no", ":slot", ":current_weather"),
		]),
	
	# script_center_init_productions
	# input:
	# 	arg1: center_no
	# output: none
	("center_init_productions",
		[
			# (store_script_param, ":center_no", 1),
		]),
	
	# script_party_transfer_to_party
	# input:
	# 	arg1: party_to_transfer
	# 	arg2: receiving_party
	# output: none
	("party_transfer_to_party",
		[
			(store_script_param, ":party_to_transfer", 1),
			(store_script_param, ":receiving_party", 2),
			
			(party_get_slot, ":party_to_transfer_wealth", ":party_to_transfer", slot_party_wealth),
			(party_get_slot, ":receiving_party_wealth", ":receiving_party", slot_party_wealth),
			(val_add, ":receiving_party_wealth", ":party_to_transfer_wealth"),
			
			(party_set_slot, ":receiving_party", slot_party_wealth, ":receiving_party_wealth"),
			
			(try_begin),
				(party_slot_ge, ":receiving_party", slot_party_type, spt_village),
				(party_get_slot, ":population_to_transfer", ":party_to_transfer", slot_party_population),
				(party_get_slot, ":party_population", ":receiving_party", slot_party_population),
				(val_add, ":party_population", ":population_to_transfer"),
				(party_set_slot, ":receiving_party", slot_party_population, ":party_population"),
			(try_end),
			
			(call_script, "script_party_transfer_members_to_party", ":party_to_transfer", ":receiving_party", 1),
		]),
	
	# script_party_transfer_members_to_party
	# input:
	# 	arg1: party_to_transfer
	# 	arg2: receiving_party
	# 	arg3: move heroes (0 no / 1 yes)
	# output: none
	("party_transfer_members_to_party",
		[
			(store_script_param, ":party_to_transfer", 1),
			(store_script_param, ":receiving_party", 2),
			(store_script_param, ":move_heroes", 3),
			
			(party_get_num_companion_stacks, ":num_stacks", ":party_to_transfer"),
			
			(try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
				(assign, ":continue", 1),
				(party_stack_get_size, ":i_stack_size", ":party_to_transfer", ":i_stack"),
				(party_stack_get_troop_id, ":troop_id", ":party_to_transfer", ":i_stack"),
				(try_begin),
					(eq, ":move_heroes", 0),
					(troop_is_hero, ":troop_id"),
					(assign, ":continue", 0),
				(try_end),
				(eq, ":continue", 1),
				(party_add_members, ":receiving_party", ":troop_id", ":i_stack_size"),
				(assign, ":really_added", reg0),
				(party_remove_members, ":party_to_transfer", ":troop_id", ":really_added"),
			(try_end),
		]),
	
	# script_init_battle_ais
	# input: none
	# output: none
	("init_battle_ais",
		[
			(try_for_range, ":cur_team", 0, 4),
				(team_give_order, ":cur_team", grc_infantry, mordr_stand_closer),
				(team_give_order, ":cur_team", grc_infantry, mordr_stand_closer),
				(team_give_order, ":cur_team", grc_archers, mordr_spread_out),
				
				(team_set_slot, ":cur_team", slot_team_battle_phase, stbp_combat),
				
				(call_script, "script_init_team_battle_ai", ":cur_team"),
			(try_end),
		]),
	
	# script_init_team_battle_ai
	# input:
	# 	arg1: team_no
	# output: none
	("init_team_battle_ai",
		[
			(store_script_param, ":team_no", 1),
			(try_begin),
				# (store_random_in_range, ":random", 0, 10),
				# (team_get_slot, ":team_main_faction", ":team_no", slot_team_test_faction),
				# ToDo: slot_team_tactic
				# (try_begin),
					# (eq, ":team_main_faction", "fac_kingdom_1"),
					# (try_begin),
						# (le, ":random", 0),
						# (assign, ":formation", stf_shieldwall),
					# (else_try),
						# (le, ":random", 1),
						# (assign, ":formation", stf_shieldwall),
					# (else_try),
						# ToDo: slot_team_formation
					# (try_end),
				# (else_try),
					# ToDo: faction
				# (try_end),
				
				(store_random_in_range, ":rand", 0, 2),
				(try_begin),
					(eq, ":rand", 0),
					(assign, ":formation", stf_shieldwall),
				(else_try),
					(assign, ":formation", stf_archers),
				(try_end),
				(team_set_slot, ":team_no", slot_team_formation, ":formation"),
				
				(assign, ":tactic", stt_default),
				(store_random_in_range, ":rand", 0, 10),
				(try_begin),
					(eq, ":rand", 0),
					(assign, ":tactic", stt_defend),
				(else_try),
					(eq, ":rand", 1),
					(assign, ":tactic", stt_short_engage),
				(try_end),
				(team_set_slot, ":team_no", slot_team_tactic, ":tactic"),
				
				(call_script, "script_team_set_division_slots_for_formation", ":team_no", ":formation"),
				
				(team_give_order, ":team_no", 4, mordr_charge),
			(try_end),
		]),
	
	# script_team_set_division_slots_for_formation
	# input:
	# 	arg1: team_no
	# 	arg2: formation
	# output: none
	("team_set_division_slots_for_formation",
		[
			(store_script_param, ":team_no", 1),
			(store_script_param, ":formation", 2),
			
			(try_begin),
				(eq, ":formation", stf_default),
				(team_set_slot, ":team_no", slot_team_harcher_division, -1),
				(team_set_slot, ":team_no", slot_team_horse_division, grc_cavalry),
				(team_set_slot, ":team_no", slot_team_throw_division, -1),
				(team_set_slot, ":team_no", slot_team_archer_division, grc_archers),
				(team_set_slot, ":team_no", slot_team_shield_division, -1),
				(team_set_slot, ":team_no", slot_team_rest_division, grc_infantry),
				(team_set_slot, ":team_no", slot_team_pike_division, -1),
				(team_set_slot, ":team_no", slot_team_lance_division, -1),
			(else_try),
				(eq, ":formation", stf_shieldwall),
				(team_set_slot, ":team_no", slot_team_harcher_division, -1),
				(team_set_slot, ":team_no", slot_team_horse_division, grc_cavalry),
				(team_set_slot, ":team_no", slot_team_throw_division, 3),
				(team_set_slot, ":team_no", slot_team_archer_division, grc_archers),
				(team_set_slot, ":team_no", slot_team_shield_division, grc_infantry),
				(team_set_slot, ":team_no", slot_team_rest_division, 3),
				(team_set_slot, ":team_no", slot_team_pike_division, -1),
				(team_set_slot, ":team_no", slot_team_lance_division, -1),
			(else_try),
				(eq, ":formation", stf_mounted_skirmisher),
				(team_set_slot, ":team_no", slot_team_harcher_division, 3),
				(team_set_slot, ":team_no", slot_team_horse_division, grc_cavalry),
				(team_set_slot, ":team_no", slot_team_throw_division, -1),
				(team_set_slot, ":team_no", slot_team_archer_division, grc_archers),
				(team_set_slot, ":team_no", slot_team_shield_division, -1),
				(team_set_slot, ":team_no", slot_team_rest_division, grc_infantry),
				(team_set_slot, ":team_no", slot_team_pike_division, -1),
				(team_set_slot, ":team_no", slot_team_lance_division, -1),
			(else_try),
				(eq, ":formation", stf_skirmisher),
				(team_set_slot, ":team_no", slot_team_harcher_division, -1),
				(team_set_slot, ":team_no", slot_team_horse_division, grc_cavalry),
				(team_set_slot, ":team_no", slot_team_throw_division, grc_archers),
				(team_set_slot, ":team_no", slot_team_archer_division, grc_archers),
				(team_set_slot, ":team_no", slot_team_shield_division, -1),
				(team_set_slot, ":team_no", slot_team_rest_division, grc_infantry),
				(team_set_slot, ":team_no", slot_team_pike_division, -1),
				(team_set_slot, ":team_no", slot_team_lance_division, -1),
			(else_try),
				(eq, ":formation", stf_thrower),
				(team_set_slot, ":team_no", slot_team_harcher_division, -1),
				(team_set_slot, ":team_no", slot_team_horse_division, grc_cavalry),
				(team_set_slot, ":team_no", slot_team_throw_division, 3),
				(team_set_slot, ":team_no", slot_team_archer_division, grc_archers),
				(team_set_slot, ":team_no", slot_team_shield_division, -1),
				(team_set_slot, ":team_no", slot_team_rest_division, grc_infantry),
				(team_set_slot, ":team_no", slot_team_pike_division, -1),
				(team_set_slot, ":team_no", slot_team_lance_division, -1),
			(else_try),
				(eq, ":formation", stf_lance),
				(team_set_slot, ":team_no", slot_team_harcher_division, -1),
				(team_set_slot, ":team_no", slot_team_horse_division, grc_cavalry),
				(team_set_slot, ":team_no", slot_team_throw_division, -1),
				(team_set_slot, ":team_no", slot_team_archer_division, grc_archers),
				(team_set_slot, ":team_no", slot_team_shield_division, -1),
				(team_set_slot, ":team_no", slot_team_rest_division, grc_infantry),
				(team_set_slot, ":team_no", slot_team_pike_division, -1),
				(team_set_slot, ":team_no", slot_team_pike_division, 3),
			(else_try),
				(eq, ":formation", stf_pikewall),
				(team_set_slot, ":team_no", slot_team_harcher_division, -1),
				(team_set_slot, ":team_no", slot_team_horse_division, grc_cavalry),
				(team_set_slot, ":team_no", slot_team_throw_division, -1),
				(team_set_slot, ":team_no", slot_team_archer_division, grc_archers),
				(team_set_slot, ":team_no", slot_team_shield_division, -1),
				(team_set_slot, ":team_no", slot_team_rest_division, grc_infantry),
				(team_set_slot, ":team_no", slot_team_pike_division, 3),
				(team_set_slot, ":team_no", slot_team_lance_division, -1),
			(else_try),
				(eq, ":formation", stf_archers),
				(team_set_slot, ":team_no", slot_team_harcher_division, grc_cavalry),
				(team_set_slot, ":team_no", slot_team_horse_division, grc_cavalry),
				(team_set_slot, ":team_no", slot_team_throw_division, 3),
				(team_set_slot, ":team_no", slot_team_archer_division, grc_archers),
				(team_set_slot, ":team_no", slot_team_shield_division, grc_infantry),
				(team_set_slot, ":team_no", slot_team_rest_division, grc_infantry),
				(team_set_slot, ":team_no", slot_team_pike_division, -1),
				(team_set_slot, ":team_no", slot_team_lance_division, -1),
			(else_try),
				(eq, ":formation", stf_siege),
				(team_set_slot, ":team_no", slot_team_harcher_division, -1),
				(team_set_slot, ":team_no", slot_team_horse_division, -1),
				(team_set_slot, ":team_no", slot_team_throw_division, grc_archers),
				(team_set_slot, ":team_no", slot_team_archer_division, grc_archers),
				(team_set_slot, ":team_no", slot_team_shield_division, -1),
				(team_set_slot, ":team_no", slot_team_rest_division, grc_infantry),
				(team_set_slot, ":team_no", slot_team_pike_division, -1),
				(team_set_slot, ":team_no", slot_team_lance_division, -1),
			(else_try),
				(eq, ":formation", stf_siege_no_throw),
				(team_set_slot, ":team_no", slot_team_harcher_division, -1),
				(team_set_slot, ":team_no", slot_team_horse_division, -1),
				(team_set_slot, ":team_no", slot_team_throw_division, grc_infantry),
				(team_set_slot, ":team_no", slot_team_archer_division, grc_archers),
				(team_set_slot, ":team_no", slot_team_shield_division, -1),
				(team_set_slot, ":team_no", slot_team_rest_division, grc_infantry),
				(team_set_slot, ":team_no", slot_team_pike_division, -1),
				(team_set_slot, ":team_no", slot_team_lance_division, -1),
			(try_end),
		]),
	
	# script_process_battle_ais
	# input: none
	# output: none
	("process_battle_ais",
		[
			(try_for_range, ":cur_team", 1, 4),
			# (try_for_range, ":cur_team", 1, 2), # ToDo: player control
				(call_script, "script_process_team_battle_ai", ":cur_team"),
			(try_end),
		]),
	
	# script_process_team_battle_ai
	# input:
	# 	arg1: team_no
	# output: none
	("process_team_battle_ai",
		[
			(store_script_param, ":team_no", 1),
			
			# (team_get_slot, ":main_faction", ":team_no", slot_team_test_faction),
			
			(team_get_slot, ":formation", ":team_no", slot_team_formation),
			(team_get_slot, ":tactic", ":team_no", slot_team_tactic),
			
			(team_get_slot, ":battle_phase", ":team_no", slot_team_battle_phase),
			
			(set_show_messages, 0),
			(try_begin),
				(eq, ":battle_phase", stbp_deploy),
				(team_get_slot, ":spawn_point", ":team_no", slot_team_test_spawn_point),
				(entry_point_get_position, pos1, ":spawn_point"),
			(else_try),
				(eq, ":battle_phase", stbp_advance),
				(team_give_order, ":team_no", grc_archers, mordr_advance),
				(team_get_order_position, pos1, ":team_no", grc_archers),
				(position_set_z_to_ground_level, pos1),
			(else_try),
				(eq, ":battle_phase", stbp_engage),
				(team_give_order, ":team_no", grc_archers, mordr_advance),
				(team_get_order_position, pos1, ":team_no", grc_archers),
				(position_set_z_to_ground_level, pos1),
			(else_try),
				(eq, ":battle_phase", stbp_combat),
			(try_end),
			
			(try_begin),
				(neq, ":battle_phase", stbp_combat),
				(this_or_next|neq, ":tactic", stt_defend),
				(neq, ":battle_phase", stbp_advance),
				
				(team_give_order, ":team_no", grc_infantry, mordr_hold),
				(team_give_order, ":team_no", grc_archers, mordr_hold),
				(team_give_order, ":team_no", grc_cavalry, mordr_hold),
				(team_give_order, ":team_no", 3, mordr_hold),
				(team_set_order_position, ":team_no", grc_infantry, pos1),
				(team_set_order_position, ":team_no", grc_archers, pos1),
				(team_set_order_position, ":team_no", grc_cavalry, pos1),
				(team_set_order_position, ":team_no", 3, pos1),
				
				(call_script, "script_apply_battle_formation_to_team", ":formation", ":team_no"),
			(try_end),
			
			(try_begin),
				(eq, ":battle_phase", stbp_deploy),
				(team_give_order, ":team_no", grc_archers, mordr_hold_fire),
				(team_set_slot, ":team_no", slot_team_battle_phase, stbp_advance),
			(else_try),
				(eq, ":battle_phase", stbp_advance),
				(call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team_no"),
				(try_begin),
					(neq, ":tactic", stt_short_engage),
					(lt, reg0, 15000),
					(team_give_order, ":team_no", grc_archers, mordr_fire_at_will),
					(team_set_slot, ":team_no", slot_team_battle_phase, stbp_engage),
				(else_try),
					(lt, reg0, 10000),
					(team_give_order, ":team_no", grc_archers, mordr_fire_at_will),
					(team_set_slot, ":team_no", slot_team_battle_phase, stbp_engage),
				(try_end),
			(else_try),
				(eq, ":battle_phase", stbp_engage),
				(call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team_no"),
				(try_begin),
					(lt, reg0, 2500),
					(team_give_order, ":team_no", grc_infantry, mordr_charge),
					(team_give_order, ":team_no", grc_archers, mordr_charge),
					(team_give_order, ":team_no", grc_cavalry, mordr_charge),
					(team_give_order, ":team_no", 3, mordr_charge),
					(team_set_slot, ":team_no", slot_team_battle_phase, stbp_combat),
				(try_end),
			(else_try),
				(eq, ":battle_phase", stbp_combat),
			(try_end),
				
			(set_show_messages, 1),
		]),
	
	# script_apply_battle_formation_to_team
	# input:
	# 	arg1: formation
	# 	arg2: team_no
	# output: none
	("apply_battle_formation_to_team",
		[
			(store_script_param, ":formation", 1),
			(store_script_param, ":team_no", 2),
			(try_begin),
				(eq, ":formation", stf_shieldwall),
				(team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
				(team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
				(team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
				
				(team_give_order, ":team_no", grc_infantry, mordr_advance),
				
				(team_give_order, ":team_no", 3, mordr_fall_back),
			(else_try),
				(eq, ":formation", stf_archers),
				(team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
				(team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
				(team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
				(team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
				
				(team_give_order, ":team_no", grc_infantry, mordr_fall_back),
				
				(team_give_order, ":team_no", 3, mordr_fall_back),
				(team_give_order, ":team_no", 3, mordr_fall_back),
			(else_try),
				(eq, ":formation", stf_lance),
				(team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
				(team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
				(team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
				
				(team_give_order, ":team_no", grc_infantry, mordr_advance),
				
				(team_give_order, ":team_no", 3, mordr_fall_back),
				(team_give_order, ":team_no", 3, mordr_fall_back),
			(else_try),
				(team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
				(team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
				(team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
				
				(team_give_order, ":team_no", grc_infantry, mordr_advance),
				(team_give_order, ":team_no", grc_infantry, mordr_advance),
				
				(team_give_order, ":team_no", 3, mordr_advance),
			(try_end),
		]),
	
	# script_team_get_average_position_of_enemies
	# input: 
	# 	arg1: team_no
	# output: 
	# 	pos0: average position
	("team_get_average_position_of_enemies",
		[
			(store_script_param_1, ":team_no"),
			(init_position, pos0),
			(assign, ":num_enemies", 0),
			(assign, ":accum_x", 0),
			(assign, ":accum_y", 0),
			(assign, ":accum_z", 0),
			(try_for_agents,":enemy_agent"),
				(agent_is_alive, ":enemy_agent"),
				(agent_is_human, ":enemy_agent"),
				(agent_get_team, ":enemy_team", ":enemy_agent"),
				(teams_are_enemies, ":team_no", ":enemy_team"),
				
				(agent_get_position, pos62, ":enemy_agent"),
				
				(position_get_x, ":x", pos62),
				(position_get_y, ":y", pos62),
				(position_get_z, ":z", pos62),
				
				(val_add, ":accum_x", ":x"),
				(val_add, ":accum_y", ":y"),
				(val_add, ":accum_z", ":z"),
				(val_add, ":num_enemies", 1),
			(try_end),
				
			(try_begin), #to avoid division by zeros at below division part.
				(le, ":num_enemies", 0),
				(assign, ":num_enemies", 1),
			(try_end),
			
			(store_div, ":average_x", ":accum_x", ":num_enemies"),
			(store_div, ":average_y", ":accum_y", ":num_enemies"),
			(store_div, ":average_z", ":accum_z", ":num_enemies"),
			
			(position_set_x, pos0, ":average_x"),
			(position_set_y, pos0, ":average_y"),
			(position_set_z, pos0, ":average_z"),
			
			(assign, reg0, ":num_enemies"),
		]),
	
	# script_get_closest3_distance_of_enemies_at_pos1
	# input: 
	# 	arg1: team_no
	# 	pos1
	# output: 
	# 	reg0: distance in cms
	("get_closest3_distance_of_enemies_at_pos1",
		[
			(assign, ":min_distance_1", 100000),
			(assign, ":min_distance_2", 100000),
			(assign, ":min_distance_3", 100000),
			
			(store_script_param, ":team_no", 1),
			(try_for_agents,":cur_agent"),
				(agent_is_alive, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_get_team, ":agent_team", ":cur_agent"),
				(teams_are_enemies, ":agent_team", ":team_no"),
				
				(agent_get_position, pos2, ":cur_agent"),
				(get_distance_between_positions,":cur_dist",pos2,pos1),
				(try_begin),
					(lt, ":cur_dist", ":min_distance_1"),
					(assign, ":min_distance_3", ":min_distance_2"),
					(assign, ":min_distance_2", ":min_distance_1"),
					(assign, ":min_distance_1", ":cur_dist"),
				(else_try),
					(lt, ":cur_dist", ":min_distance_2"),
					(assign, ":min_distance_3", ":min_distance_2"),
					(assign, ":min_distance_2", ":cur_dist"),
				(else_try),
					(lt, ":cur_dist", ":min_distance_3"),
					(assign, ":min_distance_3", ":cur_dist"),
				(try_end),
			(try_end),
			
			(assign, ":total_distance", 0),
			(assign, ":total_count", 0),
			(try_begin),
				(lt, ":min_distance_1", 100000),
				(val_add, ":total_distance", ":min_distance_1"),
				(val_add, ":total_count", 1),
			(try_end),
			(try_begin),
				(lt, ":min_distance_2", 100000),
				(val_add, ":total_distance", ":min_distance_2"),
				(val_add, ":total_count", 1),
			(try_end),
			(try_begin),
				(lt, ":min_distance_3", 100000),
				(val_add, ":total_distance", ":min_distance_3"),
				(val_add, ":total_count", 1),
			(try_end),
			(assign, ":average_distance", 100000),
			(try_begin),
				(gt, ":total_count", 0),
				(store_div, ":average_distance", ":total_distance", ":total_count"),
			(try_end),
			(assign, reg0, ":average_distance"),
			(assign, reg1, ":min_distance_1"),
			(assign, reg2, ":min_distance_2"),
			(assign, reg3, ":min_distance_3"),
		]),
	
	# script_party_process_production
	# input: 
	# 	arg1: party_no
	# output: none
	("party_process_production",
		[
			# ToDo:
			# (store_script_param, ":party_no", 1),
			
			# (party_get_slot, ":population", ":party_no", slot_party_population),
		]),
	
	# script_party_process_population
	# input: 
	# 	arg1: party_no
	# output: none
	("party_process_population",
		[
			(store_script_param, ":party_no", 1),
			
			(party_get_slot, ":party_type", ":party_no", slot_party_type),
			
			(party_get_slot, ":party_population", ":party_no", slot_party_population),
			# (party_get_slot, ":party_wealth", ":party_no", slot_party_wealth),
			
			(store_div, ":population_growth", ":party_population", 100),
			
			(store_random_in_range, ":population_growth", 2, 10),
			
			(try_begin),
				(eq, ":party_type", spt_village),
				(store_div, ":bonus_population", ":party_population", 20),
			(else_try),
				(eq, ":party_type", spt_castle),
				(store_div, ":bonus_population", ":party_population", 25),
			(else_try),
				(store_div, ":bonus_population", ":party_population", 100),
			(try_end),
			(val_add, ":population_growth", ":bonus_population"),
			
			(store_add, ":new_population", ":party_population", ":population_growth"),
			(call_script, "script_get_max_population", ":party_no"),
			(val_min, ":new_population", reg0),
			
			(party_set_slot, ":party_no", slot_party_population, ":new_population"),
			
			# (str_store_party_name, s10, ":party_no"),
			# (assign, reg10, ":party_population"),
			# (assign, reg11, ":new_population"),
			# (display_message, "@Center {s10}'s population: {reg11} (from {reg10})."),
		]),
	
	# script_get_max_population
	# input:
	# 	arg1: party_no
	# output:
	# 	reg0: max_population
	("get_max_population",
		[
			(store_script_param, ":party_no", 1),
			
			(party_get_slot, ":party_type", ":party_no", slot_party_type),
			
			(assign, ":max", 0),
			(try_begin),
				(eq, ":party_type", spt_town),
				(assign, ":max", population_max_town),
			(else_try),
				(eq, ":party_type", spt_castle),
				(assign, ":max", population_max_castle),
			(else_try),
				(eq, ":party_type", spt_village),
				(assign, ":max", population_max_village),
			(try_end),
			
			(assign, reg0, ":max"),
		]),
	
	# script_party_process_taxes
	# input:
	# 	arg1: party_no
	# output: none
	("party_process_taxes",
		[
			(store_script_param, ":party_no", 1),
			
			(party_get_slot, ":population", ":party_no", slot_party_population),
			(party_get_slot, ":wealth", ":party_no", slot_party_wealth),
			
			(store_div, ":taxes", ":population", 2),
			(store_div, ":random_max", ":taxes", 2),
			
			(store_random_in_range, ":rand", 0, ":random_max"),
			(val_add, ":taxes", ":rand"),
			
			(val_add, ":wealth", ":taxes"),
			(party_set_slot, ":party_no", slot_party_wealth, ":wealth"),
		]),
	
	# script_cf_party_send_surplus_population
	# input: 
	# 	arg1: party_no
	# output: 
	# 	reg0: num_spawned_party
	# fails if the center cannot send population
	("cf_party_send_surplus_population",
		[
			(store_script_param, ":party_no", 1),
			
			(assign, ":spawned", 0),
			
			(party_get_slot, ":party_type", ":party_no", slot_party_type),
			(try_begin),
				(eq, ":party_type", spt_town),
				# (str_store_party_name, s0, ":party_no"),
				# (display_message, "@Town {s0} sends surplus population."),
				
				(party_get_slot, ":meat_level", ":party_no", "itm_dried_meat"),
				(party_get_slot, ":leather_level", ":party_no", "itm_raw_leather"),
				
				(store_random_in_range, ":rand", 0, 10),
				(store_add, ":combined_level", ":meat_level", ":leather_level"),
				(try_begin),
					(gt, ":combined_level", ":rand"),
					(call_script, "script_cf_spawn_hunter_from_party", ":party_no"),
					(assign, ":spawned_party", reg0),
					
					(party_get_num_companions, ":num_troops", ":spawned_party"),
					(val_mul, ":num_troops", -1),
					(call_script, "script_party_modify_population", ":party_no", ":num_troops"),
					(val_add, ":spawned", 1),
				(try_end),
			(try_end),
			
			(assign, reg0, ":spawned"),
		]),
	
	# script_cf_spawn_hunter_from_party
	# input:
	# 	arg1: party_no
	# output:
	# 	reg0: spawned_party
	("cf_spawn_hunter_from_party",
		[
			(store_script_param, ":party_no", 1),
			
			(party_get_slot, ":num_hunters", ":party_no", slot_party_num_hunters),
			
			(call_script, "script_spawn_party_around_party", ":party_no", "pt_hunters"),
			(assign, ":spawned_party", reg0),
			
			(val_add, ":num_hunters", 1),
			(party_set_slot, ":party_no", slot_party_num_hunters, ":num_hunters"),
			
			(party_set_slot, ":spawned_party", slot_party_mission, spm_gather),
			(party_set_slot, ":spawned_party", slot_party_mission_object, ":party_no"),
			
			(party_set_slot, ":spawned_party", slot_party_type, spt_civilian),
			
			(party_set_ai_behavior, ":spawned_party", ai_bhvr_patrol_location),
			
			(assign, reg0, ":spawned_party"),
		]),
	
	# script_spawn_party_around_party
	# input: 
	# 	arg1: party_no
	# 	arg2: party_template_to_spawn
	# output:
	# 	reg0: spawned_party_id
	("spawn_party_around_party",
		[
			(store_script_param, ":party_no", 1),
			(store_script_param, ":party_template", 2),
			
			(store_faction_of_party, ":faction", ":party_no"),
			
			(set_spawn_radius, 2),
			
			(spawn_around_party, ":party_no", ":party_template"),
			(assign, ":spawned_party", reg0),
			
			(party_set_faction, ":spawned_party", ":faction"),
			
			(assign, reg0, ":spawned_party"),
		]),
	
	# script_cf_faction_need_party_nearby_resources
	# input:
	# 	arg1: faction_no
	# 	arg2: party_no
	# output: none
	("cf_faction_need_party_nearby_resources",
		[
			# ToDo:
		]),
	
	# script_spawn_new_center_marker_with_party_resources
	# input:
	# 	arg1: party_no
	# output: none
	("spawn_new_center_marker_with_party_resources",
		[
			# ToDo:
		]),
		
	# script_init_factions
	# input: none
	# output: none
	("init_factions",
		[
			(faction_set_slot, "fac_kingdom_1", slot_faction_culture, "fac_culture_1"),
			(faction_set_slot, "fac_kingdom_2", slot_faction_culture, "fac_culture_2"),
			(faction_set_slot, "fac_kingdom_3", slot_faction_culture, "fac_culture_3"),
			(faction_set_slot, "fac_kingdom_4", slot_faction_culture, "fac_culture_4"),
			(faction_set_slot, "fac_kingdom_5", slot_faction_culture, "fac_culture_5"),
			(faction_set_slot, "fac_kingdom_6", slot_faction_culture, "fac_culture_6"),
			
			(faction_set_slot, "fac_small_kingdom_11", slot_faction_culture, "fac_culture_1"),
			(faction_set_slot, "fac_small_kingdom_12", slot_faction_culture, "fac_culture_1"),
			(faction_set_slot, "fac_small_kingdom_13", slot_faction_culture, "fac_culture_1"),
			(faction_set_slot, "fac_small_kingdom_14", slot_faction_culture, "fac_culture_1"),
			(faction_set_slot, "fac_small_kingdom_15", slot_faction_culture, "fac_culture_1"),
			(faction_set_slot, "fac_small_kingdom_16", slot_faction_culture, "fac_culture_1"),
			(faction_set_slot, "fac_small_kingdom_17", slot_faction_culture, "fac_culture_1"),
			(faction_set_slot, "fac_small_kingdom_21", slot_faction_culture, "fac_culture_2"),
			(faction_set_slot, "fac_small_kingdom_22", slot_faction_culture, "fac_culture_2"),
			(faction_set_slot, "fac_small_kingdom_23", slot_faction_culture, "fac_culture_2"),
			(faction_set_slot, "fac_small_kingdom_24", slot_faction_culture, "fac_culture_2"),
			(faction_set_slot, "fac_small_kingdom_25", slot_faction_culture, "fac_culture_2"),
			(faction_set_slot, "fac_small_kingdom_31", slot_faction_culture, "fac_culture_3"),
			(faction_set_slot, "fac_small_kingdom_32", slot_faction_culture, "fac_culture_3"),
			(faction_set_slot, "fac_small_kingdom_33", slot_faction_culture, "fac_culture_3"),
			(faction_set_slot, "fac_small_kingdom_34", slot_faction_culture, "fac_culture_3"),
			(faction_set_slot, "fac_small_kingdom_35", slot_faction_culture, "fac_culture_3"),
			(faction_set_slot, "fac_small_kingdom_36", slot_faction_culture, "fac_culture_3"),
			(faction_set_slot, "fac_small_kingdom_41", slot_faction_culture, "fac_culture_4"),
			(faction_set_slot, "fac_small_kingdom_42", slot_faction_culture, "fac_culture_4"),
			(faction_set_slot, "fac_small_kingdom_43", slot_faction_culture, "fac_culture_4"),
			(faction_set_slot, "fac_small_kingdom_44", slot_faction_culture, "fac_culture_4"),
			(faction_set_slot, "fac_small_kingdom_45", slot_faction_culture, "fac_culture_4"),
			(faction_set_slot, "fac_small_kingdom_51", slot_faction_culture, "fac_culture_5"),
			(faction_set_slot, "fac_small_kingdom_52", slot_faction_culture, "fac_culture_5"),
			(faction_set_slot, "fac_small_kingdom_53", slot_faction_culture, "fac_culture_5"),
			(faction_set_slot, "fac_small_kingdom_54", slot_faction_culture, "fac_culture_5"),
			(faction_set_slot, "fac_small_kingdom_55", slot_faction_culture, "fac_culture_5"),
			(faction_set_slot, "fac_small_kingdom_61", slot_faction_culture, "fac_culture_6"),
			(faction_set_slot, "fac_small_kingdom_62", slot_faction_culture, "fac_culture_6"),
			(faction_set_slot, "fac_small_kingdom_63", slot_faction_culture, "fac_culture_6"),
			(faction_set_slot, "fac_small_kingdom_64", slot_faction_culture, "fac_culture_6"),
			(faction_set_slot, "fac_small_kingdom_65", slot_faction_culture, "fac_culture_6"),
			
			(faction_set_slot, "fac_kingdom_1", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_kingdom_1", slot_faction_common_num_tries, -5),
			(faction_set_slot, "fac_kingdom_1", slot_faction_veteran_num_tries, 3),
			(faction_set_slot, "fac_kingdom_1", slot_faction_elite_num_tries, 4),
			(faction_set_slot, "fac_kingdom_1", slot_faction_noble_num_tries, 3),
			
			(faction_set_slot, "fac_kingdom_2", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_kingdom_2", slot_faction_common_num_tries, 3),
			(faction_set_slot, "fac_kingdom_2", slot_faction_veteran_num_tries, 2),
			(faction_set_slot, "fac_kingdom_2", slot_faction_elite_num_tries, 0),
			(faction_set_slot, "fac_kingdom_2", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_kingdom_3", slot_faction_peasant_num_tries, 0),
			(faction_set_slot, "fac_kingdom_3", slot_faction_common_num_tries, 10),
			(faction_set_slot, "fac_kingdom_3", slot_faction_veteran_num_tries, -5),
			(faction_set_slot, "fac_kingdom_3", slot_faction_elite_num_tries, -5),
			(faction_set_slot, "fac_kingdom_3", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_kingdom_4", slot_faction_peasant_num_tries, -10),
			(faction_set_slot, "fac_kingdom_4", slot_faction_common_num_tries, 5),
			(faction_set_slot, "fac_kingdom_4", slot_faction_veteran_num_tries, 10),
			(faction_set_slot, "fac_kingdom_4", slot_faction_elite_num_tries, -5),
			(faction_set_slot, "fac_kingdom_4", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_kingdom_5", slot_faction_peasant_num_tries, 0),
			(faction_set_slot, "fac_kingdom_5", slot_faction_common_num_tries, 5),
			(faction_set_slot, "fac_kingdom_5", slot_faction_veteran_num_tries, 0),
			(faction_set_slot, "fac_kingdom_5", slot_faction_elite_num_tries, -2),
			(faction_set_slot, "fac_kingdom_5", slot_faction_noble_num_tries, -3),
			
			(faction_set_slot, "fac_kingdom_6", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_kingdom_6", slot_faction_common_num_tries, 10),
			(faction_set_slot, "fac_kingdom_6", slot_faction_veteran_num_tries, 0),
			(faction_set_slot, "fac_kingdom_6", slot_faction_elite_num_tries, -5),
			(faction_set_slot, "fac_kingdom_6", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_11", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_11", slot_faction_common_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_11", slot_faction_veteran_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_11", slot_faction_elite_num_tries, 3),
			(faction_set_slot, "fac_small_kingdom_11", slot_faction_noble_num_tries, 2),
			
			(faction_set_slot, "fac_small_kingdom_12", slot_faction_peasant_num_tries, -8),
			(faction_set_slot, "fac_small_kingdom_12", slot_faction_common_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_12", slot_faction_veteran_num_tries, 7),
			(faction_set_slot, "fac_small_kingdom_12", slot_faction_elite_num_tries, -3),
			(faction_set_slot, "fac_small_kingdom_12", slot_faction_noble_num_tries, -1),
			
			(faction_set_slot, "fac_small_kingdom_13", slot_faction_peasant_num_tries, 2),
			(faction_set_slot, "fac_small_kingdom_13", slot_faction_common_num_tries, -10),
			(faction_set_slot, "fac_small_kingdom_13", slot_faction_veteran_num_tries, -2),
			(faction_set_slot, "fac_small_kingdom_13", slot_faction_elite_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_13", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_14", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_14", slot_faction_common_num_tries, 1),
			(faction_set_slot, "fac_small_kingdom_14", slot_faction_veteran_num_tries, 7),
			(faction_set_slot, "fac_small_kingdom_14", slot_faction_elite_num_tries, -2),
			(faction_set_slot, "fac_small_kingdom_14", slot_faction_noble_num_tries, -1),
			
			(faction_set_slot, "fac_small_kingdom_15", slot_faction_peasant_num_tries, -6),
			(faction_set_slot, "fac_small_kingdom_15", slot_faction_common_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_15", slot_faction_veteran_num_tries, -1),
			(faction_set_slot, "fac_small_kingdom_15", slot_faction_elite_num_tries, -2),
			(faction_set_slot, "fac_small_kingdom_15", slot_faction_noble_num_tries, -1),
			
			(faction_set_slot, "fac_small_kingdom_16", slot_faction_peasant_num_tries, -10),
			(faction_set_slot, "fac_small_kingdom_16", slot_faction_common_num_tries, 8),
			(faction_set_slot, "fac_small_kingdom_16", slot_faction_veteran_num_tries, -1),
			(faction_set_slot, "fac_small_kingdom_16", slot_faction_elite_num_tries, -1),
			(faction_set_slot, "fac_small_kingdom_16", slot_faction_noble_num_tries, 2),
			
			(faction_set_slot, "fac_small_kingdom_17", slot_faction_peasant_num_tries, -6),
			(faction_set_slot, "fac_small_kingdom_17", slot_faction_common_num_tries, -2),
			(faction_set_slot, "fac_small_kingdom_17", slot_faction_veteran_num_tries, 3),
			(faction_set_slot, "fac_small_kingdom_17", slot_faction_elite_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_17", slot_faction_noble_num_tries, 5),
			
			(faction_set_slot, "fac_small_kingdom_21", slot_faction_peasant_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_21", slot_faction_common_num_tries, -10),
			(faction_set_slot, "fac_small_kingdom_21", slot_faction_veteran_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_21", slot_faction_elite_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_21", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_22", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_22", slot_faction_common_num_tries, 15),
			(faction_set_slot, "fac_small_kingdom_22", slot_faction_veteran_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_22", slot_faction_elite_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_22", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_23", slot_faction_peasant_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_23", slot_faction_common_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_23", slot_faction_veteran_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_23", slot_faction_elite_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_23", slot_faction_noble_num_tries, 5),
			
			(faction_set_slot, "fac_small_kingdom_24", slot_faction_peasant_num_tries, -10),
			(faction_set_slot, "fac_small_kingdom_24", slot_faction_common_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_24", slot_faction_veteran_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_24", slot_faction_elite_num_tries, -3),
			(faction_set_slot, "fac_small_kingdom_24", slot_faction_noble_num_tries, -2),
			
			(faction_set_slot, "fac_small_kingdom_25", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_25", slot_faction_common_num_tries, -2),
			(faction_set_slot, "fac_small_kingdom_25", slot_faction_veteran_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_25", slot_faction_elite_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_25", slot_faction_noble_num_tries, 2),
			
			(faction_set_slot, "fac_small_kingdom_31", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_31", slot_faction_common_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_31", slot_faction_veteran_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_31", slot_faction_elite_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_31", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_32", slot_faction_peasant_num_tries, -10),
			(faction_set_slot, "fac_small_kingdom_32", slot_faction_common_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_32", slot_faction_veteran_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_32", slot_faction_elite_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_32", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_33", slot_faction_peasant_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_33", slot_faction_common_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_33", slot_faction_veteran_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_33", slot_faction_elite_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_33", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_34", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_34", slot_faction_common_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_34", slot_faction_veteran_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_34", slot_faction_elite_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_34", slot_faction_noble_num_tries, 5),
			
			(faction_set_slot, "fac_small_kingdom_35", slot_faction_peasant_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_35", slot_faction_common_num_tries, -3),
			(faction_set_slot, "fac_small_kingdom_35", slot_faction_veteran_num_tries, -7),
			(faction_set_slot, "fac_small_kingdom_35", slot_faction_elite_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_35", slot_faction_noble_num_tries, 5),
			
			(faction_set_slot, "fac_small_kingdom_36", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_36", slot_faction_common_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_36", slot_faction_veteran_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_36", slot_faction_elite_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_36", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_41", slot_faction_peasant_num_tries, -10),
			(faction_set_slot, "fac_small_kingdom_41", slot_faction_common_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_41", slot_faction_veteran_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_41", slot_faction_elite_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_41", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_42", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_42", slot_faction_common_num_tries, -4),
			(faction_set_slot, "fac_small_kingdom_42", slot_faction_veteran_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_42", slot_faction_elite_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_42", slot_faction_noble_num_tries, -1),
			
			(faction_set_slot, "fac_small_kingdom_43", slot_faction_peasant_num_tries, -10),
			(faction_set_slot, "fac_small_kingdom_43", slot_faction_common_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_43", slot_faction_veteran_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_43", slot_faction_elite_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_43", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_44", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_44", slot_faction_common_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_44", slot_faction_veteran_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_44", slot_faction_elite_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_44", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_45", slot_faction_peasant_num_tries, -10),
			(faction_set_slot, "fac_small_kingdom_45", slot_faction_common_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_45", slot_faction_veteran_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_45", slot_faction_elite_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_45", slot_faction_noble_num_tries, 5),
			
			(faction_set_slot, "fac_small_kingdom_51", slot_faction_peasant_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_51", slot_faction_common_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_51", slot_faction_veteran_num_tries, -2),
			(faction_set_slot, "fac_small_kingdom_51", slot_faction_elite_num_tries, -3),
			(faction_set_slot, "fac_small_kingdom_51", slot_faction_noble_num_tries, -5),
			
			(faction_set_slot, "fac_small_kingdom_52", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_52", slot_faction_common_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_52", slot_faction_veteran_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_52", slot_faction_elite_num_tries, 3),
			(faction_set_slot, "fac_small_kingdom_52", slot_faction_noble_num_tries, 2),
			
			(faction_set_slot, "fac_small_kingdom_53", slot_faction_peasant_num_tries, -10),
			(faction_set_slot, "fac_small_kingdom_53", slot_faction_common_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_53", slot_faction_veteran_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_53", slot_faction_elite_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_53", slot_faction_noble_num_tries, 5),
			
			(faction_set_slot, "fac_small_kingdom_54", slot_faction_peasant_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_54", slot_faction_common_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_54", slot_faction_veteran_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_54", slot_faction_elite_num_tries, -3),
			(faction_set_slot, "fac_small_kingdom_54", slot_faction_noble_num_tries, -2),
			
			(faction_set_slot, "fac_small_kingdom_55", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_55", slot_faction_common_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_55", slot_faction_veteran_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_55", slot_faction_elite_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_55", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_61", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_61", slot_faction_common_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_61", slot_faction_veteran_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_61", slot_faction_elite_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_61", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_62", slot_faction_peasant_num_tries, -10),
			(faction_set_slot, "fac_small_kingdom_62", slot_faction_common_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_62", slot_faction_veteran_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_62", slot_faction_elite_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_62", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_63", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_63", slot_faction_common_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_63", slot_faction_veteran_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_63", slot_faction_elite_num_tries, 10),
			(faction_set_slot, "fac_small_kingdom_63", slot_faction_noble_num_tries, 5),
			
			(faction_set_slot, "fac_small_kingdom_64", slot_faction_peasant_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_64", slot_faction_common_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_64", slot_faction_veteran_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_64", slot_faction_elite_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_64", slot_faction_noble_num_tries, 0),
			
			(faction_set_slot, "fac_small_kingdom_65", slot_faction_peasant_num_tries, -5),
			(faction_set_slot, "fac_small_kingdom_65", slot_faction_common_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_65", slot_faction_veteran_num_tries, 5),
			(faction_set_slot, "fac_small_kingdom_65", slot_faction_elite_num_tries, 0),
			(faction_set_slot, "fac_small_kingdom_65", slot_faction_noble_num_tries, 0),
			
			(call_script, "script_init_factions_troop_ratio"),
			
			(call_script, "script_init_factions_politic"),
			(try_for_range, ":fac_1", "fac_faction_1", kingdoms_end),
				(faction_set_slot, ":fac_1", slot_faction_lord_gathering, -1),
			(try_end),
		]),
	
	# script_init_factions_troop_ratio
	# input: none
	# output: none
	("init_factions_troop_ratio",
		[
			(faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_infantry, 100),
			(faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_spearman, 25),
			(faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_pikeman, 5),
			(faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_skirmisher, 20),
			(faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_shock_infantry, 10),
			(faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_archer, 40),
			(faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_crossbow, 40),
			(faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_cavalry, 70),
			(faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_lancer, 15),
			(faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_horse_archer, 15),
			(faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_mounted_skirmisher, 5),
			
			(faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_infantry, 60),
			(faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_spearman, 15),
			(faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_pikeman, 5),
			(faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_skirmisher, 30),
			(faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_shock_infantry, 25),
			(faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_archer, 100),
			(faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_crossbow, 5),
			(faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_cavalry, 100),
			(faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_lancer, 25),
			(faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_horse_archer, 25),
			(faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_mounted_skirmisher, 30),
			
			(faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_infantry, 20),
			(faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_spearman, 5),
			(faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_pikeman, 5),
			(faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_skirmisher, 25),
			(faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_shock_infantry, 10),
			(faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_archer, 25),
			(faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_crossbow, 5),
			(faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_cavalry, 80),
			(faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_lancer, 100),
			(faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_horse_archer, 80),
			(faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_mounted_skirmisher, 50),
			
			(faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_infantry, 100),
			(faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_spearman, 30),
			(faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_pikeman, 10),
			(faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_skirmisher, 50),
			(faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_shock_infantry, 20),
			(faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_archer, 65),
			(faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_crossbow, 5),
			(faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_cavalry, 20),
			(faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_lancer, 10),
			(faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_horse_archer, 5),
			(faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_mounted_skirmisher, 15),
			
			(faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_infantry, 75),
			(faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_spearman, 100),
			(faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_pikeman, 55),
			(faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_skirmisher, 25),
			(faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_shock_infantry, 15),
			(faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_archer, 15),
			(faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_crossbow, 75),
			(faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_cavalry, 25),
			(faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_lancer, 30),
			(faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_horse_archer, 15),
			(faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_mounted_skirmisher, 10),
			
			(faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_infantry, 70),
			(faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_spearman, 10),
			(faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_pikeman, 10),
			(faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_skirmisher, 100),
			(faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_shock_infantry, 20),
			(faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_archer, 50),
			(faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_crossbow, 10),
			(faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_cavalry, 90),
			(faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_lancer, 30),
			(faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_horse_archer, 25),
			(faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_mounted_skirmisher, 100),
			
			(try_for_range, ":faction", "fac_small_kingdom_11", "fac_small_kingdom_21"),
				(call_script, "script_faction_copy_faction_troop_ratio", ":faction", "fac_kingdom_1"),
			(try_end),
			(try_for_range, ":faction", "fac_small_kingdom_21", "fac_small_kingdom_31"),
				(call_script, "script_faction_copy_faction_troop_ratio", ":faction", "fac_kingdom_2"),
			(try_end),
			(try_for_range, ":faction", "fac_small_kingdom_31", "fac_small_kingdom_41"),
				(call_script, "script_faction_copy_faction_troop_ratio", ":faction", "fac_kingdom_3"),
			(try_end),
			(try_for_range, ":faction", "fac_small_kingdom_41", "fac_small_kingdom_51"),
				(call_script, "script_faction_copy_faction_troop_ratio", ":faction", "fac_kingdom_4"),
			(try_end),
			(try_for_range, ":faction", "fac_small_kingdom_51", "fac_small_kingdom_61"),
				(call_script, "script_faction_copy_faction_troop_ratio", ":faction", "fac_kingdom_5"),
			(try_end),
			(try_for_range, ":faction", "fac_small_kingdom_61", kingdoms_end),
				(call_script, "script_faction_copy_faction_troop_ratio", ":faction", "fac_kingdom_6"),
			(try_end),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_11", slot_faction_troop_ratio_spearman, 15),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_11", slot_faction_troop_ratio_archer, -15),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_11", slot_faction_troop_ratio_crossbow, 15),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_12", slot_faction_troop_ratio_shock_infantry, 15),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_12", slot_faction_troop_ratio_cavalry, -10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_12", slot_faction_troop_ratio_lancer, -5),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_13", slot_faction_troop_ratio_infantry, -10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_13", slot_faction_troop_ratio_spearman, 10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_13", slot_faction_troop_ratio_lancer, 30),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_14", slot_faction_troop_ratio_archer, 35),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_14", slot_faction_troop_ratio_crossbow, -30),
			
			# (call_script, "script_faction_change_slot", "fac_small_kingdom_15", slot_faction_troop_ratio_cavalry, 20),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_15", slot_faction_troop_ratio_infantry, -10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_15", slot_faction_troop_ratio_crossbow, -5),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_15", slot_faction_troop_ratio_archer, -5),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_16", slot_faction_troop_ratio_skirmisher, 10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_16", slot_faction_troop_ratio_mounted_skirmisher, 15),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_16", slot_faction_troop_ratio_cavalry, -5),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_16", slot_faction_troop_ratio_infantry, -5),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_17", slot_faction_troop_ratio_cavalry, 5),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_17", slot_faction_troop_ratio_spearman, 10),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_21", slot_faction_troop_ratio_lancer, 35),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_21", slot_faction_troop_ratio_infantry, 10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_21", slot_faction_troop_ratio_cavalry, -10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_21", slot_faction_troop_ratio_archer, -10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_21", slot_faction_troop_ratio_spearman, 10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_21", slot_faction_troop_ratio_shock_infantry, 10),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_22", slot_faction_troop_ratio_cavalry, 10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_22", slot_faction_troop_ratio_infantry, 15),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_22", slot_faction_troop_ratio_spearman, 15),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_22", slot_faction_troop_ratio_shock_infantry, 15),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_23", slot_faction_troop_ratio_shock_infantry, 10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_23", slot_faction_troop_ratio_pikeman, 25),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_23", slot_faction_troop_ratio_spearman, -5),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_24", slot_faction_troop_ratio_skirmisher, 20),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_24", slot_faction_troop_ratio_infantry, -5),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_25", slot_faction_troop_ratio_horse_archer, 15),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_25", slot_faction_troop_ratio_archer, -10),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_31", slot_faction_troop_ratio_shock_infantry, 20),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_31", slot_faction_troop_ratio_infantry, 10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_31", slot_faction_troop_ratio_lancer, -10),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_spearman, 25),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_shock_infantry, 5),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_archer, 20),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_infantry, 40),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_skirmisher, 20),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_cavalry, -40),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_lancer, -30),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_horse_archer, -50),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_mounted_skirmisher, -30),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_33", slot_faction_troop_ratio_mounted_skirmisher, 30),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_33", slot_faction_troop_ratio_cavalry, -30),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_34", slot_faction_troop_ratio_horse_archer, -15),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_34", slot_faction_troop_ratio_cavalry, -10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_34", slot_faction_troop_ratio_mounted_skirmisher, -10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_34", slot_faction_troop_ratio_lancer, 20),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_35", slot_faction_troop_ratio_cavalry, 20),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_35", slot_faction_troop_ratio_lancer, -20),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_36", slot_faction_troop_ratio_archer, 15),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_36", slot_faction_troop_ratio_infantry, 25),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_36", slot_faction_troop_ratio_shock_infantry, 30),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_41", slot_faction_troop_ratio_cavalry, 5),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_41", slot_faction_troop_ratio_lancer, 20),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_41", slot_faction_troop_ratio_horse_archer, 10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_41", slot_faction_troop_ratio_archer, -5),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_41", slot_faction_troop_ratio_skirmisher, -10),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_42", slot_faction_troop_ratio_archer, 15),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_42", slot_faction_troop_ratio_skirmisher, -15),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_43", slot_faction_troop_ratio_skirmisher, 20),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_43", slot_faction_troop_ratio_infantry, -5),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_43", slot_faction_troop_ratio_archer, -15),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_44", slot_faction_troop_ratio_spearman, 30),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_44", slot_faction_troop_ratio_crossbow, 35),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_44", slot_faction_troop_ratio_archer, -10),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_45", slot_faction_troop_ratio_skirmisher, 10),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_archer, 60),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_crossbow, -60),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_cavalry, -10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_lancer, -10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_spearman, -5),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_pikeman, -10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_infantry, 15),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_52", slot_faction_troop_ratio_spearman, -10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_52", slot_faction_troop_ratio_cavalry, 15),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_53", slot_faction_troop_ratio_pikeman, -20),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_53", slot_faction_troop_ratio_cavalry, 35),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_54", slot_faction_troop_ratio_skirmisher, 25),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_54", slot_faction_troop_ratio_crossbow, -5),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_54", slot_faction_troop_ratio_archer, -5),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_54", slot_faction_troop_ratio_pikeman, -10),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_55", slot_faction_troop_ratio_cavalry, 5),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_55", slot_faction_troop_ratio_lancer, 55),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_55", slot_faction_troop_ratio_horse_archer, 10),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_61", slot_faction_troop_ratio_crossbow, 30),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_61", slot_faction_troop_ratio_skirmisher, -10),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_62", slot_faction_troop_ratio_archer, 30),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_62", slot_faction_troop_ratio_skirmisher, -50),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_62", slot_faction_troop_ratio_mounted_skirmisher, -15),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_63", slot_faction_troop_ratio_cavalry, 10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_63", slot_faction_troop_ratio_lancer, 15),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_63", slot_faction_troop_ratio_mounted_skirmisher, -20),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_63", slot_faction_troop_ratio_skirmisher, -15),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_64", slot_faction_troop_ratio_horse_archer, 35),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_64", slot_faction_troop_ratio_mounted_skirmisher, -25),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_64", slot_faction_troop_ratio_lancer, -5),
			
			(call_script, "script_faction_change_slot", "fac_small_kingdom_65", slot_faction_troop_ratio_pikeman, 20),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_65", slot_faction_troop_ratio_cavalry, -10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_65", slot_faction_troop_ratio_lancer, -10),
			(call_script, "script_faction_change_slot", "fac_small_kingdom_65", slot_faction_troop_ratio_horse_archer, -5),
		]),
	
	# script_faction_copy_troop_ratio
	# input:
	# 	arg1: faction_no
	# 	arg2: faction to copy slots from
	# output: none
	("faction_copy_faction_troop_ratio",
		[
			(store_script_param, ":faction_1", 1),
			(store_script_param, ":faction_2", 2),
			
			(try_for_range, ":slot", slot_faction_troop_ratio_infantry, slot_faction_troop_ratio_mounted_skirmisher + 1),
				(faction_get_slot, ":value", ":faction_2", ":slot"),
				(faction_set_slot, ":faction_1", ":slot", ":value"),
			(try_end),
		]),
	
	# script_faction_change_slot
	# input:
	# 	arg1: faction_no
	# 	arg2: slot
	# 	arg3: change
	# output: none
	("faction_change_slot",
		[
			(store_script_param, ":faction_no", 1),
			(store_script_param, ":slot", 2),
			(store_script_param, ":change", 3),
			
			(faction_get_slot, ":value", ":faction_no", ":slot"),
			(val_add, ":value", ":change"),
			(faction_set_slot, ":faction_no", ":slot", ":value"),
		]),
	
	# script_init_factions_politic
	# input: none
	# output: none
	("init_factions_politic",
		[
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_kingdom_1", "fac_kingdom_4", 0),
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_kingdom_1", "fac_kingdom_5", 0),
			
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_kingdom_2", "fac_kingdom_3", 0),
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_kingdom_2", "fac_kingdom_4", 0),
			
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_kingdom_3", "fac_kingdom_6", 0),
			
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_kingdom_5", "fac_kingdom_6", 0),
			
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_small_kingdom_11", "fac_kingdom_1", 3),
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_small_kingdom_11", "fac_kingdom_6", 0),
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_small_kingdom_12", "fac_kingdom_1", 3),
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_small_kingdom_13", "fac_kingdom_1", 1),
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_small_kingdom_14", "fac_kingdom_1", 4),
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_small_kingdom_15", "fac_kingdom_1", 4),
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_small_kingdom_16", "fac_kingdom_1", 2),
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_small_kingdom_17", "fac_kingdom_1", 3),
			
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_small_kingdom_21", "fac_kingdom_2", 4),
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_small_kingdom_22", "fac_kingdom_2", 3),
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_small_kingdom_23", "fac_kingdom_2", 2),
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_small_kingdom_24", "fac_kingdom_2", 4),
			# (call_script, "script_faction_set_random_relation_with_faction", "fac_small_kingdom_25", "fac_kingdom_2", 1),
		]),
	
	# script_init_cultures
	# input: none
	# output: none
	("init_cultures",
		[
			(faction_set_slot, "fac_culture_1", slot_faction_troops_begin, kingdom_1_troops_begin),
			(faction_set_slot, "fac_culture_1", slot_faction_troops_end, kingdom_1_troops_end),
			
			(faction_set_slot, "fac_culture_2", slot_faction_troops_begin, kingdom_2_troops_begin),
			(faction_set_slot, "fac_culture_2", slot_faction_troops_end, kingdom_2_troops_end),
			
			(faction_set_slot, "fac_culture_3", slot_faction_troops_begin, kingdom_3_troops_begin),
			(faction_set_slot, "fac_culture_3", slot_faction_troops_end, kingdom_3_troops_end),
			
			(faction_set_slot, "fac_culture_4", slot_faction_troops_begin, kingdom_4_troops_begin),
			(faction_set_slot, "fac_culture_4", slot_faction_troops_end, kingdom_4_troops_end),
			
			(faction_set_slot, "fac_culture_5", slot_faction_troops_begin, kingdom_5_troops_begin),
			(faction_set_slot, "fac_culture_5", slot_faction_troops_end, kingdom_5_troops_end),
			
			(faction_set_slot, "fac_culture_6", slot_faction_troops_begin, kingdom_6_troops_begin),
			(faction_set_slot, "fac_culture_6", slot_faction_troops_end, kingdom_6_troops_end),
			
			(faction_set_slot, "fac_culture_1", slot_faction_common_begin, "trp_swadian_light_infantry"),
			(faction_set_slot, "fac_culture_1", slot_faction_veteran_begin, "trp_swadian_spearman"),
			(faction_set_slot, "fac_culture_1", slot_faction_elite_begin, "trp_swadian_guard"),
			(faction_set_slot, "fac_culture_1", slot_faction_noble_begin, "trp_swadian_noble"),
			
			(faction_set_slot, "fac_culture_2", slot_faction_common_begin, "trp_vaegir_light_infantry"),
			(faction_set_slot, "fac_culture_2", slot_faction_veteran_begin, "trp_vaegir_heavy_infantry"),
			(faction_set_slot, "fac_culture_2", slot_faction_elite_begin, "trp_vaegir_guard"),
			(faction_set_slot, "fac_culture_2", slot_faction_noble_begin, "trp_vaegir_noble"),
			
			(faction_set_slot, "fac_culture_3", slot_faction_common_begin, "trp_khergit_light_infantry"),
			(faction_set_slot, "fac_culture_3", slot_faction_veteran_begin, "trp_khergit_heavy_infantry"),
			(faction_set_slot, "fac_culture_3", slot_faction_elite_begin, "trp_khergit_guard"),
			(faction_set_slot, "fac_culture_3", slot_faction_noble_begin, "trp_khergit_noble"),
			
			(faction_set_slot, "fac_culture_4", slot_faction_common_begin, "trp_nord_light_infantry"),
			(faction_set_slot, "fac_culture_4", slot_faction_veteran_begin, "trp_nord_medium_infantry"),
			(faction_set_slot, "fac_culture_4", slot_faction_elite_begin, "trp_nord_heavy_cavalry"),
			(faction_set_slot, "fac_culture_4", slot_faction_noble_begin, "trp_nord_heavy_infantry"),
			
			(faction_set_slot, "fac_culture_5", slot_faction_common_begin, "trp_rhodok_light_infantry"),
			(faction_set_slot, "fac_culture_5", slot_faction_veteran_begin, "trp_rhodok_heavy_infantry"),
			(faction_set_slot, "fac_culture_5", slot_faction_elite_begin, "trp_rhodok_heavy_pikeman"),
			(faction_set_slot, "fac_culture_5", slot_faction_noble_begin, "trp_rhodok_noble"),
			
			(faction_set_slot, "fac_culture_6", slot_faction_common_begin, "trp_sarranid_medium_infantry"),
			(faction_set_slot, "fac_culture_6", slot_faction_veteran_begin, "trp_sarranid_guard"),
			(faction_set_slot, "fac_culture_6", slot_faction_elite_begin, "trp_sarranid_heavy_infantry"),
			(faction_set_slot, "fac_culture_6", slot_faction_noble_begin, "trp_sarranid_noble"),
			
			(faction_set_slot, "fac_culture_1", slot_faction_lord_name_begin, "str_kingdom_rank_0"),
			(faction_set_slot, "fac_culture_2", slot_faction_lord_name_begin, "str_kingdom_rank_0"),
			(faction_set_slot, "fac_culture_3", slot_faction_lord_name_begin, "str_khergit_rank_0"),
			(faction_set_slot, "fac_culture_4", slot_faction_lord_name_begin, "str_nord_rank_0"),
			(faction_set_slot, "fac_culture_5", slot_faction_lord_name_begin, "str_rhodok_rank_0"),
			(faction_set_slot, "fac_culture_6", slot_faction_lord_name_begin, "str_sarranid_rank_0"),
			
			(faction_set_slot, "fac_culture_1", slot_faction_template_troops_begin, "trp_swadian_lord_template_0"),
			(faction_set_slot, "fac_culture_2", slot_faction_template_troops_begin, "trp_vaegir_lord_template_0"),
			(faction_set_slot, "fac_culture_3", slot_faction_template_troops_begin, "trp_khergit_lord_template_0"),
			(faction_set_slot, "fac_culture_4", slot_faction_template_troops_begin, "trp_nord_lord_template_0"),
			(faction_set_slot, "fac_culture_5", slot_faction_template_troops_begin, "trp_rhodok_lord_template_0"),
			(faction_set_slot, "fac_culture_6", slot_faction_template_troops_begin, "trp_sarranid_lord_template_0"),
			
			(faction_set_slot, "fac_culture_1", slot_faction_names_begin, swadian_names_begin),
			(faction_set_slot, "fac_culture_1", slot_faction_names_end, swadian_names_end),
			(faction_set_slot, "fac_culture_2", slot_faction_names_begin, vaegir_names_begin),
			(faction_set_slot, "fac_culture_2", slot_faction_names_end, vaegir_names_end),
			(faction_set_slot, "fac_culture_3", slot_faction_names_begin, khergit_names_begin),
			(faction_set_slot, "fac_culture_3", slot_faction_names_end, khergit_names_end),
			(faction_set_slot, "fac_culture_4", slot_faction_names_begin, nordic_names_begin),
			(faction_set_slot, "fac_culture_4", slot_faction_names_end, nordic_names_end),
			(faction_set_slot, "fac_culture_5", slot_faction_names_begin, rhodok_names_begin),
			(faction_set_slot, "fac_culture_5", slot_faction_names_end, rhodok_names_end),
			(faction_set_slot, "fac_culture_6", slot_faction_names_begin, sarranid_names_begin),
			(faction_set_slot, "fac_culture_6", slot_faction_names_end, sarranid_names_end),
			
			# (faction_set_slot, "fac_culture_", slot_faction__template_, "pt_kingdom__reinforcements__a"),
			# (try_for_range, ":culture", "fac_culture_1", "fac_culture_11"),
				# (try_for_range, ":offset", 0, 5),
					# (store_add, ":slot_beg", slot_faction_peasant_template_begin, ":offset"),
					# (store_add, ":slot_end", slot_faction_peasant_template_end, ":offset"),
					# (faction_slot_eq, ":culture", ":slot_end", 0),
					# (val_add, ":slot_beg", 1),
					# (faction_get_slot, ":value", ":culture", ":slot_beg"),
					# (faction_set_slot, ":culture", ":slot_end", ":value"),
				# (try_end),
			# (try_end),
		]),
	
	# script_init_bandits
	# input: none
	# output: none
	("init_bandits",
		[
			(faction_set_slot, "fac_faction_1", slot_faction_culture, "fac_faction_1"),
			(faction_set_slot, "fac_faction_2", slot_faction_culture, "fac_faction_2"),
			(faction_set_slot, "fac_faction_3", slot_faction_culture, "fac_faction_3"),
			(faction_set_slot, "fac_faction_4", slot_faction_culture, "fac_faction_4"),
			(faction_set_slot, "fac_faction_5", slot_faction_culture, "fac_faction_5"),
			(faction_set_slot, "fac_faction_6", slot_faction_culture, "fac_faction_6"),
			(faction_set_slot, "fac_faction_7", slot_faction_culture, "fac_faction_7"),
			
			(faction_set_slot, "fac_faction_1", slot_faction_troops_begin, "trp_bandit_forest_bandit"),
			(faction_set_slot, "fac_faction_1", slot_faction_common_begin, "trp_bandit_forest_warrior"),
			(faction_set_slot, "fac_faction_1", slot_faction_veteran_begin, "trp_bandit_forest_warrior"),
			(faction_set_slot, "fac_faction_1", slot_faction_elite_begin, "trp_bandit_forest_warrior"),
			(faction_set_slot, "fac_faction_1", slot_faction_noble_begin, "trp_bandit_forest_leader"),
			(faction_set_slot, "fac_faction_1", slot_faction_troops_end, "trp_bandit_looter"),
			
			(faction_set_slot, "fac_faction_1", slot_faction_troop_ratio_infantry, 75),
			(faction_set_slot, "fac_faction_1", slot_faction_troop_ratio_spearman, 10),
			(faction_set_slot, "fac_faction_1", slot_faction_troop_ratio_pikeman, 10),
			(faction_set_slot, "fac_faction_1", slot_faction_troop_ratio_skirmisher, 30),
			(faction_set_slot, "fac_faction_1", slot_faction_troop_ratio_shock_infantry, 60),
			(faction_set_slot, "fac_faction_1", slot_faction_troop_ratio_archer, 100),
			(faction_set_slot, "fac_faction_1", slot_faction_troop_ratio_crossbow, 90),
			(faction_set_slot, "fac_faction_1", slot_faction_troop_ratio_cavalry, 20),
			(faction_set_slot, "fac_faction_1", slot_faction_troop_ratio_lancer, 5),
			(faction_set_slot, "fac_faction_1", slot_faction_troop_ratio_horse_archer, 25),
			(faction_set_slot, "fac_faction_1", slot_faction_troop_ratio_mounted_skirmisher, 10),
			
			(faction_set_slot, "fac_faction_2", slot_faction_troops_begin, "trp_bandit_looter"),
			(faction_set_slot, "fac_faction_2", slot_faction_common_begin, "trp_bandit_marauder"),
			(faction_set_slot, "fac_faction_2", slot_faction_veteran_begin, "trp_bandit_marauder"),
			(faction_set_slot, "fac_faction_2", slot_faction_elite_begin, "trp_bandit_marauder"),
			(faction_set_slot, "fac_faction_2", slot_faction_noble_begin, "trp_bandit_leader"),
			(faction_set_slot, "fac_faction_2", slot_faction_troops_end, "trp_bandit_mountain_rider"),
			
			(faction_set_slot, "fac_faction_2", slot_faction_troop_ratio_infantry, 100),
			(faction_set_slot, "fac_faction_2", slot_faction_troop_ratio_spearman, 10),
			(faction_set_slot, "fac_faction_2", slot_faction_troop_ratio_pikeman, 10),
			(faction_set_slot, "fac_faction_2", slot_faction_troop_ratio_skirmisher, 10),
			(faction_set_slot, "fac_faction_2", slot_faction_troop_ratio_shock_infantry, 65),
			(faction_set_slot, "fac_faction_2", slot_faction_troop_ratio_archer, 20),
			(faction_set_slot, "fac_faction_2", slot_faction_troop_ratio_crossbow, 50),
			(faction_set_slot, "fac_faction_2", slot_faction_troop_ratio_cavalry, 25),
			(faction_set_slot, "fac_faction_2", slot_faction_troop_ratio_lancer, 5),
			(faction_set_slot, "fac_faction_2", slot_faction_troop_ratio_horse_archer, 15),
			(faction_set_slot, "fac_faction_2", slot_faction_troop_ratio_mounted_skirmisher, 5),
			
			(faction_set_slot, "fac_faction_3", slot_faction_troops_begin, "trp_bandit_mountain_rider"),
			(faction_set_slot, "fac_faction_3", slot_faction_common_begin, "trp_bandit_mountain_warrior"),
			(faction_set_slot, "fac_faction_3", slot_faction_veteran_begin, "trp_bandit_mountain_warrior"),
			(faction_set_slot, "fac_faction_3", slot_faction_elite_begin, "trp_bandit_mountain_warrior"),
			(faction_set_slot, "fac_faction_3", slot_faction_noble_begin, "trp_bandit_mountain_chieftain"),
			(faction_set_slot, "fac_faction_3", slot_faction_troops_end, "trp_bandit_sea_raider"),
			
			(faction_set_slot, "fac_faction_3", slot_faction_troop_ratio_infantry, 80),
			(faction_set_slot, "fac_faction_3", slot_faction_troop_ratio_spearman, 10),
			(faction_set_slot, "fac_faction_3", slot_faction_troop_ratio_pikeman, 10),
			(faction_set_slot, "fac_faction_3", slot_faction_troop_ratio_skirmisher, 80),
			(faction_set_slot, "fac_faction_3", slot_faction_troop_ratio_shock_infantry, 50),
			(faction_set_slot, "fac_faction_3", slot_faction_troop_ratio_archer, 50),
			(faction_set_slot, "fac_faction_3", slot_faction_troop_ratio_crossbow, 10),
			(faction_set_slot, "fac_faction_3", slot_faction_troop_ratio_cavalry, 35),
			(faction_set_slot, "fac_faction_3", slot_faction_troop_ratio_lancer, 10),
			(faction_set_slot, "fac_faction_3", slot_faction_troop_ratio_horse_archer, 15),
			(faction_set_slot, "fac_faction_3", slot_faction_troop_ratio_mounted_skirmisher, 60),
			
			(faction_set_slot, "fac_faction_4", slot_faction_troops_begin, "trp_bandit_sea_raider"),
			(faction_set_slot, "fac_faction_4", slot_faction_common_begin, "trp_bandit_skull_crusher"),
			(faction_set_slot, "fac_faction_4", slot_faction_veteran_begin, "trp_bandit_skull_crusher"),
			(faction_set_slot, "fac_faction_4", slot_faction_elite_begin, "trp_bandit_skull_crusher"),
			(faction_set_slot, "fac_faction_4", slot_faction_noble_begin, "trp_bandit_sea_captain"),
			(faction_set_slot, "fac_faction_4", slot_faction_troops_end, "trp_bandit_steppe_bandit"),
			
			(faction_set_slot, "fac_faction_4", slot_faction_troop_ratio_infantry, 100),
			(faction_set_slot, "fac_faction_4", slot_faction_troop_ratio_spearman, 10),
			(faction_set_slot, "fac_faction_4", slot_faction_troop_ratio_pikeman, 10),
			(faction_set_slot, "fac_faction_4", slot_faction_troop_ratio_skirmisher, 60),
			(faction_set_slot, "fac_faction_4", slot_faction_troop_ratio_shock_infantry, 50),
			(faction_set_slot, "fac_faction_4", slot_faction_troop_ratio_archer, 35),
			(faction_set_slot, "fac_faction_4", slot_faction_troop_ratio_crossbow, 10),
			(faction_set_slot, "fac_faction_4", slot_faction_troop_ratio_cavalry, 15),
			(faction_set_slot, "fac_faction_4", slot_faction_troop_ratio_lancer, 5),
			(faction_set_slot, "fac_faction_4", slot_faction_troop_ratio_horse_archer, 10),
			(faction_set_slot, "fac_faction_4", slot_faction_troop_ratio_mounted_skirmisher, 20),
			
			(faction_set_slot, "fac_faction_5", slot_faction_troops_begin, "trp_bandit_steppe_bandit"),
			(faction_set_slot, "fac_faction_5", slot_faction_common_begin, "trp_bandit_steppe_rider"),
			(faction_set_slot, "fac_faction_5", slot_faction_veteran_begin, "trp_bandit_steppe_rider"),
			(faction_set_slot, "fac_faction_5", slot_faction_elite_begin, "trp_bandit_steppe_rider"),
			(faction_set_slot, "fac_faction_5", slot_faction_noble_begin, "trp_bandit_steppe_chief"),
			(faction_set_slot, "fac_faction_5", slot_faction_troops_end, "trp_bandit_tundra_bandit"),
			
			(faction_set_slot, "fac_faction_5", slot_faction_troop_ratio_infantry, 35),
			(faction_set_slot, "fac_faction_5", slot_faction_troop_ratio_spearman, 5),
			(faction_set_slot, "fac_faction_5", slot_faction_troop_ratio_pikeman, 5),
			(faction_set_slot, "fac_faction_5", slot_faction_troop_ratio_skirmisher, 50),
			(faction_set_slot, "fac_faction_5", slot_faction_troop_ratio_shock_infantry, 20),
			(faction_set_slot, "fac_faction_5", slot_faction_troop_ratio_archer, 35),
			(faction_set_slot, "fac_faction_5", slot_faction_troop_ratio_crossbow, 5),
			(faction_set_slot, "fac_faction_5", slot_faction_troop_ratio_cavalry, 100),
			(faction_set_slot, "fac_faction_5", slot_faction_troop_ratio_lancer, 100),
			(faction_set_slot, "fac_faction_5", slot_faction_troop_ratio_horse_archer, 100),
			(faction_set_slot, "fac_faction_5", slot_faction_troop_ratio_mounted_skirmisher, 80),
			
			(faction_set_slot, "fac_faction_6", slot_faction_troops_begin, "trp_bandit_tundra_bandit"),
			(faction_set_slot, "fac_faction_6", slot_faction_common_begin, "trp_bandit_tundra_rider"),
			(faction_set_slot, "fac_faction_6", slot_faction_veteran_begin, "trp_bandit_tundra_rider"),
			(faction_set_slot, "fac_faction_6", slot_faction_elite_begin, "trp_bandit_taiga_bandit"),
			(faction_set_slot, "fac_faction_6", slot_faction_noble_begin, "trp_bandit_taiga_chieftain"),
			(faction_set_slot, "fac_faction_6", slot_faction_troops_end, "trp_bandit_desert_bandit"),
			
			(faction_set_slot, "fac_faction_6", slot_faction_troop_ratio_infantry, 50),
			(faction_set_slot, "fac_faction_6", slot_faction_troop_ratio_spearman, 10),
			(faction_set_slot, "fac_faction_6", slot_faction_troop_ratio_pikeman, 10),
			(faction_set_slot, "fac_faction_6", slot_faction_troop_ratio_skirmisher, 100),
			(faction_set_slot, "fac_faction_6", slot_faction_troop_ratio_shock_infantry, 50),
			(faction_set_slot, "fac_faction_6", slot_faction_troop_ratio_archer, 80),
			(faction_set_slot, "fac_faction_6", slot_faction_troop_ratio_crossbow, 5),
			(faction_set_slot, "fac_faction_6", slot_faction_troop_ratio_cavalry, 15),
			(faction_set_slot, "fac_faction_6", slot_faction_troop_ratio_lancer, 5),
			(faction_set_slot, "fac_faction_6", slot_faction_troop_ratio_horse_archer, 20),
			(faction_set_slot, "fac_faction_6", slot_faction_troop_ratio_mounted_skirmisher, 20),
			
			(faction_set_slot, "fac_faction_7", slot_faction_troops_begin, "trp_bandit_desert_bandit"),
			(faction_set_slot, "fac_faction_7", slot_faction_common_begin, "trp_bandit_desert_rider"),
			(faction_set_slot, "fac_faction_7", slot_faction_veteran_begin, "trp_bandit_desert_rider"),
			(faction_set_slot, "fac_faction_7", slot_faction_elite_begin, "trp_bandit_desert_nomad"),
			(faction_set_slot, "fac_faction_7", slot_faction_noble_begin, "trp_bandit_desert_chief"),
			(faction_set_slot, "fac_faction_7", slot_faction_troops_end, bandits_end),
			
			(faction_set_slot, "fac_faction_7", slot_faction_troop_ratio_infantry, 65),
			(faction_set_slot, "fac_faction_7", slot_faction_troop_ratio_spearman, 10),
			(faction_set_slot, "fac_faction_7", slot_faction_troop_ratio_pikeman, 10),
			(faction_set_slot, "fac_faction_7", slot_faction_troop_ratio_skirmisher, 80),
			(faction_set_slot, "fac_faction_7", slot_faction_troop_ratio_shock_infantry, 50),
			(faction_set_slot, "fac_faction_7", slot_faction_troop_ratio_archer, 45),
			(faction_set_slot, "fac_faction_7", slot_faction_troop_ratio_crossbow, 5),
			(faction_set_slot, "fac_faction_7", slot_faction_troop_ratio_cavalry, 80),
			(faction_set_slot, "fac_faction_7", slot_faction_troop_ratio_lancer, 75),
			(faction_set_slot, "fac_faction_7", slot_faction_troop_ratio_horse_archer, 50),
			(faction_set_slot, "fac_faction_7", slot_faction_troop_ratio_mounted_skirmisher, 90),
			
			# (try_for_range, ":culture", "fac_faction_1", "fac_kingdom_1"),
				# (try_for_range, ":offset", 0, 5),
					# (store_add, ":slot_beg", slot_faction_peasant_template_begin, ":offset"),
					# (store_add, ":slot_end", slot_faction_peasant_template_end, ":offset"),
					# (faction_slot_eq, ":culture", ":slot_end", 0),
					# (val_add, ":slot_beg", 1),
					# (faction_get_slot, ":value", ":culture", ":slot_beg"),
					# (faction_set_slot, ":culture", ":slot_end", ":value"),
				# (try_end),
			# (try_end),
		]),
	
	# script_faction_declare_war_to_faction
	# input:
	# 	arg1: faction_1
	# 	arg2: faction_2
	# output: none
	("faction_declare_war_to_faction",
		[
			(store_script_param, ":faction_1", 1),
			(store_script_param, ":faction_2", 2),
			
			(set_relation, ":faction_1", ":faction_2", relation_war-10),
			(set_relation, ":faction_2", ":faction_1", relation_war-10),
			
			(faction_get_slot, ":num_wars_1", ":faction_1", slot_faction_is_at_war),
			(try_begin),
				(lt, ":num_wars_1", 0),
				(faction_set_slot, ":faction_1", slot_faction_is_at_war, 1),
			(else_try),
				(val_add, ":num_wars_1", 1),
				(faction_set_slot, ":faction_1", slot_faction_is_at_war, ":num_wars_1"),
			(try_end),
			(faction_get_slot, ":num_wars_2", ":faction_2", slot_faction_is_at_war),
			(try_begin),
				(lt, ":num_wars_2", 0),
				(faction_set_slot, ":faction_2", slot_faction_is_at_war, 1),
			(else_try),
				(val_add, ":num_wars_2", 1),
				(faction_set_slot, ":faction_2", slot_faction_is_at_war, ":num_wars_2"),
			(try_end),
		]),
	
	# script_faction_make_peace_to_faction
	# input:
	# 	arg1: faction_1
	# 	arg2: faction_2
	# output: none
	("faction_make_peace_to_faction",
		[
			(store_script_param, ":faction_1", 1),
			(store_script_param, ":faction_2", 2),
			
			(set_relation, ":faction_1", ":faction_2", relation_neutral),
			(set_relation, ":faction_2", ":faction_1", relation_neutral),
			
			(faction_get_slot, ":num_wars_1", ":faction_1", slot_faction_is_at_war),
			(val_add, ":num_wars_1", -1),
			(faction_set_slot, ":faction_1", slot_faction_is_at_war, ":num_wars_1"),
			
			(faction_get_slot, ":num_wars_2", ":faction_2", slot_faction_is_at_war),
			(val_add, ":num_wars_2", -1),
			(faction_set_slot, ":faction_2", slot_faction_is_at_war, ":num_wars_2"),
		]),
	
	# script_faction_set_random_relation_with_faction
	# input:
	# 	arg1: faction_1
	# 	arg2: faction_2
	# 	arg3: relation (0: war, 1: bad terms, 2: neutral, 3: friendly, 4: allies, -1: random_no_war)
	("faction_set_random_relation_with_faction",
		[
			(store_script_param, ":faction_1", 1),
			(store_script_param, ":faction_2", 2),
			(store_script_param, ":relation", 3),
			
			(try_begin),
				(eq, ":relation", 0),
				(store_random_in_range, ":new_relation", -100, relation_war),
				(store_random_in_range, ":new_relation", ":new_relation", relation_war), # Make it closer to relation_war
				(call_script, "script_faction_declare_war_to_faction", ":faction_1", ":faction_2"),
			(else_try),
				(eq, ":relation", 1),
				(store_random_in_range, ":new_relation", relation_war, relation_bad),
				(store_random_in_range, ":new_relation", ":new_relation", relation_bad), # Make it closer to relation_bad
			(else_try),
				(eq, ":relation", 2),
				(store_random_in_range, ":new_relation", relation_bad, relation_friendly),
				(try_begin),
					(lt, ":new_relation", relation_neutral),
					(store_random_in_range, ":new_relation", ":new_relation", relation_neutral),
				(else_try),
					(gt, ":new_relation", relation_neutral),
					(store_random_in_range, ":new_relation", relation_neutral, ":new_relation"),
				(try_end),
			(else_try),
				(eq, ":relation", 3),
				(store_random_in_range, ":new_relation", relation_friendly, relation_allies),
				(store_random_in_range, ":new_relation", relation_friendly, ":new_relation"), # Make it closer to relation_friendly
			(else_try),
				(eq, ":relation", 4),
				(store_random_in_range, ":new_relation", relation_allies, 100),
				(store_random_in_range, ":new_relation", relation_allies, ":new_relation"), # Make it closer to relation_allies
			(else_try),
				(eq, ":relation", -1),
				(store_random_in_range, ":new_relation", relation_war, relation_allies),
			(else_try),
				(store_random_in_range, ":new_relation", relation_bad, relation_friendly),
			(try_end),
			
			(set_relation, ":faction_1", ":faction_2", ":new_relation"),
			(set_relation, ":faction_2", ":faction_1", ":new_relation"),
		]),
	
	# script_troop_change_level
	# input:
	# 	arg1: troop_no
	# 	arg2: new_rank
	# output: none
	("troop_change_level",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":new_rank", 2),
			
			(troop_get_slot, ":original_faction", ":troop_no", slot_troop_original_faction),
			(faction_get_slot, ":culture", ":original_faction", slot_faction_culture),
			
			(faction_get_slot, ":template_troop", ":culture", slot_faction_template_troops_begin),
			
			(val_clamp, ":new_rank", 0, 8),
			
			(troop_set_slot, ":troop_no", slot_troop_level, ":new_rank"),
			
			(val_add, ":template_troop", ":new_rank"),
			
			# Removing old equipment
			(try_for_range, ":equip_slot", ek_item_0, ek_food),
				(troop_get_inventory_slot, ":item", ":troop_no", ":equip_slot"),
				(gt, ":item", 0),
				(troop_remove_item, ":troop_no", ":item"),
			(try_end),
			# Following does not remove equipped items
			(troop_clear_inventory, ":troop_no"),
			
			# New stats
			(call_script, "script_troop_change_stat_with_template", ":troop_no", ":template_troop"),
			# New equipments
			(call_script, "script_troop_change_equipement_with_template", ":troop_no", ":template_troop"),
			(troop_equip_items, ":troop_no"),
		]),
	
	# script_troop_update_name
	# input:
	# 	arg1: troop_no
	# output: none
	("troop_update_name",
		[
			(store_script_param, ":troop_no", 1),
			
			(store_troop_faction, ":faction", ":troop_no"),
			(faction_get_slot, ":culture", ":faction", slot_faction_culture),
			(troop_get_slot, ":new_rank", ":troop_no", slot_troop_rank),
			
			(faction_get_slot, ":faction_name_begin", ":culture", slot_faction_lord_name_begin),
			(store_add, ":lord_name", ":faction_name_begin", ":new_rank"),
			(str_store_troop_name_plural, s0, ":troop_no"),
			
			(troop_get_slot, ":party", ":troop_no", slot_troop_leaded_party),
			(try_begin),
				(gt, ":party", 0),
				(str_store_string, s10, ":lord_name"),
				(party_set_name, ":party", "@{s10}'s Party"),
			(try_end),
			
			(troop_set_name, ":troop_no", ":lord_name"),
		]),
	
	# script_troop_change_stat_with_template
	# input:
	# 	arg1: troop_no
	# 	arg2: template
	# output: none
	("troop_change_stat_with_template",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":template", 2),
			
			(try_for_range, ":stat", ca_strength, 4),
				(store_attribute_level, ":template_stat", ":template", ":stat"),
				(store_attribute_level, ":troop_stat", ":troop_no", ":stat"),
				
				(store_sub, ":difference", ":template_stat", ":troop_stat"),
				(troop_raise_attribute, ":troop_no", ":stat", ":difference"),
			(try_end),
			
			(try_for_range, ":skill", skl_trade, skl_reserved_14), # Do we need to go through all skills?
				(store_skill_level, ":template_skill", ":skill", ":template"),
				(store_skill_level, ":troop_skill", ":skill", ":troop_no"),
				
				(store_sub, ":difference", ":template_skill", ":troop_skill"),
				(troop_raise_skill, ":troop_no", ":skill", ":difference"),
			(try_end),
			
			(try_for_range, ":wp", wpt_one_handed_weapon, wpt_firearm),
				(store_proficiency_level, ":template_wp", ":template", ":wp"),
				(store_proficiency_level, ":troop_wp", ":troop_no", ":wp"),
				
				(store_sub, ":difference", ":template_wp", ":troop_wp"),
				(troop_raise_proficiency_linear, ":troop_no", ":wp", ":difference"),
			(try_end),
		]),
	
	# script_troop_change_equipement_with_template
	# input:
	# 	arg1: troop_no
	# 	arg2: template
	# output: none
	("troop_change_equipement_with_template",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":template", 2),
			
			# (troop_get_slot, ":equip_type", ":troop_no", slot_troop_lord_equipement),
			# (call_script, "script_troop_get_lord_horse_slot", ":troop_no"),
			# (assign, ":horse", reg0),
			
			(troop_clear_inventory, "trp_temp_equipement_troop"),
			(call_script, "script_troop_change_equipement_primary_with_template", ":troop_no", ":template"),
			
			(troop_clear_inventory, "trp_temp_equipement_troop"),
			(call_script, "script_troop_change_equipement_secondary_with_template", ":troop_no", ":template"),
			
			(troop_clear_inventory, "trp_temp_equipement_troop"),
			(call_script, "script_troop_change_equipement_head_with_template", ":troop_no", ":template"),
			
			(troop_clear_inventory, "trp_temp_equipement_troop"),
			(call_script, "script_troop_change_equipement_feet_with_template", ":troop_no", ":template"),
			
			(troop_clear_inventory, "trp_temp_equipement_troop"),
			(call_script, "script_troop_change_equipement_body_with_template", ":troop_no", ":template"),
			
			(troop_clear_inventory, "trp_temp_equipement_troop"),
			(call_script, "script_troop_change_equipement_hands_with_template", ":troop_no", ":template"),
			
			(troop_clear_inventory, "trp_temp_equipement_troop"),
			(call_script, "script_troop_change_equipement_horse_with_template", ":troop_no", ":template"),
			
			(troop_clear_inventory, "trp_temp_equipement_troop"),
			(call_script, "script_troop_change_equipement_shield_with_template", ":troop_no", ":template"),
		]),
		
	# script_troop_change_equipement_primary_with_template
	# input:
	# 	arg1: troop_no
	# 	arg2: template
	# output:
	# 	reg0: item_added
	("troop_change_equipement_primary_with_template",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":template", 2),
			
			# (troop_get_slot, ":equip_type", ":troop_no", slot_troop_lord_equipement),
			(call_script, "script_troop_get_lord_horse_slot", ":troop_no"),
			(assign, ":horse", reg0),
			
			(troop_get_inventory_capacity, ":num_slots", ":template"),
			(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
				(troop_get_inventory_slot, ":cur_item", ":template", ":i_slot"),
				(gt, ":cur_item", 0),
				(item_get_type, ":item_type", ":cur_item"),
				(assign, ":continue", 0),
				(try_begin),
					(this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
					(eq, ":item_type", itp_type_two_handed_wpn),
					(assign, ":continue", 1),
				(else_try),
					(eq, ":item_type", itp_type_polearm),
					(try_begin),
						(ge, ":horse", 1),
						(neg|is_between, ":cur_item", "itm_long_bardiche", "itm_torch"),
						(neg|is_between, ":cur_item", "itm_bamboo_spear", "itm_hafted_blade_a"),
						(assign, ":continue", 1),
					(else_try),
						(eq, ":horse", 0),
						(is_between, ":cur_item", "itm_long_bardiche", "itm_torch"),
						(assign, ":continue", 1),
					(try_end),
				(try_end),
				(eq, ":continue", 1),
				(troop_add_item, "trp_temp_equipement_troop", ":cur_item", 0),
			(try_end),
			(call_script, "script_troop_take_random_troop_equipement", ":troop_no", "trp_temp_equipement_troop"),
		]),
	
	# script_troop_change_equipement_secondary_with_template
	# input:
	# 	arg1: troop_no
	# 	arg2: template
	# output:
	# 	reg0: item_added
	# 	reg1: item_added_2
	("troop_change_equipement_secondary_with_template",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":template", 2),
			
			(troop_get_slot, ":equip_type", ":troop_no", slot_troop_lord_equipement),
			(call_script, "script_troop_get_lord_horse_slot", ":troop_no"),
			(assign, ":horse", reg0),
			
			(troop_get_inventory_capacity, ":num_slots", ":template"),
			(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
				(troop_get_inventory_slot, ":cur_item", ":template", ":i_slot"),
				(gt, ":cur_item", 0),
				(item_get_type, ":item_type", ":cur_item"),
				(assign, ":continue", 0),
				
				(try_begin),
					# (eq, ":item_type", itp_type_polearm),
					(eq, ":equip_type", tle_polearm),
					(ge, ":horse", 1),
					(is_between, ":cur_item", "itm_bamboo_spear", "itm_hafted_blade_a"),
					(assign, ":continue", 1),
				(else_try),
					(eq, ":item_type", itp_type_bow),
					(this_or_next|eq, ":equip_type", tle_light_bow),
					(eq, ":equip_type", tle_heavy_bow),
					(assign, ":continue", 1),
					(call_script, "script_troop_take_first_troop_equipement_of_type", ":troop_no", ":template", itp_type_arrows),
					(assign, reg1, reg0),
				(else_try),
					(eq, ":item_type", itp_type_crossbow),
					(this_or_next|eq, ":equip_type", tle_light_crossbow),
					(eq, ":equip_type", tle_heavy_crossbow),
					(assign, ":continue", 1),
					(call_script, "script_troop_take_first_troop_equipement_of_type", ":troop_no", ":template", itp_type_bolts),
					(assign, reg1, reg0),
				(else_try),
					(eq, ":item_type", itp_type_thrown),
					(eq, ":equip_type", tle_throwing),
					(assign, ":continue", 1),
				(try_end),
				
				(eq, ":continue", 1),
				(troop_add_item, "trp_temp_equipement_troop", ":cur_item", 0),
			(try_end),
			(call_script, "script_troop_take_random_troop_equipement", ":troop_no", "trp_temp_equipement_troop"),
		]),
	
	# script_troop_change_equipement_head_with_template
	# input:
	# 	arg1: troop_no
	# 	arg2: template
	# output:
	# 	reg0: item_added
	("troop_change_equipement_head_with_template",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":template", 2),
			
			# (troop_get_slot, ":equip_type", ":troop_no", slot_troop_lord_equipement),
			# (call_script, "script_troop_get_lord_horse_slot", ":troop_no"),
			# (assign, ":horse", reg0),
			
			(troop_get_inventory_capacity, ":num_slots", ":template"),
			(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
				(troop_get_inventory_slot, ":cur_item", ":template", ":i_slot"),
				(gt, ":cur_item", 0),
				(item_get_type, ":item_type", ":cur_item"),
				(assign, ":continue", 0),
				(try_begin),
					(eq, ":item_type", itp_type_head_armor),
					(assign, ":continue", 1),
				(try_end),
				(eq, ":continue", 1),
				(troop_add_item, "trp_temp_equipement_troop", ":cur_item", 0),
			(try_end),
			(call_script, "script_troop_take_random_troop_equipement", ":troop_no", "trp_temp_equipement_troop"),
		]),
	
	# script_troop_change_equipement_feet_with_template
	# input:
	# 	arg1: troop_no
	# 	arg2: template
	# output:
	# 	reg0: item_added
	("troop_change_equipement_feet_with_template",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":template", 2),
			
			# (troop_get_slot, ":equip_type", ":troop_no", slot_troop_lord_equipement),
			# (call_script, "script_troop_get_lord_horse_slot", ":troop_no"),
			# (assign, ":horse", reg0),
			
			(troop_get_inventory_capacity, ":num_slots", ":template"),
			(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
				(troop_get_inventory_slot, ":cur_item", ":template", ":i_slot"),
				(gt, ":cur_item", 0),
				(item_get_type, ":item_type", ":cur_item"),
				(assign, ":continue", 0),
				(try_begin),
					(eq, ":item_type", itp_type_foot_armor),
					(assign, ":continue", 1),
				(try_end),
				(eq, ":continue", 1),
				(troop_add_item, "trp_temp_equipement_troop", ":cur_item", 0),
			(try_end),
			(call_script, "script_troop_take_random_troop_equipement", ":troop_no", "trp_temp_equipement_troop"),
		]),
	
	# script_troop_change_equipement_body_with_template
	# input:
	# 	arg1: troop_no
	# 	arg2: template
	# output:
	# 	reg0: item_added
	("troop_change_equipement_body_with_template",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":template", 2),
			
			# (troop_get_slot, ":equip_type", ":troop_no", slot_troop_lord_equipement),
			# (call_script, "script_troop_get_lord_horse_slot", ":troop_no"),
			# (assign, ":horse", reg0),
			
			(troop_get_inventory_capacity, ":num_slots", ":template"),
			(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
				(troop_get_inventory_slot, ":cur_item", ":template", ":i_slot"),
				(gt, ":cur_item", 0),
				(item_get_type, ":item_type", ":cur_item"),
				(assign, ":continue", 0),
				(try_begin),
					(eq, ":item_type", itp_type_body_armor),
					(assign, ":continue", 1),
				(try_end),
				(eq, ":continue", 1),
				(troop_add_item, "trp_temp_equipement_troop", ":cur_item", 0),
			(try_end),
			(call_script, "script_troop_take_random_troop_equipement", ":troop_no", "trp_temp_equipement_troop"),
		]),
	
	# script_troop_change_equipement_hands_with_template
	# input:
	# 	arg1: troop_no
	# 	arg2: template
	# output:
	# 	reg0: item_added
	("troop_change_equipement_hands_with_template",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":template", 2),
			
			# (troop_get_slot, ":equip_type", ":troop_no", slot_troop_lord_equipement),
			# (call_script, "script_troop_get_lord_horse_slot", ":troop_no"),
			# (assign, ":horse", reg0),
			
			(troop_get_inventory_capacity, ":num_slots", ":template"),
			(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
				(troop_get_inventory_slot, ":cur_item", ":template", ":i_slot"),
				(gt, ":cur_item", 0),
				(item_get_type, ":item_type", ":cur_item"),
				(assign, ":continue", 0),
				(try_begin),
					(eq, ":item_type", itp_type_hand_armor),
					(assign, ":continue", 1),
				(try_end),
				(eq, ":continue", 1),
				(troop_add_item, "trp_temp_equipement_troop", ":cur_item", 0),
			(try_end),
			(call_script, "script_troop_take_random_troop_equipement", ":troop_no", "trp_temp_equipement_troop"),
		]),
	
	# script_troop_change_equipement_horse_with_template
	# input:
	# 	arg1: troop_no
	# 	arg2: template
	# output:
	# 	reg0: item_added
	("troop_change_equipement_horse_with_template",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":template", 2),
			
			# (troop_get_slot, ":equip_type", ":troop_no", slot_troop_lord_equipement),
			(call_script, "script_troop_get_lord_horse_slot", ":troop_no"),
			(assign, ":horse", reg0),
			
			(troop_get_inventory_capacity, ":num_slots", ":template"),
			(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
				(troop_get_inventory_slot, ":cur_item", ":template", ":i_slot"),
				(gt, ":cur_item", 0),
				(item_get_type, ":item_type", ":cur_item"),
				(assign, ":continue", 0),
				(try_begin),
					(eq, ":item_type", itp_type_horse),
					(ge, ":horse", 1),
					(assign, ":continue", 1),
				(try_end),
				(eq, ":continue", 1),
				(troop_add_item, "trp_temp_equipement_troop", ":cur_item", 0),
			(try_end),
			(call_script, "script_troop_take_random_troop_equipement", ":troop_no", "trp_temp_equipement_troop"),
		]),
	
	# script_troop_change_equipement_shield_with_template
	# input:
	# 	arg1: troop_no
	# 	arg2: template
	# output:
	# 	reg0: item_added
	("troop_change_equipement_shield_with_template",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":template", 2),
			
			# (troop_get_slot, ":equip_type", ":troop_no", slot_troop_lord_equipement),
			(call_script, "script_troop_get_lord_horse_slot", ":troop_no"),
			(assign, ":horse", reg0),
			
			(troop_get_inventory_capacity, ":num_slots", ":template"),
			(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
				(troop_get_inventory_slot, ":cur_item", ":template", ":i_slot"),
				(gt, ":cur_item", 0),
				(item_get_type, ":item_type", ":cur_item"),
				(assign, ":continue", 0),
				(try_begin),
					(eq, ":item_type", itp_type_shield),
					(try_begin),
						(is_between, ":cur_item", "itm_tab_shield_kite_a", "itm_tab_shield_pavise_a"),
						(gt, ":horse", 0),
					(else_try),
						(is_between, ":cur_item", "itm_tab_shield_heater_cav_a", "itm_stones"),
						(lt, ":horse", 1),
					(else_try),
						(assign, ":continue", 1),
					(try_end),
				(try_end),
				(eq, ":continue", 1),
				(troop_add_item, "trp_temp_equipement_troop", ":cur_item", 0),
			(try_end),
			(call_script, "script_troop_take_random_troop_equipement", ":troop_no", "trp_temp_equipement_troop"),
			# Shields are not added if they are not of the right kind
			# As a side note, rhodok pavise shield is considered an infantry and cavalry shield
			# this is made so that rhodok lords will use them most of the time
		]),
	
	# script_troop_take_random_troop_equipement
	# input:
	# 	arg1: troop_no
	# 	arg2: template_troop
	# output:
	# 	reg0: item_added
	("troop_take_random_troop_equipement",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":temp_troop", 2),
			
			(assign, ":item", -1),
			
			(assign, ":num_items", 0),
			(troop_get_inventory_capacity, ":num_slots", ":temp_troop"),
			(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
				(troop_get_inventory_slot, ":cur_item", ":temp_troop", ":i_slot"),
				(gt, ":cur_item", 0),
				(val_add, ":num_items", 1),
			(try_end),
			
			(store_random_in_range, ":random", 0, ":num_items"),
			
			(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
				(troop_get_inventory_slot, ":cur_item", ":temp_troop", ":i_slot"),
				(gt, ":cur_item", 0),
				(try_begin),
					(eq, ":random", 0),
					(assign, ":item", ":cur_item"),
					(troop_add_item, ":troop_no", ":cur_item", 0),
					(assign, ":num_slots", 0),
				(try_end),
				(val_add, ":random", -1),
			(try_end),
			
			(assign, reg0, ":item"),
		]),
	
	# script_troop_take_first_troop_equipement_of_type
	# input:
	# 	arg1: troop_no
	#	arg2: template_troop
	# 	arg3: item_type
	# output:
	# 	reg0: item_added
	("troop_take_first_troop_equipement_of_type",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":temp_troop", 2),
			(store_script_param, ":item_type", 3),
			
			(assign, ":found", 0),
			(troop_get_inventory_capacity, ":num_slots", ":temp_troop"),
			(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
				(troop_get_inventory_slot, ":cur_item", ":temp_troop", ":i_slot"),
				(gt, ":cur_item", 0),
				(item_get_type, ":cur_item_type", ":cur_item"),
				(eq, ":cur_item_type", ":item_type"),
				(troop_add_item, ":troop_no", ":cur_item", 0),
				(assign, ":num_slots", 0),
				(assign, ":found", ":cur_item"),
			(try_end),
			
			(assign, reg0, ":found"),
		]),
	
	# script_troop_take_random_troop_equipement_of_type
	# input:
	# 	arg1: troop_no
	#	arg2: template_troop
	# 	arg3: item_type
	# output:
	# 	reg0: item_added
	("troop_take_random_troop_equipement_of_type",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":temp_troop", 2),
			(store_script_param, ":item_type", 3),
			
			(assign, ":found", 0),
			(troop_get_inventory_capacity, ":num_slots", ":temp_troop"),
			(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
				(troop_get_inventory_slot, ":cur_item", ":temp_troop", ":i_slot"),
				(gt, ":cur_item", 0),
				(item_get_type, ":cur_item_type", ":cur_item"),
				(eq, ":cur_item_type", ":item_type"),
				(val_add, ":found", 1),
			(try_end),
			
			(try_begin),
				(gt, ":found", 0),
				(store_random_in_range, ":random_equipement", 0, ":found"),
				
				(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
					(troop_get_inventory_slot, ":cur_item", ":temp_troop", ":i_slot"),
					(gt, ":cur_item", 0),
					(item_get_type, ":cur_item_type", ":cur_item"),
					(eq, ":cur_item_type", ":item_type"),
					
					(try_begin),
						(eq, ":random_equipement", 0),
						(assign, ":found", ":cur_item"),
						(troop_add_item, ":troop_no", ":cur_item", 0),
						(assign, ":num_slots", 0),
					(else_try),
						(val_add, ":random_equipement", -1),
					(try_end),
				(try_end),
			(try_end),
			
			(assign, reg0, ":found"),
		]),
	
	# script_party_get_companion_limit
	# input:
	# 	arg1: party_no
	# output:
	# 	reg0: party_size_limit
	("party_get_companion_limit",
		[
			(store_script_param, ":party_no", 1),
			
			(party_get_slot, ":party_type", ":party_no", slot_party_type),
			(try_begin),
				(this_or_next|eq, ":party_type", spt_war_party),
				(eq, ":party_no", "p_main_party"),
				(party_stack_get_troop_id, ":commander", ":party_no", 0),
				
				(store_attribute_level, ":party_limit", ":commander", ca_charisma),
				
				(val_mul, ":party_limit", 2),
				
				(store_skill_level, ":leadership_bonus", skl_leadership, ":commander"),
				(val_mul, ":leadership_bonus", 25),
				
				(val_add, ":party_limit", ":leadership_bonus"),
			(else_try),
				(eq, ":party_type", spt_town),
				(assign, ":party_limit", garrison_size_town),
			(else_try),
				(eq, ":party_type", spt_castle),
				(assign, ":party_limit", garrison_size_castle),
			(else_try),
				(eq, ":party_type", spt_village),
				(assign, ":party_limit", garrison_size_village),
			(else_try),
				(eq, ":party_type", spt_fort),
				(assign, ":party_limit", garrison_size_fort),
			# (else_try),
				# (party_stack_get_troop_id, ":commander", ":party_no", 0),
				# (ge, ":commander", 0),
				# (store_attribute_level, ":party_limit", ":commander", ca_charisma),
				
				# (val_mul, ":party_limit", 2),
				
				# (store_skill_level, ":leadership_bonus", skl_leadership, ":commander"),
				# (val_mul, ":leadership_bonus", 20),
				
				# (val_add, ":party_limit", ":leadership_bonus"),
			(else_try),
				(assign, ":party_limit", 0),
			(try_end),
			
			(store_faction_of_party, ":faction_no", ":party_no"),
			
			(call_script, "script_faction_get_party_size_modifier", ":faction_no"),
			(assign, ":modifier", reg0),
			
			(val_mul, ":party_limit", ":modifier"),
			(val_div, ":party_limit", 100),
			
			(assign, reg0, ":party_limit"),
		]),
	
	# script_faction_get_party_size_modifier
	# input:
	# 	arg1: faction_no
	# output:
	# 	reg0: size_modifier (percentage)
	("faction_get_party_size_modifier",
		[
			(store_script_param, ":faction_no", 1),
			
			(faction_get_slot, ":peasant_mod", ":faction_no", slot_faction_peasant_num_tries),
			(faction_get_slot, ":common_mod", ":faction_no", slot_faction_common_num_tries),
			(faction_get_slot, ":veteran_mod", ":faction_no", slot_faction_veteran_num_tries),
			(faction_get_slot, ":elite_mod", ":faction_no", slot_faction_elite_num_tries),
			(faction_get_slot, ":noble_mod", ":faction_no", slot_faction_noble_num_tries),
			
			(val_mul, ":peasant_mod", 2),	# +1%
			(val_mul, ":common_mod", 1),	# +0.5%
			(val_mul, ":veteran_mod", -1),	# -0.5%
			(val_mul, ":elite_mod", -2),	# -1%
			(val_mul, ":noble_mod", -3),	# -1.5%
			
			(assign, ":party_size_mod", 200),
			(val_add, ":party_size_mod", ":peasant_mod"),
			(val_add, ":party_size_mod", ":common_mod"),
			(val_add, ":party_size_mod", ":veteran_mod"),
			(val_add, ":party_size_mod", ":elite_mod"),
			(val_add, ":party_size_mod", ":noble_mod"),
			
			(val_div, ":party_size_mod", 2),
			
			(assign, reg0, ":party_size_mod"),
		]),
	
	# script_troop_get_lord_horse_slot
	# input:
	# 	arg1: troop_no
	# output:
	# 	reg0: horse
	("troop_get_lord_horse_slot",
		[
			(store_script_param, ":troop_no", 1),
			
			(troop_get_slot, ":horse", ":troop_no", slot_troop_lord_horse),
			
			# (troop_get_slot, ":original_faction", ":troop_no", slot_troop_original_faction),
			(troop_get_slot, ":rank", ":troop_no", slot_troop_level),
			(try_begin),
				# (eq, ":rank", 5),
				# (store_random_in_range, ":rand", 0, 2),
				# (val_add, ":horse", ":rand"),
			# (else_try),
				(ge, ":rank", 6),
				(assign, ":horse", 1),
			(else_try),
				(eq, ":rank", 0),
				(val_div, ":horse", 3),
			(else_try),
				(le, ":rank", 2),
				(val_div, ":horse", 2),
			(try_end),
			
			(assign, reg0, ":horse"),
		]),
	
	# script_troop_set_equip_type
	# input:
	# 	arg1: troop_no
	# output: none
	("troop_set_equip_type",
		[
			(store_script_param, ":troop_no", 1),
			
			(troop_get_slot, ":original_faction", ":troop_no", slot_troop_original_faction),
			(faction_get_slot, ":culture", ":original_faction", slot_faction_culture),
			
			(store_random_in_range, ":horse", 0, 10),
			(store_random_in_range, ":weapon", 0, 20),
			
			(try_begin),
				(eq, ":culture", "fac_culture_1"),
				(try_begin),
					(eq, ":horse", 0),
					(assign, ":horse", 2),
				(else_try),
					(assign, ":horse", 3),
				(try_end),
				(troop_set_slot, ":troop_no", slot_troop_lord_horse, ":horse"),
				
				(try_begin),
					(eq, ":original_faction", "fac_small_kingdom_11"), # Does not have bows
					(eq, ":weapon", 6),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_light_crossbow),
				(else_try),
					(eq, ":original_faction", "fac_small_kingdom_14"), # Does not have crossbows
					(eq, ":weapon", 7),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_light_bow),
				(else_try),
					(eq, ":original_faction", "fac_small_kingdom_16"), # Has throw
					(is_between, ":weapon", 8, 10),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_throwing),
				(else_try),
					(le, ":weapon", 5),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_polearm),
				(else_try),
					(le, ":weapon", 6),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_light_bow),
				(else_try),
					(le, ":weapon", 7),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_light_crossbow),
				(else_try),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_none),
				(try_end),
			(else_try),
				(eq, ":culture", "fac_culture_2"),
				(try_begin),
					(eq, ":horse", 0),
					# (assign, ":horse", 0),
				(else_try),
					(eq, ":horse", 1),
					(assign, ":horse", 2),
				(else_try),
					(assign, ":horse", 3),
				(try_end),
				(troop_set_slot, ":troop_no", slot_troop_lord_horse, ":horse"),
				
				(try_begin),
					(le, ":weapon", 2),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_polearm),
				(else_try),
					(le, ":weapon", 5),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_light_bow),
				(else_try),
					(le, ":weapon", 10),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_heavy_bow),
				(else_try),
					(le, ":weapon", 12),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_throwing),
				(else_try),
					(eq, ":original_faction", "fac_small_kingdom_24"), # Has more throw
					(le, ":weapon", 15),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_throwing),
				(else_try),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_none),
				(try_end),
			(else_try),
				(eq, ":culture", "fac_culture_3"),
				(try_begin),
					(eq, ":horse", 0),
					(assign, ":horse", 2),
				(else_try),
					(assign, ":horse", 3),
				(try_end),
				(troop_set_slot, ":troop_no", slot_troop_lord_horse, ":horse"),
				
				(try_begin),
					(le, ":weapon", 5),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_polearm),
				(else_try),
					(le, ":weapon", 8),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_light_bow),
				(else_try),
					(le, ":weapon", 13),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_heavy_bow),
				(else_try),
					(le, ":weapon", 14),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_throwing),
				(else_try),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_none),
				(try_end),
			(else_try),
				(eq, ":culture", "fac_culture_4"),
				(val_div, ":horse", 4),
				(val_min, ":horse", 3),
				(troop_set_slot, ":troop_no", slot_troop_lord_horse, ":horse"),
				
				(try_begin),
					(le, ":weapon", 5),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_polearm),
				(else_try),
					(le, ":weapon", 6),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_light_bow),
				(else_try),
					(le, ":weapon", 7),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_heavy_bow),
				(else_try),
					(le, ":weapon", 13),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_throwing),
				(else_try),
					(le, ":weapon", 14),
					(eq, ":original_faction", "fac_small_kingdom_44"),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_light_crossbow),
				(else_try),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_none),
				(try_end),
			(else_try),
				(eq, ":culture", "fac_culture_5"),
				(val_div, ":horse", 3),
				(val_min, ":horse", 3),
				(troop_set_slot, ":troop_no", slot_troop_lord_horse, ":horse"),
				
				(try_begin),
					(le, ":weapon", 8),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_polearm),
				(else_try),
					(le, ":weapon", 12),
					(eq, ":original_faction", "fac_small_kingdom_51"),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_light_bow),
				(else_try),
					(le, ":weapon", 10),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_light_crossbow),
				(else_try),
					(le, ":weapon", 12),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_heavy_crossbow),
				(else_try),
					(le, ":weapon", 13),
					(eq, ":original_faction", "fac_small_kingdom_54"),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_throwing),
				(else_try),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_none),
				(try_end),
			(else_try),
				(eq, ":culture", "fac_culture_6"),
				(try_begin),
					(eq, ":horse", 0),
					(assign, ":horse", 2),
				(else_try),
					(assign, ":horse", 3),
				(try_end),
				(troop_set_slot, ":troop_no", slot_troop_lord_horse, ":horse"),
				
				(try_begin),
					(le, ":weapon", 3),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_polearm),
				(else_try),
					(le, ":weapon", 4),
					(eq, ":original_faction", "fac_small_kingdom_61"),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_light_crossbow),
				(else_try),
					(le, ":weapon", 7),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_light_bow),
				(else_try),
					(le, ":weapon", 13),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_throwing),
				(else_try),
					(troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_none),
				(try_end),
			(try_end),
		]),
		
	# script_scene_get_spawn_range
	# input:
	# 	arg1: team_no
	# output:
	#	reg0: range_begin
	# 	reg1: range_end
	("scene_get_spawn_range",
		[
			(store_script_param, ":team_no", 1),
			
			(store_current_scene, ":cur_scene"),
			
			# (team_get_slot, ":battle_phase", ":team_no", slot_team_battle_phase),
			
			(try_begin),
				(eq, ":team_no", 0),
				(assign, reg0, 1), # One spawn for defenders
				(assign, reg1, 2),
			(else_try),
				(scene_get_slot, ":end", ":cur_scene", slot_scene_num_attack_spawn),
				(assign, reg0, siege_attack_spawn_begin),
				(store_add, reg1, reg0, ":end"),
			(try_end),
		]),
	
	# script_scene_get_archer_points_range
	# input: none
	# output:
	#	reg0: range_begin
	# 	reg1: range_end
	("scene_get_archer_points_range",
		[
			(store_current_scene, ":cur_scene"),
			(assign, ":begin", siege_archer_points_begin),
			(assign, ":end", ":begin"),
			
			(scene_get_slot, ":num_points", ":cur_scene", slot_scene_num_archer_points),
			(val_add, ":end", ":num_points"),
			(assign, reg0, ":begin"),
			(assign, reg1, ":end"),
		]),
	
	# script_scene_get_defend_points_range
	# input: none
	# output:
	#	reg0: range_begin
	# 	reg1: range_end
	("scene_get_defend_points_range",
		[
			(store_current_scene, ":cur_scene"),
			(assign, ":begin", siege_defend_points_begin),
			(assign, ":end", ":begin"),
			
			(scene_get_slot, ":num_points", ":cur_scene", slot_scene_num_defend_points),
			(val_add, ":end", ":num_points"),
			(assign, reg0, ":begin"),
			(assign, reg1, ":end"),
		]),
	
	# script_init_siege_scene_slots
	# input: none
	# output: none
	("init_siege_scene_slots",
		[
			(scene_set_slot, "scn_castle_01_outside", slot_scene_num_defend_points, 2),
			(scene_set_slot, "scn_castle_01_outside", slot_scene_num_attack_spawn, 2),
			(scene_set_slot, "scn_castle_01_outside", slot_scene_num_archer_points, 7),
			
			(scene_set_slot, "scn_castle_02_outside", slot_scene_num_defend_points, 2),
			(scene_set_slot, "scn_castle_02_outside", slot_scene_num_attack_spawn, 2),
			(scene_set_slot, "scn_castle_02_outside", slot_scene_num_archer_points, 12),
			
			(scene_set_slot, "scn_castle_03_outside", slot_scene_num_defend_points, 2),
			(scene_set_slot, "scn_castle_03_outside", slot_scene_num_attack_spawn, 2),
			(scene_set_slot, "scn_castle_03_outside", slot_scene_num_archer_points, 8),
			
			(scene_set_slot, "scn_castle_04_outside", slot_scene_num_defend_points, 2),
			(scene_set_slot, "scn_castle_04_outside", slot_scene_num_attack_spawn, 2),
			(scene_set_slot, "scn_castle_04_outside", slot_scene_num_archer_points, 9),
			
			(scene_set_slot, "scn_castle_05_outside", slot_scene_num_defend_points, 2),
			(scene_set_slot, "scn_castle_05_outside", slot_scene_num_attack_spawn, 2),
			(scene_set_slot, "scn_castle_05_outside", slot_scene_num_archer_points, 9),
		]),
	
	# script_set_team_defend_points
	# input: none
	# output: none
	("set_team_defend_points",
		[
			(call_script, "script_scene_get_defend_points_range"),
			(assign, ":defend_begin", reg0),
			(assign, ":defend_end", reg1),
			
			# (store_sub, ":num_defend", ":defend_end", ":defend_begin"),
			(assign, ":cur_division", 2),
			(try_for_range, ":cur_defend", ":defend_begin", ":defend_end"),
				(team_give_order, 0, ":cur_division", mordr_hold),
				(entry_point_get_position, pos0, ":cur_defend"),
				(team_set_order_position, 0, ":cur_division", pos0),
				(val_add, ":cur_division", 1),
			(try_end),
		]),
	
	# script_spawn_lord
	# input:
	# 	arg1: troop_no
	# output: none
	("spawn_lord",
		[
			(store_script_param, ":troop_no", 1),
			
			(call_script, "script_troop_get_home", ":troop_no", 1),
			(assign, ":home", reg0),
			
			# (store_troop_faction, ":troop_faction", ":troop_no"),
			# (store_faction_of_party, ":party_faction", ":home"),
			
			# (try_begin),
				# (this_or_next|le, ":home", 0),
				# (neq, ":troop_faction", ":party_faction"),
				
				# (call_script, "script_troop_update_home", ":troop_no"),
			# (try_end),
			
			(call_script, "script_spawn_party_around_party", ":home", "pt_war_party"),
			(assign, ":party", reg0),
			
			(party_set_flags, ":party", pf_show_faction, 1),
			
			(party_add_leader, ":party", ":troop_no"),
			
			(party_set_slot, ":party", slot_party_leader, ":troop_no"),
			(troop_set_slot, ":troop_no", slot_troop_leaded_party, ":party"),
			
			(party_set_slot, ":party", slot_party_type, spt_war_party),
			
			(call_script, "script_party_set_behavior", ":party", tai_traveling_to_party, ":home"),
			
			(str_store_troop_name, s10, ":troop_no"),
			(party_set_name, ":party", "@{s10}'s Party"),
		]),
	
	# script_cf_lord_can_spawn
	# input:
	# 	arg1: troop_no
	# output: none
	("cf_lord_can_spawn",
		[
			(store_script_param, ":troop_no", 1),
			(call_script, "script_troop_get_home", ":troop_no", 1),
			(assign, ":home", reg0),
			
			(ge, ":home", towns_begin),
			# ToDo:
		]),
	
	# script_troop_update_home
	# input:
	# 	arg1: troop_no
	# output:
	# 	reg0: new_home
	("troop_update_home",
		[
			(store_script_param, ":troop_no", 1),
			
			(assign, ":home", -1),
			
			(store_troop_faction, ":troop_faction", ":troop_no"),
			
			(assign, ":first_center", -1),
			
			(assign, ":end", castles_end),
			# Take first owned center (towns first)
			(try_for_range, ":cur_center", towns_begin, ":end"),
				(try_begin),
					(party_slot_eq, ":cur_center", slot_party_lord, ":troop_no"),
				
					(assign, ":home", ":cur_center"),
					(assign, ":end", 0),
				(else_try),
					(eq, ":first_center", -1),
					# We take the first center of this faction in case the capital has been taken
					(store_faction_of_party, ":party_faction", ":cur_center"),
					(eq, ":party_faction", ":troop_faction"),
					(assign, ":first_center", ":cur_center"),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":home", -1),
				# Then check villages
				(assign, ":end", villages_end),
				(try_for_range, ":cur_center", villages_begin, ":end"),
					(party_slot_eq, ":cur_center", slot_party_lord, ":troop_no"),
					
					(assign, ":home", ":cur_center"),
					# (party_get_slot, ":home", ":cur_center", slot_party_linked_party),
					(assign, ":end", 0),
				(try_end),
				(try_begin),
					(eq, ":home", -1),
					# If lord has no home, we take his leader's home
					(faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
					(try_begin),
						(ge, ":faction_leader", 0),
						
						(call_script, "script_troop_get_home", ":faction_leader", 1),
						(assign, ":home", reg0),
					(try_end),
					
					(try_begin),
						(le, ":home", 0),
						(assign, ":home", ":first_center"),
					(try_end),
				(try_end),
			(try_end),
			
			
			(troop_set_slot, ":troop_no", slot_troop_home, ":home"),
			(assign, reg0, ":home"),
		]),
	
	# script_party_process_ai
	# input:
	# 	arg1: party_no
	# output: none
	("party_process_ai",
		[
			(store_script_param, ":party_no", 1),
			(party_get_slot, ":leader", ":party_no", slot_party_leader),
			
			(troop_get_slot, ":current_behavior", ":leader", slot_troop_behavior),
			(troop_get_slot, ":current_object", ":leader", slot_troop_behavior_object),
			
			(get_party_ai_behavior, ":party_behavior", ":party_no"),
			(get_party_ai_object, ":party_object", ":party_no"),
			
			(try_begin),
				(eq,":party_behavior", ai_bhvr_avoid_party),
				(store_faction_of_party, ":party_faction", ":party_no"),
				(assign, ":best_center", -1),
				(assign, ":best_score", 9999),
				(try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
					(store_faction_of_party, ":center_faction", ":cur_center"),
					(store_relation, ":rel", ":center_faction", ":party_faction"),
					(this_or_next|eq,":center_faction", ":party_faction"),
					(ge, ":rel", relation_neutral),
					(store_distance_to_party_from_party, ":dist", ":cur_center", ":party_no"),
					(store_distance_to_party_from_party, ":dist_with_object", ":cur_center", ":party_object"),
					(val_mul, ":dist_with_object", 2),
					(val_div,":dist_with_object", 3),
					(lt, ":dist", ":dist_with_object"),
					
					(try_begin), #Own faction centers are better candidates
						(eq,":center_faction", ":party_faction"),
						(val_mul,":dist", 10),
					(else_try),
						(val_mul,":dist", 11),
					(try_end),
					
					(lt, ":dist", ":best_score"),
					(assign, ":best_center", ":cur_center"),
					(assign, ":best_score", ":dist"),
				(try_end),
				(try_begin),
					(gt, ":best_center", -1),
					(party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
					(party_set_ai_object, ":party_no", ":best_center"),
				(try_end),
			(else_try),
				(eq, ":current_behavior", tai_accompanying_party),
				(party_is_active, ":current_object"),
				
				(try_begin),
					(party_get_battle_opponent, ":opponent", ":current_object"),
					(ge, ":opponent", 0),
					
					(party_get_battle_opponent, ":own_opponent", ":party_no"),
					(eq, ":own_opponent", -1),
					
					(party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
					(party_set_ai_object, ":party_no", ":opponent"),
				(try_end),
			(else_try),
				(eq, ":current_behavior", tai_attacking_center),
				(store_distance_to_party_from_party, ":dist", ":party_no", ":current_object"),
				(try_begin),
					(lt, ":dist", 6),
					(try_begin),
						(neg|party_slot_eq, ":current_object", slot_party_besieged_by, ":party_no"),
						(party_set_slot, ":current_object", slot_party_besieged_by, ":party_no"),
					(try_end),
					(party_get_slot, ":party_type", ":current_object", slot_party_type),
					(try_begin),
						(this_or_next|eq, ":party_type", spt_town),
						(this_or_next|eq, ":party_type", spt_castle),
						(eq, ":party_type", spt_village),
						
						(try_begin),
							(party_get_battle_opponent, ":own_opponent", ":party_no"),
							(eq, ":own_opponent", -1),

							(store_random_in_range, ":random", 0, 10),
							(eq, ":random", 0),
							(party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
							(party_set_ai_object, ":party_no", ":current_object"),
						(try_end),
					# (else_try),
						# (eq, ":party_type", spt_village),
						# (store_random_in_range, ":random", 0, 10),
						# (try_begin),
							# (eq, ":random", 0),
							# (party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
							# (party_set_ai_object, ":party_no", ":current_object"),
						# (try_end),
					(else_try),
						(str_store_party_name, s10, ":current_object"),
						(display_message, "@Incorrect besieged party: {s10}"),
					(try_end),
				(try_end),
			(try_end),
		]),
	
	# script_party_process_mission
	# input:
	# 	arg1: party_no
	# output: none
	("party_process_mission",
		[
			(store_script_param, ":party_no", 1),
			
			(party_get_slot, ":leader", ":party_no", slot_party_leader),
			
			(party_get_num_companions, ":num_troops", ":party_no"),
			(call_script, "script_party_get_companion_limit", ":party_no"),
			(assign, ":party_limit", reg0),
			
			(call_script, "script_troop_get_home", ":leader", 1),
			(assign, ":home", reg0),
			
			# (get_party_ai_behavior, ":current_behavior", ":party_no"),
			# (get_party_ai_object, ":current_object", ":party_no"),
			
			(troop_get_slot, ":current_behavior", ":leader", slot_troop_behavior),
			(troop_get_slot, ":current_object", ":leader", slot_troop_behavior_object),
			
			(store_faction_of_party, ":party_faction", ":party_no"),
			
			(troop_get_slot, ":liege", ":leader", slot_troop_vassal_of),
			(try_begin),
				(lt, ":liege", 0),
				(faction_get_slot, ":liege", ":party_faction", slot_faction_leader),
			(try_end),
			
			(troop_get_slot, ":rank", ":leader", slot_troop_rank),
			
			(troop_get_slot, ":mission", ":leader", slot_troop_mission),
			(assign, ":new_mission", 0),
			
			(party_get_attached_to, ":attached_to", ":party_no"),
			
			(troop_get_slot, ":num_vassals", ":leader", slot_troop_num_vassal),
			
			(try_begin),
				(party_get_battle_opponent, ":opponent", ":party_no"),
				(ge, ":opponent", 0),
				# If fighting, do nothing else
			(else_try),
				# Get reinforcements
				(lt, ":num_troops", ":party_limit"),
				(assign, ":stop", 0),
				(try_begin),
					(eq, ":current_object", ":home"),
					(this_or_next|eq, ":current_behavior", tai_traveling_to_party),
					(eq, ":attached_to", ":home"),
					(assign, ":stop", 1),
				(else_try),
					(store_div, ":lower_party_limit", ":party_limit", 3),
					(this_or_next|lt, ":num_troops", ":lower_party_limit"),
					(neg|faction_slot_ge, ":party_faction", slot_faction_is_at_war, 1),
					(try_begin),
						(is_between, ":attached_to", walled_centers_begin, walled_centers_end),
						(lt, ":num_troops", ":lower_party_limit"),
					(else_try),
						(call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_party, ":home"),
					(try_end),
					(assign, ":stop", 1),
				(try_end),
				(eq, ":stop", 1),
			(else_try),
				# Defending territory
				(eq, ":mission", tm_defending),
				(store_random_in_range, ":random", 0, 20),
				(try_begin),
					(eq, ":random", 0),
					(call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_party, ":home"),
				(else_try),
					(assign, ":new_mission", tm_defending),
				(try_end),
			(else_try),
				(eq, ":mission", tm_attacking),
				(try_begin),
					(store_faction_of_party, ":object_faction", ":current_object"),
					(store_relation, ":relation", ":object_faction", ":party_faction"),
					(this_or_next|eq, ":object_faction", ":party_faction"),
					(gt, ":relation", relation_bad),
					(call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_party, ":home"),
				(else_try),
					(assign, ":new_mission", tm_attacking),
				(try_end),
			(else_try),
				# Gathering army
				(eq, ":mission", tm_gathering_army),
				(store_random_in_range, ":random", 0, 10),
				(try_begin),
					(eq, ":random", 0),
					(assign, ":new_mission", tm_defending),
					(call_script, "script_party_set_behavior", ":party_no", tai_patroling_center, ":home"),
				(else_try),
					(eq, ":random", 1),
					(call_script, "script_faction_find_nearest_enemy_center", ":party_faction", ":home", spt_village),
					(assign, ":enemy_center", reg0),
					(gt, ":enemy_center", 0),
					(assign, ":new_mission", tm_attacking),
					(call_script, "script_party_set_behavior", ":party_no", tai_attacking_center, ":enemy_center"),
				(else_try),
					(eq, ":random", 2),
					(ge, ":rank", rank_city),
					(call_script, "script_faction_find_nearest_enemy_center", ":party_faction", ":home", spt_town),
					(assign, ":enemy_center", reg0),
					(gt, ":enemy_center", 0),
					(assign, ":new_mission", tm_attacking),
					(call_script, "script_party_set_behavior", ":party_no", tai_attacking_center, ":enemy_center"),
				(else_try),
					(assign, ":new_mission", tm_gathering_army),
				(try_end),
			(else_try),
				# Gather the vassals
				(eq, ":mission", 0),
				(ge, ":rank", rank_castle),
				(faction_slot_ge, ":party_faction", slot_faction_is_at_war, 1),
				(gt, ":num_vassals", 0),
				(store_random_in_range, ":random", 0, 20),
				(eq, ":random", 0),
				(call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_point, ":home"),
				(assign, ":new_mission", tm_gathering_army),
			(else_try),
				# Follow liege (king or superior lord)
				(ge, ":liege", 0),
				(call_script, "script_decide_follow_or_not", ":leader", ":liege"),
				(eq, reg0, 1), # Follow
				(troop_get_slot, ":liege_party", ":liege", slot_troop_leaded_party),
				(call_script, "script_party_set_behavior", ":party_no", tai_accompanying_party, ":liege_party"),
			(else_try),
				# Patrol home center
				(call_script, "script_party_set_behavior", ":party_no", ai_bhvr_patrol_location, ":home"),
			(try_end),
			
			(troop_set_slot, ":leader", slot_troop_mission, ":new_mission"),
		]),
	
	# script_faction_find_nearest_enemy_center
	# input:
	# 	arg1: faction_no
	# 	arg2: party
	# 	arg2: party_type
	# output:
	# 	reg0: enemy_center
	("faction_find_nearest_enemy_center",
		[
			(store_script_param, ":faction_no", 1),
			(store_script_param, ":party", 2),
			(store_script_param, ":party_type", 3),
			
			(assign, ":best_center", -1),
			(assign, ":best_distance", 9999),
			
			(try_begin),
				(eq, ":party_type", spt_village),
				(try_for_range, ":center_no", villages_begin, villages_end),
					(store_faction_of_party, ":center_faction", ":center_no"),
					(store_relation, ":relation", ":center_faction", ":faction_no"),
					(lt, ":relation", relation_war),
					(store_distance_to_party_from_party, ":distance", ":party", ":center_no"),
					(lt, ":distance", ":best_distance"),
					(assign, ":best_distance", ":distance"),
					(assign, ":best_center", ":center_no"),
				(try_end),
			(else_try),
				# (ge, ":party_type", spt_castle),
				(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
					(store_faction_of_party, ":center_faction", ":center_no"),
					(store_relation, ":relation", ":center_faction", ":faction_no"),
					(lt, ":relation", relation_war),
					(store_distance_to_party_from_party, ":distance", ":party", ":center_no"),
					(lt, ":distance", ":best_distance"),
					(assign, ":best_distance", ":distance"),
					(assign, ":best_center", ":center_no"),
				(try_end),
			(try_end),
			
			(assign, reg0, ":best_center"),
		]),
	
	# script_decide_follow_or_not
	# input:
	# 	arg1: troop_no
	# 	arg2: troop_to_follow
	# output:
	# 	reg0: follow (1: yes, 0: no)
	("decide_follow_or_not",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":troop_to_follow", 2),
			
			(assign, ":follow", 0),
			
			(troop_get_slot, ":party_to_follow", ":troop_to_follow", slot_troop_leaded_party),
			
			(try_begin),
				(ge, ":party_to_follow", 0),
				
				(try_begin),
					(troop_slot_eq, ":troop_no", slot_troop_behavior, tai_accompanying_party),
					(troop_slot_eq, ":troop_no", slot_troop_behavior_object, ":troop_to_follow"),
					
					(assign, ":follow", 1),
				(else_try),
					(troop_slot_ge, ":troop_to_follow", slot_troop_mission, 1), # Has a mission
					(assign, ":follow", 1),
				(else_try),
					(troop_slot_eq, ":troop_to_follow", slot_troop_behavior, tai_accompanying_party),
					(neg|troop_slot_eq, ":troop_to_follow", slot_troop_behavior_object, ":troop_no"),
					(assign, ":follow", 1),
				(try_end),
			(try_end),
			
			(assign, reg0, ":follow"),
		]),
	
	# script_party_does_center_buisness
	# input:
	# 	arg1: party_no
	# 	arg2: cur_town
	# output: none
	("party_does_center_buisness",
		[
			(store_script_param, ":party_no", 1),
			(store_script_param, ":cur_town", 2),
			
			(call_script, "script_party_get_companion_limit", ":party_no"),
			(assign, ":limit", reg0),
			
			(party_get_num_companions, ":num_troops", ":party_no"),
			(try_begin),
				(lt, ":num_troops", ":limit"),
				
				(store_sub, ":num_max", ":limit", ":num_troops"),
				
				(party_get_num_companions, ":num_reinforcements", ":cur_town"),
				(call_script, "script_party_get_companion_limit", ":cur_town"),
				(store_div, ":center_limit", reg0, 3),
				(gt, ":num_reinforcements", ":center_limit"), # Do not give troops if not enough men in the center
				
				(party_get_slot, ":leader", ":party_no", slot_party_leader),
				
				(val_div, ":num_reinforcements", 20),
				(try_begin),
					(neg|party_slot_eq, ":cur_town", slot_party_lord, ":leader"),
					(val_div, ":num_reinforcements", 2),
				(try_end),
				(val_add, ":num_reinforcements", 2),
				
				(val_min, ":num_reinforcements", 16),
				(val_min, ":num_reinforcements", ":num_max"),
				(gt, ":num_reinforcements", 0),
				(call_script, "script_party_give_troops_to_party", ":cur_town", ":party_no", ":num_reinforcements", -1),
				# (assign, ":num_added", reg0),
				# ToDo: remove gold
			(try_end),
		]),
	
	# script_party_set_behavior
	# input:
	# 	arg1: party_no
	# 	arg2: behavior
	# 	arg3: object
	# output: none
	("party_set_behavior",
		[
			(store_script_param, ":party_no", 1),
			(store_script_param, ":behavior", 2),
			(store_script_param, ":object", 3),
			
			(party_get_attached_to, ":attached", ":party_no"),
			(try_begin),
				(ge, ":attached", 0),
				(party_detach, ":party_no"),
			(try_end),
			
			(party_get_slot, ":leader", ":party_no",  slot_party_leader),
			(troop_set_slot, ":leader", slot_troop_behavior, ":behavior"),
			(troop_set_slot, ":leader", slot_troop_behavior_object, ":object"),
			
			(try_begin),
				(eq, ":behavior", tai_patroling_center),
				(assign, ":behavior", ai_bhvr_patrol_party),
				(party_set_ai_patrol_radius, ":party_no", 3),
				(assign, ":courage", 10),
				(assign, ":aggressiveness", 5),
				(assign, ":help", 200),
			(else_try),
				(eq, ":behavior", tai_patroling_party),
				(assign, ":behavior", ai_bhvr_patrol_location),
				(party_set_ai_patrol_radius, ":party_no", 1),
				(assign, ":courage", 5),
				(assign, ":aggressiveness", 5),
				(assign, ":help", 100),
			(else_try),
				(eq, ":behavior", tai_accompanying_party),
				(assign, ":behavior", ai_bhvr_escort_party),
				(assign, ":courage", 10),
				(assign, ":aggressiveness", 0),
				(assign, ":help", 500),
			(else_try),
				(eq, ":behavior", tai_traveling_to_party),
				(assign, ":behavior", ai_bhvr_travel_to_party),
				(assign, ":courage", 5),
				(assign, ":aggressiveness", 0),
				(assign, ":help", 50),
			(else_try),
				(eq, ":behavior", tai_attacking_center),
				(party_get_position, pos1, ":object"),
				(map_get_land_position_around_position, pos2, pos1, 2),
				(assign, ":behavior", ai_bhvr_travel_to_point),
				(party_set_ai_target_position, ":party_no", pos2),
				(assign, ":courage", 5),
				(assign, ":aggressiveness", 0),
				(assign, ":help", 150),
			(else_try),
				(eq, ":behavior", tai_traveling_to_point),
				(party_get_position, pos1, ":object"),
				(map_get_land_position_around_position, pos2, pos1, 2),
				(assign, ":behavior", ai_bhvr_travel_to_point),
				(party_set_ai_target_position, ":party_no", pos2),
				(assign, ":courage", 5),
				(assign, ":aggressiveness", 1),
				(assign, ":help", 10),
			(else_try),
				(assign, ":courage", 5),
				(assign, ":aggressiveness", 5),
				(assign, ":help", 100),
			(try_end),
			
			
			(party_set_aggressiveness, ":party_no", ":aggressiveness"),
			(party_set_courage, ":party_no", ":courage"),
			(party_set_helpfulness, ":party_no", ":help"),
			
			(party_set_ai_behavior, ":party_no", ":behavior"),
			(party_set_ai_object, ":party_no", ":object"),
		]),
	
	# script_party_recruit_troops
	# input:
	# 	arg1: party_no
	# output:
	# 	reg0: num_recruited
	("party_recruit_troops",
		[
			(store_script_param, ":party_no", 1),
			
			(call_script, "script_party_get_companion_limit", ":party_no"),
			(assign, ":limit", reg0),
			
			
			# ToDo:
			# (call_script, "script_party_get_party_size_limit_modifiers", ":party_no"),
			# (assign, ":modifier", reg0),
			# (val_mul, ":limit", ":modifier"),
			# (val_div, ":limit", 100),
			
			(party_get_num_companions, ":num_troops", ":party_no"),
			(try_begin),
				(lt, ":num_troops", ":limit"),
				(neg|party_slot_ge, ":party_no", slot_party_besieged_by, 0),
				
				(call_script, "script_party_add_reinforcements", ":party_no"),
				
				# (call_script, "script_party_add_troops_with_buildings", ":party_no"),
			(try_end),
			(party_get_num_companions, ":new_num_troops", ":party_no"),
			
			(store_sub, ":num_recruited", ":new_num_troops", ":num_troops"),
			
			(assign, reg0, ":num_recruited"),
		]),
	
	# script_party_add_reinforcements
	# input:
	# 	arg1: party_no
	# output:
	# 	reg0: num_added
	#	reg1: total_cost
	("party_add_reinforcements",
		[
			(store_script_param, ":party_no", 1),
			(store_faction_of_party, ":faction", ":party_no"),
			(faction_get_slot, ":culture", ":faction", slot_faction_culture),
				
			(party_get_slot, ":party_type", ":party_no", slot_party_type),
			(try_begin), # We go up to 90% to let some margin
				(eq, ":party_type", spt_village),
				(assign, ":num_peasant", 55),
				(assign, ":num_common", 30),
				(assign, ":num_veteran", 5),
				(assign, ":num_elite", 0),
				(assign, ":num_noble", 0),
			(else_try),
				(eq, ":party_type", spt_castle),
				(assign, ":num_peasant", 10),
				(assign, ":num_common", 25),
				(assign, ":num_veteran", 40),
				(assign, ":num_elite", 10),
				(assign, ":num_noble", 5),
			(else_try),
				# (eq, ":party_type", spt_town),
				(assign, ":num_peasant", 15),
				(assign, ":num_common", 35),
				(assign, ":num_veteran", 20),
				(assign, ":num_elite", 10),
				(assign, ":num_noble", 10),
			(try_end),
			
			(faction_get_slot, ":peasant_mod", ":faction", slot_faction_peasant_num_tries),
			(faction_get_slot, ":common_mod", ":faction", slot_faction_common_num_tries),
			(faction_get_slot, ":veteran_mod", ":faction", slot_faction_veteran_num_tries),
			(faction_get_slot, ":elite_mod", ":faction", slot_faction_elite_num_tries),
			(faction_get_slot, ":noble_mod", ":faction", slot_faction_noble_num_tries),
			
			(val_add, ":num_peasant", ":peasant_mod"),
			(val_add, ":num_common", ":common_mod"),
			(val_add, ":num_veteran", ":veteran_mod"),
			(val_add, ":num_elite", ":elite_mod"),
			(val_add, ":num_noble", ":noble_mod"),
			
			(assign, ":peasant_max", ":num_peasant"),
			(store_add, ":common_max", ":peasant_max", ":num_common"),
			(store_add, ":veteran_max", ":common_max", ":num_veteran"),
			(store_add, ":elite_max", ":veteran_max", ":num_elite"),
			(store_add, ":noble_max", ":elite_max", ":num_noble"),
			
			(faction_get_slot, ":peasant_begin", ":culture", slot_faction_peasant_begin),
			(faction_get_slot, ":common_begin", ":culture", slot_faction_common_begin),
			(faction_get_slot, ":veteran_begin", ":culture", slot_faction_veteran_begin),
			(faction_get_slot, ":elite_begin", ":culture", slot_faction_elite_begin),
			(faction_get_slot, ":noble_begin", ":culture", slot_faction_noble_begin),
			(faction_get_slot, ":troops_end", ":culture", slot_faction_troops_end),
			
			(assign, ":num_added", 0),
			(assign, ":total_cost", 0),
			
			# (assign, ":reinforcements", 0),
			(store_random_in_range, ":random", 0, 100),
			(store_random_in_range, ":random_number", 50, 100),
			(try_begin),
				(lt, ":random", ":peasant_max"),
				(store_mul, ":num_to_add", 17, ":random_number"),
				(val_div, ":num_to_add", 100),
				(call_script, "script_party_add_troops", ":party_no", ":peasant_begin", ":common_begin", ":num_to_add"),
				(val_add, ":num_added", reg0),
				(val_add, ":total_cost", reg1),
			(else_try),
				(lt, ":random", ":common_max"),
				(store_mul, ":num_to_add", 13, ":random_number"),
				(val_div, ":num_to_add", 100),
				(call_script, "script_party_add_troops", ":party_no", ":common_begin", ":veteran_begin", ":num_to_add"),
				(val_add, ":num_added", reg0),
				(val_add, ":total_cost", reg1),
			(else_try),
				(lt, ":random", ":veteran_max"),
				(store_mul, ":num_to_add", 9, ":random_number"),
				(val_div, ":num_to_add", 100),
				(call_script, "script_party_add_troops", ":party_no", ":veteran_begin", ":elite_begin", ":num_to_add"),
				(val_add, ":num_added", reg0),
				(val_add, ":total_cost", reg1),
			(else_try),
				(lt, ":random", ":elite_max"),
				(store_mul, ":num_to_add", 5, ":random_number"),
				(val_div, ":num_to_add", 100),
				(call_script, "script_party_add_troops", ":party_no", ":elite_begin", ":noble_begin", ":num_to_add"),
				(val_add, ":num_added", reg0),
				(val_add, ":total_cost", reg1),
			(else_try),
				(lt, ":random", ":noble_max"),
				(store_mul, ":num_to_add", 3, ":random_number"),
				(val_div, ":num_to_add", 100),
				(call_script, "script_party_add_troops", ":party_no", ":elite_begin", ":noble_begin", ":num_to_add"),
				(val_add, ":num_added", reg0),
				(val_add, ":total_cost", reg1),
				(call_script, "script_party_add_troops", ":party_no", ":noble_begin", ":troops_end", 1),
				(val_add, ":num_added", reg0),
				(val_add, ":total_cost", reg1),
			(try_end),
			# (try_begin),
				# (gt, ":reinforcements", 0),
				
				# (party_add_template, ":party_no", ":reinforcements"),
			# (try_end),
			# (assign, reg0, ":reinforcements"),
			(assign, reg0, ":num_added"),
			(assign, reg1, ":total_cost"),
		]),
	
	# script_party_add_troops
	# input:
	# 	arg1: party_no
	# 	arg2: begin of troops to add
	# 	arg3: end of troops to add
	# 	arg4: number of troops to add
	# output:
	# 	reg0: num_added
	# 	reg1: total_cost
	("party_add_troops",
		[
			(store_script_param, ":party_no", 1),
			(store_script_param, ":begin", 2),
			(store_script_param, ":end", 3),
			(store_script_param, ":num_tries", 4),
			
			(store_faction_of_party, ":faction", ":party_no"),
			
			(assign, ":total_weight", 0),
			
			(assign, ":num_added", 0),
			(assign, ":total_cost", 0),
			
			(try_for_range, ":cur_troop", ":begin", ":end"),
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
					
					(troop_get_slot, ":troop_type", ":cur_troop", slot_troop_type),
					
					(store_add, ":faction_slot", ":troop_type", slot_faction_troop_ratio_infantry),
					(val_add, ":faction_slot", -1),
					
					(faction_get_slot, ":original_weight", ":faction", ":faction_slot"),
					(store_add, ":weight", ":original_weight", ":total_weight"),
					
					(troop_set_slot, ":cur_troop", slot_troop_temp_slot, ":weight"),
					
					(val_add, ":total_weight", ":original_weight"),
				(else_try),
					(ge, ":only_faction_1", 0), # Nearby parties can recruit faction troops at a reduced rate
					
					(faction_get_slot, ":leader", ":only_faction_1", slot_faction_leader),
					(assign, ":weight", 0),
					(try_begin),
						(ge, ":leader", 0),
						(call_script, "script_troop_get_home", ":leader", 1),
						(assign, ":home", reg0),
						(ge, ":home", centers_begin),
						(store_distance_to_party_from_party, ":distance", ":party_no", ":home"),
						(lt, ":distance", 50),
						
						(store_sub, ":mul", 70, ":distance"),
						
						(troop_get_slot, ":troop_type", ":cur_troop", slot_troop_type),
					
						(store_add, ":faction_slot", ":troop_type", slot_faction_troop_ratio_infantry),
						(val_add, ":faction_slot", -1),
						
						(faction_get_slot, ":original_weight", ":faction", ":faction_slot"),
						(val_mul, ":original_weight", ":mul"),
						(val_div, ":original_weight", 180),
						(store_add, ":weight", ":original_weight", ":total_weight"),
						
						(val_add, ":total_weight", ":original_weight"),
					(try_end),
					
					(try_begin),
						(ge, ":only_faction_2", 0),
						(faction_get_slot, ":leader", ":only_faction_2", slot_faction_leader),
						(ge, ":leader", 0),
						(call_script, "script_troop_get_home", ":leader", 1),
						(assign, ":home", reg0),
						(try_begin),
							(ge, ":home", centers_begin),
							(store_distance_to_party_from_party, ":distance", ":party_no", ":home"),
							(lt, ":distance", 50),
							(store_sub, ":mul", 70, ":distance"),
							
							(troop_get_slot, ":troop_type", ":cur_troop", slot_troop_type),
						
							(store_add, ":faction_slot", ":troop_type", slot_faction_troop_ratio_infantry),
							(val_add, ":faction_slot", -1),
							
							(faction_get_slot, ":original_weight_2", ":faction", ":faction_slot"),
							(val_mul, ":original_weight_2", ":mul"),
							(val_div, ":original_weight_2", 180),
							(val_add, ":weight", ":original_weight_2"),
							
							(val_add, ":total_weight", ":original_weight_2"),
						(try_end),
					(try_end),
					
					(troop_set_slot, ":cur_troop", slot_troop_temp_slot, ":weight"),
				(else_try),
					(troop_set_slot, ":cur_troop", slot_troop_temp_slot, 0),
				(try_end),
			(try_end),
			
			(try_for_range, ":unused", 0, ":num_tries"),
				(store_random_in_range, ":random", 0, ":total_weight"),
				(assign, ":stop", ":end"),
				(try_for_range, ":cur_troop", ":begin", ":stop"),
					(troop_slot_ge, ":cur_troop", slot_troop_temp_slot, ":random"),
					(party_add_members, ":party_no", ":cur_troop", 1),
					(try_begin),
						(lt, reg0, 1),
						(display_message, "@Unable to add troop"),
					(else_try),
						(call_script, "script_troop_get_cost", ":cur_troop"),
						(assign, ":troop_cost", reg0),
						(val_add, ":num_added", 1),
						(val_add, ":total_cost", ":troop_cost"),
					(try_end),
					(assign, ":stop", 0),
				(try_end),
			(try_end),
			(assign, reg0, ":num_added"),
			(assign, reg1, ":total_cost"),
		]),
	
	# script_party_get_party_size_limit_modifiers
	# input:
	# 	arg1: party_no
	# output:
	# 	reg0: modifier
	# ("party_get_party_size_limit_modifiers",
		# [
			# ToDo:
			# (store_script_param, ":party_no", 1),
			
			# (assign, reg0, 100),
		# ]),
	
	# script_party_send_reinforcements
	# input:
	# 	arg1: party_no
	# output:
	# 	reg0: num_sent
	("party_send_reinforcements",
		[
			(store_script_param, ":party_no", 1),
			
			(party_get_slot, ":linked_center", ":party_no", slot_party_linked_party),
			(assign, ":num_sent", 0),
			
			(try_begin),
				(call_script, "script_cf_party_need_troops", ":linked_center"),
				
				(party_get_num_companions, ":num_troops", ":party_no"),
				(val_div, ":num_troops", 3),
				
				(call_script, "script_spawn_party_around_party", ":party_no", "pt_reinforcements"),
				
				(assign, ":spawned_party", reg0),
				
				(call_script, "script_party_give_troops_to_party", ":party_no", ":spawned_party", ":num_troops", -1),
				(val_add, ":num_sent", reg0),
				(party_set_slot, ":spawned_party", slot_party_mission, spm_reinforce),
				(party_set_slot, ":spawned_party", slot_party_mission_object, ":linked_center"),
				
				(party_set_slot, ":spawned_party", slot_party_type, spt_convoy),
				
				(party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
				(party_set_ai_object, ":spawned_party", ":linked_center"),
				
				(try_begin),
					(eq, ":num_sent", 0),
					(remove_party, ":spawned_party"),
				(try_end),
			(try_end),
			
			(assign, reg0, ":num_sent"),
		]),
	
	# script_party_give_troops_to_party
	# input:
	# 	arg1: giver_party
	#	arg2: receiver_party
	# 	arg3: num_troops
	# 	arg4: priority (-1: no priority, 0: priority peasant, 1: priority common, 2: priority veteran)
	# output:
	# 	reg0: num_added
	("party_give_troops_to_party",
		[
			(store_script_param, ":giver_party", 1),
			(store_script_param, ":receiver_party", 2),
			(store_script_param, ":num_troops", 3),
			# (store_script_param, ":priority", 4),
			
			# ToDo: priority
			(assign, ":num_added", 0),
			(party_get_num_companions, ":total_troops", ":giver_party"),
			(party_get_num_companion_stacks, ":num_stacks", ":giver_party"),
			(try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":cur_troop", ":giver_party", ":cur_stack"),
				(party_stack_get_size, ":cur_troop_number", ":giver_party", ":cur_stack"),
				(store_mul, ":num_to_add", ":cur_troop_number", ":num_troops"),
				(val_div, ":num_to_add", ":total_troops"),
				
				(gt, ":num_to_add", 0),
				(val_min, ":num_to_add", ":cur_troop_number"),
				
				(party_add_members, ":receiver_party", ":cur_troop", ":num_to_add"),
				(assign, ":really_added", reg0),
				(party_remove_members, ":giver_party", ":cur_troop", ":really_added"),
				
				(val_add, ":num_added", ":really_added"),
			(try_end),
			
			(store_sub, ":left_to_add", ":num_troops", ":num_added"),
			(try_begin),
				(party_get_num_companions, ":total_troops", ":giver_party"),	
				(val_min, ":left_to_add", ":total_troops"),
				
				(gt, ":left_to_add", 0),
				
				(try_for_range, ":unused", 0, ":left_to_add"),
					(party_get_num_companion_stacks, ":num_stacks", ":giver_party"),
					(store_random_in_range, ":random_stack", 0, ":num_stacks"),
					(party_stack_get_troop_id, ":random_troop", ":giver_party", ":random_stack"),
					(party_add_members, ":receiver_party", ":random_troop", 1),
					(party_remove_members, ":giver_party", ":random_troop", reg0),
					(val_add, ":num_added", reg0),
				(try_end),
			(try_end),
			(assign, reg0, ":num_added"),
		]),
	
	# script_party_modify_population
	# input:
	# 	arg1: party_no
	# 	arg2: value
	# output: none
	("party_modify_population",
		[
			(store_script_param, ":party_no", 1),
			(store_script_param, ":value", 2),
			
			(party_get_slot, ":population", ":party_no", slot_party_population),
			(val_add, ":population", ":value"),
			(party_set_slot, ":party_no", slot_party_population, ":population"),
		]),
	
	# script_party_modify_wealth
	# input:
	# 	arg1: party_no
	# 	arg2: value
	# output: none
	("party_modify_wealth",
		[
			(store_script_param, ":party_no", 1),
			(store_script_param, ":value", 2),
			
			(party_get_slot, ":wealth", ":party_no", slot_party_wealth),
			(val_add, ":wealth", ":value"),
			(party_set_slot, ":party_no", slot_party_wealth, ":wealth"),
		]),
	
	# script_init_building_slots
	# input: none
	# output: none
	("init_building_slots",
		[
			(item_set_slot, "itm_building_hunter_camp", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_hunter_camp", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_hunter_camp", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_hunter_camp", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_woodcutter_camp", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_woodcutter_camp", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_woodcutter_camp", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_woodcutter_camp", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_mill", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_mill", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_mill", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_mill", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_fish_pond", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_fish_pond", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_fish_pond", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_fish_pond", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_mine", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_mine", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_mine", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_mine", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_stone_pit", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_stone_pit", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_stone_pit", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_stone_pit", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_cattle_ranch", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_cattle_ranch", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_cattle_ranch", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_cattle_ranch", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_farm", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_farm", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_farm", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_farm", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_slaver", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_slaver", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_slaver", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_slaver", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_market", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_market", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_market", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_market", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_fields", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_fields", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_fields", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_fields", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_tannery", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_tannery", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_tannery", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_tannery", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_militia_camp", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_militia_camp", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_militia_camp", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_militia_camp", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_smithy", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_smithy", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_smithy", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_smithy", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_stables", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_stables", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_stables", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_stables", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_archery_range", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_archery_range", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_archery_range", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_archery_range", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_barrack", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_barrack", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_barrack", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_barrack", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_training_camp", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_training_camp", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_training_camp", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_training_camp", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_workshop", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_workshop", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_workshop", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_workshop", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_fletcher", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_fletcher", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_fletcher", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_fletcher", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_university", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_university", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_university", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_university", slot_building_build_time, 0),
			
			(item_set_slot, "itm_building_temple", slot_building_cost_wood, 0),
			(item_set_slot, "itm_building_temple", slot_building_cost_stone, 0),
			(item_set_slot, "itm_building_temple", slot_building_cost_gold, 0),
			(item_set_slot, "itm_building_temple", slot_building_build_time, 0),
		]),
	
	# script_faction_get_troop_rate
	# input: 
	# 	arg1: faction_no
	# output:
	# 	reg0: rate
	("faction_get_troop_rate",
		[
			# (store_script_param, ":faction_no", 1),
			# ToDo:
			
			(assign, reg0, 100),
		]),
	
	# script_party_has_building
	# input:
	# 	arg1: party_no
	# 	arg2: building
	# output:
	# 	reg0: has_building (-1 no, 0 is destroyed, 1 yes, 2 is damaged)
	("party_has_building",
		[
			(store_script_param, ":party_no", 1),
			(store_script_param, ":building", 2),
			
			(assign, ":has_building", -1),
			
			(store_add, ":end", slot_party_building_slot_10, 1),
			(try_for_range, ":building_slot", slot_party_building_slot_1, ":end"),
				(party_get_slot, ":cur_building", ":party_no", ":building_slot"),
				(try_begin),
					(eq, ":cur_building", ":building"),
					(val_add, ":building_slot", 10),
					(party_get_slot, ":has_building", ":party_no", ":building_slot"), # gets building state
					(assign, ":end", 0),
				(try_end),
			(try_end),
			
			(assign, reg0, ":has_building"),
		]),
	
	# script_cf_party_need_troops
	# input:
	# 	arg1: party_no
	# output: none
	("cf_party_need_troops",
		[
			# ToDo: improve
			(store_script_param, ":party_no", 1),
			
			# (neg|troop_slot_ge, ":party_no", slot_party_besieged_by, 0),
			
			(call_script, "script_party_get_companion_limit", ":party_no"),
			
			(store_mul, ":limit", reg0, 3),
			(val_div, ":limit", 4),
			(party_get_num_companions, ":num_troops", ":party_no"),
			(lt, ":num_troops", ":limit"),
		]),
	
	# script_troop_get_rank
	# input:
	# 	arg1: troop_no
	# output:
	# 	reg0: rank
	("troop_get_rank",
		[
			(store_script_param, ":troop_no", 1),
			
			(assign, ":end", centers_end),
			(assign, ":rank", 0),
			
			(store_troop_faction, ":faction", ":troop_no"),
			(assign, ":num_fiefs", 0),
			(try_for_range, ":cur_center", centers_begin, ":end"),
				(store_faction_of_party, ":center_faction", ":cur_center"),
				(eq, ":faction", ":center_faction"),
				(party_get_slot, ":party_type", ":cur_center", slot_party_type),
				(try_begin),
					(eq, ":party_type", spt_village),
					(lt, ":rank", rank_two_village),
					
					(party_get_slot, ":lord", ":cur_center", slot_party_lord),
					(try_begin),
						(eq, ":lord", ":troop_no"),
						(val_add, ":rank", 1),
						(val_max, ":rank", rank_village),
						(val_min, ":rank", rank_two_village),
					(try_end),
				(else_try),
					(eq, ":party_type", spt_castle),
					(val_add, ":num_fiefs", 1),
					(lt, ":rank", rank_castle),
					(party_get_slot, ":lord", ":cur_center", slot_party_lord),
					(try_begin),
						(eq, ":lord", ":troop_no"),
						(assign, ":rank", rank_castle),
					(try_end),
				(else_try),
					(eq, ":party_type", spt_town),
					(val_add, ":num_fiefs", 2),
					(party_get_slot, ":lord", ":cur_center", slot_party_lord),
					(try_begin),
						(eq, ":lord", ":troop_no"),
						(assign, ":rank", rank_city),
					(try_end),
				(try_end),
			(try_end),
			(try_begin),
				(ge, ":num_fiefs", 4), # King and marshall ranks are only applied if kingdom is big enough
				(try_begin),
					(faction_slot_eq, ":faction", slot_faction_leader, ":troop_no"),
					(assign, ":rank", rank_king),
				(else_try),
					(faction_slot_eq, ":faction", slot_faction_marshall, ":troop_no"),
					(assign, ":rank", rank_marshall),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":rank", 0),
				(troop_get_slot, ":master", ":troop_no", slot_troop_vassal_of),
				(try_begin),
					(ge, ":master", 0),
					(assign, ":rank", rank_affiliated),
				(try_end),
			(try_end),
			
			(assign, reg0, ":rank"),
		]),
	
	# script_troop_update_level
	# input:
	# 	arg1: troop_no
	# 	arg2: cur_rank
	# 	arg3: new_rank
	# output:
	# 	reg0: rank_changed (1 yes, 0 no)
	("troop_update_level",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":cur_rank", 2),
			(store_script_param, ":new_rank", 3),
			
			(assign, ":changed", 0),
			
			(store_sub, ":diff", ":new_rank", ":cur_rank"),
			(store_mul, ":chance", ":diff", ":diff"),
			(try_begin),
				(gt, ":diff", 0),
				(val_mul, ":chance", 4),
			(else_try),
				# (lt, ":diff", 0),
				(val_mul, ":chance", 2),
			(try_end),
			
			(store_random_in_range, ":rand", 0, 100),
			(try_begin),
				(lt, ":rand", ":chance"),
				
				(try_begin),
					(gt, ":diff", 0),
					(val_add, ":cur_rank", 1),
				(else_try),
					(val_sub, ":cur_rank", 1),
				(try_end),
				(call_script, "script_troop_change_level", ":troop_no", ":cur_rank"),
				(assign, ":changed", 1),
			(try_end),
			
			(assign, reg0, ":changed"),
		]),
	
	# script_init_lord
	# input:
	# 	arg1: lord_no
	# output: none
	("init_lord",
		[
			(store_script_param, ":lord_no", 1),
			
			(troop_set_slot, ":lord_no", slot_troop_kingdom_occupation, tko_kingdom_hero),
			(troop_set_slot, ":lord_no", slot_troop_vassal_of, -1),
			
			(call_script, "script_troop_set_equip_type", ":lord_no"),
			(call_script, "script_troop_change_level", ":lord_no", 0),
			(troop_set_slot, ":lord_no", slot_troop_rank, rank_none),
			(call_script, "script_troop_set_name", ":lord_no"),
			(call_script, "script_troop_update_name", ":lord_no"),
			(call_script, "script_troop_update_home", ":lord_no"),
			
			(troop_set_slot, ":lord_no", slot_troop_leaded_party, -1),
		]),
	
	# script_troop_set_name
	# input:
	# 	arg1: troop_no
	# output: none
	("troop_set_name",
		[
			(store_script_param, ":troop_no", 1),
			(troop_get_slot, ":original_faction", ":troop_no", slot_troop_original_faction),
			(faction_get_slot, ":culture", ":original_faction", slot_faction_culture),
			
			(faction_get_slot, ":names_begin", ":culture", slot_faction_names_begin),
			(faction_get_slot, ":names_end", ":culture", slot_faction_names_end),
			
			(store_random_in_range, ":name", ":names_begin", ":names_end"),
			(troop_set_plural_name, ":troop_no", ":name"),
		]),
	
	# script_troop_give_center_to_troop
	# input:
	# 	arg1: giver_troop_no
	# 	arg2: center
	# 	arg3: receiver_troop
	# output: none
	("troop_give_center_to_troop",
		[
			(store_script_param, ":giver_troop_no", 1),
			(store_script_param, ":center", 2),
			(store_script_param, ":receiver_troop", 3),
			
			(try_begin),
				(str_store_troop_name, s10, ":giver_troop_no"),
				(str_store_troop_name, s11, ":receiver_troop"),
				(str_store_party_name, s12, ":center"),
				(display_message, "@{s10} gives {s12} to {s11}"),
			(try_end),
			
			(troop_get_slot, ":num_vassal", ":giver_troop_no", slot_troop_num_vassal),
			(val_add, ":num_vassal", 1),
			(troop_set_slot, ":giver_troop_no", slot_troop_num_vassal, ":num_vassal"),
			
			(troop_set_slot, ":receiver_troop", slot_troop_vassal_of, ":giver_troop_no"),
			
			(call_script, "script_give_center_to_troop", ":center", ":receiver_troop"),
			
			(assign, ":surplus_center", -1),
			(try_begin),
				(call_script, "script_troop_get_home", ":giver_troop_no", 0),
				(assign, ":home", reg0),
				(is_between, ":home", walled_centers_begin, walled_centers_end),
				(assign, ":end", centers_end),
				(try_for_range, ":center_no", centers_begin, ":end"),
					(party_slot_eq, ":center_no", slot_party_lord, ":giver_troop_no"),
					(neq, ":center_no", ":home"),
					(assign, ":surplus_center", ":center_no"),
					(assign, ":end", 0),
				(try_end),
			(try_end),
			(troop_set_slot, ":giver_troop_no", slot_troop_surplus_center,":surplus_center"),
			
			(assign, ":surplus_center", -1),
			(try_begin),
				(call_script, "script_troop_get_home", ":receiver_troop", 0),
				(assign, ":home", reg0),
				(is_between, ":home", walled_centers_begin, walled_centers_end),
				(assign, ":end", centers_end),
				(try_for_range, ":center_no", centers_begin, ":end"),
					(party_slot_eq, ":center_no", slot_party_lord, ":receiver_troop"),
					(neq, ":center_no", ":home"),
					(assign, ":surplus_center", ":center_no"),
					(assign, ":end", 0),
				(try_end),
			(try_end),
			(troop_set_slot, ":receiver_troop", slot_troop_surplus_center,":surplus_center"),
		]),
	
	# script_give_center_to_troop
	# input:
	# 	arg1: center_no
	# 	arg2: troop_no
	# output: none
	("give_center_to_troop",
		[
			(store_script_param, ":center_no", 1),
			(store_script_param, ":troop_no", 2),
			
			(troop_get_slot, ":old_rank", ":troop_no", slot_troop_rank),
			
			(party_set_slot, ":center_no", slot_party_lord, ":troop_no"),
			
			(call_script, "script_troop_get_rank", ":troop_no"),
			(assign, ":rank", reg0),
			(troop_set_slot, ":troop_no", slot_troop_rank, ":rank"),
			
			(call_script, "script_troop_update_name", ":troop_no"),
			(call_script, "script_troop_update_home", ":troop_no"),
			
			(try_begin),
				(ge, ":old_rank", rank_village),
				(call_script, "script_troop_get_home", ":troop_no", 0),
				(assign, ":home", reg0),
				(is_between, ":home", walled_centers_begin, walled_centers_end),
				(assign, ":end", centers_end),
				(try_for_range, ":center_no", centers_begin, ":end"),
					(party_slot_eq, ":center_no", slot_party_lord, ":troop_no"),
					(neq, ":center_no", ":home"),
					(troop_set_slot, ":troop_no", slot_troop_surplus_center, ":center_no"),
					(assign, ":end", 0),
				(try_end),
			(try_end),
		]),
	
	# script_init_troops_factions
	# input: none
	# output: none
	("init_troops_factions",
		[
			(try_for_range, ":cur_troop", soldiers_begin, soldiers_end),
				(store_troop_faction, ":troop_faction", ":cur_troop"),
				(try_begin),
					(neg|is_between, ":troop_faction", kingdoms_begin, small_kingdoms_begin),
					(troop_set_slot, ":cur_troop", slot_troop_faction_reserved_1, ":troop_faction"),
				(else_try),
					(troop_set_slot, ":cur_troop", slot_troop_faction_reserved_1, -1),
				(try_end),
				(troop_set_slot, ":cur_troop", slot_troop_faction_reserved_2, -1),
				(troop_set_slot, ":cur_troop", slot_troop_faction_not_1, -1),
				(troop_set_slot, ":cur_troop", slot_troop_faction_not_2, -1),
			(try_end),
			
			# Troops not added to factions
			(troop_set_slot, "trp_swadian_light_bowman", slot_troop_faction_not_1, "fac_small_kingdom_14"), # Has Light Longbowman instead
			(troop_set_slot, "trp_swadian_bowman", slot_troop_faction_not_1, "fac_small_kingdom_14"), # Has Heavy Longbowman instead
			(troop_set_slot, "trp_swadian_heavy_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_17"), # Has Squire instead
			
			(troop_set_slot, "trp_vaegir_light_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_22"), # Has Scout instead
			(troop_set_slot, "trp_vaegir_heavy_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_22"), # Has Horseman instead
			
			(troop_set_slot, "trp_khergit_light_infantry", slot_troop_faction_not_1, "fac_small_kingdom_32"), # Has Light Skirmisher instead
			(troop_set_slot, "trp_khergit_heavy_infantry", slot_troop_faction_not_1, "fac_small_kingdom_32"), # Has Warrior instead
			(troop_set_slot, "trp_khergit_skirmisher", slot_troop_faction_not_1, "fac_small_kingdom_32"), # Has Light Skirmisher instead
			(troop_set_slot, "trp_khergit_guard", slot_troop_faction_not_2, "fac_small_kingdom_32"), # Has Royal Guard instead
			(troop_set_slot, "trp_khergit_light_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_33"), # Has Light Steppe Cavalry instead
			(troop_set_slot, "trp_khergit_heavy_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_33"), # Has Heavy Steppe Cavalry instead
			(troop_set_slot, "trp_khergit_mounted_skirmisher", slot_troop_faction_not_1, "fac_small_kingdom_33"), # Has Scout instead
			(troop_set_slot, "trp_khergit_noble", slot_troop_faction_not_1, "fac_small_kingdom_34"), # Has Noble Cavalry and Noble Lancer instead
			(troop_set_slot, "trp_khergit_guard", slot_troop_faction_not_1, "fac_small_kingdom_36"), # Has Blade-Master instead
			
			(troop_set_slot, "trp_nord_light_bowman", slot_troop_faction_not_1, "fac_small_kingdom_42"), # Has Light Longbowman instead
			(troop_set_slot, "trp_nord_heavy_bowman", slot_troop_faction_not_1, "fac_small_kingdom_42"), # Has Heavy Longbowman instead
			(troop_set_slot, "trp_nord_light_infantry", slot_troop_faction_not_1, "fac_small_kingdom_43"), # Has Skirmisher instead
			(troop_set_slot, "trp_nord_guard", slot_troop_faction_not_1, "fac_small_kingdom_43"), # Has Heavy Skirmisher instead
			(troop_set_slot, "trp_nord_medium_longbowman", slot_troop_faction_not_1, "fac_small_kingdom_45"), # Has Bowman instead
			
			(troop_set_slot, "trp_rhodok_light_crossbowman", slot_troop_faction_not_1, "fac_small_kingdom_51"), #
			(troop_set_slot, "trp_rhodok_light_horse_archer", slot_troop_faction_not_1, "fac_small_kingdom_51"), # Has Mounted Archer instead
			(troop_set_slot, "trp_rhodok_medium_crossbowman", slot_troop_faction_not_1, "fac_small_kingdom_51"), # Has Bowman instead
			(troop_set_slot, "trp_rhodok_heavy_crossbowman", slot_troop_faction_not_1, "fac_small_kingdom_51"), # Has Heavy Bowman instead
			(troop_set_slot, "trp_rhodok_noble", slot_troop_faction_not_1, "fac_small_kingdom_51"), # Has Highlander instead
			(troop_set_slot, "trp_rhodok_noble", slot_troop_faction_not_2, "fac_small_kingdom_52"), # Has Heroic Rider instead
			(troop_set_slot, "trp_rhodok_noble_riders", slot_troop_faction_reserved_2, "fac_small_kingdom_53"), #
			
			(troop_set_slot, "trp_sarranid_noble", slot_troop_faction_not_1, "fac_small_kingdom_63"), # Has Heavy Mamluke instead
		]),
	
	# script_init_troops_types
	# input: none
	# output: none
	("init_troops_types",
		[
			(try_for_range, ":cur_troop", soldiers_begin, soldiers_end),
				(assign, ":has_shield", 0),
				(assign, ":has_bow", 0),
				(assign, ":has_xbow", 0),
				# (assign, ":has_throw", 0),
				(assign, ":has_pole", 0), # Handles spear-like weapons
				(assign, ":has_pike", 0), # Handles pikes and lances
				(assign, ":has_sidearm", 0), # Every other melee weapon
				(troop_get_inventory_capacity, ":capacity", ":cur_troop"),
				(try_for_range, ":item_slot", ek_item_0, ":capacity"),
					(troop_get_inventory_slot, ":cur_item", ":cur_troop", ":item_slot"),
					(gt, ":cur_item", 0),
					(item_get_type, ":item_type", ":cur_item"),
					(try_begin),
						(eq, ":item_type", itp_type_shield),
						(assign, ":has_shield", 1),
					(else_try),
						(eq, ":item_type", itp_type_polearm),
						(try_begin),
							(is_between, ":cur_item", "itm_pitch_fork", "itm_ashwood_pike"),
							(assign, ":has_pole", 1),
						(else_try),
							(is_between, ":cur_item", "itm_light_lance", "itm_hafted_blade_a"),
							(assign, ":has_pike", 1),
						(else_try),
							(is_between, ":cur_item", "itm_ashwood_pike", "itm_glaive"),
							(assign, ":has_pike", 1),
						(else_try),
							(eq, ":cur_item", "itm_bamboo_spear"),
							(assign, ":has_pike", 1),
							(assign, ":has_pole", 1),
						(else_try),
							(assign, ":has_sidearm", 1),
						(try_end),
					(else_try),
						(eq, ":item_type", itp_type_bow),
						(assign, ":has_bow", 1),
					(else_try),
						(eq, ":item_type", itp_type_crossbow),
						(assign, ":has_xbow", 1),
					# (else_try),
						# (eq, ":item_type", itp_type_thrown),
						# (assign, ":has_throw", 1),
					(else_try),
						(this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
						(eq, ":item_type", itp_type_two_handed_wpn),
						(assign, ":has_sidearm", 1),
					(try_end),
				(try_end),
				
				(try_begin),
					(troop_is_guarantee_horse, ":cur_troop"),
					(try_begin),
						(eq, ":has_pike", 1),
						(eq, ":has_sidearm", 0),
						(troop_set_slot, ":cur_troop", slot_troop_type, tt_lancer),
					(else_try),
						(troop_is_guarantee_ranged, ":cur_troop"),
						(try_begin),
							(this_or_next|eq, ":has_bow", 1),
							(eq, ":has_xbow", 1),
							(troop_set_slot, ":cur_troop", slot_troop_type, tt_horse_archer),
						(else_try),
							(troop_set_slot, ":cur_troop", slot_troop_type, tt_mounted_skirmisher),
						(try_end),
					(else_try),
						(troop_set_slot, ":cur_troop", slot_troop_type, tt_cavalry),
					(try_end),
				(else_try),
					(troop_is_guarantee_ranged, ":cur_troop"),
					(try_begin),
						(eq, ":has_xbow", 1),
						(troop_set_slot, ":cur_troop", slot_troop_type, tt_crossbow),
					(else_try),
						(eq, ":has_bow", 1),
						(troop_set_slot, ":cur_troop", slot_troop_type, tt_archer),
					(else_try),
						(troop_set_slot, ":cur_troop", slot_troop_type, tt_skirmisher),
					(try_end),
				(else_try),
					(eq, ":has_sidearm", 0),
					(try_begin),
						(eq, ":has_shield", 1),
						(eq, ":has_pole", 1),
						(troop_set_slot, ":cur_troop", slot_troop_type, tt_spearman),
					(else_try),
						(eq, ":has_pike", 1),
						(troop_set_slot, ":cur_troop", slot_troop_type, tt_pikeman),
					(else_try),
						(troop_set_slot, ":cur_troop", slot_troop_type, tt_shock_infantry),
					(try_end),
				(else_try),
					(eq, ":has_shield", 1),
					(troop_set_slot, ":cur_troop", slot_troop_type, tt_infantry),
				(else_try),
					(troop_set_slot, ":cur_troop", slot_troop_type, tt_shock_infantry),
				(try_end),
				
				(store_troop_faction, ":faction", ":cur_troop"),
				(faction_get_slot, ":culture", ":faction", slot_faction_culture),
				(faction_get_slot, ":peasant", ":culture", slot_faction_peasant_begin),
				(faction_get_slot, ":common", ":culture", slot_faction_common_begin),
				(faction_get_slot, ":veteran", ":culture", slot_faction_veteran_begin),
				(faction_get_slot, ":elite", ":culture", slot_faction_elite_begin),
				(faction_get_slot, ":noble", ":culture", slot_faction_noble_begin),
				(faction_get_slot, ":end", ":culture", slot_faction_troops_end),
				(try_begin),
					(is_between, ":cur_troop", ":peasant", ":common"),
					(troop_set_slot, ":cur_troop", slot_troop_quality, tq_peasant),
				(else_try),
					(is_between, ":cur_troop", ":common", ":veteran"),
					(troop_set_slot, ":cur_troop", slot_troop_quality, tq_common),
				(else_try),
					(is_between, ":cur_troop", ":veteran", ":elite"),
					(troop_set_slot, ":cur_troop", slot_troop_quality, tq_veteran),
				(else_try),
					(is_between, ":cur_troop", ":elite", ":noble"),
					(troop_set_slot, ":cur_troop", slot_troop_quality, tq_elite),
				(else_try),
					(is_between, ":cur_troop", ":noble", ":end"),
					(troop_set_slot, ":cur_troop", slot_troop_quality, tq_noble),
				(try_end),
				
				(assign, ":armor", -1),
				(assign, ":horse", -1),
				(assign, ":weapon", -1),
				(troop_get_inventory_capacity, ":capacity", ":cur_troop"),
				(try_for_range, ":item_slot", ek_item_0, ":capacity"),
					(troop_get_inventory_slot, ":cur_item", ":cur_troop", ":item_slot"),
					(gt, ":cur_item", 0),
					(item_get_type, ":item_type", ":cur_item"),
					(try_begin),
						(eq, ":item_type", itp_type_horse),
						(try_begin),
							(is_between, ":cur_item", light_horses_begin, light_horses_end),
							(try_begin),
								(neq, ":horse", -1),
								(val_min, ":horse", weight_light),
							(else_try),
								(val_max, ":horse", weight_light),
							(try_end),
						(else_try),
							(is_between, ":cur_item", medium_horses_begin, medium_horses_end),
							(try_begin),
								(neq, ":horse", -1),
								(val_min, ":horse", weight_medium),
							(else_try),
								(val_max, ":horse", weight_medium),
							(try_end),
						(else_try),
							(is_between, ":cur_item", heavy_horses_begin, heavy_horses_end),
							(try_begin),
								(neq, ":horse", -1),
								(val_min, ":horse", weight_heavy),
							(else_try),
								(val_max, ":horse", weight_heavy),
							(try_end),
						(else_try),
							# (is_between, ":cur_item", armoured_horses_begin, armoured_horses_end),
							(try_begin),
								(neq, ":horse", -1),
								(val_min, ":horse", weight_very_heavy),
							(else_try),
								(val_max, ":horse", weight_very_heavy),
							(try_end),
						(try_end),
					(else_try),
						(eq, ":item_type", itp_type_bow),
						(try_begin),
							(is_between, ":cur_item", "itm_hunting_bow", "itm_nomad_bow"),
							(try_begin),
								(neq, ":weapon", -1),
								(val_min, ":weapon", weight_light),
							(else_try),
								(val_max, ":weapon", weight_light),
							(try_end),
						(else_try),
							(is_between, ":cur_item", "itm_nomad_bow", "itm_long_bow"),
							(try_begin),
								(neq, ":weapon", -1),
								(val_min, ":weapon", weight_medium),
							(else_try),
								(val_max, ":weapon", weight_medium),
							(try_end),
						(else_try),
							# (is_between, ":cur_item", "itm_long_bow", "itm_hunting_crossbow"),
							(try_begin),
								(neq, ":weapon", -1),
								(val_min, ":weapon", weight_heavy),
							(else_try),
								(val_max, ":weapon", weight_heavy),
							(try_end),
						(try_end),
					(else_try),
						(eq, ":item_type", itp_type_crossbow),
						(try_begin),
							(is_between, ":cur_item", "itm_hunting_crossbow", "itm_crossbow"),
							(try_begin),
								(neq, ":weapon", -1),
								(val_min, ":weapon", weight_light),
							(else_try),
								(val_max, ":weapon", weight_light),
							(try_end),
						(else_try),
							(is_between, ":cur_item", "itm_crossbow", "itm_heavy_crossbow"),
							(try_begin),
								(neq, ":weapon", -1),
								(val_min, ":weapon", weight_medium),
							(else_try),
								(val_max, ":weapon", weight_medium),
							(try_end),
						(else_try),
							# (is_between, ":cur_item", "itm_heavy_crossbow", ranged_weapons_end),
							(try_begin),
								(neq, ":weapon", -1),
								(val_min, ":weapon", weight_heavy),
							(else_try),
								(val_max, ":weapon", weight_heavy),
							(try_end),
						(try_end),
					(else_try),
						(eq, ":item_type", itp_type_thrown),
						(try_begin),
							(is_between, ":cur_item", ranged_weapons_begin, "itm_darts"),
							(try_begin),
								(neq, ":weapon", -1),
								(val_min, ":weapon", weight_very_light),
							(else_try),
								(val_max, ":weapon", weight_very_light),
							(try_end),
						(else_try),
							(is_between, ":cur_item", "itm_darts", "itm_javelin"),
							(try_begin),
								(neq, ":weapon", -1),
								(val_min, ":weapon", weight_light),
							(else_try),
								(val_max, ":weapon", weight_light),
							(try_end),
							(val_max, ":weapon", weight_light),
						(else_try),
							(this_or_next|is_between, ":cur_item", "itm_javelin", "itm_jarid"),
							(eq, ":cur_item", "itm_light_throwing_axes"),
							(try_begin),
								(neq, ":weapon", -1),
								(val_min, ":weapon", weight_medium),
							(else_try),
								(val_max, ":weapon", weight_medium),
							(try_end),
						(else_try),
							# (this_or_next|is_between, ":cur_item", "itm_throwing_axes", "itm_hunting_bow"),
							# (eq, ":cur_item", "itm_jarid"),
							(try_begin),
								(neq, ":weapon", -1),
								(val_min, ":weapon", weight_heavy),
							(else_try),
								(val_max, ":weapon", weight_heavy),
							(try_end),
						(try_end),
					(else_try),
						(eq, ":item_type", itp_type_body_armor),
						(try_begin),
							(is_between, ":cur_item", very_light_armors_begin, light_armors_begin),
							(val_max, ":armor", weight_very_light),
						(else_try),
							(is_between, ":cur_item", light_armors_begin, medium_armors_begin),
							(val_max, ":armor", weight_light),
						(else_try),
							(is_between, ":cur_item", medium_armors_begin, heavy_armors_begin),
							(val_max, ":armor", weight_medium),
						(else_try),
							# (is_between, ":cur_item", heavy_armors_end, armors_end),
							(val_max, ":armor", weight_heavy),
						(try_end),
					(try_end),
				(try_end),
				
				(troop_set_slot, ":cur_troop", slot_troop_armor_weight, ":armor"),
				(troop_set_slot, ":cur_troop", slot_troop_horse_weight, ":horse"),
				(troop_set_slot, ":cur_troop", slot_troop_ranged_weapon_weight, ":weapon"),
			(try_end),
			
			# Secial treatments
			(troop_set_slot, "trp_swadian_militia", slot_troop_type, tt_crossbow),
			(troop_set_slot, "trp_swadian_guard", slot_troop_type, tt_shock_infantry), # Because swadians have too many of them
			(troop_set_slot, "trp_khergit_militia", slot_troop_type, tt_archer),
		]),
	
	# script_troop_get_home
	# input:
	# 	arg1: troop_no
	# 	arg2: walled (if home needs to be a walled center)
	# output:
	# 	reg0: home
	("troop_get_home",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":walled", 2),
			
			(troop_get_slot, ":home", ":troop_no", slot_troop_home),
			(try_begin),
				(eq, ":walled", 1),
				(party_get_slot, ":party_type", ":home", slot_party_type),
				(eq, ":party_type", spt_village),
				(party_get_slot, ":linked_center", ":home", slot_party_linked_party),
				(assign, ":home", ":linked_center"),
			(try_end),
			
			(assign, reg0, ":home"),
		]),
	
	# script_faction_get_best_candidate_for_center
	# input:
	# 	arg1: faction_no
	# 	arg2: center_no
	# output:
	# 	reg0: best_candidate
	("faction_get_best_candidate_for_center",
		[
			(store_script_param, ":faction_no", 1),
			(store_script_param, ":center_no", 2),
			
			(assign, ":best_candidate", -1),
			(assign, ":second_best", -1),
			(party_get_slot, ":party_type", ":center_no", slot_party_type),
			
			(try_begin),
				(eq, ":party_type", spt_village),
				(party_get_slot, ":linked_center", ":center_no", slot_party_linked_party),
				(party_get_slot, ":best_candidate", ":linked_center", slot_party_lord), # We take the lord of the linked center as choosen one
				(ge, ":best_candidate", 0),
			(else_try),
				(assign, ":end", lords_end),
				(try_for_range, ":troop_no", lords_begin, ":end"),
					(troop_slot_eq, ":troop_no", slot_troop_kingdom_occupation, tko_kingdom_hero),
					(store_troop_faction, ":troop_faction", ":troop_no"),
					(eq, ":troop_faction", ":faction_no"),
					
					(troop_get_slot, ":rank", ":troop_no", slot_troop_rank),
					
					(try_begin),
						(eq, ":party_type", spt_town),
						(try_begin),
							(le, ":rank", rank_village), # Only has a village or less
							(assign, ":best_candidate", ":troop_no"),
							(assign, ":end", -1),
						(else_try),
							(lt, ":rank", rank_city), # Does not have a city
							(assign, ":second_best", ":troop_no"),
						(try_end),
					(else_try),
						(eq, ":party_type", spt_castle),
						(try_begin),
							(le, ":rank", rank_village), # Only has a village or less
							(assign, ":best_candidate", ":troop_no"),
							(assign, ":end", -1),
						(else_try),
							(this_or_next|ge, ":rank", rank_city), # Has a city
							(eq, ":rank", rank_two_village), # Or has two villages
							(assign, ":second_best", ":troop_no"),
						(try_end),
					(else_try),
						(eq, ":party_type", spt_village),
						(try_begin),
							(lt, ":rank", rank_village), # Does not have a village
							(assign, ":best_candidate", ":troop_no"),
							(assign, ":end", -1),
						(else_try),
							(this_or_next|ge, ":rank", rank_city), # Has a city
							(eq, ":rank", rank_village), # Or a village
							(assign, ":second_best", ":troop_no"),
						(try_end),
					(try_end),
				(try_end),
			(try_end),
			
			(try_begin),
				(eq, ":best_candidate", -1),
				(assign, ":best_candidate", ":second_best"),
			(try_end),
			
			(assign, reg0, ":best_candidate"),
		]),
	
	# script_party_template_update_slots
	# input:
	# 	arg1: party_template
	# output:
	# 	reg0: updated
	("party_template_update_slots",
		[
			(store_script_param, ":party_template", 1),
			(party_clear, "p_temp_party"),
			
			(try_for_range, ":slot", slot_party_template_num_troop_1, slot_party_template_num_troop_6 + 1),
				(party_template_set_slot, ":party_template", ":slot", 100),
				(store_add, ":slot_sec", ":slot", 6),
				(party_template_set_slot, ":party_template", ":slot_sec", -1),
			(try_end),
			
			(assign, ":end", 20),
			(try_for_range, ":unused", 0, ":end"),
				(party_add_template, "p_temp_party", ":party_template"),
				
				(party_get_num_companion_stacks, ":num_stack", "p_temp_party"),
				(try_for_range, ":i_stack", 0, ":num_stack"),
					(party_stack_get_size, ":stack_size", "p_temp_party", ":i_stack"),
					(store_add, ":slot", ":i_stack", slot_party_template_num_troop_1),
					(party_template_slot_ge, ":party_template", ":slot", ":stack_size"),
					(party_template_set_slot, ":party_template", ":slot", ":stack_size"),
				(try_end),
				(party_clear, "p_temp_party"),
			(try_end),
			
			(party_add_template, "p_temp_party", ":party_template"),
			(party_get_num_companion_stacks, ":num_stack", "p_temp_party"),
			(try_for_range, ":i_stack", 0, ":num_stack"),
				(party_stack_get_troop_id, ":troop", "p_temp_party", ":i_stack"),
				(store_add, ":slot", ":i_stack", slot_party_template_type_troop_1),
				(party_template_set_slot, ":party_template", ":slot", ":troop"),
			(try_end),
			
			(party_clear, "p_temp_party"),
		]),
	
	# script_display_template_list
	# input: none
	# output: none
	("display_template_list",
		[
			(try_for_range, ":template", "pt_kingdom_1_reinforcements_peasant_a", "pt_village_template"),
				# (call_script, "script_party_template_update_slots", ":template"),
				
				(assign, reg10, ":template"),
				(str_store_string, s10, "@Template no {reg10} :"),
				(try_for_range, ":num_slot", slot_party_template_num_troop_1, slot_party_template_num_troop_6 + 1),
					(store_add, ":troop_slot", ":num_slot", 6),
					(party_template_get_slot, ":troop", ":template", ":troop_slot"),
					(try_begin),
						(eq, ":troop", -1),
						(str_store_string, s10, "@{s10}"),
					(else_try),
						(party_template_get_slot, ":num_troop", ":template", ":num_slot"),
						(str_store_troop_name, s11, ":troop"),
						(assign, reg11, ":num_troop"),
						(str_store_string, s10, "@{s10} {s11}-{reg11}."),
					(try_end),
				(try_end),
				(display_log_message, "@{s10}"),
			(try_end),
		]),
	
	# script_party_count_fit_for_battle
	# Returns the number of unwounded companions in a party
	# input:
	# 	arg1: party_id
	# output: 
	# 	reg0: result
	("party_count_fit_for_battle",
		[
			(store_script_param_1, ":party"),
			(party_get_num_companion_stacks, ":num_stacks",":party"),
			(assign, reg0, 0),
			(try_for_range, ":i_stack", 0, ":num_stacks"),
				(party_stack_get_troop_id, ":stack_troop",":party",":i_stack"),
				(assign, ":num_fit",0),
				(try_begin),
					(troop_is_hero, ":stack_troop"),
					(try_begin),
						(neg|troop_is_wounded, ":stack_troop"),
						(assign, ":num_fit", 1),
					(try_end),
				(else_try),
					(party_stack_get_size, ":num_fit", ":party", ":i_stack"),
					(party_stack_get_num_wounded, ":num_wounded", ":party", ":i_stack"),
					(val_sub, ":num_fit", ":num_wounded"),
				(try_end),
				(val_add, reg0, ":num_fit"),
			(try_end),
		]),
	
	# script_troop_use_template_troop
	# input:
	# 	arg1: troop_no
	# 	arg2: template_troop
	# output: none
	("troop_use_template_troop",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":template", 2),
			
			(set_show_messages, 0),
			
			(call_script, "script_troop_change_stat_with_template", ":troop_no", ":template"),
					
			# Removing old equipment
			(try_for_range, ":equip_slot", ek_item_0, ek_food),
				(troop_get_inventory_slot, ":item", ":troop_no", ":equip_slot"),
				(gt, ":item", 0),
				(troop_remove_item, ":troop_no", ":item"),
			(try_end),
			(troop_clear_inventory, ":troop_no"),
			
			(call_script, "script_troop_take_random_troop_equipement_of_type", ":troop_no", ":template", itp_type_head_armor),
			(call_script, "script_troop_take_random_troop_equipement_of_type", ":troop_no", ":template", itp_type_foot_armor),
			(call_script, "script_troop_take_random_troop_equipement_of_type", ":troop_no", ":template", itp_type_body_armor),
			(call_script, "script_troop_take_random_troop_equipement_of_type", ":troop_no", ":template", itp_type_hand_armor),
			
			(assign, ":num_item_added", 0),
			
			(try_begin),
				(troop_get_inventory_capacity, ":num_slots", ":template"),
				(assign, ":num_item", 0),
				(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
					(troop_get_inventory_slot, ":cur_item", ":template", ":i_slot"),
					(gt, ":cur_item", 0),
					(item_get_type, ":item_type", ":cur_item"),
					(this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
					(eq, ":item_type", itp_type_two_handed_wpn),
					(val_add, ":num_item", 1),
				(try_end),
				(try_begin),
					(gt, ":num_item", 0),
					(store_random_in_range, ":random_item", 0, ":num_item"),
					(try_for_range, ":i_slot", ek_item_0, ":num_slots"),
						(troop_get_inventory_slot, ":cur_item", ":template", ":i_slot"),
						(gt, ":cur_item", 0),
						(item_get_type, ":item_type", ":cur_item"),
						(this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
						(eq, ":item_type", itp_type_two_handed_wpn),
						(try_begin),
							(eq, ":random_item", 0),
							(troop_add_item, ":troop_no", ":cur_item"),
							(val_add, ":num_item_added", 1),
							(assign, ":num_slots", 0),
						(else_try),
							(val_add, ":random_item", -1),
						(try_end),
					(try_end),
				(try_end),
				(store_random_in_range, ":random", 0, 2),
				(try_begin),
					(this_or_next|eq, ":num_item", 0),
					(eq, ":random", 0),
					(call_script, "script_troop_take_random_troop_equipement_of_type", ":troop_no", ":template", itp_type_polearm),
					(gt, reg0, 0),
					(val_add, ":num_item_added", 1),
				(try_end),
			(try_end),
			(store_random_in_range, ":random", 0, 2),
			(try_begin),
				(this_or_next|troop_is_guarantee_ranged, ":template"),
				(eq, ":random", 0),
				(call_script, "script_troop_take_random_troop_equipement_of_type", "trp_temp_troop", ":template", itp_type_bow),
				(assign, ":has_bow", reg0),
				(call_script, "script_troop_take_random_troop_equipement_of_type", "trp_temp_troop", ":template", itp_type_crossbow),
				(assign, ":has_xbow", reg0),
				(call_script, "script_troop_take_random_troop_equipement_of_type", "trp_temp_troop", ":template", itp_type_thrown),
				(assign, ":has_throw", reg0),
				(try_begin),
					(gt, ":has_bow", 0),
					(le, ":has_xbow", 0),
					(le, ":has_throw", 0),
					(troop_add_item, ":troop_no", ":has_bow"),
					(val_add, ":num_item_added", 1),
					(call_script, "script_troop_take_random_troop_equipement_of_type", ":troop_no", ":template", itp_type_arrows),
					(val_add, ":num_item_added", 1),
				(else_try),
					(le, ":has_bow", 0),
					(gt, ":has_xbow", 0),
					(le, ":has_throw", 0),
					(troop_add_item, ":troop_no", ":has_xbow"),
					(val_add, ":num_item_added", 1),
					(call_script, "script_troop_take_random_troop_equipement_of_type", ":troop_no", ":template", itp_type_bolts),
					(val_add, ":num_item_added", 1),
				(else_try),
					(le, ":has_bow", 0),
					(le, ":has_xbow", 0),
					(gt, ":has_throw", 0),
					(troop_add_item, ":troop_no", ":has_throw"),
					(val_add, ":num_item_added", 1),
				(else_try),
					(store_random_in_range, ":random_type", 0, 2),
					(try_begin),
						(eq, ":random_type", 0),
						(try_begin),
							(gt, ":has_bow", 0),
							(troop_add_item, ":troop_no", ":has_bow"),
							(val_add, ":num_item_added", 1),
							(call_script, "script_troop_take_random_troop_equipement_of_type", ":troop_no", ":template", itp_type_arrows),
							(val_add, ":num_item_added", 1),
						(else_try),
							(gt, ":has_xbow", 0),
							(troop_add_item, ":troop_no", ":has_xbow"),
							(val_add, ":num_item_added", 1),
							(call_script, "script_troop_take_random_troop_equipement_of_type", ":troop_no", ":template", itp_type_bolts),
							(val_add, ":num_item_added", 1),
						(try_end),
					(else_try),
						(try_begin),
							(gt, ":has_xbow", 0),
							(troop_add_item, ":troop_no", ":has_xbow"),
							(val_add, ":num_item_added", 1),
							(call_script, "script_troop_take_random_troop_equipement_of_type", ":troop_no", ":template", itp_type_bolts),
							(val_add, ":num_item_added", 1),
						(else_try),
							(gt, ":has_throw", 0),
							(troop_add_item, ":troop_no", ":has_throw"),
							(val_add, ":num_item_added", 1),
						(try_end),
					(try_end),
				(try_end),
			(try_end),
			
			(try_begin),
				(lt, ":num_item_added", 4),
				(call_script, "script_troop_take_random_troop_equipement_of_type", ":troop_no", ":template", itp_type_shield),
			(try_end),
			
			(store_random_in_range, ":random", 0, 2),
			(try_begin),
				(this_or_next|troop_is_guarantee_horse, ":template"),
				(eq, ":random", 0),
				
				(call_script, "script_troop_take_random_troop_equipement_of_type", ":troop_no", ":template", itp_type_horse),
			(try_end),
			
			(troop_equip_items, ":troop_no"),
			
			(set_show_messages, 1),
		]),
	
	# script_calculate_hire_troop_cost
	# input:
	# 	arg1: center_to_recruit
	# 	arg2: troop_recruiter
	# output:
	# 	reg0: total cost
	# 	reg1: num troops
	("calculate_hire_troop_cost",
	[
		(store_script_param, ":current_city", 1),
		(store_script_param, ":recruiter", 2),
		
		(assign, ":total_cost", 0),
		(assign, ":total_num_troops", 0),
		(party_get_num_companion_stacks, ":num_stacks", ":current_city"),
		(try_for_range, ":stack_no", 0, ":num_stacks"),
			(party_stack_get_troop_id, ":troop_no", ":current_city", ":stack_no"),
			# (party_stack_get_size, ":stack_size", ":current_city", ":stack_no"),
			
			(store_mul, ":numbox_offset", ":stack_no", 2),
			(val_add, ":numbox_offset", 1),
			
			# (store_add, ":numbox_object", ":numbox_offset", "$g_hire_soldiers_center_troops_begin"),
			(troop_get_slot, ":num_troops", ":troop_no", slot_troop_temp_hire_number),
			
			(call_script, "script_troop_get_cost", ":troop_no"),
			(assign, ":troop_cost", reg0),
			(val_mul, ":troop_cost", ":num_troops"),
			
			(val_add, ":total_num_troops", ":num_troops"),
			
			(call_script, "script_troop_get_cost_modifier", ":troop_no", ":current_city", ":recruiter"),
			(assign, ":cost_modifier", reg0),
			(val_mul, ":troop_cost", ":cost_modifier"),
			(val_div, ":troop_cost", 100),
			
			(val_add, ":total_cost", ":troop_cost"),
		(try_end),
		(assign, reg0, ":total_cost"),
		(assign, reg1, ":total_num_troops"),
	]),
	
	# script_troop_get_cost
	# input: 
	# 	arg1: troop_id
	# output:
	# 	reg0: troop cost
	("troop_get_cost",
	[
		(store_script_param_1, ":troop_id"),
		
		(store_character_level, ":level", ":troop_id"),
		
		(store_add, ":join_cost", ":level", 1),
		(val_mul, ":join_cost", ":join_cost"),
		(val_div, ":join_cost", 4),
		(val_add, ":join_cost", 20),
		
		(try_begin),
			(troop_is_mounted, ":troop_id"), # 50% increase for mounted troops
			(val_mul, ":join_cost", 3),
			(val_div, ":join_cost", 2),
		(try_end),
		
		(assign, reg0, ":join_cost"), 
	]),
	
	# script_troop_get_cost_modifier
	# input:
	# 	arg1: troop_no
	# 	arg2: current_party
	# 	arg3: recruiter
	# output:
	# 	reg0: cost_modifier
	("troop_get_cost_modifier",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":current_party", 2),
			(store_script_param, ":recruiter", 3),
			
			(assign, ":modifier", 100),
			
			(party_get_slot, ":party_type", ":current_party", slot_party_type),
			(store_troop_faction, ":troop_faction", ":troop_no"),
			(faction_get_slot, ":culture", ":troop_faction", slot_faction_culture),
			(faction_get_slot, ":peasant_begin", ":culture", slot_faction_troops_begin),
			(faction_get_slot, ":common_begin", ":culture", slot_faction_common_begin),
			(faction_get_slot, ":veteran_begin", ":culture", slot_faction_veteran_begin),
			(faction_get_slot, ":elite_begin", ":culture", slot_faction_elite_begin),
			# (faction_get_slot, ":noble_begin", ":culture", slot_faction_noble_begin),
			(faction_get_slot, ":troops_end", ":culture", slot_faction_troops_end),
			
			(store_faction_of_party, ":party_faction", ":current_party"),
			
			(try_begin),
				(eq, ":party_type", spt_village),
				# (assign, ":relation_divider", 4),
				(try_begin),
					(is_between, ":troop_no", ":peasant_begin", ":common_begin"),
					(val_add, ":modifier", -10), # 10% reduction on peasant troops in villages
				(else_try),
					(is_between, ":troop_no", ":common_begin", ":veteran_begin"),
					(val_add, ":modifier", -5), # 5% reduction on common troops in villages
				(else_try),
					(is_between, ":troop_no", ":elite_begin", ":troops_end"),
					(val_add, ":modifier", 10), # 10% increase on elite/noble troops in villages
				(try_end),
			(else_try),
				(eq, ":party_type", spt_castle),
				# (assign, ":relation_divider", 10),
				(try_begin),
					(is_between, ":troop_no", ":peasant_begin", ":common_begin"),
					(val_add, ":modifier", 5), # 5% increase on peasant troops in castles
				(else_try),
					(is_between, ":troop_no", ":veteran_begin", ":troops_end"),
					(val_add, ":modifier", -5), # 5% reduction on veteran, elite and noble troops in castles
				(try_end),
			(try_end),
			
			# (assign, ":relation_divider", 8),
			(party_get_slot, ":center_owner", ":current_party", slot_party_lord),
			
			(try_begin),
				# Used for center reinforcements
				(eq, ":recruiter", ":center_owner"),
				(val_add, ":modifier", -50),
			(else_try),
				
				(store_troop_faction, ":recruiter_faction", ":recruiter"),
				(try_begin),
					(neq, ":party_faction", ":recruiter_faction"),
					(val_add, ":modifier", 10),
				(try_end),
				
				# ToDo:
				# (try_begin),
					# (ge, ":center_owner", 0),
					# (call_script, "script_troop_get_relation_with_troop", ":recruiter", ":center_owner"),
					# (assign, ":relation", reg0),
					# (try_begin), # Player has relation with owner and center
						# (eq, ":recruiter", "trp_player"),
						# (val_add, ":relation", 1),
						# (val_div, ":relation", 2),
						# (troop_get_slot, ":city_relation", ":current_party", slot_party_relation_with_player),
						# (val_div, ":city_relation", 2),
						# (val_add, ":relation", ":city_relation"),
					# (try_end),
					# (val_div, ":relation", ":relation_divider"),
					# (val_sub, ":modifier", ":relation"),
				# (try_end),
			(try_end),
			
			(faction_get_slot, ":party_culture", ":party_faction", slot_faction_culture),
			(try_begin), # If troop is from another faction we increase its price
				(neq, ":culture", ":party_culture"),
				(val_add, ":modifier", 25),
			(try_end),
			
			(store_skill_level, ":trade_skill", skl_trade, ":recruiter"),
			(store_skill_level, ":persuasion_skill", skl_persuasion, ":recruiter"),
			(val_div, ":persuasion_skill", 2),
			
			(val_sub, ":modifier", ":trade_skill"),
			(val_sub, ":modifier", ":persuasion_skill"),
			
			(val_max, ":modifier", 20),
			
			(assign, reg0, ":modifier"),
		]),
	
	# script_troop_get_info
	# input:
	# 	arg1: troop_no
	# output:
	# 	s0: troop info
	# 	reg0: num_lines
	("troop_get_info",
		[
			(store_script_param, ":troop_no", 1),
			
			(str_clear, s0),
			
			(assign, ":num_lines", 0),
			
			(store_attribute_level, reg11, ":troop_no", ca_strength),
			(store_attribute_level, reg12, ":troop_no", ca_agility),
			(store_attribute_level, reg13, ":troop_no", ca_intelligence),
			(store_attribute_level, reg14, ":troop_no", ca_charisma),
			# (store_character_level, reg10, ":troop_no"),
			(store_skill_level, ":ironflesh", skl_ironflesh, ":troop_no"),
			(store_mul, reg10, ":ironflesh", 2),
			(val_add, reg10, reg11),
			(val_add, reg10, 35),
			
			# (str_store_string, s0, "@Level: {reg10}^Strength: {reg11}^Agility: {reg12}^Intelligence: {reg13}^Charisma: {reg14}^"),
			(str_store_string, s0, "@Strength: {reg11}^Agility: {reg12}^Intelligence: {reg13}^Charisma: {reg14}^Health: {reg10}^"),
			(val_add, ":num_lines", 6),
			
			(assign, ":has_1h", 0),
			(assign, ":has_2h", 0),
			(assign, ":has_pole", 0),
			(assign, ":has_bow", 0),
			(assign, ":has_xbow", 0),
			(assign, ":has_throw", 0),
			(assign, ":has_horse", 0),
			(troop_get_inventory_capacity, ":capacity", ":troop_no"),
			(try_for_range, ":item_slot", ek_item_0, ":capacity"),
				(troop_get_inventory_slot, ":cur_item", ":troop_no", ":item_slot"),
				(gt, ":cur_item", 0),
				(item_get_type, ":item_type", ":cur_item"),
				(try_begin),
					(this_or_next|is_between, ":cur_item", "itm_bastard_sword_a", "itm_sword_of_war"),
					(this_or_next|eq, ":cur_item", "itm_morningstar"),
					(eq, ":cur_item", "itm_club_with_spike_head"), # Special onehanded/twohanded
					(assign, ":has_1h", 1),
					(assign, ":has_2h", 1),
				(else_try),
					(eq, ":item_type", itp_type_two_handed_wpn),
					(assign, ":has_2h", 1),
				(else_try),
					(eq, ":item_type", itp_type_polearm),
					(assign, ":has_pole", 1),
				(else_try),
					(eq, ":item_type", itp_type_bow),
					(assign, ":has_bow", 1),
				(else_try),
					(eq, ":item_type", itp_type_crossbow),
					(assign, ":has_xbow", 1),
				(else_try),
					(eq, ":item_type", itp_type_thrown),
					(assign, ":has_throw", 1),
				(else_try),
					(eq, ":item_type", itp_type_horse),
					(assign, ":has_horse", 1),
				(else_try),
					(eq, ":item_type", itp_type_one_handed_wpn),
					(assign, ":has_1h", 1),
				(try_end),
			(try_end),
			
			(assign, reg5, 0),
			(try_begin),
				(troop_is_guarantee_ranged, ":troop_no"),
				(assign, reg5, 1),
			(try_end),
			
			(try_begin),
				(eq, ":has_1h", 1),
				(store_proficiency_level, reg10, ":troop_no", wpt_one_handed_weapon),
				(str_store_string, s0, "@{s0}^One-handed: {reg10}"),
				(val_add, ":num_lines", 1),
			(try_end),
			(try_begin),
				(eq, ":has_2h", 1),
				(store_proficiency_level, reg10, ":troop_no", wpt_two_handed_weapon),
				(str_store_string, s0, "@{s0}^Two-handed: {reg10}"),
				(val_add, ":num_lines", 1),
			(try_end),
			(try_begin),
				(eq, ":has_pole", 1),
				(store_proficiency_level, reg10, ":troop_no", wpt_polearm),
				(str_store_string, s0, "@{s0}^Polearm: {reg10}"),
				(val_add, ":num_lines", 1),
			(try_end),
			(try_begin),
				(eq, ":has_bow", 1),
				(store_proficiency_level, reg10, ":troop_no", wpt_archery),
				(str_store_string, s0, "@{s0}^Archery: {reg10} {reg5?(*):}"),
				(val_add, ":num_lines", 1),
			(try_end),
			(try_begin),
				(eq, ":has_xbow", 1),
				(store_proficiency_level, reg10, ":troop_no", wpt_crossbow),
				(str_store_string, s0, "@{s0}^Crossbow: {reg10} {reg5?(*):}"),
				(val_add, ":num_lines", 1),
			(try_end),
			(try_begin),
				(eq, ":has_throw", 1),
				(store_proficiency_level, reg10, ":troop_no", wpt_throwing),
				(str_store_string, s0, "@{s0}^Throwing: {reg10} {reg5?(*):}"),
				(val_add, ":num_lines", 1),
			(try_end),
			
			# (store_skill_level, reg10, skl_ironflesh, ":troop_no"),
			(assign, reg10, ":ironflesh"),
			(store_skill_level, reg11, skl_power_strike, ":troop_no"),
			(str_store_string, s0, "@{s0}^^Ironflesh: {reg10}^Power Strike: {reg11}"),
			(val_add, ":num_lines", 3),
			
			(try_begin),
				(eq, ":has_bow", 1),
				(store_skill_level, reg10, skl_power_draw, ":troop_no"),
				(str_store_string, s0, "@{s0}^Power Draw: {reg10}"),
				(val_add, ":num_lines", 1),
			(try_end),
			(try_begin),
				(eq, ":has_throw", 1),
				(store_skill_level, reg10, skl_power_throw, ":troop_no"),
				(str_store_string, s0, "@{s0}^Power Throw: {reg10}"),
				(val_add, ":num_lines", 1),
			(try_end),
			
			(try_begin),
				(store_skill_level, reg10, skl_shield, ":troop_no"),
				(gt, reg10, 0),
				(str_store_string, s0, "@{s0}^Shield: {reg10}"),
				(val_add, ":num_lines", 1),
			(try_end),
			
			(store_skill_level, reg10, skl_athletics, ":troop_no"),
			(str_store_string, s0, "@{s0}^Athletics: {reg10}"),
			(val_add, ":num_lines", 1),
			
			(try_begin),
				(eq, ":has_horse", 1),
				(store_skill_level, reg10, skl_riding, ":troop_no"),
				(str_store_string, s0, "@{s0}^Riding: {reg10}"),
				(val_add, ":num_lines", 1),
				(try_begin),
					(this_or_next|eq, ":has_bow", 1),
					(this_or_next|eq, ":has_xbow", 1),
					(eq, ":has_throw", 1),
					(store_skill_level, reg10, skl_horse_archery, ":troop_no"),
					(str_store_string, s0, "@{s0}^Horse Archery: {reg10}"),
					(val_add, ":num_lines", 1),
				(try_end),
			(try_end),
			
			(assign, reg0, ":num_lines"),
		]),
	
	# script_troop_get_description
	# input:
	# 	arg1: troop_id
	# output:
	# 	s0: troop_description
	# 	reg0: num_lines
	("troop_get_description",
		[
			(store_script_param, ":troop_no", 1),
			
			(troop_get_slot, ":troop_type", ":troop_no", slot_troop_type),
			(store_add, ":str", "str_names_end", ":troop_type"),
			
			(troop_get_slot, ":armor", ":troop_no", slot_troop_armor_weight),
			(troop_get_slot, ":horse", ":troop_no", slot_troop_horse_weight),
			(troop_get_slot, ":weapon", ":troop_no", slot_troop_ranged_weapon_weight),
			
			(troop_get_slot, ":quality", ":troop_no", slot_troop_quality),
			(store_add, ":quality_str", ":quality", "str_troop_quality_peasant"),
			(str_store_string, s13, ":quality_str"),
			
			# (str_clear, s0),
			
			(str_store_string, s14, ":str"),
			(str_store_string, s0, "@{s13} {s14}"),
			
			(assign, ":num_lines", 1),
			
			(try_begin),
				(ge, ":armor", 0),
				(store_add, ":armor_string", ":armor", "str_weight_very_light"),
				(str_store_string, s10, ":armor_string"),
				(str_store_string, s0, "@{s0}^{s10} armor"),
				(val_add, ":num_lines", 1),
			(try_end),
			(try_begin),
				(ge, ":horse", 0),
				(store_add, ":horse_string", ":horse", "str_weight_very_light"),
				(str_store_string, s11, ":horse_string"),
				(str_store_string, s0, "@{s0}^{s11} horse"),
				(val_add, ":num_lines", 1),
			(try_end),
			(try_begin),
				(ge, ":weapon", 0),
				(store_add, ":weapon_string", ":weapon", "str_weight_very_light"),
				(str_store_string, s12, ":weapon_string"),
				(str_store_string, s0, "@{s0}^{s12} ranged weapons"),
				(val_add, ":num_lines", 1),
			(try_end),
			
			(assign, reg0, ":num_lines"),
		]),
	
	# script_setup_troop_meeting
	# input:
	# 	arg1: troop_id
	# 	arg2: troop_dna
	# output: none
	("setup_troop_meeting",
    [
		(store_script_param_1, ":meeting_troop"),
		(store_script_param_2, ":troop_dna"),
		(call_script, "script_get_meeting_scene"),
		(assign, ":meeting_scene", reg0),
		(modify_visitors_at_site,":meeting_scene"),
		(reset_visitors),
		(set_visitor,0,"trp_player"),
		(try_begin),
			(gt, ":troop_dna", -1),
			(set_visitor,17,":meeting_troop",":troop_dna"),
		(else_try),
			(set_visitor,17,":meeting_troop"),
		(try_end),
		(set_jump_mission,"mt_conversation_encounter"),
		(jump_to_scene,":meeting_scene"),
		(change_screen_map_conversation, ":meeting_troop"),
	]),
	
	# script_setup_party_meeting
	# input:
	# 	arg1: party_id
	# output: none
	("setup_party_meeting",
	[
		(store_script_param_1, ":meeting_party"),
		
		(party_stack_get_troop_id, ":meeting_troop",":meeting_party",0),
		(party_stack_get_troop_dna,":troop_dna",":meeting_party",0),
		
		(call_script, "script_setup_troop_meeting", ":meeting_troop", ":troop_dna"),
	]),
	
	# script_get_meeting_scene
	# input: none
	# output:
	# 	reg0: contain suitable scene_no
	("get_meeting_scene",
	[
		(party_get_current_terrain, ":terrain_type", "p_main_party"),
		# (assign, ":scene_to_use", "scn_random_scene"),
		(try_begin),
			(eq, ":terrain_type", rt_steppe),
			(assign, ":scene_to_use", "scn_meeting_scene_steppe"),
		(else_try),
			(eq, ":terrain_type", rt_plain),
			(assign, ":scene_to_use", "scn_meeting_scene_plain"),
		(else_try),
			(eq, ":terrain_type", rt_snow),
			(assign, ":scene_to_use", "scn_meeting_scene_snow"),
		(else_try),
			(eq, ":terrain_type", rt_desert),
			(assign, ":scene_to_use", "scn_meeting_scene_desert"),
		(else_try),
			(eq, ":terrain_type", rt_steppe_forest),
			(assign, ":scene_to_use", "scn_meeting_scene_steppe"),
		(else_try),
			(eq, ":terrain_type", rt_forest),
			(assign, ":scene_to_use", "scn_meeting_scene_plain"),
		(else_try),
			(eq, ":terrain_type", rt_snow_forest),
			(assign, ":scene_to_use", "scn_meeting_scene_snow"),
		(else_try),
			(eq, ":terrain_type", rt_desert_forest),
			(assign, ":scene_to_use", "scn_meeting_scene_desert"),
		(else_try),
			(assign, ":scene_to_use", "scn_meeting_scene_plain"),
		(try_end),
		(assign, reg0, ":scene_to_use"),
	]),
	
	# script_get_battle_scene
	# input: none
	# output:
	# 	reg0: contain suitable scene_no
	("get_battle_scene",
	[
		(party_get_current_terrain, ":terrain_type", "p_main_party"),
		# (assign, ":scene_to_use", "scn_random_scene"),
		(try_begin),
			(eq, ":terrain_type", rt_steppe),
			(assign, ":scene_to_use", "scn_random_scene_steppe"),
		(else_try),
			(eq, ":terrain_type", rt_plain),
			(assign, ":scene_to_use", "scn_random_scene_plain"),
		(else_try),
			(eq, ":terrain_type", rt_snow),
			(assign, ":scene_to_use", "scn_random_scene_snow"),
		(else_try),
			(eq, ":terrain_type", rt_desert),
			(assign, ":scene_to_use", "scn_random_scene_desert"),
		(else_try),
			(eq, ":terrain_type", rt_steppe_forest),
			(assign, ":scene_to_use", "scn_random_scene_steppe_forest"),
		(else_try),
			(eq, ":terrain_type", rt_forest),
			(assign, ":scene_to_use", "scn_random_scene_plain_forest"),
		(else_try),
			(eq, ":terrain_type", rt_snow_forest),
			(assign, ":scene_to_use", "scn_random_scene_snow_forest"),
		(else_try),
			(eq, ":terrain_type", rt_desert_forest),
			(assign, ":scene_to_use", "scn_random_scene_desert_forest"),
		(else_try),
			(assign, ":scene_to_use", "scn_meeting_scene_plain"),
		(try_end),
		(assign, reg0, ":scene_to_use"),
	]),
	
	# script_init_mercenaries
	# input: none
	# output: none
	("init_mercenaries",
		[
			(call_script, "script_troop_change_stat_with_template", "trp_swadian_mercenary_cavalry", "trp_swadian_squire"),
			# (call_script, "script_troop_copy_items_from_troop", "trp_swadian_mercenary_cavalry", "trp_swadian_squire"),
			# (troop_remove_item, "trp_swadian_mercenary_cavalry", "itm_lance"),
			(call_script, "script_troop_change_stat_with_template", "trp_swadian_mercenary_infantry", "trp_swadian_guard"),
			# (call_script, "script_troop_copy_items_from_troop", "trp_swadian_mercenary_infantry", "trp_swadian_guard"),
			# (call_script, "script_troop_remove_weapons", "trp_swadian_mercenary_infantry"),
			# (call_script, "script_troop_copy_items_of_type_from_troop", "trp_swadian_mercenary_infantry", "trp_swadian_heavy_infantry", itp_type_one_handed_wpn),
			# (troop_add_item, "trp_swadian_mercenary_infantry", "itm_tab_shield_heater_d"),
			(troop_raise_skill, "trp_swadian_mercenary_infantry", skl_power_strike, -2),
			
			(call_script, "script_troop_change_stat_with_template", "trp_vaegir_mercenary_cavalry", "trp_vaegir_heavy_cavalry"),
			# (call_script, "script_troop_copy_items_from_troop", "trp_vaegir_mercenary_cavalry", "trp_vaegir_heavy_cavalry"),
			# (call_script, "script_troop_remove_weapons", "trp_vaegir_mercenary_cavalry"),
			# (call_script, "script_troop_remove_items_of_type", "trp_vaegir_mercenary_cavalry", itp_type_body_armor),
			# (troop_add_item, "trp_vaegir_mercenary_cavalry", "itm_scimitar"),
			# (troop_add_item, "trp_vaegir_mercenary_cavalry", "itm_two_handed_battle_axe_2"),
			# (troop_add_item, "trp_vaegir_mercenary_cavalry", "itm_tab_shield_kite_cav_a"),
			# (troop_add_item, "trp_vaegir_mercenary_cavalry", "itm_studded_leather_coat"),
			(call_script, "script_troop_change_stat_with_template", "trp_vaegir_mercenary_bowman", "trp_vaegir_heavy_bowman"),
			# (call_script, "script_troop_copy_items_from_troop", "trp_vaegir_mercenary_bowman", "trp_vaegir_heavy_bowman"),
			# (call_script, "script_troop_remove_items_of_type", "trp_vaegir_mercenary_bowman", itp_type_shield),
			# (call_script, "script_troop_remove_items_of_type", "trp_vaegir_mercenary_bowman", itp_type_body_armor),
			# (call_script, "script_troop_remove_items_of_type", "trp_vaegir_mercenary_bowman", itp_type_foot_armor),
			# (troop_add_item, "trp_vaegir_mercenary_bowman", "itm_leather_jerkin"),
			# (troop_add_item, "trp_vaegir_mercenary_bowman", "itm_leather_boots"),
			# (troop_add_item, "trp_vaegir_mercenary_bowman", "itm_bodkin_arrows"),
			
			(call_script, "script_troop_change_stat_with_template", "trp_khergit_mercenary_lancer", "trp_khergit_lancer"),
			# (call_script, "script_troop_copy_items_from_troop", "trp_khergit_mercenary_lancer", "trp_khergit_lancer"),
			# (call_script, "script_troop_remove_items_of_type", "trp_khergit_mercenary_lancer", itp_type_horse),
			# (troop_add_item, "trp_khergit_mercenary_lancer", "itm_courser"),
			(call_script, "script_troop_change_stat_with_template", "trp_khergit_mercenary_horse_archer", "trp_khergit_heavy_horse_archer"),
			# (call_script, "script_troop_copy_items_from_troop", "trp_khergit_mercenary_horse_archer", "trp_khergit_heavy_horse_archer"),
			# (call_script, "script_troop_remove_items_of_type", "trp_khergit_mercenary_horse_archer", itp_type_shield),
			# (call_script, "script_troop_remove_items_of_type", "trp_khergit_mercenary_horse_archer", itp_type_body_armor),
			# (call_script, "script_troop_remove_items_of_type", "trp_khergit_mercenary_horse_archer", itp_type_foot_armor),
			# (troop_add_item, "trp_khergit_mercenary_horse_archer", "itm_tribal_warrior_outfit"),
			# (troop_add_item, "trp_khergit_mercenary_horse_archer", "itm_leather_boots"),
			
			(call_script, "script_troop_change_stat_with_template", "trp_nord_mercenary_infantry", "trp_nord_medium_infantry"),
			# (call_script, "script_troop_copy_items_from_troop", "trp_nord_mercenary_infantry", "trp_nord_medium_infantry"),
			# (call_script, "script_troop_remove_items_of_type", "trp_nord_mercenary_infantry", itp_type_thrown),
			# (call_script, "script_troop_remove_items_of_type", "trp_nord_mercenary_infantry", itp_type_body_armor),
			# (troop_add_item, "trp_nord_mercenary_infantry", "itm_byrnie"),
			(call_script, "script_troop_change_stat_with_template", "trp_nord_mercenary_longbowman", "trp_nord_heavy_longbowman"),
			# (call_script, "script_troop_copy_items_from_troop", "trp_nord_mercenary_longbowman", "trp_nord_heavy_longbowman"),
			
			(call_script, "script_troop_change_stat_with_template", "trp_rhodok_mercenary_pikeman", "trp_rhodok_pikeman"),
			# (call_script, "script_troop_copy_items_from_troop", "trp_rhodok_mercenary_pikeman", "trp_rhodok_pikeman"),
			# (call_script, "script_troop_remove_items_of_type", "trp_rhodok_mercenary_pikeman", itp_type_body_armor),
			# (call_script, "script_troop_remove_items_of_type", "trp_rhodok_mercenary_pikeman", itp_type_head_armor),
			# (call_script, "script_troop_copy_items_of_type_from_troop", "trp_rhodok_mercenary_pikeman", "trp_rhodok_spearman", itp_type_body_armor),
			# (call_script, "script_troop_copy_items_of_type_from_troop", "trp_rhodok_mercenary_pikeman", "trp_rhodok_spearman", itp_type_head_armor),
			(call_script, "script_troop_change_stat_with_template", "trp_rhodok_mercenary_crossbowman", "trp_rhodok_medium_crossbowman"),
			# (call_script, "script_troop_copy_items_from_troop", "trp_rhodok_mercenary_crossbowman", "trp_rhodok_medium_crossbowman"),
			# (call_script, "script_troop_remove_items_of_type", "trp_rhodok_mercenary_crossbowman", itp_type_body_armor),
			# (troop_add_item, "trp_rhodok_mercenary_crossbowman", "itm_aketon_green"),
			
			(call_script, "script_troop_change_stat_with_template", "trp_sarranid_mercenary_cavalry", "trp_sarranid_medium_cavalry"),
			# (call_script, "script_troop_copy_items_from_troop", "trp_sarranid_mercenary_cavalry", "trp_sarranid_medium_cavalry"),
			# (call_script, "script_troop_remove_items_of_type", "trp_sarranid_mercenary_cavalry", itp_type_body_armor),
			# (troop_add_item, "trp_sarranid_mercenary_cavalry", "itm_sarranid_cavalry_robe"),
			# (troop_add_item, "trp_sarranid_mercenary_cavalry", "itm_bamboo_spear"),
			(call_script, "script_troop_change_stat_with_template", "trp_sarranid_mercenary_skirmisher", "trp_sarranid_heavy_skirmisher"),
			# (call_script, "script_troop_copy_items_from_troop", "trp_sarranid_mercenary_skirmisher", "trp_sarranid_heavy_skirmisher"),
			# (call_script, "script_troop_remove_items_of_type", "trp_sarranid_mercenary_skirmisher", itp_type_body_armor),
			# (call_script, "script_troop_remove_items_of_type", "trp_sarranid_mercenary_skirmisher", itp_type_thrown),
			# (troop_add_item, "trp_sarranid_mercenary_skirmisher", "itm_javelin"),
			# (troop_add_item, "trp_sarranid_mercenary_skirmisher", "itm_javelin"),
			# (troop_add_item, "trp_sarranid_mercenary_skirmisher", "itm_sarranid_cavalry_robe"),
			# (troop_add_item, "trp_sarranid_mercenary_skirmisher", "itm_tab_shield_kite_c"),
			(troop_raise_skill, "trp_sarranid_mercenary_skirmisher", skl_power_throw, -1),
			
			(try_for_range, ":troop_no", factional_mercenaries_begin, mercenaries_end),
				(call_script, "script_troop_adjust_mercenary_stats", ":troop_no"),
				(troop_equip_items, ":troop_no"),
			(try_end),
		]),
	
	# script_troop_copy_items_from_troop
	# input:
	# 	arg1: recipient
	# 	arg2: troop_to_copy
	# output: none
	("troop_copy_items_from_troop",
		[
			(store_script_param, ":recipient", 1),
			(store_script_param, ":troop_no", 2),
			
			(troop_get_inventory_capacity, ":num_stacks", ":troop_no"),
			(try_for_range, ":cur_stack", 0, ":num_stacks"),
				(troop_get_inventory_slot, ":cur_item", ":troop_no", ":cur_stack"),
				(gt, ":cur_item", 0),
				(troop_add_item, ":recipient", ":cur_item"),
			(try_end),
		]),
	
	# script_troop_copy_items_of_type_from_troop
	# input:
	# 	arg1: recipient
	# 	arg2: troop_to_copy
	# 	arg3: item_type
	# output: none
	("troop_copy_items_of_type_from_troop",
		[
			(store_script_param, ":recipient", 1),
			(store_script_param, ":troop_no", 2),
			(store_script_param, ":type", 3),
			
			(troop_get_inventory_capacity, ":num_stacks", ":troop_no"),
			(try_for_range, ":cur_stack", 0, ":num_stacks"),
				(troop_get_inventory_slot, ":cur_item", ":troop_no", ":cur_stack"),
				(gt, ":cur_item", 0),
				(item_get_type, ":item_type", ":cur_item"),
				(eq, ":item_type", ":type"),
				(troop_add_item, ":recipient", ":cur_item"),
			(try_end),
		]),
	
	# script_troop_adjust_mercenary_stats
	# input:
	# 	arg1: troop_no
	# output: none
	("troop_adjust_mercenary_stats",
		[
			(store_script_param, ":troop_no", 1),
			(troop_raise_attribute, ":troop_no", ca_strength, -1),
			(troop_raise_attribute, ":troop_no", ca_agility, -1),
			(troop_raise_attribute, ":troop_no", ca_intelligence, -2),
			(troop_raise_attribute, ":troop_no", ca_charisma, -1),
		]),
	
	# script_troop_remove_armor
	# input:
	# 	arg1: troop_no
	# output: none
	("troop_remove_armor",
		[
			(store_script_param, ":troop_no", 1),
			(troop_get_inventory_capacity, ":num_stacks", ":troop_no"),
			(try_for_range, ":cur_stack", 0, ":num_stacks"),
				(troop_get_inventory_slot, ":cur_item", ":troop_no", ":cur_stack"),
				(gt, ":cur_item", 0),
				(item_get_type, ":item_type", ":cur_item"),
				(is_between, ":item_type", itp_type_head_armor, itp_type_pistol),
				(troop_remove_item, ":troop_no", ":cur_item"),
			(try_end),
		]),
	
	# script_troop_remove_weapons
	# input:
	# 	arg1: troop_no
	# output: none
	("troop_remove_weapons",
		[
			(store_script_param, ":troop_no", 1),
			(troop_get_inventory_capacity, ":num_stacks", ":troop_no"),
			(try_for_range, ":cur_stack", 0, ":num_stacks"),
				(troop_get_inventory_slot, ":cur_item", ":troop_no", ":cur_stack"),
				(gt, ":cur_item", 0),
				(item_get_type, ":item_type", ":cur_item"),
				(is_between, ":item_type", itp_type_one_handed_wpn, itp_type_goods),
				(troop_remove_item, ":troop_no", ":cur_item"),
			(try_end),
		]),
	
	# script_troop_items_of_type
	# input:
	# 	arg1: troop_no
	# output: none
	("troop_remove_items_of_type",
		[
			(store_script_param, ":troop_no", 1),
			(store_script_param, ":type", 2),
			(troop_get_inventory_capacity, ":num_stacks", ":troop_no"),
			(try_for_range, ":cur_stack", 0, ":num_stacks"),
				(troop_get_inventory_slot, ":cur_item", ":troop_no", ":cur_stack"),
				(gt, ":cur_item", 0),
				(item_get_type, ":item_type", ":cur_item"),
				(eq, ":item_type", ":type"),
				(troop_remove_item, ":troop_no", ":cur_item"),
			(try_end),
		]),
	
	# ("",
		# [
		# ]),
]