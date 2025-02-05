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
            (display_message, "@Starting banner selection"),
            (start_presentation, "prsnt_banner_selection"),
        ]),	
]
