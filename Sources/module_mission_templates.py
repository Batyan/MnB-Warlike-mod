from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from module_constants import *





##############
## Triggers ##
##############
# trigger_1 = (
    # 0, 0, 0, [],
		# []),

battle_siege_equalize_division = (
    15, 0, 0, 
	[],
	[
		(store_current_scene, ":cur_scene"),
		(scene_get_slot, ":num_points", ":cur_scene", slot_scene_num_defend_points),
		(store_add, ":end", ":num_points", grc_cavalry),
		
		(assign, ":slot", slot_team_division_3_number),
		(assign, ":num_total", 0),
		(try_for_range, ":unused", grc_cavalry, ":end"),
			(team_get_slot, ":num_current", 0, ":slot"),
			(val_add, ":num_total", ":num_current"),
			(val_add, ":slot", 1),
		(try_end),
		(store_div, ":avg", ":num_total", ":num_points"),
		(try_for_agents, ":agent_no"),
			(agent_is_alive, ":agent_no"),
			(agent_get_team, ":team", ":agent_no"),
			(eq, ":team", 0),
			(agent_get_division, ":division", ":agent_no"),
			(ge, ":division", grc_cavalry),
			(store_add, ":slot", ":division", slot_team_division_1_number),
			(team_get_slot, ":num_troops", 0, ":slot"),
			(try_begin),
				(gt, ":num_troops", ":avg"),
				(val_add, ":num_troops", -2),
				(gt, ":num_troops", ":avg"),
				(val_add, ":num_troops", 1),
				
				(store_random_in_range, ":random_division", grc_cavalry, ":end"),
				(agent_set_division, ":agent_no", ":random_division"),
				(agent_set_slot, ":agent_no", slot_agent_new_division, ":random_division"),
				
				(team_set_slot, 0, ":slot", ":num_troops"),
				(store_add, ":new_slot", ":random_division", slot_team_division_1_number),
				(team_get_slot, ":new_num_troops", 0, ":new_slot"),
				(val_add, ":new_num_troops", 1),
				(team_set_slot, ":new_slot", 0, ":new_num_troops"),
			(try_end),
		(try_end),
	])

test_battle_siege_spawn_troops = (
	10, 0, 0,
	[],
	[
		(try_for_range, ":cur_team", 0, 2),
			(assign, ":num_alive", 0),
			(try_for_agents, ":agent_no"),
				(agent_is_alive, ":agent_no"),
				(agent_is_human, ":agent_no"),
				(agent_get_team, ":team", ":agent_no"),
				(try_begin),
					(eq, ":team", ":cur_team"),
					(val_add, ":num_alive", 1),
				(try_end),
			(try_end),
			
			(assign, ":num_men_threshold", 50),
			
			(team_get_slot, ":faction_strength_bonus", ":cur_team", slot_team_test_strength),
			(val_add, ":faction_strength_bonus", 10),
			(val_mul, ":num_men_threshold", ":faction_strength_bonus"),
			(val_div, ":num_men_threshold", 10),
			
			(team_get_slot, ":faction", ":cur_team", slot_team_test_faction),
			(call_script, "script_faction_get_party_size_modifier", ":faction"),
			(val_mul, ":num_men_threshold", reg0),
			(val_div, ":num_men_threshold", 100),
			
			(try_begin),
				(lt, ":num_alive", ":num_men_threshold"),
				
				(call_script, "script_scene_get_spawn_range", ":cur_team"),
				(assign, ":spawn_begin", reg0),
				(assign, ":spawn_end", reg1),
				
				(store_random_in_range, ":spawn_point", ":spawn_begin", ":spawn_end"),
				(call_script, "script_test_spawn_team_members_siege", ":cur_team", ":spawn_point"),
				(call_script, "script_test_spawn_team_members_siege", ":cur_team", ":spawn_point"),
				(assign, reg0, ":spawn_point"),
				(assign, reg1, ":cur_team"),
				(display_message, "@Spawning new troops at spawn {reg0} for team {reg1}."),
				
				(store_random_in_range, ":spawn_point", ":spawn_begin", ":spawn_end"),
				(call_script, "script_test_spawn_team_members_siege", ":cur_team", ":spawn_point"),
				(assign, reg0, ":spawn_point"),
				(assign, reg1, ":cur_team"),
				(display_message, "@Spawning new troops at spawn {reg0} for team {reg1}."),
			(try_end),
		(try_end),
	])

test_battle_spawn_troops_2_teams = (
	10, 0, 0,
	[],
	[
		(try_for_range, ":cur_team", 0, 2),
			(assign, ":num_alive", 0),
			(try_for_agents, ":agent_no"),
				(agent_is_alive, ":agent_no"),
				(agent_is_human, ":agent_no"),
				(agent_get_team, ":team", ":agent_no"),
				(try_begin),
					(eq, ":team", ":cur_team"),
					(val_add, ":num_alive", 1),
				(try_end),
			(try_end),
			
			(assign, ":num_men_threshold", 50),
			
			(team_get_slot, ":faction_strength_bonus", ":cur_team", slot_team_test_strength),
			(val_add, ":faction_strength_bonus", 10),
			(val_mul, ":num_men_threshold", ":faction_strength_bonus"),
			(val_div, ":num_men_threshold", 10),
			
			(try_begin),
				(lt, ":num_alive", ":num_men_threshold"),
				
				(try_begin),
					(eq, ":cur_team", 1), # ToDo: player control
					(team_slot_ge, ":cur_team", slot_team_battle_phase, stbp_combat),
					(try_for_agents, ":agent_no"),
						(agent_get_team, ":agent_team", ":agent_no"),
						(eq, ":agent_team", ":cur_team"),
						(agent_set_slot, ":agent_no", slot_agent_charge, 1),
						(agent_set_division, ":agent_no", 4),
						(agent_set_slot, ":agent_no", slot_agent_new_division, 4),
					(try_end),
					(team_set_slot, ":cur_team", slot_team_battle_phase, stbp_deploy),
					(call_script, "script_init_team_battle_ai", ":cur_team"),
				(try_end),
				
				(team_get_slot, ":spawn_point", ":cur_team", slot_team_test_spawn_point),
				(call_script, "script_test_spawn_team_members", ":cur_team", ":spawn_point"),
				(call_script, "script_test_spawn_team_members", ":cur_team", ":spawn_point"),
			(try_end),
		(try_end),
	])

test_battle_spawn_troops = (
	10, 0, 0,
	[],
	[
		(try_for_range, ":cur_team", 0, 4),
			(assign, ":num_alive", 0),
			(try_for_agents, ":agent_no"),
				(agent_is_alive, ":agent_no"),
				(agent_is_human, ":agent_no"),
				(agent_get_team, ":team", ":agent_no"),
				(try_begin),
					(eq, ":team", ":cur_team"),
					(val_add, ":num_alive", 1),
				(try_end),
			(try_end),
			
			(assign, ":num_men_threshold", 50),
			
			(team_get_slot, ":faction_strength_bonus", ":cur_team", slot_team_test_strength),
			(val_add, ":faction_strength_bonus", 10),
			(val_mul, ":num_men_threshold", ":faction_strength_bonus"),
			(val_div, ":num_men_threshold", 10),
			
			(try_begin),
				(lt, ":num_alive", ":num_men_threshold"),
				
				(try_begin),
					(neq, ":cur_team", 0), # ToDo: player control
					(team_slot_ge, ":cur_team", slot_team_battle_phase, stbp_combat),
					(try_for_agents, ":agent_no"),
						(agent_get_team, ":agent_team", ":agent_no"),
						(eq, ":agent_team", ":cur_team"),
						(agent_set_slot, ":agent_no", slot_agent_charge, 1),
						(agent_set_division, ":agent_no", 4),
						(agent_set_slot, ":agent_no", slot_agent_new_division, 4),
					(try_end),
					(team_set_slot, ":cur_team", slot_team_battle_phase, stbp_deploy),
					(call_script, "script_init_team_battle_ai", ":cur_team"),
				(try_end),
				
				(team_get_slot, ":spawn_point", ":cur_team", slot_team_test_spawn_point),
				(call_script, "script_test_spawn_team_members", ":cur_team", ":spawn_point"),
				(call_script, "script_test_spawn_team_members", ":cur_team", ":spawn_point"),
			(try_end),
		(try_end),
	])

battle_reinforcements = (
	10, 0, 0,
	[],
	[
		(try_for_range, ":cur_team", 0, 2),
			(store_add, ":allied_team", ":cur_team", 2),
			(store_normalized_team_count, ":num_troops", ":cur_team"),
			(store_normalized_team_count, ":num_allied_troops", ":cur_team"),
			(val_add, ":num_troops", ":num_allied_troops"),
			(assign, ":num_men_threshold", 12),
			(try_begin),
				(lt, ":num_troops", ":num_men_threshold"),
				
				(try_begin),
					(neq, ":cur_team", 0), # ToDo: player control
					(team_slot_ge, ":cur_team", slot_team_battle_phase, stbp_combat),
					(try_for_agents, ":agent_no"),
						(agent_get_team, ":agent_team", ":agent_no"),
						(eq, ":agent_team", ":cur_team"),
						(agent_set_slot, ":agent_no", slot_agent_charge, 1),
						(agent_set_division, ":agent_no", 4),
						(agent_set_slot, ":agent_no", slot_agent_new_division, 4),
					(try_end),
					(team_set_slot, ":cur_team", slot_team_battle_phase, stbp_deploy),
					(call_script, "script_init_team_battle_ai", ":cur_team"),
				(try_end),
				(try_begin),
					(team_slot_ge, ":allied_team", slot_team_battle_phase, stbp_combat),
					(try_for_agents, ":agent_no"),
						(agent_get_team, ":agent_team", ":agent_no"),
						(eq, ":agent_team", ":allied_team"),
						(agent_set_slot, ":agent_no", slot_agent_charge, 1),
						(agent_set_division, ":agent_no", 4),
						(agent_set_slot, ":agent_no", slot_agent_new_division, 4),
					(try_end),
					(team_set_slot, ":allied_team", slot_team_battle_phase, stbp_deploy),
					(call_script, "script_init_team_battle_ai", ":allied_team"),
				(try_end),
				
				(add_reinforcements_to_entry, ":cur_team", 4),
			(try_end),
		(try_end),
	])

test_battle_init_before_battle = (
	ti_before_mission_start, 0, ti_once,
		[],
		[
			(team_set_relation, 0, 1, -1),
			(team_set_relation, 0, 2, -1),
			(team_set_relation, 0, 3, -1),
			(team_set_relation, 1, 2, -1),
			(team_set_relation, 1, 3, -1),
			(team_set_relation, 2, 3, -1),
			
			(try_for_range, ":team", 0, 4),
				(team_set_slot, ":team", slot_team_test_faction, "fac_kingdom_1"),
				(team_set_slot, ":team", slot_team_test_strength, -10),
				(store_add, ":spawn_point", ":team", 1),
				(team_set_slot, ":team", slot_team_test_spawn_point, ":spawn_point"),
				(team_set_slot, ":team", slot_team_battle_phase, stbp_deploy),
			(try_end),
			
			(assign, "$g_test_cur_team", 0),
			# (assign, "$g_test_player_troop", "trp_swadian_militia"),
		])

test_battle_init = (
	0, 0, ti_once,
		[],
		[
			(store_current_scene, ":cur_scene"),
			(modify_visitors_at_site, ":cur_scene"),
			(add_visitors_to_current_scene, 0, "trp_player", 1),
			
			(try_for_range, ":team", 0, 2),
				(team_give_order, ":team", grc_archers, mordr_stand_ground),
			(try_end),
		])
		
battle_init = (
	0, 0, ti_once,
		[],
		[
			# (store_current_scene, ":cur_scene"),
			# (modify_visitors_at_site, ":cur_scene"),
			# (add_visitors_to_current_scene, 0, "trp_player", 1),
			
			(try_for_range, ":team", 0, 2),
				(team_give_order, ":team", grc_archers, mordr_stand_ground),
			(try_end),
		])

test_battle_init_siege = (
	0, 0, ti_once,
		[],
		[
			(store_current_scene, ":cur_scene"),
			(modify_visitors_at_site, ":cur_scene"),
			(add_visitors_to_current_scene, 0, "trp_player", 1),
			
			# (try_for_range, ":team", 0, 1),
			(team_give_order, 0, grc_archers, mordr_stand_ground),
			
			(try_for_range, ":division", grc_infantry, 9),
				(team_give_order, 0, ":division", mordr_stand_closer),
				(team_give_order, 0, ":division", mordr_stand_closer),
			(try_end),
			(call_script, "script_set_team_defend_points"),
		])

test_battle_faction_select = (
	0, 0, 0,
		[],
		[
			(try_begin),
				(key_clicked, key_left),
				(team_get_slot, ":team_faction", "$g_test_cur_team", slot_team_test_faction),
				(val_add, ":team_faction", 1),
				(try_begin),
					(ge, ":team_faction", kingdoms_end),
					(assign, ":team_faction", "fac_faction_1"),
				(try_end),
				(str_store_faction_name, s10, ":team_faction"),
				(assign, reg10, "$g_test_cur_team"),
				(display_message, "@Current faction for team {reg10}: {s10}."),
				(team_set_slot, "$g_test_cur_team", slot_team_test_faction, ":team_faction"),
			(else_try),
				(key_clicked, key_right),
				(team_get_slot, ":team_faction", "$g_test_cur_team", slot_team_test_faction),
				(val_add, ":team_faction", -1),
				(try_begin),
					(lt, ":team_faction", kingdoms_begin),
					(assign, ":team_faction", "fac_small_kingdom_65"),
				(try_end),
				(str_store_faction_name, s10, ":team_faction"),
				(assign, reg10, "$g_test_cur_team"),
				(display_message, "@Current faction for team {reg10}: {s10}."),
				(team_set_slot, "$g_test_cur_team", slot_team_test_faction, ":team_faction"),
			(else_try),
				(key_clicked, key_down),
				(team_get_slot, ":team_strength", "$g_test_cur_team", slot_team_test_strength),
				(val_add, ":team_strength", -1),
				(val_max, ":team_strength", -10),
				(assign, reg10, "$g_test_cur_team"),
				(assign, reg11, ":team_strength"),
				(display_message, "@Current faction strength for team {reg10}: {reg11}."),
				(team_set_slot, "$g_test_cur_team", slot_team_test_strength, ":team_strength"),
			(else_try),
				(key_clicked, key_up),
				(team_get_slot, ":team_strength", "$g_test_cur_team", slot_team_test_strength),
				(val_add, ":team_strength", 1),
				(val_min, ":team_strength", 20),
				(assign, reg10, "$g_test_cur_team"),
				(assign, reg11, ":team_strength"),
				(display_message, "@Current faction strength for team {reg10}: {reg11}."),
				(team_set_slot, "$g_test_cur_team", slot_team_test_strength, ":team_strength"),
			(else_try),
				(key_clicked, key_page_up),
				(val_add, "$g_test_cur_team", 1),
				(try_begin),
					(gt, "$g_test_cur_team", 3),
					(assign, "$g_test_cur_team", 0),
				(try_end),
				(assign, reg10, "$g_test_cur_team"),
				(display_message, "@Current team {reg10}."),
			(else_try),
				(key_clicked, key_p),
				(val_add, "$g_test_player_troop", 1),
				(team_get_slot, ":faction", "$g_test_player_team", slot_team_test_faction),
				(faction_get_slot, ":culture", ":faction", slot_faction_culture),
				(faction_get_slot, ":troop_begin", ":culture", slot_faction_troops_begin),
				(faction_get_slot, ":troop_end", ":culture", slot_faction_troops_end),
				(val_max, "$g_test_player_troop", ":troop_begin"),
				(try_begin),
					(ge, "$g_test_player_troop", ":troop_end"),
					(assign, "$g_test_player_troop", ":troop_begin"),
				(try_end),
				(str_store_troop_name, s10, "$g_test_player_troop"),
				(display_message, "@Current troop: {s10}."),
			(else_try),
				(key_clicked, key_o),
				(try_begin),
					(team_slot_eq, "$g_test_player_team", slot_team_formation, stf_siege),
					(team_set_slot, "$g_test_player_team", slot_team_formation, stf_siege_no_throw),
					(call_script, "script_team_set_division_slots_for_formation", 0, stf_siege_no_throw),
					(display_message, "@Changed formation from siege to siege_no_throw."),
				(else_try),
					(team_slot_eq, "$g_test_player_team", slot_team_formation, stf_siege_no_throw),
					(team_set_slot, "$g_test_player_team", slot_team_formation, stf_siege),
					(call_script, "script_team_set_division_slots_for_formation", 0, stf_siege),
					(display_message, "@Changed formation from siege_no_throw to siege."),
				(else_try),
					# (neg|team_slot_ge, 0, slot_team_formation, stf_siege),
					(team_get_slot, ":formation", "$g_test_player_team", slot_team_formation),
					(val_add, ":formation", 1),
					(try_begin),
						(eq, ":formation", stf_siege),
						(assign, ":formation", stf_default),
					(try_end),
					(team_set_slot, "$g_test_player_team", slot_team_formation, ":formation"),
					(call_script, "script_team_set_division_slots_for_formation", "$g_test_player_team", ":formation"),
					(assign, reg10, ":formation"),
					(assign, reg11, "$g_test_player_team"),
					(display_message, "@Changed formation for team {reg11}, now {reg10}."),
				(try_end),
			(else_try),
				(key_clicked, key_u),
				(val_add, "$g_test_player_team", 1),
				(try_begin),
					(gt, "$g_test_player_team", 3),
					(assign, "$g_test_player_team", 0),
				(try_end),
				(assign, reg10, "$g_test_player_team"),
				(display_message, "@Player team is now team {reg10}."),
			(try_end),
		])

test_battle_spawn = (
	ti_on_agent_spawn, 0, 0,
		[],
		[
			(store_trigger_param, ":agent_no", 1),
			# (get_player_agent_no, ":player_agent"),
			(try_begin),
				# (neq, ":agent_no", ":player_agent"),
				(call_script, "script_agent_reassign_division", ":agent_no"),
				
				(agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 0),
				(agent_set_slot, ":agent_no", slot_agent_target_entry_point, 0),
				(agent_set_slot, ":agent_no", slot_agent_is_in_scripted_mode, 0),
			(try_end),
		])

battle_spawn = (
	ti_on_agent_spawn, 0, 0,
		[],
		[
			(store_trigger_param, ":agent_no", 1),
			# (get_player_agent_no, ":player_agent"),
			(try_begin),
				# (neq, ":agent_no", ":player_agent"),
				(call_script, "script_agent_reassign_division", ":agent_no"),
				
				(agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 0),
				(agent_set_slot, ":agent_no", slot_agent_target_entry_point, 0),
				(agent_set_slot, ":agent_no", slot_agent_is_in_scripted_mode, 0),
			(try_end),
		])

test_battle_siege_spawn = (
	ti_on_agent_spawn, 0, 0,
		[],
		[
			(store_trigger_param, ":agent_no", 1),
			# (get_player_agent_no, ":player_agent"),
			(try_begin),
				# (neq, ":agent_no", ":player_agent"),
				(agent_get_team, ":team_no", ":agent_no"),
				
				(call_script, "script_agent_reassign_division", ":agent_no"),
				(assign, ":division", reg0),
				
				(try_begin),
					(eq, ":team_no", 0),
					(neq, ":division", grc_archers),
					# ToDo: needs refining: reinforce weak defend points
					(call_script, "script_scene_get_defend_points_range"),
					(assign, ":begin", reg0),
					(assign, ":end", reg1),
					(store_random_in_range, ":rand", ":begin", ":end"),
					(store_sub, ":division", ":rand", ":begin"),
					(val_add, ":division", 2),
					(agent_set_slot, ":agent_no", slot_agent_new_division, ":division"),
					(agent_set_division, ":agent_no", ":division"),
				(else_try),
					(eq, ":team_no", 1),
					(agent_ai_set_always_attack_in_melee, ":agent_no", 1),
				(try_end),
				
				(agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 0),
				(agent_set_slot, ":agent_no", slot_agent_target_entry_point, 0),
				(agent_set_slot, ":agent_no", slot_agent_is_in_scripted_mode, 0),
			(try_end),
		])

test_battle_division_control = (
	5, 0, 0,
		[],
		[
			(try_for_agents, ":agent_no"),
				(agent_is_alive, ":agent_no"),
				(call_script, "script_agent_reassign_division", ":agent_no"),
			(try_end),
		])

battle_division_control = (
	5, 0, 0,
		[],
		[
			(try_for_agents, ":agent_no"),
				(agent_is_alive, ":agent_no"),
				(call_script, "script_agent_reassign_division", ":agent_no"),
			(try_end),
		])

test_battle_division_control_siege = (
	5, 0, 0,
		[],
		[
			(try_for_agents, ":agent_no"),
				(agent_is_alive, ":agent_no"),
				(call_script, "script_agent_reassign_division_siege", ":agent_no"),
			(try_end),
		])

test_battle_fix_division = (
	0.5, 0, 0,
		[],
		[
			(try_for_agents, ":agent"),
				(agent_is_alive, ":agent"),
				(agent_slot_ge, ":agent", slot_agent_new_division, 0),
				(agent_get_division, ":division", ":agent"),
				(neg|agent_slot_eq, ":agent", slot_agent_new_division, ":division"),
				(agent_get_slot, ":new_div", ":agent", slot_agent_new_division),
				(agent_set_division, ":agent", ":new_div"),
			(try_end),
		])

battle_fix_division = (
	0.5, 0, 0,
		[],
		[
			(try_for_agents, ":agent"),
				(agent_is_alive, ":agent"),
				(agent_slot_ge, ":agent", slot_agent_new_division, 0),
				(agent_get_division, ":division", ":agent"),
				(neg|agent_slot_eq, ":agent", slot_agent_new_division, ":division"),
				(agent_get_slot, ":new_div", ":agent", slot_agent_new_division),
				(agent_set_division, ":agent", ":new_div"),
			(try_end),
		])

test_battle_siege_move_archer_to_archer_position = (
	6, 0, 0,
		[
			(try_for_range, ":team", 0, 4),
				(try_for_range, ":slot", slot_team_division_1_number, slot_team_division_9_number + 1),
					(team_set_slot, ":team", ":slot", 0),
				(try_end),
			(try_end),
		],
		[
			(try_for_agents, ":agent_no"),
				(agent_is_alive, ":agent_no"),
				(agent_get_team, ":team", ":agent_no"),
				##
				(eq, ":team", 0),
				# (this_or_next|eq, ":team", 0),
				# (eq, ":team", 1),
				##
				(agent_get_division, ":division", ":agent_no"),
				(assign, ":end", 9),
				(try_for_range, ":cur_div", grc_infantry, ":end"),
					(eq, ":division", ":cur_div"),
					(store_add, ":slot", slot_team_division_1_number, ":cur_div"),
					(team_get_slot, ":num_troop", ":team", ":slot"),
					(val_add, ":num_troop", 1),
					(team_set_slot, ":team", ":slot", ":num_troop"),
					(assign, ":end", 0),
				(try_end),
				
				(try_begin),
					(eq, ":division", grc_archers),
					(agent_slot_eq, ":agent_no", slot_agent_is_not_reinforcement, 0),
					
					(agent_get_slot, ":entry_point", ":agent_no", slot_agent_target_entry_point),
					(try_begin),
						(call_script, "script_scene_get_archer_points_range"),
						(assign, ":archer_point_begin", reg0),
						(assign, ":archer_point_end", reg1),
						
						(lt, ":entry_point", ":archer_point_begin"),
						
						(store_random_in_range, ":entry_point", ":archer_point_begin", ":archer_point_end"),
						(agent_set_slot, ":agent_no", slot_agent_target_entry_point, ":entry_point"),
					(try_end),
					
					(try_begin),
						(agent_slot_eq, ":agent_no", slot_agent_is_in_scripted_mode, 1),
						(agent_get_position, pos0, ":agent_no"),
						(entry_point_get_position, pos1, ":entry_point"),
						(get_distance_between_positions, ":dist", pos0, pos1),
						(try_begin),
							(lt, ":dist", 150),
							(agent_clear_scripted_mode, ":agent_no"),
							(agent_set_slot, ":agent_no", slot_agent_is_in_scripted_mode, 0),
							(agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 1),
						(else_try),
							(agent_set_scripted_destination, ":agent_no", pos1, 0),
						(try_end),
					(else_try),
						(agent_slot_eq, ":agent_no", slot_agent_is_in_scripted_mode, 0),
						(agent_get_slot, ":entry_point", ":agent_no", slot_agent_target_entry_point),
						(entry_point_get_position, pos1, ":entry_point"),
						(agent_set_scripted_destination, ":agent_no", pos1, 0),
						(agent_set_slot, ":agent_no", slot_agent_is_in_scripted_mode, 1),
					(else_try),
						(agent_get_simple_behavior, ":agent_sb", ":agent_no"),
						(neq, ":agent_sb", aisb_go_to_pos),#scripted mode
						(agent_slot_eq, ":agent_no", slot_agent_is_in_scripted_mode, 1),
						(agent_clear_scripted_mode, ":agent_no"),
						(agent_set_slot, ":agent_no", slot_agent_is_in_scripted_mode, 0),
					(try_end),
				(else_try),
					(agent_slot_eq, ":agent_no", slot_agent_is_in_scripted_mode, 1),
					(agent_clear_scripted_mode, ":agent_no"),
					(agent_set_slot, ":agent_no", slot_agent_is_in_scripted_mode, 0),
				(try_end),
			(try_end),
		])
	
test_battle_siege_refill_ammo = (
	60, 0, 0,
		[],
		[
			(try_for_agents, ":agent_no"),
				(agent_is_alive, ":agent_no"),
				(agent_get_team, ":team", ":agent_no"),
				(try_begin),
					(eq, ":team", 0),
					# (this_or_next|eq, ":team", 0),
					# (eq, ":team", 1),
					# only change positions of defending bots
					(try_begin),
						(agent_slot_eq, ":agent_no", slot_agent_is_in_scripted_mode, 0), # is not moving to another place
						
						(agent_get_division, ":division", ":agent_no"),
						(eq, ":division", grc_archers),
						(agent_get_ammo, ":old_ammo", ":agent_no", 0),
						(ge, ":old_ammo", 0),
					
						(agent_refill_ammo, ":agent_no"),
						(agent_get_ammo, ":new_ammo", ":agent_no", 1),
						(store_sub, ":diff", ":new_ammo", ":old_ammo"),
						(try_begin),
							(le, ":diff", 1),
							
							(agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 0),
							(agent_set_slot, ":agent_no", slot_agent_target_entry_point, 0),
						(try_end),
					(else_try),
						(agent_refill_ammo, ":agent_no"),
					(try_end),
				# (else_try),
					# (agent_refill_ammo, ":agent_no"),
				(try_end),
			(try_end),
		])

test_battle_player_respawn = (
	5, 0, 0,
		[
			(get_player_agent_no, ":player_agent"),
			(neg|agent_is_alive, ":player_agent"),
		],
		[
			(call_script, "script_troop_use_template_troop", "trp_player", "$g_test_player_troop"),
			
			(store_current_scene, ":scene"),
			(modify_visitors_at_site, ":scene"),
			(team_get_slot, ":spawn_point", "$g_test_player_team", slot_team_test_spawn_point),
			(try_begin),
				(lt, ":spawn_point", 0),
				(call_script, "script_scene_get_spawn_range", "$g_test_player_team"),
				(assign, ":spawn_point", reg0),
			(try_end),
			(add_visitors_to_current_scene, ":spawn_point", "trp_player", 1),
		])

test_battle_spawn_bodyguards = (
	5, 0, 0,
		[],
		[
			(get_player_agent_no, ":player_agent"),
			(agent_is_alive, ":player_agent"),
			
			(assign, ":slot", -1),
			(try_begin),
				(neg|agent_slot_ge, ":player_agent", slot_agent_bodyguard_1, 1),
				(assign, ":slot", slot_agent_bodyguard_troop_1),
			(else_try),
				(neg|agent_slot_ge, ":player_agent", slot_agent_bodyguard_2, 1),
				(assign, ":slot", slot_agent_bodyguard_troop_2),
			(try_end),
			
			(gt, ":slot", 0),
			(store_random_in_range, ":troop", companions_begin, companions_end),
			(store_current_scene, ":scene"),
			(modify_visitors_at_site, ":scene"),
			(team_get_slot, ":spawn_point", "$g_test_player_team", slot_team_test_spawn_point),
			(try_begin),
				(lt, ":spawn_point", 0),
				(call_script, "script_scene_get_spawn_range", "$g_test_player_team"),
				(assign, ":spawn_point", reg0),
			(try_end),
			(add_visitors_to_current_scene, ":spawn_point", ":troop", 1),
			(agent_set_slot, ":player_agent", ":slot", ":troop"),
		])

test_battle_manage_bodyguards = (
	2, 0, 0,
		[],
		[
			(get_player_agent_no, ":player_agent"),
			(agent_get_slot, ":bodyguard_1", ":player_agent", slot_agent_bodyguard_1),
			(try_begin),
				(ge, ":bodyguard_1", 0),
				(this_or_next|neg|agent_is_alive, ":bodyguard_1"),
				(eq, ":bodyguard_1", 0),
				(agent_set_slot, ":player_agent", slot_agent_bodyguard_1, -1),
			(try_end),
			(agent_get_slot, ":bodyguard_2", ":player_agent", slot_agent_bodyguard_2),
			(try_begin),
				(ge, ":bodyguard_2", 0),
				(this_or_next|neg|agent_is_alive, ":bodyguard_2"),
				(eq, ":bodyguard_2", 0),
				(agent_set_slot, ":player_agent", slot_agent_bodyguard_2, -1),
			(try_end),
			
			(try_begin),
				(agent_slot_eq, ":player_agent", slot_agent_bodyguard_1, -1),
				(agent_get_slot, ":bodyguard_troop", ":player_agent", slot_agent_bodyguard_troop_1),
				(gt, ":bodyguard_troop", 0),
				(assign, ":end", 0),
				(try_for_agents, ":agent_no"),
					(neq, ":end", 1),
					(agent_is_alive, ":agent_no"),
					(agent_get_troop_id, ":agent_troop", ":agent_no"),
					(eq, ":agent_troop", ":bodyguard_troop"),
					(agent_set_slot, ":player_agent", slot_agent_bodyguard_1, ":agent_no"),
					(agent_set_slot, ":agent_no", slot_agent_guarding, ":player_agent"),
					(assign, ":end", 1),
				(try_end),
			(try_end),
			(try_begin),
				(agent_slot_eq, ":player_agent", slot_agent_bodyguard_2, -1),
				(agent_get_slot, ":bodyguard_troop", ":player_agent", slot_agent_bodyguard_troop_2),
				(gt, ":bodyguard_troop", 0),
				(assign, ":end", 0),
				(try_for_agents, ":agent_no"),
					(neq, ":end", 1),
					(agent_is_alive, ":agent_no"),
					(agent_get_troop_id, ":agent_troop", ":agent_no"),
					(eq, ":agent_troop", ":bodyguard_troop"),
					(agent_set_slot, ":player_agent", slot_agent_bodyguard_2, ":agent_no"),
					(agent_set_slot, ":agent_no", slot_agent_guarding, ":player_agent"),
					(assign, ":end", 1),
				(try_end),
			(try_end),
		])

battle_assign_team = (
	ti_on_agent_spawn, 0, 0,
		[],
		[
			(store_trigger_param, ":agent_no", 1),
			
			(try_begin),
				(agent_is_human, ":agent_no"),
				(agent_is_ally, ":agent_no"),
				(agent_get_party_id, ":party_no", ":agent_no"),
				(neq, ":party_no", "p_main_party"),
				(agent_set_team, ":agent_no", 2),
			(try_end),
		])
	
	
#################
## Definitions ##
#################
pilgrim_disguise = []





#######################
## Mission Templates ##
#######################
mission_templates = [

    ###############
    ## Hardcoded ##
	###############
	("town_default", 0, -1,
		"Town Default",
		[
			(0, mtef_scene_source|mtef_team_0, af_override_horse, 0, 1, pilgrim_disguise),
		],     
		[]),

	("conversation_encounter", 0, -1, "Conversation Encounter",
		[
			(0, mtef_visitor_source, af_override_fullhelm, 0, 1,[]), (1, mtef_visitor_source, af_override_fullhelm, 0, 1, []),
			(2, mtef_visitor_source, af_override_fullhelm, 0, 1,[]), (3, mtef_visitor_source, af_override_fullhelm, 0, 1, []),( 4,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 5,mtef_visitor_source,af_override_fullhelm,0,1,[]),( 6,mtef_visitor_source,af_override_fullhelm,0,1,[]),
			(7, mtef_visitor_source, af_override_fullhelm, 0, 1,[]), (8, mtef_visitor_source, af_override_fullhelm, 0, 1, []),( 9,mtef_visitor_source,af_override_fullhelm,0,1,[]),(10,mtef_visitor_source,af_override_fullhelm,0,1,[]),(11,mtef_visitor_source,af_override_fullhelm,0,1,[]),
			#prisoners now...
			(12,mtef_visitor_source,af_override_fullhelm,0,1,[]),(13,mtef_visitor_source,af_override_fullhelm,0,1,[]),(14,mtef_visitor_source,af_override_fullhelm,0,1,[]),(15,mtef_visitor_source,af_override_fullhelm,0,1,[]),(16,mtef_visitor_source,af_override_fullhelm,0,1,[]),
			#Other party
			(17,mtef_visitor_source,af_override_fullhelm,0,1,[]),(18,mtef_visitor_source,af_override_fullhelm,0,1,[]),(19,mtef_visitor_source,af_override_fullhelm,0,1,[]),(20,mtef_visitor_source,af_override_fullhelm,0,1,[]),(21,mtef_visitor_source,af_override_fullhelm,0,1,[]),
			(22,mtef_visitor_source,af_override_fullhelm,0,1,[]),(23,mtef_visitor_source,af_override_fullhelm,0,1,[]),(24,mtef_visitor_source,af_override_fullhelm,0,1,[]),(25,mtef_visitor_source,af_override_fullhelm,0,1,[]),(26,mtef_visitor_source,af_override_fullhelm,0,1,[]),
			(27,mtef_visitor_source,af_override_fullhelm,0,1,[]),(28,mtef_visitor_source,af_override_fullhelm,0,1,[]),(29,mtef_visitor_source,af_override_fullhelm,0,1,[]),(30,mtef_visitor_source,af_override_fullhelm,0,1,[]),(31,mtef_visitor_source,af_override_fullhelm,0,1,[]),
		],[]),
  
    ###########
	## Other ##
	###########

	("lead_charge", mtf_battle_mode, charge,
		"Lead Charge",
		[
			(1, mtef_defenders|mtef_team_0, 0, aif_start_alarmed, 12, []),
			(0, mtef_defenders|mtef_team_0, 0, aif_start_alarmed, 0,  []),
			(4, mtef_attackers|mtef_team_1, 0, aif_start_alarmed, 12, []),
			(4, mtef_attackers|mtef_team_1, 0, aif_start_alarmed, 0,  []),
		],
		[
		]),
	
	("battle_test_siege", mtf_battle_mode, charge,
		"Lead charge",
		[
			(0, mtef_visitor_source|mtef_team_0, af_override_horse, aif_start_alarmed, 0, []),
			(1, mtef_visitor_source|mtef_team_0, af_override_horse, aif_start_alarmed, 0, []),
			(2, mtef_visitor_source|mtef_team_1, af_override_horse, aif_start_alarmed, 0, []),
			(3, mtef_visitor_source|mtef_team_1, af_override_horse, aif_start_alarmed, 0, []),
			# (4, mtef_visitor_source|mtef_team_3, 0, aif_start_alarmed, 0, []),
		],
		[
			# test_battle_init_before_battle,
			test_battle_init_siege,
			test_battle_siege_spawn_troops,
			test_battle_faction_select,
			test_battle_siege_spawn,
			test_battle_division_control_siege,
			test_battle_fix_division,
			test_battle_siege_move_archer_to_archer_position,
			test_battle_siege_refill_ammo,
			
			test_battle_player_respawn,
			
			# test_battle_spawn_bodyguards,
			# test_battle_manage_bodyguards,
			
			battle_siege_equalize_division,
			
			(ti_before_mission_start, 0, ti_once,
				[],
				[
					(team_set_relation, 0, 1, -1),
					(team_set_relation, 0, 2, -1),
					(team_set_relation, 0, 3, -1),
					(team_set_relation, 1, 2, -1),
					(team_set_relation, 1, 3, -1),
					(team_set_relation, 2, 3, -1),
					
					(try_for_range, ":team", 0, 4),
						(team_set_slot, ":team", slot_team_test_faction, "fac_kingdom_1"),
						(team_set_slot, ":team", slot_team_test_strength, -10),
						(team_set_slot, 0, slot_team_battle_phase, stbp_siege_one),
					(try_end),
					
					(team_set_slot, 0, slot_team_test_spawn_point, 1),
					(team_set_slot, 1, slot_team_test_spawn_point, 2),
					
					(assign, "$g_test_cur_team", 0),
					(assign, "$g_test_player_team", 0),
					# (assign, "$g_test_player_troop", "trp_swadian_militia"),
					
					# (call_script, "script_troop_use_template_troop", "trp_player", "$g_test_player_troop"),
				]),
			
			(ti_tab_pressed, 0, 0, [],
				[
					(finish_mission, 0),
				]),
			
			(ti_after_mission_start, 0, ti_once,
				[],
				[
					(team_set_slot, 0, slot_team_formation, stf_siege),
					(call_script, "script_team_set_division_slots_for_formation", 0, stf_siege),
						
					(team_set_slot, 1, slot_team_formation, stf_default),
					(call_script, "script_team_set_division_slots_for_formation", 1, stf_default),
				]),
		]),
	
	("battle_test_plain", mtf_battle_mode, charge,
		"Lead charge",
		[
			(0, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 0, []),
			(1, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 0, []),
			(2, mtef_visitor_source|mtef_team_1, 0, aif_start_alarmed, 0, []),
			(3, mtef_visitor_source|mtef_team_2, 0, aif_start_alarmed, 0, []),
			(4, mtef_visitor_source|mtef_team_3, 0, aif_start_alarmed, 0, []),
		],
		[
			test_battle_init,
			test_battle_spawn_troops,
			test_battle_fix_division,
			test_battle_division_control,
			
			test_battle_spawn,
			test_battle_faction_select,
			
			test_battle_player_respawn,
			
			# test_battle_spawn_bodyguards,
			# test_battle_manage_bodyguards,
			
			(ti_before_mission_start, 0, ti_once,
				[],
				[
					(team_set_relation, 0, 1, -1),
					(team_set_relation, 0, 2, 1),
					(team_set_relation, 0, 3, -1),
					(team_set_relation, 1, 2, -1),
					(team_set_relation, 1, 3, 1),
					(team_set_relation, 2, 3, -1),
					
					(try_for_range, ":team", 0, 4),
						(team_set_slot, ":team", slot_team_test_faction, "fac_kingdom_1"),
						(team_set_slot, ":team", slot_team_test_strength, -10),
						(store_add, ":spawn", ":team", 1),
						(team_set_slot, ":team", slot_team_test_spawn_point, ":spawn"),
					(try_end),
					
					(assign, "$g_test_cur_team", 0),
					# (assign, "$g_test_player_troop", "trp_swadian_militia"),
					
					# (call_script, "script_troop_use_template_troop", "trp_player", "$g_test_player_troop"),
				]),
			
			(5, 0, 0,
				[],
				[
					(call_script, "script_process_battle_ais"),
				]),
			
			(ti_after_mission_start, 0, ti_once,
				[],
				[
					(call_script, "script_init_battle_ais"),
				]),
			
			(ti_tab_pressed, 0, 0, [],
			[
				(finish_mission, 0),
			]),
			
		]),
	
	("battle_field", mtf_battle_mode, charge,
		"Lead charge",
		[
			# (0, mtef_visitor_source|mtef_team_0, 0, aif_start_alarmed, 0, []),
			(1, mtef_attackers|mtef_team_0, 0, aif_start_alarmed, 0, []),
			(2, mtef_defenders|mtef_team_1, 0, aif_start_alarmed, 0, []),
			(1, mtef_visitor_source|mtef_team_2, 0, aif_start_alarmed, 0, []),
			(2, mtef_visitor_source|mtef_team_3, 0, aif_start_alarmed, 0, []),
		],
		[
			battle_init,
			battle_reinforcements,
			battle_fix_division,
			battle_division_control,
			
			battle_spawn,
			
			battle_assign_team,
			
			# test_battle_spawn_bodyguards,
			# test_battle_manage_bodyguards,
			
			(ti_before_mission_start, 0, ti_once,
				[],
				[
					(team_set_relation, 0, 1, -1),
					(team_set_relation, 0, 2, 1),
					(team_set_relation, 0, 3, -1),
					(team_set_relation, 1, 2, -1),
					(team_set_relation, 1, 3, 1),
					(team_set_relation, 2, 3, -1),
					
					(team_set_slot, 0, slot_team_test_spawn_point, 1),
					(team_set_slot, 1, slot_team_test_spawn_point, 2),
				]),
			
			(5, 0, 0,
				[],
				[
					(call_script, "script_process_battle_ais"),
				]),
			
			(ti_after_mission_start, 0, ti_once,
				[],
				[
					(call_script, "script_init_battle_ais"),
				]),
			
			(ti_tab_pressed, 0, 0, [],
			[
				(store_normalized_team_count, ":team_0", 0),
				(store_normalized_team_count, ":team_1", 1),
				(try_begin),
					(neq, ":team_0", 0),
					(neq, ":team_1", 0),
					(display_message, "@There are still enemies in the battle!"),
				(else_try),
					(party_clear, "p_player_casualties"),
					(party_clear, "p_ally_casualties"),
					(party_clear, "p_enemy_casualties"),
					
					(try_for_agents, ":cur_agent"),
						(neg|agent_is_alive, ":cur_agent"),
						(agent_is_human, ":cur_agent"),
						(agent_get_party_id, ":agent_party", ":cur_agent"),
						(agent_get_troop_id, ":agent_troop_id", ":cur_agent"),
						(try_begin),
							(eq, ":agent_party", "p_main_party"),
							(party_add_members, "p_player_casualties", ":agent_troop_id", 1),
							(try_begin),
								(agent_is_wounded, ":cur_agent"),
								(party_wound_members, "p_player_casualties", ":agent_troop_id", 1),
							(try_end),
						(else_try),
							(agent_is_ally, ":cur_agent"),
							(party_add_members, "p_ally_casualties", ":agent_troop_id", 1),
							(try_begin),
								(agent_is_wounded, ":cur_agent"),
								(party_wound_members, "p_ally_casualties", ":agent_troop_id", 1),
							(try_end),
						(else_try),
							(party_add_members, "p_enemy_casualties", ":agent_troop_id", 1),
							(try_begin),
								(agent_is_wounded, ":cur_agent"),
								(party_wound_members, "p_enemy_casualties", ":agent_troop_id", 1),
							(try_end),
						(try_end),
					(try_end),
					(try_begin),
						(eq, ":team_1", 0),
						(display_message, "@You are victorious!"),
						(finish_mission, 0),
					(else_try),
						(eq, ":team_0", 0),
						(display_message, "@You have been defeated!"),
						(finish_mission, 0),
					(try_end),
				(try_end),
			]),
			
			
			
		]),
]
