from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *





#################
## Definitions ##
#################
pt_none = 0
no_menu = 0

pf_town = pf_is_static|pf_show_faction|pf_label_large
# pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_label_small



#############
## Parties ##
#############
parties = [
    
	###############
	## Hardcoded ##
	###############
    ("main_party","Main Party",icon_player|pf_limit_members, 0, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17, 52.5),[(trp_player,1,0)]),
    ("temp_party","{!}temp_party",pf_disabled, 0, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
    ("camp_bandits","{!}camp_bandits",pf_disabled, 0, pt_none, fac_commoners,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),

	###########
	## Other ##
	###########
	# Autocalc battles
	("collective_defender", "collective_defender", pf_disabled, 0, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (0, 0), []),
	("collective_attacker", "collective_attacker", pf_disabled, 0, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (0, 0), []),
	
	("temp_casualties", "temp_casualties", pf_disabled, 0, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (0, 0), []),
	
	("player_casualties", "player_casualties", pf_disabled, 0, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (0, 0), []),
	("ally_casualties", "ally_casualties", pf_disabled, 0, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (0, 0), []),
	("enemy_casualties", "enemy_casualties", pf_disabled, 0, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (0, 0), []),
	
	("resources_party", "Resources Party", icon_player|pf_disabled, 0, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (0, 0), []),
	
	("town_11","Praven", icon_town|pf_town, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-96, 26.4),[], 170),
	("town_12","Suno", icon_town|pf_town, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-41.8, 11.8),[], 80),
	
	("town_21","Reyvadin", icon_town|pf_town, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(48.44, 39.3),[], 170),
	("town_22","Curaw", icon_town|pf_town, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(60.6, 85.5),[], 70),
	
	("town_31","Tulga", icon_town|pf_town, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(135.5, -22),[], 170),
	("town_32","Ichamur", icon_town|pf_town, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(153.5, 9.7),[], 20),
	
	("town_41","Sargoth", icon_town|pf_town, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-17.6, 79.7),[], 170),
	("town_42","Thir", icon_town|pf_town, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-50.6, 81.1),[], 110),
	
	("town_51","Jelkala", icon_town|pf_town, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-74.6, -79.7),[], 170),
	("town_52","Yalen", icon_town|pf_town, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-133.8, -45.5),[], 90),
	
	("town_61","Shariz", icon_town|pf_town, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(15, -107),[], 170),
	("town_62","Qaiyut", icon_town|pf_town, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(54.7, -97.8),[], 170),
	
	("town_131","Dhirim", icon_town|pf_town, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(12.4, -5.2),[], 170),
	
	("town_231","Rivacheg", icon_town|pf_town, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(103.8, 117),[], 170),
	("town_251","Uslum", icon_town|pf_town, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(127.2, 87.4),[], 170),
	
	("town_331","Narra", icon_town|pf_town, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(96.1, -36.1),[], 170),
	("town_341","Halmar", icon_town|pf_town, 0, pt_none, fac_small_kingdom_34,0,ai_bhvr_hold,0,(29.4, -46.2),[], 170),
	
	("town_451", "Rizi", icon_town|pf_town, 0, pt_none, fac_small_kingdom_45,0,ai_bhvr_hold,0,(-73.4, 100.4),[], 170),
	
	("town_531","Veluca", icon_town|pf_town, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-54.6, -45),[], 170),
	("town_541","Jamiche", icon_town|pf_town, 0, pt_none, fac_small_kingdom_54,0,ai_bhvr_hold,0,(-15.7, -83.3),[], 170),
	
	("town_611","Barriye", icon_town|pf_town, 0, pt_none, fac_small_kingdom_61,0,ai_bhvr_hold,0,(164.1, -109.4),[], 170),
	("town_631","Ahmerrad", icon_town|pf_town, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(123.7, -98.7),[], 170),
	
	("castle_1a","Tshibtin Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-20.4, -15),[], 170),
	("castle_1b","Kelredan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-10.3, 19.1),[], 170),
	("castle_1c","Ryibelet Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-75.2, 47.8),[], 170),
	("castle_1d","Veigar Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-109.8, 16.9),[], 170),
	("castle_1e","Rindyar Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-69.5, 5.7),[], 170),
	
	("castle_11a","Tevarin Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_11,0,ai_bhvr_hold,0,(-129.6, 36.7),[], 170),
	("castle_12a","Elberl Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_12,0,ai_bhvr_hold,0,(-136.8, 20.2),[], 170),
	("castle_14a","Kalvan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_14,0,ai_bhvr_hold,0,(-93, 60.6),[], 170),
	("castle_15a","Haringoth Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_15,0,ai_bhvr_hold,0,(-118.1, 2.8),[], 170),
	("castle_15b","Vyincourd Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_15,0,ai_bhvr_hold,0,(-81.5, -5.5),[], 170),
	("castle_16b","Tilbaut Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_16,0,ai_bhvr_hold,0,(23.7, 22.9),[], 170),
	("castle_17a","Yaragar Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_17,0,ai_bhvr_hold,0,(-63, -8.2),[], 170),
	
	("castle_2a","Ismirag Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(40.3, 68.5),[], 170),
	("castle_2b","Jeirbe Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(38.6, 85.3),[], 170),
	("castle_2c","Dramug Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(60.4, 16.9),[], 170),
	("castle_2d","Nelag Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(85.2, 77.9),[], 170),
	("castle_2e","Bulugha Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(74.7, 104.2),[], 170),
	
	("castle_21a","Slezkh Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_21,0,ai_bhvr_hold,0,(64.6, 60.8),[], 170),
	("castle_22a","Khudan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_22,0,ai_bhvr_hold,0,(95.8, 65.5),[], 170),
	("castle_24a","Yruma Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_24,0,ai_bhvr_hold,0,(80.9, 45.4),[], 170),
	
	("castle_3a","Malayurg Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(107.9, -15.5),[], 170),
	("castle_3b","Dugan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(170.9, -32),[], 170),
	("castle_3c","Tulbuk Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(147.8, 50.8),[], 170),
	("castle_3d","Unuzdaq Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(131, 16.4),[], 170),
	("castle_3e","Distar Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(144.1, -5.5),[], 170),
	
	("castle_31a","Buhdke Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_31,0,ai_bhvr_hold,0,(164.9, -10.4),[], 170),
	("castle_32a","Sungetche Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_32,0,ai_bhvr_hold,0,(110.3, 40.5),[], 170),
	("castle_35a","Uhhun Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_35,0,ai_bhvr_hold,0,(62.1, -24.8),[], 170),
	("castle_36a","Asugan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_36,0,ai_bhvr_hold,0,(175.9, -48.3),[], 170),
	
	("castle_4a","Jelbegi Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-46.6, 50.8),[], 170),
	("castle_4b","Tehlrog Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(18.3, 56.3),[], 170),
	("castle_4c","Knudarr Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-11.6, 46.8),[], 170),
	("castle_4d","Curin Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-31.8, 76),[], 170),
	("castle_4e","Hrus Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-71.5, 83.1),[], 170),
	
	("castle_41a","Ismirala Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_41,0,ai_bhvr_hold,0,(12.2, 76.2),[], 170),
	("castle_42a","Chalbek Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_42,0,ai_bhvr_hold,0,(-94.1, 114.4),[], 170),
	("castle_43a","Wercherg Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(-3.4, 115.8),[], 170),
	("castle_43b","Gamarr Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(-33.1, 113.2),[], 170),
	("castle_44a","Kulum Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_44,0,ai_bhvr_hold,0,(-118.8, 109.5),[], 170),
	("castle_44b","Aldelen Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_44,0,ai_bhvr_hold,0,(-99.4, 89.1),[], 170),
	
	("castle_5a","Estroq Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-109.4, -43.1),[], 170),
	("castle_5b","Motprezzar Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-70.1, -61.5),[], 170),
	("castle_5c","Culmar Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-49, -92),[], 170),
	("castle_5d","Maras Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-122.7, -18.4),[], 170),
	("castle_5e","Ibdeles Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-88.6, -96.3),[], 170),
	
	("castle_51a","Buerry Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_51,0,ai_bhvr_hold,0,(-98.3, -24.7),[], 170),
	("castle_52a","Almera Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_52,0,ai_bhvr_hold,0,(-157.8, -19.7),[], 170),
	("castle_53a","Ergellon Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-50.3, -23.9),[], 170),
	("castle_55a","Grunwalder Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_55,0,ai_bhvr_hold,0,(-16.7, -43.7),[], 170),
	("castle_55b","Saren Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_55,0,ai_bhvr_hold,0,(0.1, -49.7),[], 170),
	
	("castle_6a","Teramma Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(86.2, -93),[], 170),
	("castle_6b","Weyyah Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(10.3, -76.8),[], 170),
	("castle_6c","Caraf Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(33.1, -104.6),[], 170),
	("castle_6d","Jameyyed Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(70.8, -71.4),[], 170),
	("castle_6e","Dhibbain Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(72.8, -110.6),[], 170),
	
	("castle_62a","Sharwa Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_62,0,ai_bhvr_hold,0,(168.4, -63.5),[], 170),
	("castle_63b","Bardaq Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(159.8, -86.7),[], 170),
	("castle_63c","Durin Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(115.5, -70.4),[], 170),
	("castle_64a","Samarra Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_64,0,ai_bhvr_hold,0,(139.1, -75.3),[], 170),
	("castle_65a","Habba Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_65,0,ai_bhvr_hold,0,(98.0, -78.3),[], 170),
	("castle_65b","Druquba Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_65,0,ai_bhvr_hold,0,(104.8, -90.2),[], 170),
	
	("castle_bandit_4_1","Albruq Castle", icon_castle_a|pf_castle, 0, pt_none, fac_faction_4,0,ai_bhvr_hold,0,(22.5, 97.2),[], 170),
	
	("village_111","Village111", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-92, 14),[], 170),
	("village_112","Village112", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-107, 30),[], 170),
	("village_113","Village113", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-84, 33),[], 170),
	
	("village_121","Village121", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-31.7, 10),[], 170),
	("village_122","Village122", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-54.8, 23.5),[], 170),
	("village_123","Village123", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-57.1, 13.5),[], 170),
	
	("village_1a1","Village1a1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-22, -22),[], 170),
	("village_1b1","Village1b1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-8.5, 13.8),[], 170),
	("village_1c1","Village1c1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-70.5, 40.1),[], 170),
	("village_1d1","Village1d1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-114.8, 18.5),[], 170),
	("village_1e1","Village1e1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-73.6, 12.2),[], 170),
	
	("village_11a1","Village11a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_11,0,ai_bhvr_hold,0,(-131.1, 42.9),[], 170),
	("village_12a1","Village12a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_12,0,ai_bhvr_hold,0,(-145.2, 16.9),[], 170),
	("village_14a1","Gisim", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_14,0,ai_bhvr_hold,0,(-93.6, 54.1),[], 170),
	("village_15a1","Village15a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_15,0,ai_bhvr_hold,0,(-127.5, 1.9),[], 170),
	("village_15b1","Village15b1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_15,0,ai_bhvr_hold,0,(-87.9, -3),[], 170),
	("village_16b1","Village16b1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_16,0,ai_bhvr_hold,0,(19.6, 28.4),[], 170),
	("village_17a1","Village17a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_17,0,ai_bhvr_hold,0,(-57, -12.2),[], 170),
	
	("village_13a1","Village13a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(3.4, -10.1),[], 170),
	("village_13a2","Village13a2", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(11.1, 4.7),[], 170),
	("village_13a3","Village13a3", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(28.8, -15.2),[], 170),
	("village_13a4","Village13a4", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(30.5, 0.3),[], 170),
	
	("village_211","Village211", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(46, 31),[], 170),
	("village_212","Village212", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(60, 42),[], 170),
	("village_213","Village213", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(45, 52),[], 170),
	
	("village_221","Village221", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(52.4, 81.3),[], 170),
	("village_222","Village222", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(72.3, 82.5),[], 170),
	("village_223","Village223", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(63.6, 97.1),[], 170),
	
	("village_2a1","Village2a1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(46.4, 65.2),[], 170),
	("village_2b1","Village2b1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(32, 80),[], 170),
	("village_2c1","Village2c1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(67.7, 20.3),[], 170),
	("village_2d1","Village2d1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(84.1, 72.7),[], 170),
	("village_2e1","Village2e1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(78.1, 99.4),[], 170),
	
	("village_21a1","Village21a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_21,0,ai_bhvr_hold,0,(60.2, 59),[], 170),
	("village_22a1","Village22a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_22,0,ai_bhvr_hold,0,(100.7, 68.6),[], 170),
	("village_24a1","Village24a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_24,0,ai_bhvr_hold,0,(82.3, 35.8),[], 170),
	
	("village_23a1","Village23a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(97.8, 127.3),[], 170),
	("village_23a2","Village23a2", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(96.3, 111.2),[], 170),
	("village_23a3","Village23a3", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(85.6, 115.7),[], 170),
	("village_23a4","Village23a4", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(113.9, 109.3),[], 170),
	
	("village_25a1","Village25a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(116.7, 84),[], 170),
	("village_25a2","Village25a2", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(138.4, 103.6),[], 170),
	("village_25a3","Village25a3", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(136.4, 70.8),[], 170),
	
	("village_311","Village311", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(127, -25),[], 170),
	("village_312","Village312", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(134, -33),[], 170),
	("village_313","Village313", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(144, -23),[], 170),
	
	("village_321","Village321", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(162.5, 6.6),[], 170),
	("village_322","Village322", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(152.6, 23.9),[], 170),
	("village_323","Village323", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(166.5, 23.3),[], 170),
	
	("village_3a1","Village3a1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(108.4, -8.1),[], 170),
	("village_3b1","Village3b1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(164.7, -31.4),[], 170),
	("village_3c1","Village3c1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(138.7, 38),[], 170),
	("village_3d1","Village3d1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(137.2, 17),[], 170),
	("village_3e1","Village3e1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(138, -3.8),[], 170),
	
	("village_31a1","Village31a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_31,0,ai_bhvr_hold,0,(172.1, -7.6),[], 170),
	("village_32a1","Village32a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_32,0,ai_bhvr_hold,0,(119.4, 36.9),[], 170),
	("village_35a1","Village35a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_35,0,ai_bhvr_hold,0,(71.8, -28.7),[], 170),
	("village_36a1","Village36a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_36,0,ai_bhvr_hold,0,(178.2, -43.7),[], 170),
	
	("village_33a1","Village33a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(91.6, -46.3),[], 170),
	("village_33a2","Village33a2", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(86.1, -22.4),[], 170),
	("village_33a3","Village33a3", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(103.3, -30),[], 170),
	
	("village_34a1","Village34a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_34,0,ai_bhvr_hold,0,(42.8, -37.8),[], 170),
	("village_34a2","Village34a2", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_34,0,ai_bhvr_hold,0,(21, -58.9),[], 170),
	("village_34a3","Village34a3", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_34,0,ai_bhvr_hold,0,(37.4, -59.3),[], 170),
	
	("village_411","Village411", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-21, 57),[], 170),
	("village_412","Village412", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-10, 76),[], 170),
	("village_413","Village413", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-7, 59),[], 170),
	
	("village_421","Village421", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-55.1, 64.3),[], 170),
	("village_422","Village422", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-39.6, 82.6),[], 170),
	("village_423","Village423", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-68, 69.2),[], 170),
	
	("village_4a1","Village4a1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-50, 55),[], 170),
	("village_4b1","Village4b1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(12.2, 57.8),[], 170),
	("village_4c1","Village4c1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-11.4, 54),[], 170),
	("village_4d1","Village4d1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-29, 81.4),[], 170),
	("village_4e1","Village4e1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-65.2, 84.5),[], 170),
	
	("village_41a1","Village41a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_41,0,ai_bhvr_hold,0,(5.5, 78.9),[], 170),
	("village_42a1","Village42a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_42,0,ai_bhvr_hold,0,(-99.8, 109.2),[], 170),
	("village_43a1","Village43a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(-0.5, 107.9),[], 170),
	("village_43b1","Village43b1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(-39.2, 111.2),[], 170),
	("village_44a1","Village44a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_44,0,ai_bhvr_hold,0,(-124.3, 103.2),[], 170),
	("village_44b1","Village44b1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_44,0,ai_bhvr_hold,0,(-105.5, 90),[], 170),
	
	("village_45a1","Village45a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_45,0,ai_bhvr_hold,0,(-71.2, 93.4),[], 170),
	("village_45a2","Village45a2", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_45,0,ai_bhvr_hold,0,(-79.4, 111.1),[], 170),
	("village_45a3","Village45a3", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_45,0,ai_bhvr_hold,0,(-81.6, 97.8),[], 170),
	
	("village_511","Village511", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-86, -74),[], 170),
	("village_512","Village512", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-68, -94),[], 170),
	("village_513","Village513", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-60, -74),[], 170),
	
	("village_521","Village521", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-131.6, -53.3),[], 170),
	("village_522","Village522", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-139.8, -41),[], 170),
	("village_523","Village523", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-128.3, -32.4),[], 170),
	
	("village_5a1","Village5a1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-112.9, -34.5),[], 170),
	("village_5b1","Village5b1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-64.8, -64.8),[], 170),
	("village_5c1","Village5c1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-53.4, -100.9),[], 170),
	("village_5d1","Village5d1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-119.9, -26.4),[], 170),
	("village_5e1","Village5e1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-84, -102),[], 170),
	
	("village_51a1","Village51a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_51,0,ai_bhvr_hold,0,(-96.8, -28.5),[], 170),
	("village_52a1","Village52a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_52,0,ai_bhvr_hold,0,(-147.8, -16),[], 170),
	("village_53b1","Village53b1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-45.4, -25.5),[], 170),
	("village_55a1","Village55a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_55,0,ai_bhvr_hold,0,(-19, -50.7),[], 170),
	("village_55b1","Village55b1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_55,0,ai_bhvr_hold,0,(-1.9, -55.1),[], 170),
	
	("village_53a1","Village53a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-50.6, -53.9),[], 170),
	("village_53a2","Village53a2", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-67.2, -42.8),[], 170),
	("village_53a3","Village53a3", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-44.2, -38.1),[], 170),
	("village_53a4","Village53a4", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-39.9, -50.7),[], 170),
	
	("village_54a1","Village54a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_54,0,ai_bhvr_hold,0,(-24.9, -85.6),[], 170),
	("village_54a2","Village54a2", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_54,0,ai_bhvr_hold,0,(-25.2, -70),[], 170),
	("village_54a3","Village54a3", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_54,0,ai_bhvr_hold,0,(-9.5, -78.7),[], 170),
	
	("village_611","Village611", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(8, -112),[], 170),
	("village_612","Village612", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(14, -96),[], 170),
	("village_613","Village613", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(25, -114),[], 170),
	
	("village_621","Village621", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(51, -88.5),[], 170),
	("village_622","Village622", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(55.2, -112.2),[], 170),
	("village_623","Village623", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(64.5, -87.6),[], 170),
	
	("village_6a1","Village6a1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(84.5, -98.4),[], 170),
	("village_6b1","Village6b1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(3.3, -78.8),[], 170),
	("village_6c1","Village6c1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(38, -97.5),[], 170),
	("village_6d1","Village6d1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(66.3, -75.2),[], 170),
	("village_6e1","Village6e1", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(69.5, -116.1),[], 170),
	
	("village_61a1","Village61a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_61,0,ai_bhvr_hold,0,(156.8, -106.1),[], 170),
	("village_61a2","Village61a2", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_61,0,ai_bhvr_hold,0,(150.8, -112.8),[], 170),
	("village_61a3","Village61a3", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_61,0,ai_bhvr_hold,0,(165.7, -119.8),[], 170),
	
	("village_62a1","Village62a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_62,0,ai_bhvr_hold,0,(162.0, -60.7),[], 170),
	
	("village_63a1","Village62a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(117.3, -97.6),[], 170),
	("village_63a2","Village62a2", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(124.7, -115.2),[], 170),
	("village_63a3","Village62a3", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(133.4, -91.7),[], 170),
	
	("village_63b1","Village62b1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(156.5, -83.9),[], 170),
	("village_63c1","Village62c1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(115.4, -63.0),[], 170),
	
	("village_64a1","Village64a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_64,0,ai_bhvr_hold,0,(138.6, -69.0),[], 170),
	
	("village_65a1","Village65a1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_65,0,ai_bhvr_hold,0,(97.6, -71.7),[], 170),
	("village_65b1","Village65b1", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_65,0,ai_bhvr_hold,0,(101.5, -91.9),[], 170),
	
	("village_bandit_4_1","VillageBandit41", icon_village_a|pf_village, 0, pt_none, fac_faction_4,0,ai_bhvr_hold,0,(23.8, 103.9),[], 170),
	
	("centers_end", "END", pf_disabled, 0, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (0, 0), []),
	
	
	# Bridges
	("Bridge_1","{!}1",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(39.37, 65.10),[], -44.8),
	("Bridge_2","{!}2",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(56.44, 77.88),[], 4.28),
	("Bridge_3","{!}3",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(70.87, 87.95),[], 64.5),
	("Bridge_4","{!}4",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(93.71, 62.13),[], -2.13),
	("Bridge_5","{!}5",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(11.02, 72.61),[], 21.5),
	("Bridge_6","{!}6",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(-8.83, 52.24),[], -73.5),
	("Bridge_7","{!}7",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(-29.79, 76.84),[], -64),
	("Bridge_8","{!}8",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(-64.05, -6),[], 1.72),
	("Bridge_9","{!}9",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(-64.95, -9.60),[], -33.76),
	("Bridge_10","{!}10",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(-75.32, -75.27),[], -44.07),
	("Bridge_11","{!}11",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(-24.39, 67.82),[], 81.3),
	("Bridge_12","{!}12",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(-114.33, -1.94),[], -35.5),
	("Bridge_13","{!}13",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(-84.02, -7),[], -17.7),
	("Bridge_14","{!}14",icon_bridge_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_no_faction,0,ai_bhvr_hold,0,(-23.36, 75.8),[], 66.6),

]
