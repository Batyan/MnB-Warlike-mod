import random
from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *


###############
## Functions ##
###############
def wp(x):
  n = 0
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n
   
def wp_melee(x):
  n = 0
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  return n

# Polearms get a small bonus to wp
def wp_swadian(x):
  n = 0
  n |= wp_one_handed(int(x*1.00))
  n |= wp_two_handed(int(x*0.95))
  n |= wp_polearm(int(x*0.95*1.2))
  n |= wp_archery(int(x*0.90))
  n |= wp_crossbow(int(x*0.85))
  n |= wp_throwing(int(x*0.70))
  return n

def wp_vaegir(x):
  n = 0
  n |= wp_one_handed(int(x*0.90))
  n |= wp_two_handed(int(x*1.00))
  n |= wp_polearm(int(x*0.90*1.2))
  n |= wp_archery(int(x*1.00))
  n |= wp_crossbow(int(x*0.60))
  n |= wp_throwing(int(x*0.80))
  return n

def wp_khergit(x):
  n = 0
  n |= wp_one_handed(int(x*0.90))
  n |= wp_two_handed(int(x*0.85))
  n |= wp_polearm(int(x*1.00*1.2))
  n |= wp_archery(int(x*1.00))
  n |= wp_crossbow(int(x*0.60))
  n |= wp_throwing(int(x*0.75))
  return n

def wp_nord(x):
  n = 0
  n |= wp_one_handed(int(x*1.00))
  n |= wp_two_handed(int(x*0.95))
  n |= wp_polearm(int(x*0.85*1.2))
  n |= wp_archery(int(x*0.85))
  n |= wp_crossbow(int(x*0.60))
  n |= wp_throwing(int(x*0.95))
  return n

def wp_rhodok(x):
  n = 0
  n |= wp_one_handed(int(x*0.95))
  n |= wp_two_handed(int(x*0.85))
  n |= wp_polearm(int(x*1.00*1.2))
  n |= wp_archery(int(x*0.65))
  n |= wp_crossbow(int(x*0.95))
  n |= wp_throwing(int(x*0.70))
  return n

def wp_sarranid(x):
  n = 0
  n |= wp_one_handed(int(x*0.95))
  n |= wp_two_handed(int(x*0.95))
  n |= wp_polearm(int(x*0.90*1.2))
  n |= wp_archery(int(x*0.95))
  n |= wp_crossbow(int(x*0.60))
  n |= wp_throwing(int(x*1.00))
  return n

base_merchant_clothes = [itm_red_shirt, itm_linen_tunic, itm_coarse_tunic, itm_tabard, itm_leather_vest]
merchant_clothes =  base_merchant_clothes + [itm_fur_coat]
merchant_boots = [itm_wrapping_boots, itm_ankle_boots, itm_hide_boots, itm_nomad_boots, itm_leather_boots]
sarranid_merchant_clothes = base_merchant_clothes + [itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b]

#################
## Definitions ##
#################
knows_common = knows_trade_5|knows_looting_2|knows_prisoner_management_4|knows_tactics_2|knows_weapon_master_6|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_engineer_2|knows_persuasion_1

knows_merchant = knows_common|knows_inventory_management_6

def_attrib = str_7 | agi_5 | int_4 | cha_4 | level(4)
def_lord_attrib = str_7 | agi_5 | int_4 | cha_4 | level(40)
def_attrib_multiplayer = str_14 | agi_14 | int_4 | cha_4

def_lord_0 = int_9|cha_9
def_lord_0_str = str_10|agi_9|def_lord_0
def_lord_0_bal = str_10|agi_9|def_lord_0
def_lord_0_agi = str_9|agi_10|def_lord_0

def_lord_1 = int_10|cha_10
def_lord_1_str = str_14|agi_10|def_lord_1
def_lord_1_bal = str_12|agi_12|def_lord_1
def_lord_1_agi = str_10|agi_14|def_lord_1

def_lord_2 = int_11|cha_12
def_lord_2_str = str_17|agi_12|def_lord_2
def_lord_2_bal = str_15|agi_14|def_lord_2
def_lord_2_agi = str_12|agi_17|def_lord_2

def_lord_3 = int_12|cha_15
def_lord_3_str = str_20|agi_14|def_lord_3
def_lord_3_bal = str_17|agi_17|def_lord_3
def_lord_3_agi = str_14|agi_20|def_lord_3

def_lord_4 = int_13|cha_24
def_lord_4_str = str_23|agi_16|def_lord_4
def_lord_4_bal = str_20|agi_19|def_lord_4
def_lord_4_agi = str_16|agi_23|def_lord_4

def_lord_5 = int_14|cha_27
def_lord_5_str = str_26|agi_18|def_lord_5
def_lord_5_bal = str_22|agi_22|def_lord_5
def_lord_5_agi = str_18|agi_26|def_lord_5

def_lord_6 = int_14|cha_33
# def_lord_6_str = str_28|agi_19|def_lord_6
def_lord_6_str = def_lord_5_str
# def_lord_6_bal = str_24|agi_23|def_lord_6
def_lord_6_bal = def_lord_5_bal
# def_lord_6_agi = str_19|agi_28|def_lord_6
def_lord_6_agi = def_lord_5_agi

def_lord_7 = int_15|cha_35
def_lord_7_str = str_30|agi_21|def_lord_7
def_lord_7_bal = str_26|agi_25|def_lord_7
def_lord_7_agi = str_21|agi_30|def_lord_7

knows_lord_0 = knows_prisoner_management_1|knows_weapon_master_1|knows_tactics_1|knows_pathfinding_1|knows_inventory_management_2|knows_looting_1
knows_lord_1 = knows_trainer_2_1|knows_prisoner_management_2|knows_weapon_master_2|knows_tactics_1|knows_pathfinding_1|knows_inventory_management_2|knows_looting_2
knows_lord_2 = knows_leadership_1|knows_trainer_2_2|knows_prisoner_management_3|knows_weapon_master_3|knows_trade_1|knows_tactics_2|knows_pathfinding_1|knows_inventory_management_2|knows_looting_3
knows_lord_3 = knows_leadership_2|knows_trainer_2_2|knows_prisoner_management_4|knows_weapon_master_4|knows_trade_1|knows_tactics_2|knows_pathfinding_1|knows_inventory_management_2|knows_looting_4
knows_lord_4 = knows_leadership_4|knows_trainer_2_4|knows_prisoner_management_5|knows_weapon_master_5|knows_trade_2|knows_tactics_4|knows_pathfinding_1|knows_inventory_management_3|knows_looting_5
knows_lord_5 = knows_leadership_7|knows_trainer_2_5|knows_prisoner_management_6|knows_weapon_master_6|knows_trade_3|knows_tactics_5|knows_pathfinding_1|knows_inventory_management_4|knows_looting_5
# knows_lord_6 = knows_leadership_7|knows_trainer_2_6|knows_prisoner_management_6|knows_weapon_master_6|knows_trade_3|knows_tactics_6|knows_pathfinding_1|knows_inventory_management_4
knows_lord_6 = knows_lord_5
knows_lord_7 = knows_leadership_9|knows_trainer_2_6|knows_prisoner_management_8|knows_weapon_master_7|knows_trade_3|knows_tactics_6|knows_pathfinding_1|knows_inventory_management_4|knows_looting_7

knows_lord_swadian_0 = knows_lord_0|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_power_draw_4|knows_athletics_1|knows_riding_4|knows_horse_archery_2
knows_lord_swadian_1 = knows_lord_1|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_4|knows_athletics_2|knows_riding_4|knows_horse_archery_3
knows_lord_swadian_2 = knows_lord_2|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_4|knows_athletics_3|knows_riding_5|knows_shield_1|knows_horse_archery_4
knows_lord_swadian_3 = knows_lord_3|knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_4|knows_athletics_4|knows_riding_5|knows_shield_1|knows_horse_archery_5
knows_lord_swadian_4 = knows_lord_4|knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_5|knows_athletics_5|knows_riding_6|knows_shield_1|knows_horse_archery_6
knows_lord_swadian_5 = knows_lord_5|knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_6|knows_athletics_6|knows_riding_6|knows_shield_1|knows_horse_archery_7
# knows_lord_swadian_6 = knows_lord_6|knows_ironflesh_9|knows_power_strike_7|knows_power_throw_3|knows_power_draw_6|knows_athletics_6|knows_riding_8|knows_shield_1|knows_horse_archery_7
knows_lord_swadian_6 = knows_lord_swadian_5
knows_lord_swadian_7 = knows_lord_7|knows_ironflesh_10|knows_power_strike_7|knows_power_throw_3|knows_power_draw_6|knows_athletics_6|knows_riding_7|knows_shield_1|knows_horse_archery_7

knows_lord_vaegir_0 = knows_lord_0|knows_ironflesh_1|knows_power_strike_3|knows_power_throw_2|knows_power_draw_4|knows_athletics_2|knows_riding_4|knows_horse_archery_2
knows_lord_vaegir_1 = knows_lord_1|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_2|knows_power_draw_4|knows_athletics_3|knows_riding_4|knows_horse_archery_3
knows_lord_vaegir_2 = knows_lord_2|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_3|knows_power_draw_5|knows_athletics_4|knows_riding_5|knows_shield_1|knows_horse_archery_4
knows_lord_vaegir_3 = knows_lord_3|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_3|knows_power_draw_5|knows_athletics_5|knows_riding_5|knows_shield_1|knows_horse_archery_5
knows_lord_vaegir_4 = knows_lord_4|knows_ironflesh_5|knows_power_strike_6|knows_power_throw_4|knows_power_draw_6|knows_athletics_6|knows_riding_6|knows_shield_1|knows_horse_archery_6
knows_lord_vaegir_5 = knows_lord_5|knows_ironflesh_6|knows_power_strike_7|knows_power_throw_4|knows_power_draw_7|knows_athletics_7|knows_riding_6|knows_shield_1|knows_horse_archery_7
# knows_lord_vaegir_6 = knows_lord_6|knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_power_draw_7|knows_athletics_7|knows_riding_8|knows_shield_1|knows_horse_archery_7
knows_lord_vaegir_6 = knows_lord_vaegir_5
knows_lord_vaegir_7 = knows_lord_7|knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_8|knows_athletics_7|knows_riding_7|knows_shield_1|knows_horse_archery_7

knows_lord_khergit_0 = knows_lord_0|knows_ironflesh_1|knows_power_strike_3|knows_power_throw_2|knows_power_draw_4|knows_athletics_1|knows_riding_4|knows_horse_archery_3
knows_lord_khergit_1 = knows_lord_1|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_2|knows_power_draw_4|knows_athletics_2|knows_riding_4|knows_horse_archery_4
knows_lord_khergit_2 = knows_lord_2|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_3|knows_power_draw_5|knows_athletics_3|knows_riding_5|knows_shield_1|knows_horse_archery_5
knows_lord_khergit_3 = knows_lord_3|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_3|knows_power_draw_5|knows_athletics_4|knows_riding_5|knows_shield_1|knows_horse_archery_6
knows_lord_khergit_4 = knows_lord_4|knows_ironflesh_5|knows_power_strike_6|knows_power_throw_4|knows_power_draw_6|knows_athletics_5|knows_riding_6|knows_shield_1|knows_horse_archery_7
knows_lord_khergit_5 = knows_lord_5|knows_ironflesh_6|knows_power_strike_7|knows_power_throw_4|knows_power_draw_7|knows_athletics_6|knows_riding_6|knows_shield_1|knows_horse_archery_8
# knows_lord_khergit_6 = knows_lord_6|knows_ironflesh_7|knows_power_strike_7|knows_power_throw_4|knows_power_draw_7|knows_athletics_6|knows_riding_9|knows_shield_1|knows_horse_archery_8
knows_lord_khergit_6 = knows_lord_khergit_5
knows_lord_khergit_7 = knows_lord_7|knows_ironflesh_8|knows_power_strike_7|knows_power_throw_4|knows_power_draw_8|knows_athletics_6|knows_riding_7|knows_shield_1|knows_horse_archery_8

knows_lord_nord_0 = knows_lord_0|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_3|knows_power_draw_4|knows_athletics_2|knows_riding_2|knows_horse_archery_1
knows_lord_nord_1 = knows_lord_1|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_3|knows_power_draw_4|knows_athletics_3|knows_riding_2|knows_horse_archery_2
knows_lord_nord_2 = knows_lord_2|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_power_draw_5|knows_athletics_4|knows_riding_3|knows_shield_1|knows_horse_archery_3
knows_lord_nord_3 = knows_lord_3|knows_ironflesh_5|knows_power_strike_6|knows_power_throw_4|knows_power_draw_5|knows_athletics_5|knows_riding_3|knows_shield_1|knows_horse_archery_4
knows_lord_nord_4 = knows_lord_4|knows_ironflesh_6|knows_power_strike_7|knows_power_throw_5|knows_power_draw_6|knows_athletics_6|knows_riding_4|knows_shield_1|knows_horse_archery_5
knows_lord_nord_5 = knows_lord_5|knows_ironflesh_7|knows_power_strike_8|knows_power_throw_5|knows_power_draw_7|knows_athletics_7|knows_riding_4|knows_shield_1|knows_horse_archery_6
# knows_lord_nord_6 = knows_lord_6|knows_ironflesh_8|knows_power_strike_8|knows_power_throw_6|knows_power_draw_7|knows_athletics_7|knows_riding_7|knows_shield_1|knows_horse_archery_6
knows_lord_nord_6 = knows_lord_nord_5
knows_lord_nord_7 = knows_lord_7|knows_ironflesh_9|knows_power_strike_9|knows_power_throw_5|knows_power_draw_8|knows_athletics_7|knows_riding_5|knows_shield_1|knows_horse_archery_6

knows_lord_rhodok_0 = knows_lord_0|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_4|knows_athletics_2|knows_riding_3|knows_horse_archery_1
knows_lord_rhodok_1 = knows_lord_1|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_2|knows_power_draw_4|knows_athletics_3|knows_riding_3|knows_horse_archery_2
knows_lord_rhodok_2 = knows_lord_2|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_3|knows_power_draw_4|knows_athletics_4|knows_riding_4|knows_shield_1|knows_horse_archery_3
knows_lord_rhodok_3 = knows_lord_3|knows_ironflesh_6|knows_power_strike_5|knows_power_throw_3|knows_power_draw_4|knows_athletics_5|knows_riding_4|knows_shield_1|knows_horse_archery_4
knows_lord_rhodok_4 = knows_lord_4|knows_ironflesh_7|knows_power_strike_6|knows_power_throw_3|knows_power_draw_5|knows_athletics_6|knows_riding_5|knows_shield_1|knows_horse_archery_5
knows_lord_rhodok_5 = knows_lord_5|knows_ironflesh_8|knows_power_strike_7|knows_power_throw_3|knows_power_draw_6|knows_athletics_7|knows_riding_5|knows_shield_1|knows_horse_archery_6
# knows_lord_rhodok_6 = knows_lord_6|knows_ironflesh_9|knows_power_strike_7|knows_power_throw_3|knows_power_draw_6|knows_athletics_7|knows_riding_8|knows_shield_1|knows_horse_archery_6
knows_lord_rhodok_6 = knows_lord_rhodok_5
knows_lord_rhodok_7 = knows_lord_7|knows_ironflesh_10|knows_power_strike_7|knows_power_throw_3|knows_power_draw_6|knows_athletics_7|knows_riding_6|knows_shield_1|knows_horse_archery_6

knows_lord_sarranid_0 = knows_lord_0|knows_ironflesh_1|knows_power_strike_3|knows_power_throw_3|knows_power_draw_4|knows_athletics_2|knows_riding_4|knows_horse_archery_2
knows_lord_sarranid_1 = knows_lord_1|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_3|knows_power_draw_4|knows_athletics_3|knows_riding_4|knows_horse_archery_3
knows_lord_sarranid_2 = knows_lord_2|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_4|knows_power_draw_4|knows_athletics_4|knows_riding_5|knows_shield_1|knows_horse_archery_4
knows_lord_sarranid_3 = knows_lord_3|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_4|knows_power_draw_4|knows_athletics_5|knows_riding_5|knows_shield_1|knows_horse_archery_5
knows_lord_sarranid_4 = knows_lord_4|knows_ironflesh_5|knows_power_strike_6|knows_power_throw_5|knows_power_draw_5|knows_athletics_6|knows_riding_6|knows_shield_1|knows_horse_archery_6
knows_lord_sarranid_5 = knows_lord_5|knows_ironflesh_6|knows_power_strike_7|knows_power_throw_5|knows_power_draw_6|knows_athletics_7|knows_riding_6|knows_shield_1|knows_horse_archery_7
# knows_lord_sarranid_6 = knows_lord_6|knows_ironflesh_7|knows_power_strike_7|knows_power_throw_6|knows_power_draw_6|knows_athletics_7|knows_riding_8|knows_shield_1|knows_horse_archery_7
knows_lord_sarranid_6 = knows_lord_sarranid_5
knows_lord_sarranid_7 = knows_lord_7|knows_ironflesh_8|knows_power_strike_7|knows_power_throw_6|knows_power_draw_7|knows_athletics_7|knows_riding_7|knows_shield_1|knows_horse_archery_7

wp_template_0 = 120
wp_template_1 = 140
wp_template_2 = 160
wp_template_3 = 180
wp_template_4 = 200
wp_template_5 = 220
# wp_template_6 = 210
wp_template_6 = wp_template_5
wp_template_7 = 230


knows_companion_noble_low = knows_leadership_2|knows_trainer_2_2|knows_prisoner_management_1|knows_weapon_master_4|knows_tactics_3|knows_pathfinding_1
knows_companion_noble_med = knows_leadership_4|knows_trainer_2_3|knows_prisoner_management_2|knows_weapon_master_5|knows_tactics_5|knows_pathfinding_1
knows_companion_noble_high = knows_leadership_6|knows_trainer_2_4|knows_prisoner_management_3|knows_weapon_master_6|knows_tactics_7|knows_pathfinding_2

knows_companion_warrior_low = knows_leadership_1|knows_trainer_2_3|knows_weapon_master_4|knows_tactics_1
knows_companion_warrior_med = knows_leadership_2|knows_trainer_2_5|knows_weapon_master_5|knows_tactics_2
knows_companion_warrior_high = knows_leadership_3|knows_trainer_2_7|knows_weapon_master_6|knows_tactics_3

knows_companion_support_medic_low = knows_common
knows_companion_support_medic_med = knows_common
knows_companion_support_medic_high = knows_common

knows_companion_support_trade_low = knows_common
knows_companion_support_trade_med = knows_common
knows_companion_support_trade_high = knows_common

knows_companion_support_scout_low = knows_common
knows_companion_support_scout_med = knows_common
knows_companion_support_scout_high = knows_common

knows_companion_support_spy_low = knows_common
knows_companion_support_spy_med = knows_common
knows_companion_support_spy_high = knows_common

knows_companion_civilian_medic_low = knows_common
knows_companion_civilian_medic_med = knows_common
knows_companion_civilian_medic_high = knows_common

knows_companion_civilian_trade_low = knows_common
knows_companion_civilian_trade_med = knows_common
knows_companion_civilian_trade_high = knows_common

knows_companion_civilian_diplomat_low = knows_common
knows_companion_civilian_diplomat_med = knows_common
knows_companion_civilian_diplomat_high = knows_common


tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

tf_guarantee_recruit_armor  = tf_guarantee_armor | tf_guarantee_boots
tf_guarantee_common_armor   = tf_guarantee_recruit_armor | tf_guarantee_helmet
tf_guarantee_trained_armor  = tf_guarantee_common_armor | tf_guarantee_gloves
tf_guarantee_horseman       = tf_mounted | tf_guarantee_horse


reserved = 0
no_scene = 0

swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

# nord_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_younger_1 = 0x000000014000000036db6db6db6db6db00000000001db6db0000000000000000
# nord_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x000000060000000036db6db6db6db6db00000000001db6db0000000000000000
# nord_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x0000000a0000000036db6db6db6db6db00000000001db6db0000000000000000
# nord_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000c0000000036db6db6db6db6db00000000001db6db0000000000000000
# nord_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000fc000000036db6db6db6db6db00000000001db6db0000000000000000

# nord_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_younger_2 = 0x000000016000034b5becb2edaeb7692e00000000001ed93e0000000000000000
# nord_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x000000062000034b5becb2edaeb7692e00000000001ed93e0000000000000000
# nord_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x0000000a2000034b5becb2edaeb7692e00000000001ed93e0000000000000000
# nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000c2000234b5becb2edaeb7692e00000000001ed93e0000000000000000
# nord_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000fe000234b5becb2edaeb7692e00000000001ed93e0000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

sarranid_face_younger_2 = 0x0000000018046183390d63269c8dcd1d00000000001dca5d0000000000000000
sarranid_face_young_2   = 0x000000002f0c7389352b6b4d5e82369a00000000001d275d0000000000000000
sarranid_face_middle_2  = 0x000000072010634f39837342db72367400000000001e28550000000000000000
sarranid_face_old_2     = 0x0000000b1f0865104ae5b28ad084b6ee00000000001d53260000000000000000
sarranid_face_older_2   = 0x0000000fe200624b46e0b12d5a4e34e300000000001e38e30000000000000000

sarranid_face_younger_1 = 0x000000019700758b47de4f58cb8adba1000000000015a2a30000000000000000
sarranid_face_young_1   = 0x00000002c1006410329d96425645daa000000000001dda4b0000000000000000
sarranid_face_middle_1  = 0x000000072610754638e52a21248e58da00000000001e37620000000000000000
sarranid_face_old_1     = 0x0000000b2e0471c348a34a62d9a642a400000000001cd5990000000000000000
sarranid_face_older_1   = 0x0000000ffd0071c658d28dabd469eb2900000000001fa3250000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2
woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000
swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000
khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000
refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2
mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000
vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2
bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2
undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff


base_troop_attributes = str_6|agi_6|int_4|cha_4

############
## Troops ##
############
troops = [

    ###############
    ## Hardcoded ##
    ###############
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [itm_leather_boots, itm_leather_gloves, itm_linen_tunic, itm_sword_medieval_a],
   str_5|agi_5|int_60|cha_5|level(1),wp(10),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000 ],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_linen_tunic, itm_coarse_tunic, itm_tabard, itm_fur_coat, itm_leather_boots, itm_leather_gloves],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000 ],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_linen_tunic, itm_coarse_tunic, itm_tabard, itm_fur_coat, itm_leather_boots, itm_leather_gloves],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000 ],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0 ],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0 ],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0 ],

    ###########
    ## Other ##
    ###########
  
  ["temp_equipement_troop", "Equip Troop", "Equip Troop", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [],
   def_attrib, wp(70), knows_common, 0, 0 ],
  ["current_player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [itm_sword_medieval_b, itm_tab_shield_heater_cav_a, itm_light_lance, itm_leather_boots, itm_leather_gloves, itm_leather_armor_herald, itm_saddle_horse],
   base_troop_attributes|level(1),wp(10),knows_power_strike_1|knows_power_draw_1|knows_athletics_1|knows_riding_1,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000 ],
  #########
  # Lords #
  #########
  ["lord_001", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000007085111455ba5c8e382c91c00000000000d342b0000000000000000, 0 ],
  ["lord_002", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000200320538ab30c4ca6dc862000000000009c6990000000000000000, 0 ],
  ["lord_003", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002410358224db4ee51a7b541b000000000018b6940000000000000000, 0 ],
  ["lord_004", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001d0015c235ac6144e26e12b20000000000132d140000000000000000, 0 ],
  ["lord_005", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000050c330456f46ea3a552a550000000000011d6a10000000000000000, 0 ],
  ["lord_006", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000170403913614a9586231a6a6000000000010b4e30000000000000000, 0 ],
  ["lord_007", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000017044411292c89c54cd1c4dc00000000001d6ae10000000000000000, 0 ],
  ["lord_008", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002808258635a42dd8d3062a1d00000000001d56e20000000000000000, 0 ],
  ["lord_009", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000e04200826e45629636ec6e400000000001dc51e0000000000000000, 0 ],
  ["lord_010", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000027101404269c522b4a713b2300000000001cb6a10000000000000000, 0 ],
  ["lord_011", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000201024d144e3ae390b9348ec00000000001e68a40000000000000000, 0 ],
  ["lord_012", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000a042591330cd6b71e88996300000000000d36900000000000000000, 0 ],
  ["lord_013", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000090c3094296c563a8aa9d2ea00000000000556eb0000000000000000, 0 ],
  ["lord_014", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000350025cd12f46b67298d666200000000001ec6e90000000000000000, 0 ],
  ["lord_015", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002b0c5111469b35d4a37128750000000000063a9d0000000000000000, 0 ],
  ["lord_016", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_017", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e043550391bcd3235373461000000000009b9220000000000000000, 0 ],
  ["lord_018", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_019", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001f08254a46dd88ad0330b50a00000000001e36ec0000000000000000, 0 ],
  ["lord_020", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300c2106484d8d991b51e91200000000001c2ada0000000000000000, 0 ],
  ["lord_021", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001f08254a46dd88ad0330b50a00000000001e36ec0000000000000000, 0 ],
  ["lord_022", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300c2106484d8d991b51e91200000000001c2ada0000000000000000, 0 ],
  ["lord_023", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001f08254a46dd88ad0330b50a00000000001e36ec0000000000000000, 0 ],
  ["lord_024", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300c2106484d8d991b51e91200000000001c2ada0000000000000000, 0 ],
  ["lord_025", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_026", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_027", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_028", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_029", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001f08254a46dd88ad0330b50a00000000001e36ec0000000000000000, 0 ],
  ["lord_030", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300c2106484d8d991b51e91200000000001c2ada0000000000000000, 0 ],
  ["lord_031", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_032", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_033", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_034", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_035", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_036", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_037", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_038", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_039", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_040", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_041", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_042", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_043", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_044", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_045", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_046", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_047", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_048", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_049", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_050", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_051", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_052", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_053", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e042407439b8abad98a54e400000000001db8d40000000000000000, 0 ],
  ["lord_054", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300015102b2369e50b6ed7ad00000000001e395c0000000000000000, 0 ],
  ["lord_055", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000a10304b46554cd96565c6e300000000001b48d90000000000000000, 0 ],
  ["lord_056", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000020c52c748eb2e2adc5b4ac900000000001ddb640000000000000000, 0 ],
  ["lord_057", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000140813531923992121ae4a8c000000000018c31e0000000000000000, 0 ],
  ["lord_058", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002b080089690c48c7138cb8a400000000001cc6de0000000000000000, 0 ],
  ["lord_059", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000001055d236a359d70b8a66ef00000000001ebc930000000000000000, 0 ],
  ["lord_060", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000190012061794c8b96c4de50a00000000001ec4e30000000000000000, 0 ],
  ["lord_061", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000260c15104c5b7648c391e2ed00000000001e38ea0000000000000000, 0 ],
  ["lord_062", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000f08114b1acc45372d6a252900000000001db4a10000000000000000, 0 ],
  ["lord_063", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001e10150328f2753a7392592300000000001d54a30000000000000000, 0 ],
  ["lord_064", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003f1001c92b7389c32cb1ca5d00000000001da6f30000000000000000, 0 ],
  ["lord_065", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000290c00c146da92a624ae56a300000000001d575a0000000000000000, 0 ],
  ["lord_066", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003f04108434ea70c87432b5ab00000000001dc9360000000000000000, 0 ],
  ["lord_067", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003510110a4d1d6dcb248da12d00000000001da2c10000000000000000, 0 ],
  ["lord_068", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003f04020d369c563cdb0d692300000000001e26940000000000000000, 0 ],
  ["lord_069", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003d1015c82c9441c92492c8e200000000001da7950000000000000000, 0 ],
  ["lord_070", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000370415494a9551c2e6d2d75c00000000001ed4da0000000000000000, 0 ],
  ["lord_071", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000310c111446db4e3734554a8b00000000001eb90a0000000000000000, 0 ],
  ["lord_072", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003f08058142b4b94a55aa352400000000001dc89c0000000000000000, 0 ],
  ["lord_073", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000330c15c81513a936dc2ec6db00000000001e14b30000000000000000, 0 ],
  ["lord_074", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000100413025b24715b6d5b1d6200000000001dc6f30000000000000000, 0 ],
  ["lord_075", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000330c15c81513a936dc2ec6db00000000001e14b30000000000000000, 0 ],
  ["lord_076", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000100413025b24715b6d5b1d6200000000001dc6f30000000000000000, 0 ],
  ["lord_077", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000330c15c81513a936dc2ec6db00000000001e14b30000000000000000, 0 ],
  ["lord_078", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000100413025b24715b6d5b1d6200000000001dc6f30000000000000000, 0 ],
  ["lord_079", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000330c15c81513a936dc2ec6db00000000001e14b30000000000000000, 0 ],
  ["lord_080", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000100413025b24715b6d5b1d6200000000001dc6f30000000000000000, 0 ],
  ["lord_081", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000330c15c81513a936dc2ec6db00000000001e14b30000000000000000, 0 ],
  ["lord_082", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000100413025b24715b6d5b1d6200000000001dc6f30000000000000000, 0 ],
  ["lord_083", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000330c15c81513a936dc2ec6db00000000001e14b30000000000000000, 0 ],
  ["lord_084", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000330c15c81513a936dc2ec6db00000000001e14b30000000000000000, 0 ],
  ["lord_085", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000100413025b24715b6d5b1d6200000000001dc6f30000000000000000, 0 ],
  ["lord_086", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000330c15c81513a936dc2ec6db00000000001e14b30000000000000000, 0 ],
  ["lord_087", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000100413025b24715b6d5b1d6200000000001dc6f30000000000000000, 0 ],
  ["lord_088", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000330c15c81513a936dc2ec6db00000000001e14b30000000000000000, 0 ],
  ["lord_089", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000100413025b24715b6d5b1d6200000000001dc6f30000000000000000, 0 ],
  ["lord_090", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003a0863063c9c4243132db69200000000000d67520000000000000000, 0 ],
  ["lord_091", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000a0055cc1cf25a470cae191c000000000010d7260000000000000000, 0 ],
  ["lord_092", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003f1052cd669b56264296a94b00000000001db6960000000000000000, 0 ],
  ["lord_093", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003000431346734da8e479875400000000000a42930000000000000000, 0 ],
  ["lord_094", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002110414b365ac9b6d492928c00000000001c4ab40000000000000000, 0 ],
  ["lord_095", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002a10450930ab8ea2ecbad51200000000001d25220000000000000000, 0 ],
  ["lord_096", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000240c328b391a95b6de11289400000000001db2d00000000000000000, 0 ],
  ["lord_097", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003d0830cb3d23aec4da5324c4000000000016331d0000000000000000, 0 ],
  ["lord_098", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001f0c318a786a54d92c11536400000000001e551d0000000000000000, 0 ],
  ["lord_099", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001004654966dbaf49357996a400000000001ec5110000000000000000, 0 ],
  ["lord_100", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000008424f59744622d868a71e00000000001dcb230000000000000000, 0 ],
  ["lord_101", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003f0c530d46139136a5b5bd2500000000001dfd130000000000000000, 0 ],
  ["lord_102", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000035004380431b1abb224a629900000000001c4d1d0000000000000000, 0 ],
  ["lord_103", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002f0c43925adcb9b6d985bae3000000000008c7240000000000000000, 0 ],
  ["lord_104", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003804424838c986c59b8e4ab1000000000011aaa30000000000000000, 0 ],
  ["lord_105", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001000504c5aa6b6989ba9296400000000001e37b40000000000000000, 0 ],
  ["lord_106", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001b0c304c4ad46a4c6871273500000000001e79220000000000000000, 0 ],
  ["lord_107", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002a0433c9425349ba9d6ec56400000000001de6d60000000000000000, 0 ],
  ["lord_108", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001d08318a5cbaa5229d79b8ed00000000001ec3340000000000000000, 0 ],
  ["lord_109", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002d1043804733cdb4db6e03a600000000001d370b0000000000000000, 0 ],
  ["lord_110", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001d08318a5cbaa5229d79b8ed00000000001ec3340000000000000000, 0 ],
  ["lord_111", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002d1043804733cdb4db6e03a600000000001d370b0000000000000000, 0 ],
  ["lord_112", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001d08318a5cbaa5229d79b8ed00000000001ec3340000000000000000, 0 ],
  ["lord_113", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002d1043804733cdb4db6e03a600000000001d370b0000000000000000, 0 ],
  ["lord_114", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001d08318a5cbaa5229d79b8ed00000000001ec3340000000000000000, 0 ],
  ["lord_115", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002d1043804733cdb4db6e03a600000000001d370b0000000000000000, 0 ],
  ["lord_116", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001d08318a5cbaa5229d79b8ed00000000001ec3340000000000000000, 0 ],
  ["lord_117", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002d1043804733cdb4db6e03a600000000001d370b0000000000000000, 0 ],
  ["lord_118", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001d08318a5cbaa5229d79b8ed00000000001ec3340000000000000000, 0 ],
  ["lord_119", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002d1043804733cdb4db6e03a600000000001d370b0000000000000000, 0 ],
  ["lord_120", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001d08318a5cbaa5229d79b8ed00000000001ec3340000000000000000, 0 ],
  ["lord_121", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002d1043804733cdb4db6e03a600000000001d370b0000000000000000, 0 ],
  ["lord_122", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001d08318a5cbaa5229d79b8ed00000000001ec3340000000000000000, 0 ],
  ["lord_123", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002d1043804733cdb4db6e03a600000000001d370b0000000000000000, 0 ],
  ["lord_124", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001d08318a5cbaa5229d79b8ed00000000001ec3340000000000000000, 0 ],
  ["lord_125", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002d1043804733cdb4db6e03a600000000001d370b0000000000000000, 0 ],
  ["lord_126", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000151002d049359138cd4db89400000000001eca630000000000000000, 0 ],
  ["lord_127", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000e00110732ac70b89a91e55500000000001eb8a30000000000000000, 0 ],
  ["lord_128", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001f10038636f1a4a95b4b376300000000001eb8f20000000000000000, 0 ],
  ["lord_129", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000c0c02830e9b9566cc32d84d00000000001d34e30000000000000000, 0 ],
  ["lord_130", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001708010935a3764b4d51daac00000000001de46c0000000000000000, 0 ],
  ["lord_131", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003100120652b572246e51ab3000000000001e4aa90000000000000000, 0 ],
  ["lord_132", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000180805121ce59a76998a284d00000000001e26ac0000000000000000, 0 ],
  ["lord_133", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002b1010472edeb15b1299a8e500000000001ddb2b0000000000000000, 0 ],
  ["lord_134", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000230812c9249dade974d5a4ab00000000001de71a0000000000000000, 0 ],
  ["lord_135", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000908010424ed54e52573b91600000000001eeac80000000000000000, 0 ],
  ["lord_136", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003c0005c558d98e44d2b3170a00000000001d555a0000000000000000, 0 ],
  ["lord_137", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000040813004992ea290c55b7aa00000000001dc29b0000000000000000, 0 ],
  ["lord_138", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002010144642a36ec31a6a969a00000000001da7190000000000000000, 0 ],
  ["lord_139", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003a0c144f36e291c3a5bae64c00000000001d1b590000000000000000, 0 ],
  ["lord_140", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001a0c020756f446269e5add5500000000001e425c0000000000000000, 0 ],
  ["lord_141", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000038100209470b78da4badb45b00000000001e3ad90000000000000000, 0 ],
  ["lord_142", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d08020344d45146e499287400000000001cb8a60000000000000000, 0 ],
  ["lord_143", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000900128736d5864718aa370a00000000001d59720000000000000000, 0 ],
  ["lord_144", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000310810493ad0d56b726d389a00000000001f56940000000000000000, 0 ],
  ["lord_145", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000160c054a352495374465a49a00000000001eb9200000000000000000, 0 ],
  ["lord_146", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000310810493ad0d56b726d389a00000000001f56940000000000000000, 0 ],
  ["lord_147", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000160c054a352495374465a49a00000000001eb9200000000000000000, 0 ],
  ["lord_148", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000310810493ad0d56b726d389a00000000001f56940000000000000000, 0 ],
  ["lord_149", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000160c054a352495374465a49a00000000001eb9200000000000000000, 0 ],
  ["lord_150", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000310810493ad0d56b726d389a00000000001f56940000000000000000, 0 ],
  ["lord_151", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000160c054a352495374465a49a00000000001eb9200000000000000000, 0 ],
  ["lord_152", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000310810493ad0d56b726d389a00000000001f56940000000000000000, 0 ],
  ["lord_153", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000160c054a352495374465a49a00000000001eb9200000000000000000, 0 ],
  ["lord_154", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000310810493ad0d56b726d389a00000000001f56940000000000000000, 0 ],
  ["lord_155", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000160c054a352495374465a49a00000000001eb9200000000000000000, 0 ],
  ["lord_156", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000310810493ad0d56b726d389a00000000001f56940000000000000000, 0 ],
  ["lord_157", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000160c054a352495374465a49a00000000001eb9200000000000000000, 0 ],
  ["lord_158", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000310810493ad0d56b726d389a00000000001f56940000000000000000, 0 ],
  ["lord_159", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000160c054a352495374465a49a00000000001eb9200000000000000000, 0 ],
  ["lord_160", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000310810493ad0d56b726d389a00000000001f56940000000000000000, 0 ],
  ["lord_161", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000160c054a352495374465a49a00000000001eb9200000000000000000, 0 ],
  ["lord_162", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000001042d239648e12a250aa6500000000000cbaa30000000000000000, 0 ],
  ["lord_163", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003c0833860d5ba6d6e16dd6e500000000001d99db0000000000000000, 0 ],
  ["lord_164", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000011103205395e8ebb356d692d00000000001cb71d0000000000000000, 0 ],
  ["lord_165", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002f10538e575da94564add7a300000000001cd5120000000000000000, 0 ],
  ["lord_166", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000060433d428eb713d0430c89a000000000010d9b20000000000000000, 0 ],
  ["lord_167", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d10331259f18f121eacc6d400000000001e48e50000000000000000, 0 ],
  ["lord_168", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003b00219206956417ac79371200000000001d76f40000000000000000, 0 ],
  ["lord_169", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003d083384329466ccaa6e155b00000000001dc6630000000000000000, 0 ],
  ["lord_170", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000007003492165a59a91a914c6e00000000001d99240000000000000000, 0 ],
  ["lord_171", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000360830103b2291ad1d8d376b00000000001e2ad90000000000000000, 0 ],
  ["lord_172", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000170853452aec69d65389c4c900000000001eb75a0000000000000000, 0 ],
  ["lord_173", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e0031133766ca959db1d88d00000000000a32e50000000000000000, 0 ],
  ["lord_174", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000028042444308c9157167a470b00000000001d855c0000000000000000, 0 ],
  ["lord_175", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000390050d44cd6b2aa932acca5000000000014eaa90000000000000000, 0 ],
  ["lord_176", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002800331335224d4b0cf298e400000000001e48950000000000000000, 0 ],
  ["lord_177", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300425d034938d5b1d8db4e200000000001e2b1a0000000000000000, 0 ],
  ["lord_178", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000110862524ae324c5236a271c00000000001dd99b0000000000000000, 0 ],
  ["lord_179", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000170035933d2292b89592191400000000001d24510000000000000000, 0 ],
  ["lord_180", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_181", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_182", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_183", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_184", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_185", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_186", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_187", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_188", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_189", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_190", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_191", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_192", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_193", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_194", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_195", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_196", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_197", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_198", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_199", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_200", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_201", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002d086313556d6d49d968f39400000000001deaad0000000000000000, 0 ],
  ["lord_202", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000c04720528dab5e79b5ae89200000000001dc55a0000000000000000, 0 ],
  ["lord_203", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000250860c124de29e71e8ab7a200000000000e3b230000000000000000, 0 ],
  ["lord_204", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000017047013289b99a55c2c390500000000001e32e50000000000000000, 0 ],
  ["lord_205", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001610758b1d2972e9e66e2d1900000000001daa9a0000000000000000, 0 ],
  ["lord_206", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000080445c41ad5ccc97590e9e300000000001e386e0000000000000000, 0 ],
  ["lord_207", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000150063045b4c8558d2b14ca300000000001eb5640000000000000000, 0 ],
  ["lord_208", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000240062482b54d2336479cbab00000000001e35330000000000000000, 0 ],
  ["lord_209", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003d0462c8236de646da0949a500000000001e449d0000000000000000, 0 ],
  ["lord_210", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010861ca450d89c6e167ba6c00000000000eb3920000000000000000, 0 ],
  ["lord_211", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000c0061912724ca29826f22e300000000001dad190000000000000000, 0 ],
  ["lord_212", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001b10420b5531c6326cb5cd1100000000001da7130000000000000000, 0 ],
  ["lord_213", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001a0062103af391c51d50ac3500000000001da7140000000000000000, 0 ],
  ["lord_214", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003608659254db8a3c658e96a400000000001f2b090000000000000000, 0 ],
  ["lord_215", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000310c45922aab4f36dc7238d300000000001da49c0000000000000000, 0 ],
  ["lord_216", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000308711036e3b12a5435b51400000000001d371b0000000000000000, 0 ],
  ["lord_217", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000370c658d2915b6a74a50d55a00000000001ddae20000000000000000, 0 ],
  ["lord_218", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000028044186178b95555b95576300000000001dcce30000000000000000, 0 ],
  ["lord_219", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_220", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_221", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_222", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_223", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_224", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_225", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_226", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_227", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_228", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_229", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_230", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_231", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_232", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_233", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_234", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_235", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_236", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_237", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_238", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_239", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_240", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_241", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_242", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_243", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_244", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_245", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_246", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_247", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_248", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_249", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_250", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_251", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_252", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_253", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_254", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_255", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_256", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_257", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_258", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_259", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_260", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_261", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_262", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_263", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_264", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_265", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_266", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_267", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_268", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_269", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_270", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_271", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000360830103b2291ad1d8d376b00000000001e2ad90000000000000000, 0 ],
  ["lord_272", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000170853452aec69d65389c4c900000000001eb75a0000000000000000, 0 ],
  ["lord_273", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e0031133766ca959db1d88d00000000000a32e50000000000000000, 0 ],
  ["lord_274", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000028042444308c9157167a470b00000000001d855c0000000000000000, 0 ],
  ["lord_275", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000390050d44cd6b2aa932acca5000000000014eaa90000000000000000, 0 ],
  ["lord_276", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002800331335224d4b0cf298e400000000001e48950000000000000000, 0 ],
  ["lord_277", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300425d034938d5b1d8db4e200000000001e2b1a0000000000000000, 0 ],
  ["lord_278", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000110862524ae324c5236a271c00000000001dd99b0000000000000000, 0 ],
  ["lord_279", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000170035933d2292b89592191400000000001d24510000000000000000, 0 ],
  ["lord_280", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_281", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_282", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_283", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_284", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_285", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_286", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_287", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_288", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_289", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_290", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_291", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_292", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_293", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_294", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_295", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_296", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_297", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_298", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_299", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_300", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_301", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002d086313556d6d49d968f39400000000001deaad0000000000000000, 0 ],
  ["lord_302", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000c04720528dab5e79b5ae89200000000001dc55a0000000000000000, 0 ],
  ["lord_303", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000250860c124de29e71e8ab7a200000000000e3b230000000000000000, 0 ],
  ["lord_304", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000017047013289b99a55c2c390500000000001e32e50000000000000000, 0 ],
  ["lord_305", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001610758b1d2972e9e66e2d1900000000001daa9a0000000000000000, 0 ],
  ["lord_306", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000080445c41ad5ccc97590e9e300000000001e386e0000000000000000, 0 ],
  ["lord_307", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000150063045b4c8558d2b14ca300000000001eb5640000000000000000, 0 ],
  ["lord_308", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000240062482b54d2336479cbab00000000001e35330000000000000000, 0 ],
  ["lord_309", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003d0462c8236de646da0949a500000000001e449d0000000000000000, 0 ],
  ["lord_310", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010861ca450d89c6e167ba6c00000000000eb3920000000000000000, 0 ],
  ["lord_311", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000c0061912724ca29826f22e300000000001dad190000000000000000, 0 ],
  ["lord_312", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001b10420b5531c6326cb5cd1100000000001da7130000000000000000, 0 ],
  ["lord_313", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001a0062103af391c51d50ac3500000000001da7140000000000000000, 0 ],
  ["lord_314", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003608659254db8a3c658e96a400000000001f2b090000000000000000, 0 ],
  ["lord_315", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000310c45922aab4f36dc7238d300000000001da49c0000000000000000, 0 ],
  ["lord_316", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000308711036e3b12a5435b51400000000001d371b0000000000000000, 0 ],
  ["lord_317", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000370c658d2915b6a74a50d55a00000000001ddae20000000000000000, 0 ],
  ["lord_318", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000028044186178b95555b95576300000000001dcce30000000000000000, 0 ],
  ["lord_319", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_320", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_321", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_322", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_323", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_324", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_325", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_326", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_327", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_328", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_329", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_330", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_331", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_332", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_333", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_334", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_335", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_336", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_337", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_338", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_339", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_340", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_341", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_342", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_343", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_344", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_345", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_346", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_347", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_348", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_349", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_350", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_351", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_352", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_353", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_354", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_355", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_356", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_357", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_358", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_359", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_360", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_361", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_362", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_363", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_364", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_365", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_366", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_367", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_368", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_369", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_370", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_371", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000360830103b2291ad1d8d376b00000000001e2ad90000000000000000, 0 ],
  ["lord_372", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000170853452aec69d65389c4c900000000001eb75a0000000000000000, 0 ],
  ["lord_373", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e0031133766ca959db1d88d00000000000a32e50000000000000000, 0 ],
  ["lord_374", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000028042444308c9157167a470b00000000001d855c0000000000000000, 0 ],
  ["lord_375", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000390050d44cd6b2aa932acca5000000000014eaa90000000000000000, 0 ],
  ["lord_376", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002800331335224d4b0cf298e400000000001e48950000000000000000, 0 ],
  ["lord_377", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300425d034938d5b1d8db4e200000000001e2b1a0000000000000000, 0 ],
  ["lord_378", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000110862524ae324c5236a271c00000000001dd99b0000000000000000, 0 ],
  ["lord_379", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000170035933d2292b89592191400000000001d24510000000000000000, 0 ],
  ["lord_380", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_381", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_382", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_383", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_384", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_385", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_386", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_387", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_388", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_389", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_390", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_391", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_392", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_393", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_394", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_395", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_396", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_397", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_398", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_399", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_400", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_401", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002d086313556d6d49d968f39400000000001deaad0000000000000000, 0 ],
  ["lord_402", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000c04720528dab5e79b5ae89200000000001dc55a0000000000000000, 0 ],
  ["lord_403", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000250860c124de29e71e8ab7a200000000000e3b230000000000000000, 0 ],
  ["lord_404", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000017047013289b99a55c2c390500000000001e32e50000000000000000, 0 ],
  ["lord_405", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001610758b1d2972e9e66e2d1900000000001daa9a0000000000000000, 0 ],
  ["lord_406", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000080445c41ad5ccc97590e9e300000000001e386e0000000000000000, 0 ],
  ["lord_407", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000150063045b4c8558d2b14ca300000000001eb5640000000000000000, 0 ],
  ["lord_408", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000240062482b54d2336479cbab00000000001e35330000000000000000, 0 ],
  ["lord_409", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003d0462c8236de646da0949a500000000001e449d0000000000000000, 0 ],
  ["lord_410", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010861ca450d89c6e167ba6c00000000000eb3920000000000000000, 0 ],
  ["lord_411", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000c0061912724ca29826f22e300000000001dad190000000000000000, 0 ],
  ["lord_412", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001b10420b5531c6326cb5cd1100000000001da7130000000000000000, 0 ],
  ["lord_413", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001a0062103af391c51d50ac3500000000001da7140000000000000000, 0 ],
  ["lord_414", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000003608659254db8a3c658e96a400000000001f2b090000000000000000, 0 ],
  ["lord_415", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000310c45922aab4f36dc7238d300000000001da49c0000000000000000, 0 ],
  ["lord_416", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000308711036e3b12a5435b51400000000001d371b0000000000000000, 0 ],
  ["lord_417", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000370c658d2915b6a74a50d55a00000000001ddae20000000000000000, 0 ],
  ["lord_418", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000028044186178b95555b95576300000000001dcce30000000000000000, 0 ],
  ["lord_419", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_420", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_421", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_422", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_423", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_424", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_425", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_426", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_427", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_428", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_429", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_430", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_431", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_432", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_433", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_434", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_435", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_436", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_437", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_438", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_439", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000061042d341497659088e4474000000000006a76f0000000000000000, 0 ],
  ["lord_440", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_441", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_442", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_443", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_444", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_445", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_446", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_447", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_448", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_449", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_450", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_451", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_452", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_453", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_454", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_455", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_456", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_457", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_458", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_459", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_460", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_461", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_462", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_463", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_464", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_465", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_466", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_467", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_468", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_469", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_470", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["lord_471", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000360830103b2291ad1d8d376b00000000001e2ad90000000000000000, 0 ],
  ["lord_472", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000170853452aec69d65389c4c900000000001eb75a0000000000000000, 0 ],
  ["lord_473", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002e0031133766ca959db1d88d00000000000a32e50000000000000000, 0 ],
  ["lord_474", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x0000000028042444308c9157167a470b00000000001d855c0000000000000000, 0 ],
  ["lord_475", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000390050d44cd6b2aa932acca5000000000014eaa90000000000000000, 0 ],
  ["lord_476", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000002800331335224d4b0cf298e400000000001e48950000000000000000, 0 ],
  ["lord_477", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000300425d034938d5b1d8db4e200000000001e2b1a0000000000000000, 0 ],
  ["lord_478", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000110862524ae324c5236a271c00000000001dd99b0000000000000000, 0 ],
  ["lord_479", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000170035933d2292b89592191400000000001d24510000000000000000, 0 ],
  ["lord_480", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_481", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_482", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_483", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_484", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_485", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_486", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_487", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_488", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_489", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_490", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_491", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_492", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_493", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_494", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_495", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_496", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_497", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_498", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x00000000010432c526da492a4332d92100000000001ef7240000000000000000, 0 ],
  ["lord_499", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  ["lord_500", "Lord", "Lord", tf_hero, no_scene, reserved, fac_commoners, [],
   def_lord_attrib, wp(70), knows_common, 0x000000001704348f2d64843912a9229600000000001dc7530000000000000000, 0 ],
  
  
  # Companions begin
  # Nobles
  ["companion_noble_01_m", "Julian", "Julian", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_sword_medieval_b, itm_light_lance, itm_tab_shield_heater_cav_a,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_leather_herald,
    itm_mail_coif,
    itm_pack_horse],
   str_10|agi_11|int_9|cha_12|level(19), wp_swadian(95), knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_riding_6|knows_companion_noble_low, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_02_m", "Maximilian", "Maximilian", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_sword_medieval_c_long, itm_lance, itm_tab_shield_heater_cav_a,
    itm_mail_chausses, itm_mail_mittens,
    itm_haubergeon_herald,
    itm_kettle_hat,
    itm_hunter],
   str_15|agi_13|int_10|cha_15|level(30), wp_swadian(150), knows_ironflesh_6|knows_power_strike_5|knows_athletics_3|knows_riding_5|knows_companion_noble_med, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_03_m", "Maximus", "Maximus", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_morningstar, itm_heavy_lance, itm_tab_shield_heater_cav_b,
    itm_mail_boots, itm_mail_mittens,
    itm_coat_of_plates_herald,
    itm_guard_helmet,
    itm_warhorse],
   str_21|agi_14|int_12|cha_16|level(40), wp_swadian(200), knows_ironflesh_9|knows_power_strike_6|knows_athletics_4|knows_riding_6|knows_companion_noble_high, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_04_m", "Geal", "Geal", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_scimitar, itm_tab_shield_kite_cav_a,
    itm_leather_boots, itm_leather_gloves,
    itm_tribal_warrior_outfit,
    itm_vaegir_fur_cap,
    itm_steppe_horse],
   str_9|agi_12|int_9|cha_11|level(18), wp_vaegir(90), knows_ironflesh_1|knows_power_strike_4|knows_athletics_3|knows_riding_6|knows_companion_noble_low, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_05_m", "Lixen", "Lixen", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_one_handed_battle_axe_a, itm_light_lance, itm_tab_shield_kite_cav_a,
    itm_leather_boots, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet,
    itm_hunter],
   str_13|agi_16|int_11|cha_14|level(31), wp_vaegir(155), knows_ironflesh_3|knows_power_strike_5|knows_athletics_4|knows_riding_5|knows_companion_noble_med, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_06_m", "Aethrod", "Aethrod", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_bardiche, itm_war_bow, itm_bodkin_arrows,
    itm_mail_boots, itm_mail_mittens,
    itm_lamellar_armor_herald,
    itm_vaegir_war_helmet,
    itm_warhorse],
   str_18|agi_18|int_13|cha_17|level(43), wp_vaegir(215), knows_ironflesh_5|knows_power_strike_6|knows_power_draw_7|knows_athletics_5|knows_riding_6|knows_horse_archery_6|knows_companion_noble_high, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_07_m", "Lin", "Lin", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_sword_khergit_2, itm_javelin, itm_tab_shield_small_round_a,
    itm_leather_boots, itm_leather_gloves,
    itm_steppe_armor_herald,
    
    itm_steppe_horse],
   str_9|agi_11|int_9|cha_10|level(16), wp_khergit(80), knows_power_strike_4|knows_power_throw_3|knows_athletics_3|knows_riding_6|knows_horse_archery_4|knows_companion_noble_low, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_08_m", "Aleshtur", "Aleshtur", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_khergit_sword_two_handed_b, itm_khergit_bow, itm_khergit_arrows, itm_khergit_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_khergit_war_helmet,
    itm_hunter],
   str_14|agi_15|int_12|cha_15|level(33), wp_khergit(165), knows_ironflesh_2|knows_power_strike_5|knows_power_draw_5|knows_athletics_5|knows_riding_7|knows_horse_archery_7|knows_companion_noble_med, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_09_m", "Mancha", "Mancha", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_spiked_mace, itm_heavy_lance, itm_tab_shield_small_round_c,
    itm_splinted_greaves, itm_scale_gauntlets,
    itm_lamellar_armor_herald,
    itm_khergit_guard_helmet,
    itm_hunter],
   str_17|agi_20|int_14|cha_17|level(45), wp_khergit(215), knows_ironflesh_4|knows_power_strike_6|knows_athletics_5|knows_riding_7|knows_companion_noble_high, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_10_m", "Uldin", "Uldin", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_one_handed_battle_axe_a, itm_throwing_axes, itm_tab_shield_round_c,
    itm_leather_boots, itm_leather_gloves,
    itm_byrnie_herald,
    itm_nordic_fighter_helmet,
    ],
   str_11|agi_11|int_8|cha_11|level(18), wp_nord(90), knows_ironflesh_2|knows_power_strike_5|knows_power_throw_3|knows_athletics_4|knows_companion_noble_low, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_11_m", "Uthred", "Uthred", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_sword_viking_2_small, itm_long_bow, itm_bodkin_arrows, itm_tab_shield_round_d,
    itm_mail_chausses, itm_mail_mittens,
    itm_byrnie_herald,
    itm_nordic_fighter_helmet,
    ],
   str_14|agi_14|int_9|cha_13|level(27), wp_nord(135), knows_ironflesh_4|knows_power_strike_6|knows_power_draw_7|knows_athletics_5|knows_companion_noble_med, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_12_m", "Vlok", "Vlok", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_one_handed_battle_axe_b, itm_tab_shield_round_e,
    itm_iron_greaves, itm_gauntlets,
    itm_banded_armor,
    itm_nordic_warlord_helmet,
    ],
   str_18|agi_18|int_11|cha_17|level(41), wp_nord(205), knows_ironflesh_6|knows_power_strike_7|knows_athletics_6|knows_shield_1|knows_companion_noble_high, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_13_m", "Romulus", "Romulus", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_military_sickle_a, itm_tab_shield_pavise_b,
    itm_leather_boots, itm_leather_gloves,
    itm_byrnie_herald,
    itm_kettle_hat,
    ],
   str_13|agi_10|int_8|cha_12|level(20), wp_rhodok(100), knows_ironflesh_2|knows_power_strike_5|knows_athletics_3|knows_companion_noble_low, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_14_m", "Robin", "Robin", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_sword_medieval_b, itm_light_crossbow, itm_steel_bolts, itm_tab_shield_heater_cav_b,
    itm_mail_chausses, itm_mail_mittens,
    itm_surcoat_over_mail_herald,
    itm_guard_helmet,
    itm_hunter],
   str_17|agi_12|int_10|cha_14|level(30), wp_rhodok(150), knows_ironflesh_6|knows_power_strike_5|knows_athletics_2|knows_riding_5|knows_horse_archery_5|knows_companion_noble_med, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  ["companion_noble_15_m", "Bunduk", "Bunduk", tf_hero, no_scene, reserved, fac_commoners, 
   [itm_military_cleaver_b, itm_tab_shield_pavise_c, itm_siege_crossbow, itm_steel_bolts,
    itm_iron_greaves, itm_gauntlets,
    itm_coat_of_plates_herald,
    itm_full_helm_herald,
    ],
   str_24|agi_14|int_12|cha_17|level(44), wp_rhodok(220), knows_ironflesh_10|knows_power_strike_7|knows_athletics_5|knows_shield_1|knows_companion_noble_high, 0x000000000d04718d372c6d9f4d6d46a400000000001ea4910000000000000000, 0 ],
  # Warriors
  # Support
  # Civilians
  
  # Generic companions
  ["companion_001", "Companion", "Companion", tf_hero, no_scene, reserved, fac_commoners,
   [],
   def_lord_attrib,wp(70),knows_common, man_face_young_1, man_face_young_2],

  
  ############
  # Swadians #
  ############
  # Peasant
  # Basic infantry, swords, picks, maces, shields
  ["swadian_levy", "Swadian Levy", "Swadian Levies", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_fighting_pick, itm_mace_2, itm_sword_medieval_a, itm_tab_shield_heater_a,itm_tab_shield_heater_a_plain_1,itm_tab_shield_heater_a_plain_2,
    itm_ankle_boots, itm_wrapping_boots, itm_leather_boots,
    itm_padded_cloth, itm_leather_armor_herald,
    itm_padded_coif, itm_arming_cap,
    ],
   str_9|agi_9|int_7|cha_7|level(9), wpex(80,60,70,50,40,35), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_draw_1|knows_athletics_4|knows_riding_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Basic ranged, swords, picks, maces, daggers, bows, crossbows, shields
  ["swadian_militia", "Swadian Militia", "Swadian Militias", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_1,
   [itm_fighting_pick, itm_mace_2, itm_sword_medieval_a, itm_dagger, itm_arrows_b, itm_bolts, itm_hunting_bow2, itm_hunting_crossbow,
    itm_ankle_boots, itm_wrapping_boots,
    itm_padded_cloth, itm_leather_armor_herald,
    itm_padded_coif, itm_arming_cap,
    ],
   str_9|agi_11|int_6|cha_7|level(10), wpex(70,50,60,70,60,45), knows_common|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Basic infantry, spears, shields
  # SPECIAL
  ["swadian_levy_spearman", "Swadian Levy Spearman", "Swadian Levy Spearmen", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_13,
   [itm_spear, itm_tab_shield_heater_a,itm_tab_shield_heater_a_plain_1,itm_tab_shield_heater_a_plain_2,
    itm_ankle_boots, itm_wrapping_boots, itm_leather_boots,
    itm_padded_cloth, itm_leather_armor_herald,
    itm_padded_coif, itm_arming_cap,
    ],
   str_10|agi_8|int_7|cha_6|level(8), wpex(65,60,85,50,40,35), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_draw_1|knows_athletics_2|knows_riding_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Basic infantry skirmisher, swords, picks, maces, darts, shields
  # SPECIAL
  ["swadian_levy_skirmisher", "Swadian Levy Skirmisher", "Swadian Levy Skirmishers", tf_guarantee_recruit_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_16,
   [itm_fighting_pick, itm_mace_2, itm_sword_medieval_a, itm_dagger, itm_darts, itm_darts, itm_tab_shield_heater_a,itm_tab_shield_heater_a_plain_1,itm_tab_shield_heater_a_plain_2,
    itm_ankle_boots, itm_wrapping_boots, itm_leather_boots,
    itm_padded_cloth, itm_leather_armor_herald,
    itm_padded_coif, itm_arming_cap,
    ],
   str_9|agi_10|int_7|cha_7|level(10), wpex(70,50,60,50,40,75), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_throw_2|knows_power_draw_1|knows_athletics_4|knows_riding_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Basic ranged, picks, maces, daggers, bows, shields
  # SPECIAL
  ["swadian_hunter", "Swadian Hunter", "Swadian Hunters", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_14,
   [itm_fighting_pick, itm_mace_2, itm_dagger, itm_arrows_b, itm_hunting_bow2,
    itm_ankle_boots, itm_wrapping_boots,
    itm_leather_armor_herald,
    itm_padded_coif, itm_arming_cap,
    ],
   str_8|agi_10|int_6|cha_7|level(8), wpex(65,50,60,70,40,45), knows_common|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Basic infantry, polearms
  # SPECIAL
  ["swadian_levy_infantry", "Swadian Levy Infantry", "Swadian Levy Infantries", tf_guarantee_recruit_armor, no_scene, reserved, fac_small_kingdom_12,
   [itm_voulge_old,
    itm_ankle_boots, itm_wrapping_boots, itm_leather_boots,
    itm_padded_cloth, itm_leather_armor_herald,
    itm_padded_coif, itm_arming_cap,
    ],
   str_10|agi_9|int_7|cha_7|level(10), wpex(60,70,80,50,40,35), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_draw_1|knows_athletics_4|knows_riding_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Common
  # Light infantry, swords, picks, maces, shields
  ["swadian_light_infantry", "Swadian Footman", "Swadian Footmen", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_fighting_pick, itm_mace_3, itm_tab_shield_heater_b,itm_tab_shield_heater_b_plain_1,itm_tab_shield_heater_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_cloth, itm_gambeson_herald, itm_leather_jerkin_herald, itm_padded_leather_herald,
    itm_footman_helmet, itm_mail_coif, itm_helmet_with_neckguard,
    ],
   str_14|agi_15|int_7|cha_8|level(21), wpex(115,90,100,65,55,45), knows_common|knows_ironflesh_3|knows_power_strike_5|knows_power_throw_1|knows_power_draw_1|knows_athletics_5|knows_riding_2, swadian_face_young_1, swadian_face_old_2 ],
  
  # Light infantry skirmisher, swords, picks, maces, darts, shields
  ["swadian_skirmisher", "Swadian Skirmisher", "Swadian Skirmishers", tf_guarantee_common_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_fighting_pick, itm_mace_3, itm_war_darts, itm_war_darts, itm_tab_shield_heater_a,itm_tab_shield_heater_a_plain_1,itm_tab_shield_heater_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_cloth, itm_leather_armor_herald, itm_leather_jerkin_herald,
    itm_footman_helmet, itm_mail_coif, itm_padded_coif, itm_helmet_with_neckguard,
    ],
   str_12|agi_16|int_7|cha_7|level(19), wpex(85,60,70,70,60,110), knows_common|knows_ironflesh_2|knows_power_strike_5|knows_power_throw_2|knows_power_draw_1|knows_athletics_5|knows_riding_2, swadian_face_young_1, swadian_face_old_2 ],
  
  # Light ranged, swords, picks, maces, daggers, bows
  ["swadian_light_bowman", "Swadian Light Bowman", "Swadian Light Bowmen", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_1,
   [itm_fighting_pick, itm_mace_2, itm_sword_medieval_a, itm_dagger, itm_barbed_arrows, itm_barbed_arrows, itm_hunting_bow2,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_cloth, itm_leather_armor_herald,
    itm_padded_coif, itm_arming_cap, itm_footman_helmet,
    ],
   str_11|agi_16|int_6|cha_7|level(17), wpex(75,50,60,135,65,50), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_6|knows_riding_2|knows_horse_archery_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Light ranged, swords, picks, maces, daggers, crossbows, shields
  ["swadian_light_crossbowman", "Swadian Light Crossbowman", "Swadian Light Crossbowmen", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_1,
   [itm_fighting_pick, itm_mace_2, itm_sword_medieval_a, itm_dagger, itm_steel_bolts, itm_steel_bolts, itm_hunting_crossbow, itm_tab_shield_heater_a,itm_tab_shield_heater_a_plain_1,itm_tab_shield_heater_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_cloth, itm_leather_armor_herald, itm_leather_jerkin_herald,
    itm_padded_coif, itm_arming_cap, itm_mail_coif, itm_footman_helmet,
    ],
   str_12|agi_15|int_7|cha_7|level(18), wpex(75,50,60,75,125,50), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_1|knows_athletics_4|knows_riding_2|knows_horse_archery_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Light cavalry skirmisher, swords, darts, shields
  # SPECIAL
  ["swadian_mounted_skirmisher", "Swadian Mounted Skirmisher", "Swadian Mounted Skirmishers", tf_guarantee_common_armor|tf_guarantee_ranged|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_16,
   [itm_sword_medieval_a, itm_sword_medieval_a_long, itm_war_darts, itm_war_darts, itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a_plain_1,itm_tab_shield_heater_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_cloth, itm_leather_armor_herald, itm_leather_jerkin_herald,
    itm_footman_helmet, itm_mail_coif, itm_padded_coif,
    itm_saddle_horse],
   str_12|agi_16|int_7|cha_8|level(20), wpex(80,60,70,70,60,105), knows_common|knows_ironflesh_1|knows_power_strike_4|knows_power_throw_2|knows_power_draw_1|knows_athletics_3|knows_riding_6|knows_horse_archery_3, swadian_face_young_1, swadian_face_old_2 ],
  
  # Light cavalry, spears, shields
  # SPECIAL
  ["swadian_scout", "Swadian Scout", "Swadian Scouts", tf_guarantee_common_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_15,
   [itm_spear, itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a_plain_1,itm_tab_shield_heater_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_cloth, itm_leather_jerkin_herald, itm_leather_armor_herald,
    itm_footman_helmet, itm_mail_coif, itm_padded_coif, itm_padded_coif,
    itm_saddle_horse],
   str_12|agi_15|int_7|cha_8|level(19), wpex(90,80,120,60,50,50), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_power_draw_1|knows_athletics_4|knows_riding_6|knows_horse_archery_2, swadian_face_young_1, swadian_face_old_2 ],
  
  # Light ranged, swords, picks, maces, bows
  # SPECIAL
  ["swadian_light_longbowman", "Swadian Light Longbowman", "Swadian Light Longbowmen", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_14,
   [itm_fighting_pick, itm_mace_2, itm_sword_medieval_a, itm_dagger, itm_long_bow2, itm_barbed_arrows, itm_barbed_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_cloth, itm_leather_armor_herald,
    itm_padded_coif, itm_arming_cap, itm_footman_helmet,
    ],
   str_11|agi_15|int_6|cha_7|level(16), wpex(75,50,60,80,65,50), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_6|knows_athletics_6|knows_riding_2|knows_horse_archery_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Light infantry, spears, shields
  # SPECIAL
  ["swadian_light_spearman", "Swadian Light Spearman", "Swadian Light Spearmen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_15,
   [itm_war_spear, itm_tab_shield_heater_b,itm_tab_shield_heater_b_plain_1,itm_tab_shield_heater_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_cloth, itm_gambeson_herald, itm_leather_jerkin_herald, itm_padded_leather_herald,
    itm_footman_helmet, itm_mail_coif, itm_helmet_with_neckguard,
    ],
   str_15|agi_12|int_7|cha_7|level(18), wpex(90,80,130,60,50,40), knows_common|knows_ironflesh_3|knows_power_strike_5|knows_power_draw_1|knows_athletics_5|knows_riding_2, swadian_face_young_1, swadian_face_old_2 ],
  
  # Light cavalry, swords, picks, maces, lances, shields
  # SPECIAL
  ["swadian_light_horseman", "Swadian Light Horseman", "Swadian Light Horsemen", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_13,
   [itm_sword_medieval_b, itm_fighting_pick, itm_mace_3, itm_light_lance, itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a_plain_1,itm_tab_shield_heater_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_cloth, itm_gambeson_herald, itm_leather_jerkin_herald,
    itm_padded_coif, itm_mail_coif, itm_footman_helmet,
    itm_pack_horse],
   str_13|agi_16|int_8|cha_9|level(23), wpex(90,80,110,60,50,50), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_athletics_3|knows_riding_6, swadian_face_young_1, swadian_face_old_2 ],
  
  # Veteran
  # Heavy infantry, spears, shields
  ["swadian_pikeman", "Swadian Pikeman", "Swadian Pikemen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_awlpike, itm_tab_shield_heater_c,itm_tab_shield_heater_c_plain_1,itm_tab_shield_heater_c_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_haubergeon_herald, itm_mail_with_surcoat_herald,
    itm_flat_topped_helmet, itm_kettle_hat, itm_guard_helmet, itm_guard_helmet, itm_bascinet, itm_bascinet_b, itm_bascinet_c,
    ],
   str_20|agi_10|int_9|cha_8|level(24), wpex(90,80,110,60,50,40), knows_common|knows_ironflesh_6|knows_power_strike_3|knows_power_draw_1|knows_athletics_2|knows_riding_2|knows_shield_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Heavy infantry, swords, picks, maces, shields
  ["swadian_heavy_infantry", "Swadian Man-At-Arms", "Swadian Men-At-Arms", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_sword_medieval_c, itm_sword_medieval_c_small, itm_military_sickle_a, itm_mace_4, itm_tab_shield_heater_c,itm_tab_shield_heater_c_plain_1,itm_tab_shield_heater_c_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_haubergeon_herald, itm_mail_with_surcoat_herald,
    itm_kettle_hat, itm_flat_topped_helmet, itm_guard_helmet, itm_guard_helmet, itm_bascinet, itm_bascinet_b, itm_bascinet_c,
    ],
   str_19|agi_11|int_9|cha_10|level(26), wpex(120,90,105,65,55,50), knows_common|knows_ironflesh_6|knows_power_strike_3|knows_power_throw_1|knows_power_draw_2|knows_athletics_2|knows_riding_3|knows_shield_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Heavy infantry, 2h swords
  ["swadian_champion", "Swadian Champion", "Swadian Champions", tf_guarantee_trained_armor, no_scene, reserved, fac_kingdom_1,
   [itm_sword_two_handed_a,
    itm_mail_chausses, itm_mail_mittens,
    itm_mail_with_surcoat_herald,
    itm_guard_helmet, itm_guard_helmet, itm_bascinet, itm_bascinet_b, itm_bascinet_c, itm_kettle_hat,
    ],
   str_17|agi_13|int_10|cha_9|level(26), wpex(95,140,90,60,50,45), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_athletics_4|knows_riding_2, swadian_face_young_1, swadian_face_old_2 ],
  
  # Medium ranged, swords, picks, maces, bows, shields
  ["swadian_bowman", "Swadian Bowman", "Swadian Bowmen", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_fighting_pick, itm_mace_3, itm_sword_medieval_b, itm_sword_medieval_b_small, itm_bodkin_arrows, itm_short_bow2, itm_tab_shield_heater_b,itm_tab_shield_heater_b_plain_1,itm_tab_shield_heater_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_leather_herald, itm_haubergeon_herald,
    itm_mail_coif, itm_helmet_with_neckguard, itm_kettle_hat,
    ],
   str_12|agi_16|int_7|cha_8|level(20), wpex(85,50,60,125,70,55), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_4|knows_athletics_4|knows_riding_2|knows_horse_archery_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Medium ranged, swords, picks, maces, crossbows, shields
  ["swadian_crossbowman", "Swadian Crossbowman", "Swadian Crossbowmen", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_fighting_pick, itm_mace_3, itm_sword_medieval_b, itm_sword_medieval_b_small, itm_steel_bolts, itm_light_crossbow, itm_tab_shield_heater_b,itm_tab_shield_heater_b_plain_1,itm_tab_shield_heater_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_haubergeon_herald,
    itm_mail_coif, itm_helmet_with_neckguard, itm_kettle_hat,
    ],
   str_14|agi_14|int_8|cha_8|level(21), wpex(90,55,65,80,115,55), knows_common|knows_ironflesh_3|knows_power_strike_2|knows_power_draw_2|knows_athletics_3|knows_riding_2|knows_horse_archery_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Light cavalry, swords, picks, maces, shields
  ["swadian_light_cavalry", "Swadian Light Cavalry", "Swadian Light Cavalries", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_sword_medieval_b, itm_fighting_pick, itm_mace_3, itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a_plain_1,itm_tab_shield_heater_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_cloth, itm_gambeson_herald, itm_leather_jerkin_herald, itm_padded_leather_herald,
    itm_footman_helmet, itm_mail_coif, itm_helmet_with_neckguard, itm_norman_helmet,
    itm_pack_horse],
   str_14|agi_15|int_8|cha_10|level(24), wpex(110,85,100,60,50,50), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_power_draw_1|knows_athletics_4|knows_riding_6|knows_horse_archery_2, swadian_face_young_1, swadian_face_old_2 ],
  
  # Light cavalry ranged, swords, bows, crossbows, shields
  ["swadian_ranger", "Swadian Ranger", "Swadian Rangers", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_sword_medieval_b, itm_bolts, itm_light_crossbow, itm_barbed_arrows, itm_short_bow2, itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a_plain_1,itm_tab_shield_heater_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_cloth, itm_leather_armor_herald, itm_leather_jerkin_herald,
    itm_padded_coif, itm_mail_coif, itm_footman_helmet,
    itm_pack_horse],
   str_13|agi_18|int_9|cha_7|level(24), wpex(95,50,80,125,115,60), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_3|knows_riding_6|knows_horse_archery_4, swadian_face_young_1, swadian_face_old_2 ],
  
  # Light cavalry, lances, shields
  ["swadian_light_lancer", "Swadian Light Lancer", "Swadian Light Lancers", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_lance, itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a_plain_1,itm_tab_shield_heater_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_cloth, itm_leather_armor_herald, itm_gambeson_herald, itm_leather_jerkin_herald,
    itm_footman_helmet, itm_mail_coif, itm_helmet_with_neckguard,
    itm_courser],
   str_13|agi_17|int_7|cha_8|level(22), wpex(90,75,140,55,45,45), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_draw_1|knows_athletics_3|knows_riding_6|knows_horse_archery_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Medium ranged, swords, picks, maces, bows
  # SPECIAL
  ["swadian_longbowman", "Swadian Longbowman", "Swadian Longbowmen", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_14,
   [itm_fighting_pick, itm_mace_3, itm_sword_medieval_b, itm_sword_medieval_b_small, itm_long_bow2, itm_bodkin_arrows, itm_bodkin_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_haubergeon_herald,
    itm_mail_coif, itm_helmet_with_neckguard, itm_kettle_hat,
    ],
   str_14|agi_12|int_8|cha_9|level(20), wpex(85,50,60,75,70,55), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_6|knows_athletics_3|knows_riding_2|knows_horse_archery_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Heavy infantry, spears, shields
  # SPECIAL
  ["swadian_spearman", "Swadian Spearman", "Swadian Spearmen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_15,
   [itm_war_spear, itm_tab_shield_heater_c,itm_tab_shield_heater_c_plain_1,itm_tab_shield_heater_c_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_haubergeon_herald, itm_mail_with_surcoat_herald,
    itm_flat_topped_helmet, itm_kettle_hat, itm_guard_helmet, itm_guard_helmet, itm_bascinet, itm_bascinet_b, itm_bascinet_c,
    ],
   str_19|agi_10|int_9|cha_8|level(23), wpex(90,80,120,60,50,40), knows_common|knows_ironflesh_6|knows_power_strike_3|knows_power_draw_1|knows_athletics_3|knows_riding_2|knows_shield_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Heavy infantry, polearms
  # SPECIAL
  ["swadian_heavy_infantry", "Swadian Heavy Infantry", "Swadian Heavy Infantries", tf_guarantee_trained_armor, no_scene, reserved, fac_small_kingdom_12,
   [itm_voulge,
    itm_mail_chausses, itm_mail_mittens,
    itm_mail_with_surcoat_herald,
    itm_guard_helmet, itm_guard_helmet, itm_bascinet, itm_bascinet_b, itm_bascinet_c, itm_kettle_hat,
    ],
   str_18|agi_11|int_10|cha_9|level(25), wpex(95,100,115,60,50,45), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_athletics_4|knows_riding_2, swadian_face_young_1, swadian_face_old_2 ],
  
  # Heavy cavalry, lances, shields
  # SPECIAL
  ["swadian_lancer", "Swadian Lancer", "Swadian Lancers", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_13,
   [itm_lance, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_haubergeon_herald, itm_mail_with_surcoat_herald,
    itm_mail_coif, itm_helmet_with_neckguard, itm_kettle_hat,
    itm_hunter],
   str_14|agi_17|int_9|cha_10|level(27), wpex(90,75,140,55,45,45), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_power_draw_1|knows_athletics_2|knows_riding_5|knows_horse_archery_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Heavy cavalry, swords, picks, maces, lances, shields
  # SPECIAL
  ["swadian_horseman", "Swadian Horseman", "Swadian Horsemen", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_13,
   [itm_sword_medieval_c, itm_military_sickle_a, itm_mace_4, itm_lance, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_mail_chausses, itm_leather_gloves, itm_mail_mittens,
    itm_haubergeon_herald, itm_mail_with_surcoat_herald,
    itm_mail_coif, itm_helmet_with_neckguard, itm_kettle_hat,
    itm_hunter],
   str_14|agi_16|int_9|cha_12|level(28), wpex(95,95,120,60,50,55), knows_common|knows_ironflesh_6|knows_power_strike_3|knows_power_draw_1|knows_athletics_3|knows_riding_5|knows_horse_archery_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Elite
  # Heavy infantry, bastard swords, morningstars, shields
  ["swadian_sergeant", "Swadian Sergeant", "Swadian Sergeants", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_morningstar, itm_bastard_sword_b, itm_tab_shield_heater_d,itm_tab_shield_heater_d_plain_1,itm_tab_shield_heater_d_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_coat_of_plates_herald,
    itm_guard_helmet, itm_guard_helmet, itm_bascinet, itm_bascinet_b, itm_bascinet_c,
    ],
   str_24|agi_9|int_10|cha_11|level(31), wpex(115,120,95,65,55,50), knows_common|knows_ironflesh_9|knows_power_strike_4|knows_power_throw_1|knows_power_draw_2|knows_athletics_2|knows_riding_3|knows_shield_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Heavy cavalry, swords, picks, maces, bastard swords, shields
  ["swadian_heavy_cavalry", "Swadian Heavy Cavalry", "Swadian Heavy Cavalries", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_sword_medieval_c, itm_sword_medieval_c_long, itm_military_sickle_a, itm_mace_4, itm_bastard_sword_a, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_iron_greaves, itm_mail_boots, itm_mail_mittens,
    itm_mail_with_surcoat_herald, itm_coat_of_plates_herald,
    itm_guard_helmet, itm_guard_helmet, itm_bascinet, itm_bascinet_b, itm_bascinet_c,
    itm_hunter],
   str_16|agi_14|int_10|cha_15|level(32), wpex(110,115,80,60,50,55), knows_common|knows_ironflesh_8|knows_power_strike_3|knows_power_draw_1|knows_athletics_2|knows_riding_5|knows_shield_1|knows_horse_archery_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Heavy cavalry, lances, shields
  # SPECIAL
  ["swadian_heavy_lancer", "Swadian Heavy Lancer", "Swadian Heavy Lancers", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_13,
   [itm_heavy_lance, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_iron_greaves, itm_mail_boots, itm_mail_mittens,
    itm_mail_with_surcoat_herald, itm_coat_of_plates_herald,
    itm_guard_helmet, itm_guard_helmet, itm_bascinet, itm_bascinet_b, itm_bascinet_c,
    itm_hunter],
   str_17|agi_15|int_10|cha_14|level(33), wpex(100,105,130,60,50,55), knows_common|knows_ironflesh_9|knows_power_strike_3|knows_power_draw_1|knows_athletics_2|knows_riding_5|knows_shield_1|knows_horse_archery_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Heavy infantry, spears, shields
  # SPECIAL
  ["swadian_heavy_spearman", "Swadian Heavy Pikeman", "Swadian Heavy Pikemen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_11,
   [itm_awlpike_long, itm_tab_shield_heater_d,itm_tab_shield_heater_d_plain_1,itm_tab_shield_heater_d_plain_2,
    itm_iron_greaves, itm_mail_boots, itm_mail_mittens, itm_gauntlets,
    itm_coat_of_plates_herald,
    itm_guard_helmet, itm_guard_helmet, itm_bascinet, itm_bascinet_b, itm_bascinet_c,
    ],
   str_24|agi_9|int_10|cha_9|level(29), wpex(95,85,120,65,55,50), knows_common|knows_ironflesh_9|knows_power_strike_3|knows_power_draw_1|knows_athletics_2|knows_riding_2|knows_shield_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Medium ranged, swords, picks, maces, crossbows, shields
  # SPECIAL
  ["swadian_heavy_crossbowman", "Swadian Heavy Crossbowman", "Swadian Heavy Crossbowmen", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_11,
   [itm_military_sickle_a, itm_mace_4, itm_sword_medieval_c, itm_sword_medieval_c_small, itm_steel_bolts, itm_crossbow, itm_tab_shield_heater_c,itm_tab_shield_heater_c_plain_1,itm_tab_shield_heater_c_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_mail_with_surcoat_herald,
    itm_mail_coif, itm_helmet_with_neckguard, itm_kettle_hat,
    ],
   str_18|agi_14|int_10|cha_9|level(26), wpex(95,65,75,70,95,55), knows_common|knows_ironflesh_5|knows_power_strike_2|knows_power_draw_2|knows_athletics_1|knows_riding_2|knows_horse_archery_1|knows_shield_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Heavy cavalry, swords, maces, picks, 2h swords, shields
  # SPECIAL
  ["swadian_squire", "Swadian Squire", "Swadian Squires", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_17,
   [itm_sword_medieval_c, itm_sword_medieval_c_long, itm_military_sickle_a, itm_mace_4, itm_sword_two_handed_a, itm_sword_two_handed_a, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_haubergeon_herald, itm_mail_with_surcoat_herald,
    itm_mail_coif, itm_helmet_with_neckguard, itm_kettle_hat, itm_flat_topped_helmet,
    itm_hunter],
   str_15|agi_15|int_10|cha_13|level(30), wpex(95,115,95,60,50,55), knows_common|knows_ironflesh_6|knows_power_strike_3|knows_power_draw_1|knows_athletics_3|knows_riding_5|knows_horse_archery_1, swadian_face_young_1, swadian_face_old_2 ],
  
  # Heavy infantry, polearms, shields
  # SPECIAL
  ["swadian_guard", "Swadian Guard", "Swadian Guards", tf_guarantee_trained_armor, no_scene, reserved, fac_small_kingdom_12,
   [itm_voulge,
    itm_mail_boots, itm_mail_mittens,
    itm_coat_of_plates_herald,
    itm_guard_helmet, itm_guard_helmet, itm_bascinet, itm_bascinet_b, itm_bascinet_c,
    ],
   str_24|agi_10|int_11|cha_10|level(32), wpex(110,110,125,65,55,50), knows_common|knows_ironflesh_9|knows_power_strike_5|knows_power_throw_1|knows_power_draw_2|knows_athletics_3|knows_riding_3, swadian_face_young_1, swadian_face_old_2 ],
  
  # Noble
  # Heavy cavalry, swords, picks, maces, morningstars, lances, shields
  ["swadian_noble", "Swadian Knight", "Swadian Knights", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_sword_medieval_c, itm_sword_medieval_c_long, itm_military_sickle_a, itm_mace_4, itm_bastard_sword_b, itm_morningstar, itm_heavy_lance, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_iron_greaves, itm_mail_boots, itm_mail_mittens, itm_gauntlets,
    itm_coat_of_plates_herald, itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_tabard,
    itm_guard_helmet, itm_guard_helmet, itm_bascinet, itm_bascinet_b, itm_bascinet_c, itm_great_helmet_herald, itm_great_helmet_herald,
    itm_warhorse],
   str_22|agi_18|int_12|cha_20|level(49), wpex(125,120,150,80,70,65), knows_common|knows_ironflesh_8|knows_power_strike_4|knows_power_throw_1|knows_power_draw_3|knows_athletics_4|knows_riding_6|knows_shield_1|knows_horse_archery_2, swadian_face_young_1, swadian_face_old_2 ],
  
  # Heavy infantry, swords, picks, maces, morningstars, 2h swords, shields
  # SPECIAL
  ["swadian_foot_knight", "Swadian Foot Knight", "Swadian Foot Knights", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_17,
   [itm_sword_medieval_c, itm_sword_medieval_c_small, itm_military_sickle_a, itm_mace_4, itm_morningstar, itm_sword_two_handed_b, itm_sword_two_handed_b, itm_tab_shield_heater_d,itm_tab_shield_heater_d_plain_1,itm_tab_shield_heater_d_plain_2,
    itm_iron_greaves, itm_gauntlets,
    itm_coat_of_plates_herald, itm_plate_armor_herald,
    itm_great_helmet_herald, itm_guard_helmet,
    ],
   str_29|agi_15|int_12|cha_19|level(52), wpex(120,115,105,80,70,65), knows_common|knows_ironflesh_10|knows_power_strike_4|knows_power_throw_1|knows_power_draw_3|knows_athletics_3|knows_riding_5|knows_shield_1|knows_horse_archery_2, swadian_face_young_1, swadian_face_old_2 ],
  
  ###########
  # Vaegirs #
  ###########
  # Peasant
  # Basic infantry, spears, shields
  ["vaegir_levy", "Vaegir Levy Spearman", "Vaegir Levy Spearmen", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2,
   [itm_spear, itm_tab_shield_kite_a,itm_tab_shield_kite_a_plain_1,itm_tab_shield_kite_a_plain_2,
    itm_hide_boots, itm_nomad_boots,
    itm_fur_coat, itm_leather_vest_herald, itm_linen_tunic_herald,
    itm_vaegir_fur_cap, itm_leather_cap, itm_leather_warrior_cap,
    ],
   str_10|agi_8|int_5|cha_6|level(6), wpex(55,65,90,60,20,35), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_draw_1|knows_athletics_3|knows_riding_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Basic ranged, axes, daggers, bows
  ["vaegir_hunter", "Vaegir Hunter", "Vaegir Hunters", tf_guarantee_recruit_armor, no_scene, reserved, fac_kingdom_2,
   [itm_hatchet, itm_axe, itm_butchering_knife, itm_hunting_bow, itm_barbed_arrows,
    itm_nomad_boots, itm_hide_boots,
    itm_rawhide_coat, itm_leather_vest_herald, itm_linen_tunic_herald, itm_fur_coat,
    itm_vaegir_fur_cap, itm_leather_cap, itm_leather_warrior_cap,
    ],
   str_9|agi_8|int_6|cha_7|level(7), wpex(60,60,40,85,30,30), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_draw_4|knows_athletics_2|knows_riding_2|knows_horse_archery_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Basic infantry, clubs, shields
  # SPECIAL
  ["vaegir_club_levy", "Vaegir Club Levy", "Vaegir Club Levies", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_22,
   [itm_club, itm_spiked_club, itm_tab_shield_kite_a,itm_tab_shield_kite_a_plain_1,itm_tab_shield_kite_a_plain_2,
    itm_hide_boots, itm_nomad_boots,
    itm_fur_coat, itm_leather_vest_herald, itm_linen_tunic_herald,
    itm_vaegir_fur_cap, itm_leather_cap, itm_leather_warrior_cap,
    ],
   str_8|agi_9|int_5|cha_6|level(5), wpex(70,65,60,60,20,40), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_draw_1|knows_athletics_4|knows_riding_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Basic infantry, axes, shields
  # SPECIAL
  ["vaegir_levy_axeman", "Vaegir Levy Axeman", "Vaegir Levy Axemen", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_21,
   [itm_one_handed_war_axe_a, itm_tab_shield_kite_a,itm_tab_shield_kite_a_plain_1,itm_tab_shield_kite_a_plain_2,
    itm_hide_boots, itm_nomad_boots,
    itm_fur_coat, itm_leather_vest_herald, itm_linen_tunic_herald,
    itm_vaegir_fur_cap, itm_leather_cap, itm_leather_warrior_cap,
    ],
   str_10|agi_9|int_6|cha_6|level(8), wpex(75,70,65,60,20,40), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_draw_1|knows_athletics_4|knows_riding_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Basic infantry, axes, swords, shields
  # SPECIAL
  ["vaegir_levy_infantry", "Vaegir Levy", "Vaegir Levies", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_23,
   [itm_one_handed_war_axe_a, itm_sword_khergit_1, itm_tab_shield_kite_a,itm_tab_shield_kite_a_plain_1,itm_tab_shield_kite_a_plain_2,
    itm_hide_boots, itm_nomad_boots,
    itm_fur_coat, itm_leather_vest_herald, itm_linen_tunic_herald, itm_fur_coat, itm_rawhide_coat,
    itm_vaegir_fur_cap, itm_leather_cap, itm_leather_warrior_cap,
    ],
   str_9|agi_9|int_6|cha_6|level(7), wpex(65,60,55,55,20,40), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_draw_1|knows_athletics_4|knows_riding_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Basic ranged, axes, daggers, bows
  # SPECIAL
  ["vaegir_militia", "Vaegir Militia", "Vaegir Militias", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_23,
   [itm_hatchet, itm_butchering_knife, itm_hunting_bow, itm_barbed_arrows,
    itm_nomad_boots, itm_hide_boots,
    itm_leather_vest_herald, itm_linen_tunic_herald,
    itm_vaegir_fur_cap, itm_leather_cap, itm_leather_warrior_cap,
    ],
   str_8|agi_8|int_6|cha_6|level(5), wpex(55,50,45,75,20,40), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_3|knows_riding_2|knows_horse_archery_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Common
  # Light infantry, sabres, axes, 2h axes, shields
  ["vaegir_light_infantry", "Vaegir Light Infantry", "Vaegir Light Infantries", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2,
   [itm_sword_khergit_1, itm_one_handed_battle_axe_a, itm_two_handed_axe, itm_tab_shield_kite_b,itm_tab_shield_kite_b_plain_1,itm_tab_shield_kite_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald, itm_leather_vest_herald,
    itm_vaegir_fur_cap, itm_vaegir_fur_helmet, itm_vaegir_spiked_helmet,
    ],
   str_12|agi_15|int_6|cha_6|level(16), wpex(105,100,85,60,20,45), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_athletics_5|knows_riding_3, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Light ranged, sabres, bows
  ["vaegir_light_bowman", "Vaegir Light Bowman", "Vaegir Light Bowmen", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2,
   [itm_sword_khergit_1, itm_short_bow, itm_barbed_arrows, itm_barbed_arrows,
    itm_nomad_boots, itm_leather_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_linen_tunic_herald,
    itm_vaegir_fur_cap,
    ],
   str_9|agi_15|int_6|cha_8|level(15), wpex(70,60,40,150,35,30), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_6|knows_riding_2|knows_horse_archery_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Light cavalry skirmisher, sabres, axes, javelins
  ["vaegir_mounted_skirmisher", "Vaegir Mounted Skirmisher", "Vaegir Mounted Skirmishers", tf_guarantee_common_armor|tf_guarantee_shield|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2,
   [itm_sword_khergit_1, itm_one_handed_battle_axe_a, itm_javelin, itm_javelin, itm_tab_shield_kite_cav_a,itm_tab_shield_kite_cav_a_plain_1,itm_tab_shield_kite_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_leather_jerkin_herald,
    itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    itm_steppe_horse],
   str_9|agi_16|int_7|cha_8|level(17), wpex(85,80,75,65,20,100), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_3|knows_power_draw_1|knows_athletics_5|knows_riding_6|knows_horse_archery_4, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Light cavalry, sabres, axes, lances, shields
  ["vaegir_light_cavalry", "Vaegir Light Cavalry", "Vaegir Light Cavalries", tf_guarantee_common_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_2,
   [itm_scimitar, itm_one_handed_battle_axe_a, itm_light_lance, itm_tab_shield_kite_cav_a,itm_tab_shield_kite_cav_a_plain_1,itm_tab_shield_kite_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald, itm_tribal_warrior_outfit,
    itm_vaegir_spiked_helmet, itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    itm_steppe_horse, itm_pack_horse],
   str_11|agi_15|int_7|cha_9|level(19), wpex(100,90,120,60,20,50), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_athletics_4|knows_riding_6|knows_horse_archery_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Light infantry skirmisher, sabres, axes, javelins, shields
  # SPECIAL
  ["vaegir_light_skirmisher", "Vaegir Light Skirmisher", "Vaegir Light Skirmishers", tf_guarantee_common_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_24,
   [itm_sword_khergit_1, itm_one_handed_battle_axe_a, itm_javelin, itm_javelin, itm_tab_shield_kite_b,itm_tab_shield_kite_b_plain_1,itm_tab_shield_kite_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_leather_jerkin_herald,
    itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    ],
   str_10|agi_16|int_6|cha_7|level(16), wpex(95,90,85,65,20,105), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_3|knows_power_draw_1|knows_athletics_6|knows_riding_3|knows_horse_archery_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Light cavalry ranged, sabres, axes, bows, shields,
  # SPECIAL
  ["vaegir_scout", "Vaegir Scout", "Vaegir Scouts", tf_guarantee_common_armor|tf_guarantee_shield|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_25,
   [itm_sword_khergit_1, itm_one_handed_battle_axe_a, itm_mace_2, itm_short_bow, itm_barbed_arrows, itm_tab_shield_kite_cav_a,itm_tab_shield_kite_cav_a_plain_1,itm_tab_shield_kite_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald, itm_leather_vest_herald,
    itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    itm_steppe_horse],
   str_10|agi_15|int_7|cha_8|level(17), wpex(75,75,70,130,35,30), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_throw_1|knows_power_draw_4|knows_athletics_4|knows_riding_6|knows_horse_archery_5, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Medium infantry, sabres, axes, shields
  # SPECIAL
  ["vaegir_footman", "Vaegir Footman", "Vaegir Footman", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_23,
   [itm_scimitar, itm_one_handed_battle_axe_a, itm_tab_shield_kite_b,itm_tab_shield_kite_b_plain_1,itm_tab_shield_kite_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_tribal_warrior_outfit, itm_studded_leather_coat_herald,
    itm_vaegir_fur_cap, itm_vaegir_fur_helmet, itm_vaegir_spiked_helmet,
    ],
   str_13|agi_14|int_7|cha_8|level(19), wpex(100,95,90,60,20,45), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_athletics_4|knows_riding_3, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Light infantry, maces, shields
  # SPECIAL
  ["vaegir_light_club_infantry", "Vaegir Light Club Infantry", "Vaegir Light Club Infantries", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_22,
   [itm_mace_2, itm_tab_shield_kite_b,itm_tab_shield_kite_b_plain_1,itm_tab_shield_kite_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_tribal_warrior_outfit,
    itm_vaegir_fur_cap, itm_vaegir_fur_helmet, itm_vaegir_spiked_helmet,
    ],
   str_15|agi_12|int_7|cha_7|level(18), wpex(100,95,90,60,20,45), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_athletics_5|knows_riding_3, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Veteran
  # Medium infantry, sabres, shields
  ["vaegir_heavy_infantry", "Vaegir Heavy Infantry", "Vaegir Heavy Infantries", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2,
   [itm_scimitar, itm_tab_shield_kite_c,itm_tab_shield_kite_c_plain_1,itm_tab_shield_kite_c_plain_2,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_mail_hauberk_herald, itm_studded_leather_coat_herald, itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet, itm_vaegir_fur_helmet, itm_vaegir_helmet, itm_vaegir_spiked_helmet,
    ],
   str_15|agi_15|int_7|cha_8|level(22), wpex(115,110,105,65,25,50), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_athletics_4|knows_riding_2|knows_shield_1, vaegir_face_young_1, vaegir_face_old_2 ],
   
  # Medium infantry, spears, shields
  ["vaegir_spearman", "Vaegir Spearman", "Vaegir Spearmen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2,
   [itm_war_spear, itm_tab_shield_kite_c,itm_tab_shield_kite_c_plain_1,itm_tab_shield_kite_c_plain_2,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_mail_hauberk_herald, itm_studded_leather_coat_herald, itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet, itm_vaegir_fur_helmet, itm_vaegir_helmet, itm_vaegir_spiked_helmet,
    ],
   str_14|agi_16|int_8|cha_6|level(21), wpex(100,90,130,65,25,45), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_athletics_4|knows_riding_1|knows_shield_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Medium infantry skirmisher, 2h axes, javelins, shields
  ["vaegir_skirmisher", "Vaegir Skirmisher", "Vaegir Skirmishers", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2,
   [itm_two_handed_axe, itm_javelin, itm_javelin, itm_tab_shield_kite_b,itm_tab_shield_kite_b_plain_1,itm_tab_shield_kite_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_studded_leather_coat_herald, itm_tribal_warrior_outfit,
    itm_vaegir_spiked_helmet, itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    ],
   str_13|agi_15|int_7|cha_8|level(20), wpex(90,100,85,70,20,105), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_3|knows_power_draw_1|knows_athletics_4|knows_riding_2|knows_horse_archery_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Light ranged, sabres, bows
  ["vaegir_medium_bowman", "Vaegir Bowman", "Vaegir Bowmen", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2,
   [itm_scimitar, itm_strong_bow, itm_bodkin_arrows, itm_bodkin_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    ],
   str_12|agi_16|int_7|cha_10|level(22), wpex(80,60,40,135,40,30), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_5|knows_athletics_5|knows_riding_2|knows_horse_archery_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Medium cavalry, sabres, 2h axes, shields
  ["vaegir_heavy_cavalry", "Vaegir Heavy Cavalry", "Vaegir Heavy Cavalries", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_2,
   [itm_scimitar_b, itm_bardiche, itm_tab_shield_kite_cav_b,itm_tab_shield_kite_cav_b_plain_1,itm_tab_shield_kite_cav_b_plain_2,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_mail_hauberk_herald, itm_studded_leather_coat_herald, itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet, itm_vaegir_spiked_helmet, itm_vaegir_fur_helmet,
    itm_hunter],
   str_14|agi_16|int_7|cha_11|level(25), wpex(100,120,80,65,20,50), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_athletics_3|knows_riding_5|knows_horse_archery_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Light cavalry, lances, javelins, shields
  ["vaegir_light_lancer", "Vaegir Light Lancer", "Vaegir Light Lancers", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_2,
   [itm_lance, itm_javelin, itm_tab_shield_kite_cav_a,itm_tab_shield_kite_cav_a_plain_1,itm_tab_shield_kite_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_leather_jerkin_herald, itm_tribal_warrior_outfit,
    itm_vaegir_spiked_helmet, itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    itm_steppe_horse, itm_courser],
   str_13|agi_15|int_7|cha_8|level(20), wpex(90,80,135,60,25,90), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_2|knows_power_draw_1|knows_athletics_3|knows_riding_6|knows_horse_archery_3, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Light cavalry ranged, sabres, bows
  ["vaegir_mounted_bowman", "Vaegir Mounted Bowman", "Vaegir Mounted Bowmen", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2,
   [itm_scimitar, itm_nomad_bow, itm_bodkin_arrows, itm_bodkin_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_leather_jerkin_herald,
    itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    itm_steppe_horse],
   str_12|agi_15|int_9|cha_10|level(23), wpex(80,60,40,135,40,40), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_5|knows_athletics_4|knows_riding_6|knows_horse_archery_6, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Medium infantry, 2h axes
  # SPECIAL
  ["vaegir_champion", "Vaegir Champion", "Vaegir Champions", tf_guarantee_trained_armor, no_scene, reserved, fac_small_kingdom_24,
   [itm_bardiche,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_mail_hauberk_herald, itm_studded_leather_coat_herald, itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet, itm_vaegir_spiked_helmet, itm_vaegir_fur_helmet,
    ],
   str_15|agi_15|int_8|cha_9|level(24), wpex(100,130,80,65,20,50), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_athletics_5|knows_riding_2, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Heavy infantry, pikes
  # SPECIAL
  ["vaegir_pikeman", "Vaegir Pikeman", "Vaegir Pikemen", tf_guarantee_trained_armor, no_scene, reserved, fac_small_kingdom_25,
   [itm_ashwood_pike,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_mail_hauberk_herald, itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet, itm_vaegir_spiked_helmet, itm_vaegir_fur_helmet,
    ],
   str_15|agi_13|int_8|cha_9|level(22), wpex(95,90,135,70,25,50), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_1|knows_power_draw_2|knows_athletics_5|knows_riding_2, vaegir_face_young_1, vaegir_face_old_2 ],
  
   # Medium cavalry, sabres, axes, shields
   # SPECIAL
  ["vaegir_horseman", "Vaegir Horseman", "Vaegir Horsemen", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_22,
   [itm_scimitar, itm_one_handed_battle_axe_a, itm_mace_3, itm_tab_shield_kite_cav_b,itm_tab_shield_kite_cav_b_plain_1,itm_tab_shield_kite_cav_b_plain_2,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_mail_hauberk_herald, itm_studded_leather_coat_herald, itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet, itm_vaegir_spiked_helmet, itm_vaegir_fur_helmet,
    itm_hunter],
   str_15|agi_15|int_7|cha_10|level(24), wpex(110,110,105,65,20,50), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_athletics_3|knows_riding_5|knows_horse_archery_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Light ranged, sabres, bows
  # SPECIAL
  ["vaegir_medium_longbowman", "Vaegir Longbowman", "Vaegir Longbowmen", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_25,
   [itm_scimitar, itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald, itm_tribal_warrior_outfit,
    itm_vaegir_spiked_helmet, itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    ],
   str_13|agi_16|int_7|cha_10|level(23), wpex(80,60,40,120,40,30), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_6|knows_athletics_5|knows_riding_2|knows_horse_archery_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Light cavalry ranged, sabres, bows
  # SPECIAL
  ["vaegir_mounted_longbowman", "Vaegir Mounted Longbowman", "Vaegir Mounted Longbowmen", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_25,
   [itm_scimitar, itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_leather_jerkin_herald,
    itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    itm_steppe_horse],
   str_13|agi_15|int_9|cha_10|level(24), wpex(80,60,40,115,40,40), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_6|knows_athletics_4|knows_riding_6|knows_horse_archery_6, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Medium infantry, sabres, axes, shields
  # SPECIAL
  ["vaegir_heavy_footman", "Vaegir Heavy Footman", "Vaegir Heavy Footmen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_23,
   [itm_scimitar_b, itm_one_handed_war_axe_b, itm_tab_shield_kite_c,itm_tab_shield_kite_c_plain_1,itm_tab_shield_kite_c_plain_2,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_mail_hauberk_herald, itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet, itm_vaegir_fur_helmet, itm_vaegir_helmet, itm_vaegir_spiked_helmet,
    ],
   str_16|agi_14|int_8|cha_9|level(24), wpex(105,100,100,65,25,50), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_athletics_4|knows_riding_2|knows_shield_1, vaegir_face_young_1, vaegir_face_old_2 ],
   
  # Light cavalry ranged, sabres, axes, bows, shields
  # SPECIAL
  ["vaegir_hussar", "Vaegir Hussar", "Vaegir Hussars", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_21,
   [itm_scimitar, itm_one_handed_battle_axe_a, itm_nomad_bow, itm_bodkin_arrows, itm_tab_shield_kite_cav_a,itm_tab_shield_kite_cav_a_plain_1,itm_tab_shield_kite_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald, itm_tribal_warrior_outfit,
    itm_vaegir_spiked_helmet, itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    itm_steppe_horse],
   str_13|agi_15|int_9|cha_11|level(25), wpex(95,105,60,120,40,40), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_5|knows_athletics_4|knows_riding_6|knows_horse_archery_5, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Medium infantry, maces, shields
  # SPECIAL
  ["vaegir_club_infantry", "Vaegir Club Infantry", "Vaegir Club Infantries", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_22,
   [itm_mace_3, itm_tab_shield_kite_c,itm_tab_shield_kite_c_plain_1,itm_tab_shield_kite_c_plain_2,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_mail_hauberk_herald, itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet, itm_vaegir_fur_helmet, itm_vaegir_helmet, itm_vaegir_spiked_helmet,
    ],
   str_18|agi_13|int_8|cha_8|level(24), wpex(105,100,95,65,25,50), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_athletics_4|knows_riding_2|knows_shield_1, vaegir_face_young_1, vaegir_face_old_2 ],
   
  # Elite
  # Heavy infantry, poleaxes
  ["vaegir_guard", "Vaegir Guard", "Vaegir Guards", tf_guarantee_trained_armor, no_scene, reserved, fac_kingdom_2,
   [itm_long_bardiche,
    itm_mail_boots, itm_iron_greaves, itm_mail_mittens,
    itm_lamellar_armor_herald, itm_banded_armor,
    itm_vaegir_helmet, itm_vaegir_noble_helmet, itm_vaegir_lamellar_helmet,
    ],
   str_18|agi_15|int_8|cha_10|level(28), wpex(110,105,145,75,25,50), knows_common|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_1|knows_power_draw_2|knows_athletics_5|knows_riding_2, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Medium ranged, sabres, bows, shields
  ["vaegir_heavy_longbowman", "Vaegir Heavy Longbowman", "Vaegir Heavy Longbowmen", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2,
   [itm_scimitar, itm_war_bow, itm_bodkin_arrows, itm_tab_shield_kite_c,itm_tab_shield_kite_c_plain_1,itm_tab_shield_kite_c_plain_2,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_studded_leather_coat_herald, itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet, itm_vaegir_spiked_helmet, itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    ],
   str_17|agi_14|int_8|cha_12|level(28), wpex(90,60,40,110,40,40), knows_common|knows_ironflesh_3|knows_power_strike_2|knows_power_draw_6|knows_athletics_4|knows_riding_2|knows_horse_archery_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Heavy cavalry, lances, shields
  # SPECIAL
  ["vaegir_heavy_lancer", "Vaegir Heavy Lancer", "Vaegir Heavy Lancers", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_21,
   [itm_heavy_lance, itm_tab_shield_kite_cav_b,itm_tab_shield_kite_cav_b_plain_1,itm_tab_shield_kite_cav_b_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_mail_hauberk_herald, itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet, itm_vaegir_helmet,
    itm_hunter],
   str_16|agi_16|int_8|cha_11|level(28), wpex(100,105,135,75,25,55), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_1|knows_power_draw_1|knows_athletics_3|knows_riding_5|knows_horse_archery_1, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Heavy cavalry ranged, sabres, bows
  # SPECIAL
  ["vaegir_heavy_mounted_longbowman", "Vaegir Heavy Mounted Longbowman", "Vaegir Heavy Mounted Longbowmen", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_25,
   [itm_scimitar, itm_war_bow, itm_bodkin_arrows,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet, itm_vaegir_spiked_helmet, itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    itm_hunter],
   str_16|agi_15|int_9|cha_13|level(30), wpex(90,60,40,105,40,40), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_6|knows_athletics_3|knows_riding_5|knows_horse_archery_5, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Heavy infantry, pikes
  # SPECIAL
  ["vaegir_heavy_pikeman", "Vaegir Heavy Pikeman", "Vaegir Heavy Pikemen", tf_guarantee_trained_armor, no_scene, reserved, fac_small_kingdom_25,
   [itm_ashwood_pike,
    itm_mail_boots, itm_iron_greaves, itm_mail_mittens,
    itm_lamellar_armor_herald, itm_banded_armor,
    itm_vaegir_helmet, itm_vaegir_noble_helmet, itm_vaegir_lamellar_helmet,
    ],
   str_20|agi_14|int_9|cha_10|level(30), wpex(105,100,125,75,25,55), knows_common|knows_ironflesh_6|knows_power_strike_4|knows_power_throw_1|knows_power_draw_2|knows_athletics_4|knows_riding_2, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Medium infantry skirmisher, sabres, javelins, shields
  # SPECIAL
  ["vaegir_heavy_skirmisher", "Vaegir Heavy Skirmisher", "Vaegir Heavy Skirmishers", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_24,
   [itm_scimitar_b, itm_throwing_spears, itm_throwing_spears, itm_tab_shield_kite_d,itm_tab_shield_kite_d_plain_1,itm_tab_shield_kite_d_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_mail_hauberk_herald, itm_studded_leather_coat_herald, itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet, itm_vaegir_fur_helmet, itm_vaegir_helmet, itm_vaegir_spiked_helmet,
    ],
   str_15|agi_16|int_9|cha_9|level(26), wpex(105,95,90,65,25,90), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_3|knows_power_draw_1|knows_athletics_4|knows_riding_2|knows_shield_1, vaegir_face_young_1, vaegir_face_old_2 ],
   
  # Heavy infantry, sabres, axes, shields
  # SPECIAL
  ["vaegir_warrior", "Vaegir Warrior", "Vaegir Warriors", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_23,
   [itm_scimitar_b, itm_one_handed_war_axe_b, itm_tab_shield_kite_d,itm_tab_shield_kite_d_plain_1,itm_tab_shield_kite_d_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_lamellar_armor_herald, itm_banded_armor,
    itm_vaegir_helmet, itm_vaegir_noble_helmet, itm_vaegir_lamellar_helmet,
    ],
   str_19|agi_14|int_9|cha_12|level(31), wpex(125,115,110,75,25,50), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_power_throw_1|knows_power_draw_2|knows_athletics_3|knows_riding_2, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Heavy cavalry ranged, sabres, axes, bows, shields
  # SPECIAL
  ["vaegir_heavy_hussar", "Vaegir Heavy Hussar", "Vaegir Heavy Hussars", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_21,
   [itm_scimitar_b, itm_one_handed_war_axe_b, itm_strong_bow, itm_bodkin_arrows, itm_tab_shield_kite_cav_b,itm_tab_shield_kite_cav_b_plain_1,itm_tab_shield_kite_cav_b_plain_2,
    itm_mail_chausses, itm_leather_gloves, itm_mail_mittens,
    itm_mail_hauberk_herald, itm_studded_leather_coat_herald, itm_lamellar_vest_herald,
    itm_vaegir_lamellar_helmet, itm_vaegir_fur_helmet, itm_vaegir_helmet, itm_vaegir_spiked_helmet,
    itm_hunter],
   str_17|agi_15|int_9|cha_13|level(31), wpex(100,110,60,110,40,40), knows_common|knows_ironflesh_3|knows_power_strike_2|knows_power_draw_5|knows_athletics_3|knows_riding_5|knows_horse_archery_4, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Heavy infantry, maces, shields
  # SPECIAL
  ["vaegir_heavy_club_infantry", "Vaegir Heavy Club Infantry", "Vaegir Heavy Club Infantries", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_22,
   [itm_mace_4, itm_tab_shield_kite_d,itm_tab_shield_kite_d_plain_1,itm_tab_shield_kite_d_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_lamellar_armor_herald, itm_banded_armor,
    itm_vaegir_helmet, itm_vaegir_noble_helmet, itm_vaegir_lamellar_helmet,
    ],
   str_21|agi_14|int_9|cha_11|level(32), wpex(110,105,100,75,25,50), knows_common|knows_ironflesh_7|knows_power_strike_3|knows_power_throw_1|knows_power_draw_2|knows_athletics_3|knows_riding_2, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Noble
  # Heavy cavalry ranged, sabres, 2h axes, bows, shields
  ["vaegir_royal_hussar", "Vaegir Royal Hussar", "Vaegir Royal Hussars", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2,
   [itm_scimitar_b, itm_bardiche, itm_strong_bow, itm_bodkin_arrows, itm_tab_shield_kite_cav_b,itm_tab_shield_kite_cav_b_plain_1,itm_tab_shield_kite_cav_b_plain_2,
    itm_mail_boots, itm_iron_greaves, itm_mail_mittens,
    itm_brigandine_red_herald, itm_banded_armor, itm_lamellar_armor_herald,
    itm_vaegir_war_helmet, itm_vaegir_noble_helmet, itm_vaegir_helmet,
    itm_hunter],
   str_18|agi_20|int_10|cha_17|level(42), wpex(110,145,110,130,40,80), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_1|knows_power_draw_5|knows_athletics_5|knows_riding_6|knows_shield_1|knows_horse_archery_5, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Heavy ranged, sabres, bows, shields
  # SPECIAL
  ["vaegir_royal_longbowman", "Vaegir Royal Longbowman", "Vaegir Royal Longbowmen", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_25,
   [itm_scimitar_b, itm_war_bow, itm_bodkin_arrows, itm_tab_shield_kite_d,itm_tab_shield_kite_d_plain_1,itm_tab_shield_kite_d_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_brigandine_red_herald, itm_banded_armor, itm_lamellar_armor_herald,
    itm_vaegir_war_helmet, itm_vaegir_noble_helmet, itm_vaegir_helmet,
    ],
   str_17|agi_21|int_12|cha_18|level(45), wpex(115,110,100,120,45,80), knows_common|knows_ironflesh_6|knows_power_strike_4|knows_power_throw_1|knows_power_draw_7|knows_athletics_5|knows_riding_4|knows_shield_1|knows_horse_archery_4, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Heavy cavalry, lances, shields
  # SPECIAL
  ["vaegir_royal_lancer", "Vaegir Royal Lancer", "Vaegir Royal Lancer", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_21,
   [itm_heavy_lance, itm_tab_shield_kite_cav_b,itm_tab_shield_kite_cav_b_plain_1,itm_tab_shield_kite_cav_b_plain_2,
    itm_mail_boots, itm_iron_greaves, itm_mail_mittens,
    itm_banded_armor, itm_lamellar_armor_herald,
    itm_vaegir_war_helmet, itm_vaegir_noble_helmet, itm_vaegir_helmet,
    itm_warhorse],
   str_19|agi_20|int_12|cha_16|level(44), wpex(110,115,145,85,40,80), knows_common|knows_ironflesh_6|knows_power_strike_5|knows_power_throw_1|knows_power_draw_4|knows_athletics_4|knows_riding_6|knows_shield_1|knows_horse_archery_2, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Heavy cavalry, sabres, 2h axes, lances, shields
  # SPECIAL
  ["vaegir_royal_horseman", "Vaegir Royal Horseman", "Vaegir Royal Horsemen", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_22,
   [itm_scimitar_b, itm_bardiche, itm_heavy_lance, itm_tab_shield_kite_cav_b,itm_tab_shield_kite_cav_b_plain_1,itm_tab_shield_kite_cav_b_plain_2,
    itm_mail_boots, itm_iron_greaves, itm_mail_mittens,
    itm_banded_armor, itm_lamellar_armor_herald,
    itm_vaegir_war_helmet, itm_vaegir_noble_helmet, itm_vaegir_helmet,
    itm_hunter],
   str_17|agi_19|int_10|cha_16|level(39), wpex(115,140,145,85,40,80), knows_common|knows_ironflesh_6|knows_power_strike_5|knows_power_throw_1|knows_power_draw_4|knows_athletics_4|knows_riding_6|knows_shield_1|knows_horse_archery_2, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Heavy cavalry ranged, sabres, bows, shields
  # SPECIAL
  ["vaegir_royal_mounted_longbowman", "Vaegir Royal Mounted Longbowman", "Vaegir Royal Mounted Longbowmen", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_25,
   [itm_scimitar_b, itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows,
    itm_mail_boots, itm_iron_greaves, itm_mail_mittens,
    itm_brigandine_red_herald, itm_banded_armor, itm_lamellar_armor_herald,
    itm_vaegir_war_helmet, itm_vaegir_noble_helmet, itm_vaegir_helmet,
    itm_hunter],
   str_18|agi_20|int_10|cha_18|level(43), wpex(100,80,60,115,40,80), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_1|knows_power_draw_7|knows_athletics_5|knows_riding_6|knows_shield_1|knows_horse_archery_7, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Heavy cavalry skirmisher, sabres, 2h axes, javelins, shields
  # SPECIAL
  ["vaegir_royal_skirmisher", "Vaegir Royal Skirmisher", "Vaegir Royal Skirmishers", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_24,
   [itm_scimitar_b, itm_bardiche, itm_throwing_spears, itm_throwing_spears, itm_tab_shield_kite_cav_b,itm_tab_shield_kite_cav_b_plain_1,itm_tab_shield_kite_cav_b_plain_2,
    itm_mail_boots, itm_iron_greaves, itm_mail_mittens,
    itm_brigandine_red_herald, itm_banded_armor, itm_lamellar_armor_herald,
    itm_vaegir_war_helmet, itm_vaegir_noble_helmet, itm_vaegir_helmet,
    itm_hunter],
   str_19|agi_19|int_10|cha_16|level(41), wpex(110,145,110,85,40,115), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_3|knows_power_draw_4|knows_athletics_5|knows_riding_6|knows_shield_1|knows_horse_archery_6, vaegir_face_young_1, vaegir_face_old_2 ],
  
  # Heavy cavalry, sabres, 2h axes, lances, shields
  ["vaegir_knight", "Vaegir Knight", "Vaegir Knights", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_23,
   [itm_scimitar_b, itm_bardiche, itm_heavy_lance, itm_tab_shield_kite_cav_b,itm_tab_shield_kite_cav_b_plain_1,itm_tab_shield_kite_cav_b_plain_2,
    itm_mail_boots, itm_iron_greaves, itm_mail_mittens,
    itm_brigandine_red_herald, itm_banded_armor, itm_lamellar_armor_herald,
    itm_vaegir_war_helmet, itm_vaegir_noble_helmet, itm_vaegir_helmet,
    itm_warhorse],
   str_21|agi_20|int_13|cha_16|level(48), wpex(115,135,130,85,40,80), knows_common|knows_ironflesh_6|knows_power_strike_4|knows_power_throw_1|knows_power_draw_4|knows_athletics_4|knows_riding_6|knows_shield_1|knows_horse_archery_2, vaegir_face_young_1, vaegir_face_old_2 ],
  
  ############
  # Khergits #
  ############
  # Peasant
  # Basic infantry, spears
  ["khergit_levy", "Khergit Levy Spearman", "Khergit Levy Spearmen", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3,
   [itm_shortened_spear, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_nomad_boots, itm_hide_boots,
    itm_leather_vest_herald, itm_coarse_tunic_herald,
    itm_nomad_cap_b, itm_nomad_cap, itm_leather_steppe_cap_a, itm_leather_steppe_cap_c,
    ],
   str_9|agi_9|int_5|cha_5|level(5), wpex(60,50,80,50,20,40), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_draw_1|knows_athletics_3|knows_riding_2, khergit_face_young_1, khergit_face_old_2 ],
  
  # Basic ranged, maces, bows
  ["khergit_militia", "Khergit Tribesman", "Khergit Tribesmen", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3,
   [itm_club, itm_butchering_knife, itm_knife, itm_hunting_bow, itm_arrows_b, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_nomad_boots, itm_hide_boots,
    itm_leather_vest_herald, itm_coarse_tunic_herald,
    itm_nomad_cap_b, itm_nomad_cap, itm_leather_steppe_cap_a, itm_leather_steppe_cap_c,
    ],
   str_9|agi_9|int_6|cha_6|level(7), wpex(65,50,50,75,30,45), knows_common|knows_power_strike_2|knows_power_draw_4|knows_athletics_3|knows_riding_2|knows_horse_archery_1, khergit_face_young_1, khergit_face_old_2 ],
  
  # Basic cavalry ranged, lances, bows
  # SPECIAL
  ["khergit_clansman", "Khergit Clansman", "Khergit Clansman", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_34,
   [itm_light_lance, itm_hunting_bow, itm_arrows_b, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_nomad_boots, itm_hide_boots,
    itm_leather_vest_herald, itm_coarse_tunic_herald,
    itm_nomad_cap_b, itm_nomad_cap, itm_leather_steppe_cap_a, itm_leather_steppe_cap_c,
    itm_steppe_horse],
   str_9|agi_11|int_5|cha_7|level(9), wpex(55,50,70,60,30,45), knows_common|knows_power_strike_3|knows_power_draw_4|knows_athletics_2|knows_riding_5|knows_horse_archery_2, khergit_face_young_1, khergit_face_old_2 ],
  
  # Basic cavalry, spears
  # SPECIAL
  ["khergit_levy_horseman", "Khergit Levy Horseman", "Khergit Levy Horsemen", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_35,
   [itm_shortened_spear, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_nomad_boots, itm_hide_boots,
    itm_leather_vest_herald, itm_coarse_tunic_herald,
    itm_nomad_cap_b, itm_nomad_cap, itm_leather_steppe_cap_a, itm_leather_steppe_cap_c,
    itm_steppe_horse],
   str_9|agi_9|int_5|cha_7|level(7), wpex(55,50,65,50,30,45), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_1|knows_athletics_3|knows_riding_5|knows_horse_archery_1, khergit_face_young_1, khergit_face_old_2 ],
  
  # Basic infantry, swords, shields
  # SPECIAL
  ["khergit_levy_infantry", "Khergit Levy Infantry", "Khergit Levy Infantries", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_36,
   [itm_sword_khergit_1, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_nomad_boots, itm_hide_boots,
    itm_leather_vest_herald, itm_coarse_tunic_herald,
    itm_nomad_cap_b, itm_nomad_cap, itm_leather_steppe_cap_a, itm_leather_steppe_cap_c,
    ],
   str_8|agi_10|int_5|cha_6|level(6), wpex(65,55,70,50,20,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_athletics_4|knows_riding_2, khergit_face_young_1, khergit_face_old_2 ],

  # Common
  # Light infantry, sabres, maces, javelins, shields
  ["khergit_light_infantry", "Khergit Light Infantry", "Khergit Light Infantries", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3,
   [itm_sword_khergit_2, itm_winged_mace, itm_javelin, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_nomad_boots, itm_leather_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_steppe_armor_herald,
    itm_leather_steppe_cap_b, itm_leather_steppe_cap_c, itm_steppe_cap,
    ],
   str_10|agi_15|int_7|cha_6|level(15), wpex(100,80,95,60,20,80), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_athletics_4|knows_riding_3|knows_shield_1|knows_horse_archery_1, khergit_face_young_1, khergit_face_old_2 ],
  
  # Light infantry skirmisher, sabres, maces, javelins, bows, shields
  ["khergit_skirmisher", "Khergit Skirmisher", "Khergit Skirmishers", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3,
   [itm_sword_khergit_1, itm_javelin, itm_javelin, itm_short_bow, itm_barbed_arrows, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_leather_boots, itm_nomad_boots, itm_hide_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_steppe_armor_herald,
    itm_leather_steppe_cap_b, itm_leather_steppe_cap_c, itm_steppe_cap,
    ],
   str_10|agi_15|int_7|cha_7|level(16), wpex(90,75,85,120,30,100), knows_common|knows_power_strike_2|knows_power_throw_3|knows_power_draw_4|knows_athletics_5|knows_riding_3|knows_horse_archery_2, khergit_face_young_1, khergit_face_old_2 ],
  
  # Light cavalry, sabres, maces, javelins, shields
  ["khergit_light_cavalry", "Khergit Light Cavalry", "Khergit Light Cavalries", tf_guarantee_common_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3,
   [itm_sword_khergit_2, itm_winged_mace, itm_javelin, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_steppe_armor_herald,
    itm_leather_steppe_cap_b, itm_steppe_cap,
    itm_steppe_horse],
   str_10|agi_15|int_7|cha_8|level(17), wpex(110,80,100,60,20,70), knows_common|knows_ironflesh_1|knows_power_strike_4|knows_power_throw_2|knows_power_draw_2|knows_athletics_3|knows_riding_6|knows_horse_archery_3, khergit_face_young_1, khergit_face_old_2 ],
  
  # Light cavalry skirmisher, lances, bows, shields
  ["khergit_light_mounted_skirmisher", "Khergit Light Mounted Skirmisher", "Khergit Light Mounted Skirmishers", tf_guarantee_recruit_armor|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3,
   [itm_sword_khergit_1, itm_light_lance, itm_short_bow, itm_barbed_arrows, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_leather_boots, itm_nomad_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_steppe_armor_herald,
    itm_leather_steppe_cap_b, itm_leather_steppe_cap_c, itm_steppe_cap,
    itm_steppe_horse, itm_courser],
   str_9|agi_16|int_7|cha_9|level(18), wpex(85,75,115,120,25,65), knows_common|knows_power_strike_4|knows_power_throw_1|knows_power_draw_4|knows_athletics_3|knows_riding_6|knows_horse_archery_5, khergit_face_young_1, khergit_face_old_2 ],
  
  # Light cavalry, lances, shields
  ["khergit_light_lancer", "Khergit Light Lancer", "Khergit Light Lancers", tf_guarantee_common_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3,
   [itm_lance, itm_tab_shield_small_round_b,itm_tab_shield_small_round_b_plain_1,itm_tab_shield_small_round_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_nomad_robe, itm_tribal_warrior_outfit,
    itm_leather_steppe_cap_b,
    itm_courser],
   str_12|agi_16|int_7|cha_9|level(21), wpex(90,80,160,60,20,65), knows_common|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_1|knows_power_draw_2|knows_athletics_4|knows_riding_6|knows_horse_archery_2, khergit_face_young_1, khergit_face_old_2 ],
  
  # Light infantry, spears, shields
  ["khergit_light_spearman", "Khergit Light Spearman", "Khergit Light Spearmen", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3,
   [itm_spear, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_steppe_armor_herald,
    itm_leather_steppe_cap_b,
    ],
   str_11|agi_14|int_6|cha_6|level(14), wpex(85,70,135,60,20,55), knows_common|knows_ironflesh_2|knows_power_strike_5|knows_power_throw_1|knows_power_draw_2|knows_athletics_3|knows_riding_3|knows_horse_archery_1, khergit_face_young_1, khergit_face_old_2 ],
  
  # Light cavalry ranged, sabres, maces, bows
  # SPECIAL
  ["khergit_light_horse_archer", "Khergit Light Horse Archer", "Khergit Light Horse Archers", tf_guarantee_recruit_armor|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_33,
   [itm_sword_khergit_2, itm_winged_mace, itm_short_bow, itm_barbed_arrows, itm_barbed_arrows,
    itm_leather_boots, itm_nomad_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_steppe_armor_herald,
    itm_leather_steppe_cap_b, itm_steppe_cap,
    itm_steppe_horse, itm_courser],
   str_9|agi_17|int_8|cha_8|level(19), wpex(75,65,75,140,25,65), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_throw_1|knows_power_draw_4|knows_athletics_3|knows_riding_6|knows_horse_archery_5, khergit_face_young_1, khergit_face_old_2 ],
  
  # Medium infantry, spears
  # SPECIAL
  ["khergit_champion", "Khergit Champion", "Khergit Champions", tf_guarantee_common_armor, no_scene, reserved, fac_small_kingdom_32,
   [itm_hafted_blade_a,
    itm_leather_boots, itm_leather_gloves,
    itm_nomad_robe, itm_tribal_warrior_outfit,
    itm_khergit_war_helmet, itm_leather_steppe_cap_b,
    ],
   str_13|agi_16|int_8|cha_8|level(22), wpex(90,80,130,65,25,70), knows_common|knows_ironflesh_1|knows_power_strike_4|knows_power_throw_1|knows_power_draw_3|knows_athletics_5|knows_riding_3|knows_horse_archery_1, khergit_face_young_1, khergit_face_old_2 ],
  
  # Light cavalry skirmisher, sabres, maces, javelins, shields
  # SPECIAL
  ["khergit_light_steppe_cavalry", "Khergit Light Steppe Cavalry", "Khergit Light Steppe Cavalries", tf_guarantee_common_armor|tf_guarantee_horseman|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_33,
   [itm_sword_khergit_2, itm_winged_mace, itm_javelin, itm_javelin, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_steppe_armor_herald,
    itm_leather_steppe_cap_b, itm_steppe_cap,
    itm_steppe_horse],
   str_9|agi_15|int_7|cha_8|level(16), wpex(95,80,100,60,20,105), knows_common|knows_power_strike_4|knows_power_throw_3|knows_power_draw_2|knows_athletics_3|knows_riding_6|knows_horse_archery_5, khergit_face_young_1, khergit_face_old_2 ],
  
  # Light infantry skirmisher, sabres, maces, javelins, shields
  # SPECIAL
  ["khergit_light_skirmisher", "Khergit Light Skirmisher", "Khergit Light Skirmishers", tf_guarantee_common_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_32,
   [itm_sword_khergit_2, itm_winged_mace, itm_javelin, itm_javelin, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_steppe_armor_herald,
    itm_leather_steppe_cap_b,
    ],
   str_11|agi_16|int_6|cha_7|level(17), wpex(90,80,85,60,20,95), knows_common|knows_ironflesh_1|knows_power_strike_4|knows_power_throw_3|knows_power_draw_2|knows_athletics_4|knows_riding_3|knows_horse_archery_1, khergit_face_young_1, khergit_face_old_2 ],
  
  # Light cavalry, spears, shields
  # SPECIAL
  ["khergit_light_horseman", "Khergit Light Horseman", "Khergit Light Horsemen", tf_guarantee_common_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_35,
   [itm_spear, itm_short_bow, itm_barbed_arrows, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_nomad_robe, itm_tribal_warrior_outfit,
    itm_leather_steppe_cap_b,
    itm_courser],
   str_13|agi_15|int_7|cha_8|level(20), wpex(90,80,150,130,20,70), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_1|knows_power_draw_4|knows_athletics_3|knows_riding_6|knows_horse_archery_5, khergit_face_young_1, khergit_face_old_2 ],
  
  # Veteran
  # Light ranged, sabres, bows
  ["khergit_archer", "Khergit Archer", "Khergit Archers", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3,
   [itm_sword_khergit_2, itm_nomad_bow, itm_bodkin_arrows, itm_bodkin_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_tribal_warrior_outfit,
    itm_leather_steppe_cap_b, itm_leather_steppe_cap_c,
    ],
   str_10|agi_17|int_8|cha_9|level(21), wpex(75,70,75,130,30,80), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_throw_1|knows_power_draw_5|knows_athletics_5|knows_riding_3|knows_horse_archery_2, khergit_face_young_1, khergit_face_old_2 ],
  
  # Medium infantry, spears, shields
  ["khergit_heavy_spearman", "Khergit Heavy Spearman", "Khergit Heavy Spearman", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3,
   [itm_war_spear, itm_tab_shield_small_round_b,itm_tab_shield_small_round_b_plain_1,itm_tab_shield_small_round_b_plain_2,
    itm_leather_boots, itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_khergit_war_helmet, itm_leather_steppe_cap_b,
    ],
   str_14|agi_15|int_8|cha_8|level(22), wpex(90,75,130,65,20,60), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_1|knows_power_draw_2|knows_athletics_2|knows_riding_3|knows_shield_1|knows_horse_archery_1, khergit_face_young_1, khergit_face_old_2 ],
  
  # Medium cavalry, sabres, maces, shields
  ["khergit_heavy_cavalry", "Khergit Heavy Cavalry", "Khergit Heavy Cavalries", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3,
   [itm_sword_khergit_3, itm_spiked_mace, itm_sword_khergit_4, itm_winged_mace, itm_tab_shield_small_round_b,itm_tab_shield_small_round_b_plain_1,itm_tab_shield_small_round_b_plain_2,
    itm_leather_boots, itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_khergit_war_helmet, itm_leather_steppe_cap_b,
    itm_hunter],
   str_13|agi_15|int_8|cha_10|level(23), wpex(100,85,95,65,20,70), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_power_draw_1|knows_athletics_2|knows_riding_5|knows_horse_archery_1, khergit_face_young_1, khergit_face_old_2 ],
  
  # Heavy cavalry, lances, shields
  ["khergit_lancer", "Khergit Lancer", "Khergit Lancers", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3,
   [itm_heavy_lance, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_leather_boots, itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    itm_hunter],
   str_15|agi_15|int_8|cha_11|level(26), wpex(95,80,150,60,20,70), knows_common|knows_ironflesh_6|knows_power_strike_4|knows_power_throw_1|knows_power_draw_2|knows_athletics_3|knows_riding_5|knows_shield_1|knows_horse_archery_2, khergit_face_young_1, khergit_face_old_2 ],
  
  # Light cavalry ranged, sabres, bows, shields
  ["khergit_horse_archer", "Khergit Horse Archer", "Khergit Horse Archers", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3,
   [itm_sword_khergit_2, itm_nomad_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_tab_shield_small_round_b,itm_tab_shield_small_round_b_plain_1,itm_tab_shield_small_round_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_tribal_warrior_outfit, itm_nomad_robe,
    itm_leather_steppe_cap_b, itm_leather_steppe_cap_c,
    itm_steppe_horse],
   str_11|agi_17|int_9|cha_10|level(24), wpex(80,70,80,135,40,90), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_power_draw_5|knows_athletics_5|knows_riding_6|knows_horse_archery_6, khergit_face_young_1, khergit_face_old_2 ],
  
  # Medium infantry, sabres, maces, shields
  # SPECIAL
  ["khergit_heavy_infantry", "Khergit Heavy Infantry", "Khergit Heavy Infantries", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_36,
   [itm_sword_khergit_3, itm_winged_mace, itm_tab_shield_small_round_b,itm_tab_shield_small_round_b_plain_1,itm_tab_shield_small_round_b_plain_2,
    itm_leather_boots, itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_khergit_war_helmet, itm_leather_steppe_cap_b,
    ],
   str_13|agi_14|int_8|cha_7|level(19), wpex(110,80,100,65,20,60), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_2|knows_athletics_3|knows_riding_3|knows_shield_1|knows_horse_archery_1, khergit_face_young_1, khergit_face_old_2 ],
  
  # Medium cavalry skirmisher, sabres, maces, javelins, shields
  # SPECIAL
  ["khergit_heavy_steppe_cavalry", "Khergit Heavy Steppe Cavalry", "Khergit Heavy Steppe Cavalries", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_33,
   [itm_sword_khergit_3, itm_winged_mace, itm_javelin, itm_javelin, itm_tab_shield_small_round_b,itm_tab_shield_small_round_b_plain_1,itm_tab_shield_small_round_b_plain_2,
    itm_leather_boots, itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_khergit_war_helmet, itm_leather_steppe_cap_b,
    itm_hunter],
   str_13|agi_16|int_9|cha_10|level(25), wpex(85,85,95,65,20,105), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_3|knows_power_draw_1|knows_athletics_2|knows_riding_5|knows_horse_archery_5, khergit_face_young_1, khergit_face_old_2 ],
  
  # Medium infantry, sabres, maces, javelins, shields
  # SPECIAL
  ["khergit_warrior", "Khergit Warrior", "Khergit Warrior", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_32,
   [itm_sword_khergit_4, itm_spiked_mace, itm_javelin, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_leather_boots, itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_khergit_war_helmet, itm_leather_steppe_cap_b,
    ],
   str_14|agi_14|int_8|cha_8|level(21), wpex(110,80,100,65,20,80), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_athletics_4|knows_riding_3|knows_shield_1|knows_horse_archery_1, khergit_face_young_1, khergit_face_old_2 ],
  
  # Heavy cavalry, spears, shields
  # SPECIAL
  ["khergit_heavy_horseman", "Khergit Heavy Horseman", "Khergit Heavy Horsemen", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_35,
   [itm_war_spear, itm_nomad_bow, itm_bodkin_arrows, itm_tab_shield_small_round_b,itm_tab_shield_small_round_b_plain_1,itm_tab_shield_small_round_b_plain_2,
    itm_leather_boots, itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    itm_hunter],
   str_15|agi_16|int_8|cha_11|level(27), wpex(95,80,140,120,20,70), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_1|knows_power_draw_5|knows_athletics_2|knows_riding_5|knows_horse_archery_5, khergit_face_young_1, khergit_face_old_2 ],
  
  # Medium cavalry, sabres, maces, lances, spears, bows, shields
  ["khergit_mounted_skirmisher", "Khergit Mounted Skirmisher", "Khergit Mounted Skirmishers", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_31,
   [itm_sword_khergit_3, itm_winged_mace, itm_lance, itm_hafted_blade_a, itm_nomad_bow, itm_bodkin_arrows, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_tribal_warrior_outfit, itm_nomad_robe,
    itm_leather_steppe_cap_b, itm_leather_steppe_cap_c,
    itm_steppe_horse, itm_courser],
   str_14|agi_14|int_8|cha_10|level(23), wpex(95,80,140,120,40,90), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_1|knows_power_draw_5|knows_athletics_3|knows_riding_6|knows_horse_archery_5, khergit_face_young_1, khergit_face_old_2 ],
  
  # Elite
  # Medium infantry, spears
  ["khergit_guard", "Khergit Guard", "Khergit Guards", tf_guarantee_trained_armor, no_scene, reserved, fac_kingdom_3,
   [itm_hafted_blade_b,
    itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    ],
   str_16|agi_15|int_10|cha_9|level(27), wpex(100,85,150,70,25,75), knows_common|knows_ironflesh_6|knows_power_strike_5|knows_power_throw_1|knows_power_draw_3|knows_athletics_5|knows_riding_3|knows_horse_archery_1, khergit_face_young_1, khergit_face_old_2 ],
  
  # Medium cavalry ranged, sabres, maces, bows, shields
  ["khergit_heavy_horse_archer", "Khergit Heavy Horse Archer", "Khergit Heavy Horse Archers", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3,
   [itm_sword_khergit_3, itm_winged_mace, itm_khergit_bow, itm_khergit_arrows, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_leather_boots, itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_leather_steppe_cap_b, itm_khergit_war_helmet,
    itm_courser, itm_steppe_horse],
   str_13|agi_17|int_9|cha_12|level(28), wpex(95,75,85,125,40,90), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_2|knows_power_draw_5|knows_athletics_3|knows_riding_6|knows_horse_archery_7, khergit_face_young_1, khergit_face_old_2 ],
  
  # Heavy cavalry, lances, shields
  # SPECIAL
  ["khergit_heavy_lancer", "Khergit Heavy Lancer", "Khergit Heavy Lancers", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_34,
   [itm_heavy_lance, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_armor_herald,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    itm_hunter],
   str_15|agi_16|int_9|cha_13|level(30), wpex(100,85,150,60,20,70), knows_common|knows_ironflesh_8|knows_power_strike_5|knows_power_throw_1|knows_power_draw_2|knows_athletics_2|knows_riding_6|knows_shield_1|knows_horse_archery_2, khergit_face_young_1, khergit_face_old_2 ],
  
  # Medium infantry, 2h swords
  # SPECIAL
  ["khergit_blademaster", "Khergit Blade-master", "Khergit Blade-masters", tf_guarantee_trained_armor, no_scene, reserved, fac_small_kingdom_36,
   [itm_khergit_sword_two_handed_a,
    itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    ],
   str_14|agi_19|int_10|cha_8|level(28), wpex(95,125,105,70,25,75), knows_common|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_1|knows_power_draw_3|knows_athletics_6|knows_riding_3|knows_horse_archery_1, khergit_face_young_1, khergit_face_old_2 ],
  
  # Medium ranged, sabres, maces, bows, shields
  # SPECIAL
  ["khergit_heavy_archer", "Khergit Heavy Archer", "Khergit Heavy Archers", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_36,
   [itm_sword_khergit_3, itm_winged_mace, itm_khergit_bow, itm_khergit_arrows, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_leather_boots, itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_leather_steppe_cap_b, itm_khergit_war_helmet,
    ],
   str_13|agi_17|int_9|cha_11|level(27), wpex(90,75,80,120,30,80), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_power_draw_5|knows_athletics_4|knows_riding_3|knows_horse_archery_2, khergit_face_young_1, khergit_face_old_2 ],
  
  # Heavy infantry skirmisher, sabres, maces, javelins, shields
  # SPECIAL
  ["khergit_heavy_skirmisher", "Khergit Heavy Skirmisher", "Khergit Heavy Skirmishers", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_32,
   [itm_sword_khergit_4, itm_spiked_mace, itm_javelin, itm_javelin, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    ],
   str_15|agi_16|int_10|cha_8|level(27), wpex(100,85,100,70,25,105), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_power_throw_3|knows_power_draw_2|knows_athletics_3|knows_riding_3|knows_shield_1|knows_horse_archery_1, khergit_face_young_1, khergit_face_old_2 ],
  
  # Medium cavalry ranged, sabres, maces, lances, spears, bows, shields
  # SPECIAL
  ["khergit_heavy_mounted_skirmisher", "Khergit Heavy Mounted Skirmisher", "Khergit Heavy Mounted Skirmishers", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_31,
   [itm_sword_khergit_3, itm_sword_khergit_4, itm_spiked_mace, itm_hafted_blade_a, itm_heavy_lance, itm_khergit_bow, itm_khergit_arrows, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_leather_boots, itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_leather_steppe_cap_b, itm_khergit_war_helmet, itm_khergit_cavalry_helmet,
    itm_courser, itm_steppe_horse],
   str_15|agi_15|int_9|cha_11|level(27), wpex(100,80,140,120,40,90), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_5|knows_athletics_3|knows_riding_6|knows_horse_archery_6, khergit_face_young_1, khergit_face_old_2 ],
  
  # Noble
  # Heavy cavalry ranged, sabres, maces, bows, shields
  ["khergit_noble", "Khergit Noble Horse Archer", "Khergit Noble Horse Archers", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_3,
   [itm_sword_khergit_4, itm_spiked_mace, itm_khergit_bow, itm_khergit_arrows, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_splinted_greaves, itm_leather_gloves, itm_scale_gauntlets,
    itm_lamellar_armor_herald,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    itm_hunter],
   str_16|agi_22|int_11|cha_21|level(47), wpex(115,100,125,145,45,95), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_power_draw_5|knows_athletics_5|knows_riding_7|knows_shield_1|knows_horse_archery_8, khergit_face_young_1, khergit_face_old_2 ],
  
  # Heavy cavalry ranged, sabres, maces, lances, spears, bows, shields
  # SPECIAL
  ["khergit_noble_mounted_skirmisher", "Khergit Noble Mounted Skirmisher", "Khergit Noble Mounted Skirmishers", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_31,
   [itm_sword_khergit_4, itm_spiked_mace, itm_hafted_blade_a, itm_heavy_lance, itm_khergit_bow, itm_khergit_arrows, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_splinted_greaves, itm_leather_gloves, itm_scale_gauntlets,
    itm_lamellar_armor_herald,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    itm_hunter],
   str_17|agi_19|int_11|cha_19|level(43), wpex(105,100,150,135,45,85), knows_common|knows_ironflesh_6|knows_power_strike_5|knows_power_throw_2|knows_power_draw_5|knows_athletics_4|knows_riding_7|knows_shield_1|knows_horse_archery_6, khergit_face_young_1, khergit_face_old_2 ],
  
  # Heavy cavalry, sabres, maces, shields
  # SPECIAL
  ["khergit_noble_cavalry", "Khergit Noble Cavalry", "Khergit Noble Cavalry", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_34,
   [itm_sword_khergit_4, itm_spiked_mace, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_splinted_greaves, itm_leather_gloves, itm_scale_gauntlets,
    itm_lamellar_armor_herald,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    itm_warhorse_steppe],
   str_17|agi_21|int_11|cha_19|level(45), wpex(115,100,130,90,45,85), knows_common|knows_ironflesh_6|knows_power_strike_4|knows_power_throw_2|knows_power_draw_3|knows_athletics_4|knows_riding_7|knows_shield_1|knows_horse_archery_2, khergit_face_young_1, khergit_face_old_2 ],
  
  # Heavy cavalry, lances, shields
  # SPECIAL
  ["khergit_noble_lancer", "Khergit Noble Lancer", "Khergit Noble Lancer", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_34,
   [itm_heavy_lance, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_splinted_greaves, itm_scale_gauntlets,
    itm_lamellar_armor_herald,
    itm_khergit_guard_helmet,
    itm_warhorse_steppe],
   str_19|agi_21|int_11|cha_22|level(50), wpex(100,90,175,90,45,85), knows_common|knows_ironflesh_9|knows_power_strike_6|knows_power_throw_2|knows_power_draw_3|knows_athletics_3|knows_riding_7|knows_shield_1|knows_horse_archery_2, khergit_face_young_1, khergit_face_old_2 ],
  
  # Heavy cavalry, spears, shields
  # SPECIAL
  ["khergit_noble_horseman", "Khergit Noble Horseman", "Khergit Noble Horsemen", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_35,
   [itm_war_spear, itm_khergit_bow, itm_khergit_arrows, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_splinted_greaves, itm_leather_gloves, itm_scale_gauntlets,
    itm_lamellar_armor_herald,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    itm_warhorse_steppe],
   str_18|agi_22|int_11|cha_19|level(47), wpex(100,90,160,120,45,85), knows_common|knows_ironflesh_7|knows_power_strike_5|knows_power_throw_2|knows_power_draw_5|knows_athletics_4|knows_riding_7|knows_shield_1|knows_horse_archery_6, khergit_face_young_1, khergit_face_old_2 ],
  
  #########
  # Nords #
  #########
  # Peasant
  # Basic infantry, spears, shields
  ["nord_levy", "Nord Levy Spearman", "Nord Levy Spearmen", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4,
   [itm_spear, itm_tab_shield_round_a,itm_tab_shield_round_a_plain_1,itm_tab_shield_round_a_plain_2,
    itm_nomad_boots, itm_hide_boots,
    itm_tunic_herald, itm_coarse_tunic_herald, itm_fur_coat,
    itm_leather_cap, itm_nordic_archer_helmet, itm_skullcap,
    ],
   str_11|agi_8|int_5|cha_6|level(7), wpex(60,60,80,30,15,25), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1, nord_face_young_1, nord_face_old_2 ],
  
  # Basic infantry, axes, shields
  ["nord_raider", "Nord Raider", "Nord Raiders", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4,
   [itm_one_handed_war_axe_a, itm_tab_shield_round_b,itm_tab_shield_round_b_plain_1,itm_tab_shield_round_b_plain_2,
    itm_nomad_boots, itm_hide_boots,
    itm_tunic_herald, itm_coarse_tunic_herald, itm_fur_coat,
    itm_leather_cap, itm_nordic_archer_helmet, itm_skullcap,
    ],
   str_12|agi_11|int_5|cha_6|level(11), wpex(85,70,70,30,15,30), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_1|knows_athletics_3, nord_face_young_1, nord_face_old_2 ],

  # Basic ranged, daggers, axes, bows
  ["nord_militia", "Nord Militia", "Nord Militias", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4,
   [itm_knife, itm_hatchet, itm_hunting_bow2, itm_arrows_b,
    itm_nomad_boots, itm_hide_boots,
    itm_tunic_herald, itm_coarse_tunic_herald,
    itm_leather_cap, itm_skullcap,
    ],
   str_10|agi_9|int_6|cha_6|level(8), wpex(65,60,60,60,30,30), knows_common|knows_power_strike_3|knows_power_draw_4|knows_athletics_2, nord_face_young_1, nord_face_old_2 ],
  
  # Basic ranged, daggers, axes, crossbows
  # SPECIAL
  ["nord_hunter", "Nord Hunter", "Nord Hunter", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_44,
   [itm_knife, itm_hatchet, itm_hunting_crossbow, itm_bolts,
    itm_nomad_boots, itm_hide_boots,
    itm_tunic_herald, itm_coarse_tunic_herald,
    itm_leather_cap, itm_skullcap,
    ],
   str_10|agi_9|int_6|cha_6|level(8), wpex(65,60,60,30,55,30), knows_common|knows_power_strike_3|knows_athletics_1, nord_face_young_1, nord_face_old_2 ],
  
  # Common
  # Light infantry, swords, axes, javelin, shields
  ["nord_light_infantry", "Nord Light Infantry", "Nord Light Infantries", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4,
   [itm_one_handed_battle_axe_a, itm_one_handed_battle_axe_a, itm_sword_viking_2, itm_sword_viking_2_small, itm_javelin, itm_light_throwing_axes, itm_tab_shield_round_c,itm_tab_shield_round_c_plain_1,itm_tab_shield_round_c_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    ],
   str_14|agi_14|int_7|cha_9|level(21), wpex(115,105,100,55,20,80), knows_common|knows_ironflesh_3|knows_power_strike_5|knows_power_throw_3|knows_athletics_5, nord_face_young_1, nord_face_old_2 ],
  
  # Light ranged, swords, axes, bows
  ["nord_light_bowman", "Nord Light Bowman", "Nord Light Bowmen", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4,
   [itm_sword_viking_1, itm_one_handed_battle_axe_a, itm_hunting_bow2, itm_barbed_arrows, itm_barbed_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_tunic_herald, itm_coarse_tunic_herald,
    itm_nordic_archer_helmet, itm_nordic_veteran_archer_helmet,
    ],
   str_13|agi_15|int_7|cha_6|level(18), wpex(75,65,60,125,45,55), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_5|knows_riding_1, nord_face_young_1, nord_face_old_2 ],
  
  # Light cavalry skirmisher, swords, javelins, shields
  ["nord_light_cavalry", "Nord Light Cavalry", "Nord Light Cavalries", tf_guarantee_common_armor|tf_guarantee_horseman|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4,
   [itm_sword_viking_1, itm_sword_viking_1_long, itm_light_throwing_axes, itm_light_throwing_axes, itm_tab_shield_round_b,itm_tab_shield_round_b_plain_1,itm_tab_shield_round_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_tunic_herald, itm_coarse_tunic_herald,
    itm_nordic_archer_helmet, itm_nordic_veteran_archer_helmet,
    itm_saddle_horse],
   str_12|agi_14|int_6|cha_6|level(15), wpex(85,80,75,45,25,90), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_throw_3|knows_athletics_4|knows_riding_5|knows_horse_archery_3, nord_face_young_1, nord_face_old_2 ],
  
  # Light infantry, spears, shields
  # SPECIAL
  ["nord_spearman", "Nord Spearman", "Nord Spearmen", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_44,
   [itm_war_spear, itm_tab_shield_round_c,itm_tab_shield_round_c_plain_1,itm_tab_shield_round_c_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet,
    ],
   str_14|agi_14|int_6|cha_6|level(17), wpex(85,80,125,50,20,55), knows_common|knows_ironflesh_3|knows_power_strike_5|knows_power_throw_1|knows_athletics_4, nord_face_young_1, nord_face_old_2 ],
  
  # Light infantry skirmisher, swords, javelins, shields
  # SPECIAL
  ["nord_light_skirmisher", "Nord Light Skirmisher", "Nord Light Skirmishers", tf_guarantee_common_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_43,
   [itm_sword_viking_1, itm_javelin, itm_javelin, itm_tab_shield_round_c,itm_tab_shield_round_c_plain_1,itm_tab_shield_round_c_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_tunic_herald, itm_coarse_tunic_herald,
    itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    ],
   str_12|agi_15|int_7|cha_6|level(17), wpex(105,100,95,50,20,110), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_3|knows_athletics_4, nord_face_young_1, nord_face_old_2 ],
  
  # Light ranged, swords, axes, bows
  # SPECIAL
  ["nord_light_longbowman", "Nord Light Longbowman", "Nord Light Longbowmen", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_42,
   [itm_sword_viking_1, itm_one_handed_battle_axe_a, itm_long_bow, itm_barbed_arrows, itm_barbed_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_tunic_herald, itm_coarse_tunic_herald,
    itm_nordic_archer_helmet, itm_nordic_veteran_archer_helmet,
    ],
   str_15|agi_13|int_7|cha_7|level(19), wpex(75,65,60,95,45,55), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_6|knows_athletics_5|knows_riding_1, nord_face_young_1, nord_face_old_2 ],
  
  # Light cavalry ranged, swords, axes, bows
  # SPECIAL
  ["nord_mounted_bowman", "Nord Mounted Bowman", "Nord Mounted Bowmen", tf_guarantee_recruit_armor|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_41,
   [itm_sword_viking_1, itm_one_handed_battle_axe_a, itm_hunting_bow2, itm_barbed_arrows, itm_barbed_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_tunic_herald, itm_coarse_tunic_herald,
    itm_nordic_archer_helmet, itm_nordic_veteran_archer_helmet,
    itm_saddle_horse],
   str_13|agi_15|int_7|cha_7|level(19), wpex(75,65,60,120,45,55), knows_common|knows_power_strike_2|knows_power_draw_4|knows_athletics_4|knows_riding_5|knows_horse_archery_4, nord_face_young_1, nord_face_old_2 ],
  
  # Light cavalry skirmisher, swords, axes, javelins
  # SPECIAL
  ["nord_light_mounted_skirmisher", "Nord Light Mounted Skirmisher", "Nord Light Mounted Skirmisher", tf_guarantee_common_armor|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_43,
   [itm_sword_viking_1, itm_sword_viking_1_long, itm_one_handed_battle_axe_a, itm_javelin, itm_javelin, itm_javelin,
    itm_leather_boots, itm_leather_gloves,
    itm_tunic_herald, itm_coarse_tunic_herald,
    itm_nordic_archer_helmet, itm_nordic_veteran_archer_helmet,
    itm_saddle_horse],
   str_12|agi_15|int_6|cha_7|level(17), wpex(95,85,80,45,25,105), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_3|knows_athletics_4|knows_riding_5|knows_horse_archery_4, nord_face_young_1, nord_face_old_2 ],
  
  # Light cavalry, spears, shields
  # SPECIAL
  ["nord_light_spear_cavalry", "Nord Light Spear Cavalry", "Nord Light Spear Cavalries", tf_guarantee_common_armor|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_45,
   [itm_spear, itm_tab_shield_round_b,itm_tab_shield_round_b_plain_1,itm_tab_shield_round_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_nordic_archer_helmet, itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet,
    itm_saddle_horse],
   str_12|agi_14|int_7|cha_6|level(16), wpex(95,90,125,45,25,60), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_athletics_5|knows_riding_5, nord_face_young_1, nord_face_old_2 ],
  
  # Medium infantry, swords, axes, shields
  # SPECIAL
  ["nord_infantry", "Nord Infantry", "Nord Infantries", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_42,
   [itm_one_handed_battle_axe_a, itm_one_handed_battle_axe_a, itm_sword_viking_1, itm_sword_viking_1_long, itm_tab_shield_round_c,itm_tab_shield_round_c_plain_1,itm_tab_shield_round_c_plain_2,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_byrnie_herald,
    itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    ],
   str_15|agi_13|int_8|cha_9|level(22), wpex(110,100,95,55,20,55), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_athletics_3, nord_face_young_1, nord_face_old_2 ],
  
  # Light infantry skirmisher, swords, axes, javelins, shields
  # SPECIAL
  ["nord_footman", "Nord Footman", "Nord Footmen", tf_guarantee_common_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_42,
   [itm_one_handed_battle_axe_a, itm_sword_viking_1, itm_throwing_axes, itm_throwing_axes, itm_tab_shield_round_c,itm_tab_shield_round_c_plain_1,itm_tab_shield_round_c_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_tunic_herald, itm_coarse_tunic_herald,
    itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    ],
   str_12|agi_15|int_7|cha_7|level(18), wpex(105,100,95,50,20,90), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_4|knows_athletics_4, nord_face_young_1, nord_face_old_2 ],
  
  # Veteran
  # Medium infantry, swords, axes, javelins, shields
  ["nord_medium_infantry", "Nord Warrior", "Nord Warriors", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4,
   [itm_one_handed_battle_axe_a, itm_one_handed_war_axe_b, itm_sword_viking_2, itm_sword_viking_2_small, itm_throwing_axes, itm_tab_shield_round_d,itm_tab_shield_round_d_plain_1,itm_tab_shield_round_d_plain_2,
    itm_mail_chausses, itm_splinted_leather_greaves, itm_mail_mittens,
    itm_byrnie_herald, itm_mail_shirt_herald, itm_mail_hauberk_herald,
    itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_nordic_helmet,
    ],
   str_16|agi_15|int_8|cha_11|level(27), wpex(125,105,100,60,25,65), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_3|knows_athletics_5|knows_shield_1, nord_face_young_1, nord_face_old_2 ],
  
  # Medium infantry, 2h axes
  ["nord_champion", "Nord Champion", "Nord Champions", tf_guarantee_trained_armor, no_scene, reserved, fac_kingdom_4,
   [itm_two_handed_battle_axe_2,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_byrnie_herald,
    itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_nordic_helmet,
    ],
   str_16|agi_15|int_7|cha_9|level(24), wpex(95,120,100,50,25,70), knows_common|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_1|knows_athletics_3|knows_riding_1, nord_face_young_1, nord_face_old_2 ],
  
  # Light ranged, swords, axes, bows
  ["nord_medium_longbowman", "Nord Longbowman", "Nord Longbowmen", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4,
   [itm_one_handed_battle_axe_a, itm_one_handed_battle_axe_a, itm_sword_viking_2, itm_sword_viking_2_small, itm_long_bow, itm_bodkin_arrows, itm_bodkin_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_nordic_archer_helmet, itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet,
    ],
   str_16|agi_14|int_7|cha_8|level(22), wpex(80,65,60,95,45,55), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_1|knows_power_draw_6|knows_athletics_4|knows_riding_1, nord_face_young_1, nord_face_old_2 ],
  
  # Medium cavalry, 2h axes
  ["nord_horseman", "Nord Horseman", "Nord Horsemen", tf_guarantee_trained_armor|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_4,
   [itm_two_handed_axe,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    itm_sumpter_horse],
   str_15|agi_12|int_7|cha_7|level(18), wpex(95,115,95,50,25,70), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_athletics_4|knows_riding_4|knows_horse_archery_1, nord_face_young_1, nord_face_old_2 ],
  
  # Medium infantry, spears, shields
  # SPECIAL
  ["nord_heavy_spearman", "Nord Heavy Spearman", "Nord Heavy Spearmen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_44,
   [itm_war_spear, itm_tab_shield_round_d,itm_tab_shield_round_d_plain_1,itm_tab_shield_round_d_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_byrnie_herald,
    itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_nordic_helmet,
    ],
   str_18|agi_12|int_7|cha_8|level(22), wpex(100,95,115,55,25,70), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_1|knows_athletics_3|knows_shield_1, nord_face_young_1, nord_face_old_2 ],
  
  # Light cavalry, lances, shields
  # SPECIAL
  ["nord_light_lancer", "Nord Light Lancer", "Nord Light Lancers", tf_guarantee_common_armor|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_41,
   [itm_light_lance, itm_tab_shield_round_c,itm_tab_shield_round_c_plain_1,itm_tab_shield_round_c_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_nordic_archer_helmet, itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet,
    itm_saddle_horse],
   str_12|agi_15|int_7|cha_6|level(17), wpex(75,80,110,50,25,65), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_throw_1|knows_athletics_3|knows_riding_5, nord_face_young_1, nord_face_old_2 ],
  
  # Medium infantry skirmisher, swords, javelins, shields
  # SPECIAL
  ["nord_heavy_skirmisher", "Nord Heavy Skirmisher", "Nord Heavy Skirmishers", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_43,
   [itm_sword_viking_2, itm_sword_viking_2_small, itm_javelin, itm_javelin, itm_tab_shield_round_d,itm_tab_shield_round_d_plain_1,itm_tab_shield_round_d_plain_2,
    itm_mail_chausses, itm_splinted_leather_greaves, itm_mail_mittens,
    itm_byrnie_herald,
    itm_nordic_fighter_helmet, itm_nordic_helmet,
    ],
   str_15|agi_15|int_9|cha_9|level(25), wpex(100,95,90,55,25,105), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_athletics_3|knows_riding_2, nord_face_young_1, nord_face_old_2 ],
  
  # Light ranged, swords, axes, bows
  # SPECIAL
  ["nord_medium_bowman", "Nord Bowman", "Nord Bowmen", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_45,
   [itm_one_handed_battle_axe_a, itm_one_handed_battle_axe_a, itm_sword_viking_2, itm_sword_viking_2_small, itm_short_bow2, itm_bodkin_arrows, itm_bodkin_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_nordic_archer_helmet, itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet,
    ],
   str_16|agi_15|int_7|cha_7|level(22), wpex(80,65,60,120,45,55), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_1|knows_power_draw_4|knows_athletics_5|knows_riding_1, nord_face_young_1, nord_face_old_2 ],
  
  # Medium ranged, swords, axes, crossbow
  # SPECIAL
  ["nord_medium_crossbowman", "Nord Crossbowman", "Nord Crossbowmen", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_44,
   [itm_one_handed_battle_axe_a, itm_one_handed_battle_axe_a, itm_sword_viking_2, itm_sword_viking_2_small, itm_light_crossbow, itm_bolts, itm_bolts,
    itm_leather_boots, itm_leather_gloves,
    itm_byrnie_herald,
    itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    ],
   str_16|agi_15|int_7|cha_7|level(22), wpex(80,65,60,75,115,55), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_power_draw_4|knows_athletics_4|knows_riding_1, nord_face_young_1, nord_face_old_2 ],
  
  # Medium cavalry, spears, shields
  # SPECIAL
  ["nord_medium_spear_cavalry", "Nord Spear Cavalry", "Nord Spear Cavalries", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_45,
   [itm_spear, itm_tab_shield_round_c,itm_tab_shield_round_c_plain_1,itm_tab_shield_round_c_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_byrnie_herald,
    itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    itm_pack_horse],
   str_14|agi_13|int_8|cha_8|level(20), wpex(100,95,120,50,25,70), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_1|knows_athletics_4|knows_riding_4|knows_horse_archery_1, nord_face_young_1, nord_face_old_2 ],
  
  # Medium cavalry, swords, axes, shields
  # SPECIAL
  ["nord_cavalry", "Nord Cavalry", "Nord Cavalries", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_41,
   [itm_one_handed_battle_axe_a, itm_one_handed_war_axe_b, itm_sword_viking_2, itm_throwing_axes, itm_tab_shield_round_c,itm_tab_shield_round_c_plain_1,itm_tab_shield_round_c_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_byrnie_herald,
    itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    itm_pack_horse],
   str_14|agi_13|int_7|cha_8|level(19), wpex(100,95,95,50,25,90), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_3|knows_athletics_3|knows_riding_4|knows_horse_archery_3, nord_face_young_1, nord_face_old_2 ],
  
  # Elite
  # Medium cavalry, swords, axes, shields
  ["nord_heavy_cavalry", "Nord Heavy Cavalry", "Nord Heavy Cavalries", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_4,
   [itm_sword_viking_3, itm_sword_viking_3_long, itm_one_handed_battle_axe_b, itm_tab_shield_round_d,itm_tab_shield_round_d_plain_1,itm_tab_shield_round_d_plain_2,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_byrnie_herald, itm_mail_shirt_herald,
    itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_nordic_helmet,
    itm_hunter],
   str_14|agi_14|int_9|cha_8|level(22), wpex(110,100,95,55,30,75), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_athletics_3|knows_riding_4|knows_horse_archery_1, nord_face_young_1, nord_face_old_2 ],
  
  # Medium ranged, axes, swords, bows, shields
  ["nord_heavy_bowman", "Nord Heavy Bowman", "Nord Heavy Bowmen", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4,
   [itm_one_handed_battle_axe_a, itm_one_handed_war_axe_b, itm_sword_viking_2, itm_sword_viking_2_small, itm_short_bow2, itm_barbed_arrows, itm_tab_shield_round_c,itm_tab_shield_round_c_plain_1,itm_tab_shield_round_c_plain_2,
    itm_mail_chausses, itm_leather_boots, itm_leather_gloves,
    itm_byrnie_herald, itm_mail_shirt_herald,
    itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    ],
   str_15|agi_15|int_9|cha_9|level(25), wpex(95,75,70,90,45,60), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_1|knows_power_draw_4|knows_athletics_2, nord_face_young_1, nord_face_old_2 ],
  
  # Medium infantry skirmisher, poleaxes, javelins
  ["nord_guard", "Nord Guard", "Nord Guards", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4,
   [itm_long_axe_b, itm_throwing_axes, itm_throwing_axes,
    itm_mail_chausses, itm_splinted_leather_greaves, itm_mail_mittens,
    itm_byrnie_herald, itm_mail_shirt_herald, itm_mail_hauberk_herald,
    itm_nordic_fighter_helmet, itm_nordic_helmet,
    ],
   str_18|agi_16|int_8|cha_10|level(29), wpex(105,115,130,55,25,80), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_4|knows_athletics_2|knows_riding_2, nord_face_young_1, nord_face_old_2 ],
  
  # Medium ranged, axes, swords, bows
  # SPECIAL
  ["nord_heavy_longbowman", "Nord Heavy Longbowman", "Nord Heavy Longbowmen", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_42,
   [itm_one_handed_battle_axe_a, itm_one_handed_war_axe_b, itm_sword_viking_2, itm_sword_viking_2_small, itm_long_bow, itm_bodkin_arrows, itm_bodkin_arrows,
    itm_mail_chausses, itm_leather_boots, itm_leather_gloves,
    itm_byrnie_herald,
    itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    ],
   str_16|agi_14|int_8|cha_9|level(24), wpex(90,70,65,85,45,60), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_1|knows_power_draw_6|knows_athletics_3|knows_riding_1, nord_face_young_1, nord_face_old_2 ],
  
  # Medium cavalry, spears, shields
  # SPECIAL
  ["nord_heavy_spear_cavalry", "Nord Heavy Spear Cavalry", "Nord Heavy Spear Cavalries", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_45,
   [itm_war_spear, itm_tab_shield_round_d,itm_tab_shield_round_d_plain_1,itm_tab_shield_round_d_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_byrnie_herald, itm_mail_shirt_herald,
    itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_nordic_helmet,
    itm_hunter],
   str_16|agi_14|int_10|cha_10|level(27), wpex(100,95,115,55,30,75), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_1|knows_athletics_3|knows_riding_4|knows_horse_archery_1, nord_face_young_1, nord_face_old_2 ],
  
  # Medium cavalry ranged, axes, swords, bows
  # SPECIAL
  ["nord_heavy_mounted_bowman", "Nord Heavy Mounted Bowman", "Nord Heavy Mounted Bowmen", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_41,
   [itm_one_handed_battle_axe_a, itm_sword_viking_2, itm_short_bow2, itm_bodkin_arrows,
    itm_mail_chausses, itm_leather_boots, itm_leather_gloves,
    itm_byrnie_herald,
    itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    itm_hunter],
   str_15|agi_16|int_9|cha_9|level(26), wpex(85,70,65,110,45,60), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_throw_1|knows_power_draw_4|knows_athletics_2|knows_riding_4|knows_horse_archery_4, nord_face_young_1, nord_face_old_2 ],
  
  # Heavy infantry, swords, axes, shields
  # SPECIAL
  ["nord_heavy_infantry", "Nord Heavy Infantry", "Nord Heavy Infantry", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_43,
   [itm_one_handed_battle_axe_b, itm_one_handed_battle_axe_c, itm_sword_viking_3, itm_sword_viking_3_small, itm_sword_viking_3_long, itm_tab_shield_round_e,itm_tab_shield_round_e_plain_1,itm_tab_shield_round_e_plain_2,
    itm_mail_chausses, itm_splinted_leather_greaves, itm_mail_mittens,
    itm_banded_armor,
    itm_nordic_huscarl_helmet, itm_nordic_helmet,
    ],
   str_19|agi_15|int_10|cha_12|level(33), wpex(120,110,105,65,25,70), knows_common|knows_ironflesh_6|knows_power_strike_4|knows_power_throw_1|knows_athletics_4|knows_shield_1, nord_face_young_1, nord_face_old_2 ],
  
  # Noble
  # Heavy infantry, swords, axes, shields
  ["nord_noble_infantry", "Nord Huscarl", "Nord Huscarls", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4,
   [itm_sword_viking_3, itm_sword_viking_3_small, itm_sword_viking_3_long, itm_one_handed_battle_axe_b, itm_one_handed_battle_axe_c, itm_tab_shield_round_e,itm_tab_shield_round_e_plain_1,itm_tab_shield_round_e_plain_2,
    itm_mail_boots, itm_iron_greaves, itm_gauntlets, itm_mail_mittens,
    itm_banded_armor, itm_cuir_bouilli_herald,
    itm_nordic_huscarl_helmet, itm_nordic_warlord_helmet,
    ],
   str_23|agi_21|int_12|cha_17|level(50), wpex(145,110,105,70,30,90), knows_common|knows_ironflesh_8|knows_power_strike_6|knows_power_throw_3|knows_power_draw_3|knows_athletics_6|knows_riding_3|knows_shield_1|knows_horse_archery_1, nord_face_young_1, nord_face_old_2 ],
  
  # Heavy infantry skirmisher, poleaxes, javelins
  # SPECIAL
  ["nord_noble_guard", "Nord King's Guard", "Nord King's Guards", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_45,
   [itm_long_axe_c, itm_heavy_throwing_axes, itm_heavy_throwing_axes,
    itm_mail_boots, itm_iron_greaves, itm_gauntlets, itm_mail_mittens,
    itm_cuir_bouilli_herald,
    itm_nordic_huscarl_helmet, itm_nordic_warlord_helmet,
    ],
   str_26|agi_19|int_11|cha_19|level(52), wpex(125,115,145,70,30,110), knows_common|knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_power_draw_3|knows_athletics_5|knows_riding_3|knows_horse_archery_1, nord_face_young_1, nord_face_old_2 ],
  
  # Heavy cavalry, lances, shields
  # SPECIAL
  ["nord_noble_lancer", "Nord Armoured Lancer", "Nord Armoured Lancers", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_41,
   [itm_lance, itm_tab_shield_round_d,itm_tab_shield_round_d_plain_1,itm_tab_shield_round_d_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_banded_armor,
    itm_nordic_helmet, itm_nordic_huscarl_helmet, itm_nordic_warlord_helmet,
    itm_warhorse],
   str_19|agi_19|int_12|cha_15|level(42), wpex(110,105,125,70,30,90), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_athletics_3|knows_riding_5|knows_horse_archery_1, nord_face_young_1, nord_face_old_2 ],
  
  ###########
  # Rhodoks #
  ###########
  # Peasant
  # Basic infantry, spears, shields
  ["rhodok_levy_spearman", "Rhodok Levy Spearman", "Rhodok Levy Spearmen", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_5,
   [itm_spear, itm_tab_shield_pavise_a,itm_tab_shield_pavise_a_plain_1,itm_tab_shield_pavise_a_plain_2,
    itm_wrapping_boots, itm_nomad_boots, itm_hide_boots,
    itm_tunic_herald, itm_tunic_with_green_cape_herald, itm_coarse_tunic_herald,
    itm_common_hood_herald, itm_common_hood_herald, itm_common_hood_herald2, itm_head_wrappings,
    ],
   str_10|agi_7|int_5|cha_6|level(5), wpex(60,55,95,15,35,30), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Basic infantry, swords, picks, shields
  ["rhodok_levy", "Rhodok Levy", "Rhodok Levy", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_5,
   [itm_falchion, itm_fighting_pick, itm_tab_shield_pavise_a,itm_tab_shield_pavise_a_plain_1,itm_tab_shield_pavise_a_plain_2,
    itm_wrapping_boots, itm_nomad_boots, itm_hide_boots,
    itm_tunic_herald, itm_tunic_with_green_cape_herald, itm_coarse_tunic_herald,
    itm_common_hood_herald, itm_common_hood_herald, itm_common_hood_herald2, itm_head_wrappings,
    ],
   str_11|agi_7|int_6|cha_6|level(7), wpex(65,60,75,15,30,30), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_2, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Basic ranged, swords, picks, bows
  ["rhodok_militia", "Rhodok Militia", "Rhodok Militias", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_5,
   [itm_falchion, itm_fighting_pick, itm_hunting_bow2, itm_arrows_b,
    itm_wrapping_boots, itm_nomad_boots, itm_hide_boots,
    itm_tunic_herald, itm_tunic_with_green_cape_herald, itm_coarse_tunic_herald,
    itm_common_hood_herald, itm_common_hood_herald, itm_common_hood_herald2, itm_head_wrappings,
    ],
   str_9|agi_9|int_6|cha_6|level(7), wpex(50,40,45,70,35,30), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_4|knows_athletics_3, man_face_young_1, man_face_old_2 ],
  
  # Basic infantry, pikes
  # SPECIAL
  ["rhodok_levy_pikeman", "Rhodok Levy Pikeman", "Rhodok Levy Pikemen", tf_guarantee_recruit_armor, no_scene, reserved, fac_small_kingdom_52,
   [itm_pike,
    itm_wrapping_boots, itm_nomad_boots, itm_hide_boots,
    itm_tunic_herald, itm_tunic_with_green_cape_herald, itm_coarse_tunic_herald,
    itm_common_hood_herald, itm_common_hood_herald, itm_common_hood_herald2, itm_head_wrappings,
    ],
   str_12|agi_7|int_6|cha_6|level(8), wpex(60,55,95,15,35,30), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Basic ranged, swords, picks, crossbows
  # SPECIAL
  ["rhodok_levy_crossbowman", "Rhodok Levy Crossbowman", "Rhodok Levy Crossbowmen", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_54,
   [itm_falchion, itm_fighting_pick, itm_hunting_crossbow, itm_bolts,
    itm_wrapping_boots, itm_nomad_boots, itm_hide_boots,
    itm_tunic_herald, itm_tunic_with_green_cape_herald, itm_coarse_tunic_herald,
    itm_common_hood_herald, itm_common_hood_herald, itm_common_hood_herald2, itm_head_wrappings,
    ],
   str_9|agi_10|int_6|cha_7|level(9), wpex(50,40,45,35,70,30), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_athletics_2, rhodok_face_young_1, rhodok_face_old_2 ],

  # Basic ranged, swords, picks, 2h hammer, spears, bows
  # SPECIAL
  ["rhodok_hunter", "Rhodok Hunter", "Rhodok Hunters", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_51,
   [itm_falchion, itm_pitch_fork, itm_fighting_pick, itm_maul, itm_hunting_bow2, itm_arrows_b,
    itm_wrapping_boots, itm_nomad_boots, itm_hide_boots,
    itm_tunic_herald, itm_tunic_with_green_cape_herald, itm_coarse_tunic_herald,
    itm_common_hood_herald, itm_common_hood_herald, itm_common_hood_herald2, itm_head_wrappings,
    ],
   str_9|agi_10|int_6|cha_6|level(8), wpex(55,45,60,75,35,30), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_draw_4|knows_athletics_3, man_face_young_1, man_face_old_2 ],
  
  # Common
  # Light infantry, swords, picks, shields
  ["rhodok_light_infantry", "Rhodok Light Swordsman", "Rhodok Light Swordsmen", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_5,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_military_cleaver_a, itm_military_sickle_a, itm_tab_shield_pavise_b,itm_tab_shield_pavise_b_plain_1,itm_tab_shield_pavise_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_armor_herald, itm_aketon_green_herald,
    itm_footman_helmet, itm_helmet_with_neckguard, itm_padded_coif, itm_common_hood_herald, itm_mail_coif,
    ],
   str_11|agi_13|int_7|cha_6|level(14), wpex(90,75,95,20,45,35), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_athletics_4, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Light infantry, spears
  ["rhodok_pikeman", "Rhodok Pikeman", "Rhodok Pikemen", tf_guarantee_common_armor, no_scene, reserved, fac_kingdom_5,
   [itm_pike,
    itm_leather_boots, itm_leather_gloves,
    itm_aketon_green_herald, itm_ragged_outfit,
    itm_footman_helmet, itm_mail_coif, itm_helmet_with_neckguard,
    ],
   str_14|agi_11|int_7|cha_9|level(18), wpex(90,75,145,25,55,40), knows_common|knows_ironflesh_7|knows_power_strike_5|knows_power_throw_1|knows_athletics_2|knows_riding_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Light infantry, spears
  ["rhodok_guard", "Rhodok Guard", "Rhodok Guards", tf_guarantee_common_armor, no_scene, reserved, fac_kingdom_5,
   [itm_glaive,
    itm_leather_boots, itm_leather_gloves,
    itm_aketon_green_herald, itm_ragged_outfit, itm_leather_armor_herald,
    itm_footman_helmet, itm_mail_coif, itm_helmet_with_neckguard,
    ],
   str_16|agi_12|int_7|cha_9|level(21), wpex(110,95,135,25,65,45), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_athletics_5|knows_riding_2, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Light ranged, swords, picks, crossbows
  ["rhodok_light_crossbowman", "Rhodok Light Crossbowman", "Rhodok Light Crossbowmen", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_5,
   [itm_sword_medieval_a, itm_falchion, itm_fighting_pick, itm_club_with_spike_head, itm_crossbow, itm_steel_bolts, itm_steel_bolts,
    itm_hide_boots, itm_nomad_boots, itm_leather_boots, itm_leather_gloves,
    itm_leather_armor_herald, itm_tunic_with_green_cape_herald,
    itm_padded_coif, itm_common_hood_herald,
    ],
   str_10|agi_13|int_7|cha_9|level(16), wpex(65,55,60,30,130,35), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_1|knows_athletics_5|knows_riding_1|knows_horse_archery_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Light ranged, swords, picks, bows, shields
  ["rhodok_light_bowman", "Rhodok Light Bowman", "Rhodok Light Bowmen", tf_guarantee_common_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_5,
   [itm_sword_medieval_a, itm_falchion, itm_fighting_pick, itm_hunting_bow2, itm_barbed_arrows, itm_barbed_arrows, itm_tab_shield_pavise_a,itm_tab_shield_pavise_a_plain_1,itm_tab_shield_pavise_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_armor_herald, itm_aketon_green_herald,
    itm_padded_coif, itm_common_hood_herald,
    ],
   str_9|agi_14|int_7|cha_7|level(14), wpex(60,50,55,120,55,30), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_4|knows_athletics_4|knows_riding_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Light cavalry ranged, swords, picks, crossbows
  ["rhodok_light_horse_archer", "Rhodok Mounted Skirmisher", "Rhodok Mounted Skirmisher", tf_guarantee_recruit_armor|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_5,
   [itm_sword_medieval_a, itm_fighting_pick, itm_light_crossbow, itm_bolts, itm_bolts,
    itm_leather_boots, itm_leather_gloves,
    itm_aketon_green_herald, itm_leather_armor_herald,
    itm_padded_coif, itm_common_hood_herald, itm_footman_helmet, itm_mail_coif,
    itm_saddle_horse],
   str_9|agi_14|int_8|cha_7|level(15), wpex(65,55,65,30,130,40), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_1|knows_athletics_2|knows_riding_5|knows_horse_archery_5, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Light infantry, spears, shields
  # SPECIAL
  ["rhodok_light_spearman", "Rhodok Light Spearman", "Rhodok Light Spearmen", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_54,
   [itm_war_spear, itm_tab_shield_pavise_b,itm_tab_shield_pavise_b_plain_1,itm_tab_shield_pavise_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_armor_herald, itm_aketon_green_herald, itm_ragged_outfit,
    itm_footman_helmet, itm_helmet_with_neckguard, itm_padded_coif, itm_common_hood_herald, itm_mail_coif,
    ],
   str_12|agi_11|int_7|cha_8|level(15), wpex(75,65,145,20,45,35), knows_common|knows_ironflesh_5|knows_power_strike_5|knows_athletics_5, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Light cavalry ranged, swords, picks, bows
  # SPECIAL
  ["rhodok_light_mounted_archer", "Rhodok Mounted Archer", "Rhodok Mounted Archer", tf_guarantee_recruit_armor|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_51,
   [itm_sword_medieval_a, itm_fighting_pick, itm_hunting_bow2, itm_barbed_arrows, itm_barbed_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_aketon_green_herald, itm_leather_armor_herald,
    itm_padded_coif, itm_common_hood_herald,
    itm_saddle_horse],
   str_9|agi_14|int_7|cha_7|level(14), wpex(60,50,55,120,50,30), knows_common|knows_power_strike_2|knows_power_draw_4|knows_athletics_3|knows_riding_5|knows_horse_archery_5, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Light infantry skirmisher, swords, picks, javelins, shields
  # SPECIAL
  ["rhodok_light_skirmisher", "Rhodok Light Skirmisher", "Rhodok Light Skirmisher", tf_guarantee_common_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_54,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_military_sickle_a, itm_javelin, itm_javelin, itm_tab_shield_pavise_b,itm_tab_shield_pavise_b_plain_1,itm_tab_shield_pavise_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_armor_herald,
    itm_footman_helmet, itm_padded_coif, itm_common_hood_herald, itm_mail_coif,
    ],
   str_11|agi_15|int_7|cha_6|level(16), wpex(85,70,90,20,45,80), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_3|knows_athletics_5, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Light cavalry, spears, shields
  # SPECIAL
  ["rhodok_light_cavalry", "Rhodok Light Cavalry", "Rhodok Light Cavalries", tf_guarantee_recruit_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_53,
   [itm_double_sided_spear, itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a_plain_1,itm_tab_shield_heater_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_aketon_green_herald, itm_leather_armor_herald,
    itm_padded_coif, itm_common_hood_herald, itm_footman_helmet, itm_mail_coif,
    itm_saddle_horse],
   str_12|agi_13|int_7|cha_7|level(16), wpex(85,70,145,20,40,40), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_athletics_4|knows_riding_6, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Light cavalry, lances
  # SPECIAL
  ["rhodok_scout", "Rhodok Scout", "Rhodok Scout", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_55,
   [itm_light_lance,
   itm_leather_boots, itm_leather_gloves,
    itm_leather_armor_herald,
    itm_padded_coif, itm_common_hood_herald,
    itm_saddle_horse],
   str_10|agi_14|int_7|cha_7|level(15), wpex(65,60,120,25,35,40), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_athletics_3|knows_riding_5, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Veteran
  # Medium infantry, swords, picks, shields
  ["rhodok_heavy_infantry", "Rhodok Heavy Swordsman", "Rhodok Heavy Swordsmen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_5,
   [itm_military_pick, itm_military_cleaver_b, itm_tab_shield_pavise_c,itm_tab_shield_pavise_c_plain_1,itm_tab_shield_pavise_c_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_byrnie_herald,
    itm_mail_coif, itm_kettle_hat, itm_helmet_with_neckguard,
    ],
   str_14|agi_12|int_8|cha_7|level(18), wpex(85,75,90,20,55,40), knows_common|knows_ironflesh_6|knows_power_strike_3|knows_athletics_3|knows_riding_1|knows_shield_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Medium infantry, spears, shields
  ["rhodok_spearman", "Rhodok Spearman", "Rhodok Spearmen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_5,
   [itm_war_spear, itm_tab_shield_pavise_c,itm_tab_shield_pavise_c_plain_1,itm_tab_shield_pavise_c_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_byrnie_herald,
    itm_mail_coif, itm_kettle_hat, itm_helmet_with_neckguard,
    ],
   str_16|agi_9|int_8|cha_10|level(20), wpex(80,70,140,20,50,40), knows_common|knows_ironflesh_6|knows_power_strike_4|knows_athletics_3|knows_riding_2|knows_shield_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Medium infantry skirmisher, 2h maces, javelins, shields
  ["rhodok_champion", "Rhodok Champion", "Rhodok Champions", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_5,
   [itm_sledgehammer, itm_javelin, itm_javelin, itm_tab_shield_pavise_b,itm_tab_shield_pavise_b_plain_1,itm_tab_shield_pavise_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_byrnie_herald,
    itm_mail_coif, itm_footman_helmet, itm_kettle_hat, itm_helmet_with_neckguard,
    ],
   str_15|agi_12|int_8|cha_7|level(19), wpex(85,100,95,25,55,70), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_2|knows_athletics_4, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Medium ranged, swords, picks, crossbows, shields
  ["rhodok_medium_crossbowman", "Rhodok Crossbowman", "Rhodok Crossbowmen", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_kingdom_5,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_military_sickle_a, itm_heavy_crossbow, itm_steel_bolts, itm_tab_shield_pavise_b,itm_tab_shield_pavise_b_plain_1,itm_tab_shield_pavise_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_aketon_green_herald, itm_ragged_outfit,
    itm_footman_helmet, itm_mail_coif, itm_helmet_with_neckguard, itm_kettle_hat,
    ],
   str_12|agi_14|int_8|cha_11|level(22), wpex(80,65,70,35,120,40), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_power_draw_1|knows_athletics_4|knows_riding_1|knows_horse_archery_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Medium cavalry, spears, shields
  ["rhodok_cavalry", "Rhodok Cavalry", "Rhodok Cavalries", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_5,
   [itm_double_sided_spear, itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a_plain_1,itm_tab_shield_heater_cav_a_plain_2,
    itm_mail_chausses, itm_mail_mittens, itm_leather_gloves,
    itm_byrnie_herald,
    itm_kettle_hat, itm_mail_coif, itm_helmet_with_neckguard,
    itm_pack_horse],
   str_15|agi_13|int_8|cha_8|level(21), wpex(90,75,135,25,40,40), knows_common|knows_ironflesh_7|knows_power_strike_4|knows_athletics_4|knows_riding_5, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Light cavalry, swords, picks, shields
  ["rhodok_medium_cavalry", "Rhodok Horseman", "Rhodok Horsemen", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_5,
   [itm_sword_medieval_b, itm_military_sickle_a, itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a_plain_1,itm_tab_shield_heater_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_aketon_green_herald, itm_ragged_outfit,
    itm_footman_helmet, itm_mail_coif, itm_helmet_with_neckguard, itm_kettle_hat,
    itm_pack_horse],
   str_13|agi_13|int_8|cha_8|level(19), wpex(90,80,90,25,40,45), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_athletics_3|knows_riding_4, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Light cavalry skirmisher, lances, javelins, shields
  ["rhodok_light_lancer", "Rhodok Light Lancer", "Rhodok Light Lancers", tf_guarantee_trained_armor|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_5,
   [itm_light_lance, itm_javelin, itm_javelin, itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a_plain_1,itm_tab_shield_heater_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_aketon_green_herald,
    itm_footman_helmet, itm_mail_coif, itm_helmet_with_neckguard,
    itm_courser],
   str_12|agi_15|int_7|cha_8|level(19), wpex(75,70,130,25,35,70), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_2|knows_athletics_2|knows_riding_5|knows_horse_archery_3, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Light cavalry ranged, swords, picks, crossbows, shields
  # SPECIAL
  ["rhodok_mounted_crossbow", "Rhodok Mounted Crossbowman", "Rhodok Mounted Crossbowmen", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_54,
   [itm_sword_medieval_b, itm_military_sickle_a, itm_light_crossbow, itm_steel_bolts, itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a_plain_1,itm_tab_shield_heater_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_aketon_green_herald, itm_ragged_outfit,
    itm_footman_helmet, itm_mail_coif, itm_helmet_with_neckguard,
    itm_pack_horse],
   str_11|agi_15|int_8|cha_9|level(20), wpex(80,65,70,35,125,40), knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_4|knows_horse_archery_5, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Medium ranged, swords, picks, bows, shields
  # SPECIAL
  ["rhodok_bowman", "Rhodok Bowman", "Rhodok Bowmen", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_51,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_military_sickle_a, itm_short_bow2, itm_bodkin_arrows, itm_tab_shield_pavise_c,itm_tab_shield_pavise_c_plain_1,itm_tab_shield_pavise_c_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_byrnie_herald,
    itm_helmet_with_neckguard, itm_kettle_hat,
    ],
   str_12|agi_16|int_8|cha_11|level(24), wpex(75,60,65,115,60,40), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_draw_4|knows_athletics_3|knows_riding_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Elite
  # Heavy infantry, spears
  ["rhodok_heavy_pikeman", "Rhodok Heavy Pikeman", "Rhodok Heavy Pikemen", tf_guarantee_trained_armor, no_scene, reserved, fac_kingdom_5,
   [itm_pike,
    itm_iron_greaves, itm_mail_boots, itm_mail_mittens, itm_gauntlets,
    itm_surcoat_over_mail_herald,
    itm_bascinet_2, itm_bascinet_3, itm_guard_helmet, itm_bascinet,
    ],
   str_20|agi_10|int_9|cha_12|level(28), wpex(95,80,150,25,60,40), knows_common|knows_ironflesh_9|knows_power_strike_5|knows_power_throw_1|knows_athletics_1|knows_riding_3, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Medium ranged, swords, picks, crossbows, shields
  ["rhodok_heavy_crossbowman", "Rhodok Heavy Crossbowman", "Rhodok Heavy Crossbowmen", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_kingdom_5,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_military_cleaver_a, itm_military_sickle_a, itm_siege_crossbow, itm_steel_bolts, itm_tab_shield_pavise_c,itm_tab_shield_pavise_c_plain_1,itm_tab_shield_pavise_c_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_byrnie_herald,
    itm_helmet_with_neckguard, itm_kettle_hat,
    ],
   str_16|agi_13|int_10|cha_13|level(29), wpex(95,75,80,40,110,45), knows_common|knows_ironflesh_6|knows_power_strike_3|knows_power_draw_1|knows_athletics_2|knows_riding_2|knows_horse_archery_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Heavy ranged, swords, picks, bows, shields
  # SPECIAL
  ["rhodok_heavy_bowman", "Rhodok Heavy Bowman", "Rhodok Heavy Bowmen", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_51,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_military_cleaver_a, itm_military_sickle_a, itm_short_bow2, itm_bodkin_arrows, itm_tab_shield_pavise_c,itm_tab_shield_pavise_c_plain_1,itm_tab_shield_pavise_c_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_surcoat_over_mail_herald,
    itm_bascinet_2, itm_bascinet_3, itm_guard_helmet, itm_bascinet,
    ],
   str_16|agi_15|int_10|cha_13|level(31), wpex(90,70,75,110,65,45), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_power_draw_4|knows_athletics_2|knows_riding_2|knows_horse_archery_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Medium cavalry, swords, picks, shields
  # SPECIAL
  ["rhodok_heavy_cavalry", "Rhodok Heavy Cavalry", "Rhodok Heavy Cavalries", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_53,
   [itm_double_sided_spear, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_surcoat_over_mail_herald,
    itm_guard_helmet, itm_bascinet,
    itm_hunter],
   str_18|agi_14|int_9|cha_11|level(29), wpex(90,70,130,40,60,45), knows_common|knows_ironflesh_9|knows_power_strike_4|knows_power_draw_1|knows_athletics_3|knows_riding_5|knows_horse_archery_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Heavy infantry, spears, shields
  # SPECIAL
  ["rhodok_heavy_spearman", "Rhodok Heavy Spearman", "Rhodok Heavy Spearmen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_54,
   [itm_war_spear, itm_tab_shield_pavise_c,itm_tab_shield_pavise_c_plain_1,itm_tab_shield_pavise_c_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_surcoat_over_mail_herald,
    itm_bascinet_2, itm_bascinet_3, itm_guard_helmet, itm_bascinet,
    ],
   str_19|agi_13|int_10|cha_13|level(32), wpex(95,80,150,40,60,40), knows_common|knows_ironflesh_8|knows_power_strike_4|knows_power_throw_1|knows_athletics_3|knows_riding_3|knows_shield_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Medium cavalry, lances, shields
  # SPECIAL
  ["rhodok_lancer", "Rhodok Heavy Lancer", "Rhodok Heavy Lancers", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_55,
   [itm_lance, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_byrnie_herald,
    itm_helmet_with_neckguard, itm_kettle_hat,
    itm_hunter],
   str_14|agi_15|int_9|cha_10|level(25), wpex(85,80,130,40,60,50), knows_common|knows_ironflesh_7|knows_power_strike_4|knows_athletics_2|knows_riding_4|knows_horse_archery_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Heavy infantry, picks, maces, shields
  # SPECIAL
  ["rhodok_sergeant", "Rhodok Sergeant", "Rhodok Sergeants", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_51,
   [itm_military_pick, itm_military_hammer, itm_tab_shield_pavise_c,itm_tab_shield_pavise_c_plain_1,itm_tab_shield_pavise_c_plain_2,
    itm_mail_chausses, itm_mail_boots, itm_mail_mittens,
    itm_scale_armor_herald, itm_surcoat_over_mail_herald,
    itm_bascinet_2, itm_bascinet_3, itm_guard_helmet, itm_bascinet,
    ],
   str_19|agi_12|int_9|cha_12|level(29), wpex(105,90,100,50,65,45), knows_common|knows_ironflesh_8|knows_power_strike_3|knows_power_throw_1|knows_power_draw_2|knows_athletics_2|knows_riding_3|knows_shield_1, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Medium cavalry ranged, swords, picks, crossbows, shields
  # SPECIAL
  ["rhodok_heavy_mounted_crossbow", "Rhodok Heavy Mounted Crossbowman", "Rhodok Heavy Mounted Crossbowmen", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_54,
   [itm_sword_medieval_b, itm_military_sickle_a, itm_light_crossbow, itm_steel_bolts, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_byrnie_herald,
    itm_helmet_with_neckguard, itm_kettle_hat, itm_mail_coif,
    itm_hunter],
   str_14|agi_15|int_10|cha_11|level(27), wpex(95,75,80,40,120,45), knows_common|knows_ironflesh_4|knows_power_strike_2|knows_athletics_2|knows_riding_4|knows_horse_archery_5, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Medium cavalry, swords, picks, shields
  # SPECIAL
  ["rhodok_heavy_horseman", "Rhodok Heavy Horseman", "Rhodok Heavy Horsemen", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_52,
   [itm_sword_medieval_b, itm_military_sickle_a, itm_military_cleaver_a, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_byrnie_herald,
    itm_helmet_with_neckguard, itm_kettle_hat,
    itm_hunter],
   str_15|agi_14|int_9|cha_10|level(25), wpex(95,90,95,40,60,45), knows_common|knows_ironflesh_6|knows_power_strike_3|knows_athletics_3|knows_riding_4|knows_horse_archery_1, rhodok_face_young_1, rhodok_face_old_2 ],
   
  # Noble
  # Heavy infantry, swords, picks, 2h swords, crossbows, shields
  ["rhodok_noble", "Rhodok Hero", "Rhodok Heroes", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_5,
   [itm_military_cleaver_b, itm_two_handed_cleaver, itm_military_pick, itm_heavy_crossbow, itm_steel_bolts, itm_tab_shield_pavise_d,itm_tab_shield_pavise_d_plain_1,itm_tab_shield_pavise_d_plain_2, itm_tab_shield_pavise_c,itm_tab_shield_pavise_c_plain_1,itm_tab_shield_pavise_c_plain_2,
    itm_mail_boots, itm_iron_greaves, itm_mail_mittens, itm_gauntlets,
    itm_surcoat_over_mail_herald, itm_scale_armor_herald, itm_coat_of_plates_herald,
    itm_full_helm_herald, itm_bascinet_2, itm_bascinet_3, itm_guard_helmet, itm_bascinet,
    ],
   str_21|agi_15|int_13|cha_16|level(42), wpex(115,100,110,45,95,55), knows_common|knows_ironflesh_8|knows_power_strike_5|knows_power_throw_1|knows_power_draw_2|knows_athletics_4|knows_riding_3|knows_shield_1|knows_horse_archery_2, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Heavy cavalry, spears, shields
  # SPECIAL
  ["rhodok_noble_cavalry", "Rhodok Heroic Cavalry", "Rhodok Heroic Cavalries", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_53,
   [itm_double_sided_spear, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_mail_boots, itm_iron_greaves, itm_mail_mittens, itm_gauntlets,
    itm_coat_of_plates_herald,
    itm_full_helm_herald, itm_bascinet_2, itm_bascinet_3, itm_guard_helmet, itm_bascinet,
    itm_warhorse],
   str_23|agi_16|int_13|cha_16|level(45), wpex(105,100,145,45,90,55), knows_common|knows_ironflesh_10|knows_power_strike_5|knows_power_throw_1|knows_power_draw_2|knows_athletics_4|knows_riding_6|knows_horse_archery_2, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Heavy cavalry, swords, picks, morningstars, shields
  # SPECIAL
  ["rhodok_noble_horseman", "Rhodok Heroic Horseman", "Rhodok Heroic Horsemen", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_52,
   [itm_military_cleaver_b, itm_morningstar, itm_military_pick, itm_sword_medieval_b, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_surcoat_over_mail_herald, itm_scale_armor_herald,
    itm_full_helm_herald, itm_bascinet_2, itm_bascinet_3, itm_guard_helmet, itm_bascinet,
    itm_hunter],
   str_18|agi_18|int_12|cha_15|level(40), wpex(105,100,105,45,90,55), knows_common|knows_ironflesh_7|knows_power_strike_4|knows_power_throw_1|knows_power_draw_2|knows_athletics_3|knows_riding_5|knows_horse_archery_2, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Heavy cavalry, lances, shields
  # SPECIAL
  ["rhodok_noble_lancer", "Rhodok Heroic Lancer", "Rhodok Heroic Lancers", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_55,
   [itm_heavy_lance, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_surcoat_over_mail_herald, itm_scale_armor_herald,
    itm_full_helm_herald, itm_bascinet_2, itm_bascinet_3, itm_guard_helmet, itm_bascinet,
    itm_warhorse],
   str_23|agi_17|int_14|cha_16|level(47), wpex(95,90,140,45,90,60), knows_common|knows_ironflesh_8|knows_power_strike_6|knows_power_throw_1|knows_power_draw_2|knows_athletics_2|knows_riding_5|knows_horse_archery_2, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Heavy infantry, picks, maces, shields
  # SPECIAL
  ["rhodok_highlander", "Rhodok Highlander", "Rhodok Highlancers", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_51,
   [itm_military_pick, itm_military_hammer, itm_tab_shield_pavise_d,itm_tab_shield_pavise_d_plain_1,itm_tab_shield_pavise_d_plain_2,
    itm_iron_greaves, itm_mail_mittens, itm_gauntlets,
    itm_coat_of_plates_herald, itm_scale_armor_herald,
    itm_full_helm_herald, itm_bascinet_2, itm_bascinet_3, itm_guard_helmet, itm_bascinet,
    ],
   str_25|agi_14|int_13|cha_16|level(45), wpex(110,95,105,55,70,50), knows_common|knows_ironflesh_10|knows_power_strike_4|knows_power_throw_1|knows_power_draw_2|knows_athletics_3|knows_riding_3|knows_shield_1|knows_horse_archery_2, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Heavy cavalry ranged, swords, picks, crossbows, shields
  # SPECIAL
  ["rhodok_noble_mounted_crossbow", "Rhodok Heroic Mounted Crossbowman", "Rhodok Heroic Mounted Crossbowmen", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_54,
   [itm_sword_medieval_b, itm_military_pick, itm_light_crossbow, itm_steel_bolts, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_surcoat_over_mail_herald,
    itm_full_helm_herald, itm_bascinet_2, itm_bascinet_3, itm_guard_helmet, itm_bascinet,
    itm_hunter],
   str_16|agi_18|int_12|cha_16|level(39), wpex(105,100,105,45,140,55), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_athletics_3|knows_riding_5|knows_horse_archery_6, rhodok_face_young_1, rhodok_face_old_2 ],
  
  # Heavy ranged, spears, crossbows
  # SPECIAL
  ["rhodok_noble_pikeman", "Rhodok Heroic Pikeman", "Rhodok Heroic Pikemen", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_small_kingdom_52,
   [itm_pike, itm_siege_crossbow, itm_steel_bolts, itm_steel_bolts,
    itm_iron_greaves, itm_gauntlets,
    itm_coat_of_plates_herald, itm_scale_armor_herald,
    itm_full_helm_herald, itm_bascinet_2, itm_bascinet_3, itm_guard_helmet,
    ],
   str_32|agi_16|int_12|cha_18|level(55), wpex(100,95,170,45,130,55), knows_common|knows_ironflesh_10|knows_power_strike_5|knows_power_throw_1|knows_power_draw_2|knows_athletics_2|knows_riding_3|knows_horse_archery_2, rhodok_face_young_1, rhodok_face_old_2 ],
  
  #############
  # Sarranids #
  #############
  # Peasant
  # Basic infantry, swords, maces
  ["sarranid_levy", "Sarranid Levy", "Sarranid Levies", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_6,
   [itm_arabian_sword_a, itm_mace_2, itm_tab_shield_kite_a,itm_tab_shield_kite_a_plain_1,itm_tab_shield_kite_a_plain_2,
    itm_sarranid_boots_a, itm_sarranid_boots_b,
    itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b, itm_skirmisher_armor,
    itm_sarranid_felt_hat, itm_turban, itm_desert_turban,
    ],
   str_9|agi_10|int_5|cha_6|level(7), wpex(70,60,65,25,15,40), knows_common|knows_ironflesh_1|knows_power_strike_4|knows_athletics_4|knows_riding_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Basic ranged, daggers, maces, bows
  ["sarranid_militia", "Sarranid Militia", "Sarranid Militias", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_6,
   [itm_mace_2, itm_butchering_knife, itm_knife, itm_hunting_bow2, itm_arrows_b,
    itm_sarranid_boots_a, itm_sarranid_boots_b,
    itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b,
    itm_sarranid_felt_hat, itm_turban, itm_desert_turban,
    ],
   str_9|agi_9|int_5|cha_5|level(5), wpex(55,45,45,80,20,35), knows_common|knows_power_strike_2|knows_power_draw_4|knows_athletics_3, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Light infantry, swords, maces, javelins, shields
  ["sarranid_light_infantry", "Sarranid Light Infantry", "Sarranid Light Infantries", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_6,
   [itm_arabian_sword_a, itm_mace_2, itm_javelin, itm_tab_shield_kite_a,itm_tab_shield_kite_a_plain_1,itm_tab_shield_kite_a_plain_2,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_skirmisher_armor,
    itm_turban, itm_desert_turban, itm_sarranid_warrior_cap,
    ],
   str_11|agi_12|int_5|cha_6|level(11), wpex(65,60,60,30,15,65), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_throw_2|knows_athletics_4|knows_riding_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Basic cavalry, swords, maces
  # SPECIAL
  ["sarranid_levy_horse", "Sarranid Levy Horseman", "Sarranid Levy Horsemen", tf_guarantee_recruit_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_61,
   [itm_arabian_sword_a, itm_mace_2, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_sarranid_boots_a, itm_sarranid_boots_b,
    itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b, itm_skirmisher_armor,
    itm_sarranid_felt_hat, itm_turban, itm_desert_turban,
    itm_arabian_horse_a],
   str_8|agi_12|int_5|cha_6|level(8), wpex(65,55,60,25,15,40), knows_common|knows_power_strike_3|knows_athletics_3|knows_riding_5, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Basic infantry, spears, shields
  # SPECIAL
  ["sarranid_levy_spearman", "Sarranid Levy Spearman", "Sarranid Levy Spearmen", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_62,
   [itm_spear, itm_tab_shield_kite_a,itm_tab_shield_kite_a_plain_1,itm_tab_shield_kite_a_plain_2,
    itm_sarranid_boots_a, itm_sarranid_boots_b,
    itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b, itm_skirmisher_armor,
    itm_sarranid_felt_hat, itm_turban, itm_desert_turban,
    ],
   str_9|agi_9|int_5|cha_5|level(5), wpex(65,65,85,25,15,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_athletics_4|knows_riding_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Common
  # Light infantry, swords, maces, axes, spears, shields
  ["sarranid_medium_infantry", "Sarranid Infantry", "Sarranid Infantries", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_6,
   [itm_arabian_sword_b, itm_mace_3, itm_sarranid_axe_a, itm_tab_shield_tear_b,itm_tab_shield_tear_b,itm_tab_shield_tear_a_plain_1,itm_tab_shield_tear_a_plain_2,itm_tab_shield_tear_b_plain_1,itm_tab_shield_tear_b_plain_2,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_archers_vest,
    itm_desert_turban, itm_sarranid_warrior_cap,
    ],
   str_13|agi_15|int_7|cha_7|level(19), wpex(100,95,115,40,15,50), knows_common|knows_ironflesh_2|knows_power_strike_5|knows_power_throw_1|knows_athletics_6|knows_riding_2, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Light infantry skirmisher, swords, javelins, shields
  ["sarranid_light_skirmisher", "Sarranid Light Skirmisher", "Sarranid Light Skirmishers", tf_guarantee_common_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_kingdom_6,
   [itm_arabian_sword_a, itm_mace_3, itm_javelin, itm_javelin, itm_tab_shield_tear_b,itm_tab_shield_tear_b,itm_tab_shield_tear_a_plain_1,itm_tab_shield_tear_a_plain_2,itm_tab_shield_tear_b_plain_1,itm_tab_shield_tear_b_plain_2,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_archers_vest, itm_skirmisher_armor,
    itm_turban, itm_desert_turban,
    ],
   str_11|agi_17|int_5|cha_8|level(18), wpex(75,70,70,40,20,130), knows_common|knows_ironflesh_1|knows_power_strike_5|knows_power_throw_3|knows_athletics_6|knows_riding_2, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Light cavalry skirmisher, swords, maces, javelins, shields
  ["sarranid_light_cavalry", "Sarranid Light Cavalry", "Sarranid Light Cavalries", tf_guarantee_common_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_6,
   [itm_arabian_sword_a, itm_mace_3, itm_javelin, itm_javelin, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_skirmisher_armor, itm_archers_vest,
    itm_desert_turban, itm_sarranid_warrior_cap,
    itm_arabian_horse_a],
   str_10|agi_17|int_6|cha_9|level(19), wpex(80,70,75,40,20,115), knows_common|knows_ironflesh_1|knows_power_strike_4|knows_power_throw_3|knows_athletics_5|knows_riding_6|knows_horse_archery_5, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Light cavalry, lances, shields
  ["sarranid_light_lancer", "Sarranid Light Lancer", "Sarranid Light Lancers", tf_guarantee_recruit_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_6,
   [itm_light_lance, itm_tab_shield_small_round_a,itm_tab_shield_small_round_a_plain_1,itm_tab_shield_small_round_a_plain_2,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b,
    itm_turban, itm_desert_turban,
    itm_arabian_horse_b],
   str_12|agi_18|int_6|cha_7|level(20), wpex(85,80,120,40,15,60), knows_common|knows_power_strike_4|knows_power_throw_1|knows_athletics_5|knows_riding_6, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Light ranged, swords, maces, bows
  ["sarranid_light_bowman", "Sarranid Light Archer", "Sarranid Light Archers", tf_guarantee_common_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_6,
   [itm_arabian_sword_a, itm_mace_3, itm_short_bow2, itm_barbed_arrows, itm_barbed_arrows,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_archers_vest,
    itm_turban, itm_desert_turban, itm_sarranid_warrior_cap,
    ],
   str_10|agi_15|int_6|cha_8|level(16), wpex(75,65,70,135,25,45), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_6|knows_riding_3, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Light ranged, swords, maces, crossbows, shields
  # SPECIAL
  ["sarranid_light_crossbowman", "Sarranid Light Crossbowman", "Sarranid Light Crossbowmen", tf_guarantee_common_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_64,
   [itm_arabian_sword_a, itm_mace_3, itm_crossbow, itm_bolts, itm_tab_shield_tear_b,itm_tab_shield_tear_b,itm_tab_shield_tear_a_plain_1,itm_tab_shield_tear_a_plain_2,itm_tab_shield_tear_b_plain_1,itm_tab_shield_tear_b_plain_2,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_archers_vest,
    itm_turban, itm_desert_turban, itm_sarranid_warrior_cap,
    ],
   str_12|agi_13|int_6|cha_6|level(14), wpex(80,65,65,40,100,50), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_throw_1|knows_athletics_5|knows_riding_2, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Light cavalry ranged, swords, maces, bows
  # SPECIAL
  ["sarranid_light_horse_archer", "Sarranid Light Horse Archer", "Sarranid Light Horse Archers", tf_guarantee_common_armor|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_61,
   [itm_arabian_sword_a, itm_mace_3, itm_short_bow2, itm_barbed_arrows, itm_barbed_arrows,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_archers_vest,
    itm_turban, itm_desert_turban, itm_sarranid_warrior_cap,
    itm_arabian_horse_a],
   str_9|agi_16|int_6|cha_8|level(16), wpex(70,60,65,130,20,40), knows_common|knows_power_strike_2|knows_power_draw_4|knows_athletics_5|knows_riding_6|knows_horse_archery_6, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Light infantry, spears
  # SPECIAL
  ["sarranid_pikeman", "Sarranid Pikeman", "Sarranid Pikemen", tf_guarantee_common_armor, no_scene, reserved, fac_small_kingdom_65,
   [itm_pike,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_sarranid_leather_armor,
    itm_desert_turban, itm_sarranid_warrior_cap,
    ],
   str_13|agi_13|int_8|cha_6|level(17), wpex(95,80,130,40,15,50), knows_common|knows_ironflesh_3|knows_power_strike_5|knows_power_throw_1|knows_athletics_4|knows_riding_2, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Light infantry, swords, maces, axes, shields
  # SPECIAL
  ["sarranid_footman", "Sarranid Footman", "Sarranid Footmen", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_63,
   [itm_arabian_sword_b, itm_mace_3, itm_sarranid_axe_a, itm_tab_shield_tear_b,itm_tab_shield_tear_b,itm_tab_shield_tear_a_plain_1,itm_tab_shield_tear_a_plain_2,itm_tab_shield_tear_b_plain_1,itm_tab_shield_tear_b_plain_2,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_sarranid_leather_armor,
    itm_desert_turban, itm_sarranid_warrior_cap,
    ],
   str_15|agi_14|int_7|cha_7|level(20), wpex(110,105,105,40,15,50), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_1|knows_athletics_5|knows_riding_2, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Light infantry, spears, shields
  # SPECIAL
  ["sarranid_light_spearman", "Sarranid Light Spearman", "Sarranid Light Spearmen", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_62,
   [itm_spear, itm_tab_shield_tear_b,itm_tab_shield_tear_b,itm_tab_shield_tear_a_plain_1,itm_tab_shield_tear_a_plain_2,itm_tab_shield_tear_b_plain_1,itm_tab_shield_tear_b_plain_2,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_archers_vest,
    itm_desert_turban, itm_sarranid_warrior_cap,
    ],
   str_14|agi_14|int_6|cha_6|level(18), wpex(100,95,125,40,15,50), knows_common|knows_ironflesh_3|knows_power_strike_5|knows_power_throw_1|knows_athletics_6|knows_riding_2, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Veteran
  # Medium infantry, swords, maces, axes, javelins, shields
  ["sarranid_guard", "Sarranid Guard", "Sarranid Guards", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_6,
   [itm_arabian_sword_d, itm_mace_4, itm_sarranid_axe_a, itm_javelin, itm_tab_shield_tear_d,itm_tab_shield_tear_d,itm_tab_shield_tear_c_plain_1,itm_tab_shield_tear_c_plain_2,itm_tab_shield_tear_d_plain_1,itm_tab_shield_tear_d_plain_2,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_arabian_armor_b_herald,
    itm_sarranid_helmet1, itm_sarranid_mail_coif,
    ],
   str_15|agi_16|int_8|cha_9|level(25), wpex(120,105,105,45,15,90), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_athletics_5|knows_riding_3|knows_shield_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Medium infantry, 2h axes
  ["sarranid_champion", "Sarranid Champion", "Sarranid Champions", tf_guarantee_trained_armor, no_scene, reserved, fac_kingdom_6,
   [itm_two_handed_iron_mace, itm_sarranid_two_handed_axe_a,
    itm_sarranid_boots_c, itm_sarranid_boots_b, itm_leather_gloves,
    itm_arabian_armor_b_herald, itm_sarranid_cavalry_robe,
    itm_sarranid_warrior_cap, itm_sarranid_helmet1,
    ],
   str_13|agi_16|int_7|cha_9|level(22), wpex(95,125,100,45,15,60), knows_common|knows_ironflesh_3|knows_power_strike_5|knows_power_throw_1|knows_athletics_5|knows_riding_2, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Light ranged, swords, maces, bows
  ["sarranid_bowman", "Sarranid Archer", "Sarranid Archers", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_6,
   [itm_arabian_sword_b, itm_mace_4, itm_nomad_bow2, itm_bodkin_arrows, itm_bodkin_arrows,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_arabian_armor_b_herald, itm_sarranid_cavalry_robe,
    itm_sarranid_warrior_cap, itm_sarranid_helmet1, itm_sarranid_mail_coif,
    ],
   str_12|agi_18|int_7|cha_9|level(23), wpex(85,75,70,120,25,45), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_5|knows_athletics_4|knows_riding_3, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Medium infantry skirmisher, swords, maces, javelins
  ["sarranid_heavy_skirmisher", "Sarranid Heavy Skirmisher", "Sarranid Heavy Skirmishers", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_6,
   [itm_arabian_sword_b, itm_mace_4, itm_jarid, itm_jarid,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_arabian_armor_b_herald,
    itm_sarranid_warrior_cap, itm_sarranid_helmet1, itm_sarranid_mail_coif,
    ],
   str_14|agi_16|int_8|cha_9|level(24), wpex(85,80,80,45,20,110), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_4|knows_athletics_5|knows_riding_3|knows_horse_archery_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Medium cavalry, swords, maces, axes, javelins, shields
  ["sarranid_medium_cavalry", "Sarranid Cavalry", "Sarranid Cavalries", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_6,
   [itm_sarranid_cavalry_sword, itm_mace_4, itm_sarranid_axe_a, itm_javelin, itm_tab_shield_small_round_b,itm_tab_shield_small_round_b_plain_1,itm_tab_shield_small_round_b_plain_2,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_sarranid_cavalry_robe, itm_arabian_armor_b_herald,
    itm_sarranid_helmet1, itm_sarranid_mail_coif, itm_sarranid_horseman_helmet,
    itm_arabian_horse_b, itm_arabian_horse_a],
   str_15|agi_16|int_8|cha_10|level(26), wpex(115,95,100,40,15,80), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_athletics_3|knows_riding_6|knows_horse_archery_3, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Light cavalry skirmisher, swords, maces, javelins, shields
  # SPECIAL
  ["sarranid_mounted_skirmisher", "Sarranid Mounted Skirmisher", "Sarranid Mounted Skirmishers", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_65,
   [itm_sarranid_cavalry_sword, itm_mace_4, itm_javelin, itm_javelin, itm_tab_shield_small_round_b,itm_tab_shield_small_round_b_plain_1,itm_tab_shield_small_round_b_plain_2,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_sarranid_leather_armor,
    itm_desert_turban, itm_sarranid_warrior_cap,
    itm_arabian_horse_b],
   str_12|agi_18|int_8|cha_9|level(24), wpex(95,90,90,45,20,125), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_3|knows_athletics_4|knows_riding_6|knows_horse_archery_6, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Medium cavalry, lances, shields
  # SPECIAL
  ["sarranid_heavy_lancer", "Sarranid Heavy Lancer", "Sarranid Heavy Lancers", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_63,
   [itm_lance, itm_tab_shield_small_round_b,itm_tab_shield_small_round_b_plain_1,itm_tab_shield_small_round_b_plain_2,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_sarranid_cavalry_robe, itm_arabian_armor_b_herald,
    itm_sarranid_helmet1, itm_sarranid_mail_coif, itm_sarranid_horseman_helmet,
    itm_arabian_horse_b],
   str_15|agi_18|int_8|cha_9|level(27), wpex(90,85,115,45,20,60), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_athletics_3|knows_riding_6|knows_horse_archery_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Medium cavalry ranged, swords, maces, bows
  # SPECIAL
  ["sarranid_horse_archer", "Sarranid Horse Archer", "Sarranid Horse Archers", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_61,
   [itm_arabian_sword_b, itm_mace_4, itm_nomad_bow2, itm_bodkin_arrows, itm_bodkin_arrows,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_arabian_armor_b_herald, itm_sarranid_cavalry_robe,
    itm_sarranid_warrior_cap, itm_sarranid_helmet1, itm_sarranid_mail_coif,
    itm_arabian_horse_a, itm_arabian_horse_b],
   str_11|agi_18|int_7|cha_9|level(22), wpex(80,70,65,115,25,45), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_5|knows_athletics_4|knows_riding_6|knows_horse_archery_5, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Medium infantry, spears
  # SPECIAL
  ["sarranid_heavy_pikeman", "Sarranid Heavy Pikeman", "Sarranid Heavy Pikemen", tf_guarantee_trained_armor, no_scene, reserved, fac_small_kingdom_65,
   [itm_pike,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_arabian_armor_b_herald,
    itm_sarranid_helmet1, itm_sarranid_mail_coif,
    ],
   str_16|agi_14|int_9|cha_7|level(23), wpex(90,75,120,45,20,55), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_1|knows_athletics_3|knows_riding_2, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Medium ranged, swords, maces, crossbows, shields
  # SPECIAL
  ["sarranid_crossbowman", "Sarranid Crossbowman", "Sarranid Light Crossbowmen", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_64,
   [itm_arabian_sword_b, itm_mace_4, itm_crossbow, itm_steel_bolts, itm_tab_shield_tear_d,itm_tab_shield_tear_d,itm_tab_shield_tear_c_plain_1,itm_tab_shield_tear_c_plain_2,itm_tab_shield_tear_d_plain_1,itm_tab_shield_tear_d_plain_2,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_arabian_armor_b_herald, itm_sarranid_cavalry_robe,
    itm_sarranid_warrior_cap, itm_sarranid_helmet1, itm_sarranid_mail_coif,
    ],
   str_15|agi_15|int_7|cha_8|level(22), wpex(90,75,75,40,90,50), knows_common|knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_athletics_3|knows_riding_2, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Medium infantry, swords, maces, axes, shields
  # SPECIAL
  # ["sarranid_warrior", "Sarranid Warrior", "Sarranid Warriors", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_63,
  #  [itm_arabian_sword_d, itm_mace_4, itm_sarranid_axe_a, itm_tab_shield_kite_c,itm_tab_shield_kite_c_plain_1,itm_tab_shield_kite_c_plain_2,
  #   itm_sarranid_boots_c, itm_leather_gloves,
  #   itm_arabian_armor_b_herald, itm_sarranid_mail_shirt,
  #   itm_sarranid_helmet1, itm_sarranid_mail_coif,
  #   ],
  #  str_16|agi_16|int_8|cha_9|level(26), wpex(115,105,105,45,15,55), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_athletics_4|knows_riding_3|knows_shield_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Medium infantry skirmisher, swords, maces, javelins, shields
  # SPECIAL
  ["sarranid_skirmisher", "Sarranid Skirmisher", "Sarranid Skirmishers", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_63,
   [itm_arabian_sword_b, itm_mace_4, itm_javelin, itm_javelin, itm_tab_shield_tear_d,itm_tab_shield_tear_d,itm_tab_shield_tear_c_plain_1,itm_tab_shield_tear_c_plain_2,itm_tab_shield_tear_d_plain_1,itm_tab_shield_tear_d_plain_2,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_sarranid_cavalry_robe,
    itm_sarranid_warrior_cap, itm_sarranid_helmet1, itm_sarranid_mail_coif,
    ],
   str_13|agi_16|int_8|cha_9|level(23), wpex(85,80,80,45,20,115), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_3|knows_athletics_5|knows_riding_3|knows_horse_archery_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Medium infantry, spears, shields
  # SPECIAL
  ["sarranid_medium_spearman", "Sarranid Spearman", "Sarranid Spearmen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_62,
   [itm_war_spear, itm_tab_shield_tear_d,itm_tab_shield_tear_d,itm_tab_shield_tear_c_plain_1,itm_tab_shield_tear_c_plain_2,itm_tab_shield_tear_d_plain_1,itm_tab_shield_tear_d_plain_2,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_arabian_armor_b_herald,
    itm_sarranid_helmet1, itm_sarranid_mail_coif,
    ],
   str_16|agi_15|int_7|cha_8|level(23), wpex(105,105,120,45,15,55), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_power_throw_2|knows_athletics_5|knows_riding_3|knows_shield_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Elite
  # Medium infantry, swords, maces, axes, shields
  ["sarranid_heavy_infantry", "Sarranid Heavy Infantry", "Sarranid Heavy Infantries", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_6,
   [itm_arabian_sword_d, itm_iron_mace, itm_sarranid_axe_b, itm_tab_shield_tear_d,itm_tab_shield_tear_d_plain_1,itm_tab_shield_tear_d_plain_2,
    itm_sarranid_boots_d, itm_mail_mittens,
    itm_sarranid_mail_shirt,
    itm_sarranid_veiled_helmet,
    ],
   str_17|agi_18|int_8|cha_10|level(30), wpex(110,100,100,50,20,60), knows_common|knows_ironflesh_6|knows_power_strike_3|knows_power_throw_1|knows_athletics_4|knows_riding_3|knows_shield_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Heavy cavalry, sword, maces, axes, shields
  ["sarranid_heavy_cavalry", "Sarranid Mamluke", "Sarranid Mamlukes", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_6,
   [itm_sarranid_cavalry_sword, itm_iron_mace, itm_sarranid_axe_b, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_sarranid_boots_d, itm_mail_mittens,
    itm_sarranid_mail_shirt, itm_mamluke_mail_herald,
    itm_sarranid_veiled_helmet,
    itm_arabian_horse_b],
   str_16|agi_16|int_9|cha_13|level(31), wpex(105,95,100,45,15,65), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_power_throw_1|knows_athletics_2|knows_riding_6|knows_shield_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Medium ranged, swords, maxes, bows, shields
  # SPECIAL
  ["sarranid_heavy_archer", "Sarranid Heavy Archer", "Sarranid Heavy Archers", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_62,
   [itm_arabian_sword_d, itm_mace_4, itm_sarranid_axe_a, itm_strong_bow2, itm_bodkin_arrows, itm_tab_shield_tear_d,itm_tab_shield_tear_d_plain_1,itm_tab_shield_tear_d_plain_2,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_arabian_armor_b_herald,
    itm_sarranid_helmet1, itm_sarranid_mail_coif,
    ],
   str_15|agi_18|int_9|cha_10|level(29), wpex(95,75,75,110,25,70), knows_common|knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_power_draw_5|knows_athletics_4|knows_riding_3|knows_horse_archery_2, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Medium cavalry ranged, swords, maces, bows, shields
  # SPECIAL
  ["sarranid_heavy_horse_archer", "Sarranid Heavy Horse Archer", "Sarranid Heavy Horse Archers", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_61,
   [itm_sarranid_cavalry_sword, itm_mace_4, itm_sarranid_axe_a, itm_strong_bow2, itm_bodkin_arrows, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_arabian_armor_b_herald,
    itm_sarranid_helmet1, itm_sarranid_mail_coif,
    itm_arabian_horse_b],
   str_14|agi_19|int_9|cha_10|level(29), wpex(90,75,75,105,25,70), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_draw_5|knows_athletics_3|knows_riding_6|knows_horse_archery_5, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Heavy infantry, swords, maces, axes, shields
  # SPECIAL
  ["sarranid_sergeant", "Sarranid Sergeant", "Sarranid Sergeants", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_63,
   [itm_arabian_sword_d, itm_iron_mace, itm_sarranid_axe_b, itm_sarranid_two_handed_axe_b, itm_two_handed_iron_mace, itm_tab_shield_tear_d,itm_tab_shield_tear_d_plain_1,itm_tab_shield_tear_d_plain_2,
    itm_sarranid_boots_d, itm_mail_mittens,
    itm_mamluke_mail_herald,
    itm_sarranid_veiled_helmet,
    ],
   str_19|agi_17|int_9|cha_10|level(32), wpex(110,110,100,50,20,60), knows_common|knows_ironflesh_6|knows_power_strike_3|knows_power_throw_1|knows_athletics_3|knows_riding_3|knows_shield_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Heavy infantry, spears, shields
  # SPECIAL
  ["sarranid_heavy_spearman", "Sarranid Heavy Spearman", "Sarranid Heavy Spearmen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_small_kingdom_62,
   [itm_war_spear, itm_tab_shield_tear_d,itm_tab_shield_tear_d_plain_1,itm_tab_shield_tear_d_plain_2,
    itm_sarranid_boots_d, itm_mail_mittens,
    itm_sarranid_mail_shirt,
    itm_sarranid_veiled_helmet,
    ],
   str_18|agi_17|int_8|cha_9|level(29), wpex(100,100,120,50,20,60), knows_common|knows_ironflesh_7|knows_power_strike_3|knows_power_throw_1|knows_athletics_4|knows_riding_3|knows_shield_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Noble
  # Heavy cavalry ranged, swords, axes, maces, bows, shields
  ["sarranid_noble_horse_archer", "Sarranid Noble Horse Archer", "Sarranid Noble Horse Archers", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_6,
   [itm_sarranid_cavalry_sword, itm_iron_mace, itm_sarranid_axe_b, itm_strong_bow2, itm_bodkin_arrows, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_sarranid_boots_d, itm_mail_mittens, itm_scale_gauntlets,
    itm_sarranid_mail_shirt,
    itm_sarranid_veiled_helmet, itm_sarranid_mail_coif,
    itm_arabian_horse_b],
   str_18|agi_21|int_10|cha_18|level(44), wpex(110,105,105,140,25,70), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_1|knows_power_draw_5|knows_athletics_6|knows_riding_7|knows_shield_1|knows_horse_archery_6, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Heavy cavalry, swords, axes, maces, lances, shields
  # SPECIAL
  ["sarranid_noble_cavalry", "Sarranid Cataphract", "Sarranid Cataphracts", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_63,
   [itm_sarranid_cavalry_sword, itm_iron_mace, itm_sarranid_axe_b, itm_heavy_lance, itm_tab_shield_small_round_c,itm_tab_shield_small_round_c_plain_1,itm_tab_shield_small_round_c_plain_2,
    itm_sarranid_boots_d, itm_mail_mittens, itm_scale_gauntlets,
    itm_mamluke_mail_herald,
    itm_sarranid_veiled_helmet,
    itm_warhorse_sarranid],
   str_19|agi_20|int_10|cha_20|level(46), wpex(115,105,135,50,20,70), knows_common|knows_ironflesh_7|knows_power_strike_4|knows_power_throw_1|knows_power_draw_2|knows_athletics_5|knows_riding_6|knows_shield_1|knows_horse_archery_2, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Heavy cavalry skirmisher, swords, axes, maces, javelins, lances
  # SPECIAL
  ["sarranid_noble_skirmisher", "Sarranid Noble Skirmisher", "Sarranid Noble Skirmisher", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_small_kingdom_65,
   [itm_sarranid_cavalry_sword, itm_iron_mace, itm_sarranid_axe_b, itm_jarid, itm_jarid, itm_heavy_lance,
    itm_sarranid_boots_d, itm_mail_mittens, itm_scale_gauntlets,
    itm_mamluke_mail_herald, itm_sarranid_mail_shirt,
    itm_sarranid_veiled_helmet, itm_sarranid_mail_coif,
    itm_warhorse_sarranid],
   str_18|agi_21|int_10|cha_19|level(45), wpex(120,110,140,55,25,120), knows_common|knows_ironflesh_6|knows_power_strike_4|knows_power_throw_4|knows_power_draw_2|knows_athletics_6|knows_riding_6|knows_shield_1|knows_horse_archery_7, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Heavy infantry ranged, 2h swords, bows
  # SPECIAL
  ["sarranid_noble_infantry", "Sarranid Noble Infantry", "Sarranid Noble Infantry", tf_guarantee_trained_armor, no_scene, reserved, fac_small_kingdom_62,
   [itm_khergit_sword_two_handed_b, itm_nomad_bow2, itm_bodkin_arrows,
    itm_sarranid_boots_d, itm_mail_mittens, itm_scale_gauntlets,
    itm_mamluke_mail_herald,
    itm_sarranid_veiled_helmet,
    ],
   str_19|agi_19|int_10|cha_17|level(42), wpex(110,130,105,125,25,70), knows_common|knows_ironflesh_4|knows_power_strike_4|knows_power_throw_1|knows_power_draw_5|knows_athletics_6|knows_riding_5|knows_shield_1|knows_horse_archery_4, sarranid_face_young_1, sarranid_face_old_2 ],
  
  # Heavy infantry, polearm
  # SPECIAL
  ["sarranid_noble_guard", "Sarranid Noble Guard", "Sarranid Noble Guards", tf_guarantee_trained_armor, no_scene, reserved, fac_small_kingdom_62,
   [itm_military_scythe,
    itm_sarranid_boots_d, itm_mail_mittens, itm_scale_gauntlets,
    itm_mamluke_mail_herald,
    itm_sarranid_veiled_helmet,
    ],
   str_21|agi_18|int_10|cha_16|level(42), wpex(100,100,150,55,25,70), knows_common|knows_ironflesh_8|knows_power_strike_6|knows_power_throw_1|knows_athletics_5|knows_riding_5, sarranid_face_young_1, sarranid_face_old_2 ],
  
  ###############
  # Mercenaries #
  ###############
  # ["mercenary_", "Mercenary", "Mercenary", tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
  #  [



  #   ],
  #  str_|agi_|int_|cha_|level(), wpex(,,,,,), knows_common|knows_ironflesh_|knows_power_strike_|knows_power_throw_|knows_power_draw_|knows_athletics_|knows_shield_|knows_riding_|knows_horse_archery_, man_face_young_1, man_face_old_2],
  # Peasant
  # Basic infantry, swprds, maces, picks, shields
  ["mercenary_levy_infantry", "Mercenary Levy Infantry", "Mercenary Levy Infantries", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_a, itm_mace_2, itm_fighting_pick, itm_tab_shield_heater_a, itm_tab_shield_heater_a_plain_1, itm_tab_shield_heater_a_plain_2,
    itm_wrapping_boots, itm_ankle_boots, itm_nomad_boots,
    itm_tabard_herald, itm_linen_tunic_herald, itm_rich_shirt_herald, itm_coarse_tunic_herald,

    ],
   str_10|agi_8|int_5|cha_6|level(6), wpex(65,60,60,30,30,25), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_athletics_3, man_face_young_1, man_face_old_2],
  
  # Basic ranged, swords, maces, picks, bows,
  ["mercenary_levy_archer", "Mercenary Levy Archer", "Mercenary Levy Archers", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_a, itm_mace_2, itm_fighting_pick, itm_hunting_bow, itm_arrows_b,
    itm_wrapping_boots, itm_ankle_boots, itm_nomad_boots,
    itm_tabard_herald, itm_linen_tunic_herald, itm_rich_shirt_herald, itm_coarse_tunic_herald,

    ],
   str_8|agi_11|int_5|cha_6|level(7), wpex(50,45,45,65,30,25), knows_common|knows_power_strike_2|knows_power_draw_4|knows_athletics_2, man_face_young_1, man_face_old_2],
  
  # Basic ranged, swords, maces, picks, crossbows
  ["mercenary_levy_crossbowman", "Mercenary Levy Crossbowman", "Mercenary Levy Crossbowmen", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_a, itm_mace_2, itm_fighting_pick, itm_hunting_crossbow, itm_bolts,
    itm_wrapping_boots, itm_ankle_boots, itm_nomad_boots,
    itm_tabard_herald, itm_linen_tunic_herald, itm_rich_shirt_herald, itm_coarse_tunic_herald,

    ],
   str_9|agi_10|int_5|cha_6|level(7), wpex(50,45,45,30,60,25), knows_common|knows_power_strike_2|knows_athletics_2, man_face_young_1, man_face_old_2],
  
  # Basic infantry, spears, shields
  ["mercenary_levy_spearman", "Mercenary Levy Spearman", "Mercenary Levy Spearmen", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_commoners,
   [itm_spear, itm_tab_shield_heater_a, itm_tab_shield_heater_a_plain_1, itm_tab_shield_heater_a_plain_2,
    itm_wrapping_boots, itm_ankle_boots, itm_nomad_boots,
    itm_tabard_herald, itm_linen_tunic_herald, itm_rich_shirt_herald, itm_coarse_tunic_herald,

    ],
   str_11|agi_7|int_5|cha_6|level(6), wpex(60,55,75,30,30,25), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_athletics_3, man_face_young_1, man_face_old_2],
  
  # Basic infnatry ranged, swords, maces, picks, javelins, shields
  ["mercenary_levy_skirmisher", "Mercenary Levy Skirmisher", "Mercenary Levy Skirmishers", tf_guarantee_recruit_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_a, itm_mace_2, itm_fighting_pick, itm_darts, itm_tab_shield_heater_a, itm_tab_shield_heater_a_plain_1, itm_tab_shield_heater_a_plain_2,
    itm_wrapping_boots, itm_ankle_boots, itm_nomad_boots,
    itm_tabard_herald, itm_linen_tunic_herald, itm_rich_shirt_herald, itm_coarse_tunic_herald,

    ],
   str_9|agi_9|int_5|cha_6|level(6), wpex(60,55,55,30,30,70), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_throw_2|knows_athletics_3, man_face_young_1, man_face_old_2],
  
  # Common
  # Light infantry, swords, maces, picks, shields
  ["mercenary_light_infantry", "Mercenary Light Infantry", "Mercenary Light Infantries", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_a, itm_mace_3, itm_fighting_pick, itm_tab_shield_heater_b,itm_tab_shield_heater_b_plain_1,itm_tab_shield_heater_b_plain_2, itm_tab_shield_kite_b,itm_tab_shield_kite_b_plain_1,itm_tab_shield_kite_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_footman_helmet, itm_helmet_with_neckguard, itm_mail_coif
    ],
   str_13|agi_13|int_6|cha_7|level(16), wpex(100,75,75,35,40,40), knows_common|knows_ironflesh_1|knows_power_strike_4|knows_power_throw_1|knows_athletics_4|knows_riding_2, man_face_young_1, man_face_old_2 ],
  
  # Light infantry, swords, maces, picks, javelins, shields
  ["mercenary_light_skirmisher", "Mercenary Light Skirmisher", "Mercenary Light Skirmishers", tf_guarantee_common_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_a, itm_mace_3, itm_fighting_pick, itm_war_darts, itm_war_darts, itm_tab_shield_heater_b,itm_tab_shield_heater_b_plain_1,itm_tab_shield_heater_b_plain_2, itm_tab_shield_kite_b,itm_tab_shield_kite_b_plain_1,itm_tab_shield_kite_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_footman_helmet, itm_helmet_with_neckguard, itm_mail_coif
    ],
   str_12|agi_14|int_7|cha_7|level(17), wpex(85,60,60,35,40,100), knows_common|knows_ironflesh_1|knows_power_strike_4|knows_power_throw_1|knows_athletics_4|knows_riding_2, man_face_young_1, man_face_old_2 ],
  
  # Light infantry, swords, maces, picks, shields
  ["mercenary_light_spearman", "Mercenary Light Spearman", "Mercenary Light Spearmen", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_commoners,
   [itm_spear, itm_tab_shield_heater_b,itm_tab_shield_heater_b_plain_1,itm_tab_shield_heater_b_plain_2, itm_tab_shield_kite_b,itm_tab_shield_kite_b_plain_1,itm_tab_shield_kite_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_footman_helmet, itm_helmet_with_neckguard, itm_mail_coif
    ],
   str_14|agi_12|int_6|cha_7|level(16), wpex(75,75,100,40,40,35), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_1|knows_athletics_4|knows_riding_2, man_face_young_1, man_face_old_2 ],
  
  # Light ranged, swords, maces, picks, bows
  ["mercenary_light_archer", "Mercenary Light Archer", "Mercenary Light Archers", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_a, itm_dagger, itm_mace_2, itm_fighting_pick, itm_hunting_bow, itm_barbed_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald, itm_padded_leather_herald, itm_leather_armor_herald,
    itm_mail_coif, itm_footman_helmet, itm_helmet_with_neckguard,
    ],
   str_9|agi_16|int_6|cha_6|level(14), wpex(70,60,60,105,50,55), knows_common|knows_power_strike_2|knows_power_throw_1|knows_power_draw_4|knows_athletics_4|knows_riding_2, man_face_young_1, man_face_old_2 ],
  
  # Light ranged, swords, maces, picks, crossbows
  ["mercenary_light_crossbowman", "Mercenary Light Crossbowman", "Mercenary Light Crossbowmen", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_a, itm_dagger, itm_mace_2, itm_fighting_pick, itm_light_crossbow, itm_bolts,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald, itm_padded_leather_herald, itm_leather_armor_herald,
    itm_mail_coif, itm_footman_helmet, itm_helmet_with_neckguard,
    ],
   str_11|agi_15|int_6|cha_7|level(16), wpex(75,65,65,45,90,55), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_throw_1|knows_athletics_3|knows_riding_2, man_face_young_1, man_face_old_2 ],
  
  # Light cavalry, swords, picks, shields
  ["mercenary_light_cavalry", "Mercenary Light Cavalry", "Mercenary Light Cavalries", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_a, itm_sword_medieval_a_long, itm_fighting_pick, itm_mace_3, itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a_plain_1,itm_tab_shield_heater_cav_a_plain_2, itm_tab_shield_kite_cav_a,itm_tab_shield_kite_cav_a_plain_1,itm_tab_shield_kite_cav_a_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_footman_helmet, itm_helmet_with_neckguard, itm_mail_coif,
    itm_saddle_horse],
   str_10|agi_17|int_7|cha_7|level(18), wpex(105,80,90,40,45,55), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_throw_1|knows_athletics_3|knows_riding_6|knows_horse_archery_1, man_face_young_1, man_face_old_2 ],
  
  # Veteran
  # Medium infantry, swords, picks, maces, shields
  ["mercenary_infantry", "Mercenary Infantry", "Mercenary Infantries", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_military_sickle_a, itm_mace_4, itm_tab_shield_heater_c,itm_tab_shield_heater_c_plain_1,itm_tab_shield_heater_c_plain_2, itm_tab_shield_kite_c,itm_tab_shield_kite_c_plain_1,itm_tab_shield_kite_c_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_mail_hauberk_herald, itm_mail_shirt_herald, itm_heraldic_mail_with_tunic,
    itm_kettle_hat, itm_mail_coif, itm_helmet_with_neckguard
    ],
   str_15|agi_15|int_7|cha_8|level(22), wpex(105,80,80,40,45,45), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_1|knows_athletics_2|knows_riding_2|knows_shield_1, man_face_young_1, man_face_old_2 ],
  
  # Medium infantry, spears, shields
  ["mercenary_heavy_spearman", "Mercenary Heavy Spearman", "Mercenary Heavy Spearmen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_commoners,
   [itm_war_spear, itm_tab_shield_heater_c,itm_tab_shield_heater_c_plain_1,itm_tab_shield_heater_c_plain_2, itm_tab_shield_kite_c,itm_tab_shield_kite_c_plain_1,itm_tab_shield_kite_c_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_mail_hauberk_herald, itm_mail_shirt_herald, itm_heraldic_mail_with_tunic,
    itm_kettle_hat, itm_mail_coif, itm_helmet_with_neckguard
    ],
   str_16|agi_14|int_7|cha_8|level(22), wpex(80,80,105,45,45,40), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_power_throw_1|knows_athletics_2|knows_riding_2|knows_shield_1, man_face_young_1, man_face_old_2 ],
  
  # Medium cavalry, swords, picks, maces, lances, shields
  ["mercenary_cavalry", "Mercenary Cavalry", "Mercenary Cavalries", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_b, itm_mace_4, itm_military_sickle_a, itm_light_lance, itm_tab_shield_heater_cav_a,itm_tab_shield_heater_cav_a_plain_1,itm_tab_shield_heater_cav_a_plain_2, itm_tab_shield_kite_cav_a,itm_tab_shield_kite_cav_a_plain_1,itm_tab_shield_kite_cav_a_plain_2,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_mail_shirt_herald, itm_mail_hauberk_herald,
    itm_kettle_hat, itm_mail_coif, itm_helmet_with_neckguard,
    itm_pack_horse, itm_hunter],
   str_13|agi_16|int_8|cha_8|level(22), wpex(95,75,110,40,45,55), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_throw_1|knows_athletics_1|knows_riding_5|knows_horse_archery_1, man_face_young_1, man_face_old_2 ],
  
  # Light ranged, swords, picks, maces, bows
  ["mercenary_archer", "Mercenary Archer", "Mercenary Archers", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_military_sickle_a, itm_mace_4, itm_short_bow, itm_bodkin_arrows, itm_tab_shield_heater_b,itm_tab_shield_heater_b_plain_1,itm_tab_shield_heater_b_plain_2, itm_tab_shield_kite_b,itm_tab_shield_kite_b_plain_1,itm_tab_shield_kite_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_heraldic_mail_with_tunic_b,
    itm_mail_coif, itm_footman_helmet, itm_helmet_with_neckguard,
    ],
   str_12|agi_18|int_8|cha_7|level(22), wpex(75,65,65,100,50,55), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_throw_1|knows_power_draw_4|knows_athletics_3|knows_riding_2, man_face_young_1, man_face_old_2 ],
  
  # Light ranged, swords, picks, maces, crossbows, shields
  ["mercenary_crossbowman", "Mercenary Crossbowman", "Mercenary Crossbowmen", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_military_sickle_a, itm_mace_4, itm_crossbow, itm_steel_bolts, itm_tab_shield_heater_b,itm_tab_shield_heater_b_plain_1,itm_tab_shield_heater_b_plain_2, itm_tab_shield_kite_b,itm_tab_shield_kite_b_plain_1,itm_tab_shield_kite_b_plain_2,
    itm_leather_boots, itm_leather_gloves,
    itm_heraldic_mail_with_tunic_b,
    itm_kettle_hat, itm_mail_coif, itm_helmet_with_neckguard,
    ],
   str_14|agi_16|int_8|cha_8|level(23), wpex(80,70,70,50,80,55), knows_common|knows_ironflesh_3|knows_power_strike_2|knows_power_throw_1|knows_athletics_2|knows_riding_2, man_face_young_1, man_face_old_2 ],
  
  # Elite
  # Heavy infantry, swords, maces, picks, shields
  ["mercenary_heavy_infantry", "Mercenary Heavy Infantry", "Mercenary Heavy Infantries", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_d, itm_mace_4, itm_military_sickle_a, itm_tab_shield_heater_c,itm_tab_shield_heater_c_plain_1,itm_tab_shield_heater_c_plain_2, itm_tab_shield_kite_c,itm_tab_shield_kite_c_plain_1,itm_tab_shield_kite_c_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_surcoat_plain, itm_heraldic_mail_with_tabard, itm_heraldic_mail_with_tabard_plain, itm_brigandine_red_herald, itm_banded_armor,
    itm_guard_helmet, itm_bascinet
    ],
   str_20|agi_14|int_8|cha_9|level(27), wpex(110,85,85,40,45,50), knows_common|knows_ironflesh_6|knows_power_strike_2|knows_power_throw_1|knows_shield_1|knows_athletics_1|knows_riding_2, man_face_young_1, man_face_old_2 ],

  # Heavy cavalry, swords, maces, picks, lances, shields
  ["mercenary_heavy_cavalry", "Mercenary Heavy Cavalry", "Mercenary Heavy Cavalries", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_d, itm_sword_medieval_d_long, itm_mace_4, itm_military_sickle_a, itm_lance, itm_tab_shield_heater_cav_b,itm_tab_shield_heater_cav_b_plain_1,itm_tab_shield_heater_cav_b_plain_2, itm_tab_shield_kite_cav_b,itm_tab_shield_kite_cav_b_plain_1,itm_tab_shield_kite_cav_b_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_surcoat_plain, itm_brigandine_red_herald, itm_banded_armor,
    itm_guard_helmet, itm_bascinet,
    itm_hunter],
   str_19|agi_14|int_8|cha_9|level(27), wpex(85,80,80,40,45,50), knows_common|knows_ironflesh_5|knows_power_strike_2|knows_power_throw_1|knows_athletics_1|knows_riding_5, man_face_young_1, man_face_old_2 ],

  # Heavy infantry, polearms
  ["mercenary_guard", "Mercenary Guard", "Mercenary Guards", tf_guarantee_trained_armor, no_scene, reserved, fac_commoners,
   [itm_glaive,
    itm_mail_boots, itm_mail_mittens,
    itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_surcoat_plain, itm_heraldic_mail_with_tabard, itm_heraldic_mail_with_tabard_plain,
    itm_guard_helmet, itm_bascinet, itm_bascinet_b, itm_bascinet_c,
    ],
   str_15|agi_15|int_8|cha_9|level(24), wpex(90,80,115,40,45,50), knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_2, man_face_young_1, man_face_old_2 ],
  
  # Heavy ranged, swords, picks, maces, bows
  ["mercenary_heavy_archer", "Mercenary Heavy Archer", "Mercenary Heavy Archers", tf_guarantee_trained_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_mace_4, itm_military_sickle_a, itm_long_bow2, itm_bodkin_arrows, itm_tab_shield_heater_c,itm_tab_shield_heater_c_plain_1,itm_tab_shield_heater_c_plain_2, itm_tab_shield_kite_b,itm_tab_shield_kite_b_plain_1,itm_tab_shield_kite_b_plain_2,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_mail_shirt_herald, itm_mail_hauberk_herald,
    itm_kettle_hat, itm_mail_coif, itm_helmet_with_neckguard,
    ],
   str_16|agi_19|int_9|cha_8|level(29), wpex(80,70,70,70,50,60), knows_common|knows_ironflesh_4|knows_power_strike_2|knows_power_throw_1|knows_power_draw_6|knows_athletics_2|knows_riding_2, man_face_young_1, man_face_old_2 ],
  
  # Heavy ranged, swords, picks, maces, crossbows, shields
  ["mercenary_heavy_crossbowman", "Mercenary Heavy Crossbowman", "Mercenary Heavy Crossbowmen", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_mace_4, itm_military_sickle_a, itm_heavy_crossbow, itm_steel_bolts, itm_tab_shield_heater_c,itm_tab_shield_heater_c_plain_1,itm_tab_shield_heater_c_plain_2, itm_tab_shield_kite_b,itm_tab_shield_kite_b_plain_1,itm_tab_shield_kite_b_plain_2,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_mail_shirt_herald, itm_mail_hauberk_herald,
    itm_kettle_hat, itm_mail_coif, itm_helmet_with_neckguard,
    ],
   str_18|agi_17|int_9|cha_9|level(30), wpex(85,75,75,50,70,60), knows_common|knows_ironflesh_5|knows_power_strike_2|knows_power_throw_1|knows_athletics_1|knows_riding_2, man_face_young_1, man_face_old_2 ],
  
  # Medium infantry, swords, picks, maces, javelins, shields
  ["mercenary_heavy_skirmisher", "Mercenary Heavy Skirmisher", "Mercenary Heavy Skirmishers", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_d, itm_mace_4, itm_military_sickle_a, itm_javelin, itm_javelin, itm_tab_shield_heater_c,itm_tab_shield_heater_c_plain_1,itm_tab_shield_heater_c_plain_2, itm_tab_shield_kite_c,itm_tab_shield_kite_c_plain_1,itm_tab_shield_kite_c_plain_2,
    itm_mail_chausses, itm_mail_mittens,
    itm_mail_hauberk_herald, itm_mail_shirt_herald, itm_heraldic_mail_with_tunic,
    itm_kettle_hat, itm_mail_coif, itm_helmet_with_neckguard
    ],
   str_15|agi_17|int_8|cha_9|level(26), wpex(90,65,65,40,45,85), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_3|knows_athletics_3|knows_riding_2|knows_shield_1, man_face_young_1, man_face_old_2 ],
  
  # Noble
  # Heavy cavalry, swords, picks, maces, morningstars, lances, shields
  ["mercenary_knight", "Mercenary Knight", "Mercenary Knights", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_commoners,
   [itm_morningstar, itm_bastard_sword_b, itm_sword_medieval_d, itm_sword_medieval_d_long, itm_military_sickle_a, itm_mace_4, itm_heavy_lance, itm_tab_shield_heater_cav_b, itm_tab_shield_heater_cav_b_plain_1, itm_tab_shield_heater_cav_b_plain_2,
    itm_mail_boots, itm_iron_greaves, itm_gauntlets, itm_mail_mittens,
    itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_surcoat_plain, itm_heraldic_mail_with_tabard, itm_heraldic_mail_with_tabard_plain, itm_banded_armor,
    itm_guard_helmet, itm_bascinet, itm_bascinet_2, itm_bascinet_3, itm_bascinet_b, itm_bascinet_c, itm_full_helm_herald, itm_great_helmet_herald,
    itm_warhorse],
   str_20|agi_20|int_11|cha_19|level(47), wpex(115,110,135,60,60,65), knows_common|knows_ironflesh_9|knows_power_strike_4|knows_athletics_2|knows_shield_1|knows_riding_6, man_face_young_1, man_face_old_2],

  # Heavy cavalry ranged, swords, picks, maces, crossbows, shields
  ["mercenary_armoured_mounted_crossbowman", "Mercenary Armoured Mounted Crossbowman", "Mercenary Armoured Mounted Crossbowmen", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_d, itm_sword_medieval_d_long, itm_military_sickle_a, itm_mace_4, itm_light_crossbow, itm_steel_bolts, itm_tab_shield_heater_cav_b, itm_tab_shield_heater_cav_b_plain_1, itm_tab_shield_heater_cav_b_plain_2,
    itm_mail_boots, itm_mail_mittens,
    itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_surcoat_plain,
    itm_guard_helmet, itm_bascinet, itm_bascinet_2, itm_bascinet_3, itm_bascinet_b, itm_bascinet_c,
    itm_warhorse],
   str_18|agi_21|int_12|cha_18|level(46), wpex(95,90,90,60,120,65), knows_common|knows_ironflesh_6|knows_power_strike_2|knows_athletics_2|knows_riding_6|knows_horse_archery_5, man_face_young_1, man_face_old_2],
  
  # Heavy infantry, polearms
  # ["mercenary_paladin", "Mercenary Paladin", "Mercenary Paladin", tf_guarantee_trained_armor, no_scene, reserved, fac_commoners,
  #  [itm_bec_de_corbin_a,
  #   itm_iron_greaves, itm_gauntlets,
  #   itm_heraldic_mail_with_tabard, itm_heraldic_mail_with_tabard_plain, itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_surcoat_plain, itm_banded_armor,
  #   itm_bascinet_2, itm_bascinet_3, itm_full_helm_herald, itm_great_helmet_herald,
  #   ],
  # str_|agi_|int_|cha_|level(), wpex(,,,,,), knows_common|knows_ironflesh_|knows_power_strike_|knows_power_throw_|knows_power_draw_|knows_athletics_|knows_shield_|knows_riding_|knows_horse_archery_, man_face_young_1, man_face_old_2]

  ###################################
  # Special faction mercenary units # # do not follow normal recruitement process
  ###################################
  # Light cavalry, sowrds, picks, maces, shields
  # Requires stables, unit send as courrier
  ["swadian_rider", "Swadian Rider", "Swadian Riders", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_sword_medieval_b, itm_fighting_pick, itm_mace_3, itm_tab_shield_heater_cav_a,
    itm_leather_boots, itm_leather_gloves,
    itm_gambeson_herald, itm_leather_armor_herald, itm_padded_leather_herald,
    itm_padded_coif, itm_mail_coif, itm_footman_helmet,
    itm_courser],
   str_13|agi_16|int_9|cha_8|level(23), wpex(105,85,110,60,50,50), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_athletics_4|knows_riding_6, man_face_young_1, man_face_old_2 ],
  
  # Heavy cavalry, swords, morningstars, maces, shields
  # Requires order
  ["swadian_paladin", "Swadian Paladin", "Swadian Paladins", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_morningstar, itm_bastard_sword_b, itm_mace_4, itm_sword_medieval_c, itm_sword_medieval_c_long, itm_tab_shield_heater_cav_b,
    itm_gauntlets, itm_iron_greaves,
    itm_great_helmet_herald, itm_winged_great_helmet, itm_great_helmet_herald,
    itm_coat_of_plates_herald, itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_tabard, itm_plate_armor_herald,
    itm_charger, itm_charger_b],
   str_22|agi_16|int_11|cha_14|level(40), wpex(115,105,110,55,45,60), knows_common|knows_ironflesh_7|knows_power_strike_3|knows_athletics_2|knows_riding_6|knows_shield_1, man_face_young_1, man_face_old_2 ],
  
  # Heavy ranged, swords, picks, maces, bows, crossbows, shields
  # Requires order
  ["swadian_marksman", "Swadian Marksman", "Swadian Marksmen", tf_guarantee_ranged|tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_sword_medieval_c, itm_sword_medieval_c_small, itm_military_sickle_a, itm_mace_4, itm_tab_shield_heater_c, itm_short_bow2, itm_bodkin_arrows, itm_light_crossbow, itm_steel_bolts,
    itm_mail_mittens, itm_mail_chausses,
    itm_kettle_hat, itm_mail_coif,
    itm_heraldic_mail_with_surcoat, itm_mail_with_surcoat_herald,
    ],
  str_15|agi_17|int_10|cha_11|level(30), wpex(100,85,90,130,120,55), knows_common|knows_ironflesh_4|knows_power_strike_2|knows_power_draw_4|knows_athletics_3|knows_riding_2, man_face_young_1, man_face_old_2],

  # Heavy infantry, 2h swords, morningstars, swords, shields
  # Requires order
  ["swadian_kings_guard", "Swadian King's Guard", "Swadian King's Guards", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_1,
   [itm_sword_two_handed_b, itm_morningstar, itm_bastard_sword_b, itm_tab_shield_heater_d,
    itm_gauntlets, itm_mail_mittens, itm_iron_greaves,
    itm_guard_helmet, itm_great_helmet_herald,
    itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_tabard, itm_coat_of_plates_herald,
    ],
  str_20|agi_17|int_10|cha_11|level(38), wpex(120,120,115,65,55,60), knows_common|knows_ironflesh_6|knows_power_strike_4|knows_athletics_4|knows_shield_1, man_face_young_1, man_face_old_2],

  # Light cavalry ranged, swords, axes, bows, shields
  # Requires stables?
  ["vaegir_camp_follower", "Vaegir Camp Follower", "Vaegir Camp Followers", tf_female|tf_guarantee_recruit_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_2,
   [itm_scimitar, itm_one_handed_battle_axe_a, itm_nomad_bow, itm_bodkin_arrows, itm_tab_shield_kite_cav_a,
    itm_leather_gloves, itm_leather_boots, itm_nomad_boots,
    itm_vaegir_fur_helmet, itm_vaegir_fur_cap,
    itm_leather_jerkin_herald, itm_tribal_warrior_outfit,
    itm_steppe_horse],
   str_10|agi_15|int_7|cha_9|level(18), wpex(95,90,85,130,40,65), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_draw_5|knows_athletics_4|knows_riding_6|knows_horse_archery_5, woman_face_1, woman_face_2 ],
  
  # Heavy infantry, swords, 2h axes, javelins, shields
  # Requires order
  ["vaegir_vanguard", "Vaegir Vanguard", "Vaegir Vanguards", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2,
   [itm_scimitar_b, itm_bardiche, itm_tab_shield_kite_c, itm_throwing_spears,
    itm_mail_mittens, itm_mail_boots,
    itm_lamellar_armor_herald, itm_banded_armor, itm_brigandine_red_herald,
    itm_vaegir_war_helmet, itm_vaegir_noble_helmet, itm_vaegir_helmet,
    ],
  str_18|agi_20|int_11|cha_13|level(39), wpex(105,110,100,70,40,85), knows_common|knows_ironflesh_6|knows_power_strike_5|knows_power_throw_4|knows_athletics_5|knows_riding_2, man_face_young_1, man_face_old_2 ],
  
  # Heavy ranged, swords, bows, shields
  # Requires order
  ["vaegir_marksman", "Vaegir Marksman", "Vaegir Marksman", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_kingdom_2,
   [itm_scimitar_b, itm_strong_bow, itm_bodkin_arrows, itm_tab_shield_kite_d,
    itm_mail_mittens, itm_mail_boots,
    itm_lamellar_armor_herald, itm_banded_armor,
    itm_vaegir_helmet, itm_vaegir_noble_helmet,
    ],
   str_16|agi_18|int_11|cha_14|level(36), wpex(90,80,75,145,55,70), knows_common|knows_ironflesh_3|knows_power_strike_2|knows_power_draw_5|knows_athletics_3|knows_riding_2|knows_horse_archery_1, man_face_young_1, man_face_old_2 ],
  
  # Heavy Cavalry, swords, 2h axes, shields
  # Requires order
  ["vaegir_armoured_cavalry", "Vaegir Armoured Cavalry", "Vaegir Armoured Cavalry", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_kingdom_2,
   [itm_scimitar_b, itm_bardiche, itm_tab_shield_kite_cav_b,
    itm_mail_mittens, itm_gauntlets, itm_iron_greaves,
    itm_lamellar_armor_herald, itm_banded_armor, itm_heraldic_mail_with_surcoat,
    itm_vaegir_mask, itm_vaegir_helmet, itm_vaegir_noble_helmet,
    itm_warhorse],
   str_18|agi_18|int_11|cha_12|level(36), wpex(110,110,95,60,40,55), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_athletics_2|knows_riding_6|knows_shield_1, man_face_young_1, man_face_old_2 ],
  
  # Heavy cavalry ranged, swords, bows, shields
  # Requires order
  ["vaegir_armoured_horse_archer", "Vaegir Armoured Mounted Bowman", "Vaegir Armoured Mounted Bowmen", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_2,
   [itm_scimitar_b, itm_strong_bow, itm_bodkin_arrows, itm_tab_shield_kite_cav_b,
    itm_mail_mittens, itm_gauntlets, itm_iron_greaves,
    itm_lamellar_armor_herald, itm_banded_armor, itm_heraldic_mail_with_surcoat,
    itm_vaegir_mask, itm_vaegir_helmet, itm_vaegir_noble_helmet,
    itm_warhorse],
   str_15|agi_18|int_12|cha_15|level(37), wpex(85,80,70,110,45,50), knows_common|knows_ironflesh_3|knows_power_strike_2|knows_power_draw_5|knows_athletics_2|knows_riding_6|knows_horse_archery_6, man_face_young_1, man_face_old_2 ],
  
  # Heavy cavalry ranged, swords, maces, bows, shields
  # Requires order
  ["khergit_armoured_horse_archer", "Khergit Armoured Horse Archer", "Khergit Armoured Horse Archer", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3,
   [itm_sword_khergit_3, itm_winged_mace, itm_tab_shield_small_round_c, itm_khergit_bow, itm_khergit_arrows,
    itm_splinted_greaves, itm_leather_gloves,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    itm_lamellar_armor_herald,
    itm_warhorse_steppe],
   str_17|agi_19|int_11|cha_14|level(38), wpex(105,90,105,135,45,65), knows_common|knows_ironflesh_4|knows_power_strike_2|knows_power_draw_5|knows_athletics_2|knows_riding_6|knows_horse_archery_6, man_face_young_1, man_face_old_2 ],
  
  # Heavy cavalry ranged, lances, bows, javleins, shields
  # Requires order
  ["khergit_armoured_skirmisher", "Khergit Armoured Skirmisher", "Khergit Armoured Skirmishers", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3,
   [itm_heavy_lance, itm_tab_shield_small_round_c, itm_khergit_bow, itm_khergit_arrows, itm_javelin,
    itm_splinted_greaves, itm_leather_gloves,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    itm_lamellar_armor_herald,
    itm_warhorse_steppe],
   str_18|agi_19|int_11|cha_14|level(39), wpex(110,95,130,125,45,105), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_3|knows_power_draw_5|knows_athletics_3|knows_riding_6|knows_horse_archery_6, man_face_young_1, man_face_old_2 ],
  
  # Heavy infantry, swords, maces, shields
  # Requires order
  ["khergit_armoured_infantry", "Khergit Armoured Infantry", "Khergit Armoured Infantry", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_3,
   [itm_sword_khergit_4, itm_spiked_mace, itm_tab_shield_small_round_c,
    itm_splinted_greaves, itm_scale_gauntlets,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    itm_lamellar_armor_herald,
    ],
   str_17|agi_18|int_11|cha_13|level(36), wpex(115,100,120,65,45,60), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_power_draw_1|knows_athletics_5|knows_riding_2|knows_shield_1, man_face_young_1, man_face_old_2 ],
  
  # Light infantry, swords, javelins, shields
  # Requires barracks
  ["nord_camp_follower", "Nord Camp Follower", "Nord Camp Followers", tf_female|tf_guarantee_recruit_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_kingdom_4,
   [itm_sword_viking_2, itm_sword_viking_2_small, itm_javelin, itm_tab_shield_round_c,
    itm_leather_boots, itm_leather_gloves,
    itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_nordic_veteran_archer_helmet,
    itm_coarse_tunic_herald, itm_tunic_herald,
    ],
   str_12|agi_11|int_7|cha_9|level(16), wpex(110,100,95,55,40,95), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_3|knows_athletics_6, woman_face_1, woman_face_2 ],
  
  # Medium infantry, swords, axes, shields
  # Requires barracks_2
  ["nord_shield_maiden", "Nord Shield Maid", "Nord Shield Maiden", tf_female|tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4,
   [itm_sword_viking_2, itm_sword_viking_2_small, itm_one_handed_battle_axe_a, itm_one_handed_battle_axe_a, itm_tab_shield_round_d,
    itm_mail_chausses, itm_mail_mittens, itm_leather_gloves,
    itm_byrnie_herald, itm_mail_shirt_herald, itm_mail_hauberk_herald,
    itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    ],
   str_17|agi_14|int_10|cha_12|level(30), wpex(120,110,105,55,40,65), knows_common|knows_ironflesh_6|knows_power_strike_4|knows_athletics_5|knows_shield_1, woman_face_1, woman_face_2 ],
  
  # Heavy archer, swords, axes, bows, shields
  # Requires order
  ["nord_companion_archer", "Nord Companion Archer", "Nord Companion Archers", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4,
   [itm_sword_viking_3, itm_sword_viking_3_small, itm_one_handed_battle_axe_c, itm_long_bow, itm_bodkin_arrows, itm_tab_shield_round_d,
    itm_mail_chausses, itm_mail_mittens,
    itm_mail_hauberk_herald, itm_byrnie_herald, itm_mail_shirt_herald,
    itm_nordic_fighter_helmet, itm_nordic_helmet,
    ],
    str_16|agi_17|int_10|cha_11|level(31), wpex(100,95,90,95,45,60), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_draw_6|knows_athletics_3, man_face_young_1, man_face_old_2 ],

  # Heavy cavalry, swords, axes, 2h axes, shields
  ["nord_companion_cavalry", "Nord Companion Cavalry", "Nord Companion Cavalries", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4,
   [itm_sword_viking_3_long, itm_sword_viking_3, itm_one_handed_battle_axe_c, itm_one_handed_battle_axe_b, itm_great_axe, itm_tab_shield_round_d,
    itm_mail_boots, itm_mail_mittens,
    itm_banded_armor,
    itm_nordic_helmet, itm_nordic_huscarl_helmet,
    itm_hunter],
    str_17|agi_18|int_10|cha_11|level(33), wpex(110,105,100,70,30,60), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_athletics_2|knows_riding_5, man_face_young_1, man_face_old_2 ],

  # Heavy infantry, spears, shields
  ["nord_companion_spearman", "Nord Companion Spearman", "Nord Companion Spearmen", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4,
   [itm_war_spear, itm_tab_shield_round_e,
    itm_iron_greaves, itm_gauntlets,
    itm_cuir_bouilli_herald, itm_banded_armor,
    itm_nordic_huscarl_helmet, itm_nordic_warlord_helmet,
    ],
    str_20|agi_18|int_11|cha_12|level(38), wpex(95,95,130,70,30,70), knows_common|knows_ironflesh_6|knows_power_strike_4|knows_athletics_4|knows_shield_1, man_face_young_1, man_face_old_2 ],

  # Heavy infantry, swords, axes, throwing axes, shields
  ["nord_companion_infantry", "Nord Companion Infantry", "Nord Companion Infantries", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_kingdom_4,
   [itm_sword_viking_3_long, itm_sword_viking_3, itm_sword_viking_3_small, itm_one_handed_battle_axe_c, itm_one_handed_battle_axe_b, itm_tab_shield_round_e, itm_heavy_throwing_axes,
    itm_iron_greaves, itm_mail_boots, itm_mail_mittens,
    itm_banded_armor,
    itm_nordic_huscarl_helmet, itm_nordic_helmet,
    ],
    str_19|agi_19|int_11|cha_14|level(40), wpex(120,115,110,70,30,90), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_4|knows_athletics_5|knows_shield_1, man_face_young_1, man_face_old_2 ],

  # Light infantry, swords, picks, shields
  # Requires militia_camp
  # ["rhodok_freemen", "Rhodok Freeman", "Rhodok Freemen", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_commoners,
  #  [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_fighting_pick, itm_soldiers_cleaver, itm_tab_shield_pavise_b,
  #   itm_leather_boots, itm_leather_gloves,
  #   itm_hood, ###
  #   itm_coarse_tunic_herald, itm_tunic_with_green_cape_herald,
  #   ],
  #  str_|agi_|int_|cha_|level(), wpex(,,,,,), knows_common|knows_ironflesh_|knows_power_strike_|knows_power_throw_|knows_power_draw_|knows_athletics_|knows_riding_|knows_shield_|knows_horse_archery_, man_face_young_1, man_face_old_2 ],
  
  # Heavy infantry, polearms
  # Requires order, faction policy (limited voting)
  # ["rhodok_blue_blood", "Blue Blood", "Blue Bloods", tf_guarantee_trained_armor, no_scene, reserved, fac_commoners,
  #  [itm_glaive,
  #   itm_iron_greaves, itm_gauntlets,
  #   itm_full_helm_herald, itm_bascinet_2, itm_bascinet_3,
  #   itm_coat_of_plates_herald, itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_tabard,
  #   ],
  #  str_|agi_|int_|cha_|level(), wpex(,,,,,), knows_common|knows_ironflesh_|knows_power_strike_|knows_power_throw_|knows_power_draw_|knows_athletics_|knows_riding_|knows_shield_|knows_horse_archery_, man_face_young_1, man_face_old_2 ],
  
  # ["sarranid_armoured_lancer", "Sarranid Armoured Lancer", "Sarranid Armoured Lancer", tf_guarantee_trained_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_commoners,
  #  [
  #   ],
  #  str_|agi_|int_|cha_|level(), wpex(,,,,,), knows_common|knows_ironflesh_|knows_power_strike_|knows_power_throw_|knows_power_draw_|knows_athletics_|knows_riding_|knows_shield_|knows_horse_archery_, man_face_young_1, man_face_old_2 ],
  
  # ["", "", "", tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
  #  [
  #   ],
  #  str_|agi_|int_|cha_|level(), wpex(,,,,,), knows_common|knows_ironflesh_|knows_power_strike_|knows_power_throw_|knows_power_draw_|knows_athletics_|knows_riding_|knows_shield_|knows_horse_archery_, man_face_young_1, man_face_old_2 ],
  
  #######################
  # Special mercenaries #
  #######################
  # # Light cavalry ranged, sabres, swords, bows
  # ["mercenary_horse_archer", "Mercenary Horse Archer", "Mercenary Horse Archers", tf_female|tf_guarantee_recruit_armor|tf_guarantee_horseman|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
  #  [itm_arabian_sword_a, itm_sword_khergit_1, itm_war_bow, itm_bodkin_arrows,
  #   itm_leather_boots, itm_leather_gloves,
  #   itm_leather_vest_herald, itm_coarse_tunic_herald,
  #   itm_vaegir_fur_cap, itm_vaegir_fur_helmet, itm_leather_steppe_cap_b,
  #   itm_steppe_horse, itm_arabian_horse_a],
  #  str_9|agi_17|int_6|cha_9|level(18), wpex(65,60,60,85,50,60), knows_common|knows_power_strike_2|knows_power_throw_1|knows_power_draw_6|knows_athletics_4|knows_riding_6|knows_horse_archery_4, man_face_young_1, man_face_old_2 ],
  
  # ["mercenary_sword_sister", "", "", tf_female|tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
   # [],
  # ]
  
  # ["mercenary_camp_follower", "", "", tf_female|tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
   # [],
  # ]
  
  # ["mercenary_archer", "", "", tf_female|tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
   # [],
  # ]
  
  # ["mercenary_light_rider", "", "", tf_female|tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
   # [],
  # ]
  
  # ["mercenary_heavy_rider", "", "", tf_female|tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
   # [],
  # ]
  
  # ["mercenary_", "", "", tf_female|tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
   # [],
  # ]

  #################
  # Special units #
  #################
  ["swadian_caravan_master", "Caravan Master", "Caravan Masters", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_1,
   [itm_sword_medieval_b, itm_bastard_sword_a,
    itm_leather_boots, itm_wrapping_boots, itm_leather_gloves,
    itm_leather_armor_herald, itm_leather_jerkin, itm_fur_coat,
    itm_hunter],
  str_10|agi_14|int_7|cha_6|level(14), wpex(60,55,60,55,45,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_5, swadian_face_young_1, swadian_face_old_2],
  ["swadian_caravan_guard", "Caravan Guard", "Caravan Guards", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_1,
   [],
  str_10|agi_14|int_7|cha_6|level(14), wpex(60,55,60,55,45,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_5, swadian_face_young_1, swadian_face_old_2],

  ["vaegir_caravan_master", "Caravan Master", "Caravan Masters", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_1,
   [itm_scimitar,
    itm_leather_boots, itm_nomad_boots, itm_leather_gloves,
    itm_leather_vest, itm_leather_jerkin, itm_fur_coat,
    itm_hunter],
  str_10|agi_14|int_7|cha_6|level(14), wpex(60,55,60,55,45,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_5, vaegir_face_young_1, vaegir_face_old_2],
  ["vaegir_caravan_guard", "Caravan Guard", "Caravan Guards", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_1,
   [],
  str_10|agi_14|int_7|cha_6|level(14), wpex(60,55,60,55,45,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_5, vaegir_face_young_1, vaegir_face_old_2],

  ["khergit_caravan_master", "Caravan Master", "Caravan Masters", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_1,
   [itm_sword_khergit_2,
    itm_leather_boots, itm_nomad_boots, itm_leather_gloves,
    itm_leather_vest, itm_tribal_warrior_outfit, itm_fur_coat,
    itm_hunter],
  str_10|agi_14|int_7|cha_6|level(14), wpex(60,55,60,55,45,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_5, khergit_face_young_1, khergit_face_old_2],
  ["khergit_caravan_guard", "Caravan Guard", "Caravan Guards", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_1,
   [],
  str_10|agi_14|int_7|cha_6|level(14), wpex(60,55,60,55,45,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_5, khergit_face_young_1, khergit_face_old_2],

  ["nord_caravan_master", "Caravan Master", "Caravan Masters", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_1,
   [itm_sword_viking_2,
    itm_leather_boots, itm_nomad_boots, itm_leather_gloves,
    itm_leather_jerkin, itm_fur_coat,
    itm_hunter],
  str_10|agi_14|int_7|cha_6|level(14), wpex(60,55,60,55,45,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_5, nord_face_young_1, nord_face_old_2],
  ["nord_caravan_guard", "Caravan Guard", "Caravan Guards", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_1,
   [],
  str_10|agi_14|int_7|cha_6|level(14), wpex(60,55,60,55,45,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_5, nord_face_young_1, nord_face_old_2],

  ["rhodok_caravan_master", "Caravan Master", "Caravan Masters", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_1,
   [itm_sword_medieval_b,
    itm_leather_boots, itm_wrapping_boots, itm_leather_gloves,
    itm_ragged_outfit, itm_leather_jerkin, itm_fur_coat,
    itm_hunter],
  str_10|agi_14|int_7|cha_6|level(14), wpex(60,55,60,55,45,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_5, rhodok_face_young_1, rhodok_face_old_2],
  ["rhodok_caravan_guard", "Caravan Guard", "Caravan Guards", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_1,
   [],
  str_10|agi_14|int_7|cha_6|level(14), wpex(60,55,60,55,45,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_5, rhodok_face_young_1, rhodok_face_old_2],

  ["sarranid_caravan_master", "Caravan Master", "Caravan Masters", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_1,
   [itm_arabian_sword_b,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_archers_vest, itm_fur_coat,
    itm_arabian_horse_b],
  str_10|agi_14|int_7|cha_6|level(14), wpex(60,55,60,55,45,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_5, sarranid_face_young_1, sarranid_face_old_2],
  ["sarranid_caravan_guard", "Caravan Guard", "Caravan Guards", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_1,
   [],
  str_10|agi_14|int_7|cha_6|level(14), wpex(60,55,60,55,45,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_5, sarranid_face_young_1, sarranid_face_old_2],

  ###########
  # Bandits #
  ###########
  # Forest bandit
  ["bandit_forest_bandit", "Forest Bandit", "Forest Bandits", tf_guarantee_recruit_armor, no_scene, reserved, fac_faction_1,
   [itm_axe, itm_mace_1, itm_long_spiked_club, itm_hatchet, itm_hunting_bow, itm_hunting_crossbow, itm_arrows_b, itm_bolts, itm_wooden_shield, itm_leather_covered_round_shield,
    itm_leather_boots, itm_nomad_boots, itm_hide_boots, itm_wrapping_boots,
    itm_leather_jerkin, itm_leather_armor, itm_ragged_outfit,
    itm_head_wrappings, itm_common_hood, itm_hood_b, itm_hood_c, itm_hood_d, itm_black_hood,
    ],
   str_10|agi_14|int_7|cha_6|level(14), wpex(60,55,60,55,45,40), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_draw_4|knows_athletics_4|knows_riding_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_forest_ranger", "Forest Ranger", "Forest Rangers", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_faction_1,
   [itm_mace_1, itm_hatchet, itm_short_bow, itm_light_crossbow, itm_arrows_b, itm_bolts, itm_wooden_shield, itm_leather_covered_round_shield,
    itm_nomad_boots, itm_hide_boots, itm_wrapping_boots,
    itm_leather_armor, itm_leather_jerkin, itm_ragged_outfit,
    itm_head_wrappings, itm_common_hood, itm_hood_b, itm_hood_c, itm_hood_d, itm_black_hood,
    ],
   str_9|agi_15|int_8|cha_5|level(14), wpex(50,45,50,80,70,45), knows_common|knows_power_strike_2|knows_power_draw_4|knows_athletics_4|knows_riding_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_forest_warrior", "Forest Warrior", "Forest Warriors", tf_guarantee_common_armor, no_scene, reserved, fac_faction_1,
   [itm_axe, itm_shortened_spear, itm_fighting_axe, itm_one_handed_war_axe_a, itm_long_spiked_club, itm_mace_2, itm_wooden_shield, itm_leather_covered_round_shield,
    itm_nomad_boots, itm_leather_boots, itm_leather_gloves,
    itm_ragged_outfit, itm_leather_jerkin, itm_padded_leather,
    itm_common_hood, itm_hood_b, itm_hood_c, itm_hood_d, itm_black_hood,
    ],
   str_14|agi_15|int_7|cha_7|level(20), wpex(75,70,75,50,40,45), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_draw_2|knows_athletics_5|knows_riding_2, man_face_young_1, man_face_old_2 ],
  
  ["bandit_forest_horseman", "Forest Horseman", "Forest Horsemen", tf_guarantee_recruit_armor|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_faction_1,
   [itm_axe, itm_mace_1, itm_long_spiked_club, itm_hatchet, itm_hunting_bow, itm_hunting_crossbow, itm_arrows_b, itm_bolts, itm_wooden_shield, itm_leather_covered_round_shield,
    itm_leather_boots, itm_nomad_boots, itm_hide_boots, itm_wrapping_boots,
    itm_leather_jerkin, itm_leather_armor, itm_ragged_outfit,
    itm_head_wrappings, itm_common_hood, itm_hood_b, itm_hood_c, itm_hood_d, itm_black_hood,
    itm_saddle_horse],
   str_10|agi_13|int_8|cha_7|level(15), wpex(65,60,65,55,50,40), knows_common|knows_power_strike_2|knows_power_draw_4|knows_athletics_3|knows_riding_4|knows_horse_archery_2, man_face_young_1, man_face_old_2 ],
  
  ["bandit_forest_archer", "Forest Archer", "Forest Archer", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_faction_1,
   [itm_mace_1, itm_hatchet, itm_short_bow, itm_barbed_arrows,
    itm_nomad_boots, itm_hide_boots, itm_leather_boots, itm_leather_gloves,
    itm_leather_armor, itm_leather_jerkin, itm_ragged_outfit,
    itm_head_wrappings, itm_common_hood, itm_hood_b, itm_hood_c, itm_hood_d, itm_black_hood,
    ],
   str_10|agi_17|int_9|cha_6|level(19), wpex(50,45,50,100,85,45), knows_common|knows_power_strike_2|knows_power_draw_4|knows_athletics_3|knows_riding_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_forest_leader", "Forest Leader", "Forest Leaders", tf_guarantee_common_armor|tf_guarantee_shield|tf_guarantee_ranged, no_scene, reserved, fac_faction_1,
   [itm_one_handed_war_axe_a, itm_mace_2, itm_falchion, itm_wooden_shield, itm_leather_covered_round_shield, itm_crossbow, itm_bolts, itm_short_bow, itm_bodkin_arrows,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_leather,
    itm_common_hood, itm_hood_b, itm_hood_c, itm_hood_d, itm_black_hood,
    ],
   str_14|agi_18|int_10|cha_9|level(28), wpex(85,80,85,90,75,45), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_power_draw_4|knows_athletics_5|knows_riding_2|knows_leadership_1, man_face_young_1, man_face_old_2 ],
  
  # Plain bandit
  ["bandit_looter", "Bandit Looter", "Bandit Looters", tf_guarantee_recruit_armor, no_scene, reserved, fac_faction_2,
   [itm_falchion, itm_mace_2, itm_hatchet, itm_club, itm_mace_1, itm_wooden_shield, itm_nordic_shield,
    itm_nomad_boots, itm_wrapping_boots,
    itm_pelt_coat, itm_leather_armor, itm_leather_jerkin, itm_fur_coat, itm_coarse_tunic, itm_tabard,
    itm_head_wrappings, itm_common_hood, itm_black_hood,
    ],
   str_9|agi_11|int_7|cha_6|level(10), wpex(65,55,55,25,35,30), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_athletics_3|knows_riding_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_poacher", "Bandit Poacher", "Bandit Poachers", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_faction_2,
   [itm_hunting_crossbow, itm_bolts, itm_falchion, itm_hatchet, itm_club, itm_mace_1, itm_wooden_shield, itm_nordic_shield,
    itm_nomad_boots, itm_wrapping_boots,
    itm_pelt_coat, itm_leather_armor, itm_fur_coat, itm_coarse_tunic, itm_tabard,
    itm_head_wrappings, itm_common_hood, itm_black_hood,
    ],
   str_8|agi_13|int_8|cha_6|level(12), wpex(60,50,50,45,60,40), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_athletics_4|knows_riding_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_rider", "Bandit Rider", "Bandit Riders", tf_guarantee_recruit_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_faction_2,
   [itm_falchion, itm_club, itm_mace_1, itm_spear, itm_wooden_shield, itm_nordic_shield,
    itm_nomad_boots, itm_wrapping_boots,
    itm_pelt_coat, itm_leather_armor, itm_leather_jerkin, itm_fur_coat, itm_coarse_tunic, itm_tabard,
    itm_head_wrappings, itm_common_hood, itm_black_hood,
    itm_sumpter_horse],
   str_10|agi_12|int_6|cha_7|level(12), wpex(60,50,65,25,35,30), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_athletics_2|knows_riding_4, man_face_young_1, man_face_old_2 ],
  
  ["bandit_marauder", "Bandit Marauder", "Bandit Marauders", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_faction_2,
   [itm_sword_medieval_a, itm_mace_3, itm_fighting_pick, itm_falchion, itm_scythe, itm_wooden_shield, itm_nordic_shield, itm_plate_covered_round_shield,
    itm_leather_boots, itm_nomad_boots, itm_leather_gloves,
    itm_haubergeon, itm_mail_hauberk, itm_mail_shirt,
    itm_black_hood, itm_nasal_helmet, itm_segmented_helmet,
    ],
   str_16|agi_12|int_6|cha_9|level(20), wpex(75,60,60,25,30,30), knows_common|knows_ironflesh_5|knows_power_strike_2|knows_athletics_3|knows_riding_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_thug", "Bandit Thug", "Bandit Thugs", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_faction_2,
   [itm_falchion, itm_mace_2, itm_hatchet, itm_club, itm_spiked_club, itm_mace_1, itm_wooden_shield, itm_nordic_shield, itm_hunting_crossbow, itm_bolts,
    itm_leather_boots, itm_nomad_boots, itm_leather_gloves,
    itm_leather_armor, itm_leather_jerkin, itm_fur_coat, itm_coarse_tunic, itm_tabard,
    itm_head_wrappings, itm_common_hood, itm_black_hood, itm_nasal_helmet,
    ],
   str_13|agi_14|int_7|cha_8|level(19), wpex(80,70,70,30,45,40), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_athletics_4|knows_riding_2, man_face_young_1, man_face_old_2 ],
  
  ["bandit_leader", "Bandit Leader", "Bandit Leaders", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_faction_2,
   [itm_sword_medieval_a, itm_mace_3, itm_fighting_pick, itm_falchion, itm_spear, itm_plate_covered_round_shield,
    itm_leather_boots, itm_leather_gloves,
    itm_haubergeon, itm_mail_hauberk, itm_mail_shirt,
    itm_black_hood, itm_nasal_helmet, itm_segmented_helmet,
    itm_sumpter_horse],
   str_19|agi_14|int_10|cha_11|level(31), wpex(85,75,90,30,35,40), knows_common|knows_ironflesh_6|knows_power_strike_3|knows_athletics_3|knows_riding_5|knows_leadership_1, man_face_young_1, man_face_old_2 ],
  
  # Mountain bandit
  ["bandit_mountain_rider", "Mountain Rider", "Mountain Riders", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_3,
   [itm_falchion, itm_maul, itm_one_handed_war_axe_a, itm_sword_medieval_a, itm_hide_covered_round_shield, itm_javelin,
    itm_nomad_boots, itm_leather_boots, itm_hide_boots,
    itm_leather_jerkin, itm_tribal_warrior_outfit, itm_ragged_outfit,
    itm_head_wrappings, itm_skullcap,
    itm_sumpter_horse, itm_saddle_horse],
   str_11|agi_9|int_6|cha_6|level(9), wpex(55,65,50,35,30,60), knows_common|knows_ironflesh_3|knows_power_strike_2|knows_power_throw_2|knows_power_draw_1|knows_athletics_2|knows_riding_4|knows_horse_archery_2, man_face_young_1, man_face_old_2 ],
  
  ["bandit_mountain_bandit", "Mountain Bandit", "Mountain Bandits", tf_guarantee_recruit_armor|tf_guarantee_shield, no_scene, reserved, fac_faction_3,
   [itm_falchion, itm_one_handed_war_axe_a, itm_sword_medieval_a, itm_hide_covered_round_shield, itm_fur_covered_shield, itm_javelin,
    itm_nomad_boots, itm_leather_boots, itm_hide_boots,
    itm_leather_jerkin, itm_tribal_warrior_outfit, itm_ragged_outfit,
    itm_head_wrappings, itm_skullcap,
    ],
   str_10|agi_10|int_7|cha_5|level(9), wpex(65,60,55,35,30,60), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_athletics_3|knows_riding_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_mountain_warrior", "Mountain Warrior", "Mountain Warriors", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_faction_3,
   [itm_falchion, itm_maul, itm_one_handed_battle_axe_a, itm_sword_medieval_a, itm_hide_covered_round_shield, itm_fur_covered_shield,
    itm_nomad_boots, itm_leather_boots, itm_leather_gloves,
    itm_tribal_warrior_outfit, itm_studded_leather_coat,
    itm_head_wrappings, itm_skullcap, itm_nasal_helmet,
    ],
   str_13|agi_11|int_7|cha_7|level(15), wpex(70,75,65,40,35,50), knows_common|knows_ironflesh_5|knows_power_strike_5|knows_power_throw_1|knows_power_draw_2|knows_athletics_3|knows_riding_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_mountain_raider", "Mountain Raider", "Mountain Raiders", tf_guarantee_common_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_faction_3,
   [itm_falchion, itm_maul, itm_one_handed_battle_axe_a, itm_sword_medieval_a, itm_hide_covered_round_shield, itm_javelin, itm_short_bow2, itm_arrows_b,
    itm_nomad_boots, itm_leather_boots, itm_hide_boots, itm_leather_gloves,
    itm_leather_jerkin, itm_tribal_warrior_outfit, itm_ragged_outfit, itm_studded_leather_coat,
    itm_head_wrappings, itm_skullcap, itm_nasal_helmet,
    itm_saddle_horse],
   str_14|agi_14|int_8|cha_8|level(21), wpex(65,70,60,55,40,65), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_3|knows_power_draw_4|knows_athletics_4|knows_riding_4|knows_horse_archery_3, man_face_young_1, man_face_old_2 ],
  
  ["bandit_mountain_hunter", "Mountain Hunter", "Mountain Hunters", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_faction_3,
   [itm_falchion, itm_one_handed_battle_axe_a, itm_sword_medieval_a, itm_hide_covered_round_shield, itm_fur_covered_shield, itm_short_bow2, itm_barbed_arrows,
    itm_nomad_boots, itm_leather_boots, itm_hide_boots,
    itm_leather_jerkin, itm_ragged_outfit,
    itm_head_wrappings, itm_skullcap,
    ],
   str_11|agi_11|int_7|cha_6|level(12), wpex(60,55,50,75,40,50), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_power_throw_1|knows_power_draw_4|knows_athletics_3|knows_riding_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_mountain_chieftain", "Mountain Chieftain", "Mountain Chieftains", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_faction_3,
   [itm_falchion, itm_maul, itm_one_handed_battle_axe_a, itm_sword_medieval_a, itm_hide_covered_round_shield, itm_javelin,
    itm_leather_boots, itm_leather_gloves,
    itm_studded_leather_coat,
    itm_skullcap, itm_nasal_helmet,
    itm_saddle_horse],
   str_17|agi_17|int_10|cha_10|level(31), wpex(70,75,65,60,40,70), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_3|knows_power_draw_2|knows_athletics_4|knows_riding_5|knows_horse_archery_3|knows_leadership_1, man_face_young_1, man_face_old_2 ],
  
  # Sea raider
  ["bandit_sea_raider", "Sea Raider", "Sea Raiders", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_faction_4,
   [itm_sword_viking_1, itm_fighting_axe, itm_two_handed_axe, itm_spear, itm_light_throwing_axes, itm_javelin, itm_short_bow2, itm_arrows_b, itm_wooden_shield, itm_nordic_shield, itm_kite_shield_a, itm_round_shield,
    itm_leather_boots, itm_nomad_boots, itm_leather_gloves,
    itm_leather_jerkin,
    itm_nasal_helmet, itm_nordic_footman_helmet, itm_leather_cap, itm_nordic_archer_helmet, itm_skullcap, itm_nordic_veteran_archer_helmet,
    ],
   str_14|agi_13|int_6|cha_8|level(18), wpex(85,95,80,50,25,55), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_2|knows_power_draw_4|knows_athletics_2, man_face_young_1, man_face_old_2 ],
  
  ["bandit_sea_rider", "Sea Rider", "Sea Riders", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_4,
   [itm_sword_viking_1, itm_fighting_axe, itm_two_handed_axe, itm_spear, itm_light_throwing_axes, itm_javelin, itm_short_bow2, itm_arrows_b, itm_wooden_shield, itm_nordic_shield, itm_round_shield,
    itm_nomad_boots, itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin,
    itm_nasal_helmet, itm_nordic_footman_helmet, itm_leather_cap, itm_nordic_archer_helmet, itm_skullcap, itm_nordic_veteran_archer_helmet,
    itm_sumpter_horse],
   str_13|agi_13|int_6|cha_7|level(16), wpex(80,90,80,45,25,50), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_throw_2|knows_power_draw_4|knows_athletics_1|knows_riding_4|knows_horse_archery_2, man_face_young_1, man_face_old_2 ],
  
  ["bandit_skull_crusher", "Skull Crusher", "Skull Crushers", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_faction_4,
   [itm_sword_viking_2, itm_fighting_axe, itm_two_handed_battle_axe_2, itm_war_spear, itm_long_bow, itm_barbed_arrows, itm_throwing_axes, itm_javelin, itm_wooden_shield, itm_nordic_shield, itm_kite_shield_a, itm_round_shield,
    itm_mail_chausses, itm_leather_boots, itm_leather_gloves,
    itm_byrnie, itm_mail_shirt, itm_mail_hauberk,
    itm_nordic_fighter_helmet, itm_nordic_helmet, itm_nordic_huscarl_helmet,
    ],
   str_17|agi_16|int_7|cha_10|level(27), wpex(105,115,100,60,30,65), knows_common|knows_ironflesh_4|knows_power_strike_5|knows_power_throw_3|knows_power_draw_6|knows_athletics_2|knows_riding_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_sea_hunter", "Sea Hunter", "Sea Hunters", tf_guarantee_common_armor|tf_guarantee_ranged, no_scene, reserved, fac_faction_4,
   [itm_sword_viking_1, itm_fighting_axe, itm_short_bow2, itm_barbed_arrows, itm_wooden_shield, itm_nordic_shield, itm_kite_shield_a, itm_round_shield,
    itm_leather_boots, itm_nomad_boots, itm_leather_gloves,
    itm_byrnie,
    itm_nasal_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    ],
   str_15|agi_16|int_7|cha_8|level(23), wpex(90,95,80,85,35,55), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_2|knows_power_draw_4|knows_athletics_3, man_face_young_1, man_face_old_2 ],
  
  ["bandit_pillager", "Pillager", "Pillagers", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_faction_4,
   [itm_sword_viking_1, itm_fighting_axe, itm_two_handed_axe, itm_throwing_axes, itm_wooden_shield, itm_nordic_shield, itm_kite_shield_a, itm_round_shield,
    itm_nomad_boots, itm_leather_boots, itm_leather_gloves,
    itm_byrnie, itm_mail_shirt,
    itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_nordic_helmet,
    ],
   str_14|agi_16|int_8|cha_9|level(24), wpex(95,100,85,60,25,75), knows_common|knows_ironflesh_3|knows_power_strike_4|knows_power_throw_4|knows_power_draw_2|knows_athletics_3, man_face_young_1, man_face_old_2 ],
  
  ["bandit_sea_captain", "Sea Captain", "Sea Captains", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_faction_4,
   [itm_sword_viking_2, itm_sword_viking_2_small, itm_two_handed_battle_axe_2, itm_war_spear, itm_throwing_axes, itm_javelin, itm_wooden_shield, itm_nordic_shield, itm_kite_shield_a, itm_round_shield,
    itm_mail_chausses, itm_mail_mittens,
    itm_mail_hauberk,
    itm_nordic_huscarl_helmet, itm_nordic_helmet,
    itm_sumpter_horse],
   str_19|agi_18|int_10|cha_12|level(36), wpex(115,105,110,65,30,70), knows_common|knows_ironflesh_5|knows_power_strike_4|knows_power_throw_4|knows_power_draw_2|knows_athletics_3|knows_riding_5|knows_horse_archery_2|knows_leadership_1, man_face_young_1, man_face_old_2 ],
  
  # Steppe bandit
  ["bandit_steppe_bandit", "Steppe Bandit", "Steppe Bandits", tf_guarantee_recruit_armor, no_scene, reserved, fac_faction_5,
   [itm_sword_khergit_1, itm_javelin, itm_hunting_bow, itm_arrows_b, itm_leather_covered_round_shield,
    itm_hide_boots, itm_nomad_boots,
    itm_leather_vest, itm_coarse_tunic,
    itm_nomad_cap, itm_leather_steppe_cap_a, itm_nomad_cap_b,
    itm_steppe_horse],
   str_7|agi_13|int_6|cha_6|level(9), wpex(55,45,60,60,25,55), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_throw_2|knows_power_draw_4|knows_athletics_3|knows_riding_4|knows_horse_archery_4, man_face_young_1, man_face_old_2 ],
  
  ["bandit_steppe_rider", "Steppe Rider", "Steppe Riders", tf_guarantee_recruit_armor|tf_guarantee_horseman, no_scene, reserved, fac_faction_5,
   [itm_sword_khergit_2, itm_winged_mace, itm_javelin, itm_light_lance, itm_leather_covered_round_shield,
    itm_hide_boots, itm_nomad_boots, itm_leather_boots, itm_leather_gloves,
    itm_leather_vest, itm_coarse_tunic, itm_steppe_armor,
    itm_leather_steppe_cap_c, itm_nomad_cap, itm_leather_steppe_cap_a, itm_nomad_cap_b, itm_steppe_cap, itm_leather_steppe_cap_b,
    itm_steppe_horse],
   str_9|agi_14|int_6|cha_7|level(13), wpex(75,60,80,65,25,65), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_2|knows_power_draw_3|knows_athletics_2|knows_riding_5|knows_horse_archery_4, man_face_young_1, man_face_old_2 ],
  
  ["bandit_steppe_lancer", "Steppe Lancer", "Steppe Lancers", tf_guarantee_common_armor|tf_guarantee_horseman|tf_guarantee_shield, no_scene, reserved, fac_faction_5,
   [itm_light_lance, itm_leather_covered_round_shield,
    itm_hide_boots, itm_nomad_boots, itm_leather_boots, itm_leather_gloves,
    itm_tribal_warrior_outfit, itm_nomad_robe, itm_nomad_vest,
    itm_leather_steppe_cap_c, itm_nomad_cap, itm_leather_steppe_cap_a, itm_nomad_cap_b, itm_steppe_cap, itm_leather_steppe_cap_b,
    itm_steppe_horse],
   str_10|agi_15|int_7|cha_8|level(17), wpex(70,55,90,65,25,55), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_2|knows_power_draw_3|knows_athletics_2|knows_riding_5|knows_horse_archery_4, man_face_young_1, man_face_old_2 ],
  
  ["bandit_steppe_hunter", "Steppe Hunter", "Steppe Hunters", tf_guarantee_recruit_armor|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_faction_5,
   [itm_sword_khergit_1, itm_nomad_bow, itm_barbed_arrows, itm_javelin,
    itm_hide_boots, itm_nomad_boots,
    itm_steppe_armor, itm_nomad_vest, itm_leather_vest, itm_coarse_tunic,
    itm_leather_steppe_cap_c, itm_nomad_cap, itm_leather_steppe_cap_a, itm_nomad_cap_b, itm_leather_steppe_cap_b,
    itm_steppe_horse],
   str_8|agi_15|int_6|cha_7|level(13), wpex(45,35,50,60,35,55), knows_common|knows_power_strike_2|knows_power_throw_2|knows_power_draw_5|knows_athletics_3|knows_riding_5|knows_horse_archery_5, man_face_young_1, man_face_old_2 ],
  
  ["bandit_steppe_archer", "Steppe Archer", "Steppe Archers", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_faction_5,
   [itm_sword_khergit_1, itm_short_bow, itm_barbed_arrows, itm_leather_covered_round_shield,
    itm_hide_boots, itm_nomad_boots,
    itm_steppe_armor, itm_leather_vest, itm_coarse_tunic,
    itm_nomad_cap, itm_leather_steppe_cap_a, itm_nomad_cap_b, itm_leather_steppe_cap_b,
    ],
   str_9|agi_13|int_6|cha_6|level(11), wpex(50,40,55,75,35,55), knows_common|knows_power_strike_2|knows_power_throw_2|knows_power_draw_4|knows_athletics_4|knows_riding_4|knows_horse_archery_4, man_face_young_1, man_face_old_2 ],
  
  ["bandit_steppe_chief", "Steppe Chief", "Steppe Chief", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_faction_5,
   [itm_sword_khergit_2, itm_winged_mace, itm_nomad_bow, itm_barbed_arrows, itm_leather_covered_round_shield,
    itm_nomad_boots, itm_leather_boots, itm_leather_gloves,
    itm_tribal_warrior_outfit, itm_nomad_robe,
    itm_leather_steppe_cap_c, itm_nomad_cap, itm_leather_steppe_cap_a, itm_nomad_cap_b, itm_steppe_cap, itm_leather_steppe_cap_b,
    itm_steppe_horse],
   str_14|agi_18|int_10|cha_10|level(29), wpex(80,65,90,85,25,55), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_2|knows_power_draw_5|knows_athletics_3|knows_riding_5|knows_horse_archery_5|knows_leadership_1, man_face_young_1, man_face_old_2 ],
  
  # Tundra bandit
  ["bandit_tundra_bandit", "Tundra Bandit", "Tundra Bandits", tf_guarantee_recruit_armor, no_scene, reserved, fac_faction_6,
   [itm_winged_mace, itm_sword_khergit_1, itm_javelin, itm_short_bow, itm_arrows, itm_leather_covered_round_shield,
    itm_hide_boots, itm_nomad_boots,
    itm_fur_coat, itm_rawhide_coat, itm_leather_vest, itm_coarse_tunic,
    itm_nomad_cap, itm_vaegir_fur_cap, itm_vaegir_fur_cap, itm_leather_steppe_cap_b,
    ],
   str_9|agi_10|int_7|cha_7|level(10), wpex(55,45,45,65,20,45), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_throw_2|knows_power_draw_4|knows_athletics_3|knows_riding_2|knows_horse_archery_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_tundra_rider", "Tundra Rider", "Tundra Riders", tf_guarantee_recruit_armor|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_faction_6,
   [itm_winged_mace, itm_sword_khergit_1, itm_javelin, itm_short_bow, itm_arrows, itm_leather_covered_round_shield,
    itm_hide_boots, itm_nomad_boots,
    itm_fur_coat, itm_rawhide_coat, itm_leather_vest, itm_coarse_tunic,
    itm_nomad_cap, itm_vaegir_fur_cap, itm_vaegir_fur_cap, itm_leather_steppe_cap_b,
    itm_steppe_horse, itm_sumpter_horse, itm_saddle_horse],
   str_10|agi_11|int_7|cha_8|level(13), wpex(50,40,40,65,20,45), knows_common|knows_power_strike_2|knows_power_throw_2|knows_power_draw_4|knows_athletics_1|knows_riding_4|knows_horse_archery_4, man_face_young_1, man_face_old_2 ],
  
  ["bandit_tundra_hunter", "Tundra Hunter", "Tundra Hunters", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_faction_6,
   [itm_winged_mace, itm_sword_khergit_1, itm_nomad_bow, itm_barbed_arrows,
    itm_nomad_boots, itm_hide_boots,
    itm_fur_coat, itm_rawhide_coat, itm_leather_vest, itm_coarse_tunic,
    itm_nomad_cap, itm_vaegir_fur_cap, itm_vaegir_fur_cap, itm_leather_steppe_cap_b,
    ],
   str_9|agi_12|int_7|cha_9|level(14), wpex(45,35,35,55,25,40), knows_common|knows_power_strike_2|knows_power_throw_1|knows_power_draw_5|knows_athletics_2|knows_riding_2|knows_horse_archery_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_taiga_bandit", "Taiga Bandit", "Taiga Bandits", tf_guarantee_common_armor|tf_guarantee_shield, no_scene, reserved, fac_faction_6,
   [itm_winged_mace, itm_spiked_mace, itm_sword_khergit_2, itm_scimitar, itm_jarid, itm_leather_covered_round_shield,
    itm_nomad_boots, itm_leather_boots, itm_leather_gloves,
    itm_fur_coat, itm_rawhide_coat, itm_khergit_armor, itm_nomad_armor, itm_leather_jerkin,
    itm_nomad_cap, itm_vaegir_fur_cap, itm_vaegir_fur_cap, itm_steppe_cap, itm_leather_steppe_cap_b,
    ],
   str_13|agi_12|int_8|cha_10|level(20), wpex(60,50,50,60,20,60), knows_common|knows_ironflesh_2|knows_power_strike_4|knows_power_throw_4|knows_power_draw_2|knows_athletics_4|knows_riding_2|knows_horse_archery_2, man_face_young_1, man_face_old_2 ],
  
  ["bandit_taiga_hunter", "Taiga Hunter", "Taiga Hunters", tf_guarantee_common_armor|tf_guarantee_ranged, no_scene, reserved, fac_faction_6,
   [itm_winged_mace, itm_sword_khergit_2, itm_strong_bow, itm_barbed_arrows,
    itm_nomad_boots, itm_leather_boots, itm_leather_gloves,
    itm_fur_coat, itm_rawhide_coat, itm_khergit_armor, itm_nomad_armor, itm_leather_jerkin,
    itm_nomad_cap, itm_vaegir_fur_cap, itm_vaegir_fur_cap, itm_steppe_cap, itm_leather_steppe_cap_b,
    ],
   str_12|agi_13|int_8|cha_11|level(21), wpex(55,45,45,65,25,45), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_throw_2|knows_power_draw_5|knows_athletics_3|knows_riding_2|knows_horse_archery_2, man_face_young_1, man_face_old_2 ],
  
  ["bandit_taiga_chieftain", "Taiga Chieftain", "Taiga Chieftains", tf_guarantee_trained_armor|tf_guarantee_shield|tf_guarantee_ranged|tf_guarantee_horseman, no_scene, reserved, fac_faction_6,
   [itm_winged_mace, itm_sword_khergit_2, itm_scimitar, itm_strong_bow, itm_barbed_arrows, itm_leather_covered_round_shield,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin, itm_tribal_warrior_outfit,
    itm_nomad_cap, itm_vaegir_fur_cap, itm_vaegir_fur_cap, itm_steppe_cap, itm_leather_steppe_cap_b,
    itm_steppe_horse],
   str_16|agi_18|int_10|cha_13|level(34), wpex(65,60,60,70,25,45), knows_common|knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_power_draw_5|knows_athletics_3|knows_riding_5|knows_horse_archery_4|knows_leadership_1, man_face_young_1, man_face_old_2 ],
  
  # Desert bandit
  ["bandit_desert_bandit", "Desert Bandit", "Desert Bandits", tf_guarantee_recruit_armor|tf_guarantee_ranged|tf_guarantee_shield, no_scene, reserved, fac_faction_7,
   [itm_mace_2, itm_arabian_sword_a, itm_javelin, itm_leather_covered_round_shield,
    itm_sarranid_boots_a, itm_sarranid_boots_b,
    itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b,
    itm_sarranid_felt_hat, itm_turban, itm_desert_turban,
    ],
   str_9|agi_9|int_7|cha_6|level(8), wpex(40,35,35,40,30,65), knows_common|knows_power_strike_2|knows_power_throw_2|knows_athletics_2|knows_riding_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_desert_rider", "Desert Rider", "Desert Riders", tf_guarantee_common_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_faction_7,
   [itm_mace_2, itm_arabian_sword_a, itm_javelin, itm_spear, itm_leather_covered_round_shield,
    itm_sarranid_boots_a, itm_sarranid_boots_b,
    itm_skirmisher_armor, itm_archers_vest,
    itm_turban, itm_desert_turban,
    itm_arabian_horse_a],
   str_10|agi_14|int_7|cha_9|level(17), wpex(50,35,55,45,30,60), knows_common|knows_ironflesh_1|knows_power_strike_3|knows_power_throw_2|knows_athletics_2|knows_riding_4|knows_horse_archery_2, man_face_young_1, man_face_old_2 ],
  
  ["bandit_desert_hunter", "Desert Hunter", "Desert Hunters", tf_guarantee_common_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_faction_7,
   [itm_mace_2, itm_arabian_sword_a, itm_hunting_bow2, itm_barbed_arrows, itm_leather_covered_round_shield,
    itm_sarranid_boots_a, itm_sarranid_boots_b,
    itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b, itm_skirmisher_armor,
    itm_sarranid_felt_hat, itm_turban, itm_desert_turban,
    itm_arabian_horse_a],
   str_9|agi_13|int_8|cha_8|level(15), wpex(40,35,35,60,30,55), knows_common|knows_power_strike_2|knows_power_throw_1|knows_power_draw_4|knows_athletics_3|knows_riding_4|knows_horse_archery_3, man_face_young_1, man_face_old_2 ],
  
  ["bandit_desert_nomad", "Desert Nomad", "Desert Nomads", tf_guarantee_common_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_faction_7,
   [itm_mace_2, itm_arabian_sword_a, itm_javelin, itm_light_lance, itm_leather_covered_round_shield,
    itm_sarranid_boots_a, itm_sarranid_boots_b, itm_leather_gloves,
    itm_skirmisher_armor, itm_archers_vest,
    itm_turban, itm_desert_turban,
    itm_arabian_horse_a, itm_arabian_horse_b],
   str_12|agi_15|int_8|cha_10|level(22), wpex(65,40,70,45,30,75), knows_common|knows_ironflesh_2|knows_power_strike_3|knows_power_throw_2|knows_power_draw_2|knows_athletics_4|knows_riding_5|knows_horse_archery_3, man_face_young_1, man_face_old_2 ],
  
  ["bandit_desert_marauder", "Desert Marauder", "Desert Marauders", tf_guarantee_trained_armor|tf_guarantee_shield, no_scene, reserved, fac_faction_7,
   [itm_mace_3, itm_arabian_sword_a, itm_spear, itm_leather_covered_round_shield,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_sarranid_leather_armor,
    itm_turban, itm_desert_turban,
    ],
   str_12|agi_12|int_7|cha_8|level(16), wpex(55,45,60,40,30,60), knows_common|knows_ironflesh_4|knows_power_strike_2|knows_power_throw_1|knows_athletics_1|knows_riding_1, man_face_young_1, man_face_old_2 ],
  
  ["bandit_desert_chief", "Desert Chief", "Desert Chiefs", tf_guarantee_trained_armor|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_horseman, no_scene, reserved, fac_faction_7,
   [itm_mace_3, itm_arabian_sword_b, itm_javelin, itm_leather_covered_round_shield,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_sarranid_leather_armor,
    itm_turban, itm_desert_turban,
    itm_arabian_horse_a, itm_arabian_horse_b],
   str_14|agi_19|int_10|cha_12|level(32), wpex(70,60,60,40,30,65), knows_common|knows_ironflesh_5|knows_power_strike_3|knows_power_throw_3|knows_athletics_3|knows_riding_5|knows_horse_archery_4|knows_leadership_1, man_face_young_1, man_face_old_2 ],
  
  
  # Common
  ["common_hunter_bow", "Hunter", "Hunters", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_knife, itm_butchering_knife, itm_hunting_bow, itm_arrows_b,
    itm_wrapping_boots, itm_hide_boots,
    itm_rawhide_coat, itm_fur_coat, itm_pelt_coat
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,80,65,35), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, man_face_young_1, man_face_old_2 ],
  ["common_hunter_crossbow", "Hunter", "Hunters", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_knife, itm_butchering_knife, itm_hunting_crossbow, itm_bolts,
    itm_wrapping_boots, itm_hide_boots,
    itm_rawhide_coat, itm_fur_coat, itm_pelt_coat
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,60,75,35), knows_common|knows_ironflesh_2|knows_power_strike_2|knows_athletics_2|knows_riding_1, man_face_young_1, man_face_old_2 ],
  ["common_hunter_throw", "Hunter", "Hunters", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_knife, itm_butchering_knife, itm_javelin, itm_javelin,
    itm_wrapping_boots, itm_hide_boots,
    itm_rawhide_coat, itm_fur_coat, itm_pelt_coat
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,45,40,55), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_throw_2|knows_athletics_3|knows_riding_1, man_face_young_1, man_face_old_2 ],
  ["common_hunter_sarranid_throw", "Hunter", "Hunters", tf_guarantee_recruit_armor|tf_guarantee_ranged, no_scene, reserved, fac_commoners,
   [itm_knife, itm_butchering_knife, itm_javelin, itm_javelin,
    itm_sarranid_boots_a, itm_sarranid_boots_b,
    itm_skirmisher_armor, itm_sarranid_cloth_robe_b, itm_sarranid_cloth_robe,
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,45,40,55), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_throw_2|knows_athletics_3|knows_riding_1, man_face_young_1, man_face_old_2 ],
  ["common_peasant", "Peasant", "Peasants", tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
   [itm_pitch_fork, itm_sickle, itm_hatchet,
    itm_wrapping_boots, itm_hide_boots,
    itm_coarse_tunic, itm_leather_apron, itm_linen_tunic
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,80,65,35), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, man_face_young_1, man_face_old_2 ],
  ["common_peasant_woman", "Peasant", "Peasants", tf_female|tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
   [itm_pitch_fork, itm_sickle, itm_hatchet,
    itm_wrapping_boots, itm_hide_boots,
    itm_coarse_tunic, itm_leather_apron, itm_linen_tunic
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,80,65,35), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, man_face_young_1, man_face_old_2 ],
  ["common_wealthy", "Wealthy Merchant", "Wealthy Merchants", tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
   [itm_dagger, itm_sword_medieval_b_small,
    itm_leather_boots, itm_ankle_boots,
    itm_tabard, itm_red_shirt
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,80,65,35), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, man_face_young_1, man_face_old_2 ],
  ["common_noble", "Noble ", "Nobles", tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
   [itm_sword_medieval_b_small, itm_sword_viking_2_small, itm_scimitar,
    itm_leather_boots, itm_ankle_boots,
    itm_tabard, itm_red_shirt
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,80,65,35), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, man_face_young_1, man_face_old_2 ],
  ["common_beggar", "Beggar ", "Beggars", tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
   [itm_stones, itm_wooden_stick, itm_knife,
    itm_wrapping_boots,
    itm_coarse_tunic
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,80,65,35), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, man_face_young_1, man_face_old_2 ],
  ["common_beggar_woman", "Beggar ", "Beggars", tf_female|tf_guarantee_recruit_armor, no_scene, reserved, fac_commoners,
   [itm_stones, itm_wooden_stick, itm_knife,
    itm_wrapping_boots, itm_hide_boots,
    itm_coarse_tunic
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,80,65,35), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, man_face_young_1, man_face_old_2 ],
  
  ["swadian_peasant", "Swadian Peasant", "Swadian Peasants", tf_guarantee_recruit_armor, no_scene, reserved, fac_kingdom_1,
   [itm_pitch_fork, itm_sickle, itm_scythe,
    itm_wrapping_boots, itm_hide_boots,
    itm_coarse_tunic, itm_leather_apron, itm_red_shirt
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,80,65,35), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, swadian_face_young_1, swadian_face_old_2 ],
  ["vaegir_peasant", "Vaegir Peasant", "Vaegir Peasants", tf_guarantee_recruit_armor, no_scene, reserved, fac_kingdom_2,
   [itm_pitch_fork, itm_sickle, itm_hatchet,
    itm_wrapping_boots, itm_hide_boots,
    itm_fur_coat, itm_linen_tunic
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,80,65,35), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, vaegir_face_young_1, vaegir_face_old_2 ],
  ["khergit_peasant", "Khergit Peasant", "Khergit Peasants", tf_guarantee_recruit_armor, no_scene, reserved, fac_kingdom_3,
   [itm_pitch_fork, itm_sickle, itm_butchering_knife,
    itm_wrapping_boots, itm_hide_boots,
    itm_coarse_tunic, itm_linen_tunic
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,80,65,35), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, khergit_face_young_1, khergit_face_old_2 ],
  ["nord_peasant", "Nord Peasant", "Nord Peasants", tf_guarantee_recruit_armor, no_scene, reserved, fac_kingdom_4,
   [itm_pitch_fork, itm_cleaver, itm_hatchet,
    itm_wrapping_boots, itm_hide_boots,
    itm_coarse_tunic, itm_leather_apron, itm_fur_coat
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,80,65,35), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, nord_face_young_1, nord_face_old_2 ],
  ["rhodok_peasant", "Rhodok Peasant", "Rhodok Peasants", tf_guarantee_recruit_armor, no_scene, reserved, fac_kingdom_5,
   [itm_pitch_fork, itm_sickle, itm_butchering_knife,
    itm_wrapping_boots, itm_hide_boots,
    itm_coarse_tunic, itm_tabard, itm_tunic_with_green_cape
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,80,65,35), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, rhodok_face_young_1, rhodok_face_old_2 ],
  ["sarranid_peasant", "Sarranid Peasant", "Sarranid Peasants", tf_guarantee_recruit_armor, no_scene, reserved, fac_kingdom_6,
   [itm_pitch_fork, itm_sickle, itm_hatchet,
    itm_wrapping_boots, itm_hide_boots,
    itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b
    
    ],
   str_9|agi_7|int_5|cha_5|level(2), wpex(50,55,45,80,65,35), knows_common|knows_ironflesh_1|knows_power_strike_2|knows_power_draw_4|knows_athletics_2|knows_riding_1, sarranid_face_young_1, sarranid_face_old_2 ],
  
  #############
  # Templates #
  #############
  # str_|agi_|int_|cha_|level(), wpex(),
  # knows_lord_|knows_ironflesh_|knows_power_strike_|knows_power_throw_|knows_power_draw_|knows_athletics_|knows_riding_|knows_shield_|knows_horse_archery_
  ["swadian_lord_template_0", "Knight", "Knight", tf_is_merchant, no_scene, reserved, fac_culture_1,
   [itm_sword_medieval_a, itm_sword_medieval_a_long, itm_fighting_pick, itm_mace_2,
    itm_light_lance, itm_hunting_bow2, itm_hunting_crossbow, itm_bolts, itm_arrows_b,
    itm_tab_shield_heater_b, itm_tab_shield_heater_cav_a,
    itm_leather_boots, itm_ankle_boots, itm_leather_gloves,
    itm_gambeson_herald, itm_padded_cloth, itm_leather_armor_herald, itm_leather_jerkin_herald,
    itm_mail_coif, itm_norman_helmet, itm_helmet_with_neckguard, itm_footman_helmet,
    itm_saddle_horse, itm_pack_horse],
   def_lord_0_str|level(4), wp_swadian(wp_template_0), knows_lord_swadian_0, 0, 0 ],
  ["swadian_lord_template_1", "Knight", "Knight", tf_is_merchant, no_scene, reserved, fac_culture_1,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_fighting_pick, itm_mace_3, itm_bastard_sword_a,
    itm_light_lance, itm_hunting_bow2, itm_hunting_crossbow, itm_bolts, itm_arrows_b,
    itm_tab_shield_heater_b, itm_tab_shield_heater_cav_a,
    itm_leather_boots, itm_leather_gloves,
    itm_padded_leather_herald, itm_leather_jerkin_herald, itm_heraldic_mail_with_tunic_b,
    itm_mail_coif, itm_norman_helmet, itm_helmet_with_neckguard, itm_footman_helmet,
    itm_pack_horse],
   def_lord_1_str|level(4), wp_swadian(wp_template_1), knows_lord_swadian_1, 0, 0 ],
  ["swadian_lord_template_2", "Baron", "Baron", tf_is_merchant, no_scene, reserved, fac_culture_1,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_fighting_pick, itm_mace_3, itm_bastard_sword_a, itm_sword_two_handed_a,
    itm_light_lance, itm_hunting_bow2, itm_hunting_crossbow, itm_bolts, itm_barbed_arrows, itm_darts,
    itm_tab_shield_heater_b, itm_tab_shield_heater_cav_a,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_haubergeon_herald, itm_heraldic_mail_with_tunic,
    itm_mail_coif, itm_helmet_with_neckguard, itm_flat_topped_helmet, itm_kettle_hat,
    itm_hunter],
   def_lord_2_str|level(4), wp_swadian(wp_template_2), knows_lord_swadian_2, 0, 0 ],
  ["swadian_lord_template_3", "Viscount", "Viscount", tf_is_merchant, no_scene, reserved, fac_culture_1,
   [itm_sword_medieval_c, itm_sword_medieval_c_small, itm_sword_medieval_c_long, itm_military_sickle_a, itm_mace_4, itm_bastard_sword_a, itm_sword_two_handed_a,
    itm_lance, itm_hunting_bow2, itm_hunting_crossbow, itm_bolts, itm_barbed_arrows, itm_darts,
    itm_tab_shield_heater_b, itm_tab_shield_heater_cav_a,
    itm_mail_chausses, itm_mail_mittens,
    itm_mail_with_surcoat_herald, itm_haubergeon_herald, itm_heraldic_mail_with_tunic,
    itm_bascinet, itm_bascinet_b, itm_bascinet_c, itm_kettle_hat, itm_flat_topped_helmet,
    itm_hunter, itm_warhorse],
   def_lord_3_str|level(4), wp_swadian(wp_template_3), knows_lord_swadian_3, 0, 0 ],
  ["swadian_lord_template_4", "Count", "Count", tf_is_merchant, no_scene, reserved, fac_culture_1,
   [itm_sword_medieval_c, itm_sword_medieval_c_small, itm_sword_medieval_c_long, itm_military_sickle_a, itm_morningstar, itm_mace_4, itm_bastard_sword_b, itm_sword_two_handed_a,
    itm_lance, itm_short_bow2, itm_light_crossbow, itm_steel_bolts, itm_bodkin_arrows, itm_war_darts,
    itm_tab_shield_heater_c, itm_tab_shield_heater_cav_b,
    itm_mail_boots, itm_mail_mittens,
    itm_mail_with_surcoat_herald, itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_tabard,
    itm_guard_helmet, itm_guard_helmet, itm_bascinet, itm_bascinet_b, itm_bascinet_c,
    itm_warhorse],
   def_lord_4_str|level(4), wp_swadian(wp_template_4), knows_lord_swadian_4, 0, 0 ],
  ["swadian_lord_template_5", "Duke", "Duke", tf_is_merchant, no_scene, reserved, fac_culture_1,
   [itm_sword_medieval_c, itm_sword_medieval_c_small, itm_sword_medieval_c_long, itm_morningstar, itm_bastard_sword_b, itm_sword_two_handed_b,
    itm_heavy_lance, itm_short_bow2, itm_light_crossbow, itm_steel_bolts, itm_bodkin_arrows, itm_war_darts,
    itm_tab_shield_heater_d, itm_tab_shield_heater_cav_b,
    itm_iron_greaves, itm_mail_mittens, itm_gauntlets,
    itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_tabard, itm_coat_of_plates_herald,
    itm_guard_helmet, itm_great_helmet_herald,
    itm_warhorse, itm_warhorse, itm_charger, itm_charger_b],
   def_lord_5_str|level(4), wp_swadian(wp_template_5), knows_lord_swadian_5, 0, 0 ],
  ["swadian_lord_template_6", "Marshall", "Marshall", tf_is_merchant, no_scene, reserved, fac_culture_1,
   [itm_sword_medieval_c, itm_sword_medieval_c_long, itm_morningstar, itm_bastard_sword_b, itm_sword_two_handed_b,
    itm_heavy_lance, itm_short_bow2, itm_light_crossbow, itm_steel_bolts, itm_bodkin_arrows, itm_war_darts,
    itm_tab_shield_heater_cav_b,
    itm_iron_greaves, itm_gauntlets,
    itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_tabard,
    itm_great_helmet_herald, itm_winged_great_helmet,
    itm_warhorse, itm_warhorse, itm_charger, itm_charger_b],
   def_lord_6_str|level(4), wp_swadian(wp_template_6), knows_lord_swadian_6, 0, 0 ],
  ["swadian_lord_template_7", "King", "King", tf_is_merchant, no_scene, reserved, fac_culture_1,
   [itm_sword_medieval_c, itm_sword_medieval_c_long, itm_morningstar, itm_sword_two_handed_b,
    itm_heavy_lance, itm_short_bow2, itm_light_crossbow, itm_steel_bolts, itm_bodkin_arrows, itm_war_darts,
    itm_tab_shield_heater_cav_b,
    itm_iron_greaves, itm_gauntlets,
    itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_tabard, itm_plate_armor_herald,
    itm_great_helmet_herald, itm_winged_great_helmet,
    itm_warhorse, itm_warhorse, itm_charger, itm_charger_b],
   def_lord_7_str|level(4), wp_swadian(wp_template_7), knows_lord_swadian_7, 0, 0 ],
  
  ["vaegir_lord_template_0", "Knight", "Knight", tf_is_merchant, no_scene, reserved, fac_culture_2,
   [itm_sword_khergit_1, itm_two_handed_axe, itm_one_handed_battle_axe_a,
    itm_javelin, itm_hunting_bow, itm_arrows,
    itm_tab_shield_kite_b, itm_tab_shield_kite_cav_a,
    itm_leather_boots, itm_nomad_boots, itm_hide_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_leather_jerkin_herald,
    itm_vaegir_fur_cap, itm_vaegir_fur_helmet,
    itm_saddle_horse, itm_steppe_horse],
   def_lord_0_bal|level(4), wp_vaegir(wp_template_0), knows_lord_vaegir_0, 0, 0 ],
  ["vaegir_lord_template_1", "Knight", "Knight", tf_is_merchant, no_scene, reserved, fac_culture_2,
   [itm_scimitar, itm_two_handed_axe, itm_one_handed_battle_axe_a,
    itm_light_lance, itm_javelin, itm_short_bow, itm_barbed_arrows,
    itm_tab_shield_kite_b, itm_tab_shield_kite_cav_a,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald, itm_tribal_warrior_outfit,
    itm_vaegir_fur_cap, itm_vaegir_fur_helmet,
    itm_steppe_horse, itm_pack_horse],
   def_lord_1_bal|level(4), wp_vaegir(wp_template_1), knows_lord_vaegir_1, 0, 0 ],
  ["vaegir_lord_template_2", "Baron", "Baron", tf_is_merchant, no_scene, reserved, fac_culture_2,
   [itm_scimitar, itm_two_handed_battle_axe_2, itm_one_handed_battle_axe_a,
    itm_light_lance, itm_javelin, itm_nomad_bow, itm_barbed_arrows,
    itm_tab_shield_kite_b, itm_tab_shield_kite_cav_a,
    itm_leather_boots, itm_leather_gloves,
    itm_studded_leather_coat_herald,
    itm_vaegir_fur_helmet, itm_vaegir_spiked_helmet,
    itm_steppe_horse, itm_pack_horse],
   def_lord_2_bal|level(4), wp_vaegir(wp_template_2), knows_lord_vaegir_2, 0, 0 ],
  ["vaegir_lord_template_3", "Viscount", "Viscount", tf_is_merchant, no_scene, reserved, fac_culture_2,
   [itm_scimitar, itm_two_handed_battle_axe_2, itm_one_handed_battle_axe_a,
    itm_light_lance, itm_javelin, itm_nomad_bow, itm_bodkin_arrows,
    itm_tab_shield_kite_b, itm_tab_shield_kite_cav_a,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_mail_hauberk_herald, itm_studded_leather_coat_herald, itm_lamellar_vest_herald,
    itm_vaegir_helmet, itm_vaegir_spiked_helmet, itm_vaegir_lamellar_helmet,
    itm_hunter],
   def_lord_3_bal|level(4), wp_vaegir(wp_template_3), knows_lord_vaegir_3, 0, 0 ],
  ["vaegir_lord_template_4", "Count", "Count", tf_is_merchant, no_scene, reserved, fac_culture_2,
   [itm_scimitar_b, itm_bardiche, itm_long_bardiche,
    itm_lance, itm_throwing_spears, itm_strong_bow, itm_bodkin_arrows,
    itm_tab_shield_kite_c, itm_tab_shield_kite_cav_b,
    itm_mail_chausses, itm_mail_boots, itm_mail_mittens,
    itm_mail_hauberk_herald, itm_lamellar_vest_herald, itm_brigandine_red_herald,
    itm_vaegir_helmet, itm_vaegir_lamellar_helmet, itm_vaegir_noble_helmet,
    itm_hunter, itm_warhorse],
   def_lord_4_bal|level(4), wp_vaegir(wp_template_4), knows_lord_vaegir_4, 0, 0 ],
  ["vaegir_lord_template_5", "Duke", "Duke", tf_is_merchant, no_scene, reserved, fac_culture_2,
   [itm_scimitar_b, itm_bardiche, itm_long_bardiche,
    itm_lance, itm_throwing_spears, itm_war_bow, itm_strong_bow, itm_bodkin_arrows,
    itm_tab_shield_kite_d, itm_tab_shield_kite_cav_b,
    itm_iron_greaves, itm_mail_boots, itm_mail_mittens,
    itm_brigandine_red_herald, itm_lamellar_armor_herald, itm_banded_armor,
    itm_vaegir_helmet, itm_vaegir_war_helmet, itm_vaegir_noble_helmet,
    itm_warhorse],
   def_lord_5_bal|level(4), wp_vaegir(wp_template_5), knows_lord_vaegir_5, 0, 0 ],
  ["vaegir_lord_template_6", "Marshall", "Marshall", tf_is_merchant, no_scene, reserved, fac_culture_2,
   [itm_scimitar_b, itm_great_bardiche, itm_great_long_bardiche,
    itm_heavy_lance, itm_throwing_spears, itm_war_bow, itm_strong_bow, itm_bodkin_arrows,
    itm_tab_shield_kite_d, itm_tab_shield_kite_cav_b,
    itm_iron_greaves, itm_mail_mittens, itm_gauntlets,
    itm_lamellar_armor_herald, itm_banded_armor, itm_vaegir_elite_armor_herald,
    itm_vaegir_war_helmet, itm_vaegir_noble_helmet,
    itm_warhorse],
   def_lord_6_bal|level(4), wp_vaegir(wp_template_6), knows_lord_vaegir_6, 0, 0 ],
  ["vaegir_lord_template_7", "King", "King", tf_is_merchant, no_scene, reserved, fac_culture_2,
   [itm_scimitar_b, itm_great_bardiche,
    itm_heavy_lance, itm_throwing_spears, itm_war_bow, itm_strong_bow, itm_bodkin_arrows,
    itm_tab_shield_kite_cav_b,
    itm_iron_greaves, itm_gauntlets,
    itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_tabard, itm_vaegir_elite_armor_herald,
    itm_vaegir_war_helmet, itm_vaegir_mask,
    itm_warhorse],
   def_lord_7_bal|level(4), wp_vaegir(wp_template_7), knows_lord_vaegir_7, 0, 0 ],
  
  ["khergit_lord_template_0", "Chieftain", "Chieftain", tf_is_merchant, no_scene, reserved, fac_culture_3,
   [itm_sword_khergit_1,
    itm_light_lance, itm_javelin, itm_hunting_bow, itm_arrows_b,
    itm_tab_shield_small_round_a, itm_tab_shield_kite_a,
    itm_nomad_boots, itm_hide_boots, itm_leather_gloves,
    itm_leather_vest_herald, itm_steppe_armor_herald, itm_coarse_tunic_herald,
    itm_leather_steppe_cap_b, itm_steppe_cap,
    itm_steppe_horse],
   def_lord_0_agi|level(4), wp_khergit(wp_template_0), knows_lord_khergit_0, 0, 0 ],
  ["khergit_lord_template_1", "Chief", "Chief", tf_is_merchant, no_scene, reserved, fac_culture_3,
   [itm_sword_khergit_2, itm_winged_mace,
    itm_light_lance, itm_javelin, itm_short_bow, itm_barbed_arrows,
    itm_tab_shield_small_round_a, itm_tab_shield_kite_b,
    itm_leather_boots, itm_leather_gloves,
    itm_steppe_armor_herald, itm_leather_vest_herald,
    itm_leather_steppe_cap_b, itm_steppe_cap,
    itm_steppe_horse],
   def_lord_1_agi|level(4), wp_khergit(wp_template_1), knows_lord_khergit_1, 0, 0 ],
  ["khergit_lord_template_2", "War Chief", "War Chief", tf_is_merchant, no_scene, reserved, fac_culture_3,
   [itm_sword_khergit_2, itm_winged_mace, itm_hafted_blade_a,
    itm_light_lance, itm_javelin, itm_nomad_bow, itm_barbed_arrows,
    itm_tab_shield_small_round_b, itm_tab_shield_kite_b,
    itm_leather_boots, itm_leather_gloves,
    itm_tribal_warrior_outfit, itm_nomad_robe,
    itm_leather_steppe_cap_b, itm_khergit_war_helmet,
    itm_steppe_horse, itm_courser],
   def_lord_2_agi|level(4), wp_khergit(wp_template_2), knows_lord_khergit_2, 0, 0 ],
  ["khergit_lord_template_3", "War Lord", "War Lord", tf_is_merchant, no_scene, reserved, fac_culture_3,
   [itm_sword_khergit_3, itm_winged_mace, itm_hafted_blade_a,
    itm_lance, itm_javelin, itm_nomad_bow, itm_bodkin_arrows,
    itm_tab_shield_small_round_b, itm_tab_shield_kite_b,
    itm_leather_boots, itm_leather_gloves,
    itm_tribal_warrior_outfit, itm_nomad_robe, itm_lamellar_vest_herald,
    itm_leather_steppe_cap_b, itm_khergit_war_helmet,
    itm_steppe_horse, itm_courser, itm_hunter],
   def_lord_3_agi|level(4), wp_khergit(wp_template_3), knows_lord_khergit_3, 0, 0 ],
  ["khergit_lord_template_4", "Noyan", "Noyan", tf_is_merchant, no_scene, reserved, fac_culture_3,
   [itm_sword_khergit_3, itm_spiked_mace, itm_hafted_blade_a,
    itm_lance, itm_javelin, itm_khergit_bow, itm_bodkin_arrows,
    itm_tab_shield_small_round_c, itm_tab_shield_kite_c,
    itm_splinted_greaves, itm_leather_gloves,
    itm_lamellar_vest_herald,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet, itm_khergit_war_helmet,
    itm_courser, itm_hunter],
   def_lord_4_agi|level(4), wp_khergit(wp_template_4), knows_lord_khergit_4, 0, 0 ],
  ["khergit_lord_template_5", "Az Khan", "Az Khan", tf_is_merchant, no_scene, reserved, fac_culture_3,
   [itm_sword_khergit_4, itm_spiked_mace, itm_hafted_blade_b,
    itm_heavy_lance, itm_javelin, itm_khergit_bow, itm_khergit_arrows,
    itm_tab_shield_small_round_c, itm_tab_shield_kite_d,
    itm_splinted_greaves, itm_leather_gloves, itm_scale_gauntlets,
    itm_lamellar_armor_herald,
    itm_khergit_cavalry_helmet, itm_khergit_guard_helmet,
    itm_hunter, itm_warhorse_steppe],
   def_lord_5_agi|level(4), wp_khergit(wp_template_5), knows_lord_khergit_5, 0, 0 ],
  ["khergit_lord_template_6", "Il-Khan", "Il-Khan", tf_is_merchant, no_scene, reserved, fac_culture_3,
   [itm_sword_khergit_4, itm_spiked_mace, itm_hafted_blade_b,
    itm_heavy_lance, itm_javelin, itm_khergit_bow, itm_khergit_arrows,
    itm_tab_shield_small_round_c, itm_tab_shield_kite_d,
    itm_splinted_greaves, itm_scale_gauntlets,
    itm_lamellar_armor_herald,
    itm_khergit_guard_helmet,
    itm_warhorse_steppe],
   def_lord_6_agi|level(4), wp_khergit(wp_template_6), knows_lord_khergit_6, 0, 0 ],
  ["khergit_lord_template_7", "Khan", "Khan", tf_is_merchant, no_scene, reserved, fac_culture_3,
   [itm_sword_khergit_4, itm_spiked_mace, itm_hafted_blade_b,
    itm_heavy_lance, itm_javelin, itm_khergit_bow, itm_khergit_arrows,
    itm_tab_shield_small_round_c, itm_tab_shield_kite_d,
    itm_splinted_greaves, itm_lamellar_gauntlets,
    itm_khergit_elite_armor_herald,
    itm_khergit_guard_helmet,
    itm_warhorse_steppe],
   def_lord_7_agi|level(4), wp_khergit(wp_template_7), knows_lord_khergit_7, 0, 0 ],
  
  ["nord_lord_template_0", "Berserker", "Berserker", tf_is_merchant, no_scene, reserved, fac_culture_4,
   [itm_sword_viking_1, itm_sword_viking_1_long, itm_one_handed_battle_axe_a, itm_one_handed_battle_axe_a, itm_two_handed_axe, itm_long_axe,
    itm_light_throwing_axes,
    itm_tab_shield_round_b,
    itm_leather_boots, itm_nomad_boots, itm_hide_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_nordic_archer_helmet, itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet
    ],
   def_lord_0_bal|level(4), wp_nord(wp_template_0), knows_lord_nord_0, 0, 0 ],
  ["nord_lord_template_1", "Veteran", "Veteran", tf_is_merchant, no_scene, reserved, fac_culture_4,
   [itm_sword_viking_1, itm_sword_viking_1_long, itm_one_handed_battle_axe_a, itm_one_handed_battle_axe_a, itm_two_handed_axe, itm_long_axe,
    itm_light_throwing_axes, itm_hunting_bow2, itm_arrows_b, itm_hunting_crossbow, itm_bolts,
    itm_tab_shield_round_c,
    itm_leather_boots, itm_leather_gloves,
    itm_byrnie_herald,
    itm_nordic_veteran_archer_helmet, itm_nordic_footman_helmet, itm_nordic_fighter_helmet,
    itm_sumpter_horse],
   def_lord_1_bal|level(4), wp_nord(wp_template_1), knows_lord_nord_1, 0, 0 ],
  ["nord_lord_template_2", "Noble", "Noble", tf_is_merchant, no_scene, reserved, fac_culture_4,
   [itm_sword_viking_2, itm_sword_viking_2_small, itm_one_handed_war_axe_b, itm_one_handed_war_axe_b, itm_two_handed_battle_axe_2, itm_long_axe_b,
    itm_throwing_axes, itm_short_bow2, itm_arrows_b,  itm_hunting_crossbow, itm_bolts,
    itm_tab_shield_round_c,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_byrnie_herald, itm_mail_shirt_herald,
    itm_nordic_footman_helmet, itm_nordic_fighter_helmet, itm_nordic_helmet,
    itm_pack_horse],
   def_lord_2_bal|level(4), wp_nord(wp_template_2), knows_lord_nord_2, 0, 0 ],
  ["nord_lord_template_3", "Lesser Thane", "Lesser Thane", tf_is_merchant, no_scene, reserved, fac_culture_4,
   [itm_sword_viking_2, itm_sword_viking_2_small, itm_one_handed_war_axe_b, itm_one_handed_war_axe_b, itm_two_handed_battle_axe_2, itm_long_axe_b,
    itm_throwing_axes, itm_short_bow2, itm_barbed_arrows,  itm_hunting_crossbow, itm_bolts,
    itm_tab_shield_round_c,
    itm_mail_chausses, itm_mail_mittens,
    itm_byrnie_herald, itm_mail_shirt_herald, itm_mail_hauberk_herald,
    itm_nordic_fighter_helmet, itm_nordic_helmet,
    itm_hunter],
   def_lord_3_bal|level(4), wp_nord(wp_template_3), knows_lord_nord_3, 0, 0 ],
  ["nord_lord_template_4", "Thane", "Thane", tf_is_merchant, no_scene, reserved, fac_culture_4,
   [itm_sword_viking_3, itm_sword_viking_3_small, itm_sword_viking_3_long, itm_one_handed_battle_axe_b, itm_one_handed_battle_axe_c, itm_one_handed_battle_axe_b, itm_two_handed_battle_axe_2, itm_long_axe_b,
    itm_throwing_axes, itm_long_bow, itm_barbed_arrows, itm_light_crossbow, itm_steel_bolts,
    itm_tab_shield_round_d,
    itm_mail_boots, itm_mail_mittens,
    itm_mail_shirt_herald, itm_mail_hauberk_herald,
    itm_nordic_helmet, itm_nordic_huscarl_helmet,
    itm_hunter],
   def_lord_4_bal|level(4), wp_nord(wp_template_4), knows_lord_nord_4, 0, 0 ],
  ["nord_lord_template_5", "Jarl", "Jarl", tf_is_merchant, no_scene, reserved, fac_culture_4,
   [itm_sword_viking_3, itm_sword_viking_3_small, itm_sword_viking_3_long, itm_one_handed_battle_axe_b, itm_one_handed_battle_axe_c, itm_one_handed_battle_axe_b, itm_great_axe, itm_long_axe_c,
    itm_heavy_throwing_axes, itm_long_bow, itm_bodkin_arrows, itm_light_crossbow, itm_steel_bolts,
    itm_tab_shield_round_e,
    itm_mail_boots, itm_iron_greaves, itm_mail_mittens, itm_gauntlets,
    itm_banded_armor, itm_heraldic_mail_with_surcoat,
    itm_nordic_helmet, itm_nordic_huscarl_helmet, itm_nordic_warlord_helmet,
    itm_warhorse],
   def_lord_5_bal|level(4), wp_nord(wp_template_5), knows_lord_nord_5, 0, 0 ],
  ["nord_lord_template_6", "Marshall", "Marshall", tf_is_merchant, no_scene, reserved, fac_culture_4,
   [itm_sword_viking_3, itm_sword_viking_3_small, itm_sword_viking_3_long, itm_one_handed_battle_axe_b, itm_one_handed_battle_axe_c, itm_one_handed_battle_axe_b, itm_great_axe,
    itm_heavy_throwing_axes, itm_long_bow, itm_bodkin_arrows,
    itm_tab_shield_round_e,
    itm_iron_greaves, itm_gauntlets,
    itm_banded_armor, itm_cuir_bouilli_herald, itm_heraldic_mail_with_surcoat,
    itm_nordic_huscarl_helmet, itm_nordic_warlord_helmet,
    itm_warhorse],
   def_lord_6_bal|level(4), wp_nord(wp_template_6), knows_lord_nord_6, 0, 0 ],
  ["nord_lord_template_7", "King", "King", tf_is_merchant, no_scene, reserved, fac_culture_4,
   [itm_sword_viking_3, itm_sword_viking_3_long, itm_one_handed_battle_axe_c, itm_one_handed_battle_axe_b, itm_great_axe, itm_long_axe_c,
    itm_heavy_throwing_axes, itm_long_bow, itm_bodkin_arrows,
    itm_tab_shield_round_e,
    itm_iron_greaves, itm_gauntlets,
    itm_cuir_bouilli_herald, itm_heraldic_mail_with_tabard,
    itm_nordic_huscarl_helmet, itm_nordic_warlord_helmet,
    itm_warhorse],
   def_lord_7_bal|level(4), wp_nord(wp_template_7), knows_lord_nord_7, 0, 0 ],
  
  ["rhodok_lord_template_0", "Patrician", "Patrician", tf_is_merchant, no_scene, reserved, fac_culture_5,
   [itm_sword_medieval_a, itm_sword_medieval_a_long, itm_fighting_pick, itm_falchion, itm_spear,
    itm_hunting_crossbow, itm_bolts, itm_hunting_bow2, itm_arrows_b,
    itm_tab_shield_pavise_a,
    itm_hide_boots, itm_nomad_boots, itm_leather_gloves,
    itm_leather_armor_herald, itm_aketon_green_herald, itm_ragged_outfit,
    itm_footman_helmet, itm_helmet_with_neckguard, itm_padded_coif,
    itm_sumpter_horse],
   def_lord_0_str|level(4), wp_rhodok(wp_template_0), knows_lord_rhodok_0, 0, 0 ],
  ["rhodok_lord_template_1", "Burgher", "Burgher", tf_is_merchant, no_scene, reserved, fac_culture_5,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_fighting_pick, itm_maul, itm_war_spear,
    itm_hunting_crossbow, itm_bolts, itm_hunting_bow2, itm_arrows_b,
    itm_tab_shield_pavise_b,
    itm_leather_boots, itm_leather_gloves,
    itm_aketon_green_herald, itm_ragged_outfit,
    itm_footman_helmet, itm_helmet_with_neckguard, itm_mail_coif,
    itm_sumpter_horse],
   def_lord_1_str|level(4), wp_rhodok(wp_template_1), knows_lord_rhodok_1, 0, 0 ],
  ["rhodok_lord_template_2", "Elder", "Elder", tf_is_merchant, no_scene, reserved, fac_culture_5,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_military_cleaver_a, itm_military_sickle_a, itm_sledgehammer, itm_war_spear,
    itm_crossbow, itm_light_crossbow, itm_steel_bolts, itm_light_lance, itm_javelin, itm_hunting_bow2, itm_barbed_arrows,
    itm_tab_shield_pavise_b, itm_tab_shield_heater_cav_a,
    itm_leather_boots, itm_leather_gloves,
    itm_ragged_outfit, itm_byrnie_herald,
    itm_helmet_with_neckguard, itm_kettle_hat, itm_mail_coif,
    itm_pack_horse],
   def_lord_2_str|level(4), wp_rhodok(wp_template_2), knows_lord_rhodok_2, 0, 0 ],
  ["rhodok_lord_template_3", "Leader", "Leader", tf_is_merchant, no_scene, reserved, fac_culture_5,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_military_cleaver_a, itm_military_sickle_a, itm_sledgehammer, itm_war_spear, itm_pike, itm_glaive,
    itm_crossbow, itm_light_crossbow, itm_steel_bolts, itm_light_lance, itm_javelin, itm_hunting_bow2, itm_barbed_arrows,
    itm_tab_shield_pavise_b, itm_tab_shield_heater_cav_a,
    itm_mail_chausses, itm_leather_gloves,
    itm_byrnie_herald,
    itm_helmet_with_neckguard, itm_kettle_hat,
    itm_hunter],
   def_lord_3_str|level(4), wp_rhodok(wp_template_3), knows_lord_rhodok_3, 0, 0 ],
  ["rhodok_lord_template_4", "Gaffer", "Gaffer", tf_is_merchant, no_scene, reserved, fac_culture_5,
   [itm_military_cleaver_b, itm_military_pick, itm_warhammer, itm_pike, itm_glaive,
    itm_heavy_crossbow, itm_light_crossbow, itm_steel_bolts, itm_light_lance, itm_javelin, itm_short_bow2, itm_bodkin_arrows,
    itm_tab_shield_pavise_c, itm_tab_shield_heater_cav_b,
    itm_mail_chausses, itm_mail_boots, itm_mail_mittens,
    itm_byrnie_herald, itm_surcoat_over_mail_herald, itm_heraldic_mail_with_tunic,
    itm_guard_helmet, itm_bascinet_2, itm_bascinet_3,
    itm_hunter],
   def_lord_4_str|level(4), wp_rhodok(wp_template_4), knows_lord_rhodok_4, 0, 0 ],
  ["rhodok_lord_template_5", "Warden", "Warden", tf_is_merchant, no_scene, reserved, fac_culture_5,
   [itm_military_cleaver_b, itm_military_pick, itm_morningstar, itm_warhammer, itm_two_handed_cleaver, itm_glaive,
    itm_siege_crossbow, itm_light_crossbow, itm_steel_bolts, itm_lance, itm_javelin, itm_short_bow2, itm_bodkin_arrows,
    itm_tab_shield_pavise_c, itm_tab_shield_heater_cav_b,
    itm_iron_greaves, itm_mail_boots, itm_mail_mittens, itm_gauntlets,
    itm_scale_armor_herald, itm_coat_of_plates_herald, itm_heraldic_mail_with_surcoat,
    itm_guard_helmet, itm_bascinet_2, itm_bascinet_3, itm_full_helm_herald,
    itm_warhorse_b, itm_warhorse],
   def_lord_5_str|level(4), wp_rhodok(wp_template_5), knows_lord_rhodok_5, 0, 0 ],
  ["rhodok_lord_template_6", "Marshall", "Marshall", tf_is_merchant, no_scene, reserved, fac_culture_5,
   [itm_military_cleaver_b, itm_morningstar, itm_warhammer, itm_two_handed_cleaver,
    itm_siege_crossbow, itm_light_crossbow, itm_steel_bolts, itm_heavy_lance, itm_short_bow2, itm_bodkin_arrows,
    itm_tab_shield_heater_cav_b, itm_tab_shield_pavise_d,
    itm_iron_greaves, itm_gauntlets,
    itm_scale_armor_herald, itm_coat_of_plates_herald, itm_heraldic_mail_with_surcoat,
    itm_bascinet_2, itm_bascinet_3, itm_full_helm_herald,
    itm_warhorse_b, itm_warhorse],
   def_lord_6_str|level(4), wp_rhodok(wp_template_6), knows_lord_rhodok_6, 0, 0 ],
  ["rhodok_lord_template_7", "Governor", "Governor", tf_is_merchant, no_scene, reserved, fac_culture_5,
   [itm_military_cleaver_b, itm_morningstar, itm_warhammer, itm_two_handed_cleaver,
    itm_siege_crossbow, itm_light_crossbow, itm_steel_bolts, itm_heavy_lance, itm_short_bow2, itm_bodkin_arrows,
    itm_tab_shield_heater_cav_b,
    itm_iron_greaves, itm_gauntlets,
    itm_coat_of_plates_herald, itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_tabard,
    itm_bascinet_2, itm_bascinet_3, itm_full_helm_herald,
    itm_warhorse_b, itm_warhorse],
   def_lord_7_str|level(4), wp_rhodok(wp_template_7), knows_lord_rhodok_7, 0, 0 ],
   
  ["sarranid_lord_template_0", "Nobleman", "Nobleman", tf_is_merchant, no_scene, reserved, fac_culture_6,
   [itm_arabian_sword_a, itm_mace_2,
    itm_javelin,
    itm_tab_shield_tear_b, itm_tab_shield_small_round_a,
    itm_sarranid_boots_a, itm_sarranid_boots_b, itm_leather_gloves,
    itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b, itm_skirmisher_armor,
    itm_turban, itm_desert_turban,
    itm_arabian_horse_a],
   def_lord_0_agi|level(4), wp_sarranid(wp_template_0), knows_lord_sarranid_0, 0, 0 ],
  ["sarranid_lord_template_1", "Mamluke", "Mamluke", tf_is_merchant, no_scene, reserved, fac_culture_6,
   [itm_arabian_sword_b, itm_mace_3,
    itm_javelin, itm_hunting_bow2, itm_arrows_b, itm_light_lance,
    itm_tab_shield_tear_b, itm_tab_shield_small_round_a,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_archers_vest,
    itm_sarranid_warrior_cap, itm_desert_turban,
    itm_arabian_horse_a],
   def_lord_1_agi|level(4), wp_sarranid(wp_template_1), knows_lord_sarranid_1, 0, 0 ],
  ["sarranid_lord_template_2", "Noble", "Noble", tf_is_merchant, no_scene, reserved, fac_culture_6,
   [itm_arabian_sword_b, itm_mace_3, itm_sarranid_axe_a, itm_sarranid_two_handed_axe_a,
    itm_javelin, itm_short_bow2, itm_barbed_arrows, itm_light_lance, itm_crossbow, itm_bolts,
    itm_tab_shield_tear_b, itm_tab_shield_small_round_b,
    itm_sarranid_boots_b, itm_leather_gloves,
    itm_sarranid_cavalry_robe, itm_sarranid_leather_armor,
    itm_sarranid_warrior_cap, itm_sarranid_horseman_helmet,
    itm_arabian_horse_b],
   def_lord_2_agi|level(4), wp_sarranid(wp_template_2), knows_lord_sarranid_2, 0, 0 ],
  ["sarranid_lord_template_3", "Noble", "Noble", tf_is_merchant, no_scene, reserved, fac_culture_6,
   [itm_arabian_sword_b, itm_mace_3, itm_sarranid_axe_a, itm_sarranid_two_handed_axe_a,
    itm_javelin, itm_nomad_bow2, itm_bodkin_arrows, itm_lance, itm_crossbow, itm_bolts,
    itm_tab_shield_tear_b, itm_tab_shield_small_round_b,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_sarranid_cavalry_robe, itm_arabian_armor_b_herald,
    itm_sarranid_helmet1,
    itm_arabian_horse_b],
   def_lord_3_agi|level(4), wp_sarranid(wp_template_3), knows_lord_sarranid_3, 0, 0 ],
  ["sarranid_lord_template_4", "Emir", "Emir", tf_is_merchant, no_scene, reserved, fac_culture_6,
   [itm_sarranid_cavalry_sword, itm_mace_4, itm_sarranid_axe_b, itm_sarranid_two_handed_axe_b,
    itm_jarid, itm_nomad_bow2, itm_bodkin_arrows, itm_lance, itm_crossbow, itm_steel_bolts,
    itm_tab_shield_tear_d, itm_tab_shield_small_round_c,
    itm_sarranid_boots_c, itm_leather_gloves,
    itm_sarranid_mail_shirt,
    itm_sarranid_mail_coif, itm_sarranid_helmet1,
    itm_arabian_horse_b, itm_warhorse_sarranid],
   def_lord_4_agi|level(4), wp_sarranid(wp_template_4), knows_lord_sarranid_4, 0, 0 ],
  ["sarranid_lord_template_5", "Malik", "Malik", tf_is_merchant, no_scene, reserved, fac_culture_6,
   [itm_arabian_sword_d, itm_sarranid_cavalry_sword, itm_iron_mace, itm_two_handed_iron_mace, itm_sarranid_axe_b, itm_sarranid_two_handed_axe_b,
    itm_jarid, itm_strong_bow2, itm_bodkin_arrows, itm_heavy_lance, itm_heavy_crossbow, itm_steel_bolts,
    itm_tab_shield_tear_d, itm_tab_shield_small_round_c,
    itm_sarranid_boots_d, itm_mail_mittens,
    itm_mamluke_mail_herald, itm_sarranid_mail_shirt,
    itm_sarranid_veiled_helmet, itm_sarranid_mail_coif,
    itm_warhorse_sarranid],
   def_lord_5_agi|level(4), wp_sarranid(wp_template_5), knows_lord_sarranid_5, 0, 0 ],
  ["sarranid_lord_template_6", "Calif", "Calif", tf_is_merchant, no_scene, reserved, fac_culture_6,
   [itm_arabian_sword_d, itm_sarranid_cavalry_sword, itm_iron_mace, itm_two_handed_iron_mace, itm_sarranid_axe_b, itm_sarranid_two_handed_axe_b,
    itm_jarid, itm_strong_bow2, itm_bodkin_arrows, itm_heavy_lance, itm_heavy_crossbow, itm_steel_bolts,
    itm_tab_shield_small_round_c,
    itm_sarranid_boots_d, itm_scale_gauntlets,
    itm_mamluke_mail_herald, itm_sarranid_elite_armor_herald,
    itm_sarranid_veiled_helmet,
    itm_warhorse_sarranid],
   def_lord_6_agi|level(4), wp_sarranid(wp_template_6), knows_lord_sarranid_6, 0, 0 ],
  ["sarranid_lord_template_7", "Sultan", "Sultan", tf_is_merchant, no_scene, reserved, fac_culture_6,
   [itm_arabian_sword_d, itm_sarranid_cavalry_sword, itm_iron_mace, itm_two_handed_iron_mace, itm_sarranid_axe_b, itm_sarranid_two_handed_axe_b,
    itm_jarid, itm_strong_bow2, itm_bodkin_arrows, itm_heavy_lance, itm_heavy_crossbow, itm_steel_bolts,
    itm_tab_shield_small_round_c,
    itm_sarranid_boots_d, itm_scale_gauntlets,
    itm_mamluke_mail_herald, itm_sarranid_elite_armor_herald,
    itm_sarranid_veiled_helmet,
    itm_warhorse_sarranid],
   def_lord_7_agi|level(4), wp_sarranid(wp_template_7), knows_lord_sarranid_7, 0, 0 ],

  ["mercenary_lord_template_0", "Mercenary", "Mercenary", tf_is_merchant, no_scene, reserved, fac_culture_7,
   [itm_sword_medieval_a, itm_sword_medieval_a_long, itm_falchion, itm_fighting_pick, itm_mace_2, itm_spear,
    itm_hunting_crossbow, itm_hunting_bow, itm_bolts, itm_arrows_b,
    itm_tab_shield_pavise_a, itm_tab_shield_heater_a, itm_tab_shield_heater_cav_a,
    itm_leather_boots, itm_hide_boots, itm_ankle_boots, itm_leather_gloves,
    itm_leather_jerkin_herald, itm_coarse_tunic_herald, itm_tabard_herald,
    itm_footman_helmet,
    itm_saddle_horse],
   def_lord_0_bal|level(4), wp_swadian(wp_template_0), knows_lord_swadian_0, 0, 0],
  ["mercenary_lord_template_1", "Mercenary", "Mercenary", tf_is_merchant, no_scene, reserved, fac_culture_7,
   [itm_sword_medieval_b_small, itm_sword_medieval_b, itm_fighting_pick, itm_mace_3, itm_war_spear,
    itm_hunting_crossbow, itm_hunting_bow, itm_bolts, itm_barbed_arrows,
    itm_tab_shield_pavise_b, itm_tab_shield_heater_b, itm_tab_shield_heater_cav_a,
    itm_leather_boots, itm_leather_gloves,
    itm_leather_jerkin_herald,
    itm_footman_helmet,
    itm_saddle_horse],
   def_lord_1_bal|level(4), wp_swadian(wp_template_1), knows_lord_swadian_1, 0, 0],
  ["mercenary_lord_template_2", "Mercenary", "Mercenary", tf_is_merchant, no_scene, reserved, fac_culture_7,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_fighting_pick, itm_mace_3, itm_war_spear,
    itm_light_crossbow, itm_short_bow, itm_bolts, itm_barbed_arrows, itm_light_lance,
    itm_tab_shield_pavise_b, itm_tab_shield_heater_b, itm_tab_shield_heater_cav_a,
    itm_leather_boots, itm_mail_chausses, itm_leather_gloves,
    itm_byrnie_herald,
    itm_footman_helmet, itm_kettle_hat, itm_mail_coif,
    itm_pack_horse],
   def_lord_2_bal|level(4), wp_swadian(wp_template_2), knows_lord_swadian_2, 0, 0],
  ["mercenary_lord_template_3", "Mercenary", "Mercenary", tf_is_merchant, no_scene, reserved, fac_culture_7,
   [itm_sword_medieval_b_small, itm_sword_medieval_b, itm_military_pick, itm_mace_3, itm_war_spear,
    itm_light_crossbow, itm_short_bow, itm_bolts, itm_barbed_arrows, itm_light_lance, itm_javelin,
    itm_tab_shield_pavise_b, itm_tab_shield_heater_b, itm_tab_shield_heater_cav_a,
    itm_mail_chausses, itm_leather_gloves, itm_mail_mittens,
    itm_byrnie_herald,
    itm_kettle_hat,
    itm_pack_horse],
   def_lord_3_bal|level(4), wp_swadian(wp_template_3), knows_lord_swadian_3, 0, 0],
  ["mercenary_lord_template_4", "Mercenary", "Mercenary", tf_is_merchant, no_scene, reserved, fac_culture_7,
   [itm_sword_medieval_b, itm_sword_medieval_b_small, itm_military_sickle_a, itm_mace_4, itm_bastard_sword_a, itm_war_spear,
    itm_light_crossbow, itm_crossbow, itm_short_bow, itm_steel_bolts, itm_bodkin_arrows, itm_lance, itm_javelin,
    itm_tab_shield_pavise_c, itm_tab_shield_heater_c, itm_tab_shield_heater_cav_b,
    itm_mail_boots, itm_mail_mittens,
    itm_mail_hauberk_herald,
    itm_guard_helmet,
    itm_hunter],
   def_lord_4_bal|level(4), wp_swadian(wp_template_4), knows_lord_swadian_4, 0, 0],
  ["mercenary_lord_template_5", "Mercenary", "Mercenary", tf_is_merchant, no_scene, reserved, fac_culture_7,
   [itm_sword_medieval_b_small, itm_sword_medieval_b, itm_military_sickle_a, itm_mace_4, itm_bastard_sword_b, itm_war_spear,
    itm_light_crossbow, itm_heavy_crossbow, itm_long_bow2, itm_short_bow, itm_steel_bolts, itm_bodkin_arrows, itm_heavy_lance, itm_javelin,
    itm_tab_shield_pavise_c, itm_tab_shield_heater_d, itm_tab_shield_heater_cav_b,
    itm_iron_greaves, itm_gauntlets,
    itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_tabard,
    itm_guard_helmet,
    itm_hunter],
   def_lord_5_bal|level(4), wp_swadian(wp_template_5), knows_lord_swadian_5, 0, 0],
  ["mercenary_lord_template_6", "Mercenary", "Mercenary", tf_is_merchant, no_scene, reserved, fac_culture_7,
   [itm_bastard_sword_b, itm_morningstar, itm_sword_medieval_b_small, itm_sword_medieval_b, itm_mace_4,
    itm_light_crossbow, itm_heavy_crossbow, itm_long_bow2, itm_short_bow, itm_steel_bolts, itm_bodkin_arrows, itm_heavy_lance, itm_javelin,
    itm_tab_shield_pavise_d, itm_tab_shield_heater_d, itm_tab_shield_heater_cav_b,
    itm_iron_greaves, itm_gauntlets,
    itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_tabard,
    itm_guard_helmet,
    itm_warhorse],
   def_lord_6_bal|level(4), wp_swadian(wp_template_6), knows_lord_swadian_6, 0, 0],
  ["mercenary_lord_template_7", "Mercenary", "Mercenary", tf_is_merchant, no_scene, reserved, fac_culture_7,
   [itm_bastard_sword_b, itm_morningstar, itm_sword_medieval_b_small, itm_sword_medieval_b, itm_mace_4,
    itm_light_crossbow, itm_heavy_crossbow, itm_long_bow2, itm_short_bow, itm_steel_bolts, itm_bodkin_arrows, itm_heavy_lance, itm_javelin,
    itm_tab_shield_pavise_d, itm_tab_shield_heater_d, itm_tab_shield_heater_cav_a,
    itm_iron_greaves, itm_gauntlets,
    itm_heraldic_mail_with_surcoat, itm_heraldic_mail_with_tabard,
    itm_guard_helmet,
    itm_warhorse],
   def_lord_7_bal|level(4), wp_swadian(wp_template_7), knows_lord_swadian_7, 0, 0],

  # Vendors troops
  ["merchant_town_11_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_12_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_town_21_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_22_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_town_31_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_32_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_town_41_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_42_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_town_51_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_52_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_town_61_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_62_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
   
  ["merchant_town_131_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_171_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_231_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_251_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_331_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_341_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_431_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_451_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_531_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_541_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_611_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_631_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_1a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_1b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_1c_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_1d_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_1e_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_1f_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_1g_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_11a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_11b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_12a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_12b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_13a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_13b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_13c_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_14a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_14b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_15a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_15b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_15c_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_16a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_16b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_17a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_17b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_2a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_2b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_2c_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_2d_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_2e_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_2f_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_2g_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_21a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_21b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_22a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_22b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_23b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_23c_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_24a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_24b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_25b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_25c_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_25d_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_3a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_3b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_3c_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_3d_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_3e_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_3f_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_3g_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_31a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_32a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_33b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_33c_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_33d_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_34b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_35a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_36a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_36b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_4a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_4b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_4c_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_4d_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_4e_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_4f_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_4g_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_41a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_42a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_43b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_43c_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_43d_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_43e_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_44a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_44b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_44c_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_5a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_5b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_5c_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_5d_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_5e_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_5f_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_5g_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_51a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_51b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_52a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_52b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_53a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_55a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_55b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_6a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_6b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_6c_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_6d_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_6e_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_6f_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_6g_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_62a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_63a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_63b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_64a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_65a_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_65b_general", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  
  ["merchant_town_11_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_12_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_21_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_22_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_31_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_32_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_41_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_42_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_51_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_52_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_61_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_62_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
   
  ["merchant_town_131_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_171_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_231_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_251_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_331_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_341_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_431_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_451_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_531_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_541_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_611_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_631_weapons", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  
  ["merchant_town_11_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_12_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_21_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_22_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_31_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_32_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_41_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_42_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_51_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_52_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_61_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_62_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
   
  ["merchant_town_131_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_171_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_231_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_251_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_331_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_341_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_431_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_451_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_531_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_541_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_611_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_town_631_armors", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  
  ["merchant_castle_1a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_1b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_1c_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_1d_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_1e_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_1f_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_1g_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_11a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_11b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_12a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_12b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_13a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_13b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_13c_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_14a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_14b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_15a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_15b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_15c_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_16a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_16b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_17a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_17b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_2a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_2b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_2c_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_2d_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_2e_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_2f_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_2g_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_21a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_21b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_22a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_22b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_23b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_23c_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_24a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_24b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_25b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_25c_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_25d_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_3a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_3b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_3c_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_3d_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_3e_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_3f_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_3g_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_31a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_32a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_33b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_33c_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_33d_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_34b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_35a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_36a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_36b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_4a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_4b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_4c_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_4d_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_4e_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_4f_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_4g_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_41a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_42a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_43b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_43c_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_43d_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_43e_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_44a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_44b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_44c_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_5a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_5b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_5c_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_5d_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_5e_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_5f_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_5g_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_51a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_51b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_52a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_52b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_53a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_55a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_55b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_6a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_6b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_6c_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_6d_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_6e_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_6f_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_6g_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["merchant_castle_62a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_63a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_63b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_64a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_65a_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  ["merchant_castle_65b_smith", "Merchant", "Merchant", tf_hero|tf_is_merchant, no_scene, reserved, fac_commoners,
   [itm_linen_tunic, itm_wrapping_boots], def_attrib|level(4), wp(50), knows_merchant, 0, 0 ],
  
  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_commoners,[],def_attrib,0,knows_common,0 ],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data", 0, 0, 0, fac_faction_1, [], 0, 0, 0, 0, 0 ],
]





#########################
## Upgrade Definitions ##
#########################
#upgrade( from, to )
#upgrade2( from, to1, to2)
# upgrade(troops, "swadian_militia", "swadian_light_infantry")