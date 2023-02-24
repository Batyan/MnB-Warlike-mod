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
from ID_meshes import *


scripts = [ 
    
    ###############
    ## Hardcoded ##
    ###############

    # script_game_start:
    # This script is called when a new game is started
    # INPUT: none
    ("game_start",
        [
            (set_player_troop, "trp_player"), # Must be set to allow the creation screen to pass
            (assign, "$g_player_troop", "trp_player"),
            (assign, "$g_player_party", "p_main_party"),
            (party_set_slot, "$g_player_party", slot_party_type, spt_war_party),

            # (party_set_slot, "$g_player_party", slot_party_type, spt_war_party),
            
            (assign, "$g_cur_free_lord", lords_begin),

            (set_show_messages, 0),
            (call_script, "script_init_centers"),
            (call_script, "script_init_factions"),
            (call_script, "script_init_cultures"),
            (call_script, "script_init_bandits"),
            
            ## Generate some bandits to begin with
            (try_for_range, ":cur_center", villages_begin, villages_end),
                (store_random_in_range, ":rand", 0, 10),
                (try_begin),
                    (eq, ":rand", 0),
                    (call_script, "script_party_spawn_bandits", ":cur_center"),
                (try_end),
            (try_end),
            
            (call_script, "script_init_building_slots"),
            (call_script, "script_init_siege_scene_slots"),
            
            (call_script, "script_init_troops_types"),
            (call_script, "script_init_troops_factions"),
            (call_script, "script_init_troops_archer_score"),
            (call_script, "script_init_troops_mercenary"),
            
            (call_script, "script_init_arms_colors"),
            
            # ToDo: temporary
            (try_for_range, ":faction", "fac_faction_1", kingdoms_end),
                (faction_set_slot, ":faction", slot_faction_era, 0),
            (try_end),
            
            (try_for_range, ":small_kingdom", kingdoms_begin, small_kingdoms_end),
                (faction_set_slot, ":small_kingdom", slot_faction_leader, -1),
                (faction_set_slot, ":small_kingdom", slot_faction_marshall, -1),
            (try_end),

            (try_for_range, ":good", goods_begin, goods_end),
                (item_set_slot, ":good", slot_item_consumption_base, 20),
                (item_set_slot, ":good", slot_item_consumption_ratio, 3),
            (try_end),

            (try_for_range, ":party_no", centers_begin, centers_end),
                (call_script, "script_party_init_center", ":party_no"),
            (try_end),

            (try_for_range, ":lord_no", lords_begin, lords_end),
                (call_script, "script_init_lord", ":lord_no"),
            (try_end),
            
            (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
                (store_faction_of_party, ":center_faction", ":center_no"),
                (is_between, ":center_faction", kingdoms_begin, kingdoms_end),

                (call_script, "script_find_free_lord"),
                (assign, ":lord_no", reg0),
                (gt, ":lord_no", 0),
                
                (party_set_slot, ":center_no", slot_party_lord, ":lord_no"),
                
                (call_script, "script_ready_lord", ":lord_no", ":center_faction"),
                
                (call_script, "script_troop_get_rank", ":lord_no"),
                (assign, ":rank", reg0),
                (troop_set_slot, ":lord_no", slot_troop_rank, ":rank"),

                (call_script, "script_give_center_to_troop", ":center_no", ":lord_no"),
                
                (call_script, "script_troop_change_level", ":lord_no", ":rank"),
            (try_end),
            
            (try_for_range, ":party_no", centers_begin, centers_end),
                (party_get_slot, ":party_type", ":party_no", slot_party_type),
                (try_begin),
                    (eq, ":party_type", spt_town),
                    (try_for_range, ":unused", 0, 30),
                        (call_script, "script_party_add_reinforcements", ":party_no"),
                    (try_end),
                (else_try),
                    (eq, ":party_type", spt_castle),
                    (try_for_range, ":unused", 0, 20),
                        (call_script, "script_party_add_reinforcements", ":party_no"),
                    (try_end),
                (else_try),
                    (eq, ":party_type", spt_village),
                    (call_script, "script_party_add_reinforcements", ":party_no"),
                    (call_script, "script_party_add_reinforcements", ":party_no"),
                (try_end),
            (try_end),

            (try_for_range, ":merchant", merchants_begin, merchants_end),
                (troop_set_slot, ":merchant", slot_troop_last_met, -24*7*5), # Around 5 weeks' worth of goods
            (try_end),
            
            (party_set_slot, "$g_player_party", slot_party_leader, "$g_player_troop"),
            (troop_add_gold, "$g_player_troop", 10000),
            
            (assign, "$g_global_haze_amount", 0),
            (assign, "$g_global_cloud_amount", 0),
            
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
            (try_begin),
                (lt, "$debug", debug_simple),
                (display_message, "@Activating debug mode"),
                (assign, "$debug", debug_simple),
            (else_try),
                (display_message, "@Deactivation debug mode"),
                (assign, "$debug", 0),
            (try_end),
        ]),
    
    # script_game_event_party_encounter:
    # This script is called from the game engine whenever player party encounters another party or a battle on the world map
    # INPUT:
    # param1: encountered_party
    # param2: second encountered_party (if this was a battle
    ("game_event_party_encounter",
        [
            (store_script_param_1, "$g_encountered_party"),
            (store_script_param_2, "$g_encountered_party_2"), # Negative if non-battle.
            
            (party_get_slot, ":party_type", "$g_encountered_party", slot_party_type),
            (try_begin),
                (lt, "$g_encountered_party_2", 0), # Non-battle.
                (try_begin),
                    (eq, "$g_encountered_party", "p_camp_bandits"), # Camp.
                    (jump_to_menu, "mnu_camp"),
                (else_try),
                    (this_or_next|eq, ":party_type", spt_town),
                    (this_or_next|eq, ":party_type", spt_village),
                    (eq, ":party_type", spt_castle),
                    (party_get_slot, ":besieger",  "$g_encountered_party", slot_party_besieged_by),
                    (try_begin),
                        (eq, ":besieger", "$g_player_party"),
                        (jump_to_menu, "mnu_town_siege"),
                    (else_try),
                        (jump_to_menu, "mnu_town"),
                    (try_end),
                # (else_try),
                    # (is_between, "$g_encountered_party", "p_places_stone_obelisk", "p_Bridge_1"),
                    # (jump_to_menu, "mnu_visit_place"),
                (else_try),
                    # Disallow speaking with certain lords/parties
                    (try_begin),
                        (party_get_slot, ":leader", "$g_encountered_party", slot_party_leader),
                        (gt, ":leader", 0),
                        (troop_get_slot, ":last_met", ":leader", slot_troop_last_met),
                        (is_between, ":last_met", 0, 3), 
                        # If we meet shortly after refusing speech then we do not wish to speak again
                    (else_try),
                        (party_set_slot, "$g_encountered_party", slot_party_speak_allowed, 1),
                    (try_end),
                    (jump_to_menu, "mnu_simple_encounter"),
                (try_end),
            (else_try),
                
                (this_or_next|eq, ":party_type", spt_town),
                (eq, ":party_type", spt_castle),
                (jump_to_menu, "mnu_siege_camp"),
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
                    (try_begin),
                        # We allow attacking lords to flee after the end of the fight
                        (store_random_in_range, ":rand", 0, 3),
                        (this_or_next|neg|is_between, ":party_type", spt_village, spt_fort + 1),
                        (eq, ":rand", 0),
                        (call_script, "script_party_group_defeat_party_group", ":defender_party", ":attacker_party"),
                    # (else_try),
                        # Order lords to turn around ?
                        # Keep the siege a while longer and wait for reinforcements ?
                    (try_end),
                (else_try),
                    # (inflict_casualties_to_party_group, ":defender_party", 20, "p_temp_casualties"),
                    (call_script, "script_party_groups_simulate_battle", ":attacker_party", ":defender_party"),
                (try_end),
            (try_end),
            
            (set_trigger_result, ":result"),
        ]),

    # script_cf_debug
    # input:
    #   arg1: required_level
    # output: none
    ("cf_debug", 
        [
            (store_script_param, ":required_level", 1),

            (store_and, ":continue", ":required_level", "$debug"),
            (gt, ":continue", 0),
        ]),
    
    # script_party_groups_simulate_battle
    # input:
    #   arg1: attacker
    #   arg2: defender
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
            # (try_begin),
            #     (assign, reg12, ":stage"),
            #     (str_store_party_name, s10, ":attacker"),
            #     (str_store_party_name, s11, ":defender"),
            #     (assign, reg10, ":attacker_strength"),
            #     (assign, reg11, ":defender_strength"),
            #     (display_message, "@Stage {reg12}^{s10}'s strength: {reg10}.^{s11}'s strength: {reg11}."),
            # (try_end),
            (try_begin),
                (gt, ":attacker_strength", 0),
                (party_clear, "p_temp_casualties"),
                (inflict_casualties_to_party_group, ":defender", ":attacker_strength", "p_temp_casualties"),

                (call_script, "script_party_group_get_looted_gold", "p_temp_casualties"),
                (assign, ":total_gold", reg0),
                (party_get_slot, ":current_casulaties_gold", ":defender", slot_party_recent_casualties_loot),
                (val_add, ":current_casulaties_gold", ":total_gold"),
                (party_set_slot, ":defender", slot_party_recent_casualties_loot, ":current_casulaties_gold"),
            (try_end),

            (party_collect_attachments_to_party, ":defender", "p_collective_defender"),
            
            (call_script, "script_party_count_fit_for_battle", "p_collective_defender", 0),
            (assign, ":num_defenders", reg0),

            (try_begin),
                (gt, ":defender_strength", 0),
                (gt, ":num_defenders", 0),
                (party_clear, "p_temp_casualties"),
                (inflict_casualties_to_party_group, ":attacker", ":defender_strength", "p_temp_casualties"),

                (call_script, "script_party_group_get_looted_gold", "p_temp_casualties"),
                (assign, ":total_gold", reg0),
                (party_get_slot, ":current_casulaties_gold", ":attacker", slot_party_recent_casualties_loot),
                (val_add, ":current_casulaties_gold", ":total_gold"),
                (party_set_slot, ":attacker", slot_party_recent_casualties_loot, ":current_casulaties_gold"),
            (try_end),
        ]),
    
    # script_party_groups_simulate_battle_approach
    # input:
    #   arg1: attacker
    #   arg2: defender
    # output:
    #   reg0: attacker_strength
    #   reg1: defender_strength
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

            (val_max, ":attacker_defense", 1),
            (val_max, ":defender_defense", 1),
            
            (store_mul, ":attacker_reduce", ":attacker_strength", 100),
            (val_div, ":attacker_reduce", ":defender_defense"),
            (store_sub, ":attacker_reduce", 100, ":attacker_reduce"),
            (val_mul, ":attacker_reduce", ":attacker_strength"),
            (store_sqrt, ":attacker_reduce", ":attacker_reduce"),
            (val_sub, ":attacker_strength", ":attacker_reduce"),

            (store_mul, ":defender_reduce", ":defender_strength", 100),
            (val_div, ":defender_reduce", ":attacker_defense"),
            (store_sub, ":defender_reduce", 100, ":defender_reduce"),
            (val_mul, ":defender_reduce", ":defender_strength"),
            (store_sqrt, ":defender_reduce", ":defender_reduce"),
            (val_sub, ":defender_strength", ":defender_reduce"),

            # Defenders have a small bonus during the approach phase
            (val_mul, ":defender_strength", 150),
            (val_div, ":defender_strength", 100),
            
            (assign, reg0, ":attacker_strength"),
            (assign, reg1, ":defender_strength"),
        ]),
    
    # script_party_groups_simulate_battle_charge
    # input:
    #   arg1: attacker
    #   arg2: defender
    # output:
    #   reg0: attacker_strength
    #   reg1: defender_strength
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
    #   arg1: attacker
    #   arg2: defender
    # output:
    #   reg0: attacker_strength
    #   reg1: defender_strength
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
    #   arg1: party_group
    # output:
    #   reg0: strength
    #   reg1: defense
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
    #   arg1: party_group
    # output:
    #   reg0: strength
    #   reg1: defense
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
    #   arg1: party_group
    # output:
    #   reg0: strength
    #   reg1: defense
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
    #   arg1: troop
    # output:
    #   reg0: strength
    #   reg1: defense
    #   reg2: ranged_strength
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
                (store_mul, ":ranged_strength", ":weapon_weight", 5),
                (val_add, ":ranged_strength", 5),
                
                # (assign, ":mult", 100),
                # (try_begin),
                    # (this_or_next|eq, ":type", tt_archer),
                    # (eq, ":type", tt_horse_archer),
                    # (store_skill_level, ":pd", skl_power_draw, ":troop_no"),
                    # (val_mul, ":pd", 14),
                    # (val_add, ":mult", ":pd"),
                # (else_try),
                    # (store_skill_level, ":pt", skl_power_throw, ":troop_no"),
                    # (val_mul, ":pt", 10),
                    # (val_add, ":mult", ":pt"),
                # (try_end),
                # (val_mul, ":ranged_strength", ":mult"),
                # (val_div, ":ranged_strength", 100),
                
                (store_skill_level, ":pd", skl_power_draw, ":troop_no"),
                (store_skill_level, ":pt", skl_power_throw, ":troop_no"),
                
                (store_proficiency_level, ":p", ":troop_no", wpt_archery),
                (store_proficiency_level, ":c", ":troop_no", wpt_crossbow),
                (store_proficiency_level, ":t", ":troop_no", wpt_throwing),
                
                (try_begin),
                    (val_div, ":p", 2),
                    (val_mul, ":pd", 14),
                    (val_add, ":p", ":pd"),
                    
                    (val_div, ":t", 2),
                    (val_mul, ":pt", 10),
                    (val_add, ":t", ":pt"),
                    
                    (val_max, ":p", ":c"),
                    (val_max, ":p", ":t"),
                (try_end),
                (val_add, ":ranged_strength", ":p"),
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
    #   arg1: winner_party
    #   arg2: defeated_party
    # output: none
    ("party_group_defeat_party_group",
        [
            (store_script_param, ":winner_party", 1),
            (store_script_param, ":defeated_party", 2),
            
            (party_get_slot, ":party_type", ":defeated_party", slot_party_type),
            
            (call_script, "script_party_group_defeated", ":defeated_party"),
            (call_script, "script_party_group_loot_party_group", ":winner_party", ":defeated_party"),
            (call_script, "script_party_group_take_party_group_prisoner", ":winner_party", ":defeated_party"),

            (try_begin),
                (neq, ":defeated_party", "$g_player_party"),
                (call_script, "script_clear_party_group", ":defeated_party"),
            (try_end),
            # /!\ Defeated_party should be considered no longer referenced! (unless it is a center) /!\
            
            (party_set_slot, ":winner_party", slot_party_battle_stage, bs_approach),
            
            (try_begin),
                (is_between, ":party_type", spt_village, spt_fort + 1),
                
                (call_script, "script_party_defeat_center", ":winner_party", ":defeated_party"),
                
                # (party_get_slot, ":leader", ":winner_party", slot_party_leader),
                # (troop_set_slot, ":leader", slot_troop_mission, -1),
                (call_script, "script_party_process_mission", ":winner_party", 1),
                (call_script, "script_party_process_ai", ":winner_party"),
                
                (party_get_num_attached_parties, ":num_attached_parties", ":winner_party"),
                (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
                    (party_get_attached_party_with_rank, ":attached_party", ":winner_party", ":attached_party_rank"),
                    (gt, ":attached_party", 0),
                    (call_script, "script_party_process_mission", ":attached_party", 1),
                    (call_script, "script_party_process_ai", ":attached_party"),
                (try_end),
            (try_end),
        ]),

    # script_party_group_loot_party_group
        # input:
        #   arg1: party_group_looting
        #   arg2: party_group_looted
        # output: none
    ("party_group_loot_party_group",
        [
            (store_script_param, ":party_group_no", 1),
            (store_script_param, ":looted_party_group", 2),

            (call_script, "script_party_group_get_looted_gold", ":looted_party_group"),
            (assign, ":total_gold", reg0),

            (call_script, "script_party_group_share_gold", ":party_group_no", ":total_gold"),
        ]),

    # script_party_group_get_looted_gold
        # input:
        #   arg1: party_group_no
        # output:
        #   reg0: total_looted_gold
    ("party_group_get_looted_gold",
        [
            (store_script_param, ":party_group_no", 1),

            (call_script, "script_party_get_looted_gold", ":party_group_no"),
            (assign, ":total_gold", reg0),

            (party_get_slot, ":party_wealth", ":party_group_no", slot_party_wealth),
            (val_add, ":total_gold", ":party_wealth"),
            (party_set_slot, ":party_group_no", slot_party_wealth, 0),

            (party_get_slot, ":casulaties_gold", ":party_group_no", slot_party_recent_casualties_loot),
            (val_add, ":total_gold", ":casulaties_gold"),
            (party_set_slot, ":party_group_no", slot_party_recent_casualties_loot, 0),

            (party_get_num_attached_parties, ":num_attached_parties", ":party_group_no"),
            (try_for_range, ":cur_party_index", 0, ":num_attached_parties"),
                (party_get_attached_party_with_rank, ":cur_party", ":party_group_no", ":cur_party_index"),
                (call_script, "script_party_group_get_looted_gold", ":cur_party"),
                (val_add, ":total_gold", reg0),
            (try_end),

            (assign, reg0, ":total_gold"),
        ]),
    
    # script_party_group_defeated
        # input:
        #   arg1: defeated_party
        # output: none
    ("party_group_defeated",
        [
            (store_script_param, ":defeated_party", 1),
            
            (party_get_slot, ":party_type", ":defeated_party", slot_party_type),
            (try_begin),
                (eq, ":party_type", spt_war_party),
                (party_get_slot, ":leader", ":defeated_party", slot_party_leader),
                (troop_set_slot, ":leader", slot_troop_leaded_party, -1),
                
                ###
                (str_store_troop_name_link, s10, ":leader"),
                (display_log_message, "@{s10} has been defeated in battle.", text_color_capture),
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
        #   arg1: party_group_no
        #   arg2: prisoner_party
        # output: none
    ("party_group_take_party_group_prisoner",
        [
            (store_script_param, ":party_group_no", 1),
            (store_script_param, ":prisoner_party", 2),

            (party_clear, "p_prisoners_party"),
            (party_clear, "p_temp_party"),
            
            (party_get_num_prisoner_stacks, ":num_stacks", ":prisoner_party"),
            (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
                (party_prisoner_stack_get_troop_id, ":troop_id", ":prisoner_party", ":cur_stack"),
                # We do not care if its a hero or not, it will be processed elsewhere
                (party_prisoner_stack_get_size, ":stack_size", ":prisoner_party", ":cur_stack"),
                (party_add_members, "p_temp_party", ":troop_id", ":stack_size"),
                (party_remove_prisoners, ":prisoner_party", ":troop_id", ":stack_size"),
            (try_end),

            (party_get_num_companion_stacks, ":num_stacks", ":prisoner_party"),
            (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":troop_id", ":prisoner_party", ":cur_stack"),
                (party_stack_get_size, ":stack_size", ":prisoner_party", ":cur_stack"),

                (neq, ":troop_id", "$g_player_troop"),

                (party_add_members, "p_prisoners_party", ":troop_id", ":stack_size"),
                (party_remove_members, ":prisoner_party", ":troop_id", ":stack_size"),
            (try_end),

            (party_get_num_attached_parties, ":num_attached_prisoner_parties", ":prisoner_party"),
            (try_for_range, ":attached", 0, ":num_attached_prisoner_parties"),
                (party_get_attached_party_with_rank, ":attached_party", ":prisoner_party", ":attached"),
                (party_get_num_prisoner_stacks, ":num_stacks", ":attached_party"),
                (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
                    (party_prisoner_stack_get_troop_id, ":troop_id", ":attached_party", ":cur_stack"),
                    # We do not care if its a hero or not, it will be processed elsewhere
                    (party_prisoner_stack_get_size, ":stack_size", ":attached_party", ":cur_stack"),
                    (party_add_members, "p_temp_party", ":troop_id", ":stack_size"),
                    (party_remove_prisoners, ":attached_party", ":troop_id", ":stack_size"),
                (try_end),
                (party_get_num_companion_stacks, ":num_stacks", ":attached_party"),
                (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
                    (party_stack_get_troop_id, ":troop_id", ":attached_party", ":cur_stack"),
                    (party_stack_get_size, ":stack_size", ":attached_party", ":cur_stack"),
                    (party_add_members, "p_prisoners_party", ":troop_id", ":stack_size"),
                    (party_remove_members, ":attached_party", ":troop_id", ":stack_size"),
                (try_end),
            (try_end),

            (call_script, "script_party_group_take_party_prisoner", ":party_group_no", "p_prisoners_party"),
            
            (call_script, "script_party_group_free_party", ":party_group_no", "p_temp_party"),
        ]),

    # script_party_group_take_party_prisoner
        # input:
        #   arg1: party_group_no
        #   arg2: party_to_take_prisoner
        # output: none
    ("party_group_take_party_prisoner",
        [
            (store_script_param, ":party_group_no", 1),
            (store_script_param, ":prisoner_party", 2),

            (party_get_num_attached_parties, ":num_attached_parties", ":party_group_no"),

            (store_add, ":total_num_parties", ":num_attached_parties", 1),
            (party_get_num_companions, ":num_prisoners", ":prisoner_party"),
            (store_div, ":num_per_party", ":num_prisoners", ":total_num_parties"),
            (val_mod, ":num_prisoners", ":total_num_parties"),

            (try_begin),
                (gt, ":num_per_party", 0),
                # First party gets priority on troops
                (try_for_range, ":unused", 0, ":num_per_party"),
                    (party_get_num_companion_stacks, ":num_stacks", ":prisoner_party"),
                    (store_random_in_range, ":rand", 0, ":num_stacks"),
                    (party_stack_get_troop_id, ":troop_id", ":prisoner_party", ":rand"),

                    (call_script, "script_party_take_troop_prisoner", ":party_group_no", ":troop_id", ":prisoner_party", 1),
                (try_end),
                # Then we iterate over attached parties
                (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
                    (party_get_attached_party_with_rank, ":attached_party", ":party_group_no", ":attached_party_rank"),
                    (try_for_range, ":unused", 0, ":num_per_party"),

                        (party_get_num_companion_stacks, ":num_stacks", ":prisoner_party"),
                        (store_random_in_range, ":rand", 0, ":num_stacks"),
                        (party_stack_get_troop_id, ":troop_id", ":prisoner_party", ":rand"),

                        (call_script, "script_party_take_troop_prisoner", ":attached_party", ":troop_id", ":prisoner_party", 1),
                    (try_end),
                (try_end),
            (try_end),
            (try_begin),
                (gt, ":num_prisoners", 0),
                (party_get_num_companion_stacks, ":num_stacks", ":prisoner_party"),
                (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
                    (party_stack_get_size, ":stack_size", ":prisoner_party", ":cur_stack"),
                    (party_stack_get_troop_id, ":troop_id", ":prisoner_party", ":cur_stack"),
                    (call_script, "script_party_take_troop_prisoner", ":party_group_no", ":troop_id", ":prisoner_party", ":stack_size"),
                (try_end),
            (try_end),
        ]),

    # script_party_group_share_gold
        # input:
        #   arg1: party_group_no
        #   arg2: total_gold
        # output: none
    ("party_group_share_gold",
        [
            (store_script_param, ":party_group_no", 1),
            (store_script_param, ":total_gold", 2),

            (assign, ":total_gold_shared", 0),

            (party_get_num_companions, ":main_party_num_companions", ":party_group_no"),
            # We also add a flat value to make sure small parties get a little gold
            (val_add, ":main_party_num_companions", 10),
            (assign, ":total_army_size", ":main_party_num_companions"),

            (party_get_num_attached_parties, ":num_attached_parties", ":party_group_no"),
            (try_for_range, ":cur_party_index", 0, ":num_attached_parties"),
                (party_get_attached_party_with_rank, ":cur_party", ":party_group_no", ":cur_party_index"),
                (party_get_num_companions, ":num_companions", ":cur_party"),
                (val_add, ":total_army_size", ":num_companions"),
                # We also add a flat value to make sure small parties get a little gold
                (val_add, ":total_army_size", 10),
            (try_end),

            # MAIN PARTY
            (store_mul, ":share", ":main_party_num_companions", 100),
            (val_div, ":share", ":total_army_size"),
            (val_max, ":share", 1),

            (store_mul, ":gold_share", ":share", ":total_gold"),
            (val_div, ":gold_share", 100),

            (val_add, ":total_gold_shared", ":gold_share"),
            (call_script, "script_party_loot_gold", ":party_group_no", ":gold_share"),
            # /MAIN PARTY

            (try_for_range, ":cur_party_index", 0, ":num_attached_parties"),
                (party_get_attached_party_with_rank, ":cur_party", ":party_group_no", ":cur_party_index"),
                (party_get_num_companions, ":num_companions", ":cur_party"),
                (val_add, ":num_companions", 10),

                (store_mul, ":share", ":num_companions", 100),
                (val_div, ":share", ":total_army_size"),
                (val_max, ":share", 1),

                (store_mul, ":gold_share", ":share", ":total_gold"),
                (val_div, ":gold_share", 100),
                (val_add, ":total_gold_shared", ":gold_share"),
                (call_script, "script_party_loot_gold", ":cur_party", ":gold_share"),
            (try_end),

            (try_begin),
                (call_script, "script_cf_debug", debug_economy),
                (store_sub, ":surplus", ":total_gold", ":total_gold_shared"),
                (neq, ":surplus", 0),
                (assign, reg10, ":surplus"),
                (display_message, "@Fight generated {reg10} unclaimed surplus gold"),
            (try_end),
        ]),

    # script_party_loot_gold
        # input:
        #   arg1: party_no
        #   arg2: gold_amount
        # output: none
    ("party_loot_gold",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":gold_amount", 2),
            
            (call_script, "script_party_get_skill_level", ":party_no", skl_looting),
            (assign, ":looting_skill", reg0),

            (store_mul, ":looting_mult", ":looting_skill", 10),
            (val_add, ":looting_mult", 100),
            (val_mul, ":gold_amount", ":looting_mult"),
            (val_div, ":gold_amount", 100),

            (try_begin),
                (call_script, "script_cf_debug", debug_economy),
                (str_store_party_name, s10, ":party_no"),
                (assign, reg10, ":gold_amount"),
                (assign, reg11, ":looting_mult"),
                (display_message, "@{s10} receives {reg10} denars (looting, {reg11}%)"),
            (try_end),

            (call_script, "script_party_receive_gold", ":party_no", ":gold_amount"),
        ]),

    # script_party_receive_gold
        # input:
        #   arg1: party_no
        #   arg2: gold_amount
        # output: none
    ("party_receive_gold",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":gold_amount", 2),

            (party_get_slot, ":leader", ":party_no", slot_party_leader),
            (try_begin),
                (ge, ":leader", 0),
                (troop_is_hero, ":leader"),
                (troop_add_gold, ":leader", ":gold_amount"),
            (else_try),
                (party_get_slot, ":party_wealth", ":party_no", slot_party_wealth),
                (val_add, ":party_wealth", ":gold_amount"),
                (party_set_slot, ":party_no", slot_party_wealth, ":party_wealth"),
            (try_end),
        ]),

    # script_party_group_free_party
        # input:
        #   arg1: party_group_no
        #   arg2: freed_party
        # output: none
    ("party_group_free_party",
        [
            (store_script_param, ":party_group_no", 1),
            (store_script_param, ":freed_party", 2),

            (party_get_num_companion_stacks, ":num_stacks", ":freed_party"),
            (try_for_range_backwards, ":cur_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":troop_id", ":freed_party", ":cur_stack"),
                (troop_is_hero, ":troop_id"),
                (call_script, "script_troop_freed", ":troop_id", ":party_group_no"),
                (party_remove_members, ":freed_party", ":troop_id", 1),
            (try_end),

            (distribute_party_among_party_group, ":freed_party", ":party_group_no"),
        ]),

    # script_game_event_battle_end:
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
            (store_script_param, ":item", 1),
            
            (call_script, "script_item_get_buy_price_factor_from_party", ":item", "$g_player_party", "$g_encountered_party"),
            
            (assign, ":price", reg0),
            (set_trigger_result, ":price"),
        ]),
  
    #script_game_get_item_sell_price_factor:
        # This script is called from the game engine for calculating the selling price of any item.
        # INPUT:
        # param1: item_kind_id
        # OUTPUT:
        # trigger_result and reg0 = price_factor
    ("game_get_item_sell_price_factor",
        [
            (store_script_param, ":item", 1),

            (call_script, "script_item_get_sell_price_factor_from_party", ":item", "$g_player_party", "$g_encountered_party"),
            
            (assign, ":price", reg0),
            (set_trigger_result, ":price"),
        ]),
  
    #script_game_event_buy_item:
        # This script is called from the game engine when player buys an item.
        # INPUT:
        # param1: item_kind_id
    ("game_event_buy_item",
        [
            # This event is called not on the final purchase of an item but when moving the item from one inventory to the other
            # This means that the transaction is not finalized yet !
            # For now player taxes are not taken into account for center prosperity (could be abused anyways)

            # (try_begin),
            #     # Should be set before every call to trade with an npc
            #     # And unset after (unless the trader is not taxed)
            #     (ge, "$g_trading", 1),
            #     (is_between, "$g_encountered_party", centers_begin, centers_end),
            #     (store_script_param, ":item_no", 1),

            #     (store_item_value, ":value", ":item_no"),

            #     (party_get_slot, ":tax_rate", "$g_encountered_party", slot_party_taxes_buy),
            #     (gt, ":tax_rate", 0),
            #     (val_mul, ":value", ":tax_rate"),
            #     (val_div, ":value", 100),

            #     (call_script, "script_party_add_accumulated_taxes", "$g_encountered_party", ":value", tax_type_trade),
            # (try_end),
        ]),
  
    #script_game_event_sell_item:
        # This script is called from the game engine when player sells an item.
        # INPUT:
        # param1: item_kind_id
    ("game_event_sell_item",
        [
            # This event is called not on the final purchase of an item but when moving the item from one inventory to the other
            # This means that the transaction is not finalized yet !
            # For now player taxes are not taken into account for center prosperity (could be abused anyways)

            # (try_begin),
            #     # Should be set before every call to trade with an npc
            #     # And unset after (unless the trader is not taxed)
            #     (ge, "$g_trading", 1),
            #     (is_between, "$g_encountered_party", centers_begin, centers_end),
            #     (store_script_param, ":item_no", 1),

            #     (store_item_value, ":value", ":item_no"),

            #     (party_get_slot, ":tax_rate", "$g_encountered_party", slot_party_taxes_sell),
            #     (gt, ":tax_rate", 0),
            #     (val_mul, ":value", ":tax_rate"),
            #     (val_div, ":value", 100),

            #     (call_script, "script_party_add_accumulated_taxes", "$g_encountered_party", ":value", tax_type_trade),
            # (try_end),
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

            (call_script, "script_troop_get_wages_for_party", ":troop_no", ":party_no"),
            (set_trigger_result, reg0),
        ]),

    # script_game_get_total_wage
        # This script is called from the game engine for calculating total wage of the player party which is shown at the party window.
        # Input: none
        # Output: 
        #   reg0: weekly wage
    ("game_get_total_wage",
        [
            (call_script, "script_party_get_wages", "$g_player_party"),
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
            (store_script_param, ":troop_no", 1),
            (assign, ":can_sell", 0),

            (try_begin),
                (neg|troop_is_hero, ":troop_no"),
                (assign, ":can_sell", 1),
            (try_end),

            (assign, reg0, ":can_sell"),
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
            
            # (store_div, ":num_days", ":num_hours", 24),
            (assign, ":num_days", ":num_hours"),
            (store_add, ":cur_day", ":num_days", 23),
            (assign, ":cur_month", 1),
            (assign, ":cur_year", starting_year),
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
            (set_trigger_result, 9999),
        ]),

    #script_game_reset_player_party_name:
        # This script is called from the game engine when the player name is changed.
        # INPUT: none
        # OUTPUT: none
    ("game_reset_player_party_name",
        [
            # (str_store_troop_name, s10, "$g_player_troop"),
            # (troop_set_plural_name, "$g_player_troop", s10),
            
            # (call_script, "script_troop_get_rank", "$g_player_troop"),
            
            # (troop_set_slot, "$g_player_troop", slot_troop_rank, reg0),
            
            # (call_script, "script_troop_update_name", "$g_player_troop"),
        ]),

    #script_game_get_troop_note
        # This script is called from the game engine when the notes of a troop is needed.
        # INPUT: arg1 = troop_no, arg2 = note_index
        # OUTPUT: s0 = note
    ("game_get_troop_note",
        [
            (store_script_param, ":troop_no", 1),
            # (store_script_param, ":index", 2),

            (troop_get_slot, ":troop_notes", ":troop_no", slot_troop_notes),

            (str_clear, s0),

            (str_store_troop_name, s20, ":troop_no"),
            (try_begin),
                (troop_slot_eq, ":troop_no", slot_troop_notes, tn_unknown),
                (str_store_string, s0, "@{s20} is unknown."),
            (else_try),
                (store_and, ":know_faction", ":troop_notes", tn_know_faction),
                (try_begin),
                    (ge, ":know_faction", 1),
                    (store_troop_faction, ":troop_faction", ":troop_no"),
                    (str_store_faction_name_link, s21, ":troop_faction"),

                    (store_and, ":know_faction_rank", ":troop_notes", tn_know_faction_rank),
                    (try_begin),
                        (ge, ":know_faction_rank", 1),
                        (faction_slot_eq, ":troop_faction", slot_faction_leader, ":troop_no"),
                        (str_store_string, s0, "@{s0} is leader of the {s21}.^"),
                    (else_try),
                        (str_store_string, s0, "@{s0} is a vassal of the {s21}.^"),
                    (try_end),
                    (try_begin),
                        (ge, ":know_faction_rank", 1),
                        (faction_slot_eq, ":troop_faction", slot_faction_marshall, ":troop_no"),
                        (str_store_string, s0, "@{s0}He is the current marhsall.^"),
                    (try_end),
                (try_end),
                (store_and, ":know_face", ":troop_notes", tn_know_face),
                (try_begin),
                    (ge, ":know_face", 1),
                    (add_troop_note_tableau_mesh, ":troop_no", "tableau_troop_note_mesh"),
                (try_end),
            (try_end),

            (set_trigger_result, 1),
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
            (store_script_param, ":faction_no", 1),
            (store_script_param, ":note_index", 2),

            (str_clear, s0),

            (str_store_faction_name, s12, ":faction_no"),

            (try_begin),
                (eq, ":note_index", 0),
                (str_store_string, s0, "@{s12}"),

                (faction_get_slot, ":leader", ":faction_no", slot_faction_leader),
                (try_begin),
                    (ge, ":leader", 0),
                    (str_store_troop_name_link, s10, ":leader"),
                    (str_store_string, s0, "@{s0} is lead by {s10}"),
                (try_end),

            (else_try),
                (eq, ":note_index", 1),
                # ToDo: faction relations
                # ToDo: faction territories
                (str_store_string, s0, "@Current territories: ^"),
                (str_clear, s10),
                (try_for_range, ":cur_center", centers_begin, centers_end),
                    (store_faction_of_party, ":center_faction", ":cur_center"),
                    (eq, ":center_faction", ":faction_no"),
                    (str_store_party_name_link, s11, ":cur_center"),
                    (try_begin),
                        (str_is_empty, s10),
                        (str_store_string, s10, "@{s10}{s11}"),
                    (else_try),
                        (str_store_string, s10, "@{s10}, {s11}"),
                    (try_end),
                (try_end),
                (try_begin),
                    (str_is_empty, s10),
                    (str_store_string, s0, "@{s0}{s12} owns no land."),
                (else_try),
                    (str_store_string, s0, "@{s0}{s10}"),
                (try_end),
            (else_try),
                (eq, ":note_index", 2),
                # ToDo: faction policies
                # (try_for_range, ":cur_faction", kingdoms_begin, kingdoms_end),
                #     (neq, ":cur_faction", ":faction_no"),
                #     (store_relation, ":relation", ":cur_faction", ":faction_no"),
                # (try_end),
            (else_try),
                (eq, ":note_index", 3),
                # ToDo: faction vassals and mercenaries
                (try_for_range, ":cur_lord", npc_heroes_begin, npc_heroes_end),
                    (troop_slot_eq, ":cur_lord", slot_troop_kingdom_occupation, tko_kingdom_hero),
                    (store_troop_faction, ":troop_faction", ":cur_lord"),
                    (eq, ":troop_faction", ":faction_no"),
                    (troop_get_slot, ":known", ":cur_lord", slot_troop_notes),
                    (val_and, ":known", tn_know_faction|tn_know_faction_rank),
                    (ge, ":known", 1),
                (try_end),
            (try_end),

            (set_trigger_result, 1),
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
            (store_script_param, ":party_no", 1),
            (party_get_slot, ":leader", ":party_no", slot_party_leader),
            (assign, ":limit", 0),
            (try_begin),
                (ge, ":leader", 0),
                (troop_is_hero, ":leader"),
                (store_skill_level, ":prisoner_level", skl_prisoner_management, ":leader"),

                (val_mul, ":prisoner_level", 10),

                (val_mul, ":limit", ":prisoner_level"),
                (val_div, ":limit", 100),
            (else_try),
                # Parties with no leader or non-hero leaders are considered having 1 in prisoner management
                # Means 10% of party size max can be prisoners
                (val_div, ":limit", 10),
            (try_end),
            (assign, reg0, ":limit"),
            (set_trigger_result, reg0),
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
            (try_begin),
                # (is_between, ":item_no", goods_begin, goods_end),
                (ge, "$g_trading", 1),
                (assign, ":tax_rate", 0),
                (assign, ":string", 0),
                (try_begin),
                    (eq, ":extra_text_id", 6),
                    (party_get_slot, ":tax_rate", "$g_encountered_party", slot_party_taxes_buy),
                    (assign, ":string", "str_item_taxes_buy"),
                    (assign, reg10, ":tax_rate"),
                (else_try),
                    (eq, ":extra_text_id", 7),
                    (party_get_slot, ":tax_rate", "$g_encountered_party", slot_party_taxes_sell),
                    (assign, ":string", "str_item_taxes_sell"),
                    (assign, reg10, ":tax_rate"),
                (try_end),
                (gt, ":string", 0),
                (str_store_string, s0, ":string"),
                (set_result_string, s0),
                (set_trigger_result, 0x87CAD1),
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
            # (store_script_param, ":troop_no", 1),
            # (store_script_param, ":skill_no", 2),
            (set_trigger_result, 0),
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
                (eq, ":party_no_seer", "$g_player_party"),

                (try_begin),
                    (store_faction_of_party, ":seen_faction", ":party_no_seen"),
                    (is_between, ":seen_faction", kingdoms_begin, kingdoms_end),
                    (faction_set_note_available, ":seen_faction", 1),
                (try_end),

                (party_get_slot, ":party_type", ":party_no_seen", slot_party_type),
                (is_between, ":party_type", spt_village, spt_fort + 1),

                (party_set_flags, ":party_no_seen", pf_always_visible, 1),
                (party_set_note_available, ":party_no_seen", 1),

            (try_end),
            (set_trigger_result, 1),
        ]),

    #script_game_get_party_speed_multiplier
        # This script is called from the game engine when a skill's modifiers are needed
        # INPUT: arg1 = party_no
        # OUTPUT: trigger_result = multiplier (scaled by 100, meaning that giving 100 as the trigger result does not change the party speed)
    ("game_get_party_speed_multiplier",
        [
            # (store_script_param, ":party_no", 1),
            # (assign, ":speed", 100),

            # (call_script, "script_game_get_party_prisoner_limit", ":party_no"),
            # (assign, ":prisoner_limit", reg0),

            # (party_get_num_companions, ":party_size", ":party_no"),
            # (party_get_num_prisoners, ":prisoner_size", ":party_no"),

            # (try_begin),
            #     (gt, ":party_size", ":party_limit"),
            #     (store_mul, ":party_modifier", ":party_size", 100),
            #     (val_div, ":party_modifier", ":party_limit"),

            #     (val_mul, ":speed", 100),
            #     (val_div, ":speed", ":party_modifier"),
            # (try_end),
            # (try_end),
            #     (gt, ":prisoner_size", ":prisoner_limit"),
            #     (store_mul, ":prisoner_modifier", ":prisoner_limit"),
            #     (val_div, ":prisoner_modifier", ":party_limit"),

            #     (val_mul, ":speed", 100),
            #     (val_div, ":speed", ":prisoner_modifier"),
            # (try_end),

            # (val_max, ":speed", 50),

            # (set_trigger_result, ":speed"),

            (set_trigger_result, 100),
        ]),

    #script_game_get_console_command
        # This script is called from the game engine when a console command is entered from the dedicated server.
        # INPUT: anything
        # OUTPUT: s0 = result text
    ("game_get_console_command",
        [
        ]),
    
    # script_clear_party_group:
    # input:
    #   arg1: Party-id of the root of the group.
    # This script will clear the root party and all parties attached to it recursively.
    ("clear_party_group",
        [
            (store_script_param_1, ":root_party"),

            (party_get_num_attached_parties, ":num_attached_parties", ":root_party"),
            (try_for_range, ":attached_party_rank", 0, ":num_attached_parties"),
                (party_get_attached_party_with_rank, ":attached_party", ":root_party", ":attached_party_rank"),
                (call_script, "script_clear_party_group", ":attached_party"),
            (try_end),

            (party_clear, ":root_party"),
            (try_begin),
                (neg|is_between, ":root_party", centers_begin, centers_end),
                (remove_party, ":root_party"),
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
    ##         (cur_tableau_set_override_flags, af_override_head|af_override_weapons),
            
            (init_position, pos2),
            (cur_tableau_set_camera_parameters, 1, 4, 8, 10, 10000),
    
            (init_position, pos5),
            (assign, ":cam_height", 150),
    #         (val_mod, ":camera_distance", 5),
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
    #         (val_mod, ":camera_distance", 5),
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
    #         (val_mod, ":camera_distance", 5),
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
        ##      (else_try), #not used
        ##        (cur_tableau_add_override_item, "itm_heraldic_mail_with_tabard"),
        ##        (cur_tableau_add_override_item, "itm_iron_greaves"),
        ##        (cur_tableau_add_override_item, "itm_sword_medieval_c"),
        ##        (assign, ":animation", "anim_pose_5"),
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
            (cur_tableau_add_troop, "$g_player_troop", pos2, ":animation", 0),
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
    # script_agent_troop_get_banner_mesh
        # input: 
        #   arg1: agent_no
        #   arg2: troop_no
        # output: 
        #   reg0: banner_mesh
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
                    (eq, ":troop_no", "$g_player_troop"),
                    (assign, ":banner_troop", ":troop_no"),
                (else_try),
                    (is_between, ":troop_no", companions_begin, companions_end),
                    (assign, ":banner_troop", "$g_player_troop"),
                (else_try),
                    (assign, ":banner_mesh", "mesh_banners_default_a"),
                (try_end),
            (else_try),
                (agent_get_troop_id, ":troop_id", ":agent_no"),
                (this_or_next|troop_slot_ge,  ":troop_id", slot_troop_banner_scene_prop, 1),
                (eq, ":troop_no", "$g_player_troop"),
                (assign, ":banner_troop", ":troop_id"),
            (else_try),
                (agent_get_party_id, ":agent_party", ":agent_no"),
                (try_begin),
                    (lt, ":agent_party", 0),
                    (is_between, ":troop_id", companions_begin, companions_end),
                    (main_party_has_troop, ":troop_id"),
                    (assign, ":agent_party", "$g_player_party"),
                (try_end),
                (ge, ":agent_party", 0),
                (try_begin),
                    (is_between, ":agent_party", centers_begin, centers_end),
                    (party_get_slot, ":town_lord", "$g_encountered_party", slot_party_leader),
                    (ge, ":town_lord", 0),
                    (assign, ":banner_troop", ":town_lord"),
                (else_try),
                    (this_or_next|party_slot_eq, ":agent_party", slot_party_type, spt_war_party),
                    (eq, ":agent_party", "$g_player_party"),
                    (party_get_num_companion_stacks, ":num_stacks", ":agent_party"),
                    (gt, ":num_stacks", 0),
                    (party_stack_get_troop_id, ":leader_troop_id", ":agent_party", 0),
                    (this_or_next|troop_slot_ge,  ":leader_troop_id", slot_troop_banner_scene_prop, 1),
                    (eq, ":leader_troop_id", "$g_player_troop"),
                    (assign, ":banner_troop", ":leader_troop_id"),
                (try_end),
            (else_try),
                (is_between, ":troop_id", soldiers_begin, soldiers_end),
                (store_troop_faction, ":troop_faction", ":troop_id"),
                (faction_get_slot, ":culture", ":troop_faction", slot_faction_culture),
                (try_begin),
                    (eq, ":culture", "fac_culture_1"),
                    (assign, ":banner_mesh", "mesh_arms_kingdom_f"),
                (else_try),
                    (eq, ":culture", "fac_culture_2"),
                    (assign, ":banner_mesh", "mesh_arms_kingdom_b"),
                (else_try),
                    (eq, ":culture", "fac_culture_3"),
                    (assign, ":banner_mesh", "mesh_arms_kingdom_c"),
                (else_try),
                    (eq, ":culture", "fac_culture_4"),
                    (assign, ":banner_mesh", "mesh_arms_kingdom_a"),
                (else_try),
                    (eq, ":culture", "fac_culture_5"),
                    (assign, ":banner_mesh", "mesh_arms_kingdom_d"),
                (else_try),
                    (eq, ":culture", "fac_culture_6"),
                    (assign, ":banner_mesh", "mesh_arms_kingdom_e"),
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
    
    # script_init_arms_colors
    # input: none
    # output: none
    ("init_arms_colors",
        [
            # Primary colors
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a01 - arms_meshes_begin, 0xFF8C4531),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a02 - arms_meshes_begin, 0xFFD6D7CE),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a03 - arms_meshes_begin, 0xFF393A39),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a04 - arms_meshes_begin, 0xFFAD9229),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a05 - arms_meshes_begin, 0xFF4C7933),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a06 - arms_meshes_begin, 0xFF86392E),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a07 - arms_meshes_begin, 0xFFD3D4CB),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a08 - arms_meshes_begin, 0xFF232523),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a09 - arms_meshes_begin, 0xFFDEDFD6),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a10 - arms_meshes_begin, 0xFF52496B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a11 - arms_meshes_begin, 0xFFCECFC6),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a12 - arms_meshes_begin, 0xFFB7AC36),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a13 - arms_meshes_begin, 0xFF736D42),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a14 - arms_meshes_begin, 0xFFDEDFD6),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a15 - arms_meshes_begin, 0xFFCECFC6),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a16 - arms_meshes_begin, 0xFFC3C4BA),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a17 - arms_meshes_begin, 0xFFCED3C6),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a18 - arms_meshes_begin, 0xFFD0D1C8),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a19 - arms_meshes_begin, 0xFFDEDFD6),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a20 - arms_meshes_begin, 0xFF525918),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a21 - arms_meshes_begin, 0xFF333C65),
            
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b01 - arms_meshes_begin, 0xFF9F9444),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b02 - arms_meshes_begin, 0xFFA2983F),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b03 - arms_meshes_begin, 0xFF5F8047),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b04 - arms_meshes_begin, 0xFFB5B6AD),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b05 - arms_meshes_begin, 0xFF425963),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b06 - arms_meshes_begin, 0xFF8C3021),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b07 - arms_meshes_begin, 0xFF7B2821),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b08 - arms_meshes_begin, 0xFFB2AB31),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b09 - arms_meshes_begin, 0xFF9C382B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b10 - arms_meshes_begin, 0xFF4A618C),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b11 - arms_meshes_begin, 0xFFA59229),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b12 - arms_meshes_begin, 0xFFC8C5C0),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b13 - arms_meshes_begin, 0xFF866712),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b14 - arms_meshes_begin, 0xFFADA242),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b15 - arms_meshes_begin, 0xFF6B7110),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b16 - arms_meshes_begin, 0xFF313128),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b17 - arms_meshes_begin, 0xFFA23A33),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b18 - arms_meshes_begin, 0xFF526E41),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b19 - arms_meshes_begin, 0xFFA5654A),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b20 - arms_meshes_begin, 0xFF526B39),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b21 - arms_meshes_begin, 0xFF863C33),
            
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c01 - arms_meshes_begin, 0xFF737FB7),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c02 - arms_meshes_begin, 0xFFC38547),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c03 - arms_meshes_begin, 0xFFA5594A),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c04 - arms_meshes_begin, 0xFF3E6386),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c05 - arms_meshes_begin, 0xFFE4E3D8),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c06 - arms_meshes_begin, 0xFF9C6D39),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c07 - arms_meshes_begin, 0xFFD6D7D0),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c08 - arms_meshes_begin, 0xFF754A86),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c09 - arms_meshes_begin, 0xFF997244),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c10 - arms_meshes_begin, 0xFFC5C3BA),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c11 - arms_meshes_begin, 0xFF624B96),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c12 - arms_meshes_begin, 0xFF943421),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c13 - arms_meshes_begin, 0xFFC0BAAA),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c14 - arms_meshes_begin, 0xFF363529),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c15 - arms_meshes_begin, 0xFF8C8423),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c16 - arms_meshes_begin, 0xFF4F6A2E),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c17 - arms_meshes_begin, 0xFFC3C1B7),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c18 - arms_meshes_begin, 0xFF393829),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c19 - arms_meshes_begin, 0xFF73618C),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c20 - arms_meshes_begin, 0xFF4A658C),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c21 - arms_meshes_begin, 0xFF33342B),
            
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d01 - arms_meshes_begin, 0xFF783D2B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d02 - arms_meshes_begin, 0xFF313431),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d03 - arms_meshes_begin, 0xFF424D73),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d04 - arms_meshes_begin, 0xFFE1DFD8),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d05 - arms_meshes_begin, 0xFF836E33),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d06 - arms_meshes_begin, 0xFF917629),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d07 - arms_meshes_begin, 0xFF363531),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d08 - arms_meshes_begin, 0xFF9F4631),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d09 - arms_meshes_begin, 0xFFDEDFD6),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d10 - arms_meshes_begin, 0xFF548C39),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d11 - arms_meshes_begin, 0xFF78651B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d12 - arms_meshes_begin, 0xFF9C4531),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d13 - arms_meshes_begin, 0xFFD3D4CB),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d14 - arms_meshes_begin, 0xFF4A6594),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d15 - arms_meshes_begin, 0xFF2B2D2B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d16 - arms_meshes_begin, 0xFF6B7921),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d17 - arms_meshes_begin, 0xFFC0AE33),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d18 - arms_meshes_begin, 0xFF734D29),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d19 - arms_meshes_begin, 0xFFD8D8D0),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d20 - arms_meshes_begin, 0xFF897121),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d21 - arms_meshes_begin, 0xFF477473),
            
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e01 - arms_meshes_begin, 0xFF313431),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e02 - arms_meshes_begin, 0xFF9F4A36),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e03 - arms_meshes_begin, 0xFFCECFC5),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e04 - arms_meshes_begin, 0xFFD8D8D3),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e05 - arms_meshes_begin, 0xFF39455A),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e06 - arms_meshes_begin, 0xFF9F8631),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e07 - arms_meshes_begin, 0xFF9C4539),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e08 - arms_meshes_begin, 0xFFA19231),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e09 - arms_meshes_begin, 0xFFA14331),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e10 - arms_meshes_begin, 0xFF896E10),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e11 - arms_meshes_begin, 0xFF333233),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e12 - arms_meshes_begin, 0xFF3C4A57),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e13 - arms_meshes_begin, 0xFF4A6594),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e14 - arms_meshes_begin, 0xFF33322E),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e15 - arms_meshes_begin, 0xFFA13D2B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e16 - arms_meshes_begin, 0xFFBD9608),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e17 - arms_meshes_begin, 0xFF5A8A4A),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e18 - arms_meshes_begin, 0xFFDBD9D3),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e19 - arms_meshes_begin, 0xFFDBDCD3),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e20 - arms_meshes_begin, 0xFF783529),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e21 - arms_meshes_begin, 0xFFD8D9D0),
            
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f01 - arms_meshes_begin, 0xFFCDA436),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f02 - arms_meshes_begin, 0xFFC8B470),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f03 - arms_meshes_begin, 0xFF314110),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f04 - arms_meshes_begin, 0xFF733018),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f05 - arms_meshes_begin, 0xFF946510),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f06 - arms_meshes_begin, 0xFFB77F10),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f07 - arms_meshes_begin, 0xFF817721),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f08 - arms_meshes_begin, 0xFF965700),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f09 - arms_meshes_begin, 0xFF292523),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f10 - arms_meshes_begin, 0xFFB59E31),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f11 - arms_meshes_begin, 0xFF997A29),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f12 - arms_meshes_begin, 0xFF758486),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f13 - arms_meshes_begin, 0xFFA79465),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f14 - arms_meshes_begin, 0xFF653657),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f15 - arms_meshes_begin, 0xFF681E15),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f16 - arms_meshes_begin, 0xFF123144),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f17 - arms_meshes_begin, 0xFF4A4500),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f18 - arms_meshes_begin, 0xFF68350D),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f19 - arms_meshes_begin, 0xFF212839),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f20 - arms_meshes_begin, 0xFF5E6B67),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f21 - arms_meshes_begin, 0xFFA58A08),
            
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_kingdom_f - arms_meshes_begin, 0xFF54211E),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_kingdom_b - arms_meshes_begin, 0xFFD6CBBD),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_kingdom_c - arms_meshes_begin, 0xFF633039),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_kingdom_a - arms_meshes_begin, 0xFF31668E),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_kingdom_d - arms_meshes_begin, 0xFF426D31),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_kingdom_e - arms_meshes_begin, 0xFFC5A84C),
            
            (troop_set_slot, "trp_banner_background_color_array", mesh_banners_default_a - arms_meshes_begin, 0xFF212221),
            (troop_set_slot, "trp_banner_background_color_array", mesh_banners_default_b - arms_meshes_begin, 0xFF212221),
            (troop_set_slot, "trp_banner_background_color_array", mesh_banners_default_c - arms_meshes_begin, 0xFF2D3804),
            (troop_set_slot, "trp_banner_background_color_array", mesh_banners_default_d - arms_meshes_begin, 0xFFBDBEBD),
            (troop_set_slot, "trp_banner_background_color_array", mesh_banners_default_e - arms_meshes_begin, 0xFF394608),
            
            # Secondary colors
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a01 - arms_meshes_begin + arms_meshes_end, 0xFF23110A),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a02 - arms_meshes_begin + arms_meshes_end, 0xFF33565D),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a03 - arms_meshes_begin + arms_meshes_end, 0xFFBABAAF),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a04 - arms_meshes_begin + arms_meshes_end, 0xFF2E280A),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a05 - arms_meshes_begin + arms_meshes_end, 0xFFBDB618),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a06 - arms_meshes_begin + arms_meshes_end, 0xFF364973),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a07 - arms_meshes_begin + arms_meshes_end, 0xFF7B3429),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a08 - arms_meshes_begin + arms_meshes_end, 0xFFB5A629),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a09 - arms_meshes_begin + arms_meshes_end, 0xFF962221),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a10 - arms_meshes_begin + arms_meshes_end, 0xFFA5A69C),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a11 - arms_meshes_begin + arms_meshes_end, 0xFF8C3029),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a12 - arms_meshes_begin + arms_meshes_end, 0xFF181408),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a13 - arms_meshes_begin + arms_meshes_end, 0xFF0A0A05),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a14 - arms_meshes_begin + arms_meshes_end, 0xFF752D29),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a15 - arms_meshes_begin + arms_meshes_end, 0xFF8C2929),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a16 - arms_meshes_begin + arms_meshes_end, 0xFF3C4989),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a17 - arms_meshes_begin + arms_meshes_end, 0xFF3E612B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a18 - arms_meshes_begin + arms_meshes_end, 0xFF212021),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a19 - arms_meshes_begin + arms_meshes_end, 0xFF232523),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a20 - arms_meshes_begin + arms_meshes_end, 0xFFCBCBC0),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_a21 - arms_meshes_begin + arms_meshes_end, 0xFF8C8639),
            
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b01 - arms_meshes_begin + arms_meshes_end, 0xFF844D36),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b02 - arms_meshes_begin + arms_meshes_end, 0xFF4A456B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b03 - arms_meshes_begin + arms_meshes_end, 0xFF843421),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b04 - arms_meshes_begin + arms_meshes_end, 0xFF813426),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b05 - arms_meshes_begin + arms_meshes_end, 0xFF788731),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b06 - arms_meshes_begin + arms_meshes_end, 0xFF527939),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b07 - arms_meshes_begin + arms_meshes_end, 0xFFBAB6AA),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b08 - arms_meshes_begin + arms_meshes_end, 0xFF525D10),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b09 - arms_meshes_begin + arms_meshes_end, 0xFFC6B6A5),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b10 - arms_meshes_begin + arms_meshes_end, 0xFF6B1818),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b11 - arms_meshes_begin + arms_meshes_end, 0xFFA53F33),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b12 - arms_meshes_begin + arms_meshes_end, 0xFF9C4139),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b13 - arms_meshes_begin + arms_meshes_end, 0xFF944D39),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b14 - arms_meshes_begin + arms_meshes_end, 0xFF292810),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b15 - arms_meshes_begin + arms_meshes_end, 0xFFAD9618),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b16 - arms_meshes_begin + arms_meshes_end, 0xFFAA503F),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b17 - arms_meshes_begin + arms_meshes_end, 0xFF4C5633),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b18 - arms_meshes_begin + arms_meshes_end, 0xFF2E2A20),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b19 - arms_meshes_begin + arms_meshes_end, 0xFF627184),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b20 - arms_meshes_begin + arms_meshes_end, 0xFF9CA489),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_b21 - arms_meshes_begin + arms_meshes_end, 0xFFBDB6AD),

            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c01 - arms_meshes_begin + arms_meshes_end, 0xFF739B4F),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c02 - arms_meshes_begin + arms_meshes_end, 0xFFBDAD99),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c03 - arms_meshes_begin + arms_meshes_end, 0xFFC6C7BD),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c04 - arms_meshes_begin + arms_meshes_end, 0xFFD3D3CB),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c05 - arms_meshes_begin + arms_meshes_end, 0xFF7B8A42),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c06 - arms_meshes_begin + arms_meshes_end, 0xFF362D1B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c07 - arms_meshes_begin + arms_meshes_end, 0xFF5A4A70),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c08 - arms_meshes_begin + arms_meshes_end, 0xFFD6D3CE),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c09 - arms_meshes_begin + arms_meshes_end, 0xFF393C5A),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c10 - arms_meshes_begin + arms_meshes_end, 0xFF6B2C21),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c11 - arms_meshes_begin + arms_meshes_end, 0xFFA59642),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c12 - arms_meshes_begin + arms_meshes_end, 0xFFE1E1DE),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c13 - arms_meshes_begin + arms_meshes_end, 0xFF54365A),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c14 - arms_meshes_begin + arms_meshes_end, 0xFF8C8336),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c15 - arms_meshes_begin + arms_meshes_end, 0xFF425D10),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c16 - arms_meshes_begin + arms_meshes_end, 0xFF683F33),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c17 - arms_meshes_begin + arms_meshes_end, 0xFF753123),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c18 - arms_meshes_begin + arms_meshes_end, 0xFFC6C3BD),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c19 - arms_meshes_begin + arms_meshes_end, 0xFF994D57),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c20 - arms_meshes_begin + arms_meshes_end, 0xFFBABAAF),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_c21 - arms_meshes_begin + arms_meshes_end, 0xFF9C9E94),

            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d01 - arms_meshes_begin + arms_meshes_end, 0xFF150A08),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d02 - arms_meshes_begin + arms_meshes_end, 0xFFC6C7C6),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d03 - arms_meshes_begin + arms_meshes_end, 0xFF9F3131),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d04 - arms_meshes_begin + arms_meshes_end, 0xFFA22E2E),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d05 - arms_meshes_begin + arms_meshes_end, 0xFF6B3818),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d06 - arms_meshes_begin + arms_meshes_end, 0xFF733021),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d07 - arms_meshes_begin + arms_meshes_end, 0xFFD6D7D6),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d08 - arms_meshes_begin + arms_meshes_end, 0xFFBA7D1B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d09 - arms_meshes_begin + arms_meshes_end, 0xFF212021),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d10 - arms_meshes_begin + arms_meshes_end, 0xFF944531),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d11 - arms_meshes_begin + arms_meshes_end, 0xFF211C08),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d12 - arms_meshes_begin + arms_meshes_end, 0xFFE7DFDE),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d13 - arms_meshes_begin + arms_meshes_end, 0xFF833826),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d14 - arms_meshes_begin + arms_meshes_end, 0xFFEFF3EF),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d15 - arms_meshes_begin + arms_meshes_end, 0xFFDEDFDE),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d16 - arms_meshes_begin + arms_meshes_end, 0xFFECEDE4),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d17 - arms_meshes_begin + arms_meshes_end, 0xFF843421),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d18 - arms_meshes_begin + arms_meshes_end, 0xFF181008),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d19 - arms_meshes_begin + arms_meshes_end, 0xFF181918),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d20 - arms_meshes_begin + arms_meshes_end, 0xFF318E7B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_d21 - arms_meshes_begin + arms_meshes_end, 0xFFD6D3D6),

            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e01 - arms_meshes_begin + arms_meshes_end, 0xFF96771D),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e02 - arms_meshes_begin + arms_meshes_end, 0xFF2B2A2B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e03 - arms_meshes_begin + arms_meshes_end, 0xFF4A2863),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e04 - arms_meshes_begin + arms_meshes_end, 0xFF2B2A29),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e05 - arms_meshes_begin + arms_meshes_end, 0xFFBABABA),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e06 - arms_meshes_begin + arms_meshes_end, 0xFF913231),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e07 - arms_meshes_begin + arms_meshes_end, 0xFF4A659C),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e08 - arms_meshes_begin + arms_meshes_end, 0xFF5A6D18),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e09 - arms_meshes_begin + arms_meshes_end, 0xFFA58629),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e10 - arms_meshes_begin + arms_meshes_end, 0xFF3C4780),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e11 - arms_meshes_begin + arms_meshes_end, 0xFFC6C7C6),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e12 - arms_meshes_begin + arms_meshes_end, 0xFFD0D0D0),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e13 - arms_meshes_begin + arms_meshes_end, 0xFF8C4241),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e14 - arms_meshes_begin + arms_meshes_end, 0xFFA55542),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e15 - arms_meshes_begin + arms_meshes_end, 0xFFCECBC6),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e16 - arms_meshes_begin + arms_meshes_end, 0xFF31558C),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e17 - arms_meshes_begin + arms_meshes_end, 0xFFC8C918),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e18 - arms_meshes_begin + arms_meshes_end, 0xFF844131),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e19 - arms_meshes_begin + arms_meshes_end, 0xFF732C21),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e20 - arms_meshes_begin + arms_meshes_end, 0xFFB78905),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_e21 - arms_meshes_begin + arms_meshes_end, 0xFF841808),

            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f01 - arms_meshes_begin + arms_meshes_end, 0xFF180D00),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f02 - arms_meshes_begin + arms_meshes_end, 0xFF332E29),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f03 - arms_meshes_begin + arms_meshes_end, 0xFF948C35),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f04 - arms_meshes_begin + arms_meshes_end, 0xFFB1880C),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f05 - arms_meshes_begin + arms_meshes_end, 0xFF652A12),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f06 - arms_meshes_begin + arms_meshes_end, 0xFF845500),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f07 - arms_meshes_begin + arms_meshes_end, 0xFFC5C58B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f08 - arms_meshes_begin + arms_meshes_end, 0xFFC0B889),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f09 - arms_meshes_begin + arms_meshes_end, 0xFF946B28),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f10 - arms_meshes_begin + arms_meshes_end, 0xFF213400),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f11 - arms_meshes_begin + arms_meshes_end, 0xFF573500),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f12 - arms_meshes_begin + arms_meshes_end, 0xFFBDC1C0),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f13 - arms_meshes_begin + arms_meshes_end, 0xFF3F0908),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f14 - arms_meshes_begin + arms_meshes_end, 0xFF210829),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f15 - arms_meshes_begin + arms_meshes_end, 0xFFB59452),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f16 - arms_meshes_begin + arms_meshes_end, 0xFF3C7391),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f17 - arms_meshes_begin + arms_meshes_end, 0xFFACA331),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f18 - arms_meshes_begin + arms_meshes_end, 0xFFBBB283),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f19 - arms_meshes_begin + arms_meshes_end, 0xFFA48310),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f20 - arms_meshes_begin + arms_meshes_end, 0xFF26291E),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_f21 - arms_meshes_begin + arms_meshes_end, 0xFF561E08),
            
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_kingdom_f - arms_meshes_begin + arms_meshes_end, 0xFF080202),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_kingdom_b - arms_meshes_begin + arms_meshes_end, 0xFF442A1B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_kingdom_c - arms_meshes_begin + arms_meshes_end, 0xFFD0A03C),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_kingdom_a - arms_meshes_begin + arms_meshes_end, 0xFF05090D),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_kingdom_d - arms_meshes_begin + arms_meshes_end, 0xFF050A05),
            (troop_set_slot, "trp_banner_background_color_array", mesh_arms_kingdom_e - arms_meshes_begin + arms_meshes_end, 0xFF7B2D0D), 
            
            (troop_set_slot, "trp_banner_background_color_array", mesh_banners_default_a - arms_meshes_begin + arms_meshes_end, 0xFF524F14),
            (troop_set_slot, "trp_banner_background_color_array", mesh_banners_default_b - arms_meshes_begin + arms_meshes_end, 0xFF60240D),
            (troop_set_slot, "trp_banner_background_color_array", mesh_banners_default_c - arms_meshes_begin + arms_meshes_end, 0xFF8C7D18),
            (troop_set_slot, "trp_banner_background_color_array", mesh_banners_default_d - arms_meshes_begin + arms_meshes_end, 0xFF415B7B),
            (troop_set_slot, "trp_banner_background_color_array", mesh_banners_default_e - arms_meshes_begin + arms_meshes_end, 0xFF703002),
        ]),
    
    # script_test_spawn_team_members
    # input: 
    #   arg1: team
    #   arg2: spawn_point
    # output: none
    ("test_spawn_team_members",
        [
            (store_script_param, ":team_no", 1),
            (store_script_param, ":spawn_point", 2),
            
            (call_script, "script_test_spawn_team_members_siege", ":team_no", ":spawn_point"),
        ]),
    
    # script_test_spawn_team_members_siege
    # input:
    #   arg1: team
    #   arg2: spawn_point
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
            (try_end),
        ]),
    
    # script_agent_reassign_division
    # input:
    #   arg1: agent_no
    #   arg2: no_reinforcement_group, don't use reinforcements groups
    # output:
    #   reg0: division
    ("agent_reassign_division",
        [
            (store_script_param, ":agent_no", 1),
            (store_script_param, ":no_reinforcement_group", 2),
            
            (assign, ":new_div", -1),
            
            (agent_get_team, ":team", ":agent_no"),
            (try_begin),
                (agent_slot_eq, ":agent_no", slot_agent_charge, 1),
                (assign, ":new_div", grc_charge_group),
            (else_try),
                (agent_get_horse, ":horse", ":agent_no"),
                (agent_get_ammo, ":ammo", ":agent_no", 0),
                
                (assign, ":has_ranged", 0),
                # 2 Is xbow/bow 1 is throwing
                (assign, ":has_shield", 0),
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
                            (this_or_next|is_between, ":item", "itm_long_bow", "itm_war_bow"),
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
                    (agent_slot_eq, ":agent_no", slot_agent_is_reinforcement, 1),
                    (eq, ":no_reinforcement_group", 0),
                    (try_begin),
                        (gt, ":horse", 0),
                        (assign, ":new_div", grc_reinforcement_cavalry),
                    (else_try),
                        (gt, ":has_ranged", 1), # Bows/xbows
                        (gt, ":ammo", 0),
                        (assign, ":new_div", grc_reinforcement_archer),
                    (else_try),
                        (try_begin),
                        #     (agent_get_division, ":old_div", ":agent_no"),
                        #     (eq, ":old_div", grc_reinforcement_archer),
                        #     (agent_set_slot, ":agent_no", slot_agent_is_reinforcement, 0),
                        # (else_try),
                            (assign, ":new_div", grc_reinforcement_infantry),
                        (try_end),
                    (try_end),
                    (ge, ":new_div", 0),
                (else_try),
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
    #   arg1: agent_no
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
                    (this_or_next|le, ":ammo", 1),
                    (agent_slot_eq, ":agent_no", slot_agent_forced_defend, 1),
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
                    (neg|agent_slot_eq, ":agent_no", slot_agent_forced_defend, 1),
                    (gt, ":ammo", 1),
                    
                    (agent_set_slot, ":agent_no", slot_agent_is_reinforcement, 0),
                    (call_script, "script_agent_reassign_division", ":agent_no", 1),
                    (try_begin),
                        (eq, reg0, grc_infantry),
                        (agent_set_slot, ":agent_no", slot_agent_new_division, ":division"),
                        (agent_set_division, ":agent_no", ":division"),
                        (agent_set_slot, ":agent_no", slot_agent_is_reinforcement, 0),
                    (else_try),
                        (agent_set_slot, ":agent_no", slot_agent_is_reinforcement, 1),
                    (try_end),
                    # (agent_set_slot, ":agent_no", slot_agent_new_division, grc_archers),
                    # (agent_set_division, ":agent_no", grc_archers),

                    (agent_set_slot, ":agent_no", slot_agent_target_entry_point, 0),
                    (agent_set_slot, ":agent_no", slot_agent_is_in_scripted_mode, 0),
                (try_end),
            (else_try),
                (call_script, "script_agent_reassign_division", ":agent_no", 1),
            (try_end),
        ]),
    
    # script_spawn_new_center_around_party
    # input:
    #   arg1: party_no
    #   arg2: spawn_type
    # Last argument is referring to what has caused the center to spawn
    # is it a revolted group of peasant, or is it an overpopulated center that sent them to make a village for raw materials
    # Is currently unused and may never be
    # output: new_party_id
    ("spawn_new_center_around_party",
        [
            (store_script_param, ":party_no", 1),
            # (store_script_param, ":spawn_type", 2),
            
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
    #   arg1: party_no
    # output; none
    ("party_init_center",
        [
            (store_script_param, ":party_no", 1),
            
            (store_faction_of_party, ":original_faction", ":party_no"),
            (party_set_slot, ":party_no", slot_party_original_faction, ":original_faction"),
            (party_set_slot, ":party_no", slot_party_faction, ":original_faction"),
            
            (party_set_slot, ":party_no", slot_party_ressource_radius, 3),
            
            (try_for_range, ":ressource", slot_party_ressources_begin, slot_party_ressources_end),
                (party_set_slot, ":party_no", ":ressource", 0),
            (try_end),
            
            (call_script, "script_party_update_nearby_resources", ":party_no"),
            #(call_script, "script_center_init_productions", ":party_no"),
            
            (party_set_slot, ":party_no", slot_party_wealth, 0),
            (party_set_slot, ":party_no", slot_party_prosperity, 50),
            
            (party_set_slot, ":party_no", slot_party_lord, -1),
            
            (party_set_slot, ":party_no", slot_party_besieged_by, -1),

            (party_get_slot, ":party_type", ":party_no", slot_party_type),
            (try_begin),
                (eq, ":party_type", spt_village),
                (party_set_slot, ":party_no", slot_party_population_noble, population_max_village * population_growth_village_noble / 100),
                (party_set_slot, ":party_no", slot_party_population_artisan, population_max_village * population_growth_village_artisan / 100),
                (party_set_slot, ":party_no", slot_party_population, population_max_village * population_growth_village_serf / 100),
                (party_set_slot, ":party_no", slot_party_population_slave, 0),
            
                (party_set_slot, ":party_no", slot_party_population_max, population_max_village),
            (else_try),
                (eq, ":party_type", spt_castle),
                (party_set_slot, ":party_no", slot_party_population_noble, population_max_castle * population_growth_castle_noble / 100),
                (party_set_slot, ":party_no", slot_party_population_artisan, population_max_castle * population_growth_castle_artisan / 100),
                (party_set_slot, ":party_no", slot_party_population, population_max_castle * population_growth_castle_serf / 100),
                (party_set_slot, ":party_no", slot_party_population_slave, 0),
            
                (party_set_slot, ":party_no", slot_party_population_max, population_max_castle),
            (else_try),
                (party_set_slot, ":party_no", slot_party_population_noble, population_max_town * population_growth_town_noble / 100),
                (party_set_slot, ":party_no", slot_party_population_artisan, population_max_town * population_growth_town_artisan / 100),
                (party_set_slot, ":party_no", slot_party_population, population_max_town * population_growth_town_serf / 100),
                (party_set_slot, ":party_no", slot_party_population_slave, 0),
            
                (party_set_slot, ":party_no", slot_party_population_max, population_max_town),
            (try_end),

            (party_set_slot, ":party_no", slot_party_taxes_buy, 5),
            (party_set_slot, ":party_no", slot_party_taxes_sell, 2),

            (party_set_slot, ":party_no", slot_party_taxes_visit, 20),

            (try_for_range, ":unused", 0, 10),
                (call_script, "script_party_process_ressources", ":party_no"),
                (call_script, "script_party_process_production", ":party_no"),
                (call_script, "script_party_process_population", ":party_no"),
                (call_script, "script_party_process_taxes", ":party_no"),
            (try_end),

            (call_script, "script_party_init_consumption", ":party_no"),
            
            (call_script, "script_party_get_siege_scene", ":party_no"),
            (assign, ":siege_scene", reg0),
            (party_set_slot, ":party_no", slot_party_siege_scene, ":siege_scene"),
        ]),
    
    # script_party_get_siege_scene
    # input:
    #   arg1: party_no
    # output:
    #   reg0: scene
    ("party_get_siege_scene",
        [
            (store_script_param, ":party_no", 1),
            
            (party_get_current_terrain, ":terrain", ":party_no"),
            (assign, ":scene", -1),
            
            (try_begin),
                (eq, ":terrain", rt_plain),
                (party_get_position, pos10, ":party_no"),
                (position_get_z, ":z", pos10),
                (try_begin),
                    (gt, ":z", 50), # ToDo: Find right value
                    (store_random_in_range, ":scene", castle_scene_plain_dark_begin, castle_scene_plain_dark_end),
                (else_try),
                    (store_random_in_range, ":scene", castle_scene_plain_begin, castle_scene_plain_wood_end),
                (try_end),
            (else_try),
                (eq, ":terrain", rt_forest),
                (store_random_in_range, ":scene", castle_scene_plain_wood_begin, castle_scene_plain_wood_end),
            (else_try),
                (eq, ":terrain", rt_steppe),
                (store_random_in_range, ":scene", castle_scene_steppe_begin, castle_scene_steppe_wood_end),
            (else_try),
                (eq, ":terrain", rt_steppe_forest),
                (store_random_in_range, ":scene", castle_scene_steppe_wood_begin, castle_scene_steppe_wood_end),
            (else_try),
                (this_or_next|eq, ":terrain", rt_desert),
                (eq, ":terrain", rt_desert_forest),
                (store_random_in_range, ":scene", castle_scene_desert_begin, castle_scene_desert_end),
            (else_try),
                (eq, ":terrain", rt_snow),
                (store_random_in_range, ":scene", castle_scene_snow_begin, castle_scene_snow_wood_end),
            (else_try),
                (eq, ":terrain", rt_snow_forest),
                (store_random_in_range, ":scene", castle_scene_snow_wood_begin, castle_scene_snow_wood_end),
            (else_try),
                (store_random_in_range, ":scene", castle_scene_plain_begin, castle_scene_plain_wood_end),
            (try_end),
            (assign, reg0, ":scene"),
        ]),
    
    # script_party_update_nearby_resources
    # input:
    #   arg1: party_no
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
                        
                        (call_script, "script_party_update_resources_slot_with_terrain_and_height", ":party_no", ":terrain_type", ":height", ":radius"),
                    (try_end),
                (try_end),
            (try_end),
            (call_script, "script_party_update_resources_slot_with_weather", ":party_no"),

            (assign, ":total_res", 0),
            (try_for_range, ":slot", slot_party_ressources_begin, slot_party_ressources_end),
                (party_get_slot, ":num_res", ":party_no", ":slot"),
                (val_add, ":total_res", ":num_res"),
            (try_end),
            (party_set_slot, ":party_no", slot_party_total_resources, ":total_res"),
            
            # (try_for_range, ":ressource", slot_party_ressources_begin, slot_party_ressources_end),
            #     (party_get_slot, reg10, ":party_no", ":ressource"),
            #     (gt, reg10, 0),
            #     (str_store_item_name, s10, ":ressource"),
            #     (str_store_party_name_link, s11, ":party_no"),
            #     (display_log_message, "@Center {s11} has ressource {s10}: {reg10}."),
            # (try_end),
            # (str_store_party_name_link, s11, ":party_no"),
            # (assign, res11, ":total_res"),
            # (display_log_message, "@{s11} has {reg11} resources."),
        ]),
    
    # script_party_get_resources_radius
    # input:
    #   arg1: party_no
    # output:
    #   reg0: resources_radius
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
    #   arg1: party_no
    #   arg2: terrain_type
    #   arg3: height
    #   arg4: radius
    # output: none
    ("party_update_resources_slot_with_terrain_and_height",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":terrain_type", 2),
            # (store_script_param, ":height", 3),
            (store_script_param, ":radius", 4),

            (val_mul, ":radius", 9),
            
            (try_begin),
                (eq, ":terrain_type", rt_water),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_fish", 10),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_salt", 10),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_oil", 1),
                
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, 1000, ":radius"),
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, 0, ":radius"),
            (else_try),
                (eq, ":terrain_type", rt_mountain),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_iron", 10),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_stone", 10),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_salt", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_clay", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wool", 2),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_dyes", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_furs", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 1),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_goat", 4),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_pig", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_venison", 2),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_apples", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_grapes", 6),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_olives", 1),
                # (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
                
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, -500, ":radius"),
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -1000, ":radius"),
            (else_try),
                (eq, ":terrain_type", rt_steppe),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_spice", 2),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_stone", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_clay", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_oil", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_flax", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wool", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 1),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_goat", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_cattle", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_poultry", 1),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_cabbages", 2),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_grain", 2),
                # (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
                
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, -1000, ":radius"),
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -200, ":radius"),
            (else_try),
                (eq, ":terrain_type", rt_plain),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_flax", 3),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_oil", 2),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wool", 3),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_stone", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 2),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_honey", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_cabbages", 3),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_apples", 5),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_grain", 6),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_cattle", 5),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_poultry", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_pig", 1),
                # (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
                
                # (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, 0, ":radius"),
                # (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, 0, ":radius"),
            (else_try),
                (eq, ":terrain_type", rt_snow),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_clay", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wool", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_furs", 5),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_stone", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 1),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_cabbages", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_grain", 1),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_pig", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_goat", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_venison", 2),
                # (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
                
                # (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, 0, ":radius"),
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -1800, ":radius"),
            (else_try),
                (eq, ":terrain_type", rt_desert),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_clay", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_dyes", 3),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_iron", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 1),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_date_fruit", 6),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_olives", 1),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_poultry", 2),
                # (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
                
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, -2000, ":radius"),
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, 2000, ":radius"),
            (else_try),
                (this_or_next|eq, ":terrain_type", rt_bridge),
                (eq, ":terrain_type", rt_river),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_fish", 4),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_cabbages", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_apples", 1),
                # (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
                
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, 2000, ":radius"),
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -200, ":radius"),
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

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_grapes", 1),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_goat", 5),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_venison", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_pig", 1),

                # (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
                
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, 0, ":radius"),
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -1200, ":radius"),
            (else_try),
                (eq, ":terrain_type", rt_steppe_forest),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_spice", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_oil", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_flax", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_silk", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 2),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_furs", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 4),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_apples", 1),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_goat", 2),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_venison", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_pig", 1),
                # (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
                
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, -500, ":radius"),
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -400, ":radius"),
            (else_try),
                (eq, ":terrain_type", rt_forest),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_flax", 2),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_oil", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wool", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_silk", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 3),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_furs", 2),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 6),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_apples", 2),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_goat", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_venison", 2),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_pig", 3),
                # (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
                
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, 500, ":radius"),
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -200, ":radius"),
            (else_try),
                (eq, ":terrain_type", rt_snow_forest),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wool", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_silk", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 3),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_furs", 8),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 8),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_pig", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_goat", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_venison", 6),
                # (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
                
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, 500, ":radius"),
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, -2000, ":radius"),
            (else_try),
                (eq, ":terrain_type", rt_desert_forest),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_dyes", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_silk", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_leather", 1),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_date_fruit", 10),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_wood", 2),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_grapes", 2),
                (call_script, "script_party_update_resources_slot", ":party_no", "itm_raw_olives", 2),

                (call_script, "script_party_update_resources_slot", ":party_no", "itm_venison", 2),
                # (call_script, "script_party_update_resources_slot", ":party_no", "itm_", 1),
                
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_wet, -1000, ":radius"),
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, 1500, ":radius"),
            (try_end),

            (try_begin),
                (party_get_position, pos1, ":party_no"),
                (position_get_y, ":y", pos1),
                (val_div, ":y", -100),
                (position_get_x, ":x", pos1),
                (val_div, ":x", 1000),
                (val_add, ":x", 300),
                (val_div, ":x", 5),
                (val_max, ":x", 30),
                (store_mul, ":position_heat", ":y", ":x"),
                (val_div, ":position_heat", 100),
                (call_script, "script_party_update_weather_slot", ":party_no", slot_party_weather_heat, ":position_heat", 1),
            (try_end),
        ]),

    # script_party_update_resources_slot_with_weather
    # input:
    #   arg1: party_no
    # output: none
    ("party_update_resources_slot_with_weather",
        [
            # (store_script_param, ":party_no", 1),

            # (party_get_slot, ":weather_heat", ":party_no", slot_party_weather_heat),
            # (party_get_slot, ":weather_wet", ":party_no", slot_party_weather_wet),

            # (store_sub, ":offset", slot_party_ressources_current_amount_begin, slot_party_ressources_begin),
            # (try_begin),
            #     (store_add, ":slot", "itm_apples", ":offset"),
            #     (party_slot_ge, ":party_no", ":slot", 1),
            # (try_end),
        ]),
    
    # script_party_update_resources_slot
    # input:
    #   arg1: party_no
    #   arg2: resource
    #   arg3: value
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
    #   arg1: party_no
    #   arg2: slot
    #   arg3: value
    # output: none
    ("party_update_weather_slot",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":slot", 2),
            (store_script_param, ":value", 3),
            (store_script_param, ":radius", 4),
            
            (party_get_slot, ":current_weather", ":party_no", ":slot"),
            (store_div, ":modified_value", ":value", ":radius"),
            (val_add, ":current_weather", ":modified_value"),
            (party_set_slot, ":party_no", ":slot", ":current_weather"),
        ]),

    # script_party_init_consumption
    # input:
    #   arg1: party_no
    # output: none
    ("party_init_consumption",
        [
            # (store_script_param, ":party_no", 1),
        ]),
    
    # script_init_productions
    # input: none
    # output: none
    ("init_productions",
        [
            # Storing all raw materials used to produce goods
            # Raw flax -> linen
            # Wool -> wool_cloth
            # Raw_silk + raw_dyes -> velvet
            # Iron -> tools
            # Raw_leather -> leatherwork
            # Raw_grapes -> wine
            # Grain -> ale
            # Grain -> bread
            # Raw_olives -> oil

            # Possible others ?
            # Cattle -> cattle_meat
            # Cattle -> butter
            # Cattle -> cheese
            # Pig -> pork
            # Pig -> sausages
            # Chicken -> chicken meat

            (item_set_slot, "itm_refined_wood", slot_item_produced_from_1, "itm_wood"),
            (item_set_slot, "itm_refined_wood", slot_item_produced_need_1, 20),
            (item_set_slot, "itm_refined_wood", slot_item_produced_quantity, 10),

            (item_set_slot, "itm_refined_stone", slot_item_produced_from_1, "itm_stone"),
            (item_set_slot, "itm_refined_stone", slot_item_produced_need_1, 20),
            (item_set_slot, "itm_refined_stone", slot_item_produced_quantity, 10),
        ]),
    
    # script_party_transfer_to_party
    # input:
    #   arg1: party_to_transfer
    #   arg2: receiving_party
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
    #   arg1: party_to_transfer
    #   arg2: receiving_party
    #   arg3: move heroes (0 no / 1 yes)
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
                
                (team_give_order, ":cur_team", grc_cavalry, mordr_mount),

                (team_give_order, ":cur_team", grc_reinforcement_infantry, mordr_stand_closer),
                
                (team_set_slot, ":cur_team", slot_team_battle_phase, stbp_combat),
                
                (call_script, "script_init_team_battle_ai", ":cur_team"),
            (try_end),
        ]),
    
    # script_init_team_battle_ai
    # input:
    #   arg1: team_no
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
                
                (store_random_in_range, ":formation", stf_default, stf_siege),
                # (try_begin),
                #     (eq, ":rand", 0),
                #     (assign, ":formation", stf_shieldwall),
                # (else_try),
                #     (assign, ":formation", stf_archers),
                # (try_end),
                (team_set_slot, ":team_no", slot_team_formation, ":formation"),
                
                (assign, ":tactic", stt_default),
                (store_random_in_range, ":rand", 0, 10),
                (try_begin),
                    (eq, ":rand", 0),
                    (assign, ":tactic", stt_defend),
                # (else_try),
                #     (eq, ":rand", 1),
                #     (assign, ":tactic", stt_defend_skirmish),
                (else_try),
                    (eq, ":rand", 2),
                    (assign, ":tactic", stt_short_engage),
                # (else_try),
                #     (eq, ":rand", 3),
                #     (assign, ":tactic", stt_shieldwall),
                (try_end),
                (team_set_slot, ":team_no", slot_team_tactic, ":tactic"),
                
                (call_script, "script_team_set_division_slots_for_formation", ":team_no", ":formation"),
                
                (team_give_order, ":team_no", grc_charge_group, mordr_charge),
                (team_give_order, ":team_no", grc_cavalry, mordr_mount),
                (team_give_order, ":team_no", grc_reinforcement_cavalry, mordr_mount),
                
                (team_set_slot, ":team_no", slot_team_battle_phase, stbp_deploy),
            (try_end),
        ]),
    
    # script_team_set_division_slots_for_formation
    # input:
    #   arg1: team_no
    #   arg2: formation
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
                (team_set_slot, ":team_no", slot_team_throw_division, grc_other),
                (team_set_slot, ":team_no", slot_team_archer_division, grc_archers),
                (team_set_slot, ":team_no", slot_team_shield_division, grc_infantry),
                (team_set_slot, ":team_no", slot_team_rest_division, grc_other),
                (team_set_slot, ":team_no", slot_team_pike_division, -1),
                (team_set_slot, ":team_no", slot_team_lance_division, -1),
            (else_try),
                (eq, ":formation", stf_mounted_skirmisher),
                (team_set_slot, ":team_no", slot_team_harcher_division, grc_other),
                (team_set_slot, ":team_no", slot_team_horse_division, grc_cavalry),
                (team_set_slot, ":team_no", slot_team_throw_division, grc_archers),
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
                (team_set_slot, ":team_no", slot_team_throw_division, grc_other),
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
                (team_set_slot, ":team_no", slot_team_lance_division, grc_other),
            (else_try),
                (eq, ":formation", stf_pikewall),
                (team_set_slot, ":team_no", slot_team_harcher_division, -1),
                (team_set_slot, ":team_no", slot_team_horse_division, grc_cavalry),
                (team_set_slot, ":team_no", slot_team_throw_division, -1),
                (team_set_slot, ":team_no", slot_team_archer_division, grc_archers),
                (team_set_slot, ":team_no", slot_team_shield_division, -1),
                (team_set_slot, ":team_no", slot_team_rest_division, grc_infantry),
                (team_set_slot, ":team_no", slot_team_pike_division, grc_other),
                (team_set_slot, ":team_no", slot_team_lance_division, -1),
            (else_try),
                (eq, ":formation", stf_archers),
                (team_set_slot, ":team_no", slot_team_harcher_division, grc_cavalry),
                (team_set_slot, ":team_no", slot_team_horse_division, grc_cavalry),
                (team_set_slot, ":team_no", slot_team_throw_division, grc_other),
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

    # script_init_agent
    # input:
    #   arg1: agent_no
    # output: none
    ("init_agent",
        [
            (store_script_param, ":agent_no", 1),
            (agent_set_slot, ":agent_no", slot_agent_is_reinforcement, 1),
            (agent_set_slot, ":agent_no", slot_agent_target_entry_point, 0),
            (agent_set_slot, ":agent_no", slot_agent_is_in_scripted_mode, 0),
        ]),

    # script_process_battle_ais
    # input: none
    # output: none
    ("process_battle_ais",
        [
            (try_for_range, ":cur_team", 0, 4),
                (neq, ":cur_team", "$g_player_team"),
                (call_script, "script_process_team_battle_ai", ":cur_team"),
            (try_end),
        ]),
    
    # script_process_team_battle_ai
    # input:
    #   arg1: team_no
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
                (team_give_order, ":team_no", grc_reinforcement_archer, mordr_advance),
                (team_get_order_position, pos1, ":team_no", grc_reinforcement_archer),
            (else_try),
                (eq, ":battle_phase", stbp_engage),
                (neq, ":tactic", stt_defend),
                (team_give_order, ":team_no", grc_reinforcement_archer, mordr_advance),
                (team_get_order_position, pos1, ":team_no", grc_reinforcement_archer),
            (else_try),
                # (eq, ":battle_phase", stbp_combat),
                (team_get_order_position, pos1, ":team_no", grc_reinforcement_archer),
            (try_end),
            (position_set_z_to_ground_level, pos1), 
            
            (try_begin),
                (neq, ":battle_phase", stbp_combat),
                
                (team_give_order, ":team_no", grc_reinforcement_infantry, mordr_hold),
                (team_give_order, ":team_no", grc_reinforcement_archer, mordr_hold),
                (team_give_order, ":team_no", grc_reinforcement_cavalry, mordr_hold),
                (team_set_order_position, ":team_no", grc_reinforcement_infantry, pos1),
                (team_set_order_position, ":team_no", grc_reinforcement_archer, pos1),
                (team_set_order_position, ":team_no", grc_reinforcement_cavalry, pos1),
                
                (call_script, "script_apply_battle_reinforcements_formation_to_team", ":formation", ":team_no"),
            (try_end),
            
            (try_begin),
                (eq, ":battle_phase", stbp_deploy),

                # We make sure that agents are present in main army before going to next phase
                # Prevents divisions retreating when no reinforcements are coming
                (assign, ":end", 0),
                (try_for_agents, ":agent_no"),
                    (neq, ":end", 1),
                    (agent_is_alive, ":agent_no"),
                    (agent_is_human, ":agent_no"),
                    (agent_get_team, ":agent_team", ":agent_no"),
                    (eq, ":agent_team", ":team_no"),
                    (agent_get_division, ":agent_division", ":agent_no"),
                    (is_between, ":agent_division", grc_reinforcement_infantry, grc_reinforcement_cavalry + 1),
                    (assign, ":end", 1),
                (try_end),

                (try_begin),
                    (eq, ":end", 1),
                    (team_give_order, ":team_no", grc_reinforcement_archer, mordr_hold_fire),
                    (team_set_slot, ":team_no", slot_team_battle_phase, stbp_advance),
                (try_end),
            (else_try),
                (eq, ":battle_phase", stbp_advance),
                (call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team_no"),
                (try_begin),
                    (this_or_next|lt, reg0, 10000),
                    (neq, ":tactic", stt_short_engage),
                    (lt, reg0, 12000),
                    (team_give_order, ":team_no", grc_reinforcement_archer, mordr_fire_at_will),
                    (team_set_slot, ":team_no", slot_team_battle_phase, stbp_engage),
                (try_end),
            (else_try),
                (eq, ":battle_phase", stbp_engage),
                (call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team_no"),
                (try_begin),
                    (this_or_next|lt, reg0, 6000),
                    (neq, ":tactic", stt_short_engage),
                    (lt, reg0, 7000),
                    (try_for_range, ":division", grc_infantry, grc_reinforcement_infantry),
                        (team_get_order_position, pos2, ":team_no", grc_reinforcement_archer),
                        (position_set_z_to_ground_level, pos2),
                        (team_give_order, ":team_no", ":division", mordr_hold),
                        (team_set_order_position, ":team_no", ":division", pos2),
                    (try_end),
                    (team_set_slot, ":team_no", slot_team_battle_phase, stbp_prepare),
                (try_end),
            (else_try),
                (eq, ":battle_phase", stbp_combat),
            (try_end),
            (try_begin),
                (team_get_slot, ":current_phase", ":team_no", slot_team_battle_phase),
                (ge, ":current_phase", stbp_prepare),
                (call_script, "script_process_team_battle_assault_ai", ":team_no"),
            (try_end),
                
            (set_show_messages, 1),
        ]),

    # script_process_team_battle_assault_ai
    # input:
    #   arg1: team_no
    # output: none
    ("process_team_battle_assault_ai",
        [
            (store_script_param, ":team_no", 1),

            (team_get_slot, ":formation", ":team_no", slot_team_formation),
            # (team_get_slot, ":tactic", ":team_no", slot_team_tactic),
            
            (team_get_slot, ":battle_phase", ":team_no", slot_team_battle_phase),

            (try_begin),
                (eq, ":battle_phase", stbp_prepare),

                (assign, ":percentage", 4),
                (store_normalized_team_count, ":team_size", ":team_no"),
                (try_begin),
                    (le, ":team_size", 4),
                    (assign, ":percentage", 10),
                (else_try),
                    (le, ":team_size", 8),
                    (assign, ":percentage", 5),
                (try_end),
                (try_begin),
                    (call_script, "script_cf_debug", debug_simple),
                    (assign, reg10, ":team_no"),
                    (assign, reg11, ":team_size"),
                    (display_message, "@Team {reg11} advances with team size : {reg10}"),
                (try_end),

                (store_sub, ":reinforcements_offset", grc_reinforcement_infantry, grc_infantry),
                (try_for_agents, ":cur_agent"),
                    (agent_is_alive, ":cur_agent"),
                    (agent_is_human, ":cur_agent"),
                    (agent_get_team, ":agent_team", ":cur_agent"),
                    (eq, ":agent_team", ":team_no"),
                    (agent_get_division , ":agent_division", ":cur_agent"),
                    (ge, ":agent_division", grc_reinforcement_infantry),
                    (store_random_in_range, ":rand", 0, 10),
                    (try_begin),
                        (lt, ":rand", ":percentage"),
                        (store_sub, ":new_division", ":agent_division", ":reinforcements_offset"),
                        (try_begin),
                            (gt, ":new_division", grc_cavalry),
                            (assign, ":new_division", grc_infantry),
                        (try_end),
                        (agent_set_division, ":cur_agent", ":new_division"),
                        (agent_set_slot, ":cur_agent", slot_agent_new_division, ":new_division"),
                        (agent_set_slot, ":cur_agent", slot_agent_is_reinforcement, 0),
                    (try_end),
                (try_end),

                (call_script, "script_apply_battle_formation_to_team", ":formation", ":team_no"),
                (team_set_slot, ":team_no", slot_team_battle_phase, stbp_assault),
            (else_try),
                (eq, ":battle_phase", stbp_assault),
                (team_get_movement_order, ":current_order", ":team_no", grc_infantry),

                (try_begin),
                    (eq, ":current_order", mordr_charge),
                    (assign, ":num_charging", 0),
                    (assign, ":has_reinforcements", 0),
                    (try_for_agents, ":cur_agent"),
                        (agent_is_alive, ":cur_agent"),
                        (agent_is_human, ":cur_agent"),
                        (agent_get_team, ":agent_team", ":cur_agent"),
                        (eq, ":agent_team", ":team_no"),
                        (agent_get_division , ":agent_division", ":cur_agent"),
                        (try_begin),
                            (lt, ":agent_division", grc_reinforcement_infantry),
                            (neq, ":agent_division", grc_archers),
                            (val_add, ":num_charging", 1),
                        (else_try),
                            (ge, ":agent_division", grc_reinforcement_infantry),
                            (assign, ":has_reinforcements", 1),
                        (try_end),
                    (try_end),
                    (try_begin),
                        (le, ":num_charging", 10),
                        (eq, ":has_reinforcements", 1),
                        (try_for_range, ":division", grc_infantry, grc_charge_group),
                            (team_get_order_position, pos2, ":team_no", grc_reinforcement_archer),
                            (position_set_z_to_ground_level, pos2),
                            (team_give_order, ":team_no", ":division", mordr_hold),
                            (team_set_order_position, ":team_no", ":division", pos2),
                        (try_end),
                        (team_set_slot, ":team_no", slot_team_battle_phase, stbp_prepare),
                    (try_end),
                (else_try),
                    (team_get_order_position, pos1, ":team_no", grc_infantry),
                    (position_set_z_to_ground_level, pos1),
                    (call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team_no"),
                    (try_begin),
                        (lt, reg0, 2800),
                        (team_give_order, ":team_no", grc_infantry, mordr_charge),
                        (team_give_order, ":team_no", grc_cavalry, mordr_charge),
                    (else_try),
                        (team_give_order, ":team_no", grc_archers, mordr_advance),
                        (call_script, "script_apply_battle_formation_to_team", ":formation", ":team_no"),
                    (try_end),
                (try_end),
            (else_try),
                (eq, ":battle_phase", stbp_combat),
            (try_end),
        ]),
    
    # script_apply_battle_formation_to_team
    # input:
    #   arg1: formation
    #   arg2: team_no
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
                
                (team_give_order, ":team_no", grc_other, mordr_fall_back),

                (team_give_order, ":team_no", grc_flank, mordr_fall_back),
            (else_try),
                (eq, ":formation", stf_archers),
                (team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
                (team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
                (team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
                (team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
                
                (team_give_order, ":team_no", grc_infantry, mordr_fall_back),
                
                (team_give_order, ":team_no", grc_other, mordr_fall_back),
                (team_give_order, ":team_no", grc_other, mordr_fall_back),

                (team_give_order, ":team_no", grc_flank, mordr_fall_back),
            (else_try),
                (eq, ":formation", stf_lance),
                (team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
                (team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
                (team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
                
                (team_give_order, ":team_no", grc_infantry, mordr_advance),
                
                (team_give_order, ":team_no", grc_other, mordr_fall_back),
                (team_give_order, ":team_no", grc_other, mordr_fall_back),

                (team_give_order, ":team_no", grc_flank, mordr_fall_back),
            (else_try),
                (team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
                (team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
                (team_give_order, ":team_no", grc_cavalry, mordr_fall_back),
                
                (team_give_order, ":team_no", grc_infantry, mordr_advance),
                (team_give_order, ":team_no", grc_infantry, mordr_advance),
                
                (team_give_order, ":team_no", grc_other, mordr_advance),

                (team_give_order, ":team_no", grc_flank, mordr_fall_back),
            (try_end),
        ]),
    # script_apply_battle_reinforcements_formation_to_team
    # input:
    #   arg1: formation
    #   arg2: team_no
    # output: none
    ("apply_battle_reinforcements_formation_to_team",
        [
            # (store_script_param, ":formation", 1),
            (store_script_param, ":team_no", 2),
            
            (team_give_order, ":team_no", grc_reinforcement_cavalry, mordr_fall_back),
            (team_give_order, ":team_no", grc_reinforcement_cavalry, mordr_fall_back),
            (team_give_order, ":team_no", grc_reinforcement_cavalry, mordr_fall_back),
            
            (team_give_order, ":team_no", grc_reinforcement_infantry, mordr_advance),
            (team_give_order, ":team_no", grc_reinforcement_infantry, mordr_advance),
        ]),
    
    # script_team_get_average_position_of_enemies
    # input: 
    #   arg1: team_no
    # output: 
    #   pos0: average position
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
                
            (try_begin), #to avoid division by zeros in below division part.
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
    #   arg1: team_no
    #   pos1
    # output: 
    #   reg0: distance in cms
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
    
    # script_party_process_ressources
        # input: 
        #   arg1: party_no
        # output: none
    ("party_process_ressources",
        [
            (store_script_param, ":party_no", 1),
            
            (party_get_slot, ":population", ":party_no", slot_party_population),
            (party_get_slot, ":total_resources", ":party_no", slot_party_total_resources),
            (party_get_slot, ":party_type", ":party_no", slot_party_type),

            (try_begin),
                (eq, ":party_type", spt_village),
                (val_div, ":population", 2), # 50% of the village population works on ressources
            (else_try),
                (eq, ":party_type", spt_town),
                (val_div, ":population", 5), # 20% of town population works on ressources
            (else_try),
                (val_div, ":population", 3),
            (try_end),

            (assign, ":total_production", 0),
            (try_for_range, ":good", goods_begin, goods_end),
                (store_sub, ":offset", ":good", goods_begin),
                (store_add, ":production_slot", ":offset", slot_party_ressources_begin),

                (party_get_slot, ":raw_production", ":party_no", ":production_slot"),
                (gt, ":raw_production", 0),
                (val_mul, ":raw_production", ":population"),
                (store_div, ":num_prod", ":raw_production", ":total_resources"),
                (val_div, ":num_prod", 100),

                (try_begin),
                    (store_mod, ":rest", ":raw_production", ":total_resources"),
                    (store_random_in_range, ":rand", 0, ":total_resources"),
                    (gt, ":rest", ":rand"),
                    (val_add, ":num_prod", 1),
                (try_end),
                (store_add, ":last_production_slot", ":offset", slot_party_item_last_produced_begin),
                (party_set_slot, ":party_no", ":last_production_slot", ":num_prod"),

                (gt, ":num_prod", 0),
                (store_add, ":amount_slot", ":offset", slot_party_ressources_current_amount_begin),

                (assign, ":produced", ":num_prod"),

                (try_begin),
                    (gt, ":produced", 0),
                    (try_begin),
                        (call_script, "script_cf_debug", debug_economy),
                        (eq, ":party_type", spt_town),
                        (str_store_party_name, s10, ":party_no"),
                        (str_store_item_name, s11, ":good"),
                        (assign, reg10, ":produced"),
                        (display_message, "@{s10} : produced {reg10} {s11}."),
                    (try_end),

                    (party_get_slot, ":current_amount", ":party_no", ":amount_slot"),
                    (val_add, ":current_amount", ":produced"),
                    (party_set_slot, ":party_no", ":amount_slot", ":current_amount"),

                    (val_add, ":total_production", ":produced"),
                (try_end),
            (try_end),
            (try_begin),
                (call_script, "script_cf_debug", debug_economy|debug_trade),
                (is_between, ":party_no", towns_begin, towns_end),
                (str_store_party_name, s10, ":party_no"),
                (assign, reg10, ":total_production"),
                (display_message, "@{s10} : produced {reg10} resources in total."),
            (try_end),
        ]),

    # script_party_process_production
        # input:
        #   arg1: party_no
        # output: none
    ("party_process_production",
        [
            # (store_script_param, ":party_no", 1),

            # (party_get_slot, ":population", ":party_no", slot_party_population),
            # (party_get_slot, ":total_resources", ":party_no", slot_party_number_resources),
            # (party_get_slot, ":party_type", ":party_no"),
        ]),

    # script_party_process_consumption
        # input:
        #   arg1: party_no
        # output: none
    ("party_process_consumption",
        [
            (store_script_param, ":party_no", 1),

            (assign, ":total_population", 0),

            (party_get_slot, ":center_population", ":party_no", slot_party_population),
            (party_get_slot, ":center_population_noble", ":party_no", slot_party_population_noble),
            (party_get_slot, ":center_population_artisan", ":party_no", slot_party_population_artisan),
            (party_get_slot, ":center_population_slave", ":party_no", slot_party_population_slave),

            (val_add, ":total_population", ":center_population"),
            (val_add, ":total_population", ":center_population_noble"),
            (val_add, ":total_population", ":center_population_artisan"),
            (val_add, ":total_population", ":center_population_slave"),

            (try_for_range, ":item", goods_begin, goods_end),
                (store_sub, ":offset", ":item", goods_begin),

                (store_add, ":amount_slot", ":offset", slot_party_ressources_current_amount_begin),
                (store_add, ":consumption_slot", ":offset", slot_party_item_consumed_begin),

                (item_get_slot, ":consumption_base", ":item", slot_item_consumption_base),
                (item_get_slot, ":consumption_ratio", ":item", slot_item_consumption_ratio),
                (assign, ":pop_consumption", 0),
                (assign, ":surplus_consumption", 0),
                (try_begin),
                    (gt, ":consumption_base", 0),
                    (store_mul, ":consumption_power", ":total_population", ":consumption_base"),
                    (store_div, ":pop_consumption", ":consumption_power", consumption_ratio_base),
                    (store_mod, ":consumption_rest", ":consumption_power", consumption_ratio_base),
                    (try_begin),
                        (gt, ":consumption_rest", 0),
                        (store_random_in_range, ":rand", 0, consumption_ratio_base),
                        (lt, ":rand", ":consumption_rest"),
                        (val_add, ":pop_consumption", 1),
                    (try_end),
                (try_end),
                (try_begin),
                    (gt, ":consumption_ratio", 0),

                    (party_get_slot, ":current_amount", ":party_no", ":amount_slot"),
                    (store_mul, ":surplus_consumption", ":current_amount", ":consumption_ratio"),
                    (val_div, ":surplus_consumption", 100),
                (try_end),

                (store_add, ":consumption", ":pop_consumption", ":surplus_consumption"),

                (try_begin),
                    (gt, ":consumption", 0),

                    (party_get_slot, ":amount", ":party_no", ":amount_slot"),
                    (val_min, ":consumption", ":amount"),
                    (try_begin),
                        (gt, ":consumption", 0),

                        (val_sub, ":amount", ":consumption"),
                        (val_max, ":amount", 0),
                        (party_set_slot, ":party_no", ":amount_slot", ":amount"),
                    (try_end),
                    (party_set_slot, ":party_no", ":consumption_slot", ":pop_consumption"),
                    (try_begin),
                        (call_script, "script_cf_debug", debug_economy),
                        (is_between, ":party_no", towns_begin, towns_end),
                        (str_store_party_name, s10, ":party_no"),
                        (str_store_item_name, s11, ":item"),
                        (assign, reg10, ":consumption"),
                        (assign, reg11, ":pop_consumption"),
                        (assign, reg12, ":surplus_consumption"),
                        (display_message, "@{s10} consummed {reg10} {s11} ({reg11}+{reg12})"),
                    (try_end),
                (try_end),
            (try_end),
        ]),
    
    # script_party_process_population
        # input: 
        #   arg1: party_no
        # output: none
    ("party_process_population",
        [
            (store_script_param, ":party_no", 1),
            
            (party_get_slot, ":party_type", ":party_no", slot_party_type),
            
            (party_get_slot, ":serf_population", ":party_no", slot_party_population),
            (party_get_slot, ":artisan_population", ":party_no", slot_party_population_artisan),
            (party_get_slot, ":noble_population", ":party_no", slot_party_population_noble),
            (party_get_slot, ":slave_population", ":party_no", slot_party_population_slave),

            (store_add, ":party_population", ":serf_population", ":artisan_population"),
            (val_add, ":party_population", ":noble_population"),
            # Slaves do not count towards max center population

            (call_script, "script_get_max_population", ":party_no"),
            (assign, ":max_population", reg0),
            (store_mul, ":offset", ":party_population", 100),
            (val_div, ":offset", ":max_population"),
            (val_sub, ":offset", 50), # We consider 50% to be the baseline population with highest growth
            (val_abs, ":offset", ":offset"),
            (store_sub, ":offset", 100, ":offset"),
            (val_abs, ":offset", ":offset"),
            
            (try_begin),
                (eq, ":party_type", spt_village),
                (assign, ":noble_growth", population_growth_village_noble),
                (assign, ":artisan_growth", population_growth_village_artisan),
                (assign, ":serf_growth", population_growth_village_serf),
                (assign, ":slave_growth", population_growth_village_slave),
                (assign, ":base_population_growth", 10),
            (else_try),
                (eq, ":party_type", spt_castle),
                (assign, ":noble_growth", population_growth_castle_noble),
                (assign, ":artisan_growth", population_growth_castle_artisan),
                (assign, ":serf_growth", population_growth_castle_serf),
                (assign, ":slave_growth", population_growth_castle_slave),
                (assign, ":base_population_growth", 5),
            (else_try),
                (assign, ":noble_growth", population_growth_town_noble),
                (assign, ":artisan_growth", population_growth_town_artisan),
                (assign, ":serf_growth", population_growth_town_serf),
                (assign, ":slave_growth", population_growth_town_slave),
                (assign, ":base_population_growth", 15),
            (try_end),
            (assign, ":noble_threshold", ":noble_growth"),
            (store_add, ":artisan_threshold", ":noble_threshold", ":artisan_growth"),
            (store_add, ":serf_threshold", ":artisan_threshold", ":serf_growth"),
            (store_add, ":slave_threshold", ":serf_threshold", ":slave_growth"),

            (store_mul, ":population_growth", ":base_population_growth", ":offset"),
            (val_div, ":population_growth", 100),
            (store_random_in_range, ":bonus_population_growth", 0, 5),

            (assign, ":new_noble", 0),
            (assign, ":new_artisan", 0),
            (assign, ":new_serf", 0),
            (assign, ":new_slave", 0),
            (store_add, ":num_tries", ":population_growth", ":bonus_population_growth"),
            (try_for_range, ":unused", 0, ":num_tries"),
                (store_random_in_range, ":value", 0, ":slave_threshold"),
                (try_begin),
                    (lt, ":value", ":noble_threshold"),
                    (val_add, ":new_noble", 1),
                (else_try),
                    (lt, ":value", ":artisan_threshold"),
                    (val_add, ":new_artisan", 1),
                (else_try),
                    (lt, ":value", ":serf_threshold"),
                    (val_add, ":new_serf", 1),
                (try_end),
            (try_end),

            (try_begin),
                (call_script, "script_cf_debug", debug_economy),
                (str_store_party_name, s10, ":party_no"),
                (assign, reg10, ":noble_population"),
                (assign, reg11, ":artisan_population"),
                (assign, reg12, ":serf_population"),
                (assign, reg13, ":slave_population"),
                (assign, reg14, ":new_noble"),
                (assign, reg15, ":new_artisan"),
                (assign, reg16, ":new_serf"),
                (assign, reg17, ":new_slave"),
                (display_message, "@{s10} pop: nobles {reg10}+{reg14}, artisan {reg11}+{reg15}, serf {reg12}+{reg16}, slave {reg13}+{reg17}"),
            (try_end),

            (val_add, ":noble_population", ":new_noble"),
            (val_add, ":artisan_population", ":new_artisan"),
            (val_add, ":serf_population", ":new_serf"),
            (val_add, ":slave_population", ":new_slave"),

            (party_set_slot, ":party_no", slot_party_population, ":serf_population"),
            (party_set_slot, ":party_no", slot_party_population_noble, ":noble_population"),
            (party_set_slot, ":party_no", slot_party_population_artisan, ":artisan_population"),
            (party_set_slot, ":party_no", slot_party_population_slave, ":slave_population"),
            
        ]),
    
    # script_get_max_population
        # input:
        #   arg1: party_no
        # output:
        #   reg0: max_population
    ("get_max_population",
        [
            (store_script_param, ":party_no", 1),
            
            (party_get_slot, ":max", ":party_no", slot_party_population_max),
            
            (assign, reg0, ":max"),
        ]),

    # script_party_get_expected_taxes
        # input:
        #   arg1: party_no
        # output:
        #   reg0: expected_taxes
    ("party_get_expected_taxes",
        [
            (store_script_param, ":party_no", 1),

            (party_get_slot, ":population_serf", ":party_no", slot_party_population),
            (party_get_slot, ":population_noble", ":party_no", slot_party_population_noble),
            (party_get_slot, ":population_artisan", ":party_no", slot_party_population_artisan),
            # (party_get_slot, ":population_slave", ":party_no", slot_party_population_slave),
            
            (store_mul, ":taxes_serf", ":population_serf", taxes_serf_amount),
            (store_mul, ":taxes_artisan", ":population_artisan", taxes_artisan_amount),
            (store_mul, ":taxes_noble", ":population_noble", taxes_noble_amount),

            (store_add, ":taxes", ":taxes_serf", ":taxes_artisan"),
            (val_add, ":taxes", ":taxes_noble"),

            (party_get_slot, ":party_type", ":party_no", slot_party_type),
            (assign, ":mult", 120),
            (try_begin),
                (eq, ":party_type", spt_village),
                (assign, ":mult", 60),
            (else_try),
                (eq, ":party_type", spt_town),
                (assign, ":mult", 60),
            (try_end),

            (val_mul, ":taxes", ":mult"),
            (val_div, ":taxes", 10),

            (val_div, ":taxes", 12), # We are doing taxes in a monthly basis

            (assign, reg0, ":taxes"),
        ]),
    
    # script_party_process_taxes
        # input:
        #   arg1: party_no
        # output: none
    ("party_process_taxes",
        [
            (store_script_param, ":party_no", 1),

            (call_script, "script_party_get_expected_taxes", ":party_no"),
            (assign, ":taxes", reg0),

            (assign, ":member_tax", 0),
            (assign, ":vassal_tax", 0),

            (store_faction_of_party, ":party_faction", ":party_no"),
            (try_begin),
                (gt, ":party_faction", 0),
                (faction_get_slot, ":member_tax_rate", ":party_faction", slot_faction_member_tax_rate),
                (faction_get_slot, ":vassal_tax_rate", ":party_faction", slot_faction_vassal_tax_rate),

                (try_begin),
                    (gt, ":member_tax_rate", 0),

                    (faction_get_slot, ":faction_leader", ":party_faction", slot_faction_leader),
                    (ge, ":faction_leader", 0),

                    (store_mul, ":member_tax", ":member_tax_rate", ":taxes"),
                    (val_div, ":member_tax", 100),

                    (call_script, "script_troop_add_accumulated_taxes", ":faction_leader", ":member_tax", tax_type_member, 1),

                    (store_mul, ":member_tax_pay", ":member_tax", -1),
                    (call_script, "script_party_add_accumulated_taxes", ":party_no", ":member_tax_pay", tax_type_member_pay),

                    (try_begin),
                        (call_script, "script_cf_debug", debug_economy),
                        (str_store_party_name, s10, ":party_no"),
                        (str_store_troop_name, s11, ":faction_leader"),
                        (assign, reg10, ":member_tax"),
                        (display_message, "@{s10} member taxes: {reg10} to {s11}"),
                    (try_end),
                (try_end),
                (try_begin),
                    (gt, ":vassal_tax_rate", 0),

                    (party_get_slot, ":party_leader", ":party_no", slot_party_leader),
                    (ge, ":party_leader", 0),
                    (troop_get_slot, ":party_leader_lord", ":party_leader", slot_troop_vassal_of),
                    (ge, ":party_leader_lord", 0),

                    (store_mul, ":vassal_tax", ":vassal_tax_rate", ":taxes"),
                    (val_div, ":vassal_tax", 100),

                    (call_script, "script_troop_add_accumulated_taxes", ":party_leader_lord", ":vassal_tax", tax_type_vassal, 1),

                    (store_mul, ":vassal_tax_pay", ":member_tax", -1),
                    (call_script, "script_party_add_accumulated_taxes", ":party_no", ":vassal_tax_pay", tax_type_vassal_pay),

                    (try_begin),
                        (call_script, "script_cf_debug", debug_economy),
                        (str_store_troop_name, s10, ":party_leader"),
                        (str_store_troop_name, s11, ":party_leader_lord"),
                        (assign, reg10, ":vassal_tax"),
                        (display_message, "@{s10} vassal taxes: {reg10} to {s11}"),
                    (try_end),
                (try_end),
            (try_end),


            (party_get_slot, ":party_type", ":party_no", slot_party_type),
            (try_begin),
                (eq, ":party_type", spt_village),
                (party_get_slot, ":linked_party", ":party_no", slot_party_linked_party),
                (is_between, ":linked_party", centers_begin, centers_end),
                (store_mul, ":linked_taxes", 3),
                (val_div, ":linked_taxes", 10),
                # TODO: separate protection taxes
                (val_sub, ":taxes", ":linked_taxes"),

                # TODO: remove instant teleportation of money
                # (party_get_slot, ":linked_center_wealth", ":linked_party", slot_party_wealth),
                # (val_add, ":linked_center_wealth", ":linked_taxes"),
                # (party_set_slot, ":linked_party", slot_party_wealth, ":linked_center_wealth"),

                (call_script, "script_party_add_accumulated_taxes", ":linked_party", ":linked_taxes", tax_type_protection),

            (try_end),

            (try_begin),
                (call_script, "script_cf_debug", debug_economy),
                (str_store_party_name, s10, ":party_no"),
                (assign, reg10, ":taxes"),
                (display_message, "@{s10} taxes: {reg10}"),
            (try_end),
            
            (val_sub, ":taxes", ":member_tax"),
            (val_sub, ":taxes", ":vassal_tax"),
            (call_script, "script_party_add_accumulated_taxes", ":party_no", ":taxes", tax_type_population),
        ]),

    # script_troop_add_accumulated_taxes
        # input:
        #   arg1: troop_no
        #   arg2: amount
        #   arg3: tax_type
        #   arg4: direct - do we need to add this amount to the troop's wealth
        # output: none
    ("troop_add_accumulated_taxes",
        [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":amount", 2),
            (store_script_param, ":tax_type", 3),
            (store_script_param, ":direct", 4),

            (try_begin),
                (call_script, "script_cf_debug", debug_economy|debug_ai),
                (str_store_troop_name, s10, ":troop_no"),
                (assign, reg10, ":amount"),
                (assign, reg11, ":tax_type"),
                (assign, reg12, ":direct"),
                (display_message, "@Adding {reg10} denars for {s10} (type {reg11}, direct: {reg12})"),
            (try_end),

            (troop_get_slot, ":accumulated_taxes", ":troop_no", slot_troop_accumulated_taxes),
            (val_add, ":accumulated_taxes", ":amount"),
            (troop_set_slot, ":troop_no", slot_troop_accumulated_taxes, ":accumulated_taxes"),

            (troop_get_slot, ":budget_party", ":troop_no", slot_troop_budget_reserved_party),
            (troop_get_slot, ":budget_other", ":troop_no", slot_troop_budget_reserved_other),

            (call_script, "script_troop_get_allocated_budget", ":troop_no", ":amount"),
            (assign, ":budget_party_ratio", reg0),
            (assign, ":budget_other_ratio", reg1),

            (store_mul, ":budget_party_new", ":amount", ":budget_party_ratio"),
            (val_div, ":budget_party_new", 100),

            (store_mul, ":budget_other_new", ":amount", ":budget_other_ratio"),
            (val_div, ":budget_other_new", 100),

            (val_add, ":budget_party", ":budget_party_new"),
            (val_add, ":budget_other", ":budget_other_new"),

            (troop_set_slot, ":troop_no", slot_troop_budget_reserved_party, ":budget_party"),
            (troop_set_slot, ":troop_no", slot_troop_budget_reserved_other, ":budget_other"),

            (try_begin),
                (eq, ":tax_type", tax_type_vassal),
                (troop_get_slot, ":budget", ":troop_no", slot_party_budget_vassal_taxes),
                (val_add, ":budget", ":amount"),
                (troop_set_slot, ":troop_no", slot_party_budget_vassal_taxes, ":budget"),
            (else_try),
                (eq, ":tax_type", tax_type_member),
                (troop_get_slot, ":budget", ":troop_no", slot_party_budget_faction_member_taxes),
                (val_add, ":budget", ":amount"),
                (troop_set_slot, ":troop_no", slot_party_budget_faction_member_taxes, ":budget"),
            (try_end),

            (try_begin),
                (eq, ":direct", 1),
                (call_script, "script_troop_change_wealth", ":troop_no", ":amount"),
            (end_try),
        ]),

    # script_party_add_accumulated_taxes
        # input:
        #   arg1: party_no
        #   arg2: amount
        #   arg3: tax_type
        # output: none
    ("party_add_accumulated_taxes",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":amount", 2),
            (store_script_param, ":tax_type", 3),

            (try_begin),
                (call_script, "script_cf_debug", debug_economy|debug_ai),
                (str_store_party_name, s10, ":party_no"),
                (assign, reg10, ":amount"),
                (assign, reg11, ":tax_type"),
                (display_message, "@Adding {reg10} denars for {s10} (type {reg11})"),
            (try_end),

            (party_get_slot, ":accumulated_taxes", ":party_no", slot_party_accumulated_taxes),
            (val_add, ":accumulated_taxes", ":amount"),
            (party_set_slot, ":party_no", slot_party_accumulated_taxes, ":accumulated_taxes"),

            (party_get_slot, ":budget_party", ":party_no", slot_party_budget_reserved_party),
            (party_get_slot, ":budget_auxiliaries", ":party_no", slot_party_budget_reserved_auxiliaries),
            (party_get_slot, ":budget_expenses", ":party_no", slot_party_budget_reserved_expenses),
            (party_get_slot, ":budget_other", ":party_no", slot_party_budget_reserved_other),

            (call_script, "script_party_get_allocated_budget", ":party_no", ":amount"),
            (assign, ":budget_party_ratio", reg0),
            (assign, ":budget_auxiliaries_ratio", reg1),
            (assign, ":budget_expenses_ratio", reg2),
            (assign, ":budget_other_ratio", reg3),

            (store_mul, ":budget_party_new", ":amount", ":budget_party_ratio"),
            (val_div, ":budget_party_new", 100),

            (store_mul, ":budget_auxiliaries_new", ":amount", ":budget_auxiliaries_ratio"),
            (val_div, ":budget_auxiliaries_new", 100),

            (store_mul, ":budget_expenses_new", ":amount", ":budget_expenses_ratio"),
            (val_div, ":budget_expenses_new", 100),

            (store_mul, ":budget_other_new", ":amount", ":budget_other_ratio"),
            (val_div, ":budget_other_new", 100),

            (val_add, ":budget_party", ":budget_party_new"),
            (val_add, ":budget_auxiliaries", ":budget_auxiliaries_new"),
            (val_add, ":budget_expenses", ":budget_expenses_new"),
            (val_add, ":budget_other", ":budget_other_new"),

            (party_set_slot, ":party_no", slot_party_budget_reserved_party, ":budget_party"),
            (party_set_slot, ":party_no", slot_party_budget_reserved_auxiliaries, ":budget_auxiliaries"),
            (party_set_slot, ":party_no", slot_party_budget_reserved_expenses, ":budget_expenses"),
            (party_set_slot, ":party_no", slot_party_budget_reserved_other, ":budget_other"),

            (party_get_slot, ":leader", ":party_no", slot_party_leader),
            (try_begin),
                (ge, ":leader", 0),
                (call_script, "script_troop_add_accumulated_taxes", ":leader", ":budget_other_new", ":tax_type", 0),
            (try_end),
            
            (party_get_slot, ":wealth", ":party_no", slot_party_wealth),
            (val_add, ":wealth", ":amount"),
            (party_set_slot, ":party_no", slot_party_wealth, ":wealth"),

            (try_begin),
                (store_add, ":budget_slot", ":tax_type", slot_party_buget_taxes_begin),
                (is_between, ":budget_slot", slot_party_buget_taxes_begin, slot_party_buget_taxes_end),

                (party_get_slot, ":budget", ":party_no", ":budget_slot"),
                (val_add, ":budget", ":amount"),
                (party_set_slot, ":party_no", ":budget_slot", ":budget"),
            (try_end),
        ]),

    # script_troop_get_allocated_budget
        # input:
        #   arg1: troop_no
        #   arg2: amount
        # output:
        #   reg0: ratio_troop_party_wage
        #   reg1: ratio_other
    ("troop_get_allocated_budget",
        [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":amount", 2),

            (assign, ":at_war", 0),
            (try_begin),
                (store_troop_faction, ":troop_faction", ":troop_no"),
                (gt, ":troop_faction", 0),
                (faction_get_slot, ":at_war", ":troop_faction", slot_faction_is_at_war),
            (try_end),

            (assign, ":min_value", 60),
            (assign, ":max_value", 150),

            (troop_get_slot, ":current_debt", ":troop_no", slot_troop_budget_perceived_debt),
            (store_div, ":debt_value", ":current_debt", 100),
            (try_begin),
                (gt, ":debt_value", ":amount"),
                (store_div, ":penalty", ":current_debt", ":amount"),
                (val_min, ":penalty", 300),
                (val_max, ":penalty", 100),

                (val_mul, ":max_value", 100),
                (val_div, ":max_value", ":penalty"),

                (val_sub, ":penalty", 100),
                (val_div, ":penalty", 10),
                (val_sub, ":min_value", ":penalty"),

                (try_begin),
                    (call_script, "script_cf_debug", debug_economy),
                    (str_store_troop_name, s10, ":troop_no"),
                    (assign, reg10, ":penalty"),
                    (display_message, "@{s10} in debt, increasing party size penalty -{reg10}%"),
                (try_end),
            (try_end),

            (assign, ":ratio_party", 60),
            (try_begin),
                (eq, ":at_war", 0),
                (assign, ":ratio_party", ":min_value"),
            (else_try),
                (assign, ":ratio_party", ":max_value"),
            (try_end),

            (assign, ":ratio_other", 100),
            (val_sub, ":ratio_other", ":ratio_party"),
            (val_max, ":ratio_other", 0),

            (assign, reg0, ":ratio_party"),
            (assign, reg1, ":ratio_other"),
        ]),

    # script_party_get_allocated_budget
        # input:
        #   arg1: party_no
        #   arg2: amount
        # output:
        #   reg0: ratio_party_wage
        #   reg1: ratio_auxiliary_parties
        #   reg2: ratio_spendings (buildings, armor upgrades...)
        #   reg3: ratio_other
    ("party_get_allocated_budget",
        [
            (store_script_param, ":party_no", 1),
            # (store_script_param, ":amount", 2),

            (party_get_slot, ":party_type", ":party_no", slot_party_type),

            (assign, ":at_war", 0),
            (store_faction_of_party, ":party_faction", ":party_no"),
            (try_begin),
                (gt, ":party_faction", 0),
                (faction_get_slot, ":at_war", ":party_faction", slot_faction_is_at_war),
            (try_end),

            (assign, ":ratio_party", 40),
            (assign, ":ratio_auxiliaries", 10),
            (assign, ":ratio_spendings", 25),
            (try_begin),
                (eq, ":at_war", 0),

                (try_begin),
                    (eq, ":party_type", spt_town),
                (else_try),
                    (eq, ":party_type", spt_castle),
                    (assign, ":ratio_spendings", 20),
                (else_try),
                    (eq, ":party_type", spt_village),
                    (assign, ":ratio_party", 20),
                    (assign, ":ratio_auxiliaries", 0),
                    (assign, ":ratio_spendings", 10),
                (try_end),
            (else_try),
                (try_begin),
                    (eq, ":party_type", spt_town),
                    (assign, ":ratio_party", 50),
                    (assign, ":ratio_auxiliaries", 15),
                    (assign, ":ratio_spendings", 0),
                (else_try),
                    (eq, ":party_type", spt_castle),
                    (assign, ":ratio_party", 50),
                    (assign, ":ratio_auxiliaries", 15),
                    (assign, ":ratio_spendings", 0),
                (else_try),
                    (eq, ":party_type", spt_village),
                    (assign, ":ratio_party", 20),
                    (assign, ":ratio_auxiliaries", 0),
                    (assign, ":ratio_spendings", 0),
                (try_end),
            (try_end),

            (assign, ":ratio_other", 100),
            (val_sub, ":ratio_other", ":ratio_party"),
            (val_sub, ":ratio_other", ":ratio_auxiliaries"),
            (val_sub, ":ratio_other", ":ratio_spendings"),
            (val_max, ":ratio_other", 0),

            (assign, reg0, ":ratio_party"),
            (assign, reg1, ":ratio_auxiliaries"),
            (assign, reg2, ":ratio_spendings"),
            (assign, reg3, ":ratio_other"),
        ]),

    # script_troop_process_ideal_party_wages
        # input:
        #   arg1: troop_no
        # output: none
    ("troop_process_ideal_party_wages",
        [
            (store_script_param, ":troop_no", 1),

            (troop_get_slot, ":wanted_wages", ":troop_no", slot_troop_budget_reserved_party),
            (troop_get_slot, ":old_wanted_wages", ":troop_no", slot_troop_wanted_party_wages),

            (try_begin),
                (le, ":old_wanted_wages", 0),
                (assign, ":new_wanted_wages", ":wanted_wages"),
            (else_try),
                # We make an average of the last 10 months
                (store_mul, ":new_wanted_wages", ":old_wanted_wages", 9),
                (val_add, ":new_wanted_wages", ":wanted_wages"),
                (val_div, ":new_wanted_wages", 10),
            (try_end),

            (try_begin),
                (gt, ":old_wanted_wages", ":new_wanted_wages"),
                (val_sub, ":new_wanted_wages", 1),
            (else_try),
                (lt, ":old_wanted_wages", ":new_wanted_wages"),
                (val_add, ":new_wanted_wages", 1),
            (try_end),

            (try_begin),
                (call_script, "script_cf_debug", debug_economy),
                (str_store_troop_name, s10, ":troop_no"),
                (assign, reg10, ":wanted_wages"),
                (assign, reg11, ":old_wanted_wages"),
                (assign, reg12, ":new_wanted_wages"),
                # (display_message, "@{s10} wanted wages - current: {reg10}, old: {reg11}, new: {reg12}"),
            (try_end),

            (troop_set_slot, ":troop_no", slot_troop_wanted_party_wages, ":new_wanted_wages"),
        ]),

    # script_party_process_ideal_party_wages
        # input:
        #   arg1: party_no
        # output: none
    ("party_process_ideal_party_wages",
        [
            (store_script_param, ":party_no", 1),

            (party_get_slot, ":wanted_wages", ":party_no", slot_party_budget_reserved_party),

            (party_get_slot, ":old_wanted_wages", ":party_no", slot_party_wanted_party_wages),

            (try_begin),
                (le, ":old_wanted_wages", 0),
                (assign, ":new_wanted_wages", ":wanted_wages"),
            (else_try),
                # We make an average of the last 10 months
                (store_mul, ":new_wanted_wages", ":old_wanted_wages", 9),
                (val_add, ":new_wanted_wages", ":wanted_wages"),
                (val_div, ":new_wanted_wages", 10),
            (try_end),

            (try_begin),
                (gt, ":old_wanted_wages", ":new_wanted_wages"),
                (val_sub, ":new_wanted_wages", 1),
            (else_try),
                (lt, ":old_wanted_wages", ":new_wanted_wages"),
                (val_add, ":new_wanted_wages", 1),
            (try_end),

            (try_begin),
                (call_script, "script_cf_debug", debug_economy),
                (str_store_party_name, s10, ":party_no"),
                (assign, reg10, ":wanted_wages"),
                (assign, reg11, ":old_wanted_wages"),
                (assign, reg12, ":new_wanted_wages"),
                # (display_message, "@{s10} wanted wages - current: {reg10}, old: {reg11}, new: {reg12}"),
            (try_end),

            (party_set_slot, ":party_no", slot_party_wanted_party_wages, ":new_wanted_wages"),
        ]),
    
    # script_spawn_party_around_party
        # input: 
        #   arg1: party_no
        #   arg2: party_template_to_spawn
        # output:
        #   reg0: spawned_party_id
    ("spawn_party_around_party",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":party_template", 2),
            
            (set_spawn_radius, 2),
            
            (spawn_around_party, ":party_no", ":party_template"),
            (assign, ":spawned_party", reg0),

            (party_set_slot, ":spawned_party", slot_party_origin_center, ":party_no"),
            (party_set_slot, ":spawned_party", slot_party_leader, -1),
            
            (assign, reg0, ":spawned_party"),
        ]),
    
    # script_cf_faction_need_party_nearby_resources
        # input:
        #   arg1: faction_no
        #   arg2: party_no
        # output: none
    ("cf_faction_need_party_nearby_resources",
        [
            
        ]),
    
    # script_spawn_new_center_marker_with_party_resources
        # input:
        #   arg1: party_no
        # output: none
    ("spawn_new_center_marker_with_party_resources",
        [
            
        ]),

    # script_init_centers
        # input: none
        # output: none
    ("init_centers",
        [
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
        ]),
        
    # script_init_factions
        # input: none
        # output: none
    ("init_factions",
        [
            (faction_set_slot, "fac_faction_8", slot_faction_culture, "fac_culture_7"), # Mercenaries

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
            
            (faction_set_slot, "fac_kingdom_1", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_kingdom_1", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_kingdom_1", slot_faction_veteran_num_tries, 20),
            (faction_set_slot, "fac_kingdom_1", slot_faction_elite_num_tries, 60),
            (faction_set_slot, "fac_kingdom_1", slot_faction_noble_num_tries, 60),
            
            (faction_set_slot, "fac_kingdom_2", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_kingdom_2", slot_faction_common_num_tries, 75),
            (faction_set_slot, "fac_kingdom_2", slot_faction_veteran_num_tries, 50),
            (faction_set_slot, "fac_kingdom_2", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_kingdom_2", slot_faction_noble_num_tries, 0),
            
            (faction_set_slot, "fac_kingdom_3", slot_faction_peasant_num_tries, 25),
            (faction_set_slot, "fac_kingdom_3", slot_faction_common_num_tries, 50),
            (faction_set_slot, "fac_kingdom_3", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_kingdom_3", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_kingdom_3", slot_faction_noble_num_tries, 20),
            
            (faction_set_slot, "fac_kingdom_4", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_kingdom_4", slot_faction_common_num_tries, 20),
            (faction_set_slot, "fac_kingdom_4", slot_faction_veteran_num_tries, 80),
            (faction_set_slot, "fac_kingdom_4", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_kingdom_4", slot_faction_noble_num_tries, 40),
            
            (faction_set_slot, "fac_kingdom_5", slot_faction_peasant_num_tries, 40),
            (faction_set_slot, "fac_kingdom_5", slot_faction_common_num_tries, 50),
            (faction_set_slot, "fac_kingdom_5", slot_faction_veteran_num_tries, 50),
            (faction_set_slot, "fac_kingdom_5", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_kingdom_5", slot_faction_noble_num_tries, 0),
            
            (faction_set_slot, "fac_kingdom_6", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_kingdom_6", slot_faction_common_num_tries, 50),
            (faction_set_slot, "fac_kingdom_6", slot_faction_veteran_num_tries, 25),
            (faction_set_slot, "fac_kingdom_6", slot_faction_elite_num_tries, 20),
            (faction_set_slot, "fac_kingdom_6", slot_faction_noble_num_tries, 0),
            
            (faction_set_slot, "fac_small_kingdom_11", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_11", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_11", slot_faction_veteran_num_tries, 40),
            (faction_set_slot, "fac_small_kingdom_11", slot_faction_elite_num_tries, 100),
            (faction_set_slot, "fac_small_kingdom_11", slot_faction_noble_num_tries, 20),
            
            (faction_set_slot, "fac_small_kingdom_12", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_12", slot_faction_common_num_tries, 75),
            (faction_set_slot, "fac_small_kingdom_12", slot_faction_veteran_num_tries, 50),
            (faction_set_slot, "fac_small_kingdom_12", slot_faction_elite_num_tries, 20),
            (faction_set_slot, "fac_small_kingdom_12", slot_faction_noble_num_tries, 20),
            
            (faction_set_slot, "fac_small_kingdom_13", slot_faction_peasant_num_tries, 50),
            (faction_set_slot, "fac_small_kingdom_13", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_13", slot_faction_veteran_num_tries, 10),
            (faction_set_slot, "fac_small_kingdom_13", slot_faction_elite_num_tries, 80),
            (faction_set_slot, "fac_small_kingdom_13", slot_faction_noble_num_tries, 80),
            
            (faction_set_slot, "fac_small_kingdom_14", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_14", slot_faction_common_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_14", slot_faction_veteran_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_14", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_14", slot_faction_noble_num_tries, 20),
            
            (faction_set_slot, "fac_small_kingdom_15", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_15", slot_faction_common_num_tries, 80),
            (faction_set_slot, "fac_small_kingdom_15", slot_faction_veteran_num_tries, 40),
            (faction_set_slot, "fac_small_kingdom_15", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_15", slot_faction_noble_num_tries, 0),
            
            (faction_set_slot, "fac_small_kingdom_16", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_16", slot_faction_common_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_16", slot_faction_veteran_num_tries, 20),
            (faction_set_slot, "fac_small_kingdom_16", slot_faction_elite_num_tries, 20),
            (faction_set_slot, "fac_small_kingdom_16", slot_faction_noble_num_tries, 20),
            
            (faction_set_slot, "fac_small_kingdom_17", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_17", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_17", slot_faction_veteran_num_tries, 80),
            (faction_set_slot, "fac_small_kingdom_17", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_17", slot_faction_noble_num_tries, 80),
            
            (faction_set_slot, "fac_small_kingdom_21", slot_faction_peasant_num_tries, 50),
            (faction_set_slot, "fac_small_kingdom_21", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_21", slot_faction_veteran_num_tries, 50),
            (faction_set_slot, "fac_small_kingdom_21", slot_faction_elite_num_tries, 150),
            (faction_set_slot, "fac_small_kingdom_21", slot_faction_noble_num_tries, 50),
            
            (faction_set_slot, "fac_small_kingdom_22", slot_faction_peasant_num_tries, 40),
            (faction_set_slot, "fac_small_kingdom_22", slot_faction_common_num_tries, 80),
            (faction_set_slot, "fac_small_kingdom_22", slot_faction_veteran_num_tries, 80),
            (faction_set_slot, "fac_small_kingdom_22", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_22", slot_faction_noble_num_tries, 0),
            
            (faction_set_slot, "fac_small_kingdom_23", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_23", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_23", slot_faction_veteran_num_tries, 20),
            (faction_set_slot, "fac_small_kingdom_23", slot_faction_elite_num_tries, 40),
            (faction_set_slot, "fac_small_kingdom_23", slot_faction_noble_num_tries, 60),
            
            (faction_set_slot, "fac_small_kingdom_24", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_24", slot_faction_common_num_tries, 80),
            (faction_set_slot, "fac_small_kingdom_24", slot_faction_veteran_num_tries, 20),
            (faction_set_slot, "fac_small_kingdom_24", slot_faction_elite_num_tries, 40),
            (faction_set_slot, "fac_small_kingdom_24", slot_faction_noble_num_tries, 0),
            
            (faction_set_slot, "fac_small_kingdom_25", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_25", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_25", slot_faction_veteran_num_tries, 20),
            (faction_set_slot, "fac_small_kingdom_25", slot_faction_elite_num_tries, 80),
            (faction_set_slot, "fac_small_kingdom_25", slot_faction_noble_num_tries, 40),
            
            (faction_set_slot, "fac_small_kingdom_31", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_31", slot_faction_common_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_31", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_31", slot_faction_elite_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_31", slot_faction_noble_num_tries, 20),
            
            (faction_set_slot, "fac_small_kingdom_32", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_32", slot_faction_common_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_32", slot_faction_veteran_num_tries, 80),
            (faction_set_slot, "fac_small_kingdom_32", slot_faction_elite_num_tries, 20),
            (faction_set_slot, "fac_small_kingdom_32", slot_faction_noble_num_tries, 0),
            
            (faction_set_slot, "fac_small_kingdom_33", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_33", slot_faction_common_num_tries, 80),
            (faction_set_slot, "fac_small_kingdom_33", slot_faction_veteran_num_tries, 80),
            (faction_set_slot, "fac_small_kingdom_33", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_33", slot_faction_noble_num_tries, 0),
            
            (faction_set_slot, "fac_small_kingdom_34", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_34", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_34", slot_faction_veteran_num_tries, 20),
            (faction_set_slot, "fac_small_kingdom_34", slot_faction_elite_num_tries, 100),
            (faction_set_slot, "fac_small_kingdom_34", slot_faction_noble_num_tries, 40),
            
            (faction_set_slot, "fac_small_kingdom_35", slot_faction_peasant_num_tries, 30),
            (faction_set_slot, "fac_small_kingdom_35", slot_faction_common_num_tries, 10),
            (faction_set_slot, "fac_small_kingdom_35", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_35", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_35", slot_faction_noble_num_tries, 40),
            
            (faction_set_slot, "fac_small_kingdom_36", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_36", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_36", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_36", slot_faction_elite_num_tries, 80),
            (faction_set_slot, "fac_small_kingdom_36", slot_faction_noble_num_tries, 0),
            
            (faction_set_slot, "fac_small_kingdom_41", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_41", slot_faction_common_num_tries, 50),
            (faction_set_slot, "fac_small_kingdom_41", slot_faction_veteran_num_tries, 70),
            (faction_set_slot, "fac_small_kingdom_41", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_41", slot_faction_noble_num_tries, 0),
            
            (faction_set_slot, "fac_small_kingdom_42", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_42", slot_faction_common_num_tries, 40),
            (faction_set_slot, "fac_small_kingdom_42", slot_faction_veteran_num_tries, 50),
            (faction_set_slot, "fac_small_kingdom_42", slot_faction_elite_num_tries, 10),
            (faction_set_slot, "fac_small_kingdom_42", slot_faction_noble_num_tries, 0),
            
            (faction_set_slot, "fac_small_kingdom_43", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_43", slot_faction_common_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_43", slot_faction_veteran_num_tries, 40),
            (faction_set_slot, "fac_small_kingdom_43", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_43", slot_faction_noble_num_tries, 20),
            
            (faction_set_slot, "fac_small_kingdom_44", slot_faction_peasant_num_tries, 10),
            (faction_set_slot, "fac_small_kingdom_44", slot_faction_common_num_tries, 30),
            (faction_set_slot, "fac_small_kingdom_44", slot_faction_veteran_num_tries, 30),
            (faction_set_slot, "fac_small_kingdom_44", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_44", slot_faction_noble_num_tries, 20),
            
            (faction_set_slot, "fac_small_kingdom_45", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_45", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_45", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_45", slot_faction_elite_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_45", slot_faction_noble_num_tries, 80),
            
            (faction_set_slot, "fac_small_kingdom_51", slot_faction_peasant_num_tries, 20),
            (faction_set_slot, "fac_small_kingdom_51", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_51", slot_faction_veteran_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_51", slot_faction_elite_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_51", slot_faction_noble_num_tries, 60),
            
            (faction_set_slot, "fac_small_kingdom_52", slot_faction_peasant_num_tries, 10),
            (faction_set_slot, "fac_small_kingdom_52", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_52", slot_faction_veteran_num_tries, 20),
            (faction_set_slot, "fac_small_kingdom_52", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_52", slot_faction_noble_num_tries, 40),
            
            (faction_set_slot, "fac_small_kingdom_53", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_53", slot_faction_common_num_tries, 50),
            (faction_set_slot, "fac_small_kingdom_53", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_53", slot_faction_elite_num_tries, 50),
            (faction_set_slot, "fac_small_kingdom_53", slot_faction_noble_num_tries, 80),
            
            (faction_set_slot, "fac_small_kingdom_54", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_54", slot_faction_common_num_tries, 80),
            (faction_set_slot, "fac_small_kingdom_54", slot_faction_veteran_num_tries, 40),
            (faction_set_slot, "fac_small_kingdom_54", slot_faction_elite_num_tries, 40),
            (faction_set_slot, "fac_small_kingdom_54", slot_faction_noble_num_tries, 20),
            
            (faction_set_slot, "fac_small_kingdom_55", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_55", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_55", slot_faction_veteran_num_tries, 40),
            (faction_set_slot, "fac_small_kingdom_55", slot_faction_elite_num_tries, 40),
            (faction_set_slot, "fac_small_kingdom_55", slot_faction_noble_num_tries, 20),
            
            (faction_set_slot, "fac_small_kingdom_61", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_61", slot_faction_common_num_tries, 75),
            (faction_set_slot, "fac_small_kingdom_61", slot_faction_veteran_num_tries, 25),
            (faction_set_slot, "fac_small_kingdom_61", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_61", slot_faction_noble_num_tries, 25),
            
            (faction_set_slot, "fac_small_kingdom_62", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_62", slot_faction_common_num_tries, 30),
            (faction_set_slot, "fac_small_kingdom_62", slot_faction_veteran_num_tries, 30),
            (faction_set_slot, "fac_small_kingdom_62", slot_faction_elite_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_62", slot_faction_noble_num_tries, 0),
            
            (faction_set_slot, "fac_small_kingdom_63", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_63", slot_faction_common_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_63", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_63", slot_faction_elite_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_63", slot_faction_noble_num_tries, 80),
            
            (faction_set_slot, "fac_small_kingdom_64", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_64", slot_faction_common_num_tries, 40),
            (faction_set_slot, "fac_small_kingdom_64", slot_faction_veteran_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_64", slot_faction_elite_num_tries, 40),
            (faction_set_slot, "fac_small_kingdom_64", slot_faction_noble_num_tries, 20),
            
            (faction_set_slot, "fac_small_kingdom_65", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_65", slot_faction_common_num_tries, 20),
            (faction_set_slot, "fac_small_kingdom_65", slot_faction_veteran_num_tries, 60),
            (faction_set_slot, "fac_small_kingdom_65", slot_faction_elite_num_tries, 0),
            (faction_set_slot, "fac_small_kingdom_65", slot_faction_noble_num_tries, 20),
            
            (call_script, "script_init_factions_troop_ratio"),

            (faction_set_slot, "fac_small_kingdom_32", slot_faction_has_fixed_name, 1),
            (faction_set_slot, "fac_small_kingdom_51", slot_faction_has_fixed_name, 1),
            
            (call_script, "script_init_factions_politic"),

            (try_for_range, ":fac_1", kingdoms_begin, kingdoms_end),
                (faction_set_slot, ":fac_1", slot_faction_lord_gathering, -1),
                (faction_set_slot, ":fac_1", slot_faction_size, -1),

                (faction_set_slot, ":fac_1", slot_faction_vassal_tax_rate, 5),
                (faction_set_slot, ":fac_1", slot_faction_member_tax_rate, 2),

                (faction_set_slot, ":fac_1", slot_faction_is_at_war, 0),

                (try_begin),
                    (spawn_around_party, "p_centers_end", "pt_name_holders_template"),
                    (assign, ":new_party", reg0),
                    (disable_party, ":new_party"),
                    (faction_set_slot, ":fac_1", slot_faction_name_holder, ":new_party"),
                    (str_store_faction_name, s10, ":fac_1"),
                    (party_set_name, ":new_party", s10),
                (try_end),

                (call_script, "script_faction_update_size", ":fac_1"),
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
            (faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_archer, 30),
            (faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_crossbow, 30),
            (faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_cavalry, 70),
            (faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_lancer, 15),
            (faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_horse_archer, 15),
            (faction_set_slot, "fac_kingdom_1", slot_faction_troop_ratio_mounted_skirmisher, 5),
            
            (faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_infantry, 60),
            (faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_spearman, 15),
            (faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_pikeman, 5),
            (faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_skirmisher, 30),
            (faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_shock_infantry, 25),
            (faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_archer, 90),
            (faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_crossbow, 5),
            (faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_cavalry, 100),
            (faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_lancer, 25),
            (faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_horse_archer, 25),
            (faction_set_slot, "fac_kingdom_2", slot_faction_troop_ratio_mounted_skirmisher, 30),
            
            (faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_infantry, 10),
            (faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_spearman, 35),
            (faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_pikeman, 5),
            (faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_skirmisher, 25),
            (faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_shock_infantry, 10),
            (faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_archer, 20),
            (faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_crossbow, 5),
            (faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_cavalry, 80),
            (faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_lancer, 100),
            (faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_horse_archer, 80),
            (faction_set_slot, "fac_kingdom_3", slot_faction_troop_ratio_mounted_skirmisher, 50),
            
            (faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_infantry, 100),
            (faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_spearman, 30),
            (faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_pikeman, 10),
            (faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_skirmisher, 45),
            (faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_shock_infantry, 15),
            (faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_archer, 45),
            (faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_crossbow, 5),
            (faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_cavalry, 10),
            (faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_lancer, 10),
            (faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_horse_archer, 5),
            (faction_set_slot, "fac_kingdom_4", slot_faction_troop_ratio_mounted_skirmisher, 15),
            
            (faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_infantry, 80),
            (faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_spearman, 100),
            (faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_pikeman, 50),
            (faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_skirmisher, 25),
            (faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_shock_infantry, 15),
            (faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_archer, 15),
            (faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_crossbow, 75),
            (faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_cavalry, 25),
            (faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_lancer, 30),
            (faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_horse_archer, 15),
            (faction_set_slot, "fac_kingdom_5", slot_faction_troop_ratio_mounted_skirmisher, 10),
            
            (faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_infantry, 75),
            (faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_spearman, 10),
            (faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_pikeman, 10),
            (faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_skirmisher, 100),
            (faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_shock_infantry, 20),
            (faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_archer, 35),
            (faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_crossbow, 5),
            (faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_cavalry, 90),
            (faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_lancer, 30),
            (faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_horse_archer, 25),
            (faction_set_slot, "fac_kingdom_6", slot_faction_troop_ratio_mounted_skirmisher, 100),

            (faction_set_slot, "fac_faction_8", slot_faction_troop_ratio_infantry,          90),
            (faction_set_slot, "fac_faction_8", slot_faction_troop_ratio_spearman,          30),
            (faction_set_slot, "fac_faction_8", slot_faction_troop_ratio_pikeman,           10),
            (faction_set_slot, "fac_faction_8", slot_faction_troop_ratio_skirmisher,        15),
            (faction_set_slot, "fac_faction_8", slot_faction_troop_ratio_shock_infantry,    5),
            (faction_set_slot, "fac_faction_8", slot_faction_troop_ratio_archer,            20),
            (faction_set_slot, "fac_faction_8", slot_faction_troop_ratio_crossbow,          20),
            (faction_set_slot, "fac_faction_8", slot_faction_troop_ratio_cavalry,           60),
            (faction_set_slot, "fac_faction_8", slot_faction_troop_ratio_lancer,            20),
            (faction_set_slot, "fac_faction_8", slot_faction_troop_ratio_horse_archer,      10),
            (faction_set_slot, "fac_faction_8", slot_faction_troop_ratio_mounted_skirmisher,10),
            
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
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_13", slot_faction_troop_ratio_spearman, 5),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_13", slot_faction_troop_ratio_lancer, 30),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_14", slot_faction_troop_ratio_archer, 30),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_14", slot_faction_troop_ratio_crossbow, -25),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_15", slot_faction_troop_ratio_cavalry, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_15", slot_faction_troop_ratio_spearman, 10),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_16", slot_faction_troop_ratio_skirmisher, 10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_16", slot_faction_troop_ratio_mounted_skirmisher, 15),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_16", slot_faction_troop_ratio_cavalry, -5),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_16", slot_faction_troop_ratio_infantry, -5),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_17", slot_faction_troop_ratio_shock_infantry, 10), # For swadian sergeant
            (call_script, "script_faction_change_slot", "fac_small_kingdom_17", slot_faction_troop_ratio_infantry, 10),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_21", slot_faction_troop_ratio_lancer, 35),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_21", slot_faction_troop_ratio_cavalry, -15),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_21", slot_faction_troop_ratio_archer, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_21", slot_faction_troop_ratio_infantry, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_21", slot_faction_troop_ratio_spearman, -5),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_21", slot_faction_troop_ratio_shock_infantry, -5),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_22", slot_faction_troop_ratio_cavalry, 10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_22", slot_faction_troop_ratio_infantry, 15),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_22", slot_faction_troop_ratio_spearman, 15),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_22", slot_faction_troop_ratio_shock_infantry, 15),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_23", slot_faction_troop_ratio_infantry, 35),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_23", slot_faction_troop_ratio_pikeman, 25),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_23", slot_faction_troop_ratio_spearman, -5),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_24", slot_faction_troop_ratio_skirmisher, 20),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_24", slot_faction_troop_ratio_infantry, -5),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_24", slot_faction_troop_ratio_shock_infantry, 5),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_25", slot_faction_troop_ratio_horse_archer, 35),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_25", slot_faction_troop_ratio_cavalry, -35),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_31", slot_faction_troop_ratio_shock_infantry, 20),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_31", slot_faction_troop_ratio_infantry, 15),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_31", slot_faction_troop_ratio_lancer, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_31", slot_faction_troop_ratio_spearman, -15),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_spearman, 25),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_shock_infantry, 5),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_archer, 25),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_infantry, 50),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_skirmisher, 40),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_cavalry, -40),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_lancer, -30),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_horse_archer, -50),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_32", slot_faction_troop_ratio_mounted_skirmisher, -30),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_33", slot_faction_troop_ratio_mounted_skirmisher, 30),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_33", slot_faction_troop_ratio_cavalry, -30),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_33", slot_faction_troop_ratio_lancer, -10),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_34", slot_faction_troop_ratio_horse_archer, -15),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_34", slot_faction_troop_ratio_cavalry, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_34", slot_faction_troop_ratio_mounted_skirmisher, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_34", slot_faction_troop_ratio_lancer, 20),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_34", slot_faction_troop_ratio_spearman, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_34", slot_faction_troop_ratio_archer, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_34", slot_faction_troop_ratio_shock_infantry, -5),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_34", slot_faction_troop_ratio_skirmisher, -10),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_35", slot_faction_troop_ratio_cavalry, 10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_35", slot_faction_troop_ratio_horse_archer, -10),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_36", slot_faction_troop_ratio_archer, 15),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_36", slot_faction_troop_ratio_infantry, 25),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_36", slot_faction_troop_ratio_shock_infantry, 30),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_36", slot_faction_troop_ratio_spearman, -10),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_41", slot_faction_troop_ratio_cavalry, 5),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_41", slot_faction_troop_ratio_lancer, 20),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_41", slot_faction_troop_ratio_horse_archer, 10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_41", slot_faction_troop_ratio_archer, -5),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_41", slot_faction_troop_ratio_skirmisher, -10),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_42", slot_faction_troop_ratio_archer, -15),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_42", slot_faction_troop_ratio_skirmisher, 5),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_42", slot_faction_troop_ratio_infantry, 15),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_43", slot_faction_troop_ratio_skirmisher, 10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_43", slot_faction_troop_ratio_infantry, -25),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_43", slot_faction_troop_ratio_archer, -20),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_44", slot_faction_troop_ratio_spearman, 30),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_44", slot_faction_troop_ratio_crossbow, 35),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_44", slot_faction_troop_ratio_archer, -10),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_45", slot_faction_troop_ratio_skirmisher, 10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_45", slot_faction_troop_ratio_cavalry, 25),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_archer, 60),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_crossbow, -60),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_cavalry, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_lancer, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_spearman, -5),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_pikeman, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_51", slot_faction_troop_ratio_infantry, 15),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_52", slot_faction_troop_ratio_spearman, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_52", slot_faction_troop_ratio_cavalry, 25),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_53", slot_faction_troop_ratio_pikeman, -20),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_53", slot_faction_troop_ratio_cavalry, 35),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_54", slot_faction_troop_ratio_skirmisher, 30),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_54", slot_faction_troop_ratio_crossbow, -5),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_54", slot_faction_troop_ratio_archer, -5),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_54", slot_faction_troop_ratio_pikeman, -15),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_54", slot_faction_troop_ratio_horse_archer, 30),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_55", slot_faction_troop_ratio_cavalry, -5),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_55", slot_faction_troop_ratio_lancer, 55),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_55", slot_faction_troop_ratio_horse_archer, 10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_55", slot_faction_troop_ratio_pikeman, -15),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_55", slot_faction_troop_ratio_spearman, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_55", slot_faction_troop_ratio_infantry, -5),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_61", slot_faction_troop_ratio_crossbow, 40),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_61", slot_faction_troop_ratio_archer, -15),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_61", slot_faction_troop_ratio_skirmisher, -15),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_62", slot_faction_troop_ratio_archer, 25),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_62", slot_faction_troop_ratio_skirmisher, -50),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_62", slot_faction_troop_ratio_mounted_skirmisher, -35),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_62", slot_faction_troop_ratio_cavalry, -20),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_62", slot_faction_troop_ratio_infantry, 20),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_62", slot_faction_troop_ratio_spearman, 40),
            
            (call_script, "script_faction_change_slot", "fac_small_kingdom_63", slot_faction_troop_ratio_cavalry, 10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_63", slot_faction_troop_ratio_lancer, 20),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_63", slot_faction_troop_ratio_infantry, -10),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_63", slot_faction_troop_ratio_mounted_skirmisher, -60),
            (call_script, "script_faction_change_slot", "fac_small_kingdom_63", slot_faction_troop_ratio_skirmisher, -45),
            
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
        #   arg1: faction_no
        #   arg2: faction to copy slots from
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
        #   arg1: faction_no
        #   arg2: slot
        #   arg3: change
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
            (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
                (try_for_range, ":other_kingdom", kingdoms_begin, kingdoms_end),
                    (store_sub, ":offset", ":other_kingdom", kingdoms_begin),
                    (store_add, ":treaty_slot", ":offset", slot_faction_kingdom_treaties_begin),
                    (store_add, ":relation_slot", ":offset", slot_faction_kingdom_relation_begin),
                    (faction_set_slot, ":kingdom", ":treaty_slot", sfkt_none),
                    (faction_set_slot, ":kingdom", ":relation_slot", 0),
                    (faction_set_slot, ":kingdom", slot_faction_vassal_type, 0x00),
                (try_end),
            (try_end),
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
            (faction_set_slot, "fac_culture_1", slot_faction_veteran_begin, "trp_swadian_pikeman"),
            (faction_set_slot, "fac_culture_1", slot_faction_elite_begin, "trp_swadian_sergeant"),
            (faction_set_slot, "fac_culture_1", slot_faction_noble_begin, "trp_swadian_noble"),
            
            (faction_set_slot, "fac_culture_2", slot_faction_common_begin, "trp_vaegir_light_infantry"),
            (faction_set_slot, "fac_culture_2", slot_faction_veteran_begin, "trp_vaegir_heavy_infantry"),
            (faction_set_slot, "fac_culture_2", slot_faction_elite_begin, "trp_vaegir_guard"),
            (faction_set_slot, "fac_culture_2", slot_faction_noble_begin, "trp_vaegir_royal_hussar"),
            
            (faction_set_slot, "fac_culture_3", slot_faction_common_begin, "trp_khergit_light_infantry"),
            (faction_set_slot, "fac_culture_3", slot_faction_veteran_begin, "trp_khergit_light_archer"),
            (faction_set_slot, "fac_culture_3", slot_faction_elite_begin, "trp_khergit_guard"),
            (faction_set_slot, "fac_culture_3", slot_faction_noble_begin, "trp_khergit_noble"),
            
            (faction_set_slot, "fac_culture_4", slot_faction_common_begin, "trp_nord_light_infantry"),
            (faction_set_slot, "fac_culture_4", slot_faction_veteran_begin, "trp_nord_medium_infantry"),
            (faction_set_slot, "fac_culture_4", slot_faction_elite_begin, "trp_nord_heavy_cavalry"),
            (faction_set_slot, "fac_culture_4", slot_faction_noble_begin, "trp_nord_noble_infantry"),
            
            (faction_set_slot, "fac_culture_5", slot_faction_common_begin, "trp_rhodok_light_infantry"),
            (faction_set_slot, "fac_culture_5", slot_faction_veteran_begin, "trp_rhodok_heavy_infantry"),
            (faction_set_slot, "fac_culture_5", slot_faction_elite_begin, "trp_rhodok_heavy_pikeman"),
            (faction_set_slot, "fac_culture_5", slot_faction_noble_begin, "trp_rhodok_noble"),
            
            (faction_set_slot, "fac_culture_6", slot_faction_common_begin, "trp_sarranid_medium_infantry"),
            (faction_set_slot, "fac_culture_6", slot_faction_veteran_begin, "trp_sarranid_guard"),
            (faction_set_slot, "fac_culture_6", slot_faction_elite_begin, "trp_sarranid_heavy_infantry"),
            (faction_set_slot, "fac_culture_6", slot_faction_noble_begin, "trp_sarranid_noble_horse_archer"),

            (faction_set_slot, "fac_culture_1", slot_faction_caravan_master, "trp_swadian_caravan_master"),
            (faction_set_slot, "fac_culture_2", slot_faction_caravan_master, "trp_vaegir_caravan_master"),
            (faction_set_slot, "fac_culture_3", slot_faction_caravan_master, "trp_khergit_caravan_master"),
            (faction_set_slot, "fac_culture_4", slot_faction_caravan_master, "trp_nord_caravan_master"),
            (faction_set_slot, "fac_culture_5", slot_faction_caravan_master, "trp_rhodok_caravan_master"),
            (faction_set_slot, "fac_culture_6", slot_faction_caravan_master, "trp_sarranid_caravan_master"),

            (faction_set_slot, "fac_culture_1", slot_faction_caravan_guard, "trp_swadian_caravan_guard"),
            (faction_set_slot, "fac_culture_2", slot_faction_caravan_guard, "trp_vaegir_caravan_guard"),
            (faction_set_slot, "fac_culture_3", slot_faction_caravan_guard, "trp_khergit_caravan_guard"),
            (faction_set_slot, "fac_culture_4", slot_faction_caravan_guard, "trp_nord_caravan_guard"),
            (faction_set_slot, "fac_culture_5", slot_faction_caravan_guard, "trp_rhodok_caravan_guard"),
            (faction_set_slot, "fac_culture_6", slot_faction_caravan_guard, "trp_sarranid_caravan_guard"),
            
            (faction_set_slot, "fac_culture_1", slot_faction_lord_name_begin, "str_kingdom_rank_0"),
            (faction_set_slot, "fac_culture_2", slot_faction_lord_name_begin, "str_kingdom_rank_0"),
            (faction_set_slot, "fac_culture_3", slot_faction_lord_name_begin, "str_khergit_rank_0"),
            (faction_set_slot, "fac_culture_4", slot_faction_lord_name_begin, "str_nord_rank_0"),
            (faction_set_slot, "fac_culture_5", slot_faction_lord_name_begin, "str_rhodok_rank_0"),
            (faction_set_slot, "fac_culture_6", slot_faction_lord_name_begin, "str_sarranid_rank_0"),

            (faction_set_slot, "fac_culture_1", slot_faction_lady_name_begin, "str_kingdom_rank_0_f"),
            (faction_set_slot, "fac_culture_2", slot_faction_lady_name_begin, "str_kingdom_rank_0_f"),
            (faction_set_slot, "fac_culture_3", slot_faction_lady_name_begin, "str_khergit_rank_0_f"),
            (faction_set_slot, "fac_culture_4", slot_faction_lady_name_begin, "str_nord_rank_0_f"),
            (faction_set_slot, "fac_culture_5", slot_faction_lady_name_begin, "str_rhodok_rank_0_f"),
            (faction_set_slot, "fac_culture_6", slot_faction_lady_name_begin, "str_sarranid_rank_0_f"),
            
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

            (faction_set_slot, "fac_culture_7", slot_faction_troops_begin, mercenaries_begin),
            (faction_set_slot, "fac_culture_7", slot_faction_troops_end, factional_mercenaries_begin),

            # For now, mercenaries do not share the same recruitment system as factional troops
            # (faction_set_slot, "fac_culture_7", slot_faction_common_begin, "trp_mercenary_light_infantry"),
            # (faction_set_slot, "fac_culture_7", slot_faction_veteran_begin, "trp_mercenary_infantry"),
            # (faction_set_slot, "fac_culture_7", slot_faction_elite_begin, "trp_mercenary_heavy_infantry"),
            # (faction_set_slot, "fac_culture_7", slot_faction_noble_begin, "trp_mercenary_knight"),

            # Rank names should not be relevant ?
            (faction_set_slot, "fac_culture_7", slot_faction_lord_name_begin, "str_kingdom_rank_0"),
            (faction_set_slot, "fac_culture_7", slot_faction_lady_name_begin, "str_kingdom_rank_0_f"),

            (faction_set_slot, "fac_culture_7", slot_faction_template_troops_begin, "trp_mercenary_lord_template_0"),

            # Names should not be relevant ?
            # (faction_set_slot, "fac_culture_7", slot_faction_names_begin, swadian_names_begin),
            # (faction_set_slot, "fac_culture_7", slot_faction_names_end, swadian_names_end),
        ]),
    
    # script_init_bandits
        # input: none
        # output: none
    ("init_bandits",
        [
            (faction_set_slot, "fac_faction_1", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_faction_1", slot_faction_common_num_tries, -100),
            (faction_set_slot, "fac_faction_1", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_faction_1", slot_faction_elite_num_tries, -100),
            (faction_set_slot, "fac_faction_1", slot_faction_noble_num_tries, -100),
            
            (faction_set_slot, "fac_faction_2", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_faction_2", slot_faction_common_num_tries, -100),
            (faction_set_slot, "fac_faction_2", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_faction_2", slot_faction_elite_num_tries, -100),
            (faction_set_slot, "fac_faction_2", slot_faction_noble_num_tries, -100),
            
            (faction_set_slot, "fac_faction_3", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_faction_3", slot_faction_common_num_tries, -100),
            (faction_set_slot, "fac_faction_3", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_faction_3", slot_faction_elite_num_tries, -100),
            (faction_set_slot, "fac_faction_3", slot_faction_noble_num_tries, -100),
            
            (faction_set_slot, "fac_faction_4", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_faction_4", slot_faction_common_num_tries, -100),
            (faction_set_slot, "fac_faction_4", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_faction_4", slot_faction_elite_num_tries, -100),
            (faction_set_slot, "fac_faction_4", slot_faction_noble_num_tries, -100),
            
            (faction_set_slot, "fac_faction_5", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_faction_5", slot_faction_common_num_tries, -100),
            (faction_set_slot, "fac_faction_5", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_faction_5", slot_faction_elite_num_tries, -100),
            (faction_set_slot, "fac_faction_5", slot_faction_noble_num_tries, -100),
            
            (faction_set_slot, "fac_faction_6", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_faction_6", slot_faction_common_num_tries, -100),
            (faction_set_slot, "fac_faction_6", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_faction_6", slot_faction_elite_num_tries, -100),
            (faction_set_slot, "fac_faction_6", slot_faction_noble_num_tries, -100),
            
            (faction_set_slot, "fac_faction_7", slot_faction_peasant_num_tries, 0),
            (faction_set_slot, "fac_faction_7", slot_faction_common_num_tries, -100),
            (faction_set_slot, "fac_faction_7", slot_faction_veteran_num_tries, 0),
            (faction_set_slot, "fac_faction_7", slot_faction_elite_num_tries, -100),
            (faction_set_slot, "fac_faction_7", slot_faction_noble_num_tries, -100),
            
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
            (faction_set_slot, "fac_faction_1", slot_faction_elite_begin, "trp_bandit_forest_leader"),
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
            (faction_set_slot, "fac_faction_2", slot_faction_elite_begin, "trp_bandit_leader"),
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
            (faction_set_slot, "fac_faction_3", slot_faction_elite_begin, "trp_bandit_mountain_chieftain"),
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
            (faction_set_slot, "fac_faction_4", slot_faction_elite_begin, "trp_bandit_sea_captain"),
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
            (faction_set_slot, "fac_faction_5", slot_faction_elite_begin, "trp_bandit_steppe_chief"),
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
            (faction_set_slot, "fac_faction_6", slot_faction_common_begin, "trp_bandit_taiga_bandit"),
            (faction_set_slot, "fac_faction_6", slot_faction_veteran_begin, "trp_bandit_taiga_bandit"),
            (faction_set_slot, "fac_faction_6", slot_faction_elite_begin, "trp_bandit_taiga_chieftain"),
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
            (faction_set_slot, "fac_faction_7", slot_faction_common_begin, "trp_bandit_desert_nomad"),
            (faction_set_slot, "fac_faction_7", slot_faction_veteran_begin, "trp_bandit_desert_nomad"),
            (faction_set_slot, "fac_faction_7", slot_faction_elite_begin, "trp_bandit_desert_chief"),
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

            # Make bandits enemies of every faction
            (try_for_range, ":bandit_faction", bandit_factions_begin, bandit_factions_end),
                (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
                    (set_relation, ":kingdom", ":bandit_faction", -20),
                (try_end),
            (try_end),
            # Add some inter-bandit relations ?
            # Sea raiders enemy of tundra bandits
            (set_relation, "fac_faction_4", "fac_faction_6", -10),
            # Steppe bandits enemy of desert bandits
            (set_relation, "fac_faction_5", "fac_faction_7", -10),
            # Mountains bandits enemy of forest bandits
            (set_relation, "fac_faction_3", "fac_faction_1", -10),
            # Forest bandits enemy of steppe bandits
            (set_relation, "fac_faction_1", "fac_faction_3", -10),
            # Regular bandits enemy of desert bandits
            (set_relation, "fac_faction_2", "fac_faction_7", -10),
            # Mountain bandits enemy of tundra bandits
            (set_relation, "fac_faction_3", "fac_faction_6", -10),

            # Steppe bandits allies of tundra bandits
            (set_relation, "fac_faction_5", "fac_faction_6", 10),
            # Forest bandits allies of regular bandits
            (set_relation, "fac_faction_1", "fac_faction_2", 10),
            
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
        #   arg1: faction_1
        #   arg2: faction_2
        # output: none
    ("faction_declare_war_to_faction",
        [
            (store_script_param, ":faction_1", 1),
            (store_script_param, ":faction_2", 2),
            
            (set_relation, ":faction_1", ":faction_2", relation_state_war),
            
            (str_store_faction_name_link, s10, ":faction_1"),
            (str_store_faction_name_link, s11, ":faction_2"),
            (display_message, "@{s10} declaring war to {s11}"),

            (call_script, "script_faction_political_event", ":faction_1", political_event_war_declared, ":faction_2", -1, -1),

            (call_script, "script_faction_clear_treaty", ":faction_1", ":faction_2", sfkt_all_treaty_clear),
            
            (store_current_day, ":current_day"),
            (faction_get_slot, ":num_wars_1", ":faction_1", slot_faction_is_at_war),
            (try_begin),
                (le, ":num_wars_1", 0),
                (faction_set_slot, ":faction_1", slot_faction_is_at_war, 1),
                (faction_set_slot, ":faction_1", slot_faction_last_peace, ":current_day"),
            (else_try),
                (val_add, ":num_wars_1", 1),
                (faction_set_slot, ":faction_1", slot_faction_is_at_war, ":num_wars_1"),
            (try_end),
            (faction_get_slot, ":num_wars_2", ":faction_2", slot_faction_is_at_war),
            (try_begin),
                (le, ":num_wars_2", 0),
                (faction_set_slot, ":faction_2", slot_faction_is_at_war, 1),
                (faction_set_slot, ":faction_2", slot_faction_last_peace, ":current_day"),
            (else_try),
                (val_add, ":num_wars_2", 1),
                (faction_set_slot, ":faction_2", slot_faction_is_at_war, ":num_wars_2"),
            (try_end),
        ]),
    
    # script_faction_make_peace_to_faction
        # input:
        #   arg1: faction_1
        #   arg2: faction_2
        # output: none
    ("faction_make_peace_to_faction",
        [
            (store_script_param, ":faction_1", 1),
            (store_script_param, ":faction_2", 2),
            
            (set_relation, ":faction_1", ":faction_2", relation_neutral),
            # (set_relation, ":faction_2", ":faction_1", relation_neutral),
            
            (faction_get_slot, ":num_wars_1", ":faction_1", slot_faction_is_at_war),
            (val_add, ":num_wars_1", -1),
            (faction_set_slot, ":faction_1", slot_faction_is_at_war, ":num_wars_1"),
            
            (faction_get_slot, ":num_wars_2", ":faction_2", slot_faction_is_at_war),
            (val_add, ":num_wars_2", -1),
            (faction_set_slot, ":faction_2", slot_faction_is_at_war, ":num_wars_2"),
        ]),
    
    # script_faction_set_random_relation_with_faction
        # input:
        #   arg1: faction_1
        #   arg2: faction_2
        #   arg3: relation (0: war, 1: bad terms, 2: neutral, 3: friendly, -1: random_no_war)
    ("faction_set_random_relation_with_faction",
        [
            (store_script_param, ":faction_1", 1),
            (store_script_param, ":faction_2", 2),
            (store_script_param, ":relation", 3),
            
            (try_begin),
                (eq, ":relation", 0),
                (assign, ":new_relation", relation_state_war),
                (call_script, "script_faction_declare_war_to_faction", ":faction_1", ":faction_2"),
            (else_try),
                (eq, ":relation", 1),
                (assign, ":new_relation", relation_state_conflict),
            (else_try),
                (eq, ":relation", 2),
                (assign, ":new_relation", relation_state_neutral),
            (else_try),
                (eq, ":relation", 3),
                (assign, ":new_relation", relation_state_friendly),
            (else_try),
                (eq, ":relation", -1),
                (store_random_in_range, ":new_relation", relation_state_war, relation_state_friendly),
            (try_end),
            
            (try_begin),
                (call_script, "script_cf_debug", debug_faction|debug_simple),
                (str_store_faction_name, s10, ":faction_1"),
                (str_store_faction_name, s11, ":faction_2"),
                (assign, reg10, ":new_relation"),
                (display_message, "@{s10} now has a relation of {reg10} with {s11}"),
            (try_end),
            
            (set_relation, ":faction_1", ":faction_2", ":new_relation"),
            # (set_relation, ":faction_2", ":faction_1", ":new_relation"),
        ]),
    
    # script_troop_change_level
        # input:
        #   arg1: troop_no
        #   arg2: new_rank
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
            
            (store_add, ":stats_troop", ":template_troop", ":new_rank"),
            
            # New stats
            (call_script, "script_troop_change_stat_with_template", ":troop_no", ":stats_troop"),
            
            # ToDo: pay for equipement upgrade
            # Removing old equipment
            (try_for_range, ":equip_slot", ek_item_0, ek_food),
                (troop_get_inventory_slot, ":item", ":troop_no", ":equip_slot"),
                (gt, ":item", 0),
                (troop_remove_item, ":troop_no", ":item"),
            (try_end),
            # Following does not remove equipped items
            (troop_clear_inventory, ":troop_no"),
            
            (call_script, "script_troop_get_equipement_level", ":troop_no"),
            (assign, ":equipement_level", reg0),
            
            (troop_set_slot, ":troop_no", slot_troop_equipement_level, ":equipement_level"),
            
            (store_add, ":equipement_template", ":template_troop", ":equipement_level"),
            # New equipments
            (call_script, "script_troop_change_equipement_with_template", ":troop_no", ":equipement_template"),
            (troop_equip_items, ":troop_no"),
        ]),
    
    # script_troop_get_equipement_level
        # input:
        #   arg1: troop_no
        # output:
        #   reg0: level
    ("troop_get_equipement_level",
        [
            (store_script_param, ":troop_no", 1),
            
            (store_troop_faction, ":faction", ":troop_no"),
            (faction_get_slot, ":era", ":faction", slot_faction_era),
            
            (troop_get_slot, ":level", ":troop_no", slot_troop_level),
            
            (try_begin),
                (le, ":era", 1),
                (val_sub, ":level", 2),
                (val_min, ":level", 4),
            (else_try),
                (le, ":era", 4),
                # Everyone has -1 except king and marshall who get -2
                (val_mul, ":level", 12),
                (val_div, ":level", 15),
            (else_try),
                (le, ":era", 5),
                (val_sub, ":level", 1),
            (try_end),
            (val_max, ":level", 0),
            
            (assign, reg0, ":level"),
        ]),
    
    # script_troop_update_name
        # input:
        #   arg1: troop_no
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
        #   arg1: troop_no
        #   arg2: template
        # output: none
    ("troop_change_stat_with_template",
        [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":template", 2),
            
            (try_for_range, ":stat", ca_strength, ca_charisma + 1),
                (store_attribute_level, ":template_stat", ":template", ":stat"),
                (store_attribute_level, ":troop_stat", ":troop_no", ":stat"),
                
                (store_sub, ":difference", ":template_stat", ":troop_stat"),
                (troop_raise_attribute, ":troop_no", ":stat", ":difference"),
            (try_end),
            
            (try_for_range, ":skill", skl_trade, skl_reserved_15), # Do we need to go through all skills?
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
    #   arg1: troop_no
    #   arg2: template
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
    #   arg1: troop_no
    #   arg2: template
    # output:
    #   reg0: item_added
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
    #   arg1: troop_no
    #   arg2: template
    # output:
    #   reg0: item_added
    #   reg1: item_added_2
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
                    (try_begin),
                        (eq, ":equip_type", tle_light_bow),
                        (assign, ":continue", 1),
                    (else_try),
                        (eq, ":equip_type", tle_heavy_bow),
                        (assign, ":continue", 1),
                    (try_end),
                    (eq, ":continue", 1),
                    (call_script, "script_troop_take_first_troop_equipement_of_type", ":troop_no", ":template", itp_type_arrows),
                    (assign, reg1, reg0),
                (else_try),
                    (eq, ":item_type", itp_type_crossbow),
                    (try_begin),
                        (eq, ":equip_type", tle_light_crossbow),
                        (this_or_next|eq, ":cur_item", "itm_hunting_crossbow"),
                        (eq, ":cur_item", "itm_light_crossbow"),
                        (assign, ":continue", 1),
                    (else_try),
                        (eq, ":equip_type", tle_heavy_crossbow),
                        (is_between, ":cur_item", "itm_crossbow", "itm_items_end"),
                        (assign, ":continue", 1),
                    (try_end),
                    (eq, ":continue", 1),
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
    #   arg1: troop_no
    #   arg2: template
    # output:
    #   reg0: item_added
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
    #   arg1: troop_no
    #   arg2: template
    # output:
    #   reg0: item_added
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
    #   arg1: troop_no
    #   arg2: template
    # output:
    #   reg0: item_added
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
    #   arg1: troop_no
    #   arg2: template
    # output:
    #   reg0: item_added
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
    #   arg1: troop_no
    #   arg2: template
    # output:
    #   reg0: item_added
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
    #   arg1: troop_no
    #   arg2: template
    # output:
    #   reg0: item_added
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
            # this is made so that rhodok lords will use them most of the time even if mounted
        ]),
    
    # script_troop_take_random_troop_equipement
        # input:
        #   arg1: troop_no
        #   arg2: template_troop
        # output:
        #   reg0: item_added
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
        #   arg1: troop_no
        #   arg2: template_troop
        #   arg3: item_type
        # output:
        #   reg0: item_added
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
        #   arg1: troop_no
        #   arg2: template_troop
        #   arg3: item_type
        # output:
        #   reg0: item_added
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

    # script_party_get_prefered_wages_limit
        # input:
        #   arg1: party_no
        # output:
        #   reg0: wanted_wages
        #   reg1: min_prefered_wages
        #   reg2: max_prefered_wages
    ("party_get_prefered_wages_limit",
        [
            (store_script_param, ":party_no", 1),

            (assign, ":wanted_wages", 0),
            (assign, ":tolerance_min", 80),
            (assign, ":tolerance_max", 125),

            (party_get_slot, ":party_type", ":party_no", slot_party_type),
            (try_begin),
                (eq, ":party_type", spt_war_party),
                (party_get_slot, ":leader", ":party_no", slot_party_leader),
                (ge, ":leader", 0),
                (troop_get_slot, ":wanted_wages", ":leader", slot_troop_wanted_party_wages),
            (else_try),
                (party_get_slot, ":wanted_wages", ":party_no", slot_party_wanted_party_wages),
                (try_begin),
                    (eq, ":wanted_wages", 0),
                    # Troop has either not been processed or has no fixed income
                    # We can assume the latter are mercenaries with no contracts
                (try_end),

                (try_begin),
                    (is_between, ":party_type", spt_village, spt_fort + 1),
                    (assign, ":tolerance_min", 90),
                    (assign, ":tolerance_max", 150),
                (try_end),
            (try_end),

            (store_mul, ":min_wages", ":wanted_wages", ":tolerance_min"),
            (val_div, ":min_wages", 100),
            (store_mul, ":max_wages", ":wanted_wages", ":tolerance_max"),
            (val_div, ":max_wages", 100),

            (assign, reg0, ":wanted_wages"),
            (assign, reg1, ":min_wages"),
            (assign, reg2, ":max_wages"),
        ]),
    
    # script_troop_get_lord_horse_slot
        # input:
        #   arg1: troop_no
        # output:
        #   reg0: horse
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
    #   arg1: troop_no
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
                    (troop_set_slot, ":troop_no", slot_troop_lord_equipement, tle_heavy_crossbow),
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
    #   arg1: team_no
    # output:
    #   reg0: range_begin
    #   reg1: range_end
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
    #   reg0: range_begin
    #   reg1: range_end
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
    #   reg0: range_begin
    #   reg1: range_end
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
            (scene_set_slot, "scn_castle_plain_01_outside", slot_scene_num_defend_points, 2),
            (scene_set_slot, "scn_castle_plain_01_outside", slot_scene_num_attack_spawn, 2),
            (scene_set_slot, "scn_castle_plain_01_outside", slot_scene_num_archer_points, 8),
            
            (scene_set_slot, "scn_castle_plain_02_outside", slot_scene_num_defend_points, 2),
            (scene_set_slot, "scn_castle_plain_02_outside", slot_scene_num_attack_spawn, 2),
            (scene_set_slot, "scn_castle_plain_02_outside", slot_scene_num_archer_points, 9),
            
            (scene_set_slot, "scn_castle_plain_wood_01_outside", slot_scene_num_defend_points, 2),
            (scene_set_slot, "scn_castle_plain_wood_01_outside", slot_scene_num_attack_spawn, 2),
            (scene_set_slot, "scn_castle_plain_wood_01_outside", slot_scene_num_archer_points, 12),
            
            (scene_set_slot, "scn_castle_plain_dark_01_outside", slot_scene_num_defend_points, 2),
            (scene_set_slot, "scn_castle_plain_dark_01_outside", slot_scene_num_attack_spawn, 2),
            (scene_set_slot, "scn_castle_plain_dark_01_outside", slot_scene_num_archer_points, 8),
            
            (scene_set_slot, "scn_castle_steppe_01_outside", slot_scene_num_defend_points, 2),
            (scene_set_slot, "scn_castle_steppe_01_outside", slot_scene_num_attack_spawn, 2),
            (scene_set_slot, "scn_castle_steppe_01_outside", slot_scene_num_archer_points, 9),
            
            (scene_set_slot, "scn_castle_snow_01_outside", slot_scene_num_defend_points, 2),
            (scene_set_slot, "scn_castle_snow_01_outside", slot_scene_num_attack_spawn, 2),
            (scene_set_slot, "scn_castle_snow_01_outside", slot_scene_num_archer_points, 7),
            
            (scene_set_slot, "scn_castle_snow_wood_01_outside", slot_scene_num_defend_points, 2),
            (scene_set_slot, "scn_castle_snow_wood_01_outside", slot_scene_num_attack_spawn, 2),
            (scene_set_slot, "scn_castle_snow_wood_01_outside", slot_scene_num_archer_points, 9),
            
            (scene_set_slot, "scn_castle_desert_01_outside", slot_scene_num_defend_points, 2),
            (scene_set_slot, "scn_castle_desert_01_outside", slot_scene_num_attack_spawn, 2),
            (scene_set_slot, "scn_castle_desert_01_outside", slot_scene_num_archer_points, 9),
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
    #   arg1: troop_no
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
            

            (try_begin),
                (is_between, ":home", centers_begin, centers_end),
                (store_faction_of_party, ":center_faction", ":home"),
                (store_troop_faction, ":troop_faction", ":troop_no"),
                (try_begin),
                    (neq, ":center_faction", ":troop_faction"),
                    (try_begin),
                        (call_script, "script_cf_debug", debug_simple),
                        (str_store_troop_name, s10, ":troop_no"),
                        (str_store_party_name, s11, ":home"),
                        (str_store_faction_name, s12, ":center_faction"),
                        (display_message, "@Trying to spawn {s10} in {s11} with faction {s12}", text_color_impossible),
                    (try_end),
                (else_try),
                    (call_script, "script_spawn_party_around_party", ":home", "pt_war_party"),
                    (assign, ":party", reg0),
                    
                    (store_troop_faction, ":faction", ":troop_no"),
                    (party_set_faction, ":party", ":faction"),
                    
                    (party_set_flags, ":party", pf_show_faction, 1),
                    
                    (party_add_leader, ":party", ":troop_no"),
                    
                    (party_set_slot, ":party", slot_party_leader, ":troop_no"),
                    (troop_set_slot, ":troop_no", slot_troop_leaded_party, ":party"),
                    
                    (party_set_slot, ":party", slot_party_type, spt_war_party),
                    
                    (call_script, "script_party_set_behavior", ":party", tai_traveling_to_party, ":home"),
                    
                    (call_script, "script_party_process_mission", ":party", 1),
                    
                    # ToDo: special name for parties
                    (str_store_troop_name, s10, ":troop_no"),
                    (party_set_name, ":party", "@{s10}'s Party"),
                (try_end),
            (try_end),
        ]),
    
    # script_cf_lord_can_spawn
    # input:
    #   arg1: troop_no
    # output: none
    ("cf_lord_can_spawn",
        [
            (store_script_param, ":troop_no", 1),

            (store_troop_faction, ":troop_faction", ":troop_no"),
            (neg|faction_slot_eq, ":troop_faction", slot_faction_status, sfst_disabled),
            
            (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of, 0),
            
            (call_script, "script_troop_get_home", ":troop_no", 1),
            (assign, ":home", reg0),
            
            (ge, ":home", centers_begin),
            # ToDo:
        ]),
    
    # script_troop_update_home
    # input:
    #   arg1: troop_no
    # output:
    #   reg0: new_home
    ("troop_update_home",
        [
            (store_script_param, ":troop_no", 1),

            (assign, ":home", -1),
            
            (store_troop_faction, ":troop_faction", ":troop_no"),
            
            (assign, ":first_center", -1),
            
            (assign, ":end", castles_end),
            # Take first owned center (towns first)
            (try_for_range, ":cur_center", towns_begin, ":end"),
                (store_faction_of_party, ":center_faction", ":cur_center"),

                (try_begin),
                    (party_slot_eq, ":cur_center", slot_party_lord, ":troop_no"),
                    (eq, ":center_faction", ":troop_faction"),
                    
                    (assign, ":home", ":cur_center"),
                    (assign, ":end", 0),
                (else_try),
                    (eq, ":first_center", -1),
                    # We take the first center of this faction in case the capital has been taken
                    (eq, ":center_faction", ":troop_faction"),

                    (assign, ":first_center", ":cur_center"),
                (try_end),
            (try_end),
            (try_begin),
                (eq, ":home", -1),
                # Then check villages
                (assign, ":end", villages_end),
                (try_for_range, ":cur_center", villages_begin, ":end"),
                    (party_slot_eq, ":cur_center", slot_party_lord, ":troop_no"),

                    (store_faction_of_party, ":center_faction", ":cur_center"),
                    (eq, ":center_faction", ":troop_faction"),
                    
                    (assign, ":home", ":cur_center"),
                    # (party_get_slot, ":home", ":cur_center", slot_party_linked_party),
                    (assign, ":end", 0),
                (try_end),
                (try_begin),
                    (eq, ":home", -1),
                    # If lord has no home, we take his leader's home
                    (troop_get_slot, ":leader", ":troop_no", slot_troop_vassal_of),
                    (try_begin),
                        (ge, ":leader", 0),
                        (troop_get_slot, ":home", ":leader", slot_troop_home),
                        # (call_script, "script_troop_get_home", ":leader", 1),
                        # (assign, ":home", reg0),
                        (gt, ":home", 0),
                    (else_try),
                        (faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
                        (try_begin),
                            (ge, ":faction_leader", 0),
                            (neq, ":faction_leader", ":troop_no"),
                            
                            (troop_get_slot, ":home", ":faction_leader", slot_troop_home),
                            # (call_script, "script_troop_get_home", ":faction_leader", 1),
                            # (assign, ":home", reg0),
                        (try_end),
                    (try_end),
                (try_end),
            (try_end),
                        
            (try_begin),
                (le, ":home", 0),
                (assign, ":home", ":first_center"),
            (try_end),
            
            (troop_set_slot, ":troop_no", slot_troop_home, ":home"),
            (assign, reg0, ":home"),
        ]),

    # script_troop_get_home
    # input:
    #   arg1: troop_no
    #   arg2: walled (if home needs to be a walled center)
    # output:
    #   reg0: home
    ("troop_get_home",
        [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":walled", 2),
            
            (store_troop_faction, ":troop_faction", ":troop_no"),
            
            (troop_get_slot, ":home", ":troop_no", slot_troop_home),
            (try_begin),
                (le, ":home", 0),
                (call_script, "script_troop_update_home", ":troop_no"),
                (assign, ":home", reg0),
            (else_try),
                (is_between, ":home", centers_begin, centers_end),
                (store_faction_of_party, ":home_faction", ":home"),
                (neq, ":troop_faction", ":home_faction"),
                (call_script, "script_troop_update_home", ":troop_no"),
                (assign, ":home", reg0),
            (try_end),
            (try_begin),
                (gt, ":home", 0),
                (eq, ":walled", 1),
                (party_get_slot, ":party_type", ":home", slot_party_type),
                (eq, ":party_type", spt_village),
                (party_get_slot, ":linked_center", ":home", slot_party_linked_party),
                (try_begin),
                    (gt, ":linked_center", 0),
                    (store_faction_of_party, ":home_faction", ":linked_center"),
                    (try_begin),
                        (neq, ":home_faction", ":troop_faction"),
                        (troop_get_slot, ":liege", ":troop_no", slot_troop_vassal_of),
                        (try_begin),
                            (ge, ":liege", 0),
                            (call_script, "script_troop_get_home", ":liege", 1),
                            (assign, ":home", reg0),
                        (else_try),
                            (call_script, "script_troop_update_home", ":troop_no"),
                            (assign, ":home", reg0),
                        (try_end),
                    (else_try),
                        (assign, ":home", ":linked_center"),
                    (try_end),
                (try_end),
            (try_end),
            
            (assign, reg0, ":home"),
        ]),
    
    # script_party_process_ai
    # input:
    #   arg1: party_no
    # output: none
    ("party_process_ai",
        [
            (store_script_param, ":party_no", 1),
            
            (party_get_slot, ":leader", ":party_no", slot_party_leader),
            
            (troop_get_slot, ":mission", ":leader", slot_troop_mission),
            (troop_get_slot, ":mission_object", ":leader", slot_troop_mission_object),
            
            (troop_get_slot, ":current_behavior", ":leader", slot_troop_behavior),
            (troop_get_slot, ":current_object", ":leader", slot_troop_behavior_object),
            
            (party_get_attached_to, ":attached_to", ":party_no"),
            (store_faction_of_party, ":party_faction", ":party_no"),
            
            (call_script, "script_troop_get_home", ":leader", 0),
            (assign, ":home", reg0),

            (store_current_hours, ":hours"),
            
            (try_begin),
                (party_get_battle_opponent, ":opponent", ":party_no"),
                (ge, ":opponent", 0),
                (store_faction_of_party, ":opponent_faction", ":opponent"),
                (store_relation, ":rel", ":opponent_faction", ":party_faction"),
                (neq, ":opponent_faction", ":party_faction"),
                (lt, ":rel", 0),
            (else_try),
                (eq, "$g_disable_ai", 1),
                (try_begin),
                    (eq, ":attached_to", ":home"),
                (else_try),
                    (call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_party, ":home"),
                (try_end),
            (else_try),
                (eq, ":mission", tm_none),
                
                (try_begin),
                    (call_script, "script_cf_party_need_troops", ":party_no"),
                    (assign, ":need_type", reg0),
                    
                    (assign, ":stop", 0),

                    (this_or_next|ge, ":need_type", type_moderate),
                    (party_slot_eq, ":party_no", slot_party_preparing_for_war, 1),
                    (try_begin),
                        (eq, ":current_object", ":home"),
                        (this_or_next|eq, ":current_behavior", tai_traveling_to_party),
                        (eq, ":attached_to", ":home"),
                        (assign, ":stop", 1),
                    (else_try),
                        (try_begin),
                            (is_between, ":attached_to", walled_centers_begin, walled_centers_end),
                            (eq, ":need_type", type_critical),
                            # We don't move from current center if we have too few men
                        (else_try),
                            (call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_party, ":home"),
                        (try_end),
                        (assign, ":stop", 1),
                    (try_end),
                    (eq, ":stop", 1),
                (else_try),
                    (troop_get_slot, ":last_rest", ":leader", slot_troop_last_rest),
                    (assign, ":stop", 0),
                    (store_sub, ":rest_time", ":hours", ":last_rest"),
                    (this_or_next|ge, ":rest_time", 7*24),
                    (eq, ":attached_to", ":home"),

                    (try_begin),
                        (eq, ":attached_to", ":home"),
                        (try_begin),
                            (ge, ":rest_time", 7*24),
                            (troop_set_slot, ":leader", slot_troop_last_rest, ":hours"),
                        (else_try),
                            (ge, ":rest_time", 28),
                            (troop_set_slot, ":leader", slot_troop_last_rest, ":hours"),
                            (call_script, "script_party_set_behavior", ":party_no", tai_patroling_center, ":home"),
                        (try_end),
                        (assign, ":stop", 1),
                    (else_try),
                        (store_distance_to_party_from_party, ":distance", ":home", ":party_no"),
                        (le, ":distance", 20),
                        (call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_party, ":home"),
                        (assign, ":stop", 1),
                    (try_end),
                    (eq, ":stop", 1),
                (else_try),
                    (call_script, "script_party_set_behavior", ":party_no", tai_patroling_center, ":home"),
                (try_end),
            (else_try),
                (eq, ":mission", tm_defending),
                
                (is_between, ":mission_object", centers_begin, centers_end),
                (party_get_battle_opponent, ":opponent", ":mission_object"),
                (try_begin),
                    (ge, ":opponent", 0),
                    (call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_party, ":mission_object"),
                (else_try),
                    (call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_point, ":mission_object"),
                (try_end),
            (else_try),
                (eq, ":mission", tm_attacking),
                
                (assign, ":stop", 1),
                (try_begin),
                    (is_between, ":mission_object", centers_begin, centers_end),
                    (store_faction_of_party, ":object_faction", ":mission_object"),
                    (store_relation, ":faction_relation", ":object_faction", ":party_faction"),
                    (this_or_next|eq, ":object_faction", ":party_faction"),
                    (ge, ":faction_relation", relation_neutral),
                    (call_script, "script_party_process_mission", ":party_no", 1),
                    (call_script, "script_party_set_behavior", ":party_no", tai_patroling_center, ":mission_object"),
                (else_try),
                    (neg|is_between, ":mission_object", centers_begin, centers_end),
                    (call_script, "script_party_process_mission", ":party_no", 1),
                (else_try),
                    (is_between, ":mission_object", centers_begin, centers_end),
                    (store_distance_to_party_from_party, ":distance", ":mission_object", ":party_no"),
                    (try_begin),
                        (ge, ":distance", 4),
                        
                        (try_begin),
                            (this_or_next|neq, ":current_behavior", tai_attacking_center),
                            (neq, ":current_object", ":mission_object"),
                            
                            (call_script, "script_party_set_behavior", ":party_no", tai_attacking_center, ":mission_object"),
                        (try_end),
                    (else_try),
                        (party_get_slot, ":besieger", ":mission_object", slot_party_besieged_by),
                        
                        (assign, ":continue", 1),
                        (try_begin),
                            (lt, ":besieger", 0),
                            (call_script, "script_party_besiege_party", ":party_no", ":mission_object"),
                        (else_try),
                            (neq, ":besieger", ":party_no"),
                            (assign, ":continue", 0),
                            (party_get_slot, ":besieger_leader", ":besieger", slot_party_leader),
                            (ge, ":besieger_leader", 0),
                            (troop_set_slot, ":leader", slot_troop_mission, tm_escorting),
                            (troop_set_slot, ":leader", slot_troop_mission_object, ":besieger_leader"),
                        (try_end),
                        
                        (try_begin),
                            (eq, ":continue", 1),
                            (party_get_battle_opponent, ":own_opponent", ":party_no"),
                            (eq, ":own_opponent", -1),

                            (store_random_in_range, ":random", 0, 10),
                            (eq, ":random", 0),
                            
                            (troop_set_slot, ":leader", slot_troop_last_attack, ":hours"),
                            (party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
                            (party_set_ai_object, ":party_no", ":current_object"),
                        (try_end),
                    (try_end),
                (else_try),
                    (call_script, "script_party_set_behavior", ":party_no", tai_patroling_center, ":home"),
                (try_end),
            (else_try),
                (eq, ":mission", tm_escorting),
                (try_begin),
                    (eq, ":current_behavior", tai_accompanying_party),
                    (try_begin),
                        (eq, ":current_object", ":mission_object"),
                        
                        (party_get_battle_opponent, ":opponent", ":mission_object"),
                        (try_begin),
                            (ge, ":opponent", 0),
                            (party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
                            (party_set_ai_object, ":party_no", ":opponent"),
                            (troop_set_slot, ":leader", slot_troop_behavior, -1),
                        (try_end),
                    (else_try),
                        (call_script, "script_party_set_behavior", ":party_no", tai_accompanying_party, ":mission_object"),
                    (try_end),
                (else_try),
                    (eq, ":current_behavior", tai_accompanying_troop),
                    (troop_get_slot, ":object_leaded_party", ":mission_object", slot_troop_leaded_party),
                    
                    (try_begin),
                        (this_or_next|eq, ":object_leaded_party", -1),
                        (troop_slot_ge, ":mission_object", slot_troop_prisoner_of, 0), # Do not follow lord taken prisoner
                        (call_script, "script_party_process_mission", ":party_no", 1),
                        # Select an action based on the old mission
                        # Weak lords should abandon their mission and go back home (unless they are defending)
                        # Stronger lords could raid villages or continue the old mission
                    (else_try),
                        (try_begin),
                            # (eq, ":current_object", ":object_leaded_party"),
                            (party_get_battle_opponent, ":opponent", ":object_leaded_party"),
                            (try_begin),
                                (ge, ":opponent", 0),
                                (party_set_ai_object, ":party_no", ":opponent"),
                                (party_set_ai_behavior, ":party_no", ai_bhvr_attack_party),
                                (troop_set_slot, ":leader", slot_troop_behavior, -1),
                            (try_end),
                        (else_try),
                            (call_script, "script_party_set_behavior", ":party_no", tai_accompanying_troop, ":mission_object"),
                        (try_end),
                    (try_end),
                (else_try),
                    (call_script, "script_party_set_behavior", ":party_no", tai_accompanying_troop, ":mission_object"),
                (try_end),
            (try_end),
            
        ]),
    
    # script_party_process_ai
    # input: 
    #   arg1: party_no
    # output: none
    # ("party_process_ai",
    #     [
    #         (store_script_param, ":party_no", 1),

    #         (party_get_slot, ":leader", ":party_no", slot_party_leader),

    #         (troop_get_slot, ":mission", ":leader", slot_troop_mission),
    #         (troop_get_slot, ":mission_object", ":leader", slot_troop_mission_object),
            
    #         (troop_get_slot, ":behavior", ":leader", slot_troop_behavior),
    #         (troop_get_slot, ":behavior_object", ":leader", slot_troop_behavior_object),
            
    #         (try_begin),
    #             (eq, "$g_disable_ai", 1),
    #             # Ai disabled, do nothing
    #         (else_try),
    #             (eq, ":mission", tm_none),
    #             # No mission, do civic duties
    #             # Head home, visit family / friends
    #             # Go to tournaments
    #             # Patrol his territory
    #         (try_end),
    #     ]),
    
    # script_party_process_mission
    # input:
    #   arg1: party_no
    # output: none
    # ("party_process_mission",
    #     [
    #         (store_script_param, ":party_no", 1),

    #         (try_begin),
    #             (eq, "$g_disable_ai", 1),
    #             # Ai disabled, we do nothing
    #         (else_try),
    #             (party_get_slot, ":leader", ":party_no", slot_party_leader),

    #             (store_faction_of_party, ":party_faction", ":party_no"),
    #             (faction_get_slot, ":num_wars", ":party_faction", slot_faction_is_at_war),
    #             (faction_get_slot, ":preparing_war", ":party_faction", slot_faction_preparing_war),

    #             (troop_get_slot, ":old_mission", ":leader", slot_troop_mission),
    #             (troop_get_slot, ":old_mission_object", ":leader", slot_troop_mission_object),
    #             (assign, ":mission", ":old_mission"),
    #             (assign, ":mission_object", ":old_mission_object"),

    #             (party_get_num_companions, ":party_size", ":party_no"),

    #             (call_script, "script_party_get_ideal_party_size", ":party_no"),
    #             (assign, ":ideal_party_size", reg0),
    #             (assign, ":max_party_size", reg1),
    #             (call_script, "script_troop_get_mission_party_size_multiplier", ":leader"),
    #             (assign, ":party_size_multiplier", reg0),

    #             (store_mul, ":minimum_mission_party_size", ":ideal_party_size", 100),
    #             (val_div, ":minimum_mission_party_size", ":party_size_multiplier"),

    #             (try_begin),
    #                 (call_script, "script_cf_party_can_recruit", ":party_no"),
    #                 (lt, ":party_size", ":ideal_party_size"),
    #                 (assign, ":mission", tm_recruit),
    #             (else_try),
    #                 (eq, ":mission", tm_none),
    #                 (this_or_next|ge, ":num_wars", 1),
    #                 (eq, ":preparing_war", 1),
    #                 (try_begin),
    #                     (gt, ":num_vassals", 0),
    #                     # ToDo: get num following vassals
    #                     (assign, ":following_vassals", ":num_vassals"),
    #                     (try_begin),
    #                         (lt, ":following_vassals", ":num_vassals"),
    #                         (assign, ":mission", tm_gather),
    #                     (else_try),
    #                         (assign, ":mission", tm_prepare),
    #                 (else_try),
    #                     (assign, ":mission", tm_none),
    #                 (try_end),
    #             (else_try),
    #                 (eq, ":mission", tm_gather),
    #                 (try_begin),
    #                     # ToDo: get num following vassals
    #                     (assign, ":mission", tm_prepare),
    #                 (try_end),
    #             (else_try),
    #                 (eq, ":mission", tm_prepare),
    #                 # ToDo: prepare
    #             (else_try),
    #                 (eq, ":mission", tm_follow),
    #                 # ToDo: follow
    #             (else_try),
    #                 (eq, ":mission", tm_attack),
    #                 # ToDo: attack
    #             (else_try),
    #                 (eq, ":mission", tm_defend),
    #                 # ToDo: defend
    #             (try_end),


    #         (try_end),

    #     ]),

    # script_troop_get_mission_party_size_multiplier
    # input:
    #   arg1: troop_no
    # output:
    #   reg0: party_size_multiplier
    # ("troop_get_mission_party_size_multiplier",
    #     [
    #         (store_script_param, ":troop_no", 1),
    #         (troop_get_slot, ":mission", ":troop_no", slot_troop_mission),

    #         (assign, ":mult", 100),

    #         (try_begin),
    #             (eq, ":mission", tm_none),
    #         (else_try),
    #             (eq, ":mission", tm_gather),
    #             (assign, ":mult", 90),
    #         (else_try),
    #             (eq, ":mission", tm_recruit),
    #         (else_try),
    #             (eq, ":mission", tm_prepare),
    #             (assign, ":mult", 80),
    #         (else_try),
    #             (eq, ":mission", tm_attack),
    #             (assign, ":mult", 60),
    #         (else_try),
    #             (eq, ":mission", tm_defend),
    #             (assign, ":mult", 70),
    #         # (else_try),
    #             # (eq, ":mission", tm_none),
    #         # (else_try),
    #         (try_end),

    #         (assign, reg0, ":mult"),
    #     ]),
    
    # script_party_process_mission
    # input:
    #   arg1: party_no
    #   arg2: force_process
    # output: none
    ("party_process_mission",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":force_process", 2),

            (party_get_slot, ":current_iteration", ":party_no", slot_party_process_mission_iteration),
            (val_add, ":current_iteration", 1),
            (try_begin),
                (this_or_next|eq, ":force_process", 1),
                (ge, ":current_iteration", process_mission_iteration_count),
                
                (party_get_slot, ":leader", ":party_no", slot_party_leader),
                
                (call_script, "script_troop_get_home", ":leader", 0),
                (assign, ":home", reg0),
                (call_script, "script_troop_get_home", ":leader", 1),
                (assign, ":walled_home", reg0),
                
                (troop_get_slot, ":old_mission", ":leader", slot_troop_mission),
                (troop_get_slot, ":old_mission_object", ":leader", slot_troop_mission_object),
                
                (assign, ":new_mission", tm_none),
                (assign, ":new_mission_object", -1),
                
                (store_faction_of_party, ":party_faction", ":party_no"),
                (faction_get_slot, ":at_war", ":party_faction", slot_faction_is_at_war),
                
                (troop_get_slot, ":rank", ":leader", slot_troop_rank),

                (party_get_slot, ":preparing_for_war", ":party_no", slot_party_preparing_for_war),
                (party_get_slot, ":prepared_for_war", ":party_no", slot_party_prepared_for_war),
                
                (try_begin),
                    (eq, "$g_disable_ai", 1),
                (else_try),
                    (eq, ":at_war", 0),

                    (try_begin),
                        (faction_slot_eq, ":party_faction", slot_faction_preparing_war, 0),
                        (party_set_slot, ":party_no", slot_party_prepared_for_war, 0),
                        (party_set_slot, ":party_no", slot_party_preparing_for_war, 0),
                        (assign, ":preparing_for_war", 0),
                        (assign, ":prepared_for_war", 0),
                    (else_try),
                        (eq, ":prepared_for_war", 0),
                        (party_set_slot, ":party_no", slot_party_preparing_for_war, 1),
                        (assign, ":preparing_for_war", 1),
                    (try_end),
                (else_try),
                    (eq, ":prepared_for_war", 0),
                    (eq, ":preparing_for_war", 0),
                    (party_set_slot, ":party_no", slot_party_preparing_for_war, 1),
                    (assign, ":preparing_for_war", 1),

                (else_try),
                    # Defend home
                    (ge, ":home", centers_begin),
                    (party_get_battle_opponent, ":attacker", ":home"),
                    (assign, ":stop", 0),
                    (try_begin),
                        (this_or_next|ge, ":attacker", 0),
                        (party_slot_ge, ":home", slot_party_besieged_by, 0),
                        
                        (try_begin),
                            (eq, ":old_mission", tm_defending),
                            (neq, ":old_mission_object", ":home"),
                            
                            (store_distance_to_party_from_party, ":home_distance", ":party_no", ":home"),
                            (store_distance_to_party_from_party, ":mission_object_distance", ":party_no", ":old_mission_object"),
                            
                            (try_begin), # Prefer to defend own territory
                                (neg|party_slot_eq, ":old_mission_object", slot_party_lord, ":leader"),
                                (val_mul, ":mission_object_distance", 2),
                                (val_div, ":mission_object_distance", 3),
                            (try_end),
                            
                            (le, ":mission_object_distance", ":home_distance"),
                            
                            (assign, ":new_mission", tm_defending),
                            (assign, ":new_mission_object", ":old_mission_object"),
                            (assign, ":stop", 1),
                        (else_try),
                            # (eq, ":home", ":walled_home"),
                            (assign, ":new_mission", tm_defending),
                            (assign, ":new_mission_object", ":home"),
                            (assign, ":stop", 1),
                        (try_end),
                    (else_try),
                        # Defend walled home
                        (neq, ":home", ":walled_home"),
                        
                        (party_get_battle_opponent, ":attacker", ":walled_home"),
                        (this_or_next|ge, ":attacker", 0),
                        (party_slot_ge, ":walled_home", slot_party_besieged_by, 0),
                        
                        (assign, ":new_mission", tm_defending),
                        (assign, ":new_mission_object", ":walled_home"),
                        (assign, ":stop", 1),
                    (try_end),
                    (eq, ":stop", 1),
                (else_try),
                    # Siege fiefs
                    (ge, ":rank", rank_castle),
                    (troop_get_slot, ":last_attack", ":leader", slot_troop_last_attack),
                    (store_current_hours, ":cur_hour"),
                    (store_sub, ":diff", ":cur_hour", ":last_attack"),
                    (ge, ":diff", 7*24),
                    (call_script, "script_faction_find_nearest_enemy_center", ":party_faction", ":party_no", spt_castle),
                    (assign, ":center", reg0),
                    (is_between, ":center", walled_centers_begin, walled_centers_end),
                    
                    (try_begin),
                        (party_get_slot, ":besieger", ":center", slot_party_besieged_by),
                        (ge, ":besieger", 0),
                        (neq, ":besieger", ":party_no"),
                        (party_get_slot, ":besieger_leader", ":besieger", slot_party_leader),
                        (assign, ":new_mission", tm_escorting),
                        (assign, ":new_mission_object", ":besieger_leader"),
                    (else_try),
                        (assign, ":new_mission", tm_attacking),
                        (assign, ":new_mission_object", ":center"),
                    (try_end),
                (try_end),
                
                (try_begin),
                    # Follow liege
                    (troop_get_slot, ":liege", ":leader", slot_troop_vassal_of),
                    (ge, ":liege", 0),
                    (troop_slot_eq, ":liege", slot_troop_gathering, 1),
                    (troop_get_slot, ":liege_party", ":liege", slot_troop_leaded_party),
                    
                    (ge, ":liege_party", 0),
                    # We don't follow liege if we are defending territory
                    (neq, ":new_mission", tm_defending),
                    # Or if we were following someone else already
                    (this_or_next|neq, ":old_mission", tm_escorting),
                    (eq, ":old_mission_object", ":liege"),

                    (try_begin),
                        # (neq, ":new_mission_object", ":home"),
                        # (troop_get_slot, ":liege_party", ":liege", slot_troop_leaded_party),
                        (assign, ":new_mission", tm_escorting),
                        (assign, ":new_mission_object", ":liege"),
                    (try_end),
                (try_end),

                (try_begin),
                    (call_script, "script_cf_party_need_troops", ":party_no"),
                    (assign, ":type", reg0),
                    (try_begin),
                        (this_or_next|ge, ":type", type_moderate),
                        (party_slot_eq, ":party_no", slot_party_preparing_for_war, 1),
                        (assign, ":new_mission", tm_none),
                    (try_end),
                (else_try),
                    (ge, ":at_war", 1),
                    (eq, ":preparing_for_war", 1),
                    (eq, ":prepared_for_war", 0),
                    (party_set_slot, ":party_no", slot_party_prepared_for_war, 1),
                    (assign, ":prepared_for_war", 1),
                    (party_set_slot, ":party_no", slot_party_preparing_for_war, 0),
                    (assign, ":preparing_for_war", 0),
                (try_end),
                
                (troop_get_slot, ":gathering", ":leader", slot_troop_gathering),
                (try_begin),
                    (ge, ":new_mission", tm_defending),
                    (try_begin),
                        (lt, ":gathering", 1),
                        (troop_set_slot, ":leader", slot_troop_gathering, 1),
                        (call_script, "script_party_gather_vassals", ":party_no"),
                    (try_end),
                (else_try),
                    (troop_set_slot, ":leader", slot_troop_gathering, -1),
                (try_end),
                
                (troop_set_slot, ":leader", slot_troop_mission, ":new_mission"),
                (troop_set_slot, ":leader", slot_troop_mission_object, ":new_mission_object"),
                (assign, ":current_iteration", 0),
            (try_end),

            (party_set_slot, ":party_no", slot_party_process_mission_iteration, ":current_iteration"),
        ]),

    # script_party_gather_vassals
    # input:
    #   arg1: party_gathering
    # output:
    #   reg0: num_gathered
    ("party_gather_vassals",
        [
            (store_script_param, ":party_no", 1),
            (store_faction_of_party, ":party_faction", ":party_no"),
            (party_get_slot, ":party_leader", ":party_no", slot_party_leader),
            (troop_get_slot, ":leader_rank", ":party_leader", slot_troop_rank),
            
            (assign, ":num_gathered", 0),
            
            (try_for_range, ":lord_no", lords_begin, lords_end),
                (troop_get_slot, ":lord_occupation", ":lord_no", slot_troop_kingdom_occupation),
                (is_between, ":lord_occupation", tko_kingdom_hero, tko_bandit),
                (store_troop_faction, ":lord_faction", ":lord_no"),
                (troop_get_slot, ":liege", ":lord_no", slot_troop_vassal_of),
                (troop_get_slot, ":lord_party", ":lord_no", slot_troop_leaded_party),
                
                (assign, ":follow_score", 0),
                (try_begin),
                    (eq, ":liege", ":party_leader"),
                    (val_add, ":follow_score", 100),
                (else_try),
                    (eq, ":lord_faction", ":party_faction"),
                    (val_add, ":follow_score", 50),
                (else_try),
                    (store_relation, ":faction_relation", ":lord_faction", ":party_faction"),
                    (try_begin),
                        (ge, ":faction_relation", relation_state_friendly),
                        (val_add, ":follow_score", 20),
                    (else_try),
                        (le, ":faction_relation", relation_state_conflict),
                        (val_add, ":follow_score", -100),
                    (else_try),
                        (le, ":faction_relation", relation_state_war),
                        (val_add, ":follow_score", -200),
                    (try_end),
                (try_end),
                
                (troop_get_slot, ":mission", ":lord_no", slot_troop_mission),
                (try_begin),
                    (eq, ":mission", tm_defending),
                    (val_add, ":follow_score", -25),
                (else_try),
                    (eq, ":mission", tm_attacking),
                    (val_add, ":follow_score", -10),
                (else_try),
                    (eq, ":mission", tm_escorting),
                    (val_add, ":follow_score", -50),
                (try_end),
                (try_begin),
                    (troop_slot_eq, ":lord_no", slot_troop_gathering, 1),
                    (val_add, ":follow_score", -50),
                (try_end),
                
                (ge, ":follow_score", 0),
                (try_begin),
                    (ge, ":lord_party", 0),
                    (store_distance_to_party_from_party, ":dist", ":party_no", ":lord_party"),
                    (store_sub, ":dist_score", 25, ":dist"),
                    (val_mul, ":dist_score", 2),
                (try_end),
                
                (troop_get_slot, ":lord_rank", ":lord_no", slot_troop_rank),
                (store_sub, ":rank_score", ":leader_rank", ":lord_rank"),
                (val_sub, ":rank_score", 1),
                (val_mul, ":rank_score", 5),
                
                (val_add, ":follow_score", ":dist_score"),
                (val_add, ":follow_score", ":rank_score"),
                
                (try_begin),
                    (ge, ":follow_score", 100),
                    (troop_set_slot, ":lord_no", slot_troop_mission, tm_escorting),
                    (troop_set_slot, ":lord_no", slot_troop_mission_object, ":party_leader"),
                (try_end),
            (try_end),
            
            (assign, reg0, ":num_gathered"),
        ]),
        
    # script_faction_find_nearest_enemy_center
    # input:
    #   arg1: faction_no
    #   arg2: party
    #   arg2: party_type
    # output:
    #   reg0: enemy_center
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
                    (lt, ":relation", relation_state_war),
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
                    (lt, ":relation", relation_state_war),
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
    #   arg1: troop_no
    #   arg2: troop_to_follow
    # output:
    #   reg0: follow (1: yes, 0: no)
    ("decide_follow_or_not",
        [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":troop_to_follow", 2),
            
            (assign, ":follow", 0),
            
            (troop_get_slot, ":party_to_follow", ":troop_to_follow", slot_troop_leaded_party),
            
            (try_begin),
                (ge, ":party_to_follow", 0),
                
                (try_begin),
                    (troop_slot_eq, ":troop_no", slot_troop_behavior, tai_accompanying_troop),
                    (troop_slot_eq, ":troop_no", slot_troop_behavior_object, ":troop_to_follow"),
                    
                    (assign, ":follow", 1),
                (else_try),
                    (troop_slot_ge, ":troop_to_follow", slot_troop_mission, 1), # Has a mission
                    (assign, ":follow", 0),
                (else_try),
                    (troop_slot_eq, ":troop_to_follow", slot_troop_behavior, tai_accompanying_troop),
                    (neg|troop_slot_eq, ":troop_to_follow", slot_troop_behavior_object, ":troop_no"),
                    (assign, ":follow", 0),
                (try_end),
            (try_end),
            
            (assign, reg0, ":follow"),
        ]),
    
    # script_party_does_center_business
    # input:
    #   arg1: party_no
    #   arg2: cur_town
    # output: none
    ("party_does_center_business",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":cur_town", 2),

            (store_faction_of_party, ":party_faction", ":party_no"),
            (store_faction_of_party, ":center_faction", ":cur_town"),
            (party_get_slot, ":leader", ":party_no", slot_party_leader),

            (try_begin),
                (eq, ":party_faction", ":center_faction"),
                (party_slot_eq, ":cur_town", slot_party_leader, ":leader"),

                # Moves prisoners to center (only if the same lord)
                (call_script, "script_party_give_prisoners_to_party", ":party_no", ":cur_town"),
                # Pay debts
                (call_script, "script_party_pay_debts", ":party_no"),
            (try_end),
            
            (call_script, "script_party_get_prefered_wages_limit", ":party_no"),
            (assign, ":limit", reg0),
            (assign, ":limit_max", reg2),
            (call_script, "script_party_get_wages", ":party_no"),
            (assign, ":wages", reg0),

            (try_begin),
                (gt, ":wages", ":limit_max"),
                # TODO: refine number of troops to give
                (call_script, "script_party_give_troops_to_party", ":party_no", ":cur_town", 10),
            (else_try),
                (lt, ":wages", ":limit"),
                
                (assign, ":num_reinforcements", 6),
                (party_get_num_companions, ":num_companions", ":party_no"),
                (try_begin),
                    (gt, ":num_companions", 0),
                    (store_div, ":average_cost", ":wages", ":num_companions"),

                    (gt, ":average_cost", 0),
                    (store_sub, ":diff", ":limit", ":wages"),
                    (store_div, ":target", ":diff", ":average_cost"),
                    (store_add, ":num_reinforcements", ":target", 3),
                (try_end),

                (val_max, ":num_reinforcements", 6),
                (val_min, ":num_reinforcements", 15),

                (call_script, "script_cf_center_can_give_troops", ":cur_town"),
                
                (try_begin),
                    (neg|party_slot_eq, ":cur_town", slot_party_lord, ":leader"),
                    (val_div, ":num_reinforcements", 2),
                (else_try),
                    (party_slot_eq, ":party_no", slot_party_preparing_for_war, 1),
                    (val_mul, ":num_reinforcements", 2),
                (try_end),
                (val_add, ":num_reinforcements", 2),
                
                (val_min, ":num_reinforcements", 18),
                (gt, ":num_reinforcements", 0),
                (call_script, "script_party_give_troops_to_party", ":cur_town", ":party_no", ":num_reinforcements"),
                # (assign, ":num_added", reg0),
                # ToDo: remove gold
            (try_end),

            (try_begin),
                (eq, ":party_faction", ":center_faction"),
                (party_slot_eq, ":cur_town", slot_party_leader, ":leader"),

                # Transfer gold to/from the center
                (call_script, "script_party_get_total_wealth", ":cur_town", 1),
                (assign, ":center_wealth", reg0),

                (call_script, "script_party_get_total_wealth", ":party_no", 1),
                (assign, ":total_party_wealth", reg0),

                (call_script, "script_party_get_wages", ":party_no"),
                (assign, ":party_wage", reg0),

                (store_div, ":min_wealth", ":party_wage", 2),
                (assign, ":max_wealth", ":party_wage"),

                (try_begin),
                    (lt, ":total_party_wealth", ":min_wealth"),
                    (store_div, ":amount", ":min_wealth", 2),
                    (try_begin),
                        (lt, ":total_party_wealth", 0),
                        (val_sub, ":amount", ":total_party_wealth"),
                    (try_end),
                    (store_div, ":max_transfer", ":center_wealth", 3), # We try to keep some gold inside center
                    (val_min, ":amount", ":max_transfer"),

                    (call_script, "script_move_gold_from_party_to_party", ":cur_town", ":party_no", ":amount"),
                (else_try),
                    (gt, ":total_party_wealth", ":max_wealth"),
                    (store_sub, ":amount", ":total_party_wealth", ":max_wealth"),
                    (store_div, ":transfer", ":party_wage", 4),
                    (val_add, ":amount", ":transfer"),

                    (call_script, "script_move_gold_from_party_to_party", ":party_no", ":cur_town", ":amount"),
                (try_end),
            (try_end),
        ]),

    # script_move_gold_from_party_to_party
    # input:
    #   arg1: party_from
    #   arg2: party_to
    #   arg3: amount
    # output:
    #   reg0: gold_moved
    ("move_gold_from_party_to_party",
        [
            (store_script_param, ":party_from", 1),
            (store_script_param, ":party_to", 2),
            (store_script_param, ":amount", 3),

            (call_script, "script_party_remove_gold", ":party_from", ":amount"),
            (assign, ":removed", reg0),
            (call_script, "script_party_receive_gold", ":party_to", ":removed"),

            (try_begin),
                (call_script, "script_cf_debug", debug_economy),
                (str_store_party_name, s10, ":party_from"),
                (str_store_party_name, s11, ":party_to"),
                (assign, reg10, ":amount"),
                (assign, reg11, ":removed"),
                (display_message, "@{s10} move gold to {s11} (wanted: {reg10} - real {reg11})"),
            (try_end),

            (assign, reg0, 0),
        ]),
    
    # script_party_set_behavior
    # input:
    #   arg1: party_no
    #   arg2: behavior
    #   arg3: object
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

            (assign, ":ai_behavior", ai_bhvr_patrol_location),
            
            (try_begin),
                (party_get_slot, ":leader", ":party_no",  slot_party_leader),
                (ge, ":leader", 0),
                (troop_set_slot, ":leader", slot_troop_behavior, ":behavior"),
                (troop_set_slot, ":leader", slot_troop_behavior_object, ":object"),
            (try_end),
            
            (try_begin),
                (eq, ":behavior", tai_patroling_center),
                (assign, ":ai_behavior", ai_bhvr_patrol_party),
                (party_set_ai_patrol_radius, ":party_no", 2),
                (assign, ":courage", 10),
                (assign, ":aggressiveness", 8),
                (assign, ":help", 200),
            (else_try),
                (eq, ":behavior", tai_patroling_party),
                (assign, ":ai_behavior", ai_bhvr_patrol_location),
                (party_set_ai_patrol_radius, ":party_no", 1),
                (assign, ":courage", 10),
                (assign, ":aggressiveness", 5),
                (assign, ":help", 100),
            (else_try),
                # Should only be used on hero parties
                (eq, ":behavior", tai_accompanying_troop),
                (troop_get_slot, ":to_follow", ":object", slot_troop_leaded_party),
                (ge, ":to_follow", 0),
                (assign, ":object", ":to_follow"),
                (assign, ":ai_behavior", ai_bhvr_escort_party),
                (assign, ":courage", 14),
                (assign, ":aggressiveness", 1),
                (assign, ":help", 500),
            (else_try),
                (eq, ":behavior", tai_accompanying_party),
                (assign, ":ai_behavior", ai_bhvr_escort_party),
                (assign, ":courage", 14),
                (assign, ":aggressiveness", 1),
                (assign, ":help", 500),
            (else_try),
                (eq, ":behavior", tai_traveling_to_party),
                (assign, ":ai_behavior", ai_bhvr_travel_to_party),
                (assign, ":courage", 10),
                (assign, ":aggressiveness", 1),
                (assign, ":help", 50),
            (else_try),
                (eq, ":behavior", tai_attacking_center),
                (party_get_position, pos1, ":object"),
                (map_get_land_position_around_position, pos2, pos1, 2),
                (assign, ":ai_behavior", ai_bhvr_travel_to_point),
                (party_set_ai_target_position, ":party_no", pos2),
                (assign, ":courage", 14),
                (assign, ":aggressiveness", 1),
                (assign, ":help", 150),
            (else_try),
                (eq, ":behavior", tai_traveling_to_point),
                (party_get_position, pos1, ":object"),
                (map_get_land_position_around_position, pos2, pos1, 2),
                (assign, ":ai_behavior", ai_bhvr_travel_to_point),
                (party_set_ai_target_position, ":party_no", pos2),
                (assign, ":courage", 10),
                (assign, ":aggressiveness", 1),
                (assign, ":help", 50),
            (else_try),
                (assign, ":ai_behavior", ai_bhvr_patrol_location),
                (party_set_ai_patrol_radius, ":party_no", 1),
                (assign, ":object", -1),
                (assign, ":courage", 10),
                (assign, ":aggressiveness", 5),
                (assign, ":help", 100),
                (str_store_party_name, s10, ":party_no"),
                (display_debug_message, "@ERROR: Invalid party_set_behavior for party {s10}", text_color_impossible),
            (try_end),

            
            (party_set_aggressiveness, ":party_no", ":aggressiveness"),
            (party_set_courage, ":party_no", ":courage"),
            (party_set_helpfulness, ":party_no", ":help"),
            
            (party_set_ai_object, ":party_no", ":object"),
            (party_set_ai_behavior, ":party_no", ":ai_behavior"),
        ]),
    
    # script_party_recruit_troops
    # input:
    #   arg1: party_no
    # output:
    #   reg0: num_recruited
    ("party_recruit_troops",
        [
            (store_script_param, ":party_no", 1),
            
            (call_script, "script_party_get_prefered_wages_limit", ":party_no"),
            (assign, ":limit", reg0),
            (assign, ":lower_limit", reg1),

            (call_script, "script_party_get_wages", ":party_no"),
            (assign, ":wages", reg0),
            
            (party_get_num_companions, ":num_troops", ":party_no"),
            (try_begin),
                (lt, ":wages", ":limit"),
                (neg|party_slot_ge, ":party_no", slot_party_besieged_by, 0),
                
                (call_script, "script_party_add_reinforcements", ":party_no"),

                (store_mul, ":gold_cost", reg1, -1),

                (call_script, "script_party_modify_wealth", ":party_no", ":gold_cost"),

                (try_begin),
                    # We do not want to buy expensive troops from other centers when we don't need it
                    (neg|party_slot_eq, ":party_no", slot_party_type, spt_village),
                    (lt, ":wages", ":lower_limit"),
                    (call_script, "script_party_ask_reinforcements", ":party_no"),
                (try_end),
                # (call_script, "script_party_add_troops_with_buildings", ":party_no"),
            (try_end),
            (party_get_num_companions, ":new_num_troops", ":party_no"),
            
            (store_sub, ":num_recruited", ":new_num_troops", ":num_troops"),
            
            (assign, reg0, ":num_recruited"),
        ]),

    # script_party_ask_reinforcements
    # input:
    #   arg1: party_no
    # output:
    #   reg0: total_troops_coming
    #   reg1: total_cost
    ("party_ask_reinforcements",
        [
            (store_script_param, ":party_no", 1),
            (store_faction_of_party, ":party_faction", ":party_no"),

            (call_script, "script_party_get_prefered_wages_limit", ":party_no"),
            (assign, ":limit", reg0),
            (call_script, "script_party_get_wages", ":party_no"),
            (assign, ":wages", reg0),

            (store_mul, ":percentage", ":wages", 100),
            (val_div, ":percentage", ":limit"),
            (store_sub, ":base_score", 100, ":percentage"),

            # Wealthy centers can ask for more reinforcements
            (party_get_slot, ":wealth_score", ":party_no", slot_party_wealth),
            (val_div, ":wealth_score", 200),
            (val_min, ":wealth_score", 50),

            (assign, ":num_troops_coming", 0),
            (assign, ":troops_cost", 0),

            # ToDo: refine average score
            (assign, ":average_score", 100),
            (assign, ":best_center", -1),
            (assign, ":best_score", -1),
            (assign, ":best_modifier", -1),
            (assign, ":asked", 0),
            (try_for_range, ":center_no", centers_begin, centers_end),
                (neq, ":center_no", ":party_no"),
                (store_faction_of_party, ":center_faction", ":center_no"),
                # ToDo: Allow allies with reduced likelyness
                (eq, ":center_faction", ":party_faction"),

                (assign, ":continue", 0),
                (party_get_slot, ":center_type", ":center_no", slot_party_type),
                (try_begin),
                    (eq, ":center_type", spt_village),

                    (party_get_slot, ":linked_center", ":center_no", slot_party_linked_party),
                    (try_begin),
                        (eq, ":linked_center", ":party_no"),
                        (assign, ":continue", 1),
                    (else_try),
                        (store_faction_of_party, ":linked_center_faction", ":linked_center"),
                        (neq, ":linked_center_faction", ":center_faction"),
                        (assign, ":continue", 1),
                    (try_end),
                (else_try),
                    (assign, ":continue", 1),
                (try_end),
                (eq, ":continue", 1),
                # Nearby centers are more likely to send troops at a lower price
                (store_distance_to_party_from_party, ":dist", ":party_no", ":center_no"),
                (val_div, ":dist", 10),
                (store_sub, ":dist_score", 30, ":dist"),
                (val_min, ":dist_score", 30),

                (call_script, "script_cf_party_get_reinforcement_price_modifier", ":center_no"),
                (assign, ":price_modifier", reg0),
                # High prices reduce chance to buy
                (store_div, ":price_score", ":price_modifier", 10),
                (store_sub, ":price_score", 100, ":price_score"),

                (store_add, ":total_score", ":base_score", ":wealth_score"),
                (val_add, ":total_score", ":dist_score"),
                (val_add, ":total_score", ":price_score"),

                # We add some noise
                (store_random_in_range, ":rand", -10, 11),

                (val_add, ":total_score", ":rand"),

                (assign, ":buy", 0),
                (try_begin),
                    (ge, ":total_score", ":average_score"),
                    (assign, ":buy", 1),
                (else_try),
                    (le, ":dist_score", 10),
                    # Very close centers are given an advantage
                    (store_mul, ":score", ":average_score", 90),
                    (val_div, ":score", 100),
                    (ge, ":total_score", ":score"),
                    (assign, ":buy", 1),
                (try_end),

                (try_begin),
                    (eq, ":buy", 1),
                    # Ask for troops

                    (store_div, ":num_men", ":total_score", 20),
                    (ge, ":num_men", 5),

                    (call_script, "script_party_send_reinforcements", ":center_no", ":party_no", ":num_men"),
                    (assign, ":num_sent", reg0),
                    (assign, ":cost", reg1),

                    (val_mul, ":cost", ":price_modifier"),
                    (val_div, ":cost", 100),

                    (val_add, ":num_troops_coming", ":num_sent"),
                    (val_add, ":troops_cost", ":cost"),

                    (val_mul, ":num_sent", 3),
                    (val_sub, ":base_score", ":num_sent"),

                    (val_add, ":asked", 1),
                (try_end),

                (try_begin),
                    (gt, ":best_score", ":total_score"),
                    (assign, ":best_score", ":total_score"),
                    (assign, ":best_center", ":center_no"),
                    (assign, ":best_modifier", ":price_modifier"),
                (try_end),
            (try_end),
            (try_begin),
                (ge, ":best_score", 0),
                (try_begin),
                    (call_script, "script_cf_debug", debug_simple|debug_war),
                    (str_store_party_name, s10, ":best_center"),
                    (str_store_party_name, s11, ":party_no"),
                    (assign, reg10, ":best_score"),
                    (display_message, "@{s10} is the best center for {s11} : {reg10}."),
                (try_end),
                # Best center has a greater number of troops sent
                (store_div, ":num_men", ":total_score", 10),
                (ge, ":num_men", 5),

                (call_script, "script_party_send_reinforcements", ":party_no", ":center_no", ":num_men"),
                (val_add, ":num_troops_coming", reg0),
                (assign, ":cost", reg1),

                (val_mul, ":cost", ":best_modifier"),
                (val_div, ":cost", 100),

                (val_add, ":troops_cost", ":cost"),
            (try_end),
            (assign, reg0, ":num_troops_coming"),
            (assign, reg1, ":troops_cost"),
        ]),

    # script_cf_party_get_reinforcement_price_modifier
        # input:
        #   arg1: party_no
        # output:
        #   reg0: price_modifier
        # fails if center cannot send troops
    ("cf_party_get_reinforcement_price_modifier",
        [
            (store_script_param, ":party_no", 1),

            (call_script, "script_party_get_prefered_wages_limit", ":party_no"),
            (assign, ":limit", reg1),
            (call_script, "script_party_get_wages", ":party_no"),
            (assign, ":wages", reg0),

            (gt, ":wages", ":limit"),
            (store_mul, ":modifier", ":limit", 200),
            (val_div, ":modifier", ":wages"),

            (val_mul, ":modifier", ":modifier"),
            (val_div, ":modifier", 100),

            (assign, reg0, ":modifier"),
        ]),
    
    # script_era_get_troops_multiplier
        # input:
        #   arg1: era_no
        # output:
        #   reg0: peasant_mult
        #   reg1: common_mult
        #   reg2: veteran_mult
        #   reg3: elite_mult
        #   reg4: noble_mult
    ("era_get_troops_multiplier",
        [
            (store_script_param, ":era", 1),
            (try_begin),
                (eq, ":era", 0),
                (assign, reg0, 400),
                (assign, reg1, 40),
                (assign, reg2, 5),
                (assign, reg3, 0),
                (assign, reg4, 0),
            (else_try),
                (eq, ":era", 1),
                (assign, reg0, 320),
                (assign, reg1, 80),
                (assign, reg2, 10),
                (assign, reg3, 0),
                (assign, reg4, 1),
            (else_try),
                (eq, ":era", 2),
                (assign, reg0, 240),
                (assign, reg1, 100),
                (assign, reg2, 15),
                (assign, reg3, 0),
                (assign, reg4, 2),
            (else_try),
                (eq, ":era", 3),
                (assign, reg0, 180),
                (assign, reg1, 95),
                (assign, reg2, 20),
                (assign, reg3, 3),
                (assign, reg4, 4),
            (else_try),
                (eq, ":era", 4),
                (assign, reg0, 120),
                (assign, reg1, 90),
                (assign, reg2, 24),
                (assign, reg3, 6),
                (assign, reg4, 5),
            (else_try),
                (eq, ":era", 5),
                (assign, reg0, 70),
                (assign, reg1, 80),
                (assign, reg2, 28),
                (assign, reg3, 8),
                (assign, reg4, 6),
            (else_try),
                (eq, ":era", 6),
                (assign, reg0, 40),
                (assign, reg1, 65),
                (assign, reg2, 30),
                (assign, reg3, 10),
                (assign, reg4, 7),
            (else_try),
                (eq, ":era", 7),
                (assign, reg0, 20),
                (assign, reg1, 50),
                (assign, reg2, 32),
                (assign, reg3, 12),
                (assign, reg4, 8),
            (else_try),
                (eq, ":era", 8),
                (assign, reg0, 10),
                (assign, reg1, 35),
                (assign, reg2, 34),
                (assign, reg3, 14),
                (assign, reg4, 9),
            (else_try),
                (eq, ":era", 9),
                (assign, reg0, 5),
                (assign, reg1, 25),
                (assign, reg2, 35),
                (assign, reg3, 15),
                (assign, reg4, 10),
            (else_try),
                (eq, ":era", 10),
                (assign, reg0, 2),
                (assign, reg1, 15),
                (assign, reg2, 35),
                (assign, reg3, 18),
                (assign, reg4, 12),
            (else_try),
                (assign, reg10, ":era"),
                (display_debug_message, "@Error, incorrect era {reg10}!", text_color_impossible),
                (assign, reg0, 8),
                (assign, reg1, 10),
                (assign, reg2, 5),
                (assign, reg3, 2),
                (assign, reg4, 1),
            (try_end),
        ]),
        
    # script_faction_get_troops_modifier
        # input:
        #   arg1: faction_no
        # output:
        #   reg0: peasant_mult
        #   reg1: common_mult
        #   reg2: veteran_mult
        #   reg3: elite_mult
        #   reg4: noble_mult
    ("faction_get_troops_modifier",
        [
            (store_script_param, ":faction_no", 1),
            
            (faction_get_slot, ":era", ":faction_no", slot_faction_era),
            (faction_get_slot, ":era_time", ":faction_no", slot_faction_era_time),
            
            (assign, ":peasant_mult", 0),
            (assign, ":common_mult", 0),
            (assign, ":veteran_mult", 0),
            (assign, ":elite_mult", 0),
            (assign, ":noble_mult", 0),
            
            (try_begin),
                (eq, ":era", 0),
                (call_script, "script_era_get_troops_multiplier", 0),
                (assign, ":peasant_mult", reg0),
                (assign, ":common_mult", reg1),
                (assign, ":veteran_mult", reg2),
                (assign, ":elite_mult", reg3),
                (assign, ":noble_mult", reg4),
            (else_try),
                (call_script, "script_era_get_troops_multiplier", ":era"),
                (assign, ":peasant_mult", reg0),
                (assign, ":common_mult", reg1),
                (assign, ":veteran_mult", reg2),
                (assign, ":elite_mult", reg3),
                (assign, ":noble_mult", reg4),
                (store_current_day, ":current_time"),
                (store_sub, ":time_passed", ":current_time", ":era_time"),
                (try_begin),
                    (lt, ":time_passed", era_minimum_duration),
                    (store_sub, ":old_era", ":era", 1),
                    (store_sub, ":time_left", ":time_passed", era_minimum_duration),
                    (call_script, "script_era_get_troops_multiplier", ":old_era"),
                    (assign, ":peasant_old_mult", reg0),
                    (assign, ":common_old_mult", reg1),
                    (assign, ":veteran_old_mult", reg2),
                    (assign, ":elite_old_mult", reg3),
                    (assign, ":noble_old_mult", reg4),
                    
                    (val_mul, ":peasant_mult", ":time_passed"),
                    (val_mul, ":common_mult", ":time_passed"),
                    (val_mul, ":veteran_mult", ":time_passed"),
                    (val_mul, ":elite_mult", ":time_passed"),
                    (val_mul, ":noble_mult", ":time_passed"),
                    
                    (val_mul, ":peasant_old_mult", ":time_left"),
                    (val_mul, ":common_old_mult", ":time_left"),
                    (val_mul, ":veteran_old_mult", ":time_left"),
                    (val_mul, ":elite_old_mult", ":time_left"),
                    (val_mul, ":noble_old_mult", ":time_left"),
                    
                    (val_add, ":peasant_mult", ":peasant_old_mult"),
                    (val_add, ":common_mult", ":common_old_mult"),
                    (val_add, ":veteran_mult", ":veteran_old_mult"),
                    (val_add, ":elite_mult", ":elite_old_mult"),
                    (val_add, ":noble_mult", ":noble_old_mult"),
                    
                    (val_div, ":peasant_mult", era_minimum_duration),
                    (val_div, ":common_mult", era_minimum_duration),
                    (val_div, ":veteran_mult", era_minimum_duration),
                    (val_div, ":elite_mult", era_minimum_duration),
                    (val_div, ":noble_mult", era_minimum_duration),
                (try_end),
            (try_end),
        ]),

    # script_faction_apply_assimilation
        # input:
        #   arg1: faction_no
        #   arg2: original_faction
        # output:
        #   reg0: output_faction
    ("faction_apply_assimilation",
        [
            (store_script_param, ":faction_no", 1),
            (store_script_param, ":original_faction", 2),

            (assign, ":continue", 0),

            (faction_get_slot, ":assimilation_type", ":faction_no", slot_faction_policy_assimilation),
            (try_begin),
                (eq, ":assimilation_type", sfpa_total),
                (assign, ":continue", 0),
            (else_try),
                (eq, ":assimilation_type", sfpa_partial),

                (faction_get_slot, ":faction_culture", ":faction_no", slot_faction_culture),
                (faction_get_slot, ":original_faction_culture", ":original_faction", slot_faction_culture),

                (eq, ":faction_culture", ":original_faction_culture"),
                (assign, ":continue", 1),
            (else_try),
                (eq, ":assimilation_type", sfpa_none),
                (assign, ":continue", 1),
            (try_end),

            (try_begin),
                (eq, ":continue", 1),
                (assign, reg0, ":original_faction"),
            (else_try),
                (assign, reg0, ":faction_no"),
            (try_end),
        ]),
    
    # script_party_add_reinforcements
        # input:
        #   arg1: party_no
        # output:
        #   reg0: num_added
        #   reg1: total_cost
    ("party_add_reinforcements",
        [
            (store_script_param, ":party_no", 1),
            (store_faction_of_party, ":faction", ":party_no"),
            (party_get_slot, ":original_faction", ":party_no", slot_party_original_faction),

            (call_script, "script_faction_apply_assimilation", ":faction", ":original_faction"),
            (assign, ":faction", reg0),

            (faction_get_slot, ":culture", ":faction", slot_faction_culture),
            
            (call_script, "script_faction_get_troops_modifier", ":faction"),
            (assign, ":num_peasant", reg0),
            (assign, ":num_common", reg1),
            (assign, ":num_veteran", reg2),
            (assign, ":num_elite", reg3),
            (assign, ":num_noble", reg4),
            
            (party_get_slot, ":party_type", ":party_no", slot_party_type),
            (try_begin),
                (eq, ":party_type", spt_village),
                (val_mul, ":num_peasant", 4),   # 400%
                (val_div, ":num_common", 2),    # 50%
                (val_div, ":num_veteran", 10),  # 10%
                (val_mul, ":num_elite", 0),     # 0%
                (val_mul, ":num_noble", 0),     # 0%
            (else_try),
                (eq, ":party_type", spt_town),
                (val_mul, ":num_peasant", 3),   # 150%
                (val_div, ":num_peasant", 2),
                (val_mul, ":num_common", 5),    # 125%
                (val_div, ":num_common", 4),
                (val_mul, ":num_veteran", 3),   # 75%
                (val_div, ":num_veteran", 4),
                (val_mul, ":num_elite", 11),    # 110%
                (val_div, ":num_elite", 10),
                (val_mul, ":num_noble", 3),     # 150%
                (val_div, ":num_noble", 2),
            (else_try),
                (eq, ":party_type", spt_castle),
                (val_mul, ":num_peasant", 3),   # 75%
                (val_div, ":num_peasant", 4),
                (val_mul, ":num_common", 9),    # 90%
                (val_div, ":num_common", 10),
                # (val_mul, ":num_veteran", 1),   # 100%
                # (val_mul, ":num_elite", 1),     # 100%
                (val_mul, ":num_noble", 9),     # 90%
                (val_div, ":num_noble", 10),
            (try_end),
            
            (faction_get_slot, ":peasant_mod", ":faction", slot_faction_peasant_num_tries),
            (faction_get_slot, ":common_mod", ":faction", slot_faction_common_num_tries),
            (faction_get_slot, ":veteran_mod", ":faction", slot_faction_veteran_num_tries),
            (faction_get_slot, ":elite_mod", ":faction", slot_faction_elite_num_tries),
            (faction_get_slot, ":noble_mod", ":faction", slot_faction_noble_num_tries),
            
            (store_mul, ":faction_peasant", ":num_peasant", ":peasant_mod"),
            (store_mul, ":faction_common", ":num_common", ":common_mod"),
            (store_mul, ":faction_veteran", ":num_veteran", ":veteran_mod"),
            (store_mul, ":faction_elite", ":num_elite", ":elite_mod"),
            (store_mul, ":faction_noble", ":num_noble", ":noble_mod"),
            (val_div, ":faction_peasant", 100),
            (val_div, ":faction_common", 100),
            (val_div, ":faction_veteran", 100),
            (val_div, ":faction_elite", 100),
            (val_div, ":faction_noble", 100),
            
            (val_add, ":num_peasant", ":faction_peasant"),
            (val_add, ":num_common", ":faction_common"),
            (val_add, ":num_veteran", ":faction_veteran"),
            (val_add, ":num_elite", ":faction_elite"),
            (val_add, ":num_noble", ":faction_noble"),
            
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
            (store_random_in_range, ":random", 0, ":noble_max"),
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
        #   arg1: party_no
        #   arg2: begin of troops to add
        #   arg3: end of troops to add
        #   arg4: number of troops to add
        # output:
        #   reg0: num_added
        #   reg1: total_cost
    ("party_add_troops",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":begin", 2),
            (store_script_param, ":end", 3),
            (store_script_param, ":num_tries", 4),
            
            (store_faction_of_party, ":faction", ":party_no"),
            (party_get_slot, ":original_faction", ":party_no", slot_party_original_faction),

            (call_script, "script_faction_apply_assimilation", ":faction", ":original_faction"),
            (assign, ":faction", reg0),
            
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
                        
                        (store_sub, ":mul", 60, ":distance"),
                        
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
                            (store_sub, ":mul", 60, ":distance"),
                            
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
                        (try_begin),
                            (call_script, "script_cf_debug", debug_simple),
                            (display_message, "@Unable to add troop"),
                        (try_end),
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
    
    # script_party_send_reinforcements
    # input:
    #   arg1: party_no
    #   arg2: party_to_send_to
    #   arg3: optimal_number_to_send
    # output:
    #   reg0: num_sent
    #   reg1: base_troop_cost
    ("party_send_reinforcements",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":linked_center", 2),
            (store_script_param, ":num_troops", 3),
            
            (assign, ":num_sent", 0),
            (assign, ":total_cost", 0),
            
            (try_begin),
                (store_faction_of_party, ":faction", ":party_no"),
                (store_faction_of_party, ":linked_faction", ":linked_center"),
                (eq, ":faction", ":linked_faction"),
                
                (call_script, "script_spawn_party_around_party", ":party_no", "pt_reinforcements"),
                (assign, ":spawned_party", reg0),
                
                (party_set_faction, ":spawned_party", ":faction"),
            
                (call_script, "script_party_give_troops_to_party", ":party_no", ":spawned_party", ":num_troops"),
                
                (val_add, ":num_sent", reg0),
                (val_add, ":total_cost", reg1),

                (call_script, "script_party_create_debt", ":linked_center", ":party_no", ":total_cost"),
                
                (party_set_slot, ":spawned_party", slot_party_type, spt_convoy),
                (party_set_slot, ":spawned_party", slot_party_mission, spm_reinforce),
                (party_set_slot, ":spawned_party", slot_party_mission_object, ":linked_center"),
                
                (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
                (party_set_ai_object, ":spawned_party", ":linked_center"),
                
                (try_begin),
                    (eq, ":num_sent", 0),
                    (remove_party, ":spawned_party"),
                (else_try),
                    (call_script, "script_cf_debug", debug_faction),
                    (str_store_party_name, s10, ":party_no"),
                    (str_store_party_name, s11, ":linked_center"),
                    (assign, reg10, ":num_sent"),
                    (assign, reg11, ":total_cost"),
                    (call_script, "script_game_get_money_text", reg11),
                    (display_message, "@{s10} sends {reg10} men to {s11} ({s0})."),
                (try_end),
            (try_end),
            
            (assign, reg0, ":num_sent"),
            (assign, reg1, ":total_cost"),
        ]),
    
    # script_party_give_troops_to_party
    # input:
    #   arg1: giver_party
    #   arg2: receiver_party
    #   arg3: num_troops
    # output:
    #   reg0: num_added
    #   reg1: base_troop_cost
    ("party_give_troops_to_party",
        [
            (store_script_param, ":giver_party", 1),
            (store_script_param, ":receiver_party", 2),
            (store_script_param, ":num_troops", 3),
            
            (assign, ":num_added", 0),
            (assign, ":total_cost", 0),
            
            (party_get_slot, ":receiver_party_type", ":receiver_party", slot_party_type),
            (party_get_slot, ":giver_party_type", ":giver_party", slot_party_type),
            (try_begin),
                (eq, ":receiver_party_type", spt_war_party),
                (party_get_slot, ":leader", ":receiver_party", slot_party_leader),
                (party_get_slot, ":giver_leader", ":giver_party", slot_party_lord),
                (assign, ":priority", -1),
                (try_begin),
                    (eq, ":leader", ":giver_leader"),
                    (call_script, "script_party_give_troops_to_party_priority", ":giver_party", ":receiver_party", ":num_troops", -1, 0),
                    (val_add, ":num_added", reg0),
                    (val_add, ":total_cost", reg1),
                (else_try),
                    (troop_get_slot, ":leader_rank", ":leader", slot_troop_rank),
                    (try_begin),
                        (le, ":leader_rank", rank_affiliated),
                        (assign, ":priority", tq_peasant),
                    (else_try),
                        (le, ":leader_rank", rank_two_village),
                        (assign, ":priority", tq_veteran),
                    (else_try),
                        (assign, ":priority", tq_elite),
                    (try_end),
                    (call_script, "script_party_give_troops_to_party_priority", ":giver_party", ":receiver_party", ":num_troops", ":priority", 0),
                    (val_add, ":num_added", reg0),
                    (val_add, ":total_cost", reg1),
                (try_end),
            (else_try),
                (eq, ":giver_party_type", spt_war_party),
                (is_between, ":receiver_party_type", spt_village, spt_fort+1),
                (call_script, "script_party_give_troops_to_party_priority", ":giver_party", ":receiver_party", ":num_troops", tq_veteran, 0),
                (val_add, ":num_added", reg0),
                (val_add, ":total_cost", reg1),
            (else_try),
                # (eq, ":receiver_party_type", spt_convoy),
                (call_script, "script_party_give_troops_to_party_priority", ":giver_party", ":receiver_party", ":num_troops", tq_veteran, 0),
                (val_add, ":num_added", reg0),
                (val_add, ":total_cost", reg1),
            # (else_try),
                # (call_script, "script_party_give_troops_to_party_priority", ":giver_party", ":receiver_party", ":num_troops", 10, 0),
            (try_end),
            
            (assign, reg0, ":num_added"),
            (assign, reg1, ":total_cost"),
        ]),
    
    # script_party_give_troops_to_party_priority
    # input:
    #   arg1: giver_party
    #   arg2: receiver_party
    #   arg3: num_to_transfer
    #   arg4: priority
    #   arg5: move_heroes
    # output:
    #   reg0: num_transfered
    #   reg1: base_troop_cost
    ("party_give_troops_to_party_priority",
        [
            (store_script_param, ":giver_party", 1),
            (store_script_param, ":receiver_party", 2),
            (store_script_param, ":num_troops", 3),
            (store_script_param, ":priority", 4),
            (store_script_param, ":move_heroes", 5),
            
            (assign, ":num_added", 0),
            (assign, ":total_cost", 0),
            
            (party_get_num_companion_stacks, ":num_stacks", ":giver_party"),
            (assign, ":cur_value", 0),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":cur_troop", ":giver_party", ":cur_stack"),
                (this_or_next|neg|troop_is_hero, ":cur_troop"),
                (eq, ":move_heroes", 1),
                (troop_get_slot, ":troop_quality", ":cur_troop", slot_troop_quality),
                (assign, ":value", 2),
                (try_begin),
                    (gt, ":troop_quality", ":priority"),
                    # (assign, ":value", -1),
                    # Assign last value
                    (troop_set_slot, ":cur_troop", slot_troop_temp_slot, ":cur_value"),
                (else_try),
                    (party_stack_get_size, ":stack_size", ":giver_party", ":cur_stack"),
                    (val_mul, ":value", ":stack_size"),
                    (try_begin),
                        (eq, ":troop_quality", ":priority"),
                        (val_div, ":value", 2),
                    (else_try),
                        (eq, ":priority", -1),
                        (try_begin),
                            (eq, ":troop_quality", tq_peasant),
                            (val_div, ":value", 6),
                        (else_try),
                            (eq, ":troop_quality", tq_common),
                            (val_div, ":value", 3),
                        (try_end),
                    (try_end),
                    (val_add, ":cur_value", ":value"),
                    (troop_set_slot, ":cur_troop", slot_troop_temp_slot, ":cur_value"),
                (try_end),
            (try_end),
            
            (try_for_range, ":unused", 0, ":num_troops"),
                (party_get_num_companion_stacks, ":num_stacks", ":giver_party"),
                (store_sub, ":last_stack", ":num_stacks", 1),
                (ge, ":last_stack", 0),
                (party_stack_get_troop_id, ":last_troop", ":giver_party", ":last_stack"),
                (this_or_next|neg|troop_is_hero, ":last_troop"),
                (eq, ":move_heroes", 1),
                (troop_get_slot, ":max_rand", ":last_troop", slot_troop_temp_slot),
                (store_random_in_range, ":rand", 0, ":max_rand"),
                (try_for_range, ":cur_stack", 0, ":num_stacks"),
                    (party_stack_get_troop_id, ":cur_troop", ":giver_party", ":cur_stack"),
                    (this_or_next|neg|troop_is_hero, ":cur_troop"),
                    (eq, ":move_heroes", 1),
                    (troop_get_slot, ":value", ":cur_troop", slot_troop_temp_slot),
                    (try_begin),
                        # (neq, ":value", -1),
                        (lt, ":rand", ":value"),
                        
                        (party_add_members, ":receiver_party", ":cur_troop", 1),
                        (val_add, ":num_added", reg0),
                        (party_remove_members, ":giver_party", ":cur_troop", reg0),
                        (assign, ":num_stacks", 0),
                        (call_script, "script_troop_get_cost", ":cur_troop"),
                        (val_add, ":total_cost", reg0),
                    (try_end),
                (try_end),
            (try_end),
            
            (try_begin),
                (lt, ":num_added", ":num_troops"),
                (val_sub, ":num_troops", ":num_added"),
                (call_script, "script_party_give_troops_to_party_priority", ":giver_party", ":receiver_party", ":num_troops", 10, 0),
                (val_add, ":num_added", reg0),
            (try_end),
            
            (assign, reg0, ":num_added"),
            (assign, reg1, ":total_cost"),
        ]),
    
    # script_party_modify_population
    # input:
    #   arg1: party_no
    #   arg2: value
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
    #   arg1: party_no
    #   arg2: value
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
            (item_set_slot, "itm_building_hunter_camp", slot_building_cost_wood, 420),
            (item_set_slot, "itm_building_hunter_camp", slot_building_cost_stone, 0),
            (item_set_slot, "itm_building_hunter_camp", slot_building_cost_gold, 2000),
            (item_set_slot, "itm_building_hunter_camp", slot_building_build_time, 240),
            
            (item_set_slot, "itm_building_woodcutter_camp", slot_building_cost_wood, 260),
            (item_set_slot, "itm_building_woodcutter_camp", slot_building_cost_stone, 0),
            (item_set_slot, "itm_building_woodcutter_camp", slot_building_cost_gold, 3600),
            (item_set_slot, "itm_building_woodcutter_camp", slot_building_build_time, 300),
            
            (item_set_slot, "itm_building_mill", slot_building_cost_wood, 280),
            (item_set_slot, "itm_building_mill", slot_building_cost_stone, 220),
            (item_set_slot, "itm_building_mill", slot_building_cost_gold, 2500),
            (item_set_slot, "itm_building_mill", slot_building_build_time, 360),
            
            (item_set_slot, "itm_building_fish_pond", slot_building_cost_wood, 380),
            (item_set_slot, "itm_building_fish_pond", slot_building_cost_stone, 0),
            (item_set_slot, "itm_building_fish_pond", slot_building_cost_gold, 3000),
            (item_set_slot, "itm_building_fish_pond", slot_building_build_time, 280),
            
            (item_set_slot, "itm_building_mine", slot_building_cost_wood, 140),
            (item_set_slot, "itm_building_mine", slot_building_cost_stone, 0),
            (item_set_slot, "itm_building_mine", slot_building_cost_gold, 8000),
            (item_set_slot, "itm_building_mine", slot_building_build_time, 600),
            
            (item_set_slot, "itm_building_stone_pit", slot_building_cost_wood, 100),
            (item_set_slot, "itm_building_stone_pit", slot_building_cost_stone, 0),
            (item_set_slot, "itm_building_stone_pit", slot_building_cost_gold, 4000),
            (item_set_slot, "itm_building_stone_pit", slot_building_build_time, 480),
            
            (item_set_slot, "itm_building_cattle_ranch", slot_building_cost_wood, 220),
            (item_set_slot, "itm_building_cattle_ranch", slot_building_cost_stone, 160),
            (item_set_slot, "itm_building_cattle_ranch", slot_building_cost_gold, 2200),
            (item_set_slot, "itm_building_cattle_ranch", slot_building_build_time, 220),
            
            (item_set_slot, "itm_building_farm", slot_building_cost_wood, 140),
            (item_set_slot, "itm_building_farm", slot_building_cost_stone, 40),
            (item_set_slot, "itm_building_farm", slot_building_cost_gold, 2000),
            (item_set_slot, "itm_building_farm", slot_building_build_time, 320),
            
            (item_set_slot, "itm_building_slaver", slot_building_cost_wood, 120),
            (item_set_slot, "itm_building_slaver", slot_building_cost_stone, 50),
            (item_set_slot, "itm_building_slaver", slot_building_cost_gold, 3000),
            (item_set_slot, "itm_building_slaver", slot_building_build_time, 260),
            
            (item_set_slot, "itm_building_market", slot_building_cost_wood, 320),
            (item_set_slot, "itm_building_market", slot_building_cost_stone, 80),
            (item_set_slot, "itm_building_market", slot_building_cost_gold, 3400),
            (item_set_slot, "itm_building_market", slot_building_build_time, 360),
            
            (item_set_slot, "itm_building_market_2", slot_building_cost_wood, 480),
            (item_set_slot, "itm_building_market_2", slot_building_cost_stone, 120),
            (item_set_slot, "itm_building_market_2", slot_building_cost_gold, 5100),
            (item_set_slot, "itm_building_market_2", slot_building_build_time, 540),
            
            (item_set_slot, "itm_building_fields", slot_building_cost_wood, 120),
            (item_set_slot, "itm_building_fields", slot_building_cost_stone, 20),
            (item_set_slot, "itm_building_fields", slot_building_cost_gold, 4000),
            (item_set_slot, "itm_building_fields", slot_building_build_time, 480),
            
            (item_set_slot, "itm_building_tannery", slot_building_cost_wood, 200),
            (item_set_slot, "itm_building_tannery", slot_building_cost_stone, 200),
            (item_set_slot, "itm_building_tannery", slot_building_cost_gold, 5000),
            (item_set_slot, "itm_building_tannery", slot_building_build_time, 280),
            
            (item_set_slot, "itm_building_tavern", slot_building_cost_wood, 280),
            (item_set_slot, "itm_building_tavern", slot_building_cost_stone, 180),
            (item_set_slot, "itm_building_tavern", slot_building_cost_gold, 2800),
            (item_set_slot, "itm_building_tavern", slot_building_build_time, 240),
            
            (item_set_slot, "itm_building_militia_camp", slot_building_cost_wood, 240),
            (item_set_slot, "itm_building_militia_camp", slot_building_cost_stone, 100),
            (item_set_slot, "itm_building_militia_camp", slot_building_cost_gold, 4000),
            (item_set_slot, "itm_building_militia_camp", slot_building_build_time, 300),
            
            (item_set_slot, "itm_building_smithy", slot_building_cost_wood, 140),
            (item_set_slot, "itm_building_smithy", slot_building_cost_stone, 120),
            (item_set_slot, "itm_building_smithy", slot_building_cost_gold, 5000),
            (item_set_slot, "itm_building_smithy", slot_building_build_time, 420),
            
            (item_set_slot, "itm_building_stables", slot_building_cost_wood, 300),
            (item_set_slot, "itm_building_stables", slot_building_cost_stone, 60),
            (item_set_slot, "itm_building_stables", slot_building_cost_gold, 4500),
            (item_set_slot, "itm_building_stables", slot_building_build_time, 380),
            
            (item_set_slot, "itm_building_archery_range", slot_building_cost_wood, 100),
            (item_set_slot, "itm_building_archery_range", slot_building_cost_stone, 20),
            (item_set_slot, "itm_building_archery_range", slot_building_cost_gold, 2000),
            (item_set_slot, "itm_building_archery_range", slot_building_build_time, 200),
            
            (item_set_slot, "itm_building_barrack", slot_building_cost_wood, 200),
            (item_set_slot, "itm_building_barrack", slot_building_cost_stone, 340),
            (item_set_slot, "itm_building_barrack", slot_building_cost_gold, 3000),
            (item_set_slot, "itm_building_barrack", slot_building_build_time, 300),
            
            (item_set_slot, "itm_building_food_store", slot_building_cost_wood, 280),
            (item_set_slot, "itm_building_food_store", slot_building_cost_stone, 220),
            (item_set_slot, "itm_building_food_store", slot_building_cost_gold, 2000),
            (item_set_slot, "itm_building_food_store", slot_building_build_time, 260),

            (item_set_slot, "itm_building_recruitement_camp", slot_building_cost_wood, 120),
            (item_set_slot, "itm_building_recruitement_camp", slot_building_cost_stone, 80),
            (item_set_slot, "itm_building_recruitement_camp", slot_building_cost_gold, 4800),
            (item_set_slot, "itm_building_recruitement_camp", slot_building_build_time, 300),

            (item_set_slot, "itm_building_barrack_2", slot_building_cost_wood, 300),
            (item_set_slot, "itm_building_barrack_2", slot_building_cost_stone, 510),
            (item_set_slot, "itm_building_barrack_2", slot_building_cost_gold, 4500),
            (item_set_slot, "itm_building_barrack_2", slot_building_build_time, 450),

            (item_set_slot, "itm_building_smithy_2", slot_building_cost_wood, 210),
            (item_set_slot, "itm_building_smithy_2", slot_building_cost_stone, 180),
            (item_set_slot, "itm_building_smithy_2", slot_building_cost_gold, 7500),
            (item_set_slot, "itm_building_smithy_2", slot_building_build_time, 630),

            (item_set_slot, "itm_building_training_camp", slot_building_cost_wood, 150),
            (item_set_slot, "itm_building_training_camp", slot_building_cost_stone, 110),
            (item_set_slot, "itm_building_training_camp", slot_building_cost_gold, 5400),
            (item_set_slot, "itm_building_training_camp", slot_building_build_time, 360),

            (item_set_slot, "itm_building_training_camp_2", slot_building_cost_wood, 225),
            (item_set_slot, "itm_building_training_camp_2", slot_building_cost_stone, 165),
            (item_set_slot, "itm_building_training_camp_2", slot_building_cost_gold, 8100),
            (item_set_slot, "itm_building_training_camp_2", slot_building_build_time, 540),
            
            (item_set_slot, "itm_building_workshop", slot_building_cost_wood, 250),
            (item_set_slot, "itm_building_workshop", slot_building_cost_stone, 250),
            (item_set_slot, "itm_building_workshop", slot_building_cost_gold, 6700),
            (item_set_slot, "itm_building_workshop", slot_building_build_time, 480),
            
            (item_set_slot, "itm_building_fletcher", slot_building_cost_wood, 220),
            (item_set_slot, "itm_building_fletcher", slot_building_cost_stone, 20),
            (item_set_slot, "itm_building_fletcher", slot_building_cost_gold, 400),
            (item_set_slot, "itm_building_fletcher", slot_building_build_time, 320),

            (item_set_slot, "itm_building_archery_range_2", slot_building_cost_wood, 150),
            (item_set_slot, "itm_building_archery_range_2", slot_building_cost_stone, 30),
            (item_set_slot, "itm_building_archery_range_2", slot_building_cost_gold, 3000),
            (item_set_slot, "itm_building_archery_range_2", slot_building_build_time, 300),

            (item_set_slot, "itm_building_trading_post", slot_building_cost_wood, 280),
            (item_set_slot, "itm_building_trading_post", slot_building_cost_stone, 50),
            (item_set_slot, "itm_building_trading_post", slot_building_cost_gold, 6200),
            (item_set_slot, "itm_building_trading_post", slot_building_build_time, 320),

            (item_set_slot, "itm_building_food_store_2", slot_building_cost_wood, 420),
            (item_set_slot, "itm_building_food_store_2", slot_building_cost_stone, 330),
            (item_set_slot, "itm_building_food_store_2", slot_building_cost_gold, 3000),
            (item_set_slot, "itm_building_food_store_2", slot_building_build_time, 390),

            (item_set_slot, "itm_building_recruitement_camp_2", slot_building_cost_wood, 180),
            (item_set_slot, "itm_building_recruitement_camp_2", slot_building_cost_stone, 120),
            (item_set_slot, "itm_building_recruitement_camp_2", slot_building_cost_gold, 7200),
            (item_set_slot, "itm_building_recruitement_camp_2", slot_building_build_time, 450),
            
            (item_set_slot, "itm_building_university", slot_building_cost_wood, 390),
            (item_set_slot, "itm_building_university", slot_building_cost_stone, 600),
            (item_set_slot, "itm_building_university", slot_building_cost_gold, 8000),
            (item_set_slot, "itm_building_university", slot_building_build_time, 680),

            (item_set_slot, "itm_building_slaver_2", slot_building_cost_wood, 180),
            (item_set_slot, "itm_building_slaver_2", slot_building_cost_stone, 75),
            (item_set_slot, "itm_building_slaver_2", slot_building_cost_gold, 4500),
            (item_set_slot, "itm_building_slaver_2", slot_building_build_time, 390),

            (item_set_slot, "itm_building_market_3", slot_building_cost_wood, 720),
            (item_set_slot, "itm_building_market_3", slot_building_cost_stone, 180),
            (item_set_slot, "itm_building_market_3", slot_building_cost_gold, 7650),
            (item_set_slot, "itm_building_market_3", slot_building_build_time, 810),
            
            (item_set_slot, "itm_building_temple", slot_building_cost_wood, 220),
            (item_set_slot, "itm_building_temple", slot_building_cost_stone, 800),
            (item_set_slot, "itm_building_temple", slot_building_cost_gold, 10000),
            (item_set_slot, "itm_building_temple", slot_building_build_time, 920),

            (item_set_slot, "itm_building_library", slot_building_cost_wood, 560),
            (item_set_slot, "itm_building_library", slot_building_cost_stone, 240),
            (item_set_slot, "itm_building_library", slot_building_cost_gold, 7600),
            (item_set_slot, "itm_building_library", slot_building_build_time, 600),

            (item_set_slot, "itm_building_order", slot_building_cost_wood, 250),
            (item_set_slot, "itm_building_order", slot_building_cost_stone, 750),
            (item_set_slot, "itm_building_order", slot_building_cost_gold, 15000),
            (item_set_slot, "itm_building_order", slot_building_build_time, 1200),

            (item_set_slot, "itm_building_tavern_2", slot_building_cost_wood, 420),
            (item_set_slot, "itm_building_tavern_2", slot_building_cost_stone, 270),
            (item_set_slot, "itm_building_tavern_2", slot_building_cost_gold, 5600),
            (item_set_slot, "itm_building_tavern_2", slot_building_build_time, 360),

            (item_set_slot, "itm_building_trading_post_2", slot_building_cost_wood, 520),
            (item_set_slot, "itm_building_trading_post_2", slot_building_cost_stone, 75),
            (item_set_slot, "itm_building_trading_post_2", slot_building_cost_gold, 9300),
            (item_set_slot, "itm_building_trading_post_2", slot_building_build_time, 480),
        ]),
    
    # script_party_has_building
    # input:
    #   arg1: party_no
    #   arg2: building
    # output:
    #   reg0: building_state
    ("party_has_building",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":building", 2),
            
            (assign, ":has_building", -1),
            
            (assign, ":end", slot_party_building_slot_end),
            (try_for_range, ":building_slot", slot_party_building_slot_1, ":end"),
                (party_get_slot, ":cur_building", ":party_no", ":building_slot"),
                (try_begin),
                    (eq, ":cur_building", ":building"),
                    (val_add, ":building_slot", num_building_slots),
                    (party_get_slot, ":has_building", ":party_no", ":building_slot"), # gets building state
                    (assign, ":end", 0),
                (try_end),
            (try_end),
            
            (assign, reg0, ":has_building"),
        ]),
    
    # script_cf_party_need_troops
    # input:
    #   arg1: party_no
    # output:
    #   reg0: need_type
    ("cf_party_need_troops",
        [
            # ToDo: improve
            (store_script_param, ":party_no", 1),

            (party_get_slot, ":party_type", ":party_no", slot_party_type),

            (assign, ":need", 0),
            (assign, ":type", type_none),

            (try_begin),
                (is_between, ":party_no", spt_village, spt_fort + 1),
                (call_script, "script_center_need_troops", ":party_no"),
                (assign, ":type", type_moderate),
                (assign, ":need", reg0),
            (else_try),
                (eq, ":party_type", spt_war_party),
                (call_script, "script_party_get_prefered_wages_limit", ":party_no"),
                (assign, ":party_limit", reg0),
                (assign, ":party_limit_min", reg1),
                (call_script, "script_party_get_wages", ":party_no"),
                (assign, ":wages", reg0),

                (try_begin),
                    (lt, ":wages", ":party_limit"),
                    (assign, ":need", 1),
                    (assign, ":type", type_slight),
                    (lt, ":wages", ":party_limit_min"),
                    (assign, ":type", type_moderate),

                    (store_div, ":party_combat_limit", ":party_limit", 4),
                    (lt, ":wages", ":party_combat_limit"),
                    (assign, ":type", type_critical),
                (try_end),
            (try_end),

            (assign, reg0, ":type"),
            (eq, ":need", 1),
        ]),
    
    # script_center_need_troops
    # input:
    #   arg1: center_no
    # output:
    #   reg0: need_troops
    ("center_need_troops",
        [
            # ToDo: improve
            (store_script_param, ":party_no", 1),
            
            # (neg|troop_slot_ge, ":party_no", slot_party_besieged_by, 0),

            (call_script, "script_party_get_prefered_wages_limit", ":party_no"),
            # We use minimum party size
            (assign, ":limit", reg1),
            (call_script, "script_party_get_wages", ":party_no"),
            (assign, ":wages", reg0),
            
            (try_begin),
                (lt, ":wages", ":limit"),
                (assign, reg0, 1),
            (else_try),
                (assign, reg0, 0),
            (try_end),
        ]),
    
    # script_troop_get_rank
    # input:
    #   arg1: troop_no
    # output:
    #   reg0: rank
    ("troop_get_rank",
        [
            (store_script_param, ":troop_no", 1),
            
            (assign, ":end", centers_end),
            (assign, ":rank", 0),
            
            (store_troop_faction, ":faction", ":troop_no"),
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
                    (lt, ":rank", rank_castle),
                    (party_get_slot, ":lord", ":cur_center", slot_party_lord),
                    (try_begin),
                        (eq, ":lord", ":troop_no"),
                        (assign, ":rank", rank_castle),
                    (try_end),
                (else_try),
                    (eq, ":party_type", spt_town),
                    (party_get_slot, ":lord", ":cur_center", slot_party_lord),
                    (try_begin),
                        (eq, ":lord", ":troop_no"),
                        (assign, ":rank", rank_city),
                    (try_end),
                (try_end),
            (try_end),
            (faction_get_slot, ":faction_size", ":faction", slot_faction_size),
            (try_begin),
                (eq, ":faction_size", sfs_large), # King and marshall ranks are only applied if kingdom is big enough
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
        #   arg1: troop_no
        #   arg2: cur_rank
        #   arg3: new_rank
        # output:
        #   reg0: rank_changed (1 yes, 0 no)
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
                
                (assign, reg11, ":cur_rank"),
                (try_begin),
                    (gt, ":diff", 0),
                    (val_add, ":cur_rank", 1),
                (else_try),
                    (val_sub, ":cur_rank", 1),
                (try_end),
                (call_script, "script_troop_change_level", ":troop_no", ":cur_rank"),
                (try_begin),
                    (call_script, "script_cf_debug", debug_simple|debug_faction),
                    (str_store_troop_name, s10, ":troop_no"),
                    (assign, reg10, ":cur_rank"),
                    (display_message, "@{s10} changed level: from {reg11} to {reg10}."),
                (try_end),
                (assign, ":changed", 1),
            (try_end),
            
            (assign, reg0, ":changed"),
        ]),
    
    # script_init_lord
        # input:
        #   arg1: lord_no
        # output: none
    ("init_lord",
        [
            (store_script_param, ":lord_no", 1),
            
            (troop_set_slot, ":lord_no", slot_troop_kingdom_occupation, tko_none),
            (troop_set_slot, ":lord_no", slot_troop_vassal_of, -1),
            (troop_set_slot, ":lord_no", slot_troop_original_faction, "fac_kingdom_1"),
            (troop_set_slot, ":lord_no", slot_troop_leaded_party, -1),
            (troop_set_slot, ":lord_no", slot_troop_died, -1),
            (troop_set_slot, ":lord_no", slot_troop_prisoner_of, -1),
            # (troop_set_slot, ":lord_no", slot_troop_prisoner_in, -1),
            (troop_set_slot, ":lord_no", slot_troop_last_met, -1),
            (troop_set_slot, ":lord_no", slot_troop_gathering, -1),
            # We need a minimum amount of wanted wages to cover for a few troops
            (troop_set_slot, ":lord_no", slot_troop_wanted_party_wages, 500),

            # Reset family
            (try_for_range, ":slot", slot_troop_married_to, slot_troop_child_10+1),
                (try_begin),
                    (troop_get_slot, ":relative", ":lord_no", ":slot"),
                    (ge, ":relative", 0),
                    (try_for_range, ":other_slot", slot_troop_married_to, slot_troop_child_10+1),
                        (troop_slot_eq, ":relative", ":other_slot", ":lord_no"),
                        (troop_set_slot, ":relative", ":other_slot", -1),
                    (try_end),
                (try_end),
                (troop_set_slot, ":lord_no", ":slot", -1),
            (try_end),
            # Reset relations
            (store_sub, ":own_offset", ":lord_no", npc_heroes_begin),
            (store_add, ":own_relation_slot", ":own_offset", slot_troop_relations_begin),
            (try_for_range, ":other_troop", npc_heroes_begin, npc_heroes_end),
                (store_sub, ":offset", ":other_troop", npc_heroes_begin),
                (store_add, ":relation_slot", slot_troop_relations_begin, ":offset"),
                (troop_set_slot, ":lord_no", ":relation_slot", 0),
                (troop_set_slot, ":other_troop", ":own_relation_slot", 0),
            (try_end),
        ]),
    
    # script_ready_lord
        # input:
        #   arg1: lord_no
        #   arg2: faction_no
        # output: none
    ("ready_lord",
        [
            (store_script_param, ":lord_no", 1),
            (store_script_param, ":faction_no", 2),
            
            (troop_set_faction, ":lord_no", ":faction_no"),
            
            (troop_set_slot, ":lord_no", slot_troop_original_faction, ":faction_no"),
            
            (troop_set_slot, ":lord_no", slot_troop_kingdom_occupation, tko_kingdom_hero),
            
            (call_script, "script_troop_set_equip_type", ":lord_no"),
            (call_script, "script_troop_change_level", ":lord_no", 0),
            (troop_set_slot, ":lord_no", slot_troop_rank, rank_none),
            (call_script, "script_troop_set_name", ":lord_no"),
            (call_script, "script_troop_update_name", ":lord_no"),
            (call_script, "script_troop_update_home", ":lord_no"),
            
            # ToDo: refine banner selection
            (store_random_in_range, ":banner", banner_scene_props_begin, banner_scene_props_end),
            (troop_set_slot, ":lord_no", slot_troop_banner_scene_prop, ":banner"),
            
            (call_script, "script_troop_get_face_code", ":lord_no"),
            (troop_set_face_keys, ":lord_no", s0),
            
            # Reset state
            (store_current_hours, ":cur_hour"),
            (troop_set_slot, ":lord_no", slot_troop_last_attack, ":cur_hour"),
            (troop_set_slot, ":lord_no", slot_troop_last_rest, ":cur_hour"),
            
            (faction_get_slot, ":num_vassals", ":faction_no", slot_faction_num_vassals),
            (val_add, ":num_vassals", 1),
            (faction_set_slot, ":faction_no", slot_faction_num_vassals, ":num_vassals"),
        ]),

    # script_troop_death
        # input:
        #   arg1: troop_no
        # output: none
    ("troop_death",
        [
            (store_script_param, ":troop_no", 1),

            (store_current_day, ":cur_day"),

            (troop_set_slot, ":troop_no", slot_troop_kingdom_occupation, tko_dead),
            (troop_set_slot, ":troop_no", slot_troop_died, ":cur_day"),

            (assign, ":living_relative", 0),
            # Reset troop if every relative are dead
            (try_for_range, ":slot", slot_troop_married_to, slot_troop_child_10+1),
                (troop_get_slot, ":relative", ":troop_no", ":slot"),
                (try_begin),
                    (ge, ":relative", 0),
                    (troop_get_slot, ":relative_dead", ":relative", slot_troop_kingdom_occupation),
                    (try_begin),
                        (eq, ":relative_dead", tko_dead),
                        (assign, ":other_living_relative"),
                        # Reset relative if it has no living relative
                        (try_for_range, ":other_slot", slot_troop_married_to, slot_troop_child_10+1),
                            (troop_get_slot, ":other_relative", ":relative", ":other_slot"),
                            (troop_get_slot, ":occupation", ":other_relative", slot_troop_kingdom_occupation),
                            (gt, ":occupation", tko_dead),
                            (assign, ":other_living_relative", 1),
                        (try_end),
                        (try_begin),
                            (eq, ":other_living_relative", 0),
                            (call_script, "script_init_lord", ":relative"),
                        (try_end),
                    (else_try),
                        (assign, ":living_relative", 1),
                    (try_end),
                (try_end),
            (try_end),
            (try_begin),
                (eq, ":living_relative", 0),
                (call_script, "script_init_lord", ":troop_no"),
            (try_end),

        ]),
    
    # script_troop_set_name
        # input:
        #   arg1: troop_no
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
        #   arg1: giver_troop_no
        #   arg2: center
        #   arg3: receiver_troop
        # output: none
    ("troop_give_center_to_troop",
        [
            (store_script_param, ":giver_troop_no", 1),
            (store_script_param, ":center", 2),
            (store_script_param, ":receiver_troop", 3),
            
            (try_begin),
                (store_troop_faction, ":player_faction", "$g_player_troop"),
                (store_troop_faction, ":giver_faction", ":giver_troop_no"),
                (store_troop_faction, ":receiver_faction", ":receiver_troop"),
                (store_relation, ":giver_faction_player_faction_relation", ":player_faction", ":giver_faction"),
                (store_relation, ":receiver_faction_player_faction_relation", ":player_faction", ":receiver_faction"),
                (this_or_next|eq, ":player_faction", ":giver_faction"),
                (this_or_next|eq, ":player_faction", ":receiver_faction"),

                (this_or_next|ge, ":giver_faction_player_faction_relation", relation_state_friendly),
                (ge, ":receiver_faction_player_faction_relation", relation_state_friendly),

                (str_store_troop_name_link, s10, ":giver_troop_no"),
                (str_store_troop_name_link, s11, ":receiver_troop"),
                (str_store_party_name_link, s12, ":center"),
                (display_log_message, "@{s10} grants {s12} to {s11}"),
            (else_try),
                (call_script, "script_cf_debug", debug_faction|debug_simple),
                (str_store_troop_name_link, s10, ":giver_troop_no"),
                (str_store_troop_name_link, s11, ":receiver_troop"),
                (str_store_party_name_link, s12, ":center"),
                (display_log_message, "@{s10} grants {s12} to {s11}"),
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
            (troop_set_slot, ":giver_troop_no", slot_troop_surplus_center, ":surplus_center"),
            
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
            (troop_set_slot, ":receiver_troop", slot_troop_surplus_center, ":surplus_center"),
        ]),
    
    # script_give_center_to_troop
    # input:
    #   arg1: center_no
    #   arg2: troop_no
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
            (troop_set_slot, "trp_swadian_champion", slot_troop_faction_not_1, "fac_small_kingdom_12"), # Has Heavy Infantry instead
            (troop_set_slot, "trp_swadian_ranger", slot_troop_faction_not_1, "fac_small_kingdom_13"), # Has Horseman instead
            (troop_set_slot, "trp_swadian_light_lancer", slot_troop_faction_not_1, "fac_small_kingdom_13"), # Has Lancer instead
            (troop_set_slot, "trp_swadian_light_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_13"), # Has Horseman instead
            (troop_set_slot, "trp_swadian_militia", slot_troop_faction_not_1, "fac_small_kingdom_14"), # Has Hunter instead
            (troop_set_slot, "trp_swadian_light_bowman", slot_troop_faction_not_1, "fac_small_kingdom_14"), # Has Light Longbowman instead
            (troop_set_slot, "trp_swadian_bowman", slot_troop_faction_not_1, "fac_small_kingdom_14"), # Has Heavy Longbowman instead
            (troop_set_slot, "trp_swadian_pikeman", slot_troop_faction_not_1, "fac_small_kingdom_15"), # Has Spearman instead
            (troop_set_slot, "trp_swadian_champion", slot_troop_faction_not_2, "fac_small_kingdom_17"), # 
            (troop_set_slot, "trp_swadian_heavy_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_17"), # Has Squire instead

            (troop_set_slot, "trp_swadian_levy_spearman", slot_troop_faction_reserved_2, "fac_small_kingdom_15"),
            (troop_set_slot, "trp_swadian_foot_knight", slot_troop_faction_reserved_2, "fac_small_kingdom_15"),
            
            (troop_set_slot, "trp_vaegir_light_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_22"), # Has Scout instead
            (troop_set_slot, "trp_vaegir_heavy_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_22"), # Has Horseman instead
            (troop_set_slot, "trp_vaegir_light_infantry", slot_troop_faction_not_2, "fac_small_kingdom_22"), # Has Light Club Infantry instead
            (troop_set_slot, "trp_vaegir_heavy_infantry", slot_troop_faction_not_2, "fac_small_kingdom_22"), # Has Club Infantry instead
            (troop_set_slot, "trp_vaegir_light_infantry", slot_troop_faction_not_1, "fac_small_kingdom_23"), # Has Footman instead
            (troop_set_slot, "trp_vaegir_heavy_infantry", slot_troop_faction_not_1, "fac_small_kingdom_23"), # Has Heavy Footman instead
            (troop_set_slot, "trp_vaegir_guard", slot_troop_faction_not_1, "fac_small_kingdom_23"), # Has Horseman instead
            (troop_set_slot, "trp_vaegir_medium_bowman", slot_troop_faction_not_1, "fac_small_kingdom_25"), # Has Longbowman instead
            (troop_set_slot, "trp_vaegir_mounted_bowman", slot_troop_faction_not_1, "fac_small_kingdom_21"), # Has Hussar instead
            (troop_set_slot, "trp_vaegir_mounted_bowman", slot_troop_faction_not_2, "fac_small_kingdom_25"), # Has Mounted Longbowman instead
            (troop_set_slot, "trp_vaegir_royal_hussar", slot_troop_faction_not_1, "fac_small_kingdom_25"), # Has Royal Mounted Longbowman instead
            
            (troop_set_slot, "trp_khergit_light_infantry", slot_troop_faction_not_1, "fac_small_kingdom_32"), # Has Light Skirmisher instead
            (troop_set_slot, "trp_khergit_skirmisher", slot_troop_faction_not_1, "fac_small_kingdom_32"), # Has Light Skirmisher instead
            (troop_set_slot, "trp_khergit_guard", slot_troop_faction_not_1, "fac_small_kingdom_32"), # Has Heavy Skirmisher instead
            (troop_set_slot, "trp_khergit_light_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_33"), # Has Light Steppe Cavalry instead
            (troop_set_slot, "trp_khergit_heavy_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_33"), # Has Heavy Steppe Cavalry instead
            (troop_set_slot, "trp_khergit_mounted_skirmisher", slot_troop_faction_not_1, "fac_small_kingdom_33"), # Has Scout instead
            (troop_set_slot, "trp_khergit_noble", slot_troop_faction_not_1, "fac_small_kingdom_34"), # Has Noble Cavalry and Noble Lancer instead
            (troop_set_slot, "trp_khergit_mounted_skirmisher", slot_troop_faction_not_2, "fac_small_kingdom_35"), # Has Light Horseman instead
            (troop_set_slot, "trp_khergit_light_lancer", slot_troop_faction_not_1, "fac_small_kingdom_35"), # Has Light Horseman instead
            (troop_set_slot, "trp_khergit_lancer", slot_troop_faction_not_1, "fac_small_kingdom_35"), # Has Heavy Horseman instead
            (troop_set_slot, "trp_khergit_guard", slot_troop_faction_not_2, "fac_small_kingdom_36"), # Has Blade-Master instead
            
            (troop_set_slot, "trp_nord_militia", slot_troop_faction_not_1, "fac_small_kingdom_44"), # Has Levy Crossbowman instead
            (troop_set_slot, "trp_nord_light_bowman", slot_troop_faction_not_1, "fac_small_kingdom_42"), # Has Light Longbowman instead
            (troop_set_slot, "trp_nord_heavy_bowman", slot_troop_faction_not_1, "fac_small_kingdom_42"), # Has Heavy Longbowman instead
            (troop_set_slot, "trp_nord_light_infantry", slot_troop_faction_not_1, "fac_small_kingdom_42"), # Has Footman instead
            #(troop_set_slot, "trp_nord_light_infantry", slot_troop_faction_not_1, "fac_small_kingdom_42"), # 
            (troop_set_slot, "trp_nord_medium_infantry", slot_troop_faction_not_1, "fac_small_kingdom_42"), # Has Heavy Infantry instead
            (troop_set_slot, "trp_nord_light_infantry", slot_troop_faction_not_2, "fac_small_kingdom_43"), # Has Skirmisher instead
            (troop_set_slot, "trp_nord_light_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_43"), # Has Light Mounted Skirmisher instead
            (troop_set_slot, "trp_nord_guard", slot_troop_faction_not_1, "fac_small_kingdom_43"), # Has Heavy Skirmisher instead
            (troop_set_slot, "trp_nord_medium_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_44"), # Has Spear Cavalry instead
            (troop_set_slot, "trp_nord_heavy_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_44"), # Has Heavy Spear Cavalry instead
            (troop_set_slot, "trp_nord_medium_longbowman", slot_troop_faction_not_2, "fac_small_kingdom_44"), # Has Crossbowman instead
            (troop_set_slot, "trp_nord_medium_longbowman", slot_troop_faction_not_1, "fac_small_kingdom_45"), # Has Bowman instead
            (troop_set_slot, "trp_nord_light_cavalry", slot_troop_faction_not_2, "fac_small_kingdom_45"), # Has Light Spear Cavalry instead
            (troop_set_slot, "trp_nord_medium_cavalry", slot_troop_faction_not_2, "fac_small_kingdom_45"), # Has Spear Cavalry instead
            (troop_set_slot, "trp_nord_heavy_cavalry", slot_troop_faction_not_2, "fac_small_kingdom_45"), # Has Heavy Spear Cavalry instead
            
            (troop_set_slot, "trp_nord_medium_spear_cavalry", slot_troop_faction_reserved_2, "fac_small_kingdom_44"), # 
            (troop_set_slot, "trp_nord_heavy_spear_cavalry", slot_troop_faction_reserved_2, "fac_small_kingdom_44"), # 
            (troop_set_slot, "trp_nord_infantry", slot_troop_faction_reserved_2, "fac_small_kingdom_43"),
            
            (troop_set_slot, "trp_rhodok_militia", slot_troop_faction_not_1, "fac_small_kingdom_54"), # Has Levy Crossbowman instead
            (troop_set_slot, "trp_rhodok_militia", slot_troop_faction_not_2, "fac_small_kingdom_55"), # Has Levy Crossbowman instead
            (troop_set_slot, "trp_rhodok_light_crossbowman", slot_troop_faction_not_1, "fac_small_kingdom_51"), # 
            (troop_set_slot, "trp_rhodok_light_horse_archer", slot_troop_faction_not_1, "fac_small_kingdom_51"), # Has Mounted Archer instead
            (troop_set_slot, "trp_rhodok_medium_crossbowman", slot_troop_faction_not_1, "fac_small_kingdom_51"), # Has Bowman instead
            (troop_set_slot, "trp_rhodok_heavy_crossbowman", slot_troop_faction_not_1, "fac_small_kingdom_51"), # Has Heavy Bowman instead
            (troop_set_slot, "trp_rhodok_noble", slot_troop_faction_not_1, "fac_small_kingdom_51"), # Has Highlander instead
            (troop_set_slot, "trp_rhodok_medium_cavalry", slot_troop_faction_not_2, "fac_small_kingdom_52"), # 
            (troop_set_slot, "trp_rhodok_noble", slot_troop_faction_not_2, "fac_small_kingdom_52"), # Has Heroic Pikeman instead
            (troop_set_slot, "trp_rhodok_medium_cavalry", slot_troop_faction_not_1, "fac_small_kingdom_54"), # Has Mounted Crossbowman instead
            
            (troop_set_slot, "trp_rhodok_mounted_crossbow", slot_troop_faction_reserved_2, "fac_small_kingdom_55"), # 
            (troop_set_slot, "trp_rhodok_levy_crossbowman", slot_troop_faction_reserved_2, "fac_small_kingdom_55"), # 
            
            (troop_set_slot, "trp_sarranid_light_bowman", slot_troop_faction_not_1, "fac_small_kingdom_61"), # Has Light Crossbowman instead
            (troop_set_slot, "trp_sarranid_bowman", slot_troop_faction_not_1, "fac_small_kingdom_61"), # Has Crossbowman instead
            (troop_set_slot, "trp_sarranid_noble_horse_archer", slot_troop_faction_not_2, "fac_small_kingdom_62"), # Has Noble Spearman and Noble Infantry
            (troop_set_slot, "trp_sarranid_light_infantry", slot_troop_faction_not_1, "fac_small_kingdom_63"), # Has Levy Infantry instead
            (troop_set_slot, "trp_sarranid_medium_infantry", slot_troop_faction_not_1, "fac_small_kingdom_63"), # Has Footman instead
            (troop_set_slot, "trp_sarranid_light_skirmisher", slot_troop_faction_not_1, "fac_small_kingdom_63"), # 
            (troop_set_slot, "trp_sarranid_guard", slot_troop_faction_not_1, "fac_small_kingdom_63"), # Has Warrior instead
            (troop_set_slot, "trp_sarranid_heavy_skirmisher", slot_troop_faction_not_1, "fac_small_kingdom_63"), # Has Skirmisher instead
            (troop_set_slot, "trp_sarranid_heavy_infantry", slot_troop_faction_not_1, "fac_small_kingdom_63"), # Has Sergeant instead
            (troop_set_slot, "trp_sarranid_noble_horse_archer", slot_troop_faction_not_1, "fac_small_kingdom_63"), # Has Cataphract instead
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
            (troop_set_slot, "trp_swadian_militia", slot_troop_type, tt_archer),
            (troop_set_slot, "trp_swadian_sergeant", slot_troop_type, tt_shock_infantry), # Because swadians have too many of them
            (troop_set_slot, "trp_khergit_militia", slot_troop_type, tt_archer),
        ]),
    
    # script_init_troops_archer_score
    # input: none
    # output: none
    ("init_troops_archer_score",
        [
            (try_for_range, ":troop_no", soldiers_begin, soldiers_end),
                
                (call_script, "script_troop_get_archer_score", ":troop_no"),
                (assign, ":score", reg0),
                
                (troop_set_slot, ":troop_no", slot_troop_archer_score, ":score"),
            (try_end),
        ]),

    # script_troop_get_archer_score
    # input:
    #   arg1: troop_no
    # output:
    #   reg0: score
    ("troop_get_archer_score",
        [
            (store_script_param, ":troop_no", 1),

            (assign, ":score", 0),
            (store_skill_level, ":power_draw", skl_power_draw, ":troop_no"),
            (store_skill_level, ":power_strike", skl_power_strike, ":troop_no"),
            (store_skill_level, ":power_throw", skl_power_throw, ":troop_no"),
            (store_skill_level, ":ironflesh", skl_ironflesh, ":troop_no"),
            (store_proficiency_level, ":1h", ":troop_no", wpt_one_handed_weapon),
            (store_proficiency_level, ":2h", ":troop_no", wpt_two_handed_weapon),
            (store_proficiency_level, ":pole", ":troop_no", wpt_polearm),
            (store_proficiency_level, ":bow", ":troop_no", wpt_archery),
            (store_proficiency_level, ":xbow", ":troop_no", wpt_crossbow),
            (store_proficiency_level, ":throw", ":troop_no", wpt_throwing),
            (store_attribute_level, ":str", ":troop_no", ca_strength),
            
            (val_mul, ":power_draw", 25),
            (val_mul, ":power_strike", 10),
            (val_mul, ":power_throw", 15),
            (val_mul, ":ironflesh", 5),
            
            # (val_mul, ":bow", 1),
            (val_mul, ":xbow", 2),
            # (val_mul, ":throw", 1),
            
            (val_div, ":1h", 2),
            (val_div, ":2h", 2),
            (val_div, ":pole", 2),
            (val_max, ":1h", ":2h"),
            (val_max, ":1h", ":pole"),
            
            (val_add, ":bow", ":power_draw"),
            (val_add, ":throw", ":power_throw"),
            # (val_add, ":xbow", ":power_draw"),
            
            (val_max, ":bow", ":xbow"),
            (val_max, ":bow", ":throw"),
            
            (val_add, ":score", ":bow"),
            (val_sub, ":score", ":1h"),
            (val_sub, ":score", ":ironflesh"),
            (val_sub, ":score", ":power_strike"),
            (val_sub, ":score", ":str"),
            
            (val_max, ":score", 0),

            (assign, reg0, ":score"),
        ]),

    # script_init_troops_mercenary
    # input: none
    # output: none
    ("init_troops_mercenary",
        [
            (troop_set_slot, "trp_swadian_light_cavalry", slot_troop_mercenary_captain_1, "trp_swadian_heavy_cavalry"),
            (troop_set_slot, "trp_swadian_light_bowman", slot_troop_mercenary_captain_1, "trp_swadian_bowman"),
            (troop_set_slot, "trp_swadian_light_crossbowman", slot_troop_mercenary_captain_1, "trp_swadian_crossbowman"),
            (troop_set_slot, "trp_swadian_heavy_infantry", slot_troop_mercenary_captain_1, "trp_swadian_sergeant"),
            (troop_set_slot, "trp_swadian_heavy_cavalry", slot_troop_mercenary_captain_1, "trp_swadian_noble"),
            (troop_set_slot, "trp_swadian_sergeant", slot_troop_mercenary_captain_1, "trp_swadian_foot_knight"),
            (troop_set_slot, "trp_swadian_light_lancer", slot_troop_mercenary_captain_1, "trp_swadian_heavy_lancer"),
            (troop_set_slot, "trp_swadian_heavy_lancer", slot_troop_mercenary_captain_1, "trp_swadian_noble"),
            (troop_set_slot, "trp_swadian_light_longbowman", slot_troop_mercenary_captain_1, "trp_swadian_longbowman"),

            (troop_set_slot, "trp_vaegir_light_cavalry", slot_troop_mercenary_captain_1, "trp_vaegir_heavy_cavalry"),
            (troop_set_slot, "trp_vaegir_light_infantry", slot_troop_mercenary_captain_1, "trp_vaegir_heavy_infantry"),
            (troop_set_slot, "trp_vaegir_light_bowman", slot_troop_mercenary_captain_1, "trp_vaegir_medium_bowman"),
            (troop_set_slot, "trp_vaegir_heavy_cavalry", slot_troop_mercenary_captain_1, "trp_vaegir_royal_hussar"),
            (troop_set_slot, "trp_vaegir_light_lancer", slot_troop_mercenary_captain_1, "trp_vaegir_heavy_lancer"),
            (troop_set_slot, "trp_vaegir_medium_bowman", slot_troop_mercenary_captain_1, "trp_vaegir_heavy_longbowman"),
            
            (troop_set_slot, "trp_khergit_light_lancer", slot_troop_mercenary_captain_1, "trp_khergit_lancer"),
            (troop_set_slot, "trp_khergit_light_cavalry", slot_troop_mercenary_captain_1, "trp_khergit_heavy_cavalry"),
            (troop_set_slot, "trp_khergit_heavy_horse_archer", slot_troop_mercenary_captain_1, "trp_khergit_noble"),

            (troop_set_slot, "trp_nord_light_infantry", slot_troop_mercenary_captain_1, "trp_nord_medium_infantry"),
            (troop_set_slot, "trp_nord_medium_infantry", slot_troop_mercenary_captain_1, "trp_nord_noble_infantry"),
            (troop_set_slot, "trp_nord_medium_longbowman", slot_troop_mercenary_captain_1, "trp_nord_heavy_bowman"),

            (troop_set_slot, "trp_rhodok_light_infantry", slot_troop_mercenary_captain_1, "trp_rhodok_heavy_infantry"),
            (troop_set_slot, "trp_rhodok_medium_crossbowman", slot_troop_mercenary_captain_1, "trp_rhodok_heavy_crossbowman"),
            (troop_set_slot, "trp_rhodok_heavy_infantry", slot_troop_mercenary_captain_1, "trp_rhodok_noble"),

            (troop_set_slot, "trp_sarranid_light_skirmisher", slot_troop_mercenary_captain_1, "trp_sarranid_heavy_skirmisher"),
            (troop_set_slot, "trp_sarranid_medium_infantry", slot_troop_mercenary_captain_1, "trp_sarranid_guard"),
            (troop_set_slot, "trp_sarranid_guard", slot_troop_mercenary_captain_1, "trp_sarranid_heavy_infantry"),
            (troop_set_slot, "trp_sarranid_medium_cavalry", slot_troop_mercenary_captain_1, "trp_sarranid_heavy_cavalry"),
            (troop_set_slot, "trp_sarranid_heavy_cavalry", slot_troop_mercenary_captain_1, "trp_sarranid_noble_horse_archer"),
        ]),
    

    
    # script_faction_get_best_candidate_for_center
    # input:
    #   arg1: faction_no
    #   arg2: center_no
    # output:
    #   reg0: best_candidate
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
                (party_get_slot, ":candidate", ":linked_center", slot_party_lord), # We take the lord of the linked center as choosen one
                (store_troop_faction, ":troop_faction", ":candidate"),
                (ge, ":candidate", 0),
                (eq, ":troop_faction", ":faction_no"),
                (assign, ":best_candidate", ":candidate"),
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
            
            (try_begin),
                (ge, ":best_candidate", 0),
                (call_script, "script_cf_debug", debug_faction|debug_simple),
                (str_store_troop_name, s10, ":best_candidate"),
                (str_store_party_name, s11, ":center_no"),
                (display_message, "@{s10} is the best candidate for {s11}"),
            (try_end),
            
            (assign, reg0, ":best_candidate"),
        ]),
    
    # script_party_count_fit_for_battle
    # Returns the number of unwounded companions in a party
    # input:
    #   arg1: party_id
    # output: 
    #   reg0: result
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
    #   arg1: troop_no
    #   arg2: template_troop
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
    #   arg1: center_to_recruit
    #   arg2: troop_recruiter
    # output:
    #   reg0: total cost
    #   reg1: num troops
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
    #   arg1: troop_id
    # output:
    #   reg0: troop cost
    ("troop_get_cost",
    [
        (store_script_param_1, ":troop_id"),
        
        (store_character_level, ":level", ":troop_id"),
        
        (store_add, ":join_cost", ":level", 8),
        (val_mul, ":join_cost", ":join_cost"),
        (val_div, ":join_cost", 5),
        
        (try_begin),
            (troop_is_mounted, ":troop_id"), # 50% increase for mounted troops
            (val_mul, ":join_cost", 3),
            (val_div, ":join_cost", 2),
        (try_end),

        (val_mul, ":join_cost", 10),
        
        (assign, reg0, ":join_cost"), 
    ]),
    
    # script_troop_get_cost_modifier
    # input:
    #   arg1: troop_no
    #   arg2: current_party
    #   arg3: recruiter
    # output:
    #   reg0: cost_modifier
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
                        # (eq, ":recruiter", "$g_player_troop"),
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
    #   arg1: troop_no
    # output:
    #   s0: troop info
    #   reg0: num_lines
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
    #   arg1: troop_id
    # output:
    #   s0: troop_description
    #   reg0: num_lines
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
    #   arg1: troop_id
    #   arg2: troop_dna
    # output: none
    ("setup_troop_meeting",
        [
            (store_script_param_1, ":meeting_troop"),
            (store_script_param_2, ":troop_dna"),
            (call_script, "script_get_meeting_scene"),
            (assign, ":meeting_scene", reg0),
            (modify_visitors_at_site,":meeting_scene"),
            (reset_visitors),
            (set_visitor,0,"$g_player_troop"),
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
    #   arg1: party_id
    # output: none
    ("setup_party_meeting",
        [
            (store_script_param_1, ":meeting_party"),
            
            (party_stack_get_troop_id, ":meeting_troop",":meeting_party",0),
            (try_begin),
                (neg|troop_is_hero, ":meeting_troop"),
                # If troop is not hero, we chose the highest level in the party
                (store_character_level, ":max_level", ":meeting_troop"),
                (party_get_num_companion_stacks, ":num_stacks", ":meeting_party"),
                (try_for_range, ":cur_stack", 0, ":num_stacks"),
                    (party_stack_get_troop_id, ":troop_id", ":meeting_party", ":cur_stack"),
                    (store_character_level, ":troop_level", ":troop_id"),
                    (gt, ":troop_level", ":max_level"),
                    (assign, ":max_level", ":troop_level"),
                    (assign, ":meeting_troop", ":troop_id"),
                (try_end),
            (try_end),
            (party_stack_get_troop_dna,":troop_dna",":meeting_party",0),
            
            (call_script, "script_setup_troop_meeting", ":meeting_troop", ":troop_dna"),
        ]),
    
    # script_get_meeting_scene
    # input: none
    # output:
    #   reg0: contain suitable scene_no
    ("get_meeting_scene",
        [
            (party_get_current_terrain, ":terrain_type", "$g_player_party"),
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
    ## Select the scene for the next battle
    ## Scene is chosen based on current terrain
    # input: none
    # output:
    #   reg0: contain suitable scene_no
    ("get_battle_scene",
        [
            (party_get_current_terrain, ":terrain_type", "$g_player_party"),
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
    
    # script_troop_copy_items_from_troop
    # input:
    #   arg1: recipient
    #   arg2: troop_to_copy
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
    #   arg1: recipient
    #   arg2: troop_to_copy
    #   arg3: item_type
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
    
    # script_troop_remove_armor
    # input:
    #   arg1: troop_no
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
    #   arg1: troop_no
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
    #   arg1: troop_no
    #   arg2: item_type
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
    
    # script_party_select_battle_side
    # input:
    #   arg1: party_to_join
    #   arg2: battle_party_1
    #   arg3; battle_party_2
    # output:
    #   reg0: party_to_join (0: none, 1: party_1, 2: party_2)
    ("party_select_battle_side",
        [
            (store_script_param, ":party_to_join", 1),
            (store_script_param, ":battle_party_1", 2),
            (store_script_param, ":battle_party_2", 3),
            
            (store_faction_of_party, ":party_faction", ":party_to_join"),
            (store_faction_of_party, ":party_1_faction", ":battle_party_1"),
            (store_faction_of_party, ":party_2_faction", ":battle_party_2"),
            
            (store_relation, ":rel", ":party_faction", ":party_1_faction"),
            (store_relation, ":rel2", ":party_faction", ":party_2_faction"),
            
            (assign, ":continue", 0),
            (try_begin),
                (eq, ":party_faction", ":party_1_faction"),
                (assign, ":continue", 1),
            (else_try),
                (eq, ":party_faction", ":party_2_faction"),
                (assign, ":continue", 2),
            (else_try),
                (try_begin),
                    (lt, ":rel2", relation_state_conflict),
                    (ge, ":rel", relation_state_friendly),
                    (assign, ":continue", 1),
                (else_try),
                    (lt, ":rel2", relation_state_war),
                    (ge, ":rel", relation_state_neutral),
                    (assign, ":continue", 1),
                (else_try),
                    (lt, ":rel", relation_state_conflict),
                    (ge, ":rel2", relation_state_friendly),
                    (assign, ":continue", 2),
                (else_try),
                    (lt, ":rel", relation_state_war),
                    (ge, ":rel2", relation_state_neutral),
                    (assign, ":continue", 2),
                (try_end),
            (try_end),
            (assign, reg0, ":continue"),
        ]),
    
    # script_party_get_looted_gold
        # input:
        #   arg1: looted_party
        # output:
        #   reg0: gold_amount
    ("party_get_looted_gold",
        [
            (store_script_param, ":looted_party", 1),
            
            # (party_get_num_companions, ":num_enemy", ":looted_party"),
            (party_get_num_companion_stacks, ":num_stack", ":looted_party"),
            (assign, ":total_gold", 0),
            (try_for_range, ":stack_no", 0, ":num_stack"),
                (party_stack_get_troop_id, ":cur_troop", ":looted_party", ":stack_no"),

                (try_begin),
                    (troop_is_hero, ":cur_troop"),
                    (store_troop_gold, ":current_gold", ":cur_troop"),
                    # ToDo: percent gold removed global difficulty parameter
                    (store_div, ":removed_gold", ":current_gold", 20),
                    (troop_remove_gold, ":cur_troop", ":removed_gold"),
                    (val_add, ":total_gold", ":removed_gold"),
                (else_try),
                    # ToDo: refine regular troop gold cost
                    (store_character_level, ":troop_level", ":cur_troop"),
                    (party_stack_get_size, ":stack_size", ":looted_party", ":stack_no"),
                    (val_mul, ":troop_level", ":stack_size"),
                    (val_add, ":total_gold", ":troop_level"),
                (try_end),
            (try_end),

            (assign, reg0, ":total_gold"),
        ]),

    # script_party_get_loot
        # input:
        #   arg1: party_no
        #   arg2: clear_storage
        #   arg3: [optional] loot_storage, defaults(trp_temp_troop)
        # output: 
        #   reg0: loot_storage
    ("party_get_loot",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":clear_storage", 2),
            (store_script_param, ":loot_storage", 3),

            (try_begin),
                (eq, ":loot_storage", -1),
                (assign, ":loot_storage", "trp_temp_troop"),
            (try_end),
            (try_begin),
                (eq, ":clear_storage", 1),
                (troop_clear_inventory, ":loot_storage"),
            (try_end),

            (party_get_num_companions, ":party_size", ":party_no"),
            (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (try_begin),
                    (store_free_inventory_capacity, ":free_inventory", ":loot_storage"),
                    (lt, ":free_inventory", 5),
                    # Not enough free space, remove low price items
                    (troop_sort_inventory, ":loot_storage"),
                    (troop_ensure_inventory_space, ":loot_storage", 10),
                (try_end),

                (party_stack_get_troop_id, ":troop_no", ":party_no", ":cur_stack"),
                (party_stack_get_size, ":size", ":party_no", ":cur_stack"),

                (store_mul, ":probability", ":size", 2000),
                (val_div, ":probability", ":party_size"),
                # Min amount of loot from troop
                # Improves variety of loot
                (val_max, ":probability", 20), 
                (troop_loot_troop, ":loot_storage", ":troop_no", ":probability"),
            (try_end),
            (assign, reg0, ":loot_storage"),
        ]),

    # script_party_update_merchants
        ## Updates merchants inventory from party_no with new items
        # input:
        #   arg1: party_no
        # output: none
    ("party_update_merchants",
        [
            (store_script_param, ":party_no", 1),
            
            (party_get_slot, ":party_type", ":party_no", slot_party_type),
            (try_begin),
                (this_or_next|eq, ":party_type", spt_town),
                (eq, ":party_type", spt_castle),
                (store_sub, ":offset", ":party_no", towns_begin),
                (store_add, ":merchant", merchants_general_begin, ":offset"),
                (try_begin),
                    (call_script, "script_cf_merchant_can_update", ":merchant"),
                    (assign, ":num_times", reg0),
                    (try_for_range, ":unused", 0, ":num_times"),
                        (call_script, "script_troop_add_merchant_items_from_party", ":merchant", ":party_no", items_weapon|items_armor|items_good|items_horse),
                    (try_end),
                (try_end),
            (try_end),
            (try_begin),
                (eq, ":party_type", spt_town),
                (store_sub, ":offset", ":party_no", towns_begin),
                (store_add, ":merchant", merchants_weapons_begin, ":offset"),
                
                (call_script, "script_cf_merchant_can_update", ":merchant"),
                (assign, ":num_times", reg0),
                (store_faction_of_party, ":party_faction", ":party_no"),
                (party_set_faction, "p_temp_party", ":party_faction"),
                (party_clear, "p_temp_party"),
                (troop_get_inventory_capacity, ":capacity", ":merchant"),
                (val_div, ":capacity", 2),
                (troop_ensure_inventory_space, ":merchant", ":capacity"),
            
                (troop_clear_inventory, "trp_temp_troop"),
                (store_mul, ":num_tries", ":num_times", 2),
                (try_for_range, ":unused", 0, ":num_tries"),
                    #(call_script, "script_troop_add_merchant_items_from_party", ":merchant", ":party_no", items_weapon),
                    (call_script, "script_party_add_reinforcements", "p_temp_party"),
                (try_end),
                (party_get_num_companion_stacks, ":num_stacks", "p_temp_party"),
                (try_for_range, ":cur_stack", 0, ":num_stacks"),
                    (party_stack_get_troop_id, ":cur_troop", "p_temp_party", ":cur_stack"),
                    (party_stack_get_size, ":size", "p_temp_party", ":cur_stack"),
                    (val_div, ":size", 3), # We reduce the number of troops in each stack to prevent peasant items from bloating the inventory
                    (val_add, ":size", 1), # 
                    (try_for_range, ":unused", 0, ":size"),
                        (troop_loot_troop, "trp_temp_troop", ":cur_troop", 100),
                    (try_end),
                (try_end),
                (troop_get_inventory_capacity, ":num_items", "trp_temp_troop"),

                (store_sub, ":offset", ":party_no", towns_begin),
                (store_add, ":merchant", merchants_weapons_begin, ":offset"),
                # Adding weapons
                (try_for_range, ":i", 0, ":num_items"),
                    (troop_get_inventory_slot, ":item", "trp_temp_troop", ":i"),
                    (gt, ":item", 0),
                    (troop_get_inventory_slot_modifier, ":modifier", "trp_temp_troop", ":i"),
                    (item_get_type, ":item_type", ":item"),
                    (is_between, ":item_type", itp_type_one_handed_wpn, itp_type_goods),
                    (troop_add_item, ":merchant", ":item", ":modifier"),
                (try_end),
                (troop_sort_inventory, ":merchant"),
                
                (store_sub, ":offset", ":party_no", towns_begin),
                (store_add, ":merchant", merchants_armors_begin, ":offset"),
                # Adding armors
                (try_for_range, ":i", 0, ":num_items"),
                    (troop_get_inventory_slot, ":item", "trp_temp_troop", ":i"),
                    (gt, ":item", 0),
                    (troop_get_inventory_slot_modifier, ":modifier", "trp_temp_troop", ":i"),
                    (item_get_type, ":item_type", ":item"),
                    (is_between, ":item_type", itp_type_head_armor, itp_type_pistol),
                    (troop_add_item, ":merchant", ":item", ":modifier"),
                (try_end),
                (troop_sort_inventory, ":merchant"),

                # (call_script, "script_cf_merchant_can_update", ":merchant"),
                # (assign, ":num_times", reg0),

                # (try_for_range, ":unused", 0, ":num_times"),
                #     (call_script, "script_troop_add_merchant_items_from_party", ":merchant", ":party_no", items_armor),
                # (try_end),
            (try_end),
            (try_begin),
                (eq, ":party_type", spt_castle),
                (store_sub, ":offset", ":party_no", castles_begin),
                (store_add, ":merchant", merchants_smiths_begin, ":offset"),
                
                (call_script, "script_cf_merchant_can_update", ":merchant"),
                (assign, ":num_times", reg0),
                (try_for_range, ":unused", 0, ":num_times"),
                    (call_script, "script_troop_add_merchant_items_from_party", ":merchant", ":party_no", items_weapon|items_armor),
                (try_end),
            (try_end),
        ]),
    
    # script_party_update_merchants_gold
    ## Gives merchants from party_no some gold
    # input:
    #   arg1: party_no
    # output: none
    ("party_update_merchants_gold",
        [
            (store_script_param, ":party_no", 1),
            
            # (party_get_slot, ":party_type", ":party_no", slot_party_type),
            
            (store_sub, ":offset", ":party_no", towns_begin),
            (try_begin),
                (is_between, ":party_no", towns_begin, towns_end),
                (store_add, ":weapon_merchant", merchants_weapons_begin, ":offset"),
                (call_script, "script_troop_update_merchant_gold", ":weapon_merchant"),
            (try_end),
            
            (store_add, ":general_merchant", merchants_general_begin, ":offset"),
            
            (call_script, "script_troop_update_merchant_gold", ":general_merchant"),
        ]),
    
    # script_troop_update_merchant_gold
    ## Select the amount of gold that has to be given to troop_no depending on the merchant type he his
    # input:
    #   arg1: troop_no
    # output: none
    ("troop_update_merchant_gold",
        [
            (store_script_param, ":merchant", 1),
            
            (assign, ":base_gold", 100),
            
            (try_begin),
                (is_between, ":merchant", merchants_general_begin, merchants_general_end),
                (assign, ":base_gold", merchant_base_gold_earn_general),
            (else_try),
                # (is_between, ":merchant", merchants_weapons_begin, merchants_weapons_end),
                (assign, ":base_gold", merchant_base_gold_earn_weaponsmith),
            # (else_try),
                # (is_between, ":merchant", merchants_armors_begin, merchants_armors_end),
                # (assign, ":base_gold", merchant_base_gold_earn_armorsmith),
            # (else_try),
                # (is_between, ":merchant", merchants_goods_begin, merchants_goods_end),
                # (assign, ":base_gold", merchant_base_gold_earn_goods),
            # (else_try),
                # (is_between, ":merchant", merchants_horses_begin, merchants_horses_end),
                # (assign, ":base_gold", merchant_base_gold_earn_horses),
            (try_end),
            
            (call_script, "script_troop_add_merchant_gold", ":merchant", ":base_gold"),
        ]),
    
    # script_troop_add_merchant_gold
    ## Modify the amount of gold of a certain merchant
    ## ToDo: will need to be used for taxes
    # input:
    #   arg1: troop_no
    #   arg2: base_gold
    # output:
    #   reg0: gold_added
    ("troop_add_merchant_gold",
        [
            (store_script_param, ":merchant", 1),
            (store_script_param, ":base_gold", 2),
            
            (store_troop_gold, ":cur_gold", ":merchant"),
            (store_div, ":sub", ":cur_gold", 5),
            (store_sub, ":gold_added", ":base_gold", ":sub"),
            (store_random_in_range, ":bonus_gold", 0, 10),
            (val_add, ":gold_added", ":bonus_gold"),
            (troop_add_gold, ":merchant", ":gold_added"),
            
            (assign, reg0, ":gold_added"),
        ]),
    
    
    # script_troop_add_merchant_items_from_party
    # input:
    #   arg1: merchant
    #   arg2: party_no
    #   arg3: items
    # output: none
    ("troop_add_merchant_items_from_party",
        [
            (store_script_param, ":merchant", 1),
            (store_script_param, ":party_no", 2),
            (store_script_param, ":items", 3),
            
            (store_faction_of_party, ":party_faction", ":party_no"),
            (faction_get_slot, ":culture", ":party_faction", slot_faction_culture),
            
            (store_and, ":goods", ":items", items_good),
            (store_and, ":weapons", ":items", items_weapon),
            (store_and, ":armor", ":items", items_armor),
            (store_and, ":horse", ":items", items_horse),
            
            (troop_get_inventory_capacity, ":capacity", ":merchant"),
            (val_div, ":capacity", 2),
            (troop_ensure_inventory_space, ":merchant", ":capacity"),
            
            (assign, ":num_items", 0),
            (try_begin),
                (gt, ":weapons", 0),
                (val_add, ":num_items", 1),
            (try_end),
            (try_begin),
                (gt, ":armor", 0),
                (val_add, ":num_items", 1),
            (try_end),
            (try_begin),
                (gt, ":horse", 0),
                (val_add, ":num_items", 1),
            (try_end),
            (try_begin),
                (gt, ":goods", 0),
                (val_add, ":num_items", 1),
            (try_end),
            
            (try_begin),
                (gt, ":weapons", 0),
                (store_div, ":items", 15, ":num_items"),
                (try_begin),
                    (gt, ":goods", 0),
                    (val_div, ":items", 2),
                (try_end),
                (call_script, "script_troop_add_merchant_items_weapons", ":merchant", ":culture", ":items"),
            (try_end),
            (try_begin),
                (gt, ":armor", 0),
                
                (store_div, ":items", 15, ":num_items"),
                (try_begin),
                    (gt, ":goods", 0),
                    (val_div, ":items", 2),
                (try_end),
                (call_script, "script_troop_add_merchant_items_armors", ":merchant", ":culture", ":items"),
            (try_end),
            (try_begin),
                (gt, ":horse", 0),
                
                (store_div, ":items", 6, ":num_items"),
                (try_begin),
                    (gt, ":goods", 0),
                    (val_div, ":items", 2),
                (try_end),
                (call_script, "script_troop_add_merchant_items_horses", ":merchant", ":culture", ":items"),
            (try_end),
            (try_begin),
                (gt, ":goods", 0),
                
                (store_div, ":items", 15, ":num_items"),
                (val_mul, ":items", 3),
                (val_div, ":items", 2),
                (call_script, "script_troop_add_merchant_items_goods", ":merchant", ":culture", ":items"),
            (try_end),
            (troop_sort_inventory, ":merchant"),
        ]),
    
    # script_troop_add_merchant_items_weapons
    # input:
    #   arg1: merchant
    #   arg2: culture
    #   zrg3: num_items
    # output: none
    ("troop_add_merchant_items_weapons",
        [
            (store_script_param, ":merchant", 1),
            (store_script_param, ":culture", 2),
            (store_script_param, ":num_items", 3),
            
            (try_for_range, ":unused", 0, ":num_items"),
                (try_begin),
                    (eq, ":culture" ,fac_culture_1),
                    (store_random_in_range, ":rand", 0, 31),
                    (try_begin),
                        (lt, ":rand", 8),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_1", itp_type_one_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 12),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_1", itp_type_two_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 18),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_1", itp_type_polearm, 1),
                    (else_try),
                        (lt, ":rand", 20),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_1", itp_type_bow, 1),
                    (else_try),
                        (lt, ":rand", 22),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_1", itp_type_crossbow, 1),
                    (else_try),
                        (lt, ":rand", 23),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_1", itp_type_arrows, 1),
                    (else_try),
                        (lt, ":rand", 24),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_1", itp_type_bolts, 1),
                    (else_try),
                        (lt, ":rand", 25),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_1", itp_type_thrown, 1),
                    (else_try),
                        # (le, ":rand", 31),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_1", itp_type_shield, 1),
                    (try_end),
                (else_try),
                    (eq, ":culture", fac_culture_2),
                    (store_random_in_range, ":rand", 0, 35),
                    (try_begin),
                        (lt, ":rand", 7),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_2", itp_type_one_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 13),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_2", itp_type_two_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 19),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_2", itp_type_polearm, 1),
                    (else_try),
                        (lt, ":rand", 25),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_2", itp_type_bow, 1),
                    # (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_2", itp_type_crossbow, 0),
                    (else_try),
                        (lt, ":rand", 27),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_2", itp_type_arrows, 1),
                    # (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_2", itp_type_bolts, 0),
                    (else_try),
                        (lt, ":rand", 30),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_2", itp_type_thrown, 1),
                    (else_try),
                        # (lt, ":rand", 35),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_2", itp_type_shield, 1),
                    (try_end),
                (else_try),
                    (eq, ":culture", fac_culture_3),
                    (store_random_in_range, ":rand", 0, 34),
                    (try_begin),
                        (lt, ":rand", 8),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_3", itp_type_one_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 11),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_3", itp_type_two_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 18),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_3", itp_type_polearm, 1),
                    (else_try),
                        (lt, ":rand", 23),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_3", itp_type_bow, 1),
                    # (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_3", itp_type_crossbow, 0),
                    (else_try),
                        (lt, ":rand", 25),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_3", itp_type_arrows, 1),
                    # (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_3", itp_type_bolts, 0),
                    (else_try),
                        (lt, ":rand", 28),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_3", itp_type_thrown, 1),
                    (else_try),
                        # (lt, ":rand", 34),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_3", itp_type_shield, 1),
                    (try_end),
                (else_try),
                    (eq, ":culture", fac_culture_4),
                    (store_random_in_range, ":rand", 0, 38),
                    (try_begin),
                        (lt, ":rand", 8),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_4", itp_type_one_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 13),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_4", itp_type_two_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 18),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_4", itp_type_polearm, 1),
                    (else_try),
                        (lt, ":rand", 22),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_4", itp_type_bow, 1),
                    (else_try),
                        (lt, ":rand", 24),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_4", itp_type_crossbow, 1),
                    (else_try),
                        (lt, ":rand", 26),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_4", itp_type_arrows, 1),
                    (else_try),
                        (lt, ":rand", 27),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_4", itp_type_bolts, 1),
                    (else_try),
                        (lt, ":rand", 32),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_4", itp_type_thrown, 1),
                    (else_try),
                        # (lt, ":rand", 38),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_4", itp_type_shield, 1),
                    (try_end),
                (else_try),
                    (eq, ":culture", fac_culture_5),
                    (store_random_in_range, ":rand", 0, 36),
                    (try_begin),
                        (lt, ":rand", 8),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_5", itp_type_one_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 11),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_5", itp_type_two_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 19),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_5", itp_type_polearm, 1),
                    (else_try),
                        (lt, ":rand", 20),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_5", itp_type_bow, 1),
                    (else_try),
                        (lt, ":rand", 25),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_5", itp_type_crossbow, 1),
                    (else_try),
                        (lt, ":rand", 26),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_5", itp_type_arrows, 1),
                    (else_try),
                        (lt, ":rand", 28),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_5", itp_type_bolts, 1),
                    (else_try),
                        (lt, ":rand", 30),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_5", itp_type_thrown, 1),
                    (else_try),
                        # (lt, ":rand", 36),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_5", itp_type_shield, 1),
                    (try_end),
                (else_try),
                    (eq, ":culture", fac_culture_6),
                    (store_random_in_range, ":rand", 0, 38),
                    (try_begin),
                        (lt, ":rand", 8),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_6", itp_type_one_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 12),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_6", itp_type_two_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 17),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_6", itp_type_polearm, 1),
                    (else_try),
                        (lt, ":rand", 21),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_6", itp_type_bow, 1),
                    (else_try),
                        (lt, ":rand", 22),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_6", itp_type_crossbow, 1),
                    (else_try),
                        (lt, ":rand", 24),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_6", itp_type_arrows, 1),
                    (else_try),
                        (lt, ":rand", 25),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_6", itp_type_bolts, 1),
                    (else_try),
                        (lt, ":rand", 32),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_6", itp_type_thrown, 1),
                    (else_try),
                        # (lt, ":rand", 38),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_kingdom_6", itp_type_shield, 1),
                    (try_end),
                (else_try),
                    (store_random_in_range, ":rand", 0, 35),
                    (try_begin),
                        (lt, ":rand", 8),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_commoners", itp_type_one_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 12),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_commoners", itp_type_two_handed_wpn, 1),
                    (else_try),
                        (lt, ":rand", 19),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_commoners", itp_type_polearm, 1),
                    (else_try),
                        (lt, ":rand", 22),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_commoners", itp_type_bow, 1),
                    (else_try),
                        (lt, ":rand", 25),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_commoners", itp_type_crossbow, 1),
                    (else_try),
                        (lt, ":rand", 26),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_commoners", itp_type_arrows, 1),
                    (else_try),
                        (lt, ":rand", 27),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_commoners", itp_type_bolts, 1),
                    (else_try),
                        (lt, ":rand", 29),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_commoners", itp_type_thrown, 1),
                    (else_try),
                        # (lt, ":rand", 35),
                        (troop_add_merchandise_with_faction, ":merchant", "fac_commoners", itp_type_shield, 1),
                    (try_end),
                (try_end),
            (try_end),
        ]),
    
    # script_troop_add_merchant_items_armors
        # input:
        #   arg1: troop_no
        #   arg2: culture
        #   arg3: num_items
        # output: none
    ("troop_add_merchant_items_armors",
        [
            (store_script_param, ":merchant", 1),
            (store_script_param, ":culture", 2),
            (store_script_param, ":num_items", 3),
            
            (try_begin),
                (eq, ":culture", "fac_culture_1"),
                (assign, ":culture", "fac_kingdom_1"),
            (else_try),
                (eq, ":culture", "fac_culture_2"),
                (assign, ":culture", "fac_kingdom_2"),
            (else_try),
                (eq, ":culture", "fac_culture_3"),
                (assign, ":culture", "fac_kingdom_3"),
            (else_try),
                (eq, ":culture", "fac_culture_4"),
                (assign, ":culture", "fac_kingdom_4"),
            (else_try),
                (eq, ":culture", "fac_culture_5"),
                (assign, ":culture", "fac_kingdom_5"),
            (else_try),
                (eq, ":culture", "fac_culture_6"),
                (assign, ":culture", "fac_kingdom_6"),
            (else_try),
                (assign, ":culture", "fac_commoners"),
            (try_end),
            
            (try_for_range, ":unused", 0, ":num_items"),
                (store_random_in_range, ":rand", 0, 17),
                (try_begin),
                    (lt, ":rand", 2),
                    (troop_add_merchandise_with_faction, ":merchant", ":culture", itp_type_hand_armor, 1),
                (else_try),
                    (lt, ":rand", 5),
                    (troop_add_merchandise_with_faction, ":merchant", ":culture", itp_type_foot_armor, 1),
                (else_try),
                    (lt, ":rand", 12),
                    (troop_add_merchandise_with_faction, ":merchant", ":culture", itp_type_body_armor, 1),
                (else_try),
                    # (lt, ":rand", 17),
                    (troop_add_merchandise_with_faction, ":merchant", ":culture", itp_type_head_armor, 1),
                (try_end),
            (try_end),
        ]),
    
    # script_troop_add_merchant_items_horses
        # input: 
        #   arg1: troop_no
        #   arg2: culture
        #   arg3: num_items
        # output: none
    ("troop_add_merchant_items_horses",
        [
            (store_script_param, ":merchant", 1),
            (store_script_param, ":culture", 2),
            (store_script_param, ":num_items", 3),
            
            (try_begin),
                (eq, ":culture", "fac_culture_1"),
                (assign, ":culture", "fac_kingdom_1"),
            (else_try),
                (eq, ":culture", "fac_culture_2"),
                (assign, ":culture", "fac_kingdom_2"),
            (else_try),
                (eq, ":culture", "fac_culture_3"),
                (assign, ":culture", "fac_kingdom_3"),
            (else_try),
                (eq, ":culture", "fac_culture_4"),
                (assign, ":culture", "fac_kingdom_4"),
            (else_try),
                (eq, ":culture", "fac_culture_5"),
                (assign, ":culture", "fac_kingdom_5"),
            (else_try),
                (eq, ":culture", "fac_culture_6"),
                (assign, ":culture", "fac_kingdom_6"),
            (else_try),
                (assign, ":culture", "fac_commoners"),
            (try_end),
            
            (troop_add_merchandise_with_faction, ":merchant", ":culture", itp_type_horse, ":num_items"),
        ]),
    
    # script_troop_add_merchant_items_goods
    # input: 
    #   arg1: troop_no
    #   arg2: culture
    #   arg3: num_items
    # output: none
    ("troop_add_merchant_items_goods",
        [
            (store_script_param, ":merchant", 1),
            (store_script_param, ":culture", 2),
            (store_script_param, ":num_items", 3),
            
            (try_begin),
                (eq, ":culture", "fac_culture_1"),
                (assign, ":culture", "fac_kingdom_1"),
            (else_try),
                (eq, ":culture", "fac_culture_2"),
                (assign, ":culture", "fac_kingdom_2"),
            (else_try),
                (eq, ":culture", "fac_culture_3"),
                (assign, ":culture", "fac_kingdom_3"),
            (else_try),
                (eq, ":culture", "fac_culture_4"),
                (assign, ":culture", "fac_kingdom_4"),
            (else_try),
                (eq, ":culture", "fac_culture_5"),
                (assign, ":culture", "fac_kingdom_5"),
            (else_try),
                (eq, ":culture", "fac_culture_6"),
                (assign, ":culture", "fac_kingdom_6"),
            (else_try),
                (assign, ":culture", "fac_commoners"),
            (try_end),
            
            (troop_add_merchandise_with_faction, ":merchant", ":culture", itp_type_goods, ":num_items"),
        ]),
    
    # script_faction_process_politics
    # input:
    #   arg1: faction_no
    # output: none
    ("faction_process_politics",
        [
            (store_script_param, ":faction_no", 1),

            (faction_get_slot, ":num_fiefs", ":faction_no", slot_faction_num_fiefs),
            (faction_get_slot, ":num_vassals", ":faction_no", slot_faction_num_vassals),

            # Handle faction defeat
            # ToDo: for now only deactivate factions with no parties (center/lord)
            (try_begin),
                (eq, ":num_fiefs", 0),
                (faction_set_slot, ":faction_no", slot_faction_status, sfst_disabled),
                (try_begin),
                    (call_script, "script_cf_debug", debug_faction|debug_simple),
                    (str_store_faction_name, s11, ":faction_no"),
                    (display_message, "@{s11} disabled: no fief"),
                (try_end),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_status, sfst_disabled),
                (faction_set_slot, ":faction_no", slot_faction_status, sfst_default),
                (try_begin),
                    (call_script, "script_cf_debug", debug_faction|debug_simple),
                    (str_store_faction_name, s11, ":faction_no"),
                    (display_message, "@{s11} enabled"),
                (try_end),
            (try_end),
            
            # Distribute captured territory
            (faction_get_slot, ":center_no", ":faction_no", slot_faction_current_free_center),
            (try_begin),
                (is_between, ":center_no", centers_begin, centers_end),
                
                (store_faction_of_party, ":center_faction", ":center_no"),
                (eq, ":center_faction", ":faction_no"),
                
                (call_script, "script_faction_get_best_candidate_for_center", ":faction_no", ":center_no"),
                (assign, ":troop_no", reg0),
                
                (gt, ":troop_no", -1),
                (call_script, "script_give_center_to_troop", ":center_no", ":troop_no"),
                
                (faction_set_slot, ":faction_no", slot_faction_current_free_center, -1),
            (try_end),
            
            # Get new vassals
            (store_sub, ":diff", ":num_fiefs", ":num_vassals"),
            (try_for_range, ":unused", 0, 5),
                (gt, ":diff", 0),
                (store_random_in_range, ":add_vassal", ":diff", 6),
                (ge, ":add_vassal", 5),
                (call_script, "script_find_free_lord"),
                (assign, ":new_lord", reg0),
                (gt, ":new_lord", 0),
                (call_script, "script_ready_lord", ":new_lord", ":faction_no"),
                (try_begin),
                    (call_script, "script_cf_debug", debug_faction|debug_simple),
                    (str_store_troop_name, s10, ":new_lord"),
                    (str_store_faction_name, s11, ":faction_no"),
                    (display_message, "@{s10} joins {s11}"),
                (try_end),
                (val_sub, ":diff", 6),
            (try_end),

            # Elect leader
            (call_script, "script_faction_process_leader_selection", ":faction_no"),

            # Elect marshall
            (call_script, "script_faction_process_marshall_selection", ":faction_no"),
            
            # Recruit mercenary bands
            
            # Handle foreign diplomacy
            (call_script, "script_faction_process_foreign_politics", ":faction_no"),
            
            # Organize feasts if needed
            
            # Reduce war damage
            (faction_get_slot, ":war_damage", ":faction_no", slot_faction_war_damage),
            # (assign, ":vassals_score", ":num_vassals"),
            # (store_mul, ":fiefs_score", ":num_fiefs", 5),
            (try_begin),
                (gt, ":war_damage", 0),
                (store_div, ":damage_reduce", ":war_damage", 100),
                (val_sub, ":war_damage", ":damage_reduce"),
                (faction_set_slot, ":faction_no", slot_faction_war_damage, ":war_damage"),
            (try_end),
        ]),

    # script_faction_process_leader_selection
        # input:
        #   arg1: faction_no
        # output: none
    ("faction_process_leader_selection",
        [
            (store_script_param, ":faction_no", 1),

            (faction_get_slot, ":leader", ":faction_no", slot_faction_leader),
            (try_begin),
                # No leader
                # Or leader mandate is ended
                (lt, ":leader", 0),
                # ToDo: ended mandate

                (assign, ":best_candidate", -1),
                (assign, ":best_candidate_score", 0),
                (try_for_range, ":cur_lord", lords_begin, lords_end),
                    (store_troop_faction, ":lord_faction", ":cur_lord"),
                    (eq, ":lord_faction", ":faction_no"),
                    (troop_slot_eq, ":cur_lord", slot_troop_kingdom_occupation, tko_kingdom_hero),

                    (neg|troop_slot_ge, ":cur_lord", slot_troop_prisoner_of, 0),
                    (troop_get_slot, ":rank", ":cur_lord", slot_troop_rank),
                    (ge, ":rank", rank_castle),

                    (assign, ":score", 0),
                    # (troop_get_slot, ":renown", ":cur_lord", slot_troop_renown),
                    # (val_add, ":score", ":renown"),

                    (val_mul, ":rank", ":rank"),
                    (val_mul, ":rank", 90),
                    (val_add, ":score", ":rank"),

                    (troop_get_slot, ":num_vassals", ":cur_lord", slot_troop_num_vassal),
                    (val_mul, ":num_vassals", 150),
                    (val_add, ":score", ":num_vassals"),

                    (gt, ":score", ":best_candidate_score"),
                    (assign, ":best_candidate", ":cur_lord"),
                    (assign, ":best_candidate_score", ":score"),
                (try_end),

                (ge, ":best_candidate", 0),
                (faction_set_slot, ":faction_no", slot_faction_leader, ":best_candidate"),
                (try_begin),
                    (call_script, "script_cf_debug", debug_simple|debug_faction),
                    (str_store_troop_name, s10, ":best_candidate"),
                    (str_store_faction_name, s11, ":faction_no"),
                    (display_message, "@{s10} is the best candidate to lead {s11}."),
                (try_end),
            (try_end),
        ]),
    
    # script_faction_process_marshall_selection
        # input:
        #   arg1: faction_no
        # output: none
    ("faction_process_marshall_selection",
        [
            (store_script_param, ":faction_no", 1),

            (faction_get_slot, ":leader", ":faction_no", slot_faction_leader),
            (faction_get_slot, ":marshall", ":faction_no", slot_faction_marshall),
            (try_begin),
                # No marshall
                # At war or preparing war
                (lt, ":marshall", 0),
                (faction_get_slot, ":at_war", ":faction_no", slot_faction_is_at_war),
                (faction_get_slot, ":preparing_for_war", ":faction_no", slot_party_preparing_for_war),

                (try_begin),
                    (this_or_next|gt, ":at_war", 0),
                    (is_between, ":preparing_for_war", kingdoms_begin, kingdoms_end),

                    (assign, ":best_candidate", -1),
                    (assign, ":best_candidate_score", 0),
                    (try_for_range, ":cur_lord", lords_begin, lords_end),
                        (store_troop_faction, ":lord_faction", ":cur_lord"),
                        (eq, ":lord_faction", ":faction_no"),
                        (troop_slot_eq, ":cur_lord", slot_troop_kingdom_occupation, tko_kingdom_hero),

                        (neg|troop_slot_ge, ":cur_lord", slot_troop_prisoner_of, 0),
                        (troop_get_slot, ":rank", ":cur_lord", slot_troop_rank),
                        (ge, ":rank", rank_castle),

                        (assign, ":score", 0),
                        # (troop_get_slot, ":renown", ":cur_lord", slot_troop_renown),
                        # (val_add, ":score", ":renown"),

                        (val_mul, ":rank", ":rank"),
                        (val_mul, ":rank", 90),
                        (val_add, ":score", ":rank"),

                        (troop_get_slot, ":num_vassals", ":cur_lord", slot_troop_num_vassal),
                        (val_mul, ":num_vassals", 30),
                        (val_add, ":score", ":num_vassals"),

                        (try_begin),
                            (eq, ":cur_lord", ":leader"),
                            (val_sub, ":score", 100),
                        (try_end),

                        (gt, ":score", ":best_candidate_score"),
                        (assign, ":best_candidate", ":cur_lord"),
                        (assign, ":best_candidate_score", ":score"),
                    (try_end),

                    (ge, ":best_candidate", 0),
                    (faction_set_slot, ":faction_no", slot_faction_marshall, ":best_candidate"),
                    (try_begin),
                        (call_script, "script_cf_debug", debug_simple|debug_faction),
                        (str_store_troop_name, s10, ":best_candidate"),
                        (str_store_faction_name, s11, ":faction_no"),
                        (display_message, "@{s10} is the best candidate for marshall of {s11}."),
                    (try_end),
                (try_end),
            (else_try),
                (faction_get_slot, ":at_war", ":faction_no", slot_faction_is_at_war),
                (faction_get_slot, ":preparing_for_war", ":faction_no", slot_party_preparing_for_war),
                (try_begin),
                    (this_or_next|gt, ":at_war", 0),
                    (is_between, ":preparing_for_war", kingdoms_begin, kingdoms_end),

                    (troop_slot_ge, ":marshall", slot_troop_prisoner_of, 0),
                    (try_begin),
                        (call_script, "script_cf_debug", debug_simple|debug_faction),
                        (str_store_troop_name, s10, ":marshall"),
                        (str_store_faction_name, s11, ":faction_no"),
                        (display_message, "@{s10} removed of marshallship from {s11} for being prisoner."),
                    (try_end),
                (else_try),
                    (faction_set_slot, ":faction_no", slot_faction_marshall, -1),
                    (try_begin),
                        (call_script, "script_cf_debug", debug_simple|debug_faction),
                        (str_store_troop_name, s10, ":marshall"),
                        (str_store_faction_name, s11, ":faction_no"),
                        (display_message, "@{s10} removed of marshallship from {s11} for peace time."),
                    (try_end),
                (try_end),
            (try_end),
        ]),

    # script_faction_process_foreign_politics
        # input:
        #   arg1: faction_no
        # output: none
    ("faction_process_foreign_politics",
        [
            (store_script_param, ":faction_no", 1),
            (faction_get_slot, ":own_wars", ":faction_no", slot_faction_is_at_war),
            (try_for_range, ":other_faction", kingdoms_begin, kingdoms_end),
                # (store_sub, ":offset", ":other_faction", kingdoms_begin),
                # (store_add, ":relation_slot", ":offset", slot_faction_kingdom_relation_begin),
                # (faction_get_slot, ":relation", ":faction_no", ":relation_slot"),

                (store_relation, ":rel", ":faction_no", ":other_faction"),
                (try_begin),
                    (le, ":rel", relation_state_war),
                    # Decide whether to make ask for peace if needed (own damage is too high, too many centers at war, war lasting for too long)
                (else_try),
                    (ge, ":rel", relation_state_friendly),
                    (faction_get_slot, ":ally_wars", ":other_faction", slot_faction_is_at_war),
                    (neq, ":own_wars", ":ally_wars"),
                    # Process wether to make peace with own wars or declare war on ally_wars
                (else_try),
                    (le, ":rel", relation_state_conflict),
                    # Process whether to declare war
                (else_try),
                    # Neutral relations vary slowly based on common enemies, and borders
                    # Most of the relation changes will be done through events (border incident...)
                (try_end),
            (try_end),
        ]),
    
    # script_troop_get_title_string
    # input: 
    #   arg1: troop_no
    #output:
    #   str0: title
    ("troop_get_title_string",
        [
            (store_script_param, ":troop_no", 1),
            (assign, reg10, 0), # Num titles
            
            (str_clear, s10),
            
            (store_troop_faction, ":troop_faction", ":troop_no"),
            (try_begin),
                (faction_slot_eq, ":troop_faction", slot_faction_leader, ":troop_no"),
                (str_store_faction_name, s11, ":troop_faction"),
                (str_store_string, s10, "@Ruler of the {s11}"),
                (val_add, reg10, 2),
            (try_end),
            
            (call_script, "script_troop_get_home", ":troop_no", 0),
            (assign, ":home", reg0),
            (try_begin),
                (is_between, ":home", centers_begin, centers_end),
                (party_slot_eq, ":home", slot_party_lord, ":troop_no"),
                (troop_get_type, reg11, ":troop_no"),
                (str_store_party_name, s11, ":home"),
                (str_store_string, s10, "@{s10}{reg10?, l:L}{reg11?ady:ord} of {s11}"),
                (try_begin),
                    (is_between, ":home", walled_centers_begin, walled_centers_end),
                    (val_add, reg10, 2),
                (else_try),
                    (val_add, reg10, 1),
                (try_end),
            (try_end),
            
            (try_begin),
                (le, reg10, 1),
                (troop_get_slot, ":lord", ":troop_no", slot_troop_vassal_of),
                (ge, ":lord", 0),
                (str_store_troop_name, s11, ":lord"),
                (str_store_string, s10, "@{s10}{reg10?, v:V}assal of {s11}"),
                (val_add, reg10, 2),
            (try_end),
            
            (try_begin),
                (le, reg10, 1),
                (str_store_faction_name, s11, ":troop_faction"),
                (str_store_string, s10, "@{s10}{reg10?, v:V}assal for the {s11}"),
                (val_add, reg10, 2),
            (try_end),
            
            # Family strings (son/daughter of, wife/husband of, father/mother of) -- only important persons!
            
            # Some important traits (self imposed?)
            
            (str_store_string_reg, s0, s10),
        ]),
    
    # script_party_besiege_party
        # input:
        #   arg1: attacker
        #   arg2: besieged
        # output: none
    ("party_besiege_party",
        [
            (store_script_param, ":attacker", 1),
            (store_script_param, ":besieged", 2),
            
            (party_set_slot, ":besieged", slot_party_besieged_by, ":attacker"),
            
            (call_script, "script_party_update_extra_text", ":besieged"),
            
            (str_store_party_name_link, s10, ":besieged"),
            (try_begin),
                (party_get_slot, ":leader", ":attacker", slot_party_leader),
                (ge, ":leader", 0),
                (str_store_troop_name_link, s11, ":leader"),
                (display_log_message, "@{s10} is been besieged by {s11}"),
            (else_try),
                (display_log_message, "@{s10} is been besieged"),
            (try_end),
            
            (party_get_slot, ":besieged_lord", ":besieged", slot_party_lord),
            (try_begin),
                (gt, ":besieged_lord", 0),
                (troop_get_slot, ":besieged_lord_party", ":besieged_lord", slot_troop_leaded_party),
                (gt, ":besieged_lord_party", 0),
                (call_script, "script_party_process_mission", ":besieged_lord_party", 1),
            (try_end),
        ]),
    
    # script_party_lift_siege
        # input:
        #   arg1: besieged_party
        # output: none
    ("party_lift_siege",
        [
            (store_script_param, ":party_no", 1),
            
            (party_set_slot, ":party_no", slot_party_besieged_by, -1),
            
            (call_script, "script_party_update_extra_text", ":party_no"),
            
            (str_store_party_name_link, s10, ":party_no"),
            (display_log_message, "@{s10} is no longer under siege"),
        ]),

    # script_party_update_extra_text
        # input:
        #   arg1: party_no
        # output: none
    ("party_update_extra_text",
        [
            (store_script_param, ":party_no", 1),

            (party_get_slot, ":party_type", ":party_no", slot_party_type),
            (try_begin),
                (is_between, ":party_type", spt_village, spt_fort),
                (try_begin),
                    (party_get_slot, ":besieger", ":party_no", slot_party_besieged_by),
                    (ge, ":besieger", 0),

                    (party_set_extra_text, ":party_no", "@Under siege"),
                (else_try),
                    (party_get_slot, ":party_faction", ":party_no", slot_party_faction),
                    (store_faction_of_party, ":current_faction", ":party_no"),
                    (neq, ":party_faction", ":current_faction"),

                    (str_store_faction_name, s11, ":party_faction"),
                    (str_store_string, s10, "@Occupied from {s11}"),
                    (party_set_extra_text, ":party_no", s10),
                (else_try),
                    (party_set_extra_text, ":party_no", "str_empty_string"),
                (try_end),
            (try_end),
        ]),
    
    # script_party_defeat_center
    # inout:
    #   arg1: party_no
    #   arg2: center_captured
    # output: none
    ("party_defeat_center",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":center_no", 2),
            
            (store_faction_of_party, ":party_faction", ":party_no"),
            # (store_faction_of_party, ":old_center_faction", ":center_no"),
            (party_get_slot, ":center_owner_faction", ":center_no", slot_party_faction),
            
            # Does not capture attached parties
            (party_get_num_attached_parties, ":num_attached", ":center_no"),
            (try_for_range, ":rank_no", 0, ":num_attached"),
                (party_get_attached_party_with_rank, ":attached_party", ":center_no", ":rank_no"),
                (party_detach, ":attached_party"),
            (try_end),
            
            (try_begin),
                (party_slot_ge, ":center_no", slot_party_besieged_by, 0),
                (call_script, "script_party_lift_siege", ":center_no"),
            (try_end),

            (try_begin),
                (store_relation, ":relation", ":party_faction", ":center_owner_faction"),
                (ge, ":relation", 0),
                (call_script, "script_party_free_center", ":party_no", ":center_no"),
            (else_try),
                (call_script, "script_party_capture_center", ":party_no", ":center_no"),
            (try_end),
        ]),
    
    # script_party_free_center
    # inout:
    #   arg1: party_no
    #   arg2: center_freed
    # output: none
    ("party_free_center",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":center_no", 2),

            (store_faction_of_party, ":party_faction", ":party_no"),
            (party_get_slot, ":center_owner_faction", ":center_no", slot_party_faction),
            (store_faction_of_party, ":old_center_faction", ":center_no"),
            
            (call_script, "script_faction_political_event", ":party_faction", political_event_center_freed, ":center_no", ":party_no", ":old_center_faction"),

            (call_script, "script_center_change_current_faction", ":center_no", ":center_owner_faction", ":old_center_faction"),
        ]),
    
    # script_party_capture_center
    # inout:
    #   arg1: party_no
    #   arg2: center_captured
    # output: none
    ("party_capture_center",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":center_no", 2),
            
            (store_faction_of_party, ":party_faction", ":party_no"),
            (store_faction_of_party, ":old_center_faction", ":center_no"),
            
            (call_script, "script_faction_political_event", ":party_faction", political_event_center_captured, ":center_no", ":party_no", -1),

            (call_script, "script_center_change_current_faction", ":center_no", ":party_faction", ":old_center_faction"),
        ]),

    # script_get_faction_size_from_weight
        # input:
        #   arg1: weight (1 for castle, 5 for towns)
        # output:
        #   reg0: faction_size (sfs_)
    ("get_faction_size_from_weight",
        [
            (store_script_param, ":weight", 1),

            (assign, ":size", sfs_small),
            (try_begin),
                (ge, ":weight", 9),
                (assign, ":size", sfs_large),
            (else_try),
                (ge, ":weight", 5),
                (assign, ":size", sfs_medium),
            (try_end),

            (assign, reg0, ":size"),
        ]),

    # script_center_change_current_faction
        # input:
        #   arg1: center_no
        #   arg2: new_faction
        #   arg2: old_faction
        # output: none
    ("center_change_current_faction",
        [
            (store_script_param, ":center_no", 1),
            (store_script_param, ":new_faction", 2),
            # (store_script_param, ":old_faction", 3),

            (party_set_faction, ":center_no", ":new_faction"),
            
            (call_script, "script_party_update_extra_text", ":center_no"),
            
            (party_get_slot, ":leader", ":center_no", slot_party_leader),
            (try_begin),
                (ge, ":leader", 0),
                (call_script, "script_troop_update_home", ":leader"),
            (try_end),
        ]),

    # script_center_change_faction
        # input:
        #   arg1: center_no
        #   arg2: new_faction
        #   arg2: old_faction
        # output: none
    ("center_change_faction",
        [
            (store_script_param, ":center_no", 1),
            (store_script_param, ":new_faction", 2),
            (store_script_param, ":old_faction", 3),

            (party_set_slot, ":center_no", slot_party_faction, ":new_faction"),
            (party_set_faction, ":center_no", ":new_faction"),
            
            (call_script, "script_party_update_extra_text", ":center_no"),

            (party_get_slot, ":leader", ":center_no", slot_party_leader),
            (try_begin),
                (ge, ":leader", 0),
                (store_troop_faction, ":leader_faction", ":leader"),
                (neq, ":leader_faction", ":new_faction"),
                (party_set_slot, ":center_no", slot_party_leader, -1),
                
                (call_script, "script_troop_get_rank", ":leader"),
                (assign, ":rank", reg0),
                (troop_set_slot, ":leader", slot_troop_rank, ":rank"),
                
                (call_script, "script_troop_update_name", ":leader"),
                (call_script, "script_troop_update_home", ":leader"),
            (try_end),

            (call_script, "script_faction_update_size", ":new_faction"),
            (call_script, "script_faction_update_size", ":old_faction"),
        ]),

    # script_faction_update_size
        # input:
        #   arg1: faction_no
        # output: none
    ("faction_update_size",
        [
            (store_script_param, ":new_faction", 1),

            (assign, ":new_faction_weight", 0),
            (assign, ":new_faction_num_fiefs", 0),
            (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
                (store_faction_of_party, ":center_faction", ":cur_center"),
                (try_begin),
                    (eq, ":center_faction", ":new_faction"),
                    (party_get_slot, ":party_type", ":cur_center", slot_party_type),
                    (assign, ":center_weight", 0),
                    (try_begin),
                        (eq, ":party_type", spt_castle),
                        (assign, ":center_weight", 1),
                    (else_try),
                        (eq, ":party_type", spt_town),
                        (assign, ":center_weight", 5),
                    (try_end),


                    (val_add, ":new_faction_weight", ":center_weight"),
                    (val_add, ":new_faction_num_fiefs", 1),
                (try_end),
            (try_end),

            (faction_get_slot, ":new_faction_old_size", ":new_faction", slot_faction_size),

            (call_script, "script_get_faction_size_from_weight", ":new_faction_weight"),
            (assign, ":new_faction_new_size", reg0),

            (faction_set_slot, ":new_faction", slot_faction_num_fiefs, ":new_faction_num_fiefs"),
            (try_begin),
                (neq, ":new_faction_old_size", ":new_faction_new_size"),
                (faction_set_slot, ":new_faction", slot_faction_size, ":new_faction_new_size"),
                (call_script, "script_faction_update_name", ":new_faction"),
            (try_end),
        ]),

    # script_faction_update_name
        # input: 
        #   arg1: faction_no
        # output: none
    ("faction_update_name",
        [
            (store_script_param, ":faction_no", 1),
            (try_begin),
                (faction_slot_eq, ":faction_no", slot_faction_has_fixed_name, 0),
                (faction_get_slot, ":culture", ":faction_no", slot_faction_culture),
                (store_sub, ":offset", ":culture", cultures_begin),
                (faction_get_slot, ":size", ":faction_no", slot_faction_size),
                (faction_get_slot, ":name_holder", ":faction_no", slot_faction_name_holder),

                (val_mul, ":offset", faction_size_names_count),
                (val_add, ":offset", ":size"),

                (store_add, ":size_name", faction_size_names_begin, ":offset"),

                (str_store_party_name, s0, ":name_holder"),
                (str_store_string, s10, ":size_name"),
                (faction_set_name, ":faction_no", s10),

                (try_begin),
                    (call_script, "script_cf_debug", debug_simple|debug_faction),
                    (str_store_party_name, s11, ":name_holder"),
                    (str_store_faction_name, s12, ":faction_no"),
                    (assign, reg11, ":offset"),
                    (assign, reg12, ":size"),
                    (display_message, "@{s11} is now named {s12}. offset: {reg11}, size: {reg12}."),
                (try_end),
            (try_end),
        ]),
    
    # script_cf_merchant_can_update
        # input:
        #   arg1: troop_no
        # output:
        #   reg0: num_times
        #   fails if merchant can't update goods (last met within less than merchants_update_rate)
    ("cf_merchant_can_update",
        [
            (store_script_param, ":merchant", 1),
            
            (troop_get_slot, ":last_met", ":merchant", slot_troop_last_met),
            (store_current_hours, ":date"),
            (troop_set_slot, ":merchant", slot_troop_last_met, ":date"),
            (store_div, ":last_met_mod", ":last_met", merchants_update_rate),
            (val_div, ":date", merchants_update_rate),
            
            (store_sub, ":time_passed", ":date", ":last_met_mod"),
            (gt, ":time_passed", 0),
            (val_min, ":time_passed", 10),
            (try_begin),
                (call_script, "script_cf_debug", debug_economy|debug_simple),
                (assign, reg0, ":time_passed"),
                (display_message, "@Updating merchant goods ({reg0} times)."),
            (try_end),
            (assign, reg0, ":time_passed"),
        ]),
    
    # script_troop_get_face_code
        # input: 
        #   arg1: troop_no
        # output:
        #   s0: facecode
    ("troop_get_face_code",
        [
            (store_script_param, ":troop_no", 1),
            (str_store_troop_face_keys, s0, ":troop_no"),
            
            (store_troop_faction, ":faction_no", ":troop_no"),
            (faction_get_slot, ":culture", ":faction_no", slot_faction_culture),
            (troop_get_type, ":type", ":troop_no"),
            
            (try_begin),
                (eq, ":type", tf_male),
                (call_script, "script_set_random_faction_hair", ":culture"),
                (call_script, "script_set_random_faction_beard", ":culture"),
                (call_script, "script_set_random_faction_face_texture", ":culture"),
                # (call_script, "script_set_random_faction_hair_texture", ":culture"),
                (call_script, "script_set_random_faction_hair_color", ":culture"),
                # (call_script, "script_set_random_faction_skin_color", ":culture"),
                (call_script, "script_set_random_faction_morph_key", ":culture"),
            (else_try),
                # Need to add scripts for female randomization
            (try_end),
        ]),

    # script_troop_copy_face_code_from_troop
        # input: 
        #   arg1: troop_no
        #   arg2: troop_no_to_copy
        # output: none
    ("troop_copy_face_code_from_troop",
        [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":troop_no_2", 2),

            (str_store_troop_face_keys, s0, ":troop_no_2", 1),
            (troop_set_face_keys, ":troop_no", s0, 1),

            (str_store_troop_face_keys, s1, ":troop_no_2", 2),
            (troop_set_face_keys, ":troop_no", s1, 2),
        ]),

    # script_troop_copy_face_code
        # input: 
        #   arg1: troop_no
        #   arg2: face_code
        # output: none
    # ("troop_copy_face_code", 
    #     [
    #         (store_script_param, ":troop_no", 1),
    #         (store_script_param, ":face_key", 2),
    #     ]),
    
    # script_set_random_faction_hair
        # input: 
        #   arg1: faction_no
        #   s0: face_key
        # output:
        #   s0: new_face_key
    ("set_random_faction_hair",
        [
            (store_script_param, ":faction_no", 1),
            (assign, ":value", 0),
            (try_begin),
                (eq, ":faction_no", fac_culture_1),
                (store_random_in_range, ":value", 0, 16),
                (try_begin),
                    (ge, ":value", 9),
                    (val_add, ":value", 5),
                (try_end),
            (else_try),
                (eq, ":faction_no", fac_culture_2),
                (store_random_in_range, ":value", 0, 13),
                (try_begin),
                    (eq, ":value", 2),
                    (assign, ":value", 13),
                (try_end),
            (else_try),
                (eq, ":faction_no", fac_culture_3),
                (store_random_in_range, ":value", 7, 14),
            (else_try),
                (eq, ":faction_no", fac_culture_4),
                (store_random_in_range, ":value", 3, 12),
            (else_try),
                (eq, ":faction_no", fac_culture_5),
                (store_random_in_range, ":value", 0, 13),
                (try_begin),
                    (is_between, ":value", 1, 4),
                    (val_add, ":value", 3),
                (else_try),
                    (ge, ":value", 5),
                    (val_add, ":value", 8),
                (try_end),
            (else_try),
                (eq, ":faction_no", fac_culture_6),
                (store_random_in_range, ":value", 0, 8),
                (try_begin),
                    (is_between, ":value", 1, 8),
                    (val_add, ":value", 3),
                (try_end),
            (try_end),
            (face_keys_set_hair, s0, ":value"),
        ]),
        
    # script_set_random_faction_beard
    # input: 
    #   arg1: faction_no
    #   s0: face_key
    # output:
    #   s0: new_face_key
    ("set_random_faction_beard",
        [
            # (store_script_param, ":faction_no", 1),
        ]),
        
    # script_set_random_faction_face_texture
    # input: 
    #   arg1: faction_no
    #   s0: face_key
    # output:
    #   s0: new_face_key
    ("set_random_faction_face_texture",
        [
            (store_script_param, ":faction_no", 1),
            (assign, ":value", 0),
            (try_begin),
                (eq, ":faction_no", fac_culture_1),
                (store_random_in_range, ":value", 1, 4),
            (else_try),
                (eq, ":faction_no", fac_culture_2),
                (store_random_in_range, ":value", 0, 3),
            (else_try),
                (eq, ":faction_no", fac_culture_3),
                (store_random_in_range, ":value", 3, 5),
            (else_try),
                (eq, ":faction_no", fac_culture_4),
                (store_random_in_range, ":value", 0, 2),
            (else_try),
                (eq, ":faction_no", fac_culture_5),
                (store_random_in_range, ":value", 3, 6),
                (try_begin),
                    (eq, ":value", 4),
                    (assign, ":value", 6),
                (try_end),
            (else_try),
                (eq, ":faction_no", fac_culture_6),
                (store_random_in_range, ":value", 6, 8),
            (try_end),
            (face_keys_set_face_texture, s0, ":value"),
        ]),
        
    # script_set_random_faction_hair_texture
    # input: 
    #   arg1: faction_no
    #   s0: face_key
    # output:
    #   s0: new_face_key
    # ("set_random_faction_hair_texture",
        # [
            # (store_script_param, ":faction_no", 1),
        # ]),
        
    # script_set_random_faction_hair_color
    # input: 
    #   arg1: faction_no
    #   s0: face_key
    # output:
    #   s0: new_face_key
    ("set_random_faction_hair_color",
        [
            (store_script_param, ":faction_no", 1),
            (assign, ":value", 0),
            (try_begin),
                (eq, ":faction_no", fac_culture_1),
                (store_random_in_range, ":value", 20, 64),
            (else_try),
                (eq, ":faction_no", fac_culture_2),
                (store_random_in_range, ":value", 10, 50),
            (else_try),
                (eq, ":faction_no", fac_culture_3),
                (store_random_in_range, ":value", 30, 64),
            (else_try),
                (eq, ":faction_no", fac_culture_4),
                (store_random_in_range, ":value", 0, 30),
            (else_try),
                (eq, ":faction_no", fac_culture_5),
                (store_random_in_range, ":value", 30, 64),
            (else_try),
                (eq, ":faction_no", fac_culture_6),
                (store_random_in_range, ":value", 30, 64),
            (try_end),
            (face_keys_set_hair_color, s0, ":value"),
        ]),
        
    # script_set_random_faction_skin_color
    # input: 
    #   arg1: faction_no
    #   s0: face_key
    # output:
    #   s0: new_face_key
    # ("set_random_faction_skin_color",
        # [
            # (store_script_param, ":faction_no", 1),
        # ]),
        
    # script_set_random_faction_morph_key
    # input: 
    #   arg1: faction_no
    #   s0: face_key
    # output:
    #   s0: new_face_key
    ("set_random_faction_morph_key",
        [
            # (store_script_param, ":faction_no", 1),
        ]),
    
    # script_find_free_lord
    # input: none
    # output:
    #   reg0: troop_no
    ("find_free_lord",
        [
            (assign, ":end", 1000),
            (try_for_range, ":unused", 0, ":end"),
                (try_begin),
                    (is_between, "$g_cur_free_lord", lords_begin, lords_end),
                    (troop_get_slot, ":occupation", "$g_cur_free_lord", slot_troop_kingdom_occupation),
                    (try_begin),
                        (eq, ":occupation", tko_none),
                        (store_troop_faction, ":lord_faction", "$g_cur_free_lord"),
                        (eq, ":lord_faction", fac_commoners),
                        (assign, ":end", 0),
                    (try_end),
                    (val_add, "$g_cur_free_lord", 1),
                (else_try),
                    (assign, "$g_cur_free_lord", lords_begin),
                (try_end),
            (try_end),
            
            (try_begin),
                # We don't have enough lords in the lord pool, we can create more
                # Should it be an error ? So that the limit can be further increased next time
                # Or to report potential lord leaks (lords not active but not removed)
                (eq, ":end", 1000),
                (try_begin),
                    (call_script, "script_cf_debug", debug_all),
                    (display_message, "@ERROR: Lord pool empty!", text_color_impossible),
                (else_try),
                    (display_debug_message, "@ERROR: Lord pool empty!", text_color_impossible),
                (try_end),
                (assign, reg0, -1),
            (else_try),
                (store_sub, reg0, "$g_cur_free_lord", 1),
            (try_end),
        ]),
    
    # script_cf_party_join_battle
    # input:
    #   arg1: party_no
    #   arg2: battling_party_1
    #   arg3: battling_party_2
    # output:
    #   reg0: battle_side
    ("cf_party_join_battle",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":battling_party_1", 2),
            (store_script_param, ":battling_party_2", 3),
            
            (party_is_active, ":party_no"),
            (neq, ":party_no", "$g_encountered_party"),
            (neq, ":party_no", "$g_encountered_party_2"),
            (party_get_slot, ":party_type", ":party_no", slot_party_type),
            (eq, ":party_type", spt_war_party),
            (party_get_attached_to, ":attached_party", ":party_no"),
            (lt, ":attached_party", 0),
            (store_distance_to_party_from_party, ":distance", ":party_no", "$g_encountered_party"),
            (lt, ":distance", reinforcement_range),
            (call_script, "script_party_select_battle_side", ":party_no", ":battling_party_1", ":battling_party_2"),
        ]),
    
    # script_agent_get_archer_score
        # input:
        #   arg1: agent_no
        # output:
        #   reg0: archer_score
    ("agent_get_archer_score",
        [
            (store_script_param, ":agent_no", 1),
            (agent_get_troop_id, ":troop_no", ":agent_no"),
            (assign, ":score", 0),
            
            (try_begin),
                (neg|troop_is_hero, ":troop_no"),
                (troop_get_slot, ":score", ":troop_no", slot_troop_archer_score),
                (assign, ":has_shield", 0),
                (store_add, ":end", ek_item_3, 1),
                (try_for_range, ":i_slot", ek_item_0, ":end"),
                    (agent_get_item_slot, ":item", ":agent_no", ":i_slot"),
                    (is_between, ":item", shields_begin, shields_end),
                    (assign, ":has_shield", 1),
                    (assign, ":end", 0),
                (try_end),
                (try_begin),
                    (eq, ":has_shield", 1),
                    (val_sub, ":score", archer_score_shield_malus),
                (try_end),
            # (else_try),
            #     # Need troops personalities to handle score
            #     (assign, ":has_shield", 0),
            #     (assign, ":has_ranged", 0),
            #     (store_add, ":end", ek_item_3, 1),
            #     (try_for_range, ":i_slot", ek_item_0, ":end"),
            #         (agent_get_item_slot, ":item", ":agent_no", ":i_slot"),
            #         (item_get_type, ":item_type", ":item"),
            #         (try_begin),
            #             (eq, ":item_type", itp_type_shield),
            #             (assign, ":has_shield", 1),
            #         (else_try),
            #             (this_or_next|eq, ":item_type", itp_type_thrown),
            #             (this_or_next|eq, ":item_type", itp_type_crossbow),
            #             (eq, ":item_type", itp_type_bow),
            #             (this_or_next|eq, ":has_ranged", 0),
            #             (eq, ":has_ranged", itp_type_thrown), # Override thrown weapon if better ranged is available
            #             (assign, ":has_ranged", ":item_type"),
            #         (try_end),
            #     (try_end),

            (try_end),
            
            (assign, reg0, ":score"),
        ]),
    
    # script_faction_damage_faction
        # input:
        #   arg1: dealing_faction
        #   arg2: receiving_faction
        #   arg3: damage_amount
        #   arg4: forced -- if forced then we do not decrease the dealing faction's war_damage
        # output:
        #   reg0: total_war_damage
    ("faction_damage_faction",
        [
            (store_script_param, ":dealing_faction", 1),
            (store_script_param, ":receiving_faction", 2),
            (store_script_param, ":damage_amount", 3),
            (store_script_param, ":forced", 4),
            
            (faction_get_slot, ":current_damage", ":receiving_faction", slot_faction_war_damage),
            (store_add, ":total_damage", ":current_damage", ":damage_amount"),
            (faction_set_slot, ":receiving_faction", slot_faction_war_damage, ":total_damage"),
            
            (try_begin),
                (eq, ":forced", 0),
                # Decrease dealing faction's war damage
                (faction_get_slot, ":current_damage", ":dealing_faction", slot_faction_war_damage),
                (store_div, ":damage_reduced", ":damage_amount", war_damage_inflicted_bonus_divider),
                (val_sub, ":current_damage", ":damage_reduced"),
                (faction_set_slot, ":dealing_faction", slot_faction_war_damage, ":current_damage"),
            (try_end),
            
            (assign, reg0, ":total_damage"),
        ]),
    
    # script_transform_war_damage_to_relation_change
        # input:
        #   arg1: war_damage
        # output:
        #   reg0: relation_change
    ("transform_war_damage_to_relation_change",
        [
            (store_script_param, ":war_damage", 1),
            
            (store_div, ":relation_change", ":war_damage", 10),
            (store_mod, ":relation_change_rand", ":war_damage", 10),
            (store_random_in_range, ":rand", 0, 10),
            (try_begin),
                (gt, ":relation_change_rand", ":rand"),
                (val_add, ":relation_change", 1),
            (try_end),
            (val_mul, ":relation_change", -1),
            
            (assign, reg0, ":relation_change"),
        ]),
    
    # script_faction_change_relation_with_faction
        # input:
        #   arg1: faction_1
        #   arg2: faction_2
        #   arg3: relation_change
        #   arg4: send_event
        # output:
        #   reg0: new_relation
    ("faction_change_relation_with_faction",
        [
            (store_script_param, ":faction_1", 1),
            (store_script_param, ":faction_2", 2),
            (store_script_param, ":relation_change", 3),
            (store_script_param, ":send_event", 4),

            (store_sub, ":offset", ":faction_2", kingdoms_begin),
            (store_add, ":relation_slot", slot_faction_kingdom_relation_begin, ":offset"),
            (faction_get_slot, ":current_relation", ":faction_1", ":relation_slot"),
            (assign, ":new_relation", ":current_relation"),

            (try_begin),
                (neq, ":relation_change", 0),
                (store_add, ":new_relation", ":current_relation", ":relation_change"),
                (val_clamp, ":new_relation", -100, 101),

                (try_begin),
                    (eq, ":send_event", 1),
                    (call_script, "script_faction_political_event", ":faction_1", political_event_relation_change, ":faction_2", ":new_relation", ":relation_change"),
                (try_end),
                
                (try_begin),
                    (neq, ":new_relation", ":current_relation"),
                    (faction_set_slot, ":faction_1", ":relation_slot", ":new_relation"),
                    
                    (call_script, "script_cf_debug", debug_faction),
                    (str_store_faction_name, s10, ":faction_1"),
                    (str_store_faction_name, s11, ":faction_2"),
                    (assign, reg10, ":current_relation"),
                    (assign, reg11, ":new_relation"),
                    (display_message, "@{s10} and {s11} relation was {reg10}, now {reg11}"),
                (try_end),
            (try_end),
            
            (assign, reg0, ":new_relation"),
        ]),
    
    # script_faction_political_event
        # input:
        #   arg1: faction_no
        #   arg2: event_type
        #   arg3: parameter_1
        #   arg4: parameter_2
        #   arg5: parameter_3
        # output: 
        #   reg0: event_output (0: event ignored, 1: event processed)
    ("faction_political_event",
        [
            (store_script_param, ":faction_no", 1),
            (store_script_param, ":event_type", 2),
            (store_script_param, ":parameter_1", 3),
            (store_script_param, ":parameter_2", 4),
            (store_script_param, ":parameter_3", 5),

            (assign, ":output", 0),

            (try_begin),
                (eq, ":event_type", political_event_relation_change),
            (else_try),
                (eq, ":event_type", political_event_war_declared),
                (call_script, "script_faction_political_event_war_declared", ":faction_no", ":parameter_1"),
            (else_try),
                (eq, ":event_type", political_event_center_freed),
                (call_script, "script_faction_political_event_center_freed", ":faction_no", ":parameter_1", ":parameter_2", ":parameter_3"),
            (else_try),
                (eq, ":event_type", political_event_center_captured),
                (call_script, "script_faction_political_event_center_captured", ":faction_no", ":parameter_1", ":parameter_2"),
            (else_try),
                (eq, ":event_type", political_event_vassal_captured),
                (call_script, "script_faction_political_event_vassal_captured", ":faction_no", ":parameter_1", ":parameter_2"),
            (else_try),
                (eq, ":event_type", political_event_vassal_freed),
                (call_script, "script_faction_political_event_vassal_freed", ":faction_no", ":parameter_1", ":parameter_2"),
            (try_end),
            
            (try_begin),
                (call_script, "script_cf_debug", debug_faction),
                (try_begin),
                    (ge, ":faction_no", 0),
                    (str_store_faction_name, s10, ":faction_no"),
                (else_try),
                    (str_store_string, s10, "@Unknown faction"),
                (try_end),
                (assign, reg10, ":event_type"),
                (assign, reg11, ":output"),
                (display_message, "@{s10} event: {reg10} {reg11?processed:ignored}"),
            (try_end),
            (assign, reg0, ":output"),
        ]),

    # script_faction_political_event_war_declared
        # input:
        #   arg1: faction_attacker
        #   arg2: faction_defender
    ("faction_political_event_war_declared",
        [
            (store_script_param, ":faction_attacker", 1),
            (store_script_param, ":faction_defender", 2),

            (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
                (neq, ":faction_no", ":faction_attacker"),
                (neq, ":faction_no", ":faction_defender"),
                (store_relation, ":relation_attacker", ":faction_no", ":faction_attacker"),
                (store_relation, ":relation_defender", ":faction_no", ":faction_defender"),

                (store_sub, ":offset", ":faction_no", kingdoms_begin),
                (store_add, ":treaties_slot", ":offset", slot_faction_kingdom_treaties_begin),

                (faction_get_slot, ":treaty_defender", ":faction_defender", ":treaties_slot"),
                (faction_get_slot, ":treaty_attacker", ":faction_attacker", ":treaties_slot"),

                (faction_get_slot, ":vassal_type", ":faction_no", slot_faction_vassal_type),
                (faction_get_slot, ":vassal_type_defender", ":faction_defender", slot_faction_vassal_type),
                # (faction_get_slot, ":vassal_type_attacker", ":faction_attacker", slot_faction_vassal_type),

                (store_and, ":alliance_defender", ":treaty_defender", sfkt_alliance),
                (store_and, ":defensive_defender", ":treaty_defender", sfkt_defensive_alliance),
                (store_and, ":vassal_defender", ":treaty_defender", sfkt_vassal),
                (store_and, ":overlord_defender", ":treaty_defender", sfkt_overlord),

                (store_and, ":alliance_attacker", ":treaty_attacker", sfkt_alliance),
                # (store_and, ":defensive_attacker", ":treaty_attacker", sfkt_defensive_alliance),
                # (store_and, ":vassal_attacker", ":treaty_attacker", sfkt_vassal),
                (store_and, ":overlord_attacker", ":treaty_attacker", sfkt_overlord),

                (assign, ":must_declare_attacker", 0),
                (assign, ":must_declare_defender", 0),

                (try_begin),
                    (this_or_next|gt, ":alliance_defender", 0),
                    (gt, ":defensive_defender", 0),

                    (assign, ":must_declare_attacker", 1),
                (else_try),
                    (gt, ":vassal_defender", 0),

                    (store_and, ":is_bulwark", ":vassal_type", sfvt_bulwark),
                    (gt, ":is_bulwark", 0),
                    (assign, ":must_declare_attacker", 1),
                (else_try),
                    (gt, ":overlord_defender", 0),

                    (store_and, ":is_protectorate", ":vassal_type_defender", sfvt_protectorate),
                    (gt, ":is_protectorate", 0),
                    (assign, ":must_declare_attacker", 1),
                (try_end),

                (try_begin),
                    (gt, ":alliance_attacker", 0),

                    (assign, ":must_declare_defender", 1),
                # (else_try),
                #     (gt, ":vassal_attacker", 0),

                #     (store_and, ":is_sattrapy", ":vassal_type", sfvt_sattrapy),
                #     (gt, ":is_sattrapy", 0),
                #     (assign, ":must_declare_defender", 1),
                (else_try),
                    (gt, ":overlord_attacker", 0),

                    (store_and, ":is_sattrapy", ":vassal_type", sfvt_sattrapy),
                    (gt, ":is_sattrapy", 0),
                    (assign, ":must_declare_defender", 1),
                (try_end),

                (try_begin),
                    (eq, ":must_declare_defender", 1),
                    (eq, ":must_declare_attacker", 0),
                    (gt, ":relation_defender", relation_state_war),
                    (try_begin),
                        (call_script, "script_cf_debug", debug_faction),
                        (str_store_faction_name, s10, ":faction_no"),
                        (assign, reg10, ":treaty_defender"),
                        (assign, reg11, ":treaty_attacker"),
                        (assign, reg12, ":treaties_slot"),
                        (display_log_message, "@{s10} joins war on side of attacker ({reg10} {reg11} {reg12})"),
                    (try_end),
                    (call_script, "script_faction_declare_war_to_faction", ":faction_no", ":faction_defender"),
                (else_try),
                    (eq, ":must_declare_defender", 0),
                    (eq, ":must_declare_attacker", 1),
                    (gt, ":relation_attacker", relation_state_war),
                    (try_begin),
                        (call_script, "script_cf_debug", debug_faction),
                        (str_store_faction_name, s10, ":faction_no"),
                        (assign, reg10, ":treaty_defender"),
                        (assign, reg11, ":treaty_attacker"),
                        (assign, reg12, ":treaties_slot"),
                        (display_log_message, "@{s10} joins war on side of defender ({reg10} {reg11} {reg12})"),
                    (try_end),
                    (call_script, "script_faction_declare_war_to_faction", ":faction_attacker", ":faction_no"),
                (else_try),
                    (eq, ":must_declare_defender", 1),
                    (eq, ":must_declare_attacker", 1),
                    (try_begin),
                        (call_script, "script_cf_debug", debug_faction),
                        (str_store_faction_name, s10, ":faction_no"),
                        (display_message, "@{s10} can't join war on either side"),
                    (try_end),
                # (else_try),
                #     (try_begin),
                #         (call_script, "script_cf_debug", debug_all),
                #         (str_store_faction_name, s10, ":faction_no"),
                #         (display_message, "@{s10} ignoring the event"),
                #     (try_end),
                (try_end),
            (try_end),
        ]),

    # script_faction_political_event_center_freed
        # input:
        #   arg1: freeing_faction
        #   arg2: center_freed
        #   arg3: freeing_party
        #   arg4: freed_from_faction
    ("faction_political_event_center_freed",
        [
            # (store_script_param, ":freeing_faction", 1),
            (store_script_param, ":center_freed", 2),
            (store_script_param, ":freeing_party", 3),
            (store_script_param, ":freed_from_faction", 4),

            (party_get_slot, ":center_type", ":center_freed", slot_party_type),
            (party_get_slot, ":center_owner_faction", ":center_freed", slot_party_faction),
            (assign, ":damage", 0),
            # We want to reduce our damage if we free an occupied center
            (try_begin),
                (eq, ":center_type", spt_town),
                (store_div, ":damage", war_damage_base_town_taken, -2),
            (else_try),
                (eq,":center_type", spt_castle),
                (store_div, ":damage", war_damage_base_castle_taken, -2),
            (else_try),
                (eq, ":center_type", spt_village),
                (store_div, ":damage", war_damage_base_village_taken, -2),
            (try_end),
            
            # Political consequences
            (call_script, "script_faction_damage_faction", ":center_owner_faction", ":freed_from_faction", ":damage", 0),
            
            (try_begin),
                (ge, ":freeing_party", 0),
                (party_get_slot, ":leader", ":freeing_party", slot_party_leader),
                (str_store_troop_name_link, s10, ":leader"),
                (str_store_party_name_link, s11, ":center_freed"),
                
                (display_log_message, "@{s11} has been freed by {s10}", text_color_freed),
            (try_end),
        ]),

    # script_faction_political_event_center_captured
        # input:
        #   arg1: capturing_faction
        #   arg2: center_captured
        #   arg3: capturing_party
    ("faction_political_event_center_captured",
        [
            (store_script_param, ":capturing_faction", 1),
            (store_script_param, ":center_captured", 2),
            (store_script_param, ":capturing_party", 3),

            (party_get_slot, ":center_type", ":center_captured", slot_party_type),
            (party_get_slot, ":center_owner_faction", ":center_captured", slot_party_faction),
            (assign, ":damage", 0),
            (try_begin),
                (eq, ":center_type", spt_town),
                (assign, ":damage", war_damage_base_town_taken),
            (else_try),
                (eq,":center_type", spt_castle),
                (assign, ":damage", war_damage_base_castle_taken),
            (else_try),
                (eq, ":center_type", spt_village),
                (assign, ":damage", war_damage_base_village_taken),
            (try_end),
            
            # Political consequences
            (call_script, "script_faction_damage_faction", ":center_owner_faction", ":capturing_faction", ":damage", 0),
            
            (try_begin),
                (ge, ":capturing_party", 0),
                (party_get_slot, ":leader", ":capturing_party", slot_party_leader),
                (try_begin),
                    (ge, ":leader", 0),
                    (str_store_troop_name_link, s10, ":leader"),
                (else_try),
                    (str_store_party_name, s10, ":capturing_party"),
                (try_end),
                (str_store_party_name_link, s11, ":center_captured"),
                
                (display_log_message, "@{s11} has been captured by {s10}", text_color_capture),
            (try_end),
        ]),

    # script_faction_political_event_center_captured
        # input:
        #   arg1: capturing_faction
        #   arg2: troop_captured
        #   arg3: capturing_party
    ("faction_political_event_vassal_captured",
        [
            (store_script_param, ":capturing_faction", 1),
            (store_script_param, ":troop_captured", 2),
            (store_script_param, ":capturing_party", 3),

            (store_troop_faction, ":captured_faction", ":troop_captured"),

            (try_begin),
                (call_script, "script_cf_debug", debug_simple|debug_war),
                (str_store_troop_name_link, s10, ":troop_captured"),
                (try_begin),
                    (ge, ":capturing_party", 0),
                    (str_store_party_name_link, s11, ":capturing_party"),
                (else_try),
                    (str_store_faction_name, s11, ":capturing_faction"),
                (try_end),
                (display_log_message, "@{s10} has been captured by {s11}."),
            (try_end),

            (call_script, "script_faction_damage_faction", ":capturing_faction", ":captured_faction", war_damage_base_lord_defeated, 0),

            (call_script, "script_transform_war_damage_to_relation_change", war_damage_base_lord_defeated),
            (assign, ":relation_damage", reg0),
            (call_script, "script_faction_change_relation_with_faction", ":captured_faction", ":capturing_faction", ":relation_damage", 0),
        ]),

    # script_faction_political_event_center_captured
        # input:
        #   arg1: freeing_faction
        #   arg2: troop_freed
        #   arg3: freeing_party
    ("faction_political_event_vassal_freed",
        [
            (store_script_param, ":freeing_faction", 1),
            (store_script_param, ":troop_freed", 2),
            (store_script_param, ":freeing_party", 3),

            (store_troop_faction, ":freed_faction", ":troop_freed"),

            (try_begin),
                (call_script, "script_cf_debug", debug_simple|debug_war),
                (str_store_troop_name_link, s10, ":troop_freed"),
                (try_begin),
                    (ge, ":freeing_party", 0),
                    (str_store_party_name_link, s11, ":freeing_party"),
                    (assign, reg10, 1),
                (else_try),
                    (assign, reg10, 0),
                (try_end),
                (display_log_message, "@{s10} has been freed {reg10?by {s11}:from captivity}."),
            (try_end),

            (call_script, "script_faction_change_relation_with_faction", ":freed_faction", ":freeing_faction", 1, 0),
        ]),

    # script_faction_create_treaty
        # input:
        #   arg1: faction_1
        #   arg2: faction_2
        #   arg3: treaty_type
    ("faction_create_treaty",
        [
            (store_script_param, ":faction_1", 1),
            (store_script_param, ":faction_2", 2),
            (store_script_param, ":treaty_type", 3),

            (try_begin),
                (this_or_next|eq, ":treaty_type", sfkt_alliance),
                (this_or_next|eq, ":treaty_type", sfkt_defensive_alliance),
                (this_or_next|eq, ":treaty_type", sfkt_vassal),
                (eq, ":treaty_type", sfkt_overlord),

                (set_relation, ":faction_1", ":faction_2", relation_state_friendly),
            (else_try),
                (eq, ":treaty_type", sfkt_non_agression),
                (set_relation, ":faction_1", ":faction_2", relation_state_neutral),
            (else_try),
                (eq, ":treaty_type", sfkt_truce),
                (set_relation, ":faction_1", ":faction_2", relation_state_conflict),
            (try_end),

            (call_script, "script_faction_set_treaty", ":faction_1", ":faction_2", ":treaty_type"),

            (try_begin),
                (call_script, "script_cf_debug", debug_faction),
                (str_store_faction_name, s10, ":faction_1"),
                (str_store_faction_name, s11, ":faction_2"),
                (assign, reg10, ":treaty_type"),
                (display_message, "@{s10} creates treaty {reg10} with {s11}"),
            (try_end),
        ]),

    # script_faction_revoke_treaty
        # input:
        #   arg1: faction_1
        #   arg2: faction_2
        #   arg3: treaty_type
    ("faction_revoke_treaty",
        [
            (store_script_param, ":faction_1", 1),
            (store_script_param, ":faction_2", 2),
            (store_script_param, ":treaty_type", 3),

            (store_sub, ":offset", ":faction_2", kingdoms_begin),
            (store_add, ":treaty_slot", ":offset", slot_faction_kingdom_treaties_begin),

            (assign, ":clearer_type", sfkt_none_treaty_clear),
            (assign, ":clear_other", 0),
            (try_begin),
                (this_or_next|eq, ":treaty_type", sfkt_truce),
                (this_or_next|eq, ":treaty_type", sfkt_non_agression),
                (this_or_next|eq, ":treaty_type", sfkt_defensive_alliance),
                (eq, ":treaty_type", sfkt_alliance),

                (assign, ":clearer_type", sfkt_military_treaty_clear),
                (assign, ":clear_other", 1),
            (else_try),
                (this_or_next|eq, ":treaty_type", sfkt_open_trade),
                (this_or_next|eq, ":treaty_type", sfkt_trade_preference),
                (eq, ":treaty_type", sfkt_trade_exclusivity),

                (assign, ":clearer_type", sfkt_economic_treaty_clear),
                (assign, ":clear_other", 1),
            (else_try),
                (this_or_next|eq, ":treaty_type", sfkt_vassal),
                (eq, ":treaty_type", sfkt_overlord),

                (assign, ":clearer_type", sfkt_vassal_treaty_clear),
                (try_begin),
                    (eq, ":treaty_type", sfkt_vassal),
                    (assign, ":clear_other", 1),
                (else_try),
                    (eq, ":treaty_type", sfkt_overlord),
                    (assign, ":clear_other", 1),
                (try_end),
            (try_end),

            (faction_get_slot, ":treaty", ":faction_1", ":treaty_slot"),
            (val_and, ":treaty", ":clearer_type"),
            (faction_set_slot, ":faction_1", ":treaty_slot", ":treaty"),

            (try_begin),
                (eq, ":clear_other", 1),

                (store_sub, ":other_offset", ":faction_1", kingdoms_begin),
                (store_add, ":other_treaty_slot", ":other_offset", slot_faction_kingdom_treaties_begin),

                (faction_get_slot, ":treaty", ":faction_2", ":other_treaty_slot"),
                (val_and, ":treaty", ":clearer_type"),
                (faction_set_slot, ":faction_2", ":other_treaty_slot", ":treaty"),
            (try_end),
        ]),

    # script_faction_set_treaty
        # input:
        #   arg1: faction_1
        #   arg2: faction_2
        #   arg3: treaty_type
    ("faction_set_treaty",
        [
            (store_script_param, ":faction_1", 1),
            (store_script_param, ":faction_2", 2),
            (store_script_param, ":treaty_type", 3),

            (store_sub, ":offset", ":faction_2", kingdoms_begin),
            (store_add, ":treaty_slot", ":offset", slot_faction_kingdom_treaties_begin),

            (assign, ":clearer_type", sfkt_none_treaty_clear),
            (assign, ":other_treaty_type", sfkt_none),
            (try_begin),
                (this_or_next|eq, ":treaty_type", sfkt_truce),
                (this_or_next|eq, ":treaty_type", sfkt_non_agression),
                (this_or_next|eq, ":treaty_type", sfkt_defensive_alliance),
                (eq, ":treaty_type", sfkt_alliance),

                (assign, ":clearer_type", sfkt_military_treaty_clear),
                (assign, ":other_treaty_type", ":treaty_type"),
            (else_try),
                (this_or_next|eq, ":treaty_type", sfkt_open_trade),
                (this_or_next|eq, ":treaty_type", sfkt_trade_preference),
                (eq, ":treaty_type", sfkt_trade_exclusivity),

                (assign, ":clearer_type", sfkt_economic_treaty_clear),
                (assign, ":other_treaty_type", ":treaty_type"),
            (else_try),
                (this_or_next|eq, ":treaty_type", sfkt_vassal),
                (eq, ":treaty_type", sfkt_overlord),

                (assign, ":clearer_type", sfkt_vassal_treaty_clear),
                (try_begin),
                    (eq, ":treaty_type", sfkt_vassal),
                    (assign, ":other_treaty_type", sfkt_overlord),
                (else_try),
                    (eq, ":treaty_type", sfkt_overlord),
                    (assign, ":other_treaty_type", sfkt_vassal),
                (try_end),
            (try_end),

            (faction_get_slot, ":treaty", ":faction_1", ":treaty_slot"),
            (val_and, ":treaty", ":clearer_type"),
            (val_or, ":treaty", ":treaty_type"),
            (faction_set_slot, ":faction_1", ":treaty_slot", ":treaty"),

            (try_begin),
                (neq, ":other_treaty_type", sfkt_none),

                (store_sub, ":other_offset", ":faction_1", kingdoms_begin),
                (store_add, ":other_treaty_slot", ":other_offset", slot_faction_kingdom_treaties_begin),

                (faction_get_slot, ":treaty", ":faction_2", ":other_treaty_slot"),
                (val_and, ":treaty", ":clearer_type"),
                (val_or, ":treaty", ":other_treaty_type"),
                (faction_set_slot, ":faction_2", ":other_treaty_slot", ":treaty"),
            (try_end),
        ]),

    # script_faction_clear_treaty
        # input:
        #   arg1: faction_1
        #   arg2: faction_2
        #   arg3: clearer_type
    ("faction_clear_treaty",
        [
            (store_script_param, ":faction_1", 1),
            (store_script_param, ":faction_2", 2),
            (store_script_param, ":clearer_type", 3),

            (store_sub, ":offset", ":faction_2", kingdoms_begin),
            (store_add, ":treaty_slot", ":offset", slot_faction_kingdom_treaties_begin),

            (faction_get_slot, ":treaty", ":faction_1", ":treaty_slot"),
            (val_and, ":treaty", ":clearer_type"),
            (faction_set_slot, ":faction_1", ":treaty_slot", ":treaty"),
        ]),

    # script_party_spawn_bandits
        # input:
        #   arg1: center_no
        # output:
        #   reg0: bandit_party
        #   reg1: bandit_faction
    ("party_spawn_bandits",
        [
            (store_script_param, ":center_no", 1),

            (party_get_slot, ":center_original_faction", ":center_no", slot_party_original_faction),
            (faction_get_slot, ":center_culture", ":center_original_faction", slot_faction_culture),
            (party_get_current_terrain, ":terrain", ":center_no"),
            (party_get_slot, ":center_prosperity", ":center_no", slot_party_prosperity),
            
            (assign, ":bandit_party", -1),
            (assign, ":bandit_faction", -1),
            (assign, ":bandit_leader", -1),

            # Roll bandit strength
            (assign, ":bandit_chance", 2),
            (assign, ":max_strength", 4),
            (try_begin),
                # High prosperity will increase the max strength of bandits -- up to 3
                (store_div, ":strength_change", ":center_prosperity", 30),
                (val_add, ":max_strength", ":strength_change"),
            (try_end),
            (store_random_in_range, ":bandit_strength", 1, ":max_strength"),

            # Low prosperity will increase the chance of having bandits
            (store_sub, ":chance_modifier", 100, ":center_prosperity"),
            (val_div, ":chance_modifier", 10),
            (val_add, ":bandit_chance", ":chance_modifier"),

            (store_random_in_range, ":rand", 0, 1000),
            (try_begin),
                (le, ":bandit_chance", ":rand"),
                (assign, ":bandit_strength", 0),
                (assign, ":desert_bandit", 0),
                (assign, ":plain_bandit", 0),
                (assign, ":forest_bandit", 0),
                (assign, ":mountain_bandit", 0),
                (assign, ":steppe_bandit", 0),
                (assign, ":tundra_bandit", 0),
                (assign, ":sea_raiders", 0),

                (try_begin),
                    (eq, ":terrain", rt_plain),
                    # More likely to spawn normal bandits
                    (val_add, ":plain_bandit", 20),
                (else_try),
                    (eq, ":terrain", rt_steppe),
                    (val_add, ":steppe_bandit", 20),
                (else_try),
                    (eq, ":terrain", rt_snow),
                    (val_add, ":tundra_bandit", 20),
                (else_try),
                    (eq, ":terrain", rt_desert),
                    (val_add, ":desert_bandit", 20),
                (try_end),
                # Also use nearby tiles ?
                # Or village production ?

                (try_begin),
                    (eq, ":center_culture", fac_culture_1),
                    (val_add, ":plain_bandit", 10),
                    (val_add, ":forest_bandit", 10),
                (else_try),
                    (eq, ":center_culture", fac_culture_2),
                    (val_add, ":tundra_bandit", 10),
                    (val_add, ":mountain_bandit", 5),
                (else_try),
                    (eq, ":center_culture", fac_culture_3),
                    (val_add, ":steppe_bandit", 10),
                (else_try),
                    (eq, ":center_culture", fac_culture_4),
                    (val_add, ":sea_raiders", 20),
                    (val_add, ":forest_bandit", 5),
                (else_try),
                    (eq, ":center_culture", fac_culture_5),
                    (val_add, ":mountain_bandit", 40),
                    (val_add, ":forest_bandit", 5),
                (else_try),
                    (eq, ":center_culture", fac_culture_6),
                    (val_add, ":desert_bandit", 10),
                (try_end),

                (store_add, ":grand_total", ":plain_bandit", ":forest_bandit"),
                (val_add, ":grand_total", ":mountain_bandit"),
                (val_add, ":grand_total", ":tundra_bandit"),
                (val_add, ":grand_total", ":steppe_bandit"),
                (val_add, ":grand_total", ":desert_bandit"),
                (val_add, ":grand_total", ":sea_raiders"),
                
                (store_random_in_range, ":rest", 0, ":grand_total"),
                (val_sub, ":rest", ":forest_bandit"),
                (try_begin),
                    (lt, ":rest", 0),
                    (assign, ":bandit_faction", "fac_faction_1"),
                    (assign, ":bandit_leader", "trp_bandit_forest_leader"),
                (else_try),
                    (store_sub, ":rest", ":rest", ":plain_bandit"),
                    (lt, ":rest", 0),
                    (assign, ":bandit_faction", "fac_faction_2"),
                    (assign, ":bandit_leader", "trp_bandit_leader"),
                (else_try),
                    (store_sub, ":rest", ":rest", ":mountain_bandit"),
                    (lt, ":rest", 0),
                    (assign, ":bandit_faction", "fac_faction_3"),
                    (assign, ":bandit_leader", "trp_bandit_mountain_chieftain"),
                (else_try),
                    (store_sub, ":rest", ":rest", ":sea_raiders"),
                    (lt, ":rest", 0),
                    (assign, ":bandit_faction", "fac_faction_4"),
                    (assign, ":bandit_leader", "trp_bandit_sea_captain"),
                (else_try),
                    (store_sub, ":rest", ":rest", ":steppe_bandit"),
                    (lt, ":rest", 0),
                    (assign, ":bandit_faction", "fac_faction_5"),
                    (assign, ":bandit_leader", "trp_bandit_steppe_chief"),
                (else_try),
                    (store_sub, ":rest", ":rest", ":tundra_bandit"),
                    (lt, ":rest", 0),
                    (assign, ":bandit_faction", "fac_faction_6"),
                    (assign, ":bandit_leader", "trp_bandit_taiga_chieftain"),
                (else_try),
                    (store_sub, ":rest", ":rest", ":desert_bandit"),
                    (lt, ":rest", 0),
                    (assign, ":bandit_faction", "fac_faction_7"),
                    (assign, ":bandit_leader", "trp_bandit_desert_chief"),
                (try_end),

                (try_begin),
                    (neq, ":bandit_faction", -1),
                    (try_begin),
                        (call_script, "script_cf_debug", debug_ai),
                        (str_store_party_name, s10, ":center_no"),
                        (display_message, "@Spawning bandit party at {s10}."),
                    (try_end),
                    (call_script, "script_spawn_party_around_party", ":center_no", "pt_outlaws"),
                    (assign, ":bandit_party", reg0),
                    (party_set_faction, ":bandit_party", ":bandit_faction"),

                    (party_set_slot, ":bandit_party", slot_party_type, spt_bandit),
                    (party_set_ai_behavior, ":bandit_party", ai_bhvr_patrol_location),

                    (store_random_in_range, ":chance_leader", 0, 100),
                    (try_begin),
                        # Chance for a bandit leader
                        (le, ":chance_leader", 10),
                        (neq, ":bandit_leader", -1),
                        (party_add_members, ":bandit_party", ":bandit_leader", 1),
                        (val_add, ":bandit_strength", 2),
                    # (else_try),
                        # Need to count so that not too many heroes are present before adding a new one
                        # Possibly needs to increase odds if there are few heroes
                        # Chance for a bandit hero if no leader
                        #(eq, ":chance_leader", 99),
                    (try_end),

                    (val_max, ":bandit_strength", 1),
                    (try_for_range, ":unused", 0, ":bandit_strength"),
                        (call_script, "script_party_add_reinforcements", ":bandit_party"),
                        # (assign, ":num_added", reg0),
                        # (try_begin),
                        #     (eq, ":num_added", 0),
                        #     (val_add, ":bandit_strength", 1),
                        # (try_end),
                    (try_end),
                (try_end),
            (try_end),

            (assign, reg0, ":bandit_party"),
            (assign, reg1, ":bandit_faction"),
        ]),

    # script_party_take_troop_prisoner
        # input:
        #   arg1: party_id
        #   arg2: troop_id
        #   arg3: from_party
        # output: none
    ("party_take_troop_prisoner",
        [
            (store_script_param, ":party_id", 1),
            (store_script_param, ":troop_id", 2),
            (store_script_param, ":from_party", 3),
            (store_script_param, ":amount", 4),

            (try_begin),
                (troop_is_hero, ":troop_id"),
                (call_script, "script_troop_taken_prisoner", ":troop_id", ":party_id"),
                (assign, ":amount", 1),
                (party_force_add_prisoners, ":party_id", ":troop_id", ":amount"),

                (store_faction_of_party, ":party_faction", ":party_id"),
                (call_script, "script_faction_political_event", ":party_faction", political_event_vassal_captured, ":troop_id", ":party_id", -1),
            (else_try),
                (party_add_prisoners, ":party_id", ":troop_id", ":amount"),
            (try_end),
            (try_begin),
                (ge, ":from_party", 0),
                (party_remove_members, ":from_party", ":troop_id", ":amount"),
            (try_end),
        ]),

    # script_troop_taken_prisoner
        # input:
        #   arg1: troop_id
        #   arg2: prisoner_of_party
        # output: none
    ("troop_taken_prisoner",
        [
            (store_script_param, ":troop_id", 1),
            (store_script_param, ":party_no", 2),

            (troop_set_slot, ":troop_id", slot_troop_prisoner_of, ":party_no"),
            (troop_set_slot, ":troop_id", slot_troop_gathering, -1), # Stop gathering when defeated
            (try_begin),
                (call_script, "script_cf_debug", debug_simple|debug_war),
                (str_store_troop_name, s10, ":troop_id"),
                (str_store_party_name, s11, ":party_no"),
                (display_message, "@{s10} has been taken prisoner by {s11}."),
            (try_end),
        ]),

    # script_troop_freed
        # input: 
        #   arg1: troop_id
        #   arg2: freeing_party
        # output: none
    ("troop_freed",
        [
            (store_script_param, ":troop_id", 1),
            (store_script_param, ":party_no", 2),

            (try_begin),
                # Remove troop for party id if not already done
                (troop_get_slot, ":prisoner_of", ":troop_id", slot_troop_prisoner_of),
                (ge, ":prisoner_of", 0),
                (party_remove_prisoners, ":prisoner_of", ":troop_id", 1),
            (try_end),

            (troop_set_slot, ":troop_id", slot_troop_prisoner_of, -1),
            # (troop_set_slot, ":troop_id", slot_troop_prisoner_in, -1),

            (assign, ":party_faction", -1),
            (try_begin),
                (ge, ":party_no", 0),
                (store_faction_of_party, ":party_faction", ":party_no"),
            (try_end),
            (call_script, "script_faction_political_event", ":party_faction", political_event_vassal_freed, ":troop_id", ":party_no", -1),
        ]),

    # script_troop_released
        # input:
        #   arg1: troop_id
        # output: none
    ("troop_released", 
        [
            (store_script_param, ":troop_id", 1),

            (call_script, "script_troop_freed", ":troop_id", -1),
        ]),

    # script_troop_proficiency_decay
        # input:
        #   arg1: troop_no
        # output: none
    ("troop_proficiency_decay",
        [
            (store_script_param, ":troop_no", 1),

            (store_skill_level, ":weap_master", skl_weapon_master, ":troop_no"),
            (store_mul, ":wp_limit", ":weap_master", 10),
            (store_add, ":wp_div", 15, ":weap_master"), # Weapon master increases the threshold
            (val_add, ":wp_limit", 20), # Min 20, max 120
            # ToDo: Increase the wp loss when older ?
            (try_for_range, ":att", wpt_one_handed_weapon, wpt_firearm+1),
                (store_proficiency_level, ":wp", ":troop_no", ":att"),
                (store_sub, ":diff", ":wp", ":wp_limit"),
                (store_div, ":wp_loss", ":diff", ":wp_div"), # Loses from 6.666% to 4% every month
                (store_mod, ":top", ":diff", ":wp_div"),
                (store_random_in_range, ":rand", 0, ":wp_div"),
                (try_begin),
                    (gt, ":top", ":rand"),
                    (val_add, ":wp_loss", 1),
                (try_end),
                (gt, ":wp_loss", 0),
                (try_begin),
                    (call_script, "script_cf_debug", debug_all),
                    (str_store_troop_name, s10, ":troop_no"),
                    (try_begin),
                        (eq, ":att", wpt_one_handed_weapon),
                        (str_store_string, s11, "@One Handed Weapons"),
                    (else_try),
                        (eq, ":att", wpt_two_handed_weapon),
                        (str_store_string, s11, "@Two Handed Weapons"),
                    (else_try),
                        (eq, ":att", wpt_polearm),
                        (str_store_string, s11, "@Pole Weapons"),
                    (else_try),
                        (eq, ":att", wpt_archery),
                        (str_store_string, s11, "@Archery"),
                    (else_try),
                        (eq, ":att", wpt_crossbow),
                        (str_store_string, s11, "@Crossbows"),
                    (else_try),
                        (eq, ":att", wpt_throwing),
                        (str_store_string, s11, "@Throwing Weapons"),
                    (else_try),
                        (str_store_string, s11, "@Firearms"),
                    (try_end),
                    (assign, reg10, ":wp_loss"),
                    (display_message, "@{s10} lost {reg10} proficiency points in {s11}"),
                (try_end),
                (val_mul, ":wp_loss", -1),
                (troop_raise_proficiency_linear, ":troop_no", ":att", ":wp_loss"),
            (try_end),
        ]),

    # script_troop_is_in_family_of
        # input: 
        #   arg1: troop_1
        #   arg2: troop_2
        #   arg3: num_moves
        # output:
        #   reg0: found_depth : the depths at which the family member has been found -1 if not found
        # The script is used to find family members that are not in the same house
        # The script might be ressource intensive, and should be used if possible only during menus and with a low number of moves
    ("troop_is_in_family_of",
        [
            (store_script_param, ":troop_1", 1),
            (store_script_param, ":troop_2", 2),
            (store_script_param, ":num_moves", 3),

            (assign, ":found", -1),
            (try_begin),
                (gt, ":num_moves", 0),
                (assign, ":found", -1),
                (store_add, ":end", slot_troop_child_10, 1),
                (try_for_range, ":family_slot", slot_troop_married_to, ":end"),
                    (troop_get_slot, ":family_member", ":troop_1", ":family_slot"),
                    (try_begin),
                        (eq, ":family_member", ":troop_2"),
                        (assign, ":found", 1),
                        (assign, ":end", 0),
                    (try_end),
                (try_end),
                (try_begin),
                    (eq, ":found", -1),
                    (store_add, ":end", slot_troop_child_10, 1),
                    (store_sub, ":decreased_moves", ":num_moves", 1),
                    (try_for_range, ":family_slot", slot_troop_married_to, ":end"),
                        (troop_get_slot, ":family_member", ":troop_1", ":family_slot"),
                        (ge, ":family_member", 0),
                        (call_script, "script_troop_is_in_family_of", ":family_member", ":troop_2", ":decreased_moves"),
                        (assign, ":ret", reg0),
                        (try_begin),
                            (ge, ":ret", 0),
                            (assign, ":end", 0),
                            (store_add, ":found", ":ret", 1),
                        (try_end),
                    (try_end),
                (try_end),
            (try_end),
            (assign, reg0, ":found"),
        ]),

    # script_party_process_buildings
        # input:
        #   arg1: party_no
        #   arg2: time_interval
        # output: none
    ("party_process_buildings",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":interval", 2),

            (party_get_slot, ":leader", ":party_no", slot_party_leader),

            # (party_get_slot, ":cur_gold", ":party_no", slot_party_wealth),
            # (party_get_slot, ":cur_stone", ":party_no", "itm_stone"),
            # (party_get_slot, ":cur_wood", ":party_no", "itm_wood"),

            # Process buildings construction time
            (try_for_range, ":building_slot", slot_party_building_slot_1, slot_party_building_slot_end),
                (party_get_slot, ":building", ":party_no", ":building_slot"),
                (is_between, ":building", center_buildings_begin, center_buildings_end),

                (store_add, ":slot", ":building_slot", num_building_slots),
                (party_get_slot, ":state", ":party_no", ":slot"),

                # (item_get_slot, ":wood_cost", ":building", slot_building_cost_wood),
                # # (item_get_slot, ":stone_cost", ":building", slot_building_cost_stone),
                # (item_get_slot, ":gold_cost", ":building", slot_building_cost_gold),
                (item_get_slot, ":time", ":building", slot_building_build_time),

                # (store_mul, ":wood_added", ":wood_cost", 100),
                # (val_div, ":wood_added", ":interval"),

                # (store_mul, ":stone_added", ":stone_cost", 100),
                # (val_div, ":stone_added", ":interval"),

                # (store_mul, ":gold_added", ":gold_cost", 100),
                # (val_div, ":gold_added", ":interval"),

                (try_begin),

                    (store_mul, ":time_added", ":time", 100),
                    (val_div, ":time_added", ":interval"),

                    (try_begin),
                        # Building not constructed
                        # Drains ressources
                        (lt, ":state", 0),

                        (try_begin),
                            (val_add, ":state", ":time_added"),
                            (try_begin),
                                (ge, ":state", 0),
                                (assign, ":state", 50),
                                (try_begin),
                                    (this_or_next|call_script, "script_cf_debug", debug_economy|debug_simple),
                                    (eq, ":leader", "$g_player_troop"),
                                    (str_store_party_name_link, s10, ":party_no"),
                                    (str_store_item_name, s11, ":building"),
                                    (display_log_message, "@{s10} has finished construction of {s11}."),
                                (try_end),
                            (try_end),
                            (party_set_slot, ":party_no", ":slot", ":state"),
                        (try_end),
                    (else_try),
                        # Building damaged
                        # Drains some ressources and barely works
                        (is_between, ":state", 0, 50),

                        (try_begin),
                            (val_div, ":time_added", 2),
                            (val_add, ":state", ":time_added"),

                            (try_begin),
                                (ge, ":state", 50),

                                (try_begin),
                                    (this_or_next|call_script, "script_cf_debug", debug_economy|debug_simple),
                                    (eq, ":leader", "$g_player_troop"),
                                    (str_store_party_name_link, s10, ":party_no"),
                                    (str_store_item_name, s11, ":building"),
                                    (display_log_message, "@{s10} has finished repairs of {s11}."),
                                (try_end),
                            (try_end),
                            (party_set_slot, ":party_no", ":slot", ":state"),
                        (try_end),
                    (else_try),
                        # Building just built or slightly damaged
                        # Drains no ressources and functions at reduced efficiency
                        (is_between, ":state", 50, 100),

                        (try_begin),
                            (val_div, ":time_added", 2),
                            (val_add, ":state", ":time_added"),

                            (val_min, ":state", 100),

                            (party_set_slot, ":party_no", ":slot", ":state"),
                        (try_end),
                    (try_end),
                (try_end),
            (try_end),

            # Process special building effects
        ]),

    # script_troop_change_renown
        # input: 
        #   arg1: troop_id
        #   arg2: amount
        # output: 
        #   reg0: new_renown
    ("troop_change_renown",
        [
            (store_script_param, ":troop_id", 1),
            (store_script_param, ":amount", 2),

            (troop_get_slot, ":current", ":troop_id", slot_troop_renown),
            (store_add, ":new", ":current", ":amount"),
            (val_max, ":new", 0),

            (troop_set_slot, ":troop_id", slot_troop_renown, ":new"),

            (try_begin),
                (this_or_next|eq, ":troop_id", "$g_player_troop"),
                (call_script, "script_cf_debug", debug_all),
                (call_script, "script_cf_debug", debug_simple),
                (assign, reg10, ":current"),
                (assign, reg11, ":new"),
                (display_message, "@Renown changed from {reg10} to {reg11}."),
            (try_end),

            (assign, reg0, ":new"),
        ]),

    # script_troop_change_honor
        # input: 
        #   arg1: troop_id
        #   arg2: amount
        # output: 
        #   reg0: new_honor
    ("troop_change_honor", 
        [
            (store_script_param, ":troop_id", 1),
            (store_script_param, ":amount", 2),

            (troop_get_slot, ":current", ":troop_id", slot_troop_honor),
            (store_add, ":new", ":current", ":amount"),
            (val_clamp, ":new", 0, 101),

            (troop_set_slot, ":troop_id", slot_troop_honor, ":new"),

            (try_begin),
                (this_or_next|eq, ":troop_id", "$g_player_troop"),
                (call_script, "script_cf_debug", debug_all),
                (call_script, "script_cf_debug", debug_simple),
                (assign, reg10, ":current"),
                (assign, reg11, ":new"),
                (display_message, "@Honor changed from {reg10} to {reg11}."),
            (try_end),

            (assign, reg0, ":new"),
        ]),

    # script_troop_change_wealth
        # input:
        #   arg1: troop_no
        #   arg2: amount
        # output:
        #   reg0: new_wealth
    ("troop_change_wealth",
        [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":amount", 2),

            (troop_add_gold, ":troop_no", ":amount"),
            (store_troop_gold, reg0, ":troop_no"),
        ]),

    # script_party_change_morale
        # input: 
        #   arg1: party_id
        #   arg2: amount
        # output: 
        #   reg0: new_morale
    ("party_change_morale", 
        [
            (store_script_param, ":party_id", 1),
            (store_script_param, ":amount", 2),

            (party_get_slot, ":current", ":party_id", slot_party_morale),
            (store_add, ":new", ":current", ":amount"),
            (val_clamp, ":new", 0, 101),

            (party_set_slot, ":party_id", slot_party_morale, ":new"),

            # (try_begin),
            #     (this_or_next|eq, ":party_id", "$g_player_party"),
            #     (call_script, "script_cf_debug", debug_war),
            #     (call_script, "script_cf_debug", debug_simple|debug_war),
            #     (assign, reg10, ":current"),
            #     (assign, reg11, ":new"),
            #     (str_store_party_name, s10, ":party_id"),
            #     (display_message, "@{s10} morale changed from {reg10} to {reg11}."),
            # (try_end),

            (assign, reg0, ":new"),
        ]),

    # script_agent_init_morale_values
        # input:
        #   arg1: agent_no
        # output: none
    ("agent_init_morale_values",
        [
            (store_script_param, ":agent_no", 1),

            (agent_get_party_id, ":party", ":agent_no"),
            (try_begin),
                (ge, ":party", 0),
                (party_get_slot, ":party_morale", ":party", slot_party_morale),
                (agent_set_slot, ":agent_no", slot_agent_morale, ":party_morale"),

                (call_script, "script_agent_get_morale_modifiers", ":agent_no"),
                (assign, ":morale_modifier", reg0),
                (agent_set_slot, ":agent_no", slot_agent_morale_modifier, ":morale_modifier"),

                # Add leader bonuses + troop bonuses
            (try_end),
        ]),

    # script_agent_update_morale_values
        # input:
        #   arg1: agent_no
        # output: none
    ("agent_update_morale_values",
        []),

    # script_agent_get_morale_modifiers
        # input:
        #   arg1: agent_no
        # output: 
        #   reg0: morale_value
    ("agent_get_morale_modifiers",
        [
            (assign, reg0, 0),
        ]),

    # script_party_pay_wages
        # input:
        #   arg1: party_no
        # output:
        #   reg0: paid_wages
    ("party_pay_wages",
        [
            (store_script_param, ":party_no", 1),

            (assign, ":paid_wages", 0),
            (party_get_slot, ":party_type", ":party_no", slot_party_type),

            (try_begin),
                (is_between, ":party_type", spt_bandit, spt_fort + 1),

                (assign, ":paid_wages", 0),
                (call_script, "script_party_get_wages", ":party_no"),
                (assign, ":party_wages", reg0),

                (try_begin),
                    (is_between, ":party_type", spt_village, spt_fort + 1),
                    # Only centers pay wages directly
                    # The rest is accumulated in debts

                    (call_script, "script_party_remove_gold", ":party_no", ":party_wages"),
                    (assign, ":paid_wages", reg0),

                    (try_begin),
                        (call_script, "script_cf_debug", debug_economy),
                        (eq, ":party_type", spt_war_party),
                        (str_store_party_name, s10, ":party_no"),
                        (assign, reg10, ":party_wages"),
                        (assign, reg11, ":paid_wages"),
                        (display_message, "@{s10} paying wages: {reg10} - total paid: {reg11}"),
                    (try_end),
                (try_end),

                (try_begin),
                    (neq, ":paid_wages", ":party_wages"),
                    (store_sub, ":unpaid_wages", ":party_wages", ":paid_wages"),
                    (call_script, "script_party_unpaid_wages_penalties", ":party_no", ":unpaid_wages", ":party_wages"),
                (try_end),
            (try_end),

            (assign, reg0, ":paid_wages"),
        ]),

    # script_party_pay_debts
        # input:
        #   arg1: party_no
        # output:
        #   reg0: paid_debts
    ("party_pay_debts",
        [
            (store_script_param, ":party_no", 1),

            (assign, ":paid_debts", 0),

            (party_get_slot, ":unpaid_wages", ":party_no", slot_party_unpaid_wages),
            (try_begin),
                (gt, ":unpaid_wages", 0),
                (call_script, "script_party_get_total_wealth", ":party_no", 1),
                (assign, ":wealth", reg0),
                (try_begin),
                    (gt, ":wealth", 0),
                    (store_div, ":max_payment", ":wealth", 5),
                    (val_min, ":max_payment", ":unpaid_wages"),
                    (call_script, "script_party_remove_gold", ":party_no", ":max_payment"),
                    (store_sub, ":unpaid_wages_left", ":unpaid_wages", ":max_payment"),
                    (party_set_slot, ":party_no", slot_party_unpaid_wages, ":unpaid_wages_left"),
                (try_end),
            (try_end),

            (assign, reg0, ":paid_debts"),
        ]),

    # script_party_get_total_wealth
        # input: 
        #   arg1: party_no
        #   arg2: ignore_debts
        # output:
        #   reg0: total_wealth
    ("party_get_total_wealth", 
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":ignore_debts", 2),

            (assign, ":total_wealth", 0),
            
            (party_get_slot, ":party_wealth", ":party_no", slot_party_wealth),
            (party_get_slot, ":leader", ":party_no", slot_party_leader),
            (party_get_slot, ":party_type", ":party_no", slot_party_type),

            (try_begin),
                (this_or_next|ge, ":party_wealth", 0),
                (eq, ":ignore_debts", 0),

                (val_add, ":total_wealth", ":party_wealth"),
            (try_end),

            (try_begin),
                (gt, ":leader", 0),

                (troop_get_slot, ":leader_party", ":leader", slot_troop_leaded_party),
                (ge, ":leader_party", 0),
                (party_get_attached_to, ":attached_to", ":leader_party"),

                # Leader is either leading the party or is waiting inside
                (this_or_next|eq, ":leader_party", ":party_no"),
                (eq, ":attached_to", ":party_no"),

                (store_troop_gold, ":leader_wealth", ":leader"),

                (this_or_next|ge, ":leader_wealth", 0),
                (eq, ":ignore_debts", 0),

                (val_add, ":total_wealth", ":leader_wealth"),
            (try_end),

            (try_begin),
                (is_between, ":party_type", spt_caravan, spt_convoy + 1),
                (party_get_attached_to, ":attached_party", ":party_no"),
                (party_get_slot, ":linked_center", ":party_no", slot_party_linked_party),
                (ge, ":linked_center", centers_begin),
                (eq, ":linked_center", ":attached_party"),
                (party_get_slot, ":center_wealth", ":linked_center", slot_party_wealth),

                (this_or_next|ge, ":center_wealth", 0),
                (eq, ":ignore_debts", 0),

                (val_add, ":total_wealth", ":center_wealth"),
            (try_end),

            (try_begin),
                (eq, ":ignore_debts", 0),
                (party_get_slot, ":debts", ":party_no", slot_party_unpaid_wages),
                (val_sub, ":total_wealth", ":debts"),
            (try_end),

            (assign, reg0, ":total_wealth"),
        ]),

    # script_party_remove_gold
        # input:
        #   arg1: party_no
        #   arg2: gold_amount
        # output: 
        #   reg0: gold_removed
    ("party_remove_gold", 
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":amount", 2),

            (assign, ":gold_removed", 0),
            (try_begin),
                (party_get_slot, ":party_wealth", ":party_no", slot_party_wealth),
                (party_get_slot, ":leader", ":party_no", slot_party_leader),
                (party_get_slot, ":party_type", ":party_no", slot_party_type),
                
                (gt, ":amount", 0),
                (try_begin),
                    (gt, ":party_wealth", 0),
                    (assign, ":gold_removed", ":amount"),
                    (val_min, ":gold_removed", ":party_wealth"),
                    (val_sub, ":party_wealth", ":gold_removed"),
                    (party_set_slot, ":party_no", slot_party_wealth, ":party_wealth"),
                    (val_sub, ":amount", ":gold_removed"),
                (try_end),

                (gt, ":amount", 0),
                (try_begin),
                    (ge, ":leader", 0),

                    (troop_get_slot, ":leader_party", ":leader", slot_troop_leaded_party),
                    (ge, ":leader_party", 0),
                    (party_get_attached_to, ":attached_to", ":leader_party"),

                    # Leader is either leading the party or is waiting inside
                    (this_or_next|eq, ":leader_party", ":party_no"),
                    (eq, ":attached_to", ":party_no"),

                    (store_troop_gold, ":leader_wealth", ":leader"),
                    (gt, ":leader_wealth", 0),
                    (assign, ":gold_removed_leader", ":amount"),
                    (val_min, ":gold_removed_leader", ":leader_wealth"),
                    (troop_remove_gold, ":leader", ":gold_removed_leader"),
                    (val_sub, ":amount", ":gold_removed_leader"),
                    (val_add, ":gold_removed", ":gold_removed_leader"),
                (try_end),

                (gt, ":amount", 0),
                (try_begin),
                    (is_between, ":party_type", spt_caravan, spt_convoy + 1),
                    (party_get_attached_to, ":attached_party", ":party_no"),
                    (party_get_slot, ":linked_center", ":party_no", slot_party_linked_party),
                    (ge, ":linked_center", centers_begin),
                    (eq, ":linked_center", ":attached_party"),
                    (party_get_slot, ":center_wealth", ":linked_center", slot_party_wealth),
                    (gt, ":center_wealth", 0),
                    (assign, ":gold_removed_center", ":amount"),
                    (val_min, ":gold_removed_center", ":center_wealth"),
                    (val_sub, ":center_wealth", ":gold_removed_center"),
                    (party_set_slot, ":linked_center", slot_party_wealth, ":center_wealth"),
                    (val_sub, ":amount", ":gold_removed_center"),
                    (val_add, ":gold_removed", ":gold_removed_center"),
                (try_end),                
            (try_end),

            (assign, reg0, ":gold_removed"),
        ]),

    # script_party_unpaid_wages_penalties
        # input:
        #   arg1: party_no
        #   arg2: unpaid_wages
        #   arg3: total_wages
        # output: none
    ("party_unpaid_wages_penalties",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":unpaid_wages", 2),
            (store_script_param, ":total_wages", 3),

            (party_get_slot, ":old_debts", ":party_no", slot_party_unpaid_wages),
            
            # Lose morale equals to 1/10th of the percentage of unpaid wages
            (store_mul, ":morale_penalties", ":unpaid_wages", 10),
            (val_div, ":morale_penalties", ":total_wages"),
            (val_mul, ":morale_penalties", -1),
            (try_begin),
                (call_script, "script_cf_debug", debug_economy),
                (str_store_party_name, s10, ":party_no"),
                (assign, reg10, ":unpaid_wages"),
                (assign, reg11, ":old_debts"),
                (display_message, "@{s10} has unpaid wages: {reg10} (old debts: {reg11})"),
            (try_end),
            (call_script, "script_party_change_morale", ":party_no", ":morale_penalties"),
            
            (val_add, ":old_debts", ":unpaid_wages"),
            (party_set_slot, ":party_no", slot_party_unpaid_wages, ":old_debts"),
        ]),

    # script_party_get_wages
        # input:
        #   arg1: party_no
        # output:
        #   reg0: party_wages
    ("party_get_wages", 
        [
            (store_script_param, ":party_no", 1),
            (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
            (party_get_slot, ":leader", ":party_no", slot_party_leader),
            (assign, ":party_wages", 0),
            (try_for_range, ":cur_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":troop_id", ":party_no", ":cur_stack"),
                (party_stack_get_size, ":stack_size", ":party_no", ":cur_stack"),
                (neq, ":leader", ":troop_id"),

                (call_script, "script_troop_get_wages", ":troop_id"),
                (store_mul, ":stack_wages", reg0, ":stack_size"),
                (val_add, ":party_wages", ":stack_wages"),
            (try_end),

            (call_script, "script_party_get_wages_modifier", ":party_no"),
            (assign, ":modifier", reg0),

            (val_mul, ":party_wages", ":modifier"),
            (val_div, ":party_wages", 100),

            (assign, reg0, ":party_wages"),
        ]),

    # script_party_get_wages_modifier
        # input: 
        #   arg1: party_no
        # output: 
        #   reg0: modifier
    ("party_get_wages_modifier", 
        [
            (store_script_param, ":party_no", 1),
            (assign, ":modifier", 1000),

            (try_begin),
                # Garrisoned troops pay 1/2th wages
                (is_between, ":party_no", centers_begin, centers_end),
                (val_div, ":modifier", 2),
                # ToDo: possible buildings reducing wages
            (else_try),
                (party_get_slot, ":party_leader", ":party_no", slot_party_leader),
                (try_begin), # 2% less per leadership point
                    (ge, ":party_leader", 0),
                    (store_skill_level, ":leadership", skl_leadership, ":party_leader"),
                    (val_mul, ":leadership", 20),
                    (val_sub, ":modifier", ":leadership"),
                (try_end),
            (try_end),
            (assign, reg0, ":modifier"),
        ]),

    # script_troop_get_wages_for_party
        # input:
        #   arg1: troop_no
        #   arg2: party_no
        # output: 
        #   reg0: troop_wages
    ("troop_get_wages_for_party",
        [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":party_no", 2),

            (call_script, "script_troop_get_wages", ":troop_no"),
            (assign, ":troop_wages", reg0),

            (call_script, "script_party_get_wages_modifier", ":party_no"),
            (assign, ":modifier", reg0),
            (val_mul, ":troop_wages", ":modifier"),
            (val_div, ":troop_wages", 100),

            (assign, reg0, ":troop_wages"),
        ]),

    # script_troop_get_wages
        # input:
        #   arg1: troop_no
        # output:
        #   reg0: troop_wages
    ("troop_get_wages",
        [
            (store_script_param, ":troop_no", 1),

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

            (assign, reg0, ":troop_level"),
        ]),

    # script_troop_change_relation_with_troop
        # input:
        #   arg1: troop_no
        #   arg2: other_troop_no
        #   arg3: change
    ("troop_change_relation_with_troop",
        [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":other_troop_no", 2),
            (store_script_param, ":change", 3),

            (store_sub, ":troop_no_offset", ":other_troop_no", npc_heroes_begin),
            (store_add, ":slot_rel_1", ":troop_no_offset", slot_troop_relations_begin),
            (troop_get_slot, ":relation_1", ":troop_no", ":slot_rel_1"),
            (val_add, ":relation_1", ":change"),
            (val_clamp, ":relation_1", -100, 101),
            (troop_set_slot, ":troop_no", ":slot_rel_1", ":relation_1"),

            (store_sub, ":other_troop_no_offset", ":troop_no", npc_heroes_begin),
            (store_add, ":slot_rel_2", ":other_troop_no_offset", slot_troop_relations_begin),
            (troop_get_slot, ":relation_2", ":other_troop_no", ":slot_rel_2"),
            (val_add, ":relation_2", ":change"),
            (val_clamp, ":relation_2", -100, 101),
            (troop_set_slot, ":other_troop_no", ":slot_rel_2", ":relation_2"),

            (try_begin),
                (call_script, "script_cf_debug", debug_simple),
                (str_store_troop_name, s10, ":troop_no"),
                (str_store_troop_name, s11, ":other_troop_no"),
                (assign, reg10, ":change"),
                (assign, reg11, ":relation_1"),
                (assign, reg12, ":relation_2"),
                (display_message, "@Relation {s10} - {s11} changed ({reg10}): {reg11} / {reg12}"),
            (try_end),
        ]),

    # script_troop_change_relation_with_party_heroes
        # input:
        #   arg1: troop_no
        #   arg2: party_no
        #   arg3: change
        # output: none
    ("troop_change_relation_with_party_heroes",
        [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":party_no", 2),
            (store_script_param, ":change", 3),

            # Iterate through other attached parties ?
            # (party_get_num_attached_parties, ":num_attached", ":party_no"),
            # (try_for_range, ":cur_attached", 0, ":num_attached"),
                # (party_get_attached_party_with_rank, ":cur_party", ":party_no", ":cur_attached"),
                (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
                (try_for_range, ":cur_stack", 0, ":num_stacks"),
                    (party_stack_get_troop_id, ":troop_id", ":party_no", ":cur_stack"),
                    (troop_is_hero, ":troop_id"),
                    (call_script, "script_troop_change_relation_with_troop", ":troop_no", ":troop_id", ":change"),
                (try_end),
                # (call_script, "script_change_troop_relation_with_party_group_heroes", ":troop_no", ":cur_party", ":change"),
            # (try_end),
        ]),

    # script_item_get_sell_price
        # input:
        #   arg1: item_no
        #   arg2: selling_party
        #   arg3: buying_party
        # output:
        #   reg0: sell_price
    ("item_get_sell_price",
        [
            (store_script_param, ":item_no", 1),
            (store_script_param, ":selling_party", 2),
            (store_script_param, ":buying_party", 3),

            (store_item_value, ":price", ":item_no"),
            (call_script, "script_item_get_sell_price_factor_from_party", ":item_no", ":selling_party", ":buying_party"),
            (assign, ":price_factor", reg0),
            (assign, ":tax_factor", reg1),

            (store_mul, ":final_price", ":price", ":price_factor"),
            (val_div, ":final_price", 100),

            (store_mul, ":tax_amount", ":price", ":tax_factor"),
            (val_div, ":tax_amount", 100),

            (assign, reg0, ":final_price"),
            (assign, reg1, ":tax_amount"),
        ]),

    # script_item_get_buy_price
        # input:
        #   arg1: item_no
        #   arg2: buying_party
        #   arg3: selling_party
        # output:
        #   reg0: buy_price
    ("item_get_buy_price",
        [
            (store_script_param, ":item_no", 1),
            (store_script_param, ":buying_party", 2),
            (store_script_param, ":selling_party", 3),

            (store_item_value, ":price", ":item_no"),
            (call_script, "script_item_get_buy_price_factor_from_party", ":item_no", ":buying_party", ":selling_party"),
            (assign, ":price_factor", reg0),
            (assign, ":tax_factor", reg1),

            (store_mul, ":final_price", ":price", ":price_factor"),
            (val_div, ":final_price", 100),

            (store_mul, ":tax_amount", ":price", ":tax_factor"),
            (val_div, ":tax_amount", 100),

            (assign, reg0, ":final_price"),
            (assign, reg1, ":tax_amount"),
        ]),

    # script_troop_prisoner
        # input:
        #   arg1: troop_no
        # output:
        #   reg0: troop_freed
    ("troop_prisoner", 
        [
            (store_script_param, ":troop_no", 1),

            (assign, ":freed", 0),

            (troop_get_slot, ":prisoner_of", ":troop_no", slot_troop_prisoner_of),
            (try_begin),
                (gt, ":prisoner_of", 0),
                (party_is_active, ":prisoner_of"),
                (party_count_prisoners_of_type, ":prisoner", ":prisoner_of", ":troop_no"),
                (gt, ":prisoner", 0),

                # ToDo: refine chance
                (store_random_in_range, ":rand", 0, 100),
                (try_begin),
                    (eq, ":rand", 0),
                    (call_script, "script_troop_released", ":troop_no"),
                    (assign, ":freed", 1),
                (try_end),
            (else_try),
                # Captor no longer valid
                (call_script, "script_troop_released", ":troop_no"),
                (assign, ":freed", 1),
            (try_end),

            (assign, reg0, ":freed"),
        ]),

    # script_update_troop_notes
        # input:
        #   arg1: troop_no
        # output: none
    ("update_troop_notes",
        [
            (store_script_param, ":troop_no", 1),

            (str_store_troop_name_link, s10, ":troop_no"),
            (display_message, "@Notes updated ({s10})"),
        ]),
    # script_update_faction_notes
        # input:
        #   arg1: faction_no
        # output: none
    ("update_faction_notes",
        [
            (store_script_param, ":faction_no", 1),

            (str_store_faction_name_link, s10, ":faction_no"),
            (display_message, "@Notes updated ({s10})"),
        ]),

    # script_update_party_notes
        # input:
        #   arg1: party_no
        # output: none
    ("update_party_notes",
        [
            (store_script_param, ":party_no", 1),

            (str_store_party_name_link, s10, ":party_no"),
            (display_message, "@Notes updated ({s10})"),
        ]),

    # script_troop_get_gold_rating
        # Get an estimation of the troops value in gold from the seer_troop
        # input: 
        #   arg1: troop_no
        #   arg2: seer_troop
        # output:
        #   reg0: gold_rating
    ("troop_get_gold_rating",
        [
            (store_script_param, ":troop_no", 1),
            (store_script_param, ":seer_troop", 2),

            (assign, ":gold_rating", 0),

            (try_for_range, ":item_slot", ek_item_0, ek_head),
                (troop_get_inventory_slot, ":item_no", ":troop_no", ":item_slot"),
                (call_script, "script_item_get_estimated_price", ":item_no", ":seer_troop"),
                (val_add, ":gold_rating", reg0),
            (try_end),

            (try_begin),
                (call_script, "script_cf_debug", debug_simple|debug_economy),
                (assign, reg10, ":gold_rating"),
                (str_store_troop_name, s10, ":troop_no"),
                (str_store_troop_name, s11, ":seer_troop"),
                (call_script, "script_game_get_money_text", reg10),
                (display_message, "@{s11} sees {s10} as valued {s0}."),
            (try_end),

            (assign, reg0, ":gold_rating"),
        ]),

    # script_item_get_estimated_price
        # input: 
        #   arg1: item_no
        #   arg2: troop_no
        # output:
        #   output: estimated_price
    ("item_get_estimated_price",
        [
            (store_script_param, ":item_no", 1),
            (store_script_param, ":troop_no", 2),

            (assign, ":estimated_price", 0),

            (store_item_value, ":real_price", ":item_no"),
            # Trade skill influences the random outcome
            (store_skill_level, ":trade", skl_trade, ":troop_no"),

            # We add different static elements to have a different number for each item/price/troop/day
            (store_add, ":rand", "$g_daily_random", ":real_price"),
            (val_add, ":rand", ":item_no"),
            (val_add, ":rand", ":troop_no"),

            (store_mod, ":percentage_error", ":rand", 11),
            (val_sub, ":percentage_error", 5),
            (store_sub, ":trade_penalties", 10, ":trade"),
            (val_mul, ":percentage_error", ":trade_penalties"),

            (store_mul, ":estimated_price", ":real_price", ":percentage_error"),
            (val_div, ":estimated_price", 100),
            (val_add, ":estimated_price", ":real_price"),

            (assign, reg0, ":estimated_price"),
        ]),

    # script_troop_bargain
        # input:
        #   arg1: bargaining_troop
        #   arg2: other_troop
        #   arg3: ratio_offered
        #   arg4: bargain_type
        #       -1: aggressive bargain, uses strength and indimidation
        #       1: friendly bargain, uses intelligence and persuasion
        #   arg5: difficulty
        # output:
        #   reg0: outcome
        #       outcome_success, outcome_neutral, outcome_failure
        # this script is called when bargain between 2 troops
    ("troop_bargain",
        [
            (store_script_param, ":bargaining_troop", 1),
            (store_script_param, ":other_troop", 2),
            (store_script_param, ":ratio_offered", 3),
            (store_script_param, ":bargain_type", 4),
            (store_script_param, ":difficulty", 5),

            (assign, ":outcome", outcome_neutral),

            (assign, ":skill", 0),
            (assign, ":attribute", 0),
            (assign, ":main_attribute_weight", 3),
            (assign, ":main_skill_weight", 5),

            (try_begin),
                (eq, ":bargain_type", bargain_type_strength),
                (assign, ":skill", skl_intimidation),
                (assign, ":attribute", ca_strength),
            (else_try),
                (assign, ":skill", skl_persuasion),
                (assign, ":attribute", ca_intelligence),
            (try_end),
            (store_skill_level, ":bargaining_troop_skill", ":skill", ":bargaining_troop"),
            (val_mul, ":bargaining_troop_skill", ":main_skill_weight"),

            (store_attribute_level, ":b_attribute", ":bargaining_troop", ":attribute"),
            (store_attribute_level, ":o_attribute", ":other_troop", ":attribute"),
            (val_mul, ":b_attribute", ":main_attribute_weight"),
            (val_mul, ":o_attribute", ":main_attribute_weight"),

            # Both persuasion use charisma (less weighted)
            (store_attribute_level, ":b_charisma", ":bargaining_troop", ca_charisma),
            (store_attribute_level, ":o_charisma", ":other_troop", ca_charisma),
            (val_add, ":b_attribute", ":b_charisma"),
            (val_add, ":o_attribute", ":o_charisma"),

            (store_sub, ":difference", ":b_attribute", ":o_attribute"),
            (val_add, ":difference", ":bargaining_troop_skill"),

            (val_add, ":difference", ":ratio_offered"),

            (store_add, ":difficulty_mult", ":difficulty", 100),
            (val_mul, ":difference", ":difficulty_mult"),
            (val_div, ":difference", 100),

            (store_div, ":neutral_offset", ":difficulty", 4),

            (try_begin),
                (gt, ":difference", 100),
                # Use 1/4th difficulty to have chance at neutral outcome.
                (store_sub, ":neutral", ":difference", ":neutral_offset"),
                (try_begin),
                    (gt, ":neutral", 100),
                    (assign, ":outcome", outcome_success),
                (try_end),
            (else_try),
                (lt, ":difference", 100),
                # Use 1/4th difficulty to have chance at neutral outcome.
                (store_add, ":neutral", ":difference", ":neutral_offset"),
                (try_begin),
                    (lt, ":neutral", 100),
                    (assign, ":outcome", outcome_failure),
                (try_end),
            (try_end),

            (try_begin),
                (call_script, "script_cf_debug", debug_simple|debug_war),
                (str_store_troop_name, s10, ":bargaining_troop"),
                (str_store_troop_name, s11, ":other_troop"),
                (assign, reg10, ":difference"),
                (assign, reg11, ":ratio_offered"),
                # (assign, reg12, ":outcome"),
                (store_add, ":bargain_string", ":outcome", "str_outcome_neutral"),
                (str_store_string, s12, ":bargain_string"),
                (display_message, "@{s10} bargain with {s11}: Offered ratio ({reg11}) transformed to {reg10}. Outcome is {s12}."),
            (try_end),

            (assign, reg0, ":outcome"),
        ]),

    # script_party_bargain
        # input:
        #   arg1: bargaining_party
        #   arg2: other_party
        #   arg3: ratio_offered
        #   arg4: bargain_type
        #   arg5: difficulty
        # output:
        #   reg0: outcome
        #       outcome_success, outcome_neutral, outcome_failure
        # this script is called when bargain between 2 parties
    ("party_bargain", 
        [
            (store_script_param, ":bargaining_party", 1),
            (store_script_param, ":other_party", 2),
            (store_script_param, ":ratio_offered", 3),
            (store_script_param, ":bargain_type", 4),
            (store_script_param, ":difficulty", 5),

            (assign, ":outcome", outcome_neutral),

            (try_begin),
                (eq, ":bargain_type", bargain_type_strength),
                (call_script, "script_party_group_calculate_strength", ":bargaining_party"),
                # We use sqrt to have lower influence on ratio
                (assign, ":strength", reg0),
                (assign, ":defense", reg1),
                (val_add, ":strength", ":defense"),
                (val_max, ":strength", 1),

                (call_script, "script_party_group_calculate_strength", ":other_party"),
                # We use sqrt to have lower influence on ratio
                (assign, ":other_party_strength", reg0),
                (assign, ":other_party_defense", reg1),
                (val_add, ":other_party_strength", ":other_party_defense"),
                (val_max, ":other_party_strength", 1),

                (val_mul, ":strength", 100),
                (val_div, ":strength", ":other_party_strength"),

                (val_mul, ":strength", ":ratio_offered"),
                (val_div, ":strength", 100),

                (assign, ":skill", 0),
                (try_begin),
                    (party_get_slot, ":leader", ":bargaining_party", slot_party_leader),
                    (this_or_next|gt, ":leader", 0),
                    (eq, ":bargaining_party", "$g_player_party"),

                    (store_skill_level, ":skill", ":leader", skl_intimidation),
                (try_end),

                (try_begin),
                    (party_get_slot, ":leader", ":other_party", slot_party_leader),
                    (this_or_next|gt, ":leader", 0),
                    (eq, ":bargaining_party", "$g_player_party"),

                    (store_skill_level, ":other_skill", ":leader", skl_intimidation),
                    (val_sub, ":skill", ":other_skill"),
                (try_end),

                (try_begin),
                    (neq, ":skill", 0),
                    (val_mul, ":skill", 2),
                    (val_add, ":skill", 100),
                    (val_mul, ":strength", ":skill"),
                    (val_div, ":strength", 100),
                (try_end),

                (try_begin),
                    (neq, ":difficulty", 0),
                    (store_add, ":difficulty_mult", ":difficulty", 100),
                    (val_mul, ":strength", ":difficulty_mult"),
                    (val_div, ":strength", 100),
                (try_end),

                (store_div, ":neutral_offset", ":difficulty", 4),

                (try_begin),
                    (gt, ":strength", 100),

                    (store_sub, ":neutral", ":strength", ":neutral_offset"),
                    (try_begin),
                        (gt, ":neutral", 100),
                        (assign, ":outcome", outcome_success),
                    (try_end),
                (else_try),
                    (lt, ":strength", 100),

                    (store_add, ":neutral", ":strength", ":neutral_offset"),
                    (try_begin),
                        (lt, ":neutral", 100),
                        (assign, ":outcome", outcome_failure),
                    (try_end),
                (try_end),
            # (else_try),
                # peaceful bargain type with parties ?
            (try_end),

            (try_begin),
                (call_script, "script_cf_debug", debug_simple|debug_war),
                (str_store_party_name, s10, ":bargaining_party"),
                (str_store_party_name, s11, ":other_party"),
                (assign, reg10, ":strength"),
                (assign, reg11, ":ratio_offered"),
                # (assign, reg12, ":outcome"),
                (store_add, ":bargain_string", ":outcome", "str_outcome_neutral"),
                (str_store_string, s12, ":bargain_string"),
                (display_message, "@{s10} bargain with {s11}: Offered ratio ({reg11}) transformed to {reg10}. Outcome is {s12}."),
            (try_end),

            (assign, reg0, ":outcome"),
        ]),

    # script_get_bandit_dialog
        # input:
        #   arg1: bandit_party
        #   arg2: string_id
        # output:
        #   s0: result_string
    ("get_bandit_dialog",
        [
            (store_script_param, ":bandit_party", 1),
            (store_script_param, ":string_id", 2),

            (store_faction_of_party, ":faction", ":bandit_party"),
            (try_begin),
                (is_between, ":faction", bandit_factions_begin, bandit_factions_end),
                (store_sub, ":offset", ":faction", bandit_factions_begin),
                (val_add, ":string_id", ":offset"),
                (str_store_string, s0, ":string_id"),
            (else_try),
                (str_store_string, s0, "str_dialog_error"),
            (try_end),
        ]),

    # script_party_take_player_party_prisoner
        # input:
        #   arg1: party_no
        # output: none
    ("party_take_player_party_prisoner",
        [
            (store_script_param, ":party_no", 1),

            (assign, "$g_player_captor_party", ":party_no"),
            
            (call_script, "script_party_group_defeat_party_group", ":party_no", "$g_player_party"),

            (troop_set_slot, "$g_player_troop", slot_troop_prisoner_of, ":party_no"),

            (set_camera_follow_party, ":party_no"),
            (rest_for_hours, 12, 1, 0),
            (disable_party, "$g_player_party"),
        ]),

    # script_player_party_free
        # input: none
        # output: none
    ("player_party_free",
        [
            (enable_party, "$g_player_party"),
            (call_script, "script_troop_freed", "$g_player_troop", -1),
            # (party_force_add_members, "$g_player_party", "$g_player_troop", 1),
            (party_relocate_near_party, "$g_player_party", "$g_player_captor_party", 5),
            (assign, "$g_player_captor_party", -1),

            (set_camera_follow_party, "$g_player_party"),
            (rest_for_hours, 0, 0, 0),
        ]),

    # script_troop_escape_chance
        # input:
        #   arg1: troop_no
        #   arg2: holder_party
        #   arg3: escape_type
        # output:
        #   reg0: outcome (1 success, -1 failure, 0)
    ("troop_escape_chance",
        [
            (store_script_param, ":troop_no", 1),
            # (store_script_param, ":holder_party", 2),
            (store_script_param, ":escape_type", 3),

            (assign, ":needed_value", 35),
            (assign, ":skill", 0),
            (assign, ":outcome", outcome_neutral),

            (try_begin),
                (eq, ":escape_type", escape_type_wits),
                (store_skill_level, ":skill_1", skl_persuasion, ":troop_no"),
                (store_skill_level, ":skill_2", skl_trade, ":troop_no"),
                (val_mul, ":skill_1", 2),
                (store_add, ":skill", ":skill_1", ":skill_2"),
            (else_try),
                (eq, ":escape_type", escape_type_agility),

                (store_skill_level, ":skill_1", skl_pathfinding, ":troop_no"),
                (store_skill_level, ":skill_2", skl_spotting, ":troop_no"),
                (store_skill_level, ":skill_3", skl_tracking, ":troop_no"),
                (store_add, ":skill", ":skill_1", ":skill_2"),
                (val_add, ":skill", ":skill_3"),
            (else_try),
                (eq, ":escape_type", escape_type_strength),

                (store_skill_level, ":skill_1", skl_intimidation, ":troop_no"),
                (store_skill_level, ":skill_2", skl_ironflesh, ":troop_no"),
                (store_skill_level, ":skill_3", skl_power_strike, ":troop_no"),
                (store_add, ":skill", ":skill_1", ":skill_2"),
                (val_add, ":skill", ":skill_3"),
            (try_end),

            (store_random_in_range, ":rand", 0, 41),
            (val_add, ":skill", ":rand"),

            (try_begin),
                (gt, ":skill", ":needed_value"),
                (assign, ":outcome", outcome_success),
            (else_try),
                (assign, ":outcome", outcome_failure),
            (try_end),

            (assign, reg0, ":outcome"),
        ]),

    # script_prepare_troop_followers
        # input: none
        # output: none
    ("prepare_troop_followers",
        [
            (try_for_range, ":lord_no", lords_begin, lords_end),
                (troop_set_slot, ":lord_no", slot_troop_num_followers, 0),
                (troop_set_slot, ":lord_no", slot_troop_num_followers_ready, 0),
            (try_end),
            (try_for_range, ":lord_no", lords_begin, lords_end),
                (troop_get_slot, ":occupation", ":lord_no", slot_troop_kingdom_occupation),
                (neg|troop_slot_ge, ":lord_no", slot_troop_prisoner_of, 0), # Do not process prisoners
                (try_begin),
                    (eq, ":occupation", tko_kingdom_hero),
                    (troop_get_slot, ":leaded_party", ":lord_no", slot_troop_leaded_party),
                    (ge, ":leaded_party", 0),
                    (party_is_active, ":leaded_party"),
                    (troop_get_slot, ":lord_mission", ":lord_no", slot_troop_mission),
                    (eq, ":lord_mission", tm_escorting),
                    (troop_get_slot, ":lord_mission_object", ":lord_no", slot_troop_mission_object),
                    (ge, ":lord_mission_object", 0),
                    (troop_get_slot, ":num_followers", ":lord_mission_object", slot_troop_num_followers),
                    (val_add, ":num_followers", 1),
                    (troop_set_slot, ":lord_mission_object", slot_troop_num_followers, ":num_followers"),
                    (troop_get_slot, ":lord_mission_object_party", ":lord_mission_object", slot_troop_leaded_party),
                    (ge, ":lord_mission_object_party", 1),
                    (party_is_active, ":lord_mission_object_party"),
                    (store_distance_to_party_from_party, ":distance", ":lord_mission_object_party", ":leaded_party"),
                    (le, ":distance", 4),
                    (troop_get_slot, ":num_followers_ready", ":lord_mission_object", slot_troop_num_followers_ready),
                    (val_add, ":num_followers_ready", 1),
                    (troop_set_slot, ":lord_mission_object", slot_troop_num_followers_ready, ":num_followers"),
                (try_end),
            (try_end),
            (try_begin),
                (call_script, "script_cf_debug", debug_ai),
                (try_for_range, ":lord_no", lords_begin, lords_end),
                    (troop_get_slot, ":followers", ":lord_no", slot_troop_num_followers),
                    (troop_get_slot, ":followers_ready", ":lord_no", slot_troop_num_followers_ready),
                    (gt, ":followers", 0),
                    (str_store_troop_name, s10, ":lord_no"),
                    (assign, reg10, ":followers"),
                    (assign, reg11, ":followers_ready"),
                    (display_message, "@Lord {s10} has {reg10} followers ({reg11} ready)"),
                (try_end),
            (try_end),
        ]),

    # script_party_create_debt
        # input:
        #   arg1: debtor
        #   arg2: creditor
        #   arg3: amount
        # output: none
    ("party_create_debt",
        [
            (store_script_param, ":debtor", 1),
            (store_script_param, ":creditor", 2),
            (store_script_param, ":amount", 3),

            (store_mul, ":debtor_amount", ":amount", -1),

            (try_begin),
                (call_script, "script_cf_debug", debug_economy),

                (str_store_party_name, s10, ":debtor"),
                (str_store_party_name, s11, ":creditor"),
                (assign, reg10, ":amount"),
                
                (display_message, "@{s10} creating debt for {s11} ({reg10})"),
            (try_end),

            # TODO: for now we transfer the gold directly
            (call_script, "script_party_modify_wealth", ":debtor", ":debtor_amount"),
            (call_script, "script_party_modify_wealth", ":creditor", ":amount"),
        ]),

    # script_party_process_attached_parties
        # input:
        #   arg1: party_no
        # output: none
    ("party_process_attached_parties",
        [
            (store_script_param, ":party_no", 1),

            (party_get_slot, ":party_type", ":party_no", slot_party_type),
            (party_get_slot, ":attached_party_1", ":party_no", slot_party_attached_party_1),
            (party_get_slot, ":attached_party_2", ":party_no", slot_party_attached_party_2),

            (try_begin),
                (eq, ":party_type", spt_town),
                # patrols
                (try_begin),
                    (le, ":attached_party_1", 0),
                    (call_script, "script_cf_party_create_patrol", ":party_no", slot_party_attached_party_1),
                (else_try),
                    (neg|party_is_active, ":attached_party_1"),
                    (party_set_slot, ":party_no", slot_party_attached_party_1, -1),
                    (try_begin),
                        (call_script, "script_cf_debug", debug_war),
                        (str_store_party_name, s10, ":party_no"),
                        (display_message, "@{s10} releasing inactive attached party"),
                    (try_end),
                (try_end),
                # caravans
                (try_begin),
                    (le, ":attached_party_2", 0),
                    (call_script, "script_cf_party_create_caravan", ":party_no", slot_party_attached_party_2),
                (else_try),
                    (neg|party_is_active, ":attached_party_2"),
                    (party_set_slot, ":party_no", slot_party_attached_party_2, -1),
                    (try_begin),
                        (call_script, "script_cf_debug", debug_war),
                        (str_store_party_name, s10, ":party_no"),
                        (display_message, "@{s10} releasing inactive attached party 2"),
                    (try_end),
                (try_end),
            (else_try),
                (eq, ":party_type", spt_castle),
                # patrols
            (else_try),
                (eq, ":party_type", spt_village),
                # villagers
                # patrols
            (try_end),
        ]),

    # script_cf_party_create_patrol
        # input:
        #   arg1: party_no
        #   arg2: store_slot
        # output: none
    ("cf_party_create_patrol",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":slot", 2),

            (call_script, "script_cf_center_can_give_troops", ":party_no"),

            (store_faction_of_party, ":party_faction", ":party_no"),
            (party_get_slot, ":attached_party_reserved_wages", ":party_no", slot_party_budget_reserved_auxiliaries),

            (call_script, "script_spawn_party_around_party", ":party_no", "pt_patrol"),
            (assign, ":spawned_party", reg0),

            (party_set_faction, ":spawned_party", ":party_faction"),
            (party_set_slot, ":spawned_party", slot_party_budget_reserved_party, ":attached_party_reserved_wages"),
            (party_set_slot, ":spawned_party", slot_party_wanted_party_wages, ":attached_party_reserved_wages"),
            (party_set_slot, ":spawned_party", slot_party_type, spt_patrol),
            (party_set_slot, ":spawned_party", slot_party_linked_party, ":party_no"),

            (store_current_hours, ":hours"),
            (party_set_slot, ":spawned_party", slot_party_last_rest, ":hours"),

            (party_set_slot, ":party_no", ":slot", ":spawned_party"),
            (call_script, "script_party_give_troops_to_party", ":party_no", ":spawned_party", 5),
            (try_begin),
                (call_script, "script_cf_debug", debug_war|debug_ai),
                (str_store_party_name, s10, ":party_no"),
                (display_message, "@{s10} generating attached party patrol"),
            (try_end),
        ]),

    # script_cf_party_create_caravan
        # input:
        #   arg1: party_no
        #   arg2: store_slot
        # output: none
    ("cf_party_create_caravan",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":slot", 2),
            
            (call_script, "script_cf_center_can_give_troops", ":party_no"),

            (assign, ":end", goods_end),
            (assign, ":continue", 0),
            (try_for_range, ":good", goods_begin, ":end"),
                (store_sub, ":offset", ":good", goods_begin),
                (store_add, ":amount_slot", ":offset", slot_party_ressources_current_amount_begin),
                (store_add, ":production_slot", ":offset", slot_party_item_last_produced_begin),
                (store_add, ":consumption_slot", ":offset", slot_party_item_consumed_begin),

                (party_get_slot, ":amount", ":party_no", ":amount_slot"),
                (party_get_slot, ":production", ":party_no", ":production_slot"),
                (party_get_slot, ":consumption", ":party_no", ":consumption_slot"),

                (store_sub, ":difference", ":production", ":consumption"),
                (lt, ":difference", 0),
                (store_div, ":ticks_left", ":amount", ":difference"),
                # We don't want to send a caravan if we still have >10 ticks of storage
                (gt, ":ticks_left", -10),

                (assign, ":continue", 1),
                (assign, ":end", goods_begin),
            (try_end),
            (eq, ":continue", 1),

            (store_faction_of_party, ":party_faction", ":party_no"),
            (party_slot_eq, ":party_no", slot_party_faction, ":party_faction"),
            # (party_get_slot, ":attached_party_reserved_wages", ":party_no", slot_party_budget_reserved_auxiliaries),
            # (val_div, ":attached_party_reserved_wages", 2),

            (call_script, "script_spawn_party_around_party", ":party_no", "pt_caravan"),
            (assign, ":spawned_party", reg0),

            (party_set_faction, ":spawned_party", ":party_faction"),
            (party_set_slot, ":spawned_party", slot_party_budget_reserved_party, 5000),
            (party_set_slot, ":spawned_party", slot_party_wanted_party_wages, 5000),
            (party_set_slot, ":spawned_party", slot_party_type, spt_caravan),
            (party_set_slot, ":spawned_party", slot_party_linked_party, ":party_no"),
            (party_set_slot, ":spawned_party", slot_party_mission_object, -1),

            (party_set_slot, ":party_no", ":slot", ":spawned_party"),

            (faction_get_slot, ":culture", ":party_faction", slot_faction_culture),
            (faction_get_slot, ":caravan_master", ":culture", slot_faction_caravan_master),
            (try_begin),
                (gt, ":caravan_master", 0),
                (party_force_add_members, ":spawned_party", ":caravan_master", 1),
            (else_try),
                (party_force_add_members, ":spawned_party", "trp_swadian_caravan_master", 1),
            (try_end),
            (try_begin),
                (call_script, "script_cf_debug", debug_trade|debug_ai),
                (str_store_party_name, s10, ":party_no"),
                (display_message, "@{s10} generating attached party caravan"),
            (try_end),
        ]),

    # script_cf_center_can_give_troops
        # input:
        #   arg1: center_no
        # output: none
    ("cf_center_can_give_troops",
        [
            (store_script_param, ":center_no", 1),

            (call_script, "script_party_get_wages", ":center_no"),
            (assign, ":center_wages", reg0),
            (call_script, "script_party_get_prefered_wages_limit", ":center_no"),
            (store_div, ":center_limit", reg1, 2),
            (try_begin),
                (party_slot_eq, ":center_no", slot_party_type, spt_village),
                (val_div, ":center_limit", 2), # Forces villages to give troops to their lord
            (try_end),
            (gt, ":center_wages", ":center_limit"), # Do not give troops if not enough men in the center
        ]),

    # script_party_give_prisoners_to_party
        # input:
        #   arg1: party_giver
        #   arg2: party_receiver
        # output:
        #   reg0: num_prisoners_given
    ("party_give_prisoners_to_party",
        [
            (store_script_param, ":party_giver", 1),
            (store_script_param, ":party_receiver", 2),

            (assign, ":num_prisoners_given", 0),

            (party_get_num_prisoner_stacks, ":num_prisoner_stacks", ":party_giver"),
            (try_for_range_backwards, ":cur_stack", 0, ":num_prisoner_stacks"),
                (party_prisoner_stack_get_troop_id, ":prisoner_troop_id", ":party_giver", ":cur_stack"),

                (party_prisoner_stack_get_size, ":stack_size", ":party_giver", ":cur_stack"),

                (party_remove_prisoners, ":party_giver", ":prisoner_troop_id", ":stack_size"),
                (assign, ":removed", reg0),
                (gt, ":removed", 0),
                (val_add, ":num_prisoners_given", ":stack_size"),
                (party_force_add_prisoners, ":party_receiver", ":prisoner_troop_id", ":stack_size"),
                (try_begin),
                    (troop_is_hero, ":prisoner_troop_id"),
                    (troop_set_slot, ":prisoner_troop_id", slot_troop_prisoner_of, ":party_receiver"),
                (try_end),
            (try_end),
            (assign, reg0, ":num_prisoners_given"),
        ]),

    # script_party_patrol_process
        # input:
        #   arg1: party_no
        # output: none
    ("party_patrol_process",
        [
            (store_script_param, ":party_no", 1),

            (party_get_slot, ":last_rest", ":party_no", slot_party_last_rest),
            (party_get_slot, ":home", ":party_no", slot_party_linked_party),
            (call_script, "script_party_get_wages", ":party_no"),
            (assign, ":current_wages", reg0),

            (party_get_num_companions, ":num_troops", ":party_no"),
            (party_get_num_prisoners, ":num_prisoners", ":party_no"),
            (val_mul, ":num_prisoners", 2),

            (store_current_hours, ":hours"),
            (store_sub, ":rest_time", ":hours", ":last_rest"),

            (call_script, "script_party_get_prefered_wages_limit", ":party_no"),
            (assign, ":wanted_wages", reg0),
            (assign, ":min_wages", reg1),
            # (assign, ":max_wages", reg2),


            (assign, ":go_home", 0),
            (try_begin),
                (ge, ":num_prisoners", ":num_troops"),
                (assign, ":go_home", 1),
            (else_try),
                (gt, ":rest_time", 10*24),
                (assign, ":go_home", 1),
            (else_try),
                (le, ":current_wages", ":min_wages"),
                (assign, ":go_home", 1),
            # (else_try),
            #     (ge, ":current_wages", ":max_wages"),
            #     (assign, ":go_home", 1),
            (try_end),

            (try_begin),
                # Do center business
                (party_get_cur_town, ":cur_town", ":party_no"),
                (try_begin),
                    (is_between, ":cur_town", centers_begin, centers_end),

                    (party_set_slot, ":party_no", slot_party_last_rest, ":hours"),
                    (try_begin),
                        (ge, ":num_prisoners", 1),
                        (call_script, "script_party_give_prisoners_to_party", ":party_no", ":cur_town"),
                    (try_end),
                    (try_begin),
                        (le, ":current_wages", ":wanted_wages"),
                        (assign, ":go_home", 1),

                        (call_script, "script_cf_center_can_give_troops", ":cur_town"),
                        (store_random_in_range, ":num_troops", 3, 7),
                        (call_script, "script_party_give_troops_to_party", ":cur_town", ":party_no", ":num_troops"),
                    (try_end),
                (try_end),
            (try_end),
            (try_begin),
                (eq, ":go_home", 1),
                (call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_party, ":home"),
                # Go back home
            # (else_try),
                # Assist another party ?
            (else_try),
                # Patrol center
                (party_get_slot, ":home", ":party_no", slot_party_linked_party),
                (call_script, "script_party_set_behavior", ":party_no", tai_patroling_center, ":home"),
            (try_end),
        ]),

    # script_party_caravan_process
        # input:
        #   arg1: party_no
        # output: none
    ("party_caravan_process",
        [
            (store_script_param, ":party_no", 1),

            (party_get_slot, ":mission_object", ":party_no", slot_party_mission_object),
            (party_get_slot, ":mission", ":party_no", slot_party_mission),
            (party_get_cur_town, ":cur_town", ":party_no"),
            (party_get_slot, ":home", ":party_no", slot_party_linked_party),

            (try_begin),
                (eq, ":cur_town", ":mission_object"),
                (is_between, ":cur_town", centers_begin, centers_end),

                (store_current_hours, ":hours"),
                (try_begin),
                    (eq, ":cur_town", ":home"),
                    (call_script, "script_party_get_wages", ":party_no"),
                    (assign, ":current_wages", reg0),
                    (call_script, "script_party_get_prefered_wages_limit", ":party_no"),
                    (assign, ":wanted_wages", reg0),

                    (party_get_num_prisoners, ":num_prisoners", ":party_no"),
                    (try_begin),
                        (ge, ":num_prisoners", 1),
                        (call_script, "script_party_give_prisoners_to_party", ":party_no", ":cur_town"),
                    (try_end),

                    (call_script, "script_party_empty_goods", ":party_no", ":home"),
                    (call_script, "script_party_caravan_select_destination", ":party_no"),
                    (assign, ":new_destination", reg0),
                    (try_begin),
                        (le, ":current_wages", ":wanted_wages"),
                        (eq, ":cur_town", ":home"),
                        (try_begin),
                            (call_script, "script_cf_center_can_give_troops", ":cur_town"),
                            (store_random_in_range, ":num_troops", 3, 7),
                            (call_script, "script_party_give_troops_to_party", ":cur_town", ":party_no", ":num_troops"),
                        (try_end),
                    (else_try),
                        (eq, ":new_destination", ":home"),
                        (call_script, "script_party_caravan_set_objectives", ":party_no"),
                        (try_begin),
                            (party_slot_ge, ":party_no", slot_party_mission_objective_1, goods_begin),
                            (call_script, "script_party_caravan_set_destination", ":party_no"),
                        (else_try),
                            (call_script, "script_cf_debug", debug_trade),
                            (str_store_party_name, s10, ":party_no"),
                            (str_store_party_name, s11, ":home"),
                            (display_message, "@{s10} from {s11} has no objective and stays put"),
                        (try_end),
                    (else_try),
                        (party_set_slot, ":party_no", slot_party_mission, spm_trade),
                        (party_set_slot, ":party_no", slot_party_mission_object, ":new_destination"),
                        (call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_party, ":new_destination"),
                    (try_end),

                (else_try),
                    (eq, ":mission", spm_trade),
                    (party_set_slot, ":party_no", slot_party_mission, spm_waiting),
                    (party_set_slot, ":party_no", slot_party_last_rest, ":hours"),
                    (call_script, "script_party_caravan_clear_destination", ":party_no", ":cur_town"),
                (else_try),
                    (party_get_slot, ":last_rest", ":party_no", slot_party_last_rest),
                    (store_sub, ":rest_time", ":hours", ":last_rest"),
                    (gt, ":rest_time", 18),
                    (call_script, "script_party_caravan_select_destination", ":party_no"),
                    (assign, ":new_destination", reg0),
                    (call_script, "script_party_caravan_prepare_trading_run", ":party_no", ":new_destination", ":cur_town"),
                    (party_set_slot, ":party_no", slot_party_mission, spm_trade),
                    (party_set_slot, ":party_no", slot_party_mission_object, ":new_destination"),
                    (call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_party, ":new_destination"),
                (try_end),
            (else_try),
                (eq, ":mission_object", -1),
                (call_script, "script_party_caravan_select_destination", ":party_no"),
                (assign, ":new_destination", reg0),

                (try_begin),
                    (is_between, ":new_destination", centers_begin, centers_end),
                    (neq, ":cur_town", ":new_destination"),
                    (party_set_slot, ":party_no", slot_party_mission, spm_trade),
                    (party_set_slot, ":party_no", slot_party_mission_object, ":new_destination"),
                    (call_script, "script_party_set_behavior", ":party_no", tai_traveling_to_party, ":new_destination"),
                (try_end),
            (try_end),
        ]),

    # script_party_caravan_set_objectives
        # input:
        #   arg1: party_no
        # output: none
    ("party_caravan_set_objectives",
        [
            (store_script_param, ":party_no", 1),
            (party_get_slot, ":home", ":party_no", slot_party_linked_party),

            (assign, ":end_loop", slot_party_mission_objective_3 + 1),
            (try_for_range, ":slot", slot_party_mission_objective_1, ":end_loop"),
                (assign, ":chosen_item", 0),
                (assign, ":chosen_item_score", 9999),
                (try_for_range, ":item", goods_begin, goods_end),

                    (assign, ":exists", 0),
                    (try_for_range, ":other_slot", slot_party_mission_objective_1, slot_party_mission_objective_3 + 1),
                        (party_get_slot, ":other_value", ":party_no", ":other_slot"),
                        (eq, ":other_value", ":item"),
                        (assign, ":exists", 1),
                    (try_end),
                    (try_begin),
                        (eq, ":exists", 0),
                        (call_script, "script_party_item_get_caravan_score", ":home", ":item"),
                        (assign, ":score", reg0),
                        (lt, ":score", ":chosen_item_score"),
                        (assign, ":chosen_item", ":item"),
                        (assign, ":chosen_item_score", ":score"),
                    (try_end),
                (try_end),

                (try_begin),
                    (lt, ":chosen_item_score", 9999),
                    (gt, ":chosen_item", goods_begin),
                    (party_set_slot, ":party_no", ":slot", ":chosen_item"),

                    (try_begin),
                        (call_script, "script_cf_debug", debug_trade),
                        (str_store_party_name, s10, ":home"),
                        (str_store_item_name, s11, ":chosen_item"),
                        (assign, reg10, ":chosen_item_score"),
                        (display_message, "@Caravan from {s10} targets {s11} : {reg10}"),
                    (try_end),
                (else_try),
                    (assign, ":end_loop", 0),
                (try_end),
            (try_end),

        ]),

    # script_party_caravan_select_destination
        # input:
        #   arg1: party_no
        # output:
        #   reg0: destination
    ("party_caravan_select_destination",
        [
            (store_script_param, ":party_no", 1),

            (party_get_slot, ":current_destination", ":party_no", slot_party_mission_object),
            (try_begin),
                (party_get_slot, ":option_1", ":party_no", slot_party_mission_target_1),
                (is_between, ":option_1", centers_begin, centers_end),
                (neq, ":option_1", ":current_destination"),
                (assign, reg0, ":option_1"),
            (else_try),
                (party_get_slot, ":option_2", ":party_no", slot_party_mission_target_2),
                (is_between, ":option_2", centers_begin, centers_end),
                (neq, ":option_2", ":current_destination"),
                (assign, reg0, ":option_2"),
            (else_try),
                (party_get_slot, ":option_3", ":party_no", slot_party_mission_target_3),
                (is_between, ":option_3", centers_begin, centers_end),
                (neq, ":option_3", ":current_destination"),
                (assign, reg0, ":option_3"),
            (else_try),
                (party_get_slot, ":linked_party", ":party_no", slot_party_linked_party),
                (is_between, ":linked_party", centers_begin, centers_end),
                (assign, reg0, ":linked_party"),
            (else_try),
                (assign, reg0, -1),
            (try_end),
        ]),


    # script_party_caravan_set_destination
        # input:
        #   arg1: party_no
        # output: none
    ("party_caravan_set_destination",
        [
            (store_script_param, ":party_no", 1),
            (party_get_slot, ":home", ":party_no", slot_party_linked_party),

            (store_faction_of_party, ":party_faction", ":party_no"),
            (assign, ":end_loop", slot_party_mission_target_3 + 1),
            (try_for_range, ":slot", slot_party_mission_target_1, ":end_loop"),

                (assign, ":chosen_center", 0),
                (assign, ":chosen_center_score", 9999),
                (try_for_range, ":center", towns_begin, towns_end),

                    (try_begin),
                        (store_faction_of_party, ":center_faction", ":center"),
                        (store_relation, ":relation", ":center_faction", ":party_faction"),
                        (lt, ":relation", 0),
                    (else_try),
                        (assign, ":exists", 0),
                        (try_for_range, ":other_slot", slot_party_mission_target_1, slot_party_mission_target_3 + 1),
                            (party_get_slot, ":other_value", ":party_no", ":other_slot"),
                            (eq, ":other_value", ":center"),
                            (assign, ":exists", 1),
                        (try_end),
                        (try_begin),
                            (eq, ":exists", 0),
                            (neq, ":center", ":home"),
                            (call_script, "script_party_center_get_caravan_score", ":center", ":party_no", ":home", caravan_score_type_buying),
                            (assign, ":score", reg0),
                            (lt, ":score", ":chosen_center_score"),
                            (assign, ":chosen_center", ":center"),
                            (assign, ":chosen_center_score", ":score"),
                        (try_end),
                    (try_end),
                (try_end),

                (try_begin),
                    (lt, ":chosen_center_score", 9999),
                    (ge, ":chosen_center", towns_begin),
                    (party_set_slot, ":party_no", ":slot", ":chosen_center"),

                    (try_begin),
                        (call_script, "script_cf_debug", debug_trade),
                        (str_store_party_name, s10, ":home"),
                        (str_store_party_name, s11, ":chosen_center"),
                        (assign, reg10, ":chosen_center_score"),
                        (display_message, "@Caravan from {s10} targets {s11} : {reg10}"),
                    (try_end),
                (else_try),
                    (assign, ":end_loop", 0),
                (try_end),
            (try_end),
        ]),

    # script_party_center_get_caravan_score
        # input:
        #   arg1: center
        #   arg2: caravan
        #   arg3: caravan_home
        #   arg4: score_type: caravan_score_type_buying / caravan_score_type_selling / caravan_score_type_all
        # output:
        #   reg0: score
    ("party_center_get_caravan_score",
        [
            (store_script_param, ":center", 1),
            (store_script_param, ":caravan", 2),
            (store_script_param, ":caravan_home", 3),
            (store_script_param, ":score_type", 4),

            (store_distance_to_party_from_party, ":distance", ":center", ":caravan_home"),
            (store_mul, ":distance_score", ":distance", caravan_score_distance_ratio),
            (val_div, ":distance_score", 100),

            (assign, ":resource_score", 0),

            (assign, ":has_objective", 0),
            (store_add, ":end", slot_party_mission_objective_3, 1),
            (try_for_range, ":objective_slot", slot_party_mission_objective_1, ":end"),
                (party_get_slot, ":objective", ":caravan", ":objective_slot"),
                (is_between, ":objective", goods_begin, goods_end),
                (assign, ":has_objective", 1),
            (try_end),

            (try_for_range, ":resource", goods_begin, goods_end),
                (assign, ":continue", 0),
                (try_begin),
                    (eq, ":has_objective", 1),
                    (assign, ":is_objective", 0),
                    (store_add, ":end", slot_party_mission_objective_3, 1),
                    (try_for_range, ":objective_slot", slot_party_mission_objective_1, ":end"),
                        (party_slot_eq, ":caravan", ":objective_slot", ":resource"),
                        (assign, ":is_objective", 1),
                    (try_end),
                    (try_begin),
                        (eq, ":is_objective", 1),
                        (assign, ":continue", 1),
                    (try_end),
                (else_try),
                    (assign, ":continue", 1),
                (try_end),

                (eq, ":continue", 1),
                (call_script, "script_party_item_get_caravan_score", ":center", ":resource"),
                (assign, ":score", reg0),
                (try_begin),
                    (eq, ":score_type", caravan_score_type_buying),
                    (val_sub, ":resource_score", ":score"),
                (else_try),
                    (eq, ":score_type", caravan_score_type_selling),
                    (val_add, ":resource_score", ":score"),
                (else_try),
                    (val_abs, ":score"),
                    (val_sub, ":resource_score", ":score"),
                (try_end),
            (try_end),

            (store_add, ":total", ":distance_score", ":resource_score"),

            # (try_begin),
            #     (call_script, "script_cf_debug", debug_trade),
            #     (str_store_party_name, s10, ":caravan_home"),
            #     (str_store_party_name, s11, ":center"),
            #     (assign, reg10, ":resource_score"),
            #     (assign, reg12, ":distance_score"),
            #     (assign, reg13, ":total"),
            #     (display_message, "@Caravan from {s10} score for {s11} : {reg10} + distance {reg12} = {reg13}"),
            # (try_end),

            (assign, reg0, ":total"),
        ]),

    # script_party_item_get_caravan_score
        # input:
        #   arg1: center
        #   arg2: item
        # output:
        #   reg0: score : <0 => center wants to buy - >0 => center wants to sell
    ("party_item_get_caravan_score",
        [
            (store_script_param, ":center", 1),
            (store_script_param, ":item", 2),

            (store_sub, ":offset", ":item", goods_begin),
            (store_add, ":production_slot", slot_party_item_last_produced_begin, ":offset"),
            (store_add, ":consumption_slot", slot_party_item_consumed_begin, ":offset"),
            (store_add, ":amount_slot", slot_party_ressources_current_amount_begin, ":offset"),
            (party_get_slot, ":center_production", ":center", ":production_slot"),
            (party_get_slot, ":center_consumption", ":center", ":consumption_slot"),
            (party_get_slot, ":center_amount", ":center", ":amount_slot"),

            # (assign, ":resource_need_score", 0),
            # (assign, ":resource_amount_score", 0),

            (store_mul, ":center_score", ":center_amount", caravan_score_resource_amount_ratio),
            (val_div, ":center_score", 100),

            (store_sub, ":center_offset", ":center_production", ":center_consumption"),
            (store_mul, ":center_offset_score", ":center_offset", caravan_score_resource_production_ratio),
            (val_div, ":center_offset_score", 100),

            (assign, ":score", 0),

            (try_begin),
                (eq, ":center_offset_score", 0),
                # We are uncertain on if we want to buy or sell

                (store_sub, ":score", ":center_score", 50),
                # (val_div, ":score", 10),
            (else_try),
                (gt, ":center_offset_score", 0),
                # We might want to sell this item -> positive score

                (store_sub, ":score", ":center_offset_score", ":center_score"),
                (val_max, ":score", 0),
            (else_try),
                # We might want to buy this item -> negative score

                (store_add, ":score", ":center_offset_score", ":center_score"),
                (val_min, ":score", 0),
            (try_end),

            # (party_get_slot, ":caravan_home", ":caravan", slot_party_linked_party),

            # (party_get_slot, ":caravan_home_production", ":caravan_home", ":production_slot"),
            # (party_get_slot, ":caravan_home_consumption", ":caravan_home", ":consumption_slot"),
            # (store_sub, ":caravan_home_offset", ":caravan_home_production", ":caravan_home_consumption"),

            # (try_begin),
            #     # (ge, ":caravan_home_offset", 0),
            #     (try_begin),
            #         (neq, ":score_type", caravan_score_type_buying),
            #         # We want to buy
            #         (store_mul, ":current_resource_amount_score", ":center_offset", 1),
            #         # (store_mul, ":current_resource_need_score", ":caravan_home_offset", -1),

            #         (val_add, ":resource_amount_score", ":current_resource_amount_score"),
            #         # (val_add, ":resource_need_score", ":current_resource_need_score"),
            #     (try_end),
            # (else_try),
            #     # (lt, ":caravan_home_offset", 0),
            #     (try_begin),
            #         (neq, ":score_type", caravan_score_type_selling),
            #         # We want to sell
            #         (store_mul, ":current_resource_amount_score", ":center_offset", -1),
            #         # (store_mul, ":current_resource_need_score", ":caravan_home_offset", 1),

            #         (val_add, ":resource_amount_score", ":current_resource_amount_score"),
            #         # (val_add, ":resource_need_score", ":current_resource_need_score"),
            #     (try_end),
            # (try_end),

            # (val_mul, ":resource_amount_score", caravan_score_resource_production_ratio),
            # (val_div, ":resource_amount_score", 100),
            # (val_mul, ":resource_need_score", caravan_score_resource_need_ratio),
            # (val_div, ":resource_need_score", 100),

            # (store_add, ":score", ":resource_amount_score", ":resource_need_score"),
            (assign, reg0, ":score"),
        ]),

    # script_party_caravan_clear_destination
        # input:
        #   arg1: party_no
        #   arg2: clear_destination
        # output: none
    ("party_caravan_clear_destination",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":clear_destination", 2),

            (try_begin),
                (party_get_slot, ":option", ":party_no", slot_party_mission_target_1),
                (eq, ":option", ":clear_destination"),
                (party_set_slot, ":party_no", slot_party_mission_target_1, -1),
            (else_try),
                (party_get_slot, ":option", ":party_no", slot_party_mission_target_2),
                (eq, ":option", ":clear_destination"),
                (party_set_slot, ":party_no", slot_party_mission_target_2, -1),
            (else_try),
                (party_get_slot, ":option", ":party_no", slot_party_mission_target_3),
                (eq, ":option", ":clear_destination"),
                (party_set_slot, ":party_no", slot_party_mission_target_3, -1),
            (try_end),
        ]),

    # script_party_caravan_prepare_trading_run
        # input:
        #   arg1: party_caravan
        #   arg2: destination
        #   arg3: origin
        # output: none
    ("party_caravan_prepare_trading_run",
        [
            (store_script_param, ":party_caravan", 1),
            (store_script_param, ":destination", 2),
            (store_script_param, ":origin", 3),

            (assign, ":number_objectives", 0),
            (try_for_range, ":slot", slot_party_mission_objective_1, slot_party_mission_objective_3 + 1),
                (party_slot_ge, ":party_caravan", ":slot", goods_begin),
                (val_add, ":number_objectives", 1),
            (try_end),

            (assign, ":total_amount", 0),
            (try_for_range, ":item", goods_begin, goods_end),
                (store_sub, ":offset", ":item", goods_begin),
                (store_add, ":slot_amount", slot_party_ressources_current_amount_begin, ":offset"),
                (party_get_slot, ":amount", ":party_caravan", ":slot_amount"),
                (val_add, ":total_amount", ":amount"),
            (try_end),
            (store_sub, ":remaining_cargo", caravan_max_cargo_size, ":total_amount"),

            (try_begin),
                (gt, ":number_objectives", 0),
                (store_div, ":amount_goal", caravan_max_cargo_size, ":number_objectives"),
                (try_for_range, ":item", goods_begin, goods_end),
                    (assign, ":is_objective", 0),
                    (try_begin),
                        (store_sub, ":offset", ":item", goods_begin),
                        (store_add, ":slot_amount", slot_party_ressources_current_amount_begin, ":offset"),
                        (party_get_slot, ":amount", ":party_caravan", ":slot_amount"),
                        (lt, ":amount", ":amount_goal"),
                        (try_for_range, ":slot", slot_party_mission_objective_1, slot_party_mission_objective_3 + 1),
                            (party_slot_eq, ":party_caravan", ":slot", ":item"),
                            (assign, ":is_objective", 1),
                        (try_end),
                    (try_end),
                    (try_begin),
                        (eq, ":is_objective", 1),
                        (store_sub, ":offset", ":item", goods_begin),
                        (store_add, ":slot_amount", slot_party_ressources_current_amount_begin, ":offset"),
                        (party_get_slot, ":amount", ":party_caravan", ":slot_amount"),
                        (le, ":amount", ":amount_goal"),
                        (store_sub, ":amount_to_buy", ":amount_goal", ":amount"),
                        (call_script, "script_party_buy_item_from_party", ":party_caravan", ":item", ":origin", ":amount_to_buy"),
                        (val_sub, ":remaining_cargo", reg0),
                    (try_end),
                (try_end),
            (try_end),

            (try_begin),
                (gt, ":remaining_cargo", 0),
                # TODO: buy goods to sell to next destination
            (try_end),
            (try_begin),
                (call_script, "script_cf_debug", debug_trade),
                (assign, reg10, ":remaining_cargo"),
                (str_store_party_name, s10, ":party_caravan"),
                (str_store_party_name, s11, ":origin"),
                (str_store_party_name, s12, ":destination"),
                (display_message, "@Caravan {s10} from {s11} has {reg10} cargo space heading for {s12}"),
            (try_end),
        ]),

    # script_item_get_buy_price_factor_from_party
        # input:
        #   arg1: item_no
        #   arg2: party_buyer
        #   arg3: party_no
        # output:
        #   reg0: price_factor
        #   reg0: tax_factor
    ("item_get_buy_price_factor_from_party",
        [
            (store_script_param, ":item_no", 1),
            (store_script_param, ":party_buyer", 2),
            (store_script_param, ":party_no", 3),

            (assign, ":price", 300),
            
            (try_begin),
                (is_between, ":party_no", centers_begin, centers_end),
                (is_between, ":item_no", goods_begin, goods_end),
                (party_get_slot, ":own_production", ":party_no", ":item_no"),
                (store_sub, ":production_modifier", 20, ":own_production"),
                (try_begin),
                    # We reduce the effect of own production the more we produce
                    # It is to avoid buying for ridiculous prices in highly productive places
                    (lt, ":production_modifier", 0), 
                    (store_mul, ":inv_prod", ":production_modifier", -1),
                    (val_div, ":inv_prod", 15),
                    (val_add, ":inv_prod", 1),
                    (val_div, ":production_modifier", ":inv_prod"),
                (try_end),
                (val_sub, ":price", ":production_modifier"),
            (try_end),
            
            (call_script, "script_party_get_skill_level", ":party_buyer", skl_trade),
            (assign, ":trade_skill", reg0),

            (val_mul, ":trade_skill", 5),
            (val_sub, ":price", ":trade_skill"),

            (party_get_slot, ":tax_rate", ":party_no", slot_party_taxes_buy),
            (val_add, ":price", ":tax_rate"),

            (assign, reg0, ":price"),
            (assign, reg1, ":tax_rate"),
        ]),

    # script_item_get_sell_price_factor_from_party
        # input:
        #   arg1: item_no
        #   arg2: party_seller
        #   arg3: party_no
        # output:
        #   reg0: price_factor
        #   reg0: tax_factor
    ("item_get_sell_price_factor_from_party",
        [
            (store_script_param, ":item_no", 1),
            (store_script_param, ":party_seller", 2),
            (store_script_param, ":party_no", 3),

            (assign, ":price", 25),
            
            (try_begin),
                (is_between, ":party_no", centers_begin, centers_end),
                (is_between, ":item_no", goods_begin, goods_end),
                (party_get_slot, ":own_production", ":party_no", ":item_no"),
                (store_add, ":production_modifier", -20, ":own_production"),
                (try_begin),
                    # We reduce the effect of own production the more we produce
                    # It is to avoid selling for ridiculous prices in highly productive places
                    (gt, ":production_modifier", 0),
                    (store_div, ":prod", ":production_modifier", 30),
                    (val_add, ":prod", 1),
                    (val_div, ":production_modifier", ":prod"),
                (try_end),
                (val_sub, ":price", ":production_modifier"),
            (try_end),
            
            (call_script, "script_party_get_skill_level", ":party_seller", skl_trade),
            (assign, ":trade_skill", reg0),

            (val_mul, ":trade_skill", 4),
            (val_add, ":price", ":trade_skill"),
            
            # (val_min, ":price", 95),
            (val_max, ":price", 5),

            (val_max, ":price", 105),
            
            (party_get_slot, ":tax_rate", ":party_no", slot_party_taxes_sell),
            (val_sub, ":price", ":tax_rate"),

            (assign, reg0, ":price"),
            (assign, reg1, ":tax_rate"),
        ]),

    # script_party_buy_item_from_party
        # input:
        #   arg1: party_buyer
        #   arg2: item
        #   arg3: party_seller
        #   arg4: amount_wanted
        # output:
        #   reg0: amount_bought
    ("party_buy_item_from_party",
        [
            (store_script_param, ":party_buyer", 1),
            (store_script_param, ":item", 2),
            (store_script_param, ":party_seller", 3),
            (store_script_param, ":amount_wanted", 4),

            (assign, ":amount_bought", 0),
            (try_begin),
                (call_script, "script_cf_party_can_sell_item", ":party_seller", ":item"),

                (store_sub, ":offset", ":item", goods_begin),
                (store_add, ":amount_slot", slot_party_ressources_current_amount_begin, ":offset"),
                (party_get_slot, ":seller_amount", ":party_seller", ":amount_slot"),

                # We don't want to buy everything
                (store_div, ":max_amount", ":seller_amount", 2),

                (val_min, ":amount_wanted", ":max_amount"),

                (call_script, "script_item_get_buy_price", ":item", ":party_buyer", ":party_seller"),
                (assign, ":price", reg0),
                (assign, ":tax", reg1),

                (store_mul, ":total_price", ":price", ":amount_wanted"),
                (store_mul, ":total_cost", ":total_price", -1),
                (store_mul, ":total_tax", ":tax", ":amount_wanted"),
                (val_add, ":total_cost", ":total_tax"),

                (store_sub, ":new_seller_amount", ":seller_amount", ":amount_wanted"),
                (party_set_slot, ":party_seller", ":amount_slot", ":new_seller_amount"),

                (party_get_slot, ":buyer_amount", ":party_buyer", ":amount_slot"),
                (val_add, ":buyer_amount", ":amount_wanted"),
                (party_set_slot, ":party_buyer", ":amount_slot", ":buyer_amount"),

                (call_script, "script_party_modify_wealth", ":party_buyer", ":total_cost"),
                (call_script, "script_party_transfer_wealth", ":party_buyer", ":party_seller", ":total_tax", tax_type_trade),

                (val_add, ":amount_bought", ":amount_wanted"),

                (try_begin),
                    (call_script, "script_cf_debug", debug_trade),
                    (str_store_party_name, s10, ":party_buyer"),
                    (str_store_item_name, s11, ":item"),
                    (str_store_party_name, s12, ":party_seller"),
                    (assign, reg10, ":amount_bought"),
                    (display_message, "@{s10} buying {reg10} {s11} from {s12}"),
                (try_end),

            (try_end),

            (assign, reg0, ":amount_bought"),
        ]),

    # script_cf_party_can_sell_item
        # input:
        #   arg1: party_seller
        #   arg2: item
        # output: none
    ("cf_party_can_sell_item",
        [
            # (store_script_param, ":party_seller", 1),
            # (store_script_param, ":item", 2),

            # TODO: refine, for now we always sell items

            (eq, 1, 1),
        ]),

    # script_party_enter_center
        # input:
        #   arg1: party_no
        #   arg2: center_no
        # output: none
    ("party_enter_center",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":center_no", 2),

            (party_attach_to_party, ":party_no", ":center_no"),

            (try_begin),
                (is_between, ":center_no", centers_begin, centers_end),
                (party_get_slot, ":taxes", ":center_no", slot_party_taxes_visit),
                (gt, ":taxes", 0),

                # The party is not a party created by the center
                (party_get_slot, ":linked_party", ":party_no", slot_party_linked_party),
                (neq, ":linked_party", ":center_no"),

                # The party is not the leader of the center
                (assign, ":is_leader", 0),
                (try_begin),
                    (party_slot_eq, ":party_no", slot_party_type, spt_war_party),
                    
                    (party_get_slot, ":center_leader", ":center_no", slot_party_leader),
                    (party_get_slot, ":party_leader", ":party_no", slot_party_leader),
                    (eq, ":center_leader", ":party_leader"),
                    (ge, ":center_leader", 0),
                    (ge, ":party_leader", 0),

                    (assign, ":is_leader", 1),
                (try_end),

                (eq, ":is_leader", 0),

                (call_script, "script_party_transfer_wealth", ":party_no", ":center_no", ":taxes", tax_type_visitor),
            (try_end),
        ]),

    # script_party_transfer_wealth
        # input:
        #   arg1: party_giver
        #   arg2: party_receiver
        #   arg3: amount
        #   arg4: tax_type - optional if transfer is not part of a tax
        # output: none
    ("party_transfer_wealth",
        [
            (store_script_param, ":party_giver", 1),
            (store_script_param, ":party_receiver", 2),
            (store_script_param, ":amount", 3),
            (store_script_param, ":tax_type", 4),


            (try_begin),
                (is_between, ":party_receiver", centers_begin, centers_end),
                (gt, ":tax_type", tax_type_none),
                (call_script, "script_party_add_accumulated_taxes", ":party_receiver", ":amount", ":tax_type"),
            (else_try),
                (call_script, "script_party_modify_wealth", ":party_receiver", ":amount"),
            (try_end),
            (store_mul, ":payment", ":amount", -1),
            (call_script, "script_party_modify_wealth", ":party_giver", ":payment"),
        ]),

    # script_party_get_skill_level
        # input:
        #   arg1: party_no
        #   arg2: skill
        # output:
        #   reg0: skill_value
    ("party_get_skill_level",
        [
            (store_script_param, ":party_no", 1),
            (store_script_param, ":skill", 2),

            # TODO: maybe to refine ? parties without leader seem to have random stat returned ?

            (party_get_skill_level, reg0, ":party_no", ":skill"),
        ]),

    # script_party_empty_goods
        # input:
        #   arg1: party_no
        #   arg2: party_container
        # output: none
    ("party_empty_goods",
        [
            (store_script_param, ":party", 1),
            (store_script_param, ":party_container", 2),

            (try_for_range, ":item", goods_begin, goods_end),
                (store_sub, ":offset", ":item", goods_begin),
                (store_add, ":amount_slot", ":offset", slot_party_ressources_current_amount_begin),

                (party_get_slot, ":good_amount", ":party", ":amount_slot"),
                (party_set_slot, ":party", ":amount_slot", 0),

                (party_get_slot, ":container_good_amount", ":party_container", ":amount_slot"),
                (val_add, ":container_good_amount", ":good_amount"),
                (party_set_slot, ":party_container", ":amount_slot", ":container_good_amount"),

                (try_begin),
                    (call_script, "script_cf_debug", debug_trade|debug_economy),
                    (str_store_party_name, s10, ":party"),
                    (str_store_party_name, s11, ":party_container"),
                    (str_store_item_name, s12, ":item"),
                    (assign, reg10, ":good_amount"),
                    (display_message, "@{s10} move {reg10} {s12} to {s11}"),
                (try_end),
            (try_end),
        ]),
]
