from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *
pmf_is_prisoner = 0x0001


pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small


party_templates = [

    ###############
    ## Hardcoded ##
	###############
    ("none","none",icon_player,0,fac_commoners,merchant_personality,[]),
    ("rescued_prisoners","Rescued Prisoners",icon_player,0,fac_commoners,merchant_personality,[]),
    ("enemy","Enemy",icon_player,0,fac_commoners,merchant_personality,[]),
    ("hero_party","Hero Party",icon_player,0,fac_commoners,merchant_personality,[]),

    ###########
	## Other ##
	###########
	
	("village_template", "Village template", icon_village_a|pf_village, 0, fac_commoners, 0, []),
	("castle_template", "Castle template", icon_castle_a|pf_castle, 0, fac_commoners, 0, []),
	("town_template", "Town template", icon_town|pf_village, 0, fac_commoners, 0, []),
	
	("hunters", "Hunters", icon_axeman, 0, fac_commoners, aggressiveness_1|courage_6, [(trp_common_hunter, 2, 6),]),
	("caravan", "Caravan", icon_mule, 0, fac_commoners, 0, []),
	("peasants", "Peasants", icon_peasant, 0, fac_commoners, 0, []),
	("patrol", "Patrol", icon_vaegir_knight, pf_show_faction, fac_commoners, 0, []),
	("scout", "Scout", icon_player_horseman, pf_show_faction, fac_commoners, 0, []),
	("war_party", "War Party", icon_gray_knight, pf_show_faction|pf_default_behavior, fac_commoners, 0, []),
	
	("reinforcements", "Reinforcements", icon_axeman, 0, fac_commoners, convoy_personality, []),
	
	("templates_end", "end", 0, 0, 0, 0, [ ]),
]
