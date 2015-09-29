from ID_items import *
from ID_quests import *
from ID_factions import *
from ID_meshes import *


################
## Item Slots ##
################

item_slots = 0



slot_building_cost_wood		= 1
slot_building_cost_stone	= 2
slot_building_cost_gold		= 3
slot_building_build_time	= 4

#################
## Agent Slots ##
#################

agent_slots = 0

slot_agent_new_division = 1

slot_agent_is_in_scripted_mode	= 2
slot_agent_target_entry_point	= 3
slot_agent_is_not_reinforcement	= 4

slot_agent_charge = 5

slot_agent_bodyguard_1 = 6
slot_agent_bodyguard_2 = 7
slot_agent_guarding = 6

slot_agent_bodyguard_troop_1 = 8
slot_agent_bodyguard_troop_2 = 9

slot_agent_forced_defend = 10


    
###################
## Faction Slots ##
###################

faction_slots = 0

slot_faction_banner	= 1

slot_faction_troop_ratio_infantry			= 2
slot_faction_troop_ratio_spearman			= 3
slot_faction_troop_ratio_pikeman			= 4
slot_faction_troop_ratio_skirmisher			= 5
slot_faction_troop_ratio_shock_infantry		= 6
slot_faction_troop_ratio_archer				= 7
slot_faction_troop_ratio_crossbow			= 8
slot_faction_troop_ratio_cavalry			= 9
slot_faction_troop_ratio_lancer				= 10
slot_faction_troop_ratio_horse_archer		= 11
slot_faction_troop_ratio_mounted_skirmisher	= 12

# Culture Master Begin
slot_faction_template_troops_begin	= 13

slot_faction_names_begin			= 14
slot_faction_names_end				= 15

slot_faction_lord_name_begin		= 16

slot_faction_troops_begin			= 17
slot_faction_troops_end				= 18

# slot_faction_base_reinforcements	= 13

slot_faction_peasant_begin			= 17
slot_faction_common_begin			= 20
slot_faction_veteran_begin			= 21
slot_faction_elite_begin			= 22
slot_faction_noble_begin			= 23

# slot_faction_peasant_template_begin = 24
# slot_faction_common_template_begin = 25
# slot_faction_veteran_template_begin = 26
# slot_faction_elite_template_begin = 27
# slot_faction_noble_template_begin = 28
# slot_faction_templates_end = 29
# Culture Master End

slot_faction_leader					= 30
slot_faction_marshall				= 31

slot_faction_peasant_num_tries = 32
slot_faction_common_num_tries = 33
slot_faction_veteran_num_tries = 34
slot_faction_elite_num_tries = 35
slot_faction_noble_num_tries = 36

slot_faction_current_free_center = 37

slot_faction_culture = 38

slot_faction_peasant_template_end = 39
slot_faction_common_template_end = 40
slot_faction_veteran_template_end = 41
slot_faction_elite_template_end = 42
slot_faction_noble_template_end = 43

slot_faction_is_at_war = 44

slot_faction_lord_gathering = 45

slot_faction_master_culture = 46

# slot_faction_troop_ratio_begin = slot_faction_troop_ratio_infantry

slot_faction_era = 47		# Current era the faction is at
slot_faction_era_time = 48	# Time at which the faction has attained this era

slot_faction_num_vassals = 49
slot_faction_num_fiefs = 50

#################
## Party Slots ##
#################

party_slots = 0

slot_party_type				= 1

spt_caravan		= 5
spt_civilian	= 6
spt_war_party	= 7
spt_patrol		= 8
spt_scout		= 9
spt_convoy		= 10

spt_village		= 11
spt_castle		= 12
spt_town		= 13
spt_fort		= 14

slot_party_leader			= 2
slot_party_lord				= slot_party_leader

slot_party_weather_wet 		= 3
slot_party_weather_heat		= 4

slot_party_mission 			= 5

spm_colonise	= 1
spm_courier		= 2
spm_trade		= 3
spm_gather		= 4
spm_reinforce	= 5

slot_party_mission_object	= 6

slot_party_wealth 			= 7
slot_party_population 		= 8

population_max_town = 5000
population_max_castle = 50
population_max_village = 500

slot_party_ressource_radius = 9

slot_party_linked_party		= 10

slot_party_num_hunters 		= 11
slot_party_num_peasants		= 12
slot_party_num_caravans		= 13
slot_party_num_patrols		= 14
slot_party_num_scouts		= 15
# slot_party_num_

slot_party_ressources_begin = itm_spice # 18
slot_party_ressources_end = itm_sumpter_horse # 55
slot_party_ressources_count = slot_party_ressources_end - slot_party_ressources_begin # 37

slot_party_ressources_temp_modifiers_begin = slot_party_ressources_end # 55
slot_party_ressources_temp_modifiers_end = slot_party_ressources_temp_modifiers_begin + slot_party_ressources_count # 92

slot_party_building_slot_1	= 101
slot_party_building_slot_2	= 102
slot_party_building_slot_3	= 103
slot_party_building_slot_4	= 104
slot_party_building_slot_5	= 105
slot_party_building_slot_6	= 106
slot_party_building_slot_7	= 107
slot_party_building_slot_8	= 108
slot_party_building_slot_9	= 109
slot_party_building_slot_10	= 110

slot_party_building_state_1 = 111
slot_party_building_state_2 = 112
slot_party_building_state_3 = 113
slot_party_building_state_4 = 114
slot_party_building_state_5 = 115
slot_party_building_state_6 = 116
slot_party_building_state_7 = 117
slot_party_building_state_8 = 118
slot_party_building_state_9 = 119
slot_party_building_state_10 = 120

pbs_destroyed	= 0
pbs_healthy		= 1
pbs_damaged		= 2

slot_party_original_faction = 121

slot_party_besieged_by = 122

slot_party_battle_stage = 123

bs_approach = 1
bs_approach_2 = 2
bs_approach_3 = 3
bs_approach_4 = 4
bs_charge = 5
bs_charge_2 = 6
bs_melee = 7

slot_party_siege_scene = 124
# 125
# 126


#################
## Scene Slots ##
#################

scene_slots = 0

slot_scene_num_defend_points = 1

slot_scene_num_attack_spawn = 2

slot_scene_num_archer_points = 3



#################
## Troop Slots ##
#################

troop_slots = 0

slot_troop_temp_slot				= 0
slot_troop_temp_hire_number			= slot_troop_temp_slot

slot_troop_banner_scene_prop		= 1

slot_troop_type						= 2
tt_infantry				= 1
tt_spearman				= 2
tt_pikeman				= 3
tt_skirmisher			= 4
tt_shock_infantry		= 5
tt_archer				= 6
tt_crossbow				= 7
tt_cavalry				= 8
tt_lancer				= 9
tt_horse_archer			= 10
tt_mounted_skirmisher	= 11

slot_troop_quality					= 3
tq_peasant		= 0
tq_common		= 1
tq_veteran		= 2
tq_elite		= 3
tq_noble		= 4


slot_troop_lord_equipement 			= 4
tle_none = 0
tle_light_bow = 1
tle_heavy_bow = 2
tle_light_crossbow = 3
tle_heavy_crossbow = 4
tle_throwing = 5
tle_polearm = 6

slot_troop_lord_horse 				= 5

slot_troop_original_faction 		= 6

slot_troop_rank 					= 7 # real rank
slot_troop_level					= 8 # current rank
slot_troop_equipement_level			= 9 # current rank

# slot_troop_mercenary_captain_1		= slot_troop_level				# Only troops
# slot_troop_mercenary_captain_2		= slot_troop_equipement_level	# Only troops

slot_troop_kingdom_occupation 		= 12
tko_none = 0
tko_kingdom_hero = 1
tko_mercenary = 2

slot_troop_personality 				= 13
tp_default = 0x0000

tp_mercyfull = 0x0001
tp_mercyless = 0x0002

tp_cautious = 0x0004
tp_haste = 0x0008 # ToDo

tp_generous = 0x0010
tp_ = 0x0020 # ToDo

tp_noble = 0x0040 # ToDo
tp_renega = 0x0080 # ToDO

# tp_

slot_troop_leaded_party				= 14

slot_troop_building_one 			= 15
slot_troop_building_end				= 16

slot_troop_days_next_rethink		= 17

slot_troop_num_vassal				= 18
slot_troop_vassal_of				= 19

slot_troop_home						= 20

slot_troop_mission 					= 21
tm_none					= 0
# tm_gathering_army 		= 1
# tm_sieging_center 		= 2
# tm_raiding_center 		= 3
tm_defending			= 1
tm_attacking			= 2
tm_escorting			= 3

slot_troop_mission_object			= 22

slot_troop_behavior_object 			= 23
slot_troop_behavior 				= 24

slot_troop_prisoner_of				= 25 # Only heroes

slot_troop_faction_reserved_1		= 25 # Only regulars
slot_troop_faction_reserved_2		= 26
slot_troop_faction_not_1			= 27
slot_troop_faction_not_2			= 28

slot_troop_armor_weight 			= 29
slot_troop_horse_weight 			= 30
slot_troop_ranged_weapon_weight 	= 31

weight_very_light = 0
weight_light = 1
weight_medium = 2
weight_heavy = 3
weight_very_heavy = 4

slot_troop_last_met 				= 32

slot_troop_surplus_center			= 33

slot_troop_gathering				= 34

slot_troop_last_attack				= 35
slot_troop_last_rest				= 36
<<<<<<< HEAD

slot_troop_archer_score				= 37
=======
>>>>>>> origin/master

##################
## Player Slots ##
##################

player_slots = 0




################
## Team Slots ##
################

team_slots = 0

slot_team_test_faction		= 1
slot_team_test_strength		= 2
slot_team_test_spawn_point	= 3

slot_team_formation			= 4
stf_default 			= 0 # inf: 1, 			archer: 2, 			cav: 3
stf_shieldwall 			= 1 # inf shield: 1, 	archer: 2, 			cav: 3, rest: 4
stf_mounted_skirmisher 	= 3 # inf: 1, 			archer: 2, 			cav: 3, harcher: 4
stf_skirmisher 			= 4 # inf: 1, 			archer+throw: 2, 	cav: 3
stf_thrower 			= 5 # inf: 1, 			archer: 2, 			cav: 3, thrower: 4
stf_lance 				= 6 # inf: 1, 			archer: 2, 			cav: 3, lancer: 4
stf_pikewall 			= 7 # inf: 1, 			archer: 2, 			cav: 3, pike+spear: 4
stf_archers 			= 8 # inf: 1, 			archer: 2, 			cav: 3, thrower: 4
stf_siege				= 9 # archer+throw: 1
stf_siege_no_throw		= 10 # archer: 1


slot_team_tactic			= 5
stt_default = 0
stt_shieldwall = 1
stt_defend = 2
stt_short_engage = 3

slot_team_battle_phase		= 6
stbp_deploy = 0
stbp_advance = 1
stbp_engage = 2
stbp_combat = 3

stbp_siege_one = 1
stbp_siege_two = 2

slot_team_harcher_division	= 7
slot_team_horse_division	= 8
slot_team_throw_division	= 9
slot_team_archer_division	= 10
slot_team_shield_division	= 11
slot_team_rest_division		= 12
slot_team_pike_division		= 13
slot_team_lance_division	= 14

slot_team_division_1_number = 15
slot_team_division_2_number = 16
slot_team_division_3_number = 17
slot_team_division_4_number = 18
slot_team_division_5_number = 19
slot_team_division_6_number = 20
slot_team_division_7_number = 21
slot_team_division_8_number = 22
slot_team_division_9_number = 23

slot_team_num_division		= 24



#################
## Quest Slots ##
#################

quest_slots = 0





##########################
## Party Template Slots ##
##########################

party_template_slots = 0

slot_party_template_num_troop_1 = 1
slot_party_template_num_troop_2 = 2
slot_party_template_num_troop_3 = 3
slot_party_template_num_troop_4 = 4
slot_party_template_num_troop_5 = 5
slot_party_template_num_troop_6 = 6

slot_party_template_type_troop_1 = 7
slot_party_template_type_troop_2 = 8
slot_party_template_type_troop_3 = 9
slot_party_template_type_troop_4 = 10
slot_party_template_type_troop_5 = 11
slot_party_template_type_troop_6 = 12



######################
## Scene Prop Slots ##
######################

scene_prop_slots = 0





###########
## Other ##
###########

other = 0

banner_meshes_begin = "mesh_banner_a01"
banner_meshes_end = "mesh_banner_mesh_end"
banner_meshes_end_minus_one = 1

banner_scene_props_begin = "spr_banner_a"
banner_scene_props_end = "spr_banner_end"
banner_scene_props_end_minus_one = "spr_banner_kingdom_f"

npc_kingdoms_begin = 0
npc_kingdoms_end = 1

arms_meshes_begin = mesh_arms_a01
arms_meshes_end = mesh_troop_label_banner

# PARTIES
centers_begin = "p_town_11"
centers_end = "p_centers_end"

towns_begin		= centers_begin
castles_begin	= "p_castle_1a"
villages_begin	= "p_village_111"
towns_end		= castles_begin
castles_end		= villages_begin
villages_end	= centers_end

walled_centers_begin = towns_begin
walled_centers_end = castles_end

# FACTIONS
kingdoms_begin = fac_kingdom_1
kingdoms_end = fac_kingdoms_end

small_kingdoms_begin = fac_small_kingdom_11
small_kingdoms_end = kingdoms_end

cultures_begin = fac_culture_1
cultures_end = fac_cultures_end

# ITEMS
goods_begin = "itm_spice"
goods_end = "itm_saddle_horse"

horses_begin = goods_end
horses_end = "itm_arrows"
light_horses_begin = horses_begin
light_horses_end = "itm_sumpter_horse"
medium_horses_begin = light_horses_end
medium_horses_end = "itm_hunter"
heavy_horses_begin = medium_horses_end
heavy_horses_end = "itm_warhorse"
armoured_horses_begin = heavy_horses_end
armoured_horses_end = horses_end

ammo_begin = horses_end
ammo_end = "itm_leather_gloves"

gloves_begin = ammo_end
gloves_end = "itm_wrapping_boots"

boots_begin = gloves_end
boots_end = "itm_red_shirt"

armors_begin = boots_end
armors_end = "itm_head_wrappings"

very_light_armors_begin = armors_begin
light_armors_begin = "itm_leather_armor"
medium_armors_begin = "itm_studded_leather_coat"
heavy_armors_begin = "itm_brigandine_red"

headgear_begin = armors_end
headgear_end = "itm_wooden_stick"

weapons_begin = headgear_end
weapons_end = "itm_wooden_shield"

shields_begin = weapons_end
shields_end = "itm_stones"

ranged_weapons_begin = shields_end
ranged_weapons_end = "itm_items_end"

throwing_weapons_begin = ranged_weapons_begin
throwing_weapons_end = "itm_hunting_bow"

archers_weapons_begin = throwing_weapons_end
archers_weapons_end = ranged_weapons_end

# TROOPS
soldiers_begin			= "trp_swadian_levy"
soldiers_end			= "trp_common_hunter"

companions_begin = "trp_companion_noble_01_m"
companions_end = soldiers_begin

kingdom_1_troops_begin	= "trp_swadian_levy"
kingdom_2_troops_begin	= "trp_vaegir_levy"
kingdom_3_troops_begin	= "trp_khergit_levy"
kingdom_4_troops_begin	= "trp_nord_levy"
kingdom_5_troops_begin	= "trp_rhodok_levy"
kingdom_6_troops_begin	= "trp_sarranid_levy"

mercenaries_begin		= "trp_mercenary_footman"
factional_mercenaries_begin = "trp_swadian_mercenary_cavalry"

bandits_begin			= "trp_bandit_forest_bandit"

kingdom_1_troops_end	= kingdom_2_troops_begin
kingdom_2_troops_end	= kingdom_3_troops_begin
kingdom_3_troops_end	= kingdom_4_troops_begin
kingdom_4_troops_end	= kingdom_5_troops_begin
kingdom_5_troops_end	= kingdom_6_troops_begin
kingdom_6_troops_end	= mercenaries_begin

mercenaries_end			= bandits_begin

bandits_end				= soldiers_end

ressource_gathering_pace = 200

lords_begin = "trp_lord_001"
lords_end = companions_begin

# SCENES
castle_scene_begin = "scn_castle_plain_01_outside"
castle_scene_end = "scn_meeting_scene_steppe"

castle_scene_plain_begin = "scn_castle_plain_01_outside"
castle_scene_plain_wood_begin = "scn_castle_plain_wood_01_outside"
castle_scene_plain_dark_begin = "scn_castle_plain_dark_01_outside"
castle_scene_steppe_begin = "scn_castle_steppe_01_outside"
castle_scene_steppe_wood_begin = "scn_castle_steppe_01_outside"
castle_scene_snow_begin = "scn_castle_snow_01_outside"
castle_scene_snow_wood_begin = "scn_castle_snow_01_outside"
castle_scene_desert_begin = "scn_castle_desert_01_outside"
castle_scene_desert_wood_begin = castle_scene_end

castle_scene_plain_end = castle_scene_plain_wood_begin
castle_scene_plain_wood_end = castle_scene_plain_dark_begin
castle_scene_plain_dark_end = castle_scene_steppe_begin
castle_scene_steppe_end = castle_scene_steppe_wood_begin
castle_scene_steppe_wood_end = castle_scene_snow_begin
castle_scene_snow_end = castle_scene_snow_wood_begin
castle_scene_snow_wood_end = castle_scene_desert_begin
castle_scene_desert_end = castle_scene_desert_wood_begin
castle_scene_desert_wood_end = castle_scene_end


# OTHER
garrison_size_town = 400
garrison_size_castle = 250
garrison_size_village = 50
garrison_size_fort = 50

base_party_size_rank_0 = 10
base_party_size_rank_1 = 15
base_party_size_rank_2 = 40
base_party_size_rank_3 = 55
base_party_size_rank_4 = 100
base_party_size_rank_5 = 150
base_party_size_rank_6 = 200
base_party_size_rank_7 = 200

siege_attack_spawn_begin = 2
siege_defend_points_begin = 10
siege_archer_points_begin = 20

rank_king = 7
rank_marshall = 6
rank_city = 5
rank_castle = 4
rank_two_village = 3
rank_village = 2
rank_affiliated = 1
rank_none = 0

tai_beseiging_center = 1
tai_patroling_center = 2
tai_patroling_party = 3
tai_raiding_center = 4
tai_attacking_party = 5
tai_gathering_army = 6
tai_accompanying_party = 7
tai_accompanying_troop = 8
tai_traveling_to_party = 9
tai_traveling_to_point = 10
tai_attacking_center = 11

names_begin = "str_swadian_name_1"
names_end = "str_names_end"

swadian_names_begin = names_begin
vaegir_names_begin = "str_vaegir_name_1"
khergit_names_begin = "str_khergit_name_1"
nordic_names_begin = "str_nordic_name_1"
rhodok_names_begin = "str_rhodok_name_1"
sarranid_names_begin = "str_sarranid_name_1"

swadian_names_end = vaegir_names_begin
vaegir_names_end = khergit_names_begin
khergit_names_end = nordic_names_begin
nordic_names_end = rhodok_names_begin
rhodok_names_end = sarranid_names_begin
sarranid_names_end = names_end

relation_war = -50
relation_bad = -10
relation_neutral = 0
relation_friendly = 10
relation_economic = 20
relation_defensive = 35
relation_allies = 50

center_buildings_begin = "itm_building_hunter_camp"
center_buildings_end = "itm_buildings_end"

center_village_buildings_begin = center_buildings_begin
center_village_buildings_end = "itm_building_barrack_2"
center_castle_buildings_begin = "itm_building_militia_camp"
center_castle_buildings_end = "itm_building_university"
center_town_buildings_begin = "itm_building_slaver"
center_town_buildings_end = center_buildings_end

text_color_impossible = 0xc01010
text_color_gold = 0x55eeee
text_color_valid = 0x00ee55

era_minimum_duration = 1

merchants_begin = "trp_merchant_town_11_general"
merchants_end = "trp_banner_background_color_array"

merchants_general_begin = merchants_begin
merchants_general_end = "trp_merchant_town_11_weapons"
merchants_weapons_begin = merchants_general_end
merchants_weapons_end = "trp_merchant_town_11_armors"
merchants_armors_begin = merchants_weapons_end
merchants_armors_end = "trp_merchant_castle_1a_smith"
merchants_smiths_begin = merchants_armors_end
merchants_smiths_end = merchants_end
# merchants_smiths_end = "trp_merchant_town_11_horse"
# merchants_horses_begin = merchants_smiths_end
# merchants_horses_end = "trp_merchant_town_11_goods"
# merchants_goods_begin = merchants_horses_end
# merchants_goods_end = merchants_end

items_good = 0x1
items_weapon = 0x2
items_armor = 0x4
items_horse = 0x8

merchant_base_gold_earn_weaponsmith = 500
merchant_base_gold_earn_armorsmith = 600
merchant_base_gold_earn_goods = 400
merchant_base_gold_earn_horses = 650
merchant_base_gold_earn_general = 350

<<<<<<< HEAD
train_levies_cost = 25
=======
train_levies_cost = 40
>>>>>>> origin/master

merchants_update_rate = 7*24

reinforcement_range = 8
<<<<<<< HEAD

starting_year = 733

archer_score_shield_malus = 60
=======
>>>>>>> origin/master

##################
## Achievements ##
##################

#NORMAL ACHIEVEMENTS
ACHIEVEMENT_NONE_SHALL_PASS = 1,
ACHIEVEMENT_MAN_EATER = 2,
ACHIEVEMENT_THE_HOLY_HAND_GRENADE = 3,
ACHIEVEMENT_LOOK_AT_THE_BONES = 4,
ACHIEVEMENT_KHAAAN = 5,
ACHIEVEMENT_GET_UP_STAND_UP = 6,
ACHIEVEMENT_BARON_GOT_BACK = 7,
ACHIEVEMENT_BEST_SERVED_COLD = 8,
ACHIEVEMENT_TRICK_SHOT = 9,
ACHIEVEMENT_GAMBIT = 10,
ACHIEVEMENT_OLD_SCHOOL_SNIPER = 11,
ACHIEVEMENT_CALRADIAN_ARMY_KNIFE = 12,
ACHIEVEMENT_MOUNTAIN_BLADE = 13,
ACHIEVEMENT_HOLY_DIVER = 14,
ACHIEVEMENT_FORCE_OF_NATURE = 15,

#SKILL RELATED ACHIEVEMENTS:
ACHIEVEMENT_BRING_OUT_YOUR_DEAD = 16,
ACHIEVEMENT_MIGHT_MAKES_RIGHT = 17,
ACHIEVEMENT_COMMUNITY_SERVICE = 18,
ACHIEVEMENT_AGILE_WARRIOR = 19,
ACHIEVEMENT_MELEE_MASTER = 20,
ACHIEVEMENT_DEXTEROUS_DASTARD = 21,
ACHIEVEMENT_MIND_ON_THE_MONEY = 22,
ACHIEVEMENT_ART_OF_WAR = 23,
ACHIEVEMENT_THE_RANGER = 24,
ACHIEVEMENT_TROJAN_BUNNY_MAKER = 25,

#MAP RELATED ACHIEVEMENTS:
ACHIEVEMENT_MIGRATING_COCONUTS = 26,
ACHIEVEMENT_HELP_HELP_IM_BEING_REPRESSED = 27,
ACHIEVEMENT_SARRANIDIAN_NIGHTS = 28,
ACHIEVEMENT_OLD_DIRTY_SCOUNDREL = 29,
ACHIEVEMENT_THE_BANDIT = 30,
ACHIEVEMENT_GOT_MILK = 31,
ACHIEVEMENT_SOLD_INTO_SLAVERY = 32,
ACHIEVEMENT_MEDIEVAL_TIMES = 33,
ACHIEVEMENT_GOOD_SAMARITAN = 34,
ACHIEVEMENT_MORALE_LEADER = 35,
ACHIEVEMENT_ABUNDANT_FEAST = 36,
ACHIEVEMENT_BOOK_WORM = 37,
ACHIEVEMENT_ROMANTIC_WARRIOR = 38,

#POLITICALLY ORIENTED ACHIEVEMENTS:
ACHIEVEMENT_HAPPILY_EVER_AFTER = 39,
ACHIEVEMENT_HEART_BREAKER = 40,
ACHIEVEMENT_AUTONOMOUS_COLLECTIVE = 41,
ACHIEVEMENT_I_DUB_THEE = 42,
ACHIEVEMENT_SASSY = 43,
ACHIEVEMENT_THE_GOLDEN_THRONE = 44,
ACHIEVEMENT_KNIGHTS_OF_THE_ROUND = 45,
ACHIEVEMENT_TALKING_HELPS = 46,
ACHIEVEMENT_KINGMAKER = 47,
ACHIEVEMENT_PUGNACIOUS_D = 48,
ACHIEVEMENT_GOLD_FARMER = 49,
ACHIEVEMENT_ROYALITY_PAYMENT = 50,
ACHIEVEMENT_MEDIEVAL_EMLAK = 51,
ACHIEVEMENT_CALRADIAN_TEA_PARTY = 52,
ACHIEVEMENT_MANIFEST_DESTINY = 53,
ACHIEVEMENT_CONCILIO_CALRADI = 54,
ACHIEVEMENT_VICTUM_SEQUENS = 55,

#MULTIPLAYER ACHIEVEMENTS:
ACHIEVEMENT_THIS_IS_OUR_LAND = 56,
ACHIEVEMENT_SPOIL_THE_CHARGE = 57,
ACHIEVEMENT_HARASSING_HORSEMAN = 58,
ACHIEVEMENT_THROWING_STAR = 59,
ACHIEVEMENT_SHISH_KEBAB = 60,
ACHIEVEMENT_RUIN_THE_RAID = 61,
ACHIEVEMENT_LAST_MAN_STANDING = 62,
ACHIEVEMENT_EVERY_BREATH_YOU_TAKE = 63,
ACHIEVEMENT_CHOPPY_CHOP_CHOP = 64,
ACHIEVEMENT_MACE_IN_YER_FACE = 65,
ACHIEVEMENT_THE_HUSCARL = 66,
ACHIEVEMENT_GLORIOUS_MOTHER_FACTION = 67,
ACHIEVEMENT_ELITE_WARRIOR = 68,

#COMBINED ACHIEVEMENTS
ACHIEVEMENT_SON_OF_ODIN = 69,
ACHIEVEMENT_KING_ARTHUR = 70,
ACHIEVEMENT_KASSAI_MASTER = 71,
ACHIEVEMENT_IRON_BEAR = 72,
ACHIEVEMENT_LEGENDARY_RASTAM = 73,
ACHIEVEMENT_SVAROG_THE_MIGHTY = 74,
