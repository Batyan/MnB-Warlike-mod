from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from module_constants import *





triggers = [

    (0.1, 0, ti_once,
        [
            (map_free, 0),
            (neg|troop_slot_ge, "$g_player_troop", slot_troop_banner_scene_prop, 1),
            (troop_slot_eq, "$g_player_troop", slot_troop_noble, 1),
        ],
        [
            (start_presentation, "prsnt_banner_selection"),
        ]),	

    (1, 0, ti_once,
        [
            (map_free, 0),

            (neq, "$g_intro_tutorial_trigger_date", 0),

            (call_script, "script_get_current_day"),
            (assign, ":current_day", reg0),
            (gt, ":current_day", "$g_intro_tutorial_trigger_date"),
        ],
        [
            (try_begin),
                (check_quest_active, "qst_introduction_waiting"),
                # (call_script, "script_succeed_quest", "qst_introduction_waiting"),

                (quest_get_slot, ":giver", "qst_introduction_waiting", slot_quest_giver_troop),
                (quest_get_slot, ":destination", "qst_introduction_waiting", slot_quest_destination),
            
                (party_set_flags, ":destination", pf_always_visible, 1),
                (party_set_note_available, ":destination", 1),

                (str_store_troop_name, s10, ":giver"),
                (str_store_party_name, s11, ":destination"),
                (str_store_string, s0, "@You received a letter indicating that {s10} wishes to see you.^You can meet him at the tavern of {s11}."),
                (call_script, "script_quest_add_note", "qst_introduction_waiting", 0),

                (jump_to_menu, "mnu_intro_quest_summon_letter"),
            (else_try),
                # Trigger consequences for refusing to help
            (try_end),
        ]), 
]
