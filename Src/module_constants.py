from ID_items import *
from ID_quests import *
from ID_factions import *
from ID_meshes import *
from ID_strings import *



###############
## Constants ##
###############

debug_simple = 0x01 				# Displays basic debug informations (the game should still be playable with this on)
debug_economy = 0x02 				# Displays economic informations only (productions, population, wealth)
debug_ai = 0x04 					# Displays informations about party ais
debug_faction = 0x08 				# Displays informations about factions (politics)
debug_war = debug_ai|debug_faction 	# Activates both faction and ai
debug_trade = 0x10 					# Displays informations about trading
debug_current = 0x20 				# Displays informations about the current feature being worked on (temporary debug state)
debug_all = 0xFF 					# Displays every debug line available (most likely spams the screen)

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
bandit_factions_begin = fac_faction_1
bandit_factions_end = fac_kingdom_1

kingdoms_begin = fac_kingdom_1
kingdoms_end = fac_kingdoms_end

small_kingdoms_begin = fac_small_kingdom_11
small_kingdoms_end = kingdoms_end

cultures_begin = fac_culture_1
cultures_end = fac_cultures_end

# ITEMS
goods_begin = itm_spice
goods_end = itm_saddle_horse

recipes_begin = itm_recipe_wool
recipes_end = itm_recipes_end

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
soldiers_end			= "trp_common_hunter_bow"

companions_begin = "trp_companion_noble_01_m"
companions_end = soldiers_begin

kingdom_1_troops_begin	= "trp_swadian_levy"
kingdom_2_troops_begin	= "trp_vaegir_levy"
kingdom_3_troops_begin	= "trp_khergit_levy"
kingdom_4_troops_begin	= "trp_nord_levy"
kingdom_5_troops_begin	= "trp_rhodok_levy_spearman"
kingdom_6_troops_begin	= "trp_sarranid_levy"

mercenaries_begin		= "trp_mercenary_levy_infantry"
factional_mercenaries_begin = "trp_swadian_rider"

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

npc_heroes_begin = "trp_current_player"
npc_heroes_end = companions_end

# SCENES
castle_scene_begin = "scn_castle_plain_01_outside"
castle_scene_end = "scn_meeting_scene_steppe"

castle_scene_plain_begin = "scn_castle_plain_01_outside"
castle_scene_plain_wood_begin = "scn_castle_plain_wood_01_outside"
castle_scene_plain_dark_begin = "scn_castle_plain_dark_01_outside"
castle_scene_forest_begin = "scn_castle_steppe_01_outside" # "scn_castle_forest_01_outside"
castle_scene_forest_wood_begin = "scn_castle_steppe_01_outside" # "scn_castle_forest_wood_01_outside"
castle_scene_forest_dark_begin = "scn_castle_steppe_01_outside" # "scn_castle_forest_dark_01_outside"
castle_scene_sea_begin = "scn_castle_steppe_01_outside" # "scn_castle_sea_01_outside"
castle_scene_sea_wood_begin = "scn_castle_steppe_01_outside" # "scn_castle_sea_wood_01_outside"
castle_scene_sea_dark_begin = "scn_castle_steppe_01_outside" # "scn_castle_sea_dark_01_outside"
castle_scene_steppe_begin = "scn_castle_steppe_01_outside"
castle_scene_steppe_wood_begin = "scn_castle_snow_01_outside" # TODO
castle_scene_steppe_forest_begin = "scn_castle_snow_01_outside" # TODO
castle_scene_steppe_forest_wood_begin = "scn_castle_snow_01_outside" # TODO
castle_scene_snow_begin = "scn_castle_snow_01_outside"
castle_scene_snow_wood_begin = "scn_castle_snow_wood_01_outside"
castle_scene_snow_forest_begin = "scn_castle_desert_01_outside" # "scn_castle_snow_forest_01_outside"
castle_scene_snow_forest_wood_begin = "scn_castle_desert_01_outside" # "scn_castle_snow_forest_wood_01_outside"
castle_scene_desert_begin = "scn_castle_desert_01_outside"
castle_scene_desert_wood_begin = castle_scene_end

castle_scene_plain_end = castle_scene_plain_wood_begin
castle_scene_plain_wood_end = castle_scene_plain_dark_begin
castle_scene_plain_dark_end = castle_scene_forest_begin
castle_scene_forest_end = castle_scene_forest_wood_begin
castle_scene_forest_wood_end = castle_scene_forest_dark_begin
castle_scene_forest_dark_end = castle_scene_sea_begin
castle_scene_sea_end = castle_scene_sea_wood_begin
castle_scene_sea_wood_end = castle_scene_sea_dark_begin
castle_scene_sea_dark_end = castle_scene_steppe_begin
castle_scene_steppe_end = castle_scene_steppe_wood_begin
castle_scene_steppe_wood_end = castle_scene_steppe_forest_begin
castle_scene_steppe_forest_end = castle_scene_steppe_forest_wood_begin
castle_scene_steppe_forest_wood_end = castle_scene_snow_begin
castle_scene_snow_end = castle_scene_snow_wood_begin
castle_scene_snow_wood_end = castle_scene_snow_forest_begin
castle_scene_snow_forest_end = castle_scene_snow_forest_wood_begin
castle_scene_snow_forest_wood_end = castle_scene_desert_begin
castle_scene_desert_end = castle_scene_desert_wood_begin
castle_scene_desert_wood_end = castle_scene_end


# OTHER

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

relation_state_war = -40
relation_state_conflict = -20
relation_state_neutral = 0
relation_state_friendly = 20

relation_terrible = -80
relation_bad = -40
relation_tense = -20
relation_neutral = 0
relation_positive = 20
relation_friendly = 40
relation_excellent = 80

relation_change_factor = 20

relation_change_center_freed = 32
relation_change_vassal_freed = 8
relation_change_war_declared = relation_change_factor * -25
relation_change_joined_war = relation_change_factor * 5
relation_change_submit = relation_change_factor * -50

center_buildings_begin = "itm_building_hunter_camp"
center_buildings_end = "itm_buildings_end"

center_village_buildings_begin = center_buildings_begin
center_village_buildings_end = "itm_building_barrack_2"
center_castle_buildings_begin = "itm_building_militia_camp"
center_castle_buildings_end = "itm_building_university"
center_town_buildings_begin = "itm_building_slaver"
center_town_buildings_end = center_buildings_end

text_color_impossible = 0xc01010
text_color_gold = 0xffdd55
text_color_valid = 0x00ee55
text_color_info = 0x5555ff
text_color_capture = 0xDD2200
text_color_freed = 0x22DD00
text_color_debug = 0xCCCCCC
text_color_war = 0xBB0101
text_color_default = 0x000000
text_color_light = 0x222222
text_color_white = 0xFFFFFF

text_color_budget_positive = 0x20a020
text_color_budget_negative = 0xa02020
text_color_budget_neutral = 0x222222

era_minimum_duration = 365

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

train_levies_cost = 25

merchants_update_rate = 7*24

reinforcement_range = 8

starting_year = 733

archer_score_shield_malus = 60

war_damage_base_lord_defeated = 20
war_damage_base_lord_killed = 100

war_damage_base_village_taken = 40
war_damage_base_castle_taken = 120
war_damage_base_town_taken = 300

war_damage_raid_divider = 2
war_damage_siege_divider = 20

war_damage_inflicted_bonus_divider = 5

war_damage_natural_decline_base = 2
war_damage_natural_decline_divider = 100

war_damage_penalties_begin = 150
war_damage_penalties_offset_begin = 10

war_damage_casualties_divider = 1 # Each set of casualties generates a single point of war damage

faction_size_names_begin = str_swadian_faction_small
faction_size_names_end = str_sarranid_faction_large + 1
faction_size_names_count = 3

outcome_success = 1
outcome_neutral = 0
outcome_failure = -1

bargain_type_strength = -1
bargain_type_cunning = 1

escape_type_wits = 1
escape_type_agility = 2
escape_type_strength = 3

process_mission_iteration_count = 5

type_critical = 3
type_moderate = 2
type_slight = 1
type_none = 0

caravan_max_cargo_size = 60

caravan_score_distance_ratio = 3
caravan_score_resource_production_ratio = 500
caravan_score_resource_amount_ratio = 10
caravan_score_war_penatly = 100

caravan_score_type_selling = 1
caravan_score_type_buying = 2
caravan_score_type_all = 0

political_event_relation_change = 1
political_event_war_declared = 2
political_event_treaty_signed = 3
political_event_center_captured = 4
political_event_center_looted = 5
political_event_center_freed = 6
political_event_vassal_captured = 7
political_event_vassal_freed = 8
political_event_helped = 9
political_event_fulfil_treaty = 10
political_event_break_treaty = 11
political_event_war_party_defeated = 12
political_event_caravan_defeated = 13

political_event_helped_join_defensive_war = 14
political_event_helped_join_offensive_war = 15

center_size_village = 1
center_size_castle = 3
center_size_town = 10

party_size_leader = 12
party_size_town = 10
party_size_castle = 6
party_size_village = 2
party_size_none = 1

attitude_negative = -1
attitude_neutral = 0
attitude_positive = 1

relation_weight_faction = 1
relation_weight_leader = 1

max_bandit_party = 75

prisoner_escape_chance = 1
prisoner_ransom_chance = 25

base_hero_value_king = 10000000
base_hero_value_city = 5000000
base_hero_value_castle = 2000000
base_hero_value_village = 500000
base_hero_value_two_village = base_hero_value_village * 150 / 100
base_hero_value_none = 100000

base_hero_value_vassals_percentage = 15
base_hero_value_renown_multiplier = 10

faction_wealth_shared_ratio = 3
faction_wealth_shared_min = 10 # minimum amount of wealth shared per lord in the faction
faction_wealth_fiefless_share_multiplier = 10

faction_tax_rate_funds_min = 0
faction_tax_rate_funds_base = 2
faction_tax_rate_funds_max_peace = 25
faction_tax_rate_funds_max_war = 10
faction_tax_rate_member_base = 2
faction_tax_rate_vassal_base = 5

quests_begin = "qst_swear_vassalage_fief"
quests_end = "qst_quests_end"

quest_descriptions_begin = "str_quest_description_swear_vassalage_fief"
quest_descriptions_end = "qst_quest_description_end"

vassal_outcome_too_many = 1
vassal_outcome_unknown = 2
vassal_outcome_refused = 3
vassal_outcome_no_fief = 4
vassal_outcome_accepted = 5

goods_ratio_production_village = 50
goods_ratio_transformation_village = 20

goods_ratio_production_castle = 33
goods_ratio_transformation_castle = 20

goods_ratio_production_town = 10
goods_ratio_transformation_town = 10

################
## Item Slots ##
################

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

item_slots = 0

slot_building_cost_wood		= 1
slot_building_cost_stone	= slot_building_cost_wood + 1
slot_building_cost_gold		= slot_building_cost_stone + 1
slot_building_build_time	= slot_building_cost_gold + 1

slot_recipe_required_item = slot_building_build_time + 1
slot_recipe_required_item_quantity = slot_recipe_required_item + 1
slot_recipe_workload = slot_recipe_required_item_quantity + 1
slot_recipe_produced_item = slot_recipe_workload + 1
slot_recipe_produced_item_quantity = slot_recipe_produced_item + 1
slot_recipe_consume = slot_recipe_produced_item_quantity + 1
slot_recipe_produced_item_max_ratio = slot_recipe_consume + 1

slot_item_perish_ratio = slot_recipe_produced_item_max_ratio + 1

# Amount of items consumed per 1000000 pop
slot_item_consumption_weight_serf = slot_item_perish_ratio + 1
slot_item_consumption_weight_artisan = slot_item_consumption_weight_serf + 1
slot_item_consumption_weight_noble = slot_item_consumption_weight_artisan + 1
slot_item_consumption_weight_slave = slot_item_consumption_weight_noble + 1
slot_item_consumption_quality = slot_item_consumption_weight_slave + 1

# Category represent groups of goods that can be substituted
slot_item_consumption_category = slot_item_consumption_quality + 1

icc_food = 1
icc_drink = 2
icc_clothes = 3

consumption_ratio_base = 1000000

#################
## Agent Slots ##
#################

agent_slots = 0

slot_agent_new_division = 1

slot_agent_is_in_scripted_mode	= 2
slot_agent_target_entry_point	= 3
slot_agent_is_reinforcement	= 4

slot_agent_charge = 5

slot_agent_bodyguard_1 = 6
slot_agent_bodyguard_2 = 7
slot_agent_guarding = 6

slot_agent_bodyguard_troop_1 = 8
slot_agent_bodyguard_troop_2 = 9

slot_agent_forced_defend = 10

slot_agent_morale = 11
slot_agent_morale_modifier = 12 # Used to keep track of current morale
    
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
slot_faction_lady_name_begin		= 17

slot_faction_troops_begin			= 18
slot_faction_troops_end				= 19

# slot_faction_base_reinforcements	= 13

slot_faction_peasant_begin			= slot_faction_troops_begin
slot_faction_common_begin			= 20
slot_faction_veteran_begin			= 21
slot_faction_elite_begin			= 22
slot_faction_noble_begin			= 23

slot_faction_caravan_master			= 24
slot_faction_caravan_guard			= 25

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

slot_faction_original_color = slot_faction_noble_template_end + 1

slot_faction_is_at_war = slot_faction_original_color + 1

slot_faction_lord_gathering = slot_faction_is_at_war + 1

slot_faction_master_culture = slot_faction_lord_gathering + 1

# slot_faction_troop_ratio_begin = slot_faction_troop_ratio_infantry

slot_faction_era = slot_faction_master_culture + 1	# Current era the faction is at
slot_faction_era_time = slot_faction_era + 1		# Time at which the faction has attained this era

slot_faction_num_vassals = slot_faction_era_time + 1
slot_faction_num_vassals_active = slot_faction_num_vassals + 1
slot_faction_num_fiefs = slot_faction_num_vassals_active + 1
slot_faction_num_walled_fiefs = slot_faction_num_fiefs + 1

slot_faction_strength_active = slot_faction_num_walled_fiefs + 1
slot_faction_strength_ready = slot_faction_strength_active + 1

slot_faction_strength_defensive_allies = slot_faction_strength_ready + 1
slot_faction_strength_offensive_allies = slot_faction_strength_defensive_allies + 1

slot_faction_war_damage = slot_faction_strength_offensive_allies + 1

slot_faction_safety = slot_faction_war_damage + 1

# Last time the faction was at peace
slot_faction_last_peace = slot_faction_safety + 1

slot_faction_preparing_war = slot_faction_last_peace + 1

slot_faction_size = slot_faction_preparing_war + 1
slot_faction_size_category = slot_faction_size + 1
sfs_small = 0
sfs_medium = 1
sfs_large = 2


# slots used for faction focus in ai decision
slot_faction_mission_focus_1 = slot_faction_size_category + 1
slot_faction_mission_focus_2 = slot_faction_mission_focus_1 + 1
slot_faction_mission_focus_3 = slot_faction_mission_focus_2 + 1
slot_faction_mission_focus_4 = slot_faction_mission_focus_3 + 1
slot_faction_mission_focus_5 = slot_faction_mission_focus_4 + 1
slot_faction_mission_focus_6 = slot_faction_mission_focus_5 + 1
slot_faction_mission_focus_7 = slot_faction_mission_focus_6 + 1
slot_faction_mission_focus_8 = slot_faction_mission_focus_7 + 1
slot_faction_mission_focus_9 = slot_faction_mission_focus_8 + 1
slot_faction_mission_focus_10 = slot_faction_mission_focus_9 + 1
slot_faction_mission_focus_11 = slot_faction_mission_focus_10 + 1
slot_faction_mission_focus_12 = slot_faction_mission_focus_11 + 1
slot_faction_mission_focus_13 = slot_faction_mission_focus_12 + 1
slot_faction_mission_focus_14 = slot_faction_mission_focus_13 + 1
slot_faction_mission_focus_15 = slot_faction_mission_focus_14 + 1
slot_faction_mission_focus_16 = slot_faction_mission_focus_15 + 1
slot_faction_mission_focus_17 = slot_faction_mission_focus_16 + 1
slot_faction_mission_focus_18 = slot_faction_mission_focus_17 + 1
slot_faction_mission_focus_19 = slot_faction_mission_focus_18 + 1
slot_faction_mission_focus_20 = slot_faction_mission_focus_19 + 1

slot_faction_vassal_tax_rate = slot_faction_mission_focus_20 + 1
slot_faction_member_tax_rate = slot_faction_vassal_tax_rate + 1
slot_faction_funds_tax_rate = slot_faction_member_tax_rate + 1

slot_faction_status = slot_faction_funds_tax_rate + 1
sfst_default = 1
sfst_disabled = -1

slot_faction_policy_assimilation = slot_faction_status + 1

# Assimilation is forced on captured centers
sfpa_total = 0
# Assimilation is forced on captured centers only if culture is different
sfpa_partial = 1
# No assimilation on captured centers
sfpa_none = 2

slot_faction_vassal_type = slot_faction_policy_assimilation + 1

# Vassal treaties
sfvt_none = 0x00 # not a vassal
sfvt_tributary = 0x01 # pays tribute
sfvt_vassal = 0x02 # foreign policy is limited
sfvt_sattrapy = 0x10 # joins offensive wars of overlord
sfvt_bulwark = 0x40 # joins defensive wars of overlord
sfvt_protectorate = 0x80 # joins defensive wars of vassal

sfvt_default_vassal_type = sfvt_tributary | sfvt_vassal | sfvt_sattrapy | sfvt_bulwark | sfvt_protectorate

slot_faction_battle_casualties = slot_faction_vassal_type + 1

slot_faction_name_holder = slot_faction_battle_casualties + 1
slot_faction_has_fixed_name = slot_faction_name_holder + 1

slot_faction_kingdom_relation_begin = slot_faction_has_fixed_name + 1
slot_faction_kingdom_relation_end = slot_faction_kingdom_relation_begin - kingdoms_begin + kingdoms_end

slot_faction_kingdom_treaties_begin = slot_faction_kingdom_relation_end
slot_faction_kingdom_treaties_end = slot_faction_kingdom_treaties_begin - kingdoms_begin + kingdoms_end

slot_faction_kingdom_temporary_treaties_begin = slot_faction_kingdom_treaties_end
slot_faction_kingdom_temporary_treaties_end = slot_faction_kingdom_temporary_treaties_begin - kingdoms_begin + kingdoms_end

slot_faction_kingdom_temporary_treaties_duration_begin = slot_faction_kingdom_temporary_treaties_end
slot_faction_kingdom_temporary_treaties_duration_end = slot_faction_kingdom_temporary_treaties_duration_begin - kingdoms_begin + kingdoms_end

slot_faction_kingdom_temporary_treaties_object_begin = slot_faction_kingdom_temporary_treaties_duration_end
slot_faction_kingdom_temporary_treaties_object_end = slot_faction_kingdom_temporary_treaties_object_begin - kingdoms_begin + kingdoms_end

sfkt_none = 0x0000

sfkt_none_treaty_clear = 0xFFFF

# Military treaties
sfkt_truce = 0x0001
sfkt_non_agression = 0x0002
sfkt_defensive_alliance = 0x0004
sfkt_alliance = 0x0008

sfkt_military_treaty_mask = 0x000F
sfkt_military_treaty_clear = 0xFFF0

# Economic treaties
sfkt_open_trade = 0x0010
sfkt_trade_preference = 0x0020
sfkt_trade_exclusivity = 0x0040

sfkt_economic_treaty_clear = 0xFF0F

# Temporary treaties
sfkt_tribute = 0x0100

# Vassal treaties
sfkt_vassal = 0x1000 	# represents being a vassal of targeted faction
sfkt_overlord = 0x2000 	# represents being the overlord of targeted faction

sfkt_vassal_treaty_clear = 0x00FF
sfkt_tribute_treaty_clear = 0xF0FF

sfkt_all_treaty_clear = 0x0000

sfkt_defensive_mask = sfkt_defensive_alliance|sfkt_alliance|sfkt_vassal|sfkt_overlord

# For reference distance between:
#   Suno - Burglen: 30
#	Sargoth - Praven: 95
# 	Shariz - Praven: 174
slot_faction_kingdom_distance_begin = slot_faction_kingdom_temporary_treaties_object_end
slot_faction_kingdom_distance_end = slot_faction_kingdom_distance_begin - kingdoms_begin + kingdoms_end

# slot_faction_kingdom_treaty_expiration_begin = slot_faction_kingdom_distance_end
# slot_faction_kingdom_treaty_expiration_end = slot_faction_kingdom_treaty_expiration_begin - kingdoms_begin + kingdoms_end

faction_distance_close = 25
faction_distance_far = 100

slot_faction_wealth = slot_faction_kingdom_distance_end + 1
slot_faction_accumulated_taxes = slot_faction_wealth + 1
slot_faction_last_share_amount = slot_faction_accumulated_taxes + 1

slot_faction_budget_tribute = slot_faction_last_share_amount + 1
slot_faction_budget_tribute_payment = slot_faction_budget_tribute + 1
slot_faction_budget_funds = slot_faction_budget_tribute_payment + 1
slot_faction_budget_funds_payment = slot_faction_budget_funds + 1

slot_faction_wealth_shared_ratio = slot_faction_budget_funds_payment + 1

slot_faction_tmp = slot_faction_wealth_shared_ratio + 1

#######################
## War Storage Slots ##
## ####################

war_storages_begin = "fac_war_storage_1"
war_storages_end = "fac_war_storage_end"


slot_war_active = 9
slot_war_ended = slot_war_active + 1
slot_war_start_date = slot_war_ended + 1

slot_war_defender_strength = slot_war_start_date + 1
slot_war_attacker_strength = slot_war_defender_strength + 1

slot_war_defender_willingness_score = slot_war_attacker_strength + 1
slot_war_attacker_willingness_score = slot_war_defender_willingness_score + 1

slot_war_kingdom_participant_begin = slot_war_attacker_willingness_score + 1
slot_war_kingdom_participant_end = slot_war_kingdom_participant_begin - kingdoms_begin + kingdoms_end

swkp_main_defender = -2
swkp_defender = -1
swkp_bystander = 0
swkp_aggressor = 1
swkp_main_aggressor = 2

slot_war_kingdom_willingness_begin = slot_war_kingdom_participant_end
slot_war_kingdom_willingness_end = slot_war_kingdom_willingness_begin - kingdoms_begin + kingdoms_end

kw_desperate = -2
kw_failling = -1
kw_neutral = 0
kw_eager = 1

proposal_peace_base_score = 0
proposal_peace_score_village_captured = 10
proposal_peace_score_castle_captured = 100
proposal_peace_score_town_captured = 300

num_peace_proposal = 20
wppt_transfer_center = 1
wppt_liberate_center = 2
wppt_tribute = 3
wppt_liberate_prisoners_common = 4
wppt_liberate_prisoners_heroes = 5
wppt_vassalize = 6

slot_war_peace_proposal_object_begin = slot_war_kingdom_willingness_end + 1
slot_war_peace_proposal_object_end = slot_war_peace_proposal_object_begin + num_peace_proposal
slot_war_peace_proposal_type_begin = slot_war_peace_proposal_object_end + 1
slot_war_peace_proposal_type_end = slot_war_peace_proposal_type_begin + num_peace_proposal
slot_war_peace_proposal_target_begin = slot_war_peace_proposal_type_end + 1
slot_war_peace_proposal_target_end = slot_war_peace_proposal_target_begin + num_peace_proposal
slot_war_peace_proposal_value_begin = slot_war_peace_proposal_target_end + 1
slot_war_peace_proposal_value_end = slot_war_peace_proposal_value_begin + num_peace_proposal

# slot_war_kingdom_participation_score_begin = slot_war_kingdom_willingness_end
# slot_war_kingdom_participation_score_end = slot_war_kingdom_participation_score_begin - kingdoms_begin + kingdoms_end

### Slots included between these two will be reset to 0 when the war storage is reset
slot_war_clear_slots_begin = slot_war_active
slot_war_clear_slots_end = slot_war_peace_proposal_type_end
###


#################
## Party Slots ##
#################

party_slots = 0

slot_party_type				= 1

spt_civilian	= 5
spt_bandit		= 6
spt_caravan		= 7
spt_patrol		= 8
spt_scout		= 9
spt_convoy		= 10
spt_war_party	= 11

spt_village		= 12
spt_castle		= 13
spt_town		= 14
spt_fort		= 15

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
spm_waiting		= 6

slot_party_mission_object	= 6

slot_party_wealth 			= 7
slot_party_population 		= 8   # Does not include slave population
slot_party_population_noble = 9
slot_party_population_artisan = 10
slot_party_population_slave = 11

population_max_town = 34000
population_max_castle = 8500
population_max_village = 12000
slot_party_population_max 	= 12

population_growth_castle_noble = 8
population_growth_castle_artisan = 24
population_growth_castle_serf = 68
population_growth_castle_slave = 0

population_growth_town_noble = 8
population_growth_town_artisan = 30
population_growth_town_serf = 62
population_growth_town_slave = 0

population_growth_village_noble = 1
population_growth_village_artisan = 4
population_growth_village_serf = 95
population_growth_village_slave = 0

taxes_noble_amount = 20
taxes_artisan_amount = 5
taxes_serf_amount = 2

slot_party_wanted_party_wages = 13
slot_party_accumulated_taxes = 14

slot_party_wages_cache = 15 # Used to get non accurate wages

slot_party_ressource_radius = 16

slot_party_total_resources = 17

slot_party_ressources_begin = itm_spice # 18
slot_party_ressources_end = itm_saddle_horse # 66
slot_party_ressources_count = slot_party_ressources_end - slot_party_ressources_begin # 48

slot_party_ressources_current_amount_begin = slot_party_ressources_end # 65
slot_party_ressources_current_amount_end = slot_party_ressources_current_amount_begin + slot_party_ressources_count # 113

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

slot_party_linked_party = 126

slot_party_faction = 127

# Taxes are a way for land owners to earn money
# It is possible to customise what your citizens are taxed on
# Imposing a fixed taxation will decrease population growth as poorer people are the most affected
# Imposing taxes on buying and selling will have generaly low impoact on the popultation (as long as they are not too high and balanced) but will impact trade
# Taxing on property will have an impact on your reputation
# Taxing on wealth will have an impact on nobility
# Taxing visitors may decrease their numbers (does not tax official traders)
# Having a good balance on taxes will yeild the best results
# Having low taxes will be generaly liked by the population but may not offset the loss in money
# Abrupt changes in taxes may greatly change the mood of the population, keep changes low if you want the population under control (unless when decreasing taxes)
slot_party_taxes_sell		= 128 # Taxes paid upon buying inside the center
slot_party_taxes_buy		= 129 # Taxes paid upon selling inside the center
slot_party_taxes_property	= 130 # Taxes paid on owning property
slot_party_taxes_fixed		= 131 # Fixed taxes paid by everyone
slot_party_taxes_wealth		= 132 # Taxes paid upon earning money inside the city (also applied to buying and selling)
slot_party_taxes_visit		= 133 # Taxes paid upon entering the city (not paid by residents)

default_fixed_tax_rate_village = 20
default_fixed_tax_rate_castle = 40
default_fixed_tax_rate_town = 20

default_buy_tax_rate_village = 20
default_buy_tax_rate_castle = 28
default_buy_tax_rate_town = 40

default_sell_tax_rate_village = 8
default_sell_tax_rate_castle = 16
default_sell_tax_rate_town = 12

slot_party_speak_allowed = 134

slot_party_notes = 135
pn_unknown	= 0x00
pn_know_faction = 0x01
pn_know_original= 0x02
pn_know_lord	= 0x04
pn_know_linked	= 0x08
pn_know_wealth	= 0x10
pn_know_population = 0x20
pn_know_tax		= 0x40
pn_know_slaves	= 0x80
# pn_know_

slot_party_morale = 136

slot_party_taxes = 137
slot_party_prosperity = 138

slot_party_unpaid_wages = 139

slot_party_temp = 140

slot_party_origin_center = 141

slot_party_preparing_for_war = 142
slot_party_prepared_for_war = 143

slot_party_process_mission_iteration = 144

# slot_party_num_peasants		= 146
# slot_party_num_caravans		= 147
# slot_party_num_patrols		= 148
# slot_party_num_scouts		= 149
# slot_party_num_others 		= 150 # Contains every other non fighting party


slot_party_recent_casualties_loot = 151 # Contains gold looted during simulated battle

slot_party_budget_last_wealth = 152

slot_party_budget_taxes = slot_party_budget_last_wealth + 1
slot_party_budget_protection_taxes = slot_party_budget_taxes + 1
slot_party_budget_pay_protection_taxes = slot_party_budget_protection_taxes + 1
slot_party_budget_vassal_taxes = slot_party_budget_pay_protection_taxes + 1
slot_party_budget_pay_vassal_taxes = slot_party_budget_vassal_taxes + 1
slot_party_budget_faction_member_taxes = slot_party_budget_pay_vassal_taxes + 1
slot_party_budget_pay_faction_member_taxes = slot_party_budget_faction_member_taxes + 1
slot_party_budget_trade = slot_party_budget_pay_faction_member_taxes + 1
slot_party_budget_visitor = slot_party_budget_trade + 1
slot_party_budget_funds = slot_party_budget_visitor + 1
slot_party_budget_pay_funds = slot_party_budget_funds + 1
slot_party_budget_tribute = slot_party_budget_pay_funds + 1
slot_party_budget_pay_tribute = slot_party_budget_tribute + 1
slot_party_budget_occupation = slot_party_budget_pay_tribute + 1
slot_party_budget_pay_occupation = slot_party_budget_occupation + 1
slot_party_budget_debts = slot_party_budget_pay_occupation + 1
slot_party_budget_expenses = slot_party_budget_debts + 1
slot_party_budget_late_wages = slot_party_budget_expenses + 1
slot_party_budget_wages = slot_party_budget_late_wages + 1
slot_party_budget_private_expenses = slot_party_budget_wages + 1
slot_party_budget_troops_hiring = slot_party_budget_private_expenses + 1
slot_party_budget_troops_buying = slot_party_budget_troops_hiring + 1
slot_party_budget_troops_selling = slot_party_budget_troops_hiring + 1

tax_type_none = -1
tax_type_population = 0
tax_type_protection = 1
tax_type_protection_pay = 2
tax_type_vassal = 3
tax_type_vassal_pay = 4
tax_type_member = 5
tax_type_member_pay = 6
tax_type_trade = 7
tax_type_visitor = 8
tax_type_funds = 9
tax_type_funds_pay = 10
tax_type_tribute = 11
tax_type_tribute_pay = 12
tax_type_occupation = 13
tax_type_occupation_pay = 14
tax_type_debts = 15
tax_type_expenses = 16
tax_type_late_wages = 17
tax_type_wages = 18
tax_type_private_expenses = 19
tax_type_troops_hiring = 20
tax_type_troops_buying = 21
tax_type_troops_selling = 22

slot_party_buget_taxes_begin = slot_party_budget_taxes
slot_party_buget_taxes_end = slot_party_budget_troops_selling + 1

slot_party_budget_reserved_party = slot_party_buget_taxes_end
slot_party_budget_reserved_auxiliaries = slot_party_budget_reserved_party + 1
slot_party_budget_reserved_expenses = slot_party_budget_reserved_auxiliaries + 1
slot_party_budget_reserved_other = slot_party_budget_reserved_expenses + 1

slot_party_attached_party_1 = slot_party_budget_reserved_other + 1
slot_party_attached_party_2 = slot_party_attached_party_1 + 1
slot_party_attached_party_3 = slot_party_attached_party_2 + 1

slot_party_last_rest = slot_party_attached_party_3 + 1 # for small parties

slot_party_mission_target_1 = slot_party_last_rest + 1
slot_party_mission_target_2 = slot_party_mission_target_1 + 1
slot_party_mission_target_3 = slot_party_mission_target_2 + 1
slot_party_mission_objective_1 = slot_party_mission_target_3 + 1
slot_party_mission_objective_2 = slot_party_mission_objective_1 + 1
slot_party_mission_objective_3 = slot_party_mission_objective_2 + 1

slot_party_readiness = slot_party_mission_objective_3 + 1

sfsr_unavailable = 0
sfsr_ready = 0 # For now those are the same until we implement party readiness

slot_party_building_slot_1	= slot_party_readiness + 1
slot_party_building_slot_2	= slot_party_building_slot_1 + 1
slot_party_building_slot_3	= slot_party_building_slot_2 + 1
slot_party_building_slot_4	= slot_party_building_slot_3 + 1
slot_party_building_slot_5	= slot_party_building_slot_4 + 1
slot_party_building_slot_6	= slot_party_building_slot_5 + 1
slot_party_building_slot_7	= slot_party_building_slot_6 + 1
slot_party_building_slot_8	= slot_party_building_slot_7 + 1
slot_party_building_slot_9	= slot_party_building_slot_8 + 1
slot_party_building_slot_10	= slot_party_building_slot_9 + 1

slot_party_building_slot_end = slot_party_building_slot_10 + 1
num_building_slots = slot_party_building_slot_end - slot_party_building_slot_1

# Tells the current state of the building
# Some buildings only function at full stat (100)
# Negative values indicate that the building is not yet constructed or has been damaged
# No building does anything positive when state is negative
# Values between 0 and 100 are for damaged buildings or buildings just built
# During this time they function at a reduced rate
slot_party_building_state_1 = slot_party_building_slot_10 + 1
slot_party_building_state_2 = slot_party_building_state_1 + 1
slot_party_building_state_3 = slot_party_building_state_2 + 1
slot_party_building_state_4 = slot_party_building_state_3 + 1
slot_party_building_state_5 = slot_party_building_state_4 + 1
slot_party_building_state_6 = slot_party_building_state_5 + 1
slot_party_building_state_7 = slot_party_building_state_6 + 1
slot_party_building_state_8 = slot_party_building_state_7 + 1
slot_party_building_state_9 = slot_party_building_state_8 + 1
slot_party_building_state_10 = slot_party_building_state_9 + 1

slot_party_autosort_options = slot_party_building_state_10 + 1

autosort_no_sort = 0x00
autosort_low_level_first = 0x01
autosort_high_level_first = 0x02
autosort_foreign_first = 0x10
autosort_local_first = 0x20

autosort_level_flag = 0x0F
autosort_culture_flag = 0xF0
autosort_level_clearer = 0xF0
autosort_culture_clearer = 0x0F

slot_party_reserved = slot_party_autosort_options + 1

# For centers
slot_party_item_consumed_begin 	= slot_party_reserved + 1 # Number of items consumed
slot_party_item_consumed_end	= slot_party_item_consumed_begin + goods_end - goods_begin
slot_party_item_last_produced_begin 	= slot_party_item_consumed_end # Number of items produced
slot_party_item_last_produced_end	= slot_party_item_last_produced_begin + goods_end - goods_begin
# For parties (caravans)
slot_party_item_stored_price_begin 	= slot_party_item_consumed_begin
slot_party_item_stored_price_end 	= slot_party_item_consumed_end

slot_party_production_target_begin = slot_party_item_last_produced_end + 1
slot_party_production_target_end = slot_party_production_target_begin + recipes_end - recipes_begin

slot_party_override_production_target = slot_party_production_target_end + 1

slot_party_player_shakedown = slot_party_override_production_target + 1

slot_party_governor = slot_party_player_shakedown + 1

#################
## Scene Slots ##
#################

siege_attack_spawn_begin = 2
siege_defend_points_begin = 10
siege_archer_points_begin = 20

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

slot_troop_temp_array_begin			= 1

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

# Real rank is based on the number of fiefs a lord holds
# Current rank slowly changes to match real rank
slot_troop_rank 					= 7 # real rank
slot_troop_level					= 8 # current rank
slot_troop_equipement_level			= 9 # current rank

slot_troop_mercenary_captain_1		= slot_troop_level				# Only troops
slot_troop_mercenary_captain_2		= slot_troop_equipement_level	# Only troops

slot_troop_kingdom_occupation 		= 12
tko_dead = -1 	# Dead people are not the same as not living ones
				# Dead people are still shown in character notes
				# And can be mentionned in conversations
tko_none = 0
tko_kingdom_hero = 1
tko_mercenary = 2
tko_bandit = 3
tko_reserved = 4

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
slot_troop_garrisoned 				= slot_troop_leaded_party + 1

slot_troop_building_one 			= slot_troop_garrisoned + 1
slot_troop_building_end				= slot_troop_building_one + 1

slot_troop_days_next_rethink		= slot_troop_building_end + 1

slot_troop_num_vassal				= slot_troop_days_next_rethink + 1
slot_troop_vassal_of				= slot_troop_num_vassal + 1

slot_troop_home						= slot_troop_vassal_of + 1
slot_troop_current_home				= slot_troop_home + 1

slot_troop_mission 					= slot_troop_current_home + 1
tm_none					= 0
tm_defending			= 1
tm_attacking			= 2
tm_escorting			= 3

slot_troop_mission_object			= slot_troop_mission + 1

slot_troop_behavior_object 			= slot_troop_mission_object + 1
slot_troop_behavior 				= slot_troop_behavior_object + 1
tb_none 				= 0
tb_move 				= 1
tb_follow 				= 2
tb_patrol				= 3

slot_troop_prisoner_of				= slot_troop_behavior + 1 # Only heroes

slot_troop_faction_reserved_1		= slot_troop_prisoner_of # Only regulars
slot_troop_faction_reserved_2		= slot_troop_faction_reserved_1 + 1 # Only regulars
slot_troop_faction_not_1			= slot_troop_faction_reserved_2 + 1
slot_troop_faction_not_2			= slot_troop_faction_not_1 + 1
slot_troop_faction_not_3			= slot_troop_faction_not_2 + 1

slot_troop_armor_weight 			= slot_troop_faction_not_3 + 1
slot_troop_horse_weight 			= slot_troop_armor_weight + 1
slot_troop_ranged_weapon_weight 	= slot_troop_horse_weight + 1

weight_very_light = 0
weight_light = 1
weight_medium = 2
weight_heavy = 3
weight_very_heavy = 4

slot_troop_surplus_center			= 33

slot_troop_gathering				= 34

slot_troop_last_attack				= 35
slot_troop_last_rest				= 36

slot_troop_archer_score				= 37

slot_troop_mercenary_from			= 38
slot_troop_mercenary_captain 		= 39

# Handles notes
slot_troop_notes					= 40

# ToDo: add different note level
tn_unknown 					= 0x00
tn_know_main_fief			= 0x01
tn_know_fiefs				= 0x02
tn_know_faction				= 0x04
tn_know_faction_rank		= 0x08
tn_know_family_rank 		= 0x10 # Relations to an important member of the family
tn_know_family_name 		= 0x20
tn_know_family_importance	= 0x40
tn_know_family 				= tn_know_family_rank | tn_know_family_name | tn_know_family_importance
tn_know_personality 		= 0x80
tn_know_face   				= 0x100

slot_troop_married_to 			= 41
slot_troop_father				= 42
slot_troop_mother 				= 43
slot_troop_child_1 				= 44
slot_troop_child_2 				= 45
slot_troop_child_3 				= 46
slot_troop_child_4 				= 47
slot_troop_child_5 				= 48
slot_troop_child_6				= 49
slot_troop_child_7				= 50
slot_troop_child_8				= 51
slot_troop_child_9				= 52
slot_troop_child_10				= 53

slot_troop_family				= 54

slot_troop_died = 55 # Contains the date of death of an NPC

slot_troop_honor = 56
slot_troop_renown = 57

slot_troop_accompanying = 58 # Used for companions -- Stores the current party the troop is following
slot_troop_companion_of = 59 # Used for companions -- Stores the leader it is following

slot_troop_num_followers = 60 # Stores number of parties trying to follow
slot_troop_num_followers_ready = 61 # Stores number of parties currently nearby and following

slot_troop_wanted_party_wages = 62
slot_troop_accumulated_taxes = 63

slot_troop_budget_vassal_taxes = 64
slot_troop_budget_faction_member_taxes = 65
slot_troop_budget_faction_funds = slot_troop_budget_faction_member_taxes + 1

slot_troop_budget_reserved_party = slot_troop_budget_faction_funds + 1
slot_troop_budget_reserved_other = slot_troop_budget_reserved_party + 1

slot_troop_budget_debt = slot_troop_budget_reserved_other + 1
slot_troop_budget_perceived_debt = slot_troop_budget_debt + 1

slot_troop_last_met = slot_troop_budget_perceived_debt + 1

slot_troop_culture = slot_troop_last_met + 1

slot_troop_ratio_special_multiplier = slot_troop_culture + 1

slot_troop_relations_begin = 400


# # # ToDo: remove test slots
slot_troop_mission_kills = 398
slot_troop_mission_deaths = 399
slot_item_mission_kills = 400
slot_faction_mission_kills = 400
slot_faction_mission_deaths = 401
# # #

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
stt_defend_skirmish = 4

slot_team_battle_phase		= 6
stbp_deploy = 1
stbp_advance = 2
stbp_engage = 3
stbp_prepare = 4
stbp_assault = 5
stbp_combat = 6

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

slot_team_division_1_type 	= 25
slot_team_division_2_type 	= 26
slot_team_division_3_type 	= 27
slot_team_division_4_type 	= 28
slot_team_division_5_type 	= 29
slot_team_division_6_type 	= 30
slot_team_division_7_type 	= 31
slot_team_division_8_type 	= 32
slot_team_division_9_type 	= 33
stdt_shield = 1
stdt_infantry = 2
stdt_heavy_infantry = 3
stdt_light_infantry = 4
stdt_shock_infantry = 5
stdt_cavalry = 6
stdt_lance = 7
stdt_heavy_cavalry = 8
stdt_light_cavalry = 9
stdt_horse_skirmisher = 10
stdt_horse_archer = 11
stdt_skirmisher = 12
stdt_ranged = 13
stdt_crossbow = 14
stdt_archer = 15
stdt_charge = -1

# grc_infantry = 0
# grc_archers = 1
# grc_cavalry = 2
grc_other = 3
grc_flank = 4
grc_charge_group = 5
grc_reinforcement_infantry = 6
grc_reinforcement_archer = 7
grc_reinforcement_cavalry = 8

#################
## Quest Slots ##
#################

quest_slots = 0

slot_quest_giver_troop = 1
slot_quest_expiration_days = slot_quest_giver_troop + 1
slot_quest_dont_give_again_period = slot_quest_expiration_days + 1
slot_quest_dont_give_again_remaining_days = slot_quest_dont_give_again_period + 1

slot_quest_description = slot_quest_dont_give_again_remaining_days + 1

slot_quest_object = slot_quest_description + 1



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
