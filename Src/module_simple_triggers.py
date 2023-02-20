from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *
from module_constants import *

daily = 1           # 1
weekly = daily*7    # 7
monthly = daily*30  # 30
yearly = daily*365  # 

simple_triggers = [

    (monthly*2, # Parties trigger
        [
            (try_for_range, ":party_no", centers_begin, centers_end),
                (call_script, "script_party_recruit_troops", ":party_no"),
                (assign, ":num_recruited", reg0),
                (val_mul, ":num_recruited", -1),
                (call_script, "script_party_modify_population", ":party_no", ":num_recruited"),
                (party_get_slot, ":party_type", ":party_no", slot_party_type),
                
                (try_begin),
                    (eq, ":party_type", spt_town),
                    (call_script, "script_party_update_merchants_gold", ":party_no"),
                (try_end),

                # Generate bandits
                (store_random_in_range, ":rand", 0, 50),
                (try_begin), # Generate bandits more often if center prosperity is low
                    (le, ":rand", 3),
                    (call_script, "script_party_spawn_bandits", ":party_no"),
                (try_end),
            (try_end),
        ]),
    
    (monthly, # Parties trigger
        [
            (try_for_range, ":lord", lords_begin, lords_end),
                (troop_set_slot, ":lord", slot_troop_accumulated_taxes, 0),
                (troop_set_slot, ":lord", slot_troop_budget_vassal_taxes, 0),
                (troop_set_slot, ":lord", slot_troop_budget_faction_member_taxes, 0),
                (troop_set_slot, ":lord", slot_troop_budget_reserved_party, 0),
                (troop_set_slot, ":lord", slot_troop_budget_reserved_other, 0),
            (try_end),
            (try_for_range, ":center", centers_begin, centers_end),
                (party_set_slot, ":center", slot_party_accumulated_taxes, 0),
                (party_set_slot, ":center", slot_party_budget_reserved_party, 0),
                (party_set_slot, ":center", slot_party_budget_reserved_auxiliaries, 0),
                (party_set_slot, ":center", slot_party_budget_reserved_expenses, 0),
                (party_set_slot, ":center", slot_party_budget_reserved_other, 0),
                (party_set_slot, ":center", slot_party_budget_taxes, 0),
                (party_set_slot, ":center", slot_party_budget_protection_taxes, 0),
                (party_set_slot, ":center", slot_party_budget_vassal_taxes, 0),
                (party_set_slot, ":center", slot_party_budget_faction_member_taxes, 0),
                (party_set_slot, ":center", slot_party_budget_pay_protection_taxes, 0),
                (party_set_slot, ":center", slot_party_budget_pay_vassal_taxes, 0),
                (party_set_slot, ":center", slot_party_budget_pay_faction_member_taxes, 0),
                (party_set_slot, ":center", slot_party_budget_trade, 0),
            (try_end),

            (try_for_parties, ":party_no"),
                (party_is_active, ":party_no"),
                (party_get_slot, ":party_type", ":party_no", slot_party_type),
                (try_begin),
                    (is_between, ":party_type", spt_village, spt_fort), # Need to move this part in a trigger for centers
                    (call_script, "script_party_process_ressources", ":party_no"), # Made in the same way as faction political calculations

                    (call_script, "script_party_process_production", ":party_no"),
                    (call_script, "script_party_process_consumption", ":party_no"),
                    (call_script, "script_party_process_population", ":party_no"),
                    (call_script, "script_party_process_taxes", ":party_no"),
                    (call_script, "script_party_process_buildings", ":party_no", monthly),
                    (call_script, "script_party_process_attached_parties", ":party_no"),
                (else_try),
                    (eq, ":party_type", spt_war_party),
                    # (get_party_ai_object, ":object", ":party_no"),
                    (party_get_cur_town, ":cur_town", ":party_no"),
                    (try_begin),
                        (ge, ":cur_town", centers_begin),
                        (call_script, "script_party_does_center_business", ":party_no", ":cur_town"),
                    (try_end),
                (else_try),
                    (eq, ":party_type", spt_patrol),
                    (call_script, "script_party_patrol_process", ":party_no"),
                (else_try),
                    (eq, ":party_type", spt_caravan),
                    (call_script, "script_party_caravan_process", ":party_no"),
                (try_end),
            (try_end),

            (try_for_range, ":lord", lords_begin, lords_end),
                (troop_get_slot, ":occupation", ":lord", slot_troop_kingdom_occupation),
                (eq, ":occupation", tko_kingdom_hero),

                (troop_get_slot, ":real_debt", ":lord", slot_troop_budget_debt),
                (troop_get_slot, ":perceived_debt", ":lord", slot_troop_budget_perceived_debt),
                (val_mul, ":perceived_debt", 9),
                (val_add, ":perceived_debt", ":real_debt"),
                (val_div, ":perceived_debt", 10),
                (troop_set_slot, ":lord", slot_troop_budget_perceived_debt, ":perceived_debt"),

                (call_script, "script_troop_process_ideal_party_wages", ":lord"),
            (try_end),
            (try_for_range, ":center", centers_begin, centers_end),
                (call_script, "script_party_process_ideal_party_wages", ":center"),
            (try_end),

            (store_random_in_range, "$g_daily_random", 0, 10000),
        ]),
    
    (daily*6, # Sieges
        [
            (try_for_parties, ":party_no"),
                (party_is_active, ":party_no"),
                (party_get_slot, ":party_type", ":party_no", slot_party_type),
                (try_begin),
                    (is_between, ":party_type", spt_village, spt_fort),
                    (try_begin),
                        (party_get_slot, ":besieger", ":party_no", slot_party_besieged_by),
                        (ge, ":besieger", 0),
                        (try_begin),
                            (neg|party_is_active, ":besieger"),
                            (call_script, "script_party_lift_siege", ":party_no"),
                            # (party_set_slot, ":party_no", slot_party_besieged_by, -1),
                        (else_try),
                            (store_distance_to_party_from_party, ":dist", ":party_no", ":besieger"),
                            (gt, ":dist", 6),
                            # (party_get_slot, ":leader", ":besieger", slot_party_leader),
                            # (troop_get_slot, ":current_behavior", ":leader", slot_troop_behavior),
                            # (troop_get_slot, ":current_object", ":leader", slot_troop_behavior_object),
                            
                            # (this_or_next|neq, ":current_behavior", tai_attacking_center),
                            # (neq, ":current_object", ":party_no"),
                            (call_script, "script_party_lift_siege", ":party_no"),
                            # (party_set_slot, ":party_no", slot_party_besieged_by, -1),
                        (try_end),
                    (try_end),
                # (else_try),
                    # (eq, ":party_type", spt_war_party),
                (try_end),
            (try_end),
        ]),
    
    (daily*2, # Reinforcements transfering
        [
            (try_for_parties, ":party_no"),
                (party_is_active, ":party_no"),
                (party_get_slot, ":party_type", ":party_no", slot_party_type),

                (store_faction_of_party, ":party_faction", ":party_no"),

                (try_begin),
                    (eq, ":party_type", spt_convoy),
                    (party_slot_eq, ":party_no", slot_party_mission, spm_reinforce),
                    
                    (try_begin),
                        (get_party_ai_object, ":object", ":party_no"),

                        (try_begin),
                            (is_between, ":object", centers_begin, centers_end),
                            (store_faction_of_party, ":center_faction", ":object"),
                            (neq, ":center_faction", ":party_faction"),
                            (store_relation, ":rel", ":center_faction", ":party_faction"),
                            (lt, ":rel", relation_neutral),

                            (party_get_slot, ":origin_party", ":party_no", slot_party_origin_center),
                            (neq, ":object", ":origin_party"),
                            (party_set_slot, ":party_no", slot_party_mission_object, ":origin_party"),
                            
                            (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
                            (party_set_ai_object, ":party_no", ":origin_party"),
                        (else_try),
                            (party_get_cur_town, ":cur_town", ":party_no"),
                            (eq, ":object", ":cur_town"),
                            (call_script, "script_party_transfer_members_to_party", ":party_no", ":cur_town", 1),
                            (remove_party, ":party_no"),
                        (try_end),
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
                (try_end),
            (try_end),
        ]),
    
    # (0.5,
        # [
            # (store_current_hours, ":day"),
            # (store_div, ":long_years", 1461), # 1461 = 365.25*4 (4 whole years)
            # (val_sub, ":day_of_year", ":long_year"), # Remove excess days from years with 366 days
            # (store_mod, ":day_of_year", ":day", 365),
            # (store_add, ":offset_day_of_year", ":day_of_year", 40),
            # (val_mod, ":offset_day_of_year", 365), # We use an offset to move the end of the year winter to a value of 0
            # (store_mul, ":season", ":offset_day_of_year", 4),
            # (val_div, ":season", 365),
            
            # (assign, ":cloud_base", 50),
            # (assign, ":cloud_variant", 50),
            # (assign, ":cloud_spike", 20),
            
            # (try_begin),
                # (eq, ":season", 0),
                # (assign, ":cloud_base", 40),
                # (assign, ":cloud_variant", 25),
                # (assign, ":cloud_spike", 4),
            # (else_try),
                # (eq, ":season", 1),
                # (assign, ":cloud_base", 30),
                # (assign, ":cloud_variant", 50),
                # (assign, ":cloud_spike", 2),
            # (else_try),
                # (eq, ":season", 2),
                # (assign, ":cloud_base", 20),
                # (assign, ":cloud_variant", 10),
                # (assign, ":cloud_spike", 20),
            # (else_try),
                # (eq, ":season", 3),
                # (assign, ":cloud_base", 60),
                # (assign, ":cloud_variant", 40),
                # (assign, ":cloud_spike", 6),
            # (try_end),
            
            # (party_get_current_terrain, ":terrain", "$g_player_party"),
            # (try_begin),
                # (this_or_next|eq, ":terrain", rt_snow),
                # (eq, ":terrain", rt_snow_forest),
                # (val_add, ":cloud_base", 5),
                # (val_add, ":cloud_variant", 10),
                # (val_add, ":cloud_spike", -5),
            # (else_try),
                # (this_or_next|eq, ":terrain", rt_steppe),
                # (eq, ":terrain", rt_steppe_forest),
                # (val_add, ":cloud_base", -5),
                # (val_add, ":cloud_variant", -10),
                # (val_add, ":cloud_spike", 5),
            # (else_try),
                # (this_or_next|eq, ":terrain", rt_desert),
                # (eq, ":terrain", rt_desert_forest),
                # (val_add, ":cloud_base", -50),
                # (val_add, ":cloud_variant", -50),
                # (val_add, ":cloud_spike", -20),
            # (else_try),
                
            # (try_end),
            
            # (val_clamp, ":cloud_base", 0, 100),
            # (val_clamp, ":cloud_variant", 0, 100),
            # (val_clamp, ":cloud_spike", 2, 100),
            
            # (try_begin),
                # (this_or_next|eq, ":terrain", rt_forest),
                # (this_or_next|eq, ":terrain", rt_snow_forest),
                # (this_or_next|eq, ":terrain", rt_steppe_forest),
                # (eq, ":terrain", rt_desert_forest),
                # (val_mul, ":cloud_spike", 3),
                # (val_div, ":cloud_spike", 2),
                # (val_add, ":cloud_variant", 10),
            # (try_end),
            
            # (store_mul, ":cloud", "$g_global_cloud_amount", ":cloud_base"),
            # (store_random_in_range, ":variant", 0, ":cloud_variant"),
            # (val_add, ":cloud", ":variant"),
            
        # ]),
    
    (0.1, # Weather
        [
            (try_for_parties, ":party_no"),
                (neq, ":party_no", "$g_player_party"),
                (party_is_active, ":party_no"),
                # (party_get_slot, ":party_type", ":party_no", slot_party_type),
                (party_get_attached_to, ":cur_attached_town", ":party_no"),
                (lt, ":cur_attached_town", 1),
                (party_get_cur_town, ":cur_town", ":party_no"),
                (is_between, ":cur_town", centers_begin, centers_end),
                (party_get_num_companions, ":num_troops", ":party_no"),
                (gt, ":num_troops", 0),
                (call_script, "script_party_enter_center", ":party_no", ":cur_town"),
            (try_end),

            (get_global_haze_amount, ":haze"),
            (get_global_cloud_amount, ":cloud"),
            (val_mul, ":haze", 9),
            (val_mul, ":cloud", 9),
            (val_add, ":haze", "$g_global_haze_amount"),
            (val_div, ":haze", 10),
            (val_add, ":cloud", "$g_global_cloud_amount"),
            (val_div, ":cloud", 10),
            (set_global_haze_amount, ":haze"),
            (set_global_cloud_amount, ":cloud"),
        ]),

    (0.1, # Player prisoner
        [
            (troop_get_slot, ":player_prisoner", "$g_player_troop", slot_troop_prisoner_of),
            (try_begin),
                (gt, ":player_prisoner", 0),
                (try_begin),
                    (key_is_down, key_space),
                    (jump_to_menu, "mnu_player_prisoner_take_action"),
                (try_end),
                (set_camera_follow_party, ":player_prisoner"),
            (else_try),
                # ToDo: free player
            (try_end),
        ]),
    
    (weekly, # Lord mission
        [
            (call_script, "script_prepare_troop_followers"),
            (try_for_range, ":lord_no", lords_begin, lords_end),
                (troop_get_slot, ":occupation", ":lord_no", slot_troop_kingdom_occupation),
                (neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of, 0), # Do not process prisoners
                (try_begin),
                    (eq, ":occupation", tko_kingdom_hero),
                    (troop_get_slot, ":leaded_party", ":lord_no", slot_troop_leaded_party),
                    (gt, ":leaded_party", 0),
                    (party_is_active, ":leaded_party"),
                    (call_script, "script_party_process_mission", ":leaded_party", 0),
                (try_end),
            (try_end),
        ]),
    
    (weekly*2,
        [
            (try_for_range, ":lord_no", lords_begin, lords_end),
                (troop_get_slot, ":occupation", ":lord_no", slot_troop_kingdom_occupation),
                (troop_get_slot, ":prisoner_of", ":lord_no", slot_troop_prisoner_of),
                (try_begin),
                    (le, ":prisoner_of", 0), # Do not process prisoners
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
                        (troop_get_slot, ":equipement_rank", ":lord_no", slot_troop_equipement_level),
                        (call_script, "script_troop_get_equipement_level", ":lord_no"),
                        (assign, ":best_equipement_rank", reg0),
                        (try_begin),
                            (this_or_next|neq, ":lord_level", ":real_rank"),
                            (neq, ":equipement_rank", ":best_equipement_rank"),
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
                            (try_begin),
                                (ge, ":selected", 0),
                                (call_script, "script_troop_give_center_to_troop", ":lord_no", ":surplus_fief", ":selected"),
                            (else_try), # Promote a relative with a fief
                                (call_script, "script_find_free_lord"),
                                (assign, ":new_lord", reg0),
                                (gt, ":new_lord", 0),
                                (call_script, "script_ready_lord", ":new_lord", ":faction"),
                                (call_script, "script_troop_give_center_to_troop", ":lord_no", ":surplus_fief", ":new_lord"),
                            (try_end),
                        (try_end),
                        
                        # Decrease days until next rethink for following marshall
                        (troop_get_slot, ":days_left", ":lord_no", slot_troop_days_next_rethink),
                        (val_sub, ":days_left", 1),
                        (val_max, ":days_left", 0),
                        (troop_set_slot, ":lord_no", slot_troop_days_next_rethink, ":days_left"),
                    # (else_try),
                        
                    (try_end),
                (else_try),
                    # Try to free lord
                    # Very low chance if at war (escape)
                    # Highly likely if good relations (npc or faction)
                    # Increased chance if long time since prisoner
                    (call_script, "script_troop_prisoner", ":lord_no"),
                (try_end),
            (try_end),
        ]),

    (yearly, # Yearly wages for parties
        [
            (try_for_parties, ":party_no"),
                (neq, ":party_no", "$g_player_party"),
                # Every party must pay wages
                (call_script, "script_party_pay_wages", ":party_no"),
                (call_script, "script_party_pay_debts", ":party_no"),
            (try_end),

            # For player we call the budget menu
            (assign, "$g_process_effects", 1),
            (start_presentation, "prsnt_budget_report"),
        ]),
    
    (yearly, # Weapon proficiency decay
        [
            (try_begin),
                # Might do it for all heroes
                # But will need to have them increase their proficiency after every battle
                # Or do it only to player companions at a reduced rate
                (call_script, "script_troop_proficiency_decay", "$g_player_troop"),
            (try_end),
        ]),
    
    (daily*2, # AI processing
        [
            (try_for_range, ":lord_no", lords_begin, lords_end),
                (troop_get_slot, ":occupation", ":lord_no", slot_troop_kingdom_occupation),
                (try_begin),
                    # (this_or_next|eq, ":occupation", tko_),
                    (eq, ":occupation", tko_kingdom_hero),
                    (troop_get_slot, ":leaded_party", ":lord_no", slot_troop_leaded_party),
                    (gt, ":leaded_party", 0),
                    (party_is_active, ":leaded_party"),
                    (call_script, "script_party_process_ai", ":leaded_party"),
                (try_end),
            (try_end),
        ]),
    
    (monthly*6/(kingdoms_end - kingdoms_begin), # Faction politics processing
        [
            (try_begin),
                (neg|is_between, "$g_politics_cur_faction", kingdoms_begin, kingdoms_end),
                (assign, "$g_politics_cur_faction", kingdoms_begin),
            (try_end),
            (try_begin),
                (call_script, "script_cf_debug", debug_faction|debug_simple),
                (str_store_faction_name, s10, "$g_politics_cur_faction"),
                (display_message, "@Current faction politics: {s10}"),
            (try_end),
            
            (call_script, "script_faction_process_politics", "$g_politics_cur_faction"),
            
            (val_add, "$g_politics_cur_faction", 1),
        ]),
    
    (monthly*2, # Free center processing
        [
            (try_for_range_backwards, ":cur_center", centers_begin, centers_end),
                (party_get_slot, ":lord", ":cur_center", slot_party_lord),
                (lt, ":lord", 0),
                (store_faction_of_party, ":center_faction", ":cur_center"),
                (faction_set_slot, ":center_faction", slot_faction_current_free_center, ":cur_center"),
            (try_end),
        ]),
]
