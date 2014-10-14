from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *
from module_constants import *





simple_triggers = [

	# Parties trigger
    (24,
	[
		(try_for_parties, ":party_no"),
			(party_get_slot, ":party_type", ":party_no", slot_party_type),
			(try_begin),
				(is_between, ":party_type", spt_village, spt_fort),
				(call_script, "script_party_process_production", ":party_no"),
				(call_script, "script_party_process_population", ":party_no"),
				(call_script, "script_party_process_taxes", ":party_no"),
				
				(try_begin),
					(party_get_slot, ":population", ":party_no", slot_party_population),
					(gt, ":population", 20),
					(assign, ":num_recruited", 0),
					
					(try_begin),
						(eq, ":party_type", spt_village),
						
						(call_script, "script_party_send_reinforcements", ":party_no"),
						(call_script, "script_party_recruit_troops", ":party_no"),
						(assign, ":num_recruited", reg0),
					(else_try),
						# (is_between, ":party_type", spt_castle, spt_fort),
						
						(call_script, "script_party_recruit_troops", ":party_no"),
						(assign, ":num_recruited", reg0),
					(try_end),
					(val_mul, ":num_recruited", -1),
					(call_script, "script_party_modify_population", ":party_no", ":num_recruited"),
				(try_end),
			(else_try),
				(eq, ":party_type", spt_war_party),
				# (get_party_ai_object, ":object", ":party_no"),
				(party_get_cur_town, ":cur_town", ":party_no"),
				(try_begin),
					(ge, ":cur_town", centers_begin),
					(call_script, "script_party_does_center_buisness", ":party_no", ":cur_town"),
				(try_end),
			(try_end),
			# (try_begin),
				# (this_or_next|eq, ":party_type", spt_village),
				# (eq, ":party_type", spt_town),
			# (try_end),
		(try_end),
		(store_random_in_range, "$g_daily_random", 0, 10000),
		(assign, reg0, "$g_daily_random"),
		(display_message, "@Random daily number: {reg0}"),
	]),
	
	# (12,
	# [
		
	# ]),
	
	(6,
	[
		(try_for_parties, ":party_no"),
			(party_get_slot, ":party_type", ":party_no", slot_party_type),
			(try_begin),
				(is_between, ":party_type", spt_village, spt_fort),
				# (store_random_in_range, ":random", 0, 10),
				# (try_begin),
					# (eq, ":random", 0),
					# (call_script, "script_cf_party_send_surplus_population", ":party_no"),
				# (try_end),
				(try_begin),
					(party_get_slot, ":besieger", ":party_no", slot_party_besieged_by),
					(ge, ":besieger", 0),
					(try_begin),
						(neg|party_is_active, ":besieger"),
						(party_set_slot, ":party_no", slot_party_besieged_by, -1),
					(else_try),
						# (store_distance_to_party_from_party, ":dist", ":party_no", ":besieger"),
						# (gt, ":dist", 15),
						(party_get_slot, ":leader", ":besieger", slot_party_leader),
						(troop_get_slot, ":current_behavior", ":leader", slot_troop_behavior),
						(troop_get_slot, ":current_object", ":leader", slot_troop_behavior_object),
						
						(this_or_next|neq, ":current_behavior", tai_attacking_center),
						(neq, ":current_object", ":party_no"),
						(party_set_slot, ":party_no", slot_party_besieged_by, -1),
					(try_end),
				(try_end),
			(else_try),
				(eq, ":party_type", spt_war_party),
				(call_script, "script_party_process_mission", ":party_no"),
			(try_end),
		(try_end),
	]),
	
	(2,
	[
		(try_for_parties, ":party_no"),
			(party_get_slot, ":party_type", ":party_no", slot_party_type),
			(try_begin),
				(eq, ":party_type", spt_convoy),
				(party_slot_eq, ":party_no", slot_party_mission, spm_reinforce),
				
				(try_begin),
					(get_party_ai_object, ":object", ":party_no"),
					(party_get_cur_town, ":cur_town", ":party_no"),
					(eq, ":object", ":cur_town"),
					(call_script, "script_party_transfer_members_to_party", ":party_no", ":cur_town", 1),
					(remove_party, ":party_no"),
				(try_end),
			(else_try),
				# (is_between, ":party_type", spt_village, spt_fort),
			# (else_try),
				(eq, ":party_type", spt_scout),
				# (party_slot_eq, ":party_no", slot_party_mission, spm_colonise),
				# (party_set_slot, ":party_no", slot_party_ressource_radius, 3),
				# (call_script, "script_party_update_nearby_resources", ":party_no"),
				# (store_faction_of_party, ":faction", ":party_no"),
				# (try_begin),
					# (call_script, "script_cf_faction_need_party_nearby_resources", ":faction", ":party_no"),
					# (call_script, "script_spawn_new_center_marker_with_party_resources", ":party_no"),
				# (try_end),
			(else_try),
				(eq, ":party_type", spt_war_party),
				(call_script, "script_party_process_ai", ":party_no"),
			(try_end),
		(try_end),
	]),
	
	(0.1,
	[
		(try_for_parties, ":party_no"),
			(neq, ":party_no", "p_main_party"),
			# (party_get_slot, ":party_type", ":party_no", slot_party_type),
			(party_get_attached_to, ":cur_attached_town", ":party_no"),
			(lt, ":cur_attached_town", 1),
			(party_get_cur_town, ":cur_town", ":party_no"),
			(is_between, ":cur_town", centers_begin, centers_end),
			(party_attach_to_party, ":party_no", ":cur_town"),
		(try_end),
	]),
	
	# Lords trigger
	(24,
	[
		(try_for_range, ":lord_no", lords_begin, lords_end),
			(troop_get_slot, ":occupation", ":lord_no", slot_troop_kingdom_occupation),
			# ToDo
			(try_begin),
				(eq, ":occupation", tko_kingdom_hero),
				(troop_get_slot, ":leaded_party", ":lord_no", slot_troop_leaded_party),
				(try_begin),
					(gt, ":leaded_party", 0),
					# 
				(else_try),
					(call_script, "script_cf_lord_can_spawn", ":lord_no"),
					(call_script, "script_spawn_lord", ":lord_no"),
				# (else_try),
				(try_end),
				
				(troop_get_slot, ":lord_level", ":lord_no", slot_troop_level),
				# (call_script, "script_troop_get_rank", ":lord_no"),
				# (assign, ":real_rank", reg0),
				(troop_get_slot, ":real_rank", ":lord_no", slot_troop_rank),
				(try_begin),
					(neq, ":lord_level", ":real_rank"),
					(call_script, "script_troop_update_level", ":lord_no", ":lord_level", ":real_rank"),
				(try_end),
				
				(try_begin),
					(ge, ":real_rank", rank_castle),
					(troop_get_slot, ":surplus_fief", ":lord_no", slot_troop_surplus_center),
					(gt, ":surplus_fief", 0),
					(party_get_slot, ":party_type", ":surplus_fief", slot_party_type),
					(store_troop_faction, ":faction", ":lord_no"),
					(assign, ":selected", -1),
					(assign, ":end", lords_end),
					(try_for_range, ":other_lord", lords_begin, ":end"),
						(store_troop_faction, ":other_faction", ":other_lord"),
						(eq, ":other_faction", ":faction"),
						(try_begin),
							(troop_slot_eq, ":other_lord", slot_troop_vassal_of, ":lord_no"),
							(troop_get_slot, ":rank", ":other_lord", slot_troop_rank),
							(try_begin),
								(lt, ":rank", rank_castle),
								(this_or_next|gt, ":party_type", spt_village),
								(lt, ":rank", rank_village),
								(assign, ":selected", ":other_lord"),
							(else_try),
								(lt, ":rank", rank_village),
								(assign, ":selected", ":other_lord"),
								(assign, ":end", 0),
							(try_end),
						(else_try),
							(troop_slot_eq, ":other_lord", slot_troop_vassal_of, -1),
							(troop_get_slot, ":rank", ":other_lord", slot_troop_rank),
							(lt, ":rank", rank_castle),
							(this_or_next|gt, ":party_type", spt_village),
							(neq, ":rank", rank_two_village),
							(eq, ":selected", -1),
							(assign, ":selected", ":other_lord"),
						(try_end),
					(try_end),
					(ge, ":selected", 0),
					(call_script, "script_troop_give_center_to_troop", ":lord_no", ":surplus_fief", ":selected"),
				(try_end),
				
				# Decrease days until next rethink for following marshall
				(troop_get_slot, ":days_left", ":lord_no", slot_troop_days_next_rethink),
				(val_sub, ":days_left", 1),
				(val_max, ":days_left", 0),
				(troop_set_slot, ":lord_no", slot_troop_days_next_rethink, ":days_left"),
			# (else_try),
				
			(try_end),
		(try_end),
	]),
	
	# (12,
	# [
	
	# ]),
	
	(6,
	[
		# (try_for_range, ":lord_no", lords_begin, lords_end),
			# (troop_get_slot, ":occupation", ":lord_no", slot_troop_kingdom_occupation),
			# (store_troop_faction, ":faction", ":lord_no"),
			# (try_begin),
				# (this_or_next|eq, ":occupation", tko_),
				# (eq, ":occupation", tko_kingdom_hero),
				# (call_script, "script_troop_process_ai", ":lord_no"),
			# (else_try),
			# (try_end),
		# (try_end),
	]),
	
	(24*7,
	[
		(try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
			(faction_get_slot, ":center_no", ":faction_no", slot_faction_current_free_center),
			(ge, ":center_no", centers_begin),
			
			(call_script, "script_faction_get_best_candidate_for_center", ":faction_no", ":center_no"),
			(assign, ":troop_no", reg0),
			
			(gt, ":troop_no", -1),
			(call_script, "script_give_center_to_troop", ":center_no", ":troop_no"),
			
			(faction_set_slot, ":faction_no", slot_faction_current_free_center, -1),
		(try_end),
		
		(try_for_range_backwards, ":cur_center", centers_begin, centers_end),
			(party_get_slot, ":lord", ":cur_center", slot_party_lord),
			(lt, ":lord", 0),
			(store_faction_of_party, ":center_faction", ":cur_center"),
			(faction_set_slot, ":center_faction", slot_faction_current_free_center, ":cur_center"),
		(try_end),
	]),
]
