from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *




############
## Scales ##
############
banner_scale = 0.3
avatar_scale = 0.15





###############
## Map Icons ##
###############
map_icons = [

    ("player", 0, "player", avatar_scale, snd_footstep_grass, 0.15, 0.173, 0),
    ("player_horseman", 0, "player_horseman", avatar_scale, snd_gallop, 0.15, 0.173, 0),
	
	("gray_knight",0,"knight_a", avatar_scale, snd_gallop, 0.15, 0.173, 0),
	("vaegir_knight",0,"knight_b", avatar_scale, snd_gallop, 0.15, 0.173, 0),
	("flagbearer_a",0,"flagbearer_a", avatar_scale, snd_gallop, 0.15, 0.173, 0),
	("flagbearer_b",0,"flagbearer_b", avatar_scale, snd_gallop, 0.15, 0.173, 0),
	("peasant",0,"peasant_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
	("khergit",0,"khergit_horseman", avatar_scale,snd_gallop, 0.15, 0.173, 0),
	("khergit_horseman_b",0,"khergit_horseman_b", avatar_scale,snd_gallop, 0.15, 0.173, 0),
	("axeman",0,"bandit_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
	("woman",0,"woman_a", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
	("woman_b",0,"woman_b", avatar_scale,snd_footstep_grass, 0.15, 0.173, 0),
	
	("town",mcn_no_shadow,"map_town_a", 0.35,0),
	("town_snow",mcn_no_shadow,"map_town_snow_a", 0.35,0),
	("town_steppe",mcn_no_shadow,"map_town_steppe_a", 0.35,0),
	("town_desert",mcn_no_shadow,"map_town_desert_a", 0.35,0),
	
	("castle_a",mcn_no_shadow,"map_castle_a", 0.35,0),
	("castle_b",mcn_no_shadow,"map_castle_b", 0.35,0),
	("castle_c",mcn_no_shadow,"map_castle_c", 0.35,0),
	("castle_d",mcn_no_shadow,"map_castle_d", 0.35,0),
	("castle_snow_a",mcn_no_shadow,"map_castle_snow_a", 0.35,0),
	("castle_snow_b",mcn_no_shadow,"map_castle_snow_b", 0.35,0),
	
	("village_a",mcn_no_shadow,"map_village_a", 0.45, 0),
	("village_b",mcn_no_shadow,"map_village_b", 0.45, 0),
	("village_c",mcn_no_shadow,"map_village_c", 0.45, 0),
	("village_burnt_a",mcn_no_shadow,"map_village_burnt_a", 0.45, 0),
	("village_deserted_a",mcn_no_shadow,"map_village_deserted_a", 0.45, 0),
	("village_burnt_b",mcn_no_shadow,"map_village_burnt_b", 0.45, 0),
	("village_deserted_b",mcn_no_shadow,"map_village_deserted_b", 0.45, 0),
	("village_burnt_c",mcn_no_shadow,"map_village_burnt_c", 0.45, 0),
	("village_deserted_c",mcn_no_shadow,"map_village_deserted_c", 0.45, 0),
	("village_snow_a",mcn_no_shadow,"map_village_snow_a", 0.45, 0),
	("village_snow_burnt_a",mcn_no_shadow,"map_village_snow_burnt_a", 0.45, 0),
	("village_snow_deserted_a",mcn_no_shadow,"map_village_snow_deserted_a", 0.45, 0),
	
	("camp",mcn_no_shadow,"camp_tent", 0.13, 0),
	("ship",mcn_no_shadow,"boat_sail_on", 0.23, snd_footstep_grass, 0.0, 0.05, 0),
	("ship_on_land",mcn_no_shadow,"boat_sail_off", 0.23, 0),
	("mule",0,"icon_mule", 0.2,snd_footstep_grass, 0.15, 0.173, 0),
	("cattle",0,"icon_cow", 0.2,snd_footstep_grass, 0.15, 0.173, 0),
	("training_ground",mcn_no_shadow,"training", 0.35,0),
	
	("bridge_a",mcn_no_shadow,"map_river_bridge_a", 1.27,0),
	("bridge_b",mcn_no_shadow,"map_river_bridge_b", 0.7,0),
	("bridge_snow_a",mcn_no_shadow,"map_river_bridge_snow_a", 1.27,0),

	("bandit_lair",mcn_no_shadow,"map_bandit_lair", 0.45, 0),

	# Banners

	("heraldic_banner_01", 0,"custom_map_banner_01", banner_scale, 0,
	[
		(ti_on_init_map_icon,
		[
			(store_trigger_param_1, ":party_no"),
			(cur_map_icon_set_tableau_material, "tableau_heraldic_banner_square", ":party_no"),
		]),
	]),
	("heraldic_banner_02", 0,"custom_map_banner_02", banner_scale, 0,
	[
		(ti_on_init_map_icon,
		[
			(store_trigger_param_1, ":party_no"),
			(cur_map_icon_set_tableau_material, "tableau_heraldic_banner_short", ":party_no"),
		]),
	]),
	("heraldic_banner_03", 0,"custom_map_banner_03", banner_scale, 0,
	[
		(ti_on_init_map_icon,
		[
			(store_trigger_param_1, ":party_no"),
			(cur_map_icon_set_tableau_material, "tableau_heraldic_banner_tall", ":party_no"),
		]),
	]),
]
