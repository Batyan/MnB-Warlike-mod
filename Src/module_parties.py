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
pf_village = pf_is_static|pf_show_faction|pf_label_small



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

	("prisoners_party", "prisoners_party", pf_disabled, 0, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (0,0), []),
	
	("town_11","Praven", icon_town|pf_town, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-96, 26.4),[], 170),
	("town_12","Suno", icon_town|pf_town, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-46.7, 13.8),[], 80),
	
	("town_21","Reyvadin", icon_town|pf_town, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(48.44, 39.3),[], 170),
	("town_22","Curaw", icon_town|pf_town, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(59.0, 89.4),[], 70),
	
	("town_31","Tulga", icon_town|pf_town, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(135.5, -22),[], 170),
	("town_32","Ichamur", icon_town|pf_town, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(153.5, 9.7),[], 20),
	
	("town_41","Sargoth", icon_town|pf_town, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-17.6, 79.7),[], 170),
	("town_42","Thir", icon_town|pf_town, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-50.6, 81.1),[], 110),
	
	("town_51","Jelkala", icon_town|pf_town, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-74.6, -79.7),[], 170),
	("town_52","Yalen", icon_town|pf_town, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-133.8, -45.5),[], 90),
	
	("town_61","Shariz", icon_town|pf_town, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(15, -107),[], 170),
	("town_62","Qaiyut", icon_town|pf_town, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(54.7, -97.8),[], 170),
	
	("town_131","Dhirim", icon_town|pf_town, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(12.4, -5.2),[], 170),
	("town_171","Burglen", icon_town|pf_town, 0, pt_none, fac_small_kingdom_17,0,ai_bhvr_hold,0,(-19.8, 1.6),[], 170),
	
	("town_231","Rivacheg", icon_town|pf_town, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(102.7, 119),[], 170),
	("town_251","Uslum", icon_town|pf_town, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(127.2, 87.4),[], 170),
	
	("town_331","Narra", icon_town|pf_town, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(96.1, -36.1),[], 170),
	("town_341","Halmar", icon_town|pf_town, 0, pt_none, fac_small_kingdom_34,0,ai_bhvr_hold,0,(32.3, -54.6),[], 170),
	
	("town_431", "Wercherg", icon_town|pf_town, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(-3.4, 115.8),[], 170),
	("town_451", "Rizi", icon_town|pf_town, 0, pt_none, fac_small_kingdom_45,0,ai_bhvr_hold,0,(-73.4, 100.4),[], 170),
	
	("town_531","Veluca", icon_town|pf_town, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-54.6, -45),[], 170),
	("town_541","Jamiche", icon_town|pf_town, 0, pt_none, fac_small_kingdom_54,0,ai_bhvr_hold,0,(-15.7, -83.3),[], 170),
	
	("town_611","Barriye", icon_town|pf_town, 0, pt_none, fac_small_kingdom_61,0,ai_bhvr_hold,0,(164.1, -109.4),[], 170),
	("town_631","Ahmerrad", icon_town|pf_town, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(123.7, -98.7),[], 170),

	("castle_1a","Yaragar Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-63, -8.2),[], 170),
	("castle_1b","Lendil Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-42.4, -9.7),[], 170),
	("castle_1c","Ryibelet Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-75.2, 47.8),[], 170),
	("castle_1d","Veigar Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-109.8, 16.9),[], 170),
	("castle_1e","Rindyar Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-69.5, 5.7),[], 170),
	("castle_1f","Reidan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-29.5, 27.3),[], 170),
	("castle_1g","Vyilberl Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-70.3, 23.7),[], 170),
	
	("castle_11a","Tevarin Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_11,0,ai_bhvr_hold,0,(-129.6, 36.7),[], 170),
	("castle_11b","Vyigan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_11,0,ai_bhvr_hold,0,(-115.4, 39.7),[], 170),
	("castle_12a","Elberl Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_12,0,ai_bhvr_hold,0,(-142.3, 27.7),[], 170),
	("castle_12b","Byistar Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_12,0,ai_bhvr_hold,0,(-135.7, 9.6),[], 170),
	("castle_13b","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(55.0, -4.6),[], 170),
	("castle_13c","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(4.4, -22.1),[], 170),
	("castle_13d","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(25.8, -25),[], 170),
	("castle_14a","Kalvan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_14,0,ai_bhvr_hold,0,(-85, 57.8),[], 170),
	("castle_14b","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_14,0,ai_bhvr_hold,0,(-100.9, 63.2),[], 170),
	("castle_15a","Haringoth Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_15,0,ai_bhvr_hold,0,(-116.5, -2),[], 170),
	("castle_15b","Vyincourd Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_15,0,ai_bhvr_hold,0,(-81.5, -5.5),[], 170),
	("castle_15c","Vyincan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_15,0,ai_bhvr_hold,0,(-100.9, 6.3),[], 170),
	("castle_16a","Tilbaut Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_16,0,ai_bhvr_hold,0,(40.6, 13.4),[], 170),
	("castle_16b","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_16,0,ai_bhvr_hold,0,(16.1, 26.9),[], 170),
	("castle_17a","Tshibtin Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_17,0,ai_bhvr_hold,0,(-20.4, -15),[], 170),
	("castle_17b","Kelredan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_17,0,ai_bhvr_hold,0,(-10.3, 19.1),[], 170),
	
	("castle_2a","Ismirag Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(40.3, 68.5),[], 170),
	("castle_2b","Jeirbe Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(38.6, 85.3),[], 170),
	("castle_2c","Dramug Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(61.9, 19.9),[], 170),
	("castle_2d","Nelag Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(85.2, 77.9),[], 170),
	("castle_2e","Bulugha Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(74.7, 104.2),[], 170),
	("castle_2f","Seimag Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(62.1, 111.4),[], 170),
	("castle_2g","Brameg Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(33.9, 40.8),[], 170),
	
	("castle_21a","Slezkh Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_21,0,ai_bhvr_hold,0,(67.4, 60.2),[], 170),
	("castle_21b","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_21,0,ai_bhvr_hold,0,(55.2, 76.3),[], 170),
	("castle_22a","Khudan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_22,0,ai_bhvr_hold,0,(95.8, 65.5),[], 170),
	("castle_22b","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_22,0,ai_bhvr_hold,0,(109.1, 84),[], 170),
	("castle_23b","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(96.1, 94),[], 170),
	("castle_23c","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(122.9, 118.7),[], 170),
	("castle_24a","Yruma Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_24,0,ai_bhvr_hold,0,(77, 42.3),[], 170),
	("castle_24b","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_24,0,ai_bhvr_hold,0,(90.9, 48.9),[], 170),
	("castle_25b","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(118.5, 64),[], 170),
	("castle_25c","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(123.2, 102.9),[], 170),
	("castle_25d","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(137.5, 70.5),[], 170),
	
	("castle_3a","Malayurg Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(116.1, -18),[], 170),
	("castle_3b","Dugan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(94.8, -1),[], 170),
	("castle_3c","Tulbuk Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(147.8, 50.8),[], 170),
	("castle_3d","Unuzdaq Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(131, 16.4),[], 170),
	("castle_3e","Distar Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(144.1, -5.5),[], 170),
	("castle_3f","Dalagan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(121.5, 2.3),[], 170),
	("castle_3g","Sunduk Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(152.8, -36.5),[], 170),
	
	("castle_31a","Buhdke Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_31,0,ai_bhvr_hold,0,(164.9, -10.4),[], 170),
	("castle_32a","Sungetche Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_32,0,ai_bhvr_hold,0,(110.3, 40.5),[], 170),
	("castle_33b","Shalgan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(77.3, -50.5),[], 170),
	("castle_33c","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(71.8, -12.7),[], 170),
	("castle_33d","Dichebe Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(77.7, 7.5),[], 170),
	("castle_34b","Vanush Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_34,0,ai_bhvr_hold,0,(21.6, -39.8),[], 170),
	("castle_35a","Uhhun Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_35,0,ai_bhvr_hold,0,(62.1, -24.8),[], 170),
	("castle_35b","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_35,0,ai_bhvr_hold,0,(43.5, -35.5),[], 170),
	("castle_36a","Asugan Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_36,0,ai_bhvr_hold,0,(175.9, -48.3),[], 170),
	("castle_36b","Dungedke Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_36,0,ai_bhvr_hold,0,(170.8, -31.8),[], 170),
	
	("castle_4a","Jelbegi Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-47.7, 48.5),[], 170),
	("castle_4b","Tehlrog Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(10.2, 43.5),[], 170),
	("castle_4c","Knudarr Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-15.5, 46.2),[], 170),
	("castle_4d","Curin Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-31.8, 76),[], 170),
	("castle_4e","Hrus Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-71.5, 83.1),[], 170),
	("castle_4d","Horbek Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-3.5, 63),[], 170),
	("castle_4e","Camdarr Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-42.7, 66.5),[], 170),
	
	("castle_41a","Ismirala Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_41,0,ai_bhvr_hold,0,(12.2, 76.2),[], 170),
	("castle_41b","New Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_41,0,ai_bhvr_hold,0,(22.0, 60.0),[], 170),
	("castle_42a","Raeth Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_42,0,ai_bhvr_hold,0,(-9.9, 33.9),[], 170),
	("castle_43b","Gamarr Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(-33.1, 113.2),[], 170),
	("castle_43c","Albruq Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(21.5, 91.2),[], 170),
	("castle_43d","Curth Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(18.9, 110.4),[], 170),
	("castle_43e","Uelek Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(39.4, 110.3),[], 170),
	("castle_44a","Kulum Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_44,0,ai_bhvr_hold,0,(-118.8, 109.5),[], 170),
	("castle_44b","Aldelen Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_44,0,ai_bhvr_hold,0,(-108.9, 92.7),[], 170),
	("castle_44c","Rozgoth Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_44,0,ai_bhvr_hold,0,(-94.3, 80.3),[], 170),
	("castle_45b","Chalbek Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_45,0,ai_bhvr_hold,0,(-94.1, 114.4),[], 170),
	
	("castle_5a","Estroq Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-109.4, -43.1),[], 170),
	("castle_5b","Malken Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-70.1, -61.5),[], 170),
	("castle_5c","Culmar Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-49, -92),[], 170),
	("castle_5d","Maras Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-122.7, -18.4),[], 170),
	("castle_5e","Ibdeles Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-88.6, -96.3),[], 170),
	("castle_5f","Jarindi Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-86.9, -50.8),[], 170),
	("castle_5g","Gibdas Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-107.6, -61.7),[], 170),
	
	("castle_51a","Vera Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_51,0,ai_bhvr_hold,0,(-101.1, -19.4),[], 170),
	("castle_51b","Ereth Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_51,0,ai_bhvr_hold,0,(-83.0, -33.8),[], 170),
	("castle_52a","Almera Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_52,0,ai_bhvr_hold,0,(-157.5, -12.4),[], 170),
	("castle_52b","Malaka Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_52,0,ai_bhvr_hold,0,(-162.0, -32.4),[], 170),
	("castle_53a","Ergellon Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-50.3, -23.9),[], 170),
	("castle_54a","Udbas Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_54,0,ai_bhvr_hold,0,(-9.6, -66.1),[], 170),
	("castle_55a","Grunwalder Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_55,0,ai_bhvr_hold,0,(-22.2, -40.0),[], 170),
	("castle_55b","Saren Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_55,0,ai_bhvr_hold,0,(3.3, -45.4),[], 170),
	
	("castle_6a","Teramma Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(86.2, -93),[], 170),
	("castle_6b","Weyyah Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(10.3, -76.8),[], 170),
	("castle_6c","Caraf Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(33.1, -104.6),[], 170),
	("castle_6d","Jameyyed Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(70.8, -71.4),[], 170),
	("castle_6e","Dhibbain Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(72.8, -110.6),[], 170),
	("castle_6f","Qameyyah Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(3.1, -91.5),[], 170),
	("castle_6g","Hashaq Castle", icon_castle_a|pf_castle, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(55.5, -56.9),[], 170),
	
	("castle_62a","Sharwa Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_62,0,ai_bhvr_hold,0,(168.4, -63.5),[], 170),
	("castle_63a","Bardaq Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(159.8, -86.7),[], 170),
	("castle_63b","Durin Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(115.5, -70.4),[], 170),
	("castle_63c","Sayn Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(101.1, -111.4),[], 170),
	("castle_64a","Samarra Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_64,0,ai_bhvr_hold,0,(139.1, -75.3),[], 170),
	("castle_65a","Habba Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_65,0,ai_bhvr_hold,0,(98.0, -78.3),[], 170),
	("castle_65b","Druquba Castle", icon_castle_a|pf_castle, 0, pt_none, fac_small_kingdom_65,0,ai_bhvr_hold,0,(104.8, -90.2),[], 170),
	
	("village_111","Lyindha", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-92, 14),[], 170),
	("village_112","Veidar", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-107, 30),[], 170),
	("village_113","Azgad", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-84, 33),[], 170),
	
	("village_121","Talhberl", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-37.6, 12.5),[], 170),
	("village_122","Ruluns", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-54.8, 23.5),[], 170),
	("village_123","Ibiran", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-57.1, 13.5),[], 170),
	
	("village_1a1","Uxkhal", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-57, -12.2),[], 170),
	("village_1b1","Lendil", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-46.4, -3.5),[], 170),
	("village_1c1","Ryibelet", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-70.5, 40.1),[], 170),
	("village_1d1","Veigar", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-119.6, 19.5),[], 170),
	("village_1e1","Ryindyar", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-73.6, 12.2),[], 170),
	("village_1f1","New Village", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-37.5, 30.7),[], 170),
	("village_1g1","New Village", icon_village_a|pf_village, 0, pt_none, fac_kingdom_1,0,ai_bhvr_hold,0,(-75.7, 25.3),[], 170),
	
	("village_11a1","Balanli", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_11,0,ai_bhvr_hold,0,(-131.1, 42.9),[], 170),
	("village_11b1","Vyigan", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_11,0,ai_bhvr_hold,0,(-118.8, 32.7),[], 170),
	
	("village_12a1","Elberl", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_12,0,ai_bhvr_hold,0,(-147.4, 22.2),[], 170),
	("village_12b1","Istyia", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_12,0,ai_bhvr_hold,0,(-142, 11.5),[], 170),
	
	("village_13a1","Tosdar", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(3.4, -10.1),[], 170),
	("village_13a2","Emirin", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(11.1, 4.7),[], 170),
	("village_13a3","Yalibe", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(20.4, -7.8),[], 170),
	("village_13a4","Ushkuru", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(30.5, 0.3),[], 170),
	("village_13b1","Ehlerdah", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(45.7, -7.9),[], 170),
	("village_13c1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(-4.1, -24.7),[], 170),
	("village_13d1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_13,0,ai_bhvr_hold,0,(28.7, -16.3),[], 170),
	
	("village_14a1","Gisim", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_14,0,ai_bhvr_hold,0,(-90, 53),[], 170),
	("village_14b1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_14,0,ai_bhvr_hold,0,(-101.9, 55),[], 170),
	
	("village_15a1","Nemeja", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_15,0,ai_bhvr_hold,0,(-122.2, 3.4),[], 170),
	("village_15b1","Nadalb", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_15,0,ai_bhvr_hold,0,(-87.9, -3),[], 170),
	("village_15c1","Vyincan", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_15,0,ai_bhvr_hold,0,(-99.5, -0.3),[], 170),
	
	("village_16a1","Tadsamesh", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_16,0,ai_bhvr_hold,0,(29.7, 19.1),[], 170),
	("village_16b1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_16,0,ai_bhvr_hold,0,(15.2, 16.8),[], 170),
	
	("village_17a1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_17,0,ai_bhvr_hold,0,(-10.4, -0.9),[], 170),
	("village_17a2","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_17,0,ai_bhvr_hold,0,(-22.5, 9.2),[], 170),
	("village_17a3","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_17,0,ai_bhvr_hold,0,(-27.5, -5.4),[], 170),
	("village_17b1","Nomar", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_17,0,ai_bhvr_hold,0,(-22, -22),[], 170),
	("village_17c1","Chide", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_17,0,ai_bhvr_hold,0,(-8.5, 13.8),[], 170),
	
	("village_211","Ayyike", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(46, 31),[], 170),
	("village_212","Ulburban", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(60, 42),[], 170),
	("village_213","Rduna", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(45, 52),[], 170),
	
	("village_221","Rebache", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(49.8, 92.2),[], 170),
	("village_222","Bazeck", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(72.3, 82.5),[], 170),
	("village_223","Ruvar", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(63.6, 97.1),[], 170),
	
	("village_2a1","Pizkh", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(46.4, 65.2),[], 170),
	("village_2b1","Mazen", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(32, 80),[], 170),
	("village_2c1","Tebandra", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(70.9, 22.1),[], 170),
	("village_2d1","Hanun", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(84.1, 72.7),[], 170),
	("village_2e1","Udiniand", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(78.1, 99.4),[], 170),
	("village_2f1","New Village", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(68.2, 115.6),[], 170),
	("village_2g1","New Village", icon_village_a|pf_village, 0, pt_none, fac_kingdom_2,0,ai_bhvr_hold,0,(34.3, 33.9),[], 170),
	
	("village_21a1","Slezkh", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_21,0,ai_bhvr_hold,0,(60.2, 59),[], 170),
	("village_21b1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_21,0,ai_bhvr_hold,0,(63.1, 77),[], 170),
	
	("village_22a1","Khudan", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_22,0,ai_bhvr_hold,0,(100.7, 68.6),[], 170),
	("village_22b1","Tismirr", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_22,0,ai_bhvr_hold,0,(108.1, 77.8),[], 170),
	
	("village_23a1","Vezin", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(97.8, 127.3),[], 170),
	("village_23a2","Fisdnar", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(96.3, 111.2),[], 170),
	("village_23a3","Shapeshte", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(85.6, 115.7),[], 170),
	("village_23a4","Milishe", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(109.2, 112.1),[], 170),
	("village_23b1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(94.3, 100.3),[], 170),
	("village_23c1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_23,0,ai_bhvr_hold,0,(123.1, 125.9),[], 170),
	
	("village_24a1","Karindi", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_24,0,ai_bhvr_hold,0,(82.3, 35.8),[], 170),
	("village_24b1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_24,0,ai_bhvr_hold,0,(82.5, 56),[], 170),
	
	("village_25a1","Shulus", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(122.4, 88.4),[], 170),
	("village_25a2","Tridina", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(138.4, 103.6),[], 170),
	("village_25a3","Dimishte", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(152.8, 91.4),[], 170),
	("village_25b1","Shizike", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(127.9, 54.5),[], 170),
	("village_25c1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(127.2, 107.1),[], 170),
	("village_25d1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_25,0,ai_bhvr_hold,0,(139.3, 77),[], 170),

	("village_311","Dusturil", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(127, -25),[], 170),
	("village_312","Dashbigha", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(134, -33),[], 170),
	("village_313","Dash Kulun", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(144, -23),[], 170),
	
	("village_321","Dirigh Aban", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(162.5, 6.6),[], 170),
	("village_322","Ada Kulun", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(152.6, 23.9),[], 170),
	("village_323","Amalke", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(166.5, 23.3),[], 170),
	
	("village_3a1","Tash Kulun", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(119.8, -12.6),[], 170),
	("village_3b1","Dugan", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(98.4, -7.2),[], 170),
	("village_3c1","Tulbuk", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(138.7, 38),[], 170),
	("village_3d1","Amashke", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(137.2, 17),[], 170),
	("village_3e1","Bulugur", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(138, -3.8),[], 170),
	("village_3f1","New Village", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(112.4, 9.3),[], 170),
	("village_3g1","New Village", icon_village_a|pf_village, 0, pt_none, fac_kingdom_3,0,ai_bhvr_hold,0,(145.8, -41.6),[], 170),
	
	("village_31a1","Buhdke", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_31,0,ai_bhvr_hold,0,(172.1, -7.6),[], 170),
	
	("village_32a1","Bhulaban", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_32,0,ai_bhvr_hold,0,(119.4, 36.9),[], 170),
	
	("village_33a1","Kedelke", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(91.6, -46.3),[], 170),
	("village_33a2","Zagnush", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(86.1, -22.4),[], 170),
	("village_33a3","Zadke Kulun", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(103.3, -30),[], 170),
	("village_33b1","Shalgan", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(84.2, -54.1),[], 170),
	("village_33c1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(77.7, -11),[], 170),
	("village_33d1","Dichebe", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_33,0,ai_bhvr_hold,0,(88.6, 11.4),[], 170),
	
	("village_34a1","Peshmi", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_34,0,ai_bhvr_hold,0,(15.6, -59.0),[], 170),
	("village_34a2","Hun Aban", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_34,0,ai_bhvr_hold,0,(31.3, -77.2),[], 170),
	("village_34a3","Duhke", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_34,0,ai_bhvr_hold,0,(34.5, -63.1),[], 170),
	("village_34b1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_34,0,ai_bhvr_hold,0,(32.4, -42.6),[], 170),
	
	("village_35a1","Uhhun", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_35,0,ai_bhvr_hold,0,(71.8, -28.7),[], 170),
	("village_35b1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_35,0,ai_bhvr_hold,0,(49.0, -23.6),[], 170),
	
	("village_36a1","Asugan", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_36,0,ai_bhvr_hold,0,(178.2, -43.7),[], 170),
	("village_36b1","An Ashuk", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_36,0,ai_bhvr_hold,0,(164.9, -30.7),[], 170),
	
	("village_411","Fearichen", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-21, 57),[], 170),
	("village_412","Fenada", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-10, 76),[], 170),
	("village_413","Javig", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-22.1, 71.5),[], 170),
	
	("village_421","Haen", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-55.1, 64.3),[], 170),
	("village_422","Jelewynn", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-39.6, 82.6),[], 170),
	("village_423","Acheleg", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-68, 69.2),[], 170),
	
	("village_4a1","Jelbegi", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-50, 55),[], 170),
	("village_4b1","Vayejeg", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(4.1, 49.4),[], 170),
	("village_4c1","Mechin", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-11.4, 54),[], 170),
	("village_4d1","Kwynn", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-29, 81.4),[], 170),
	("village_4e1","Hrus", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-65.2, 84.5),[], 170),
	("village_4f1","Ambean", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-7, 59),[], 170),
	("village_4g1","Kadariq", icon_village_a|pf_village, 0, pt_none, fac_kingdom_4,0,ai_bhvr_hold,0,(-42.3, 71.7),[], 170),
	
	("village_41a1","Ismirala", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_41,0,ai_bhvr_hold,0,(5.5, 78.9),[], 170),
	("village_41b1","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_41,0,ai_bhvr_hold,0,(12.7, 57.7),[], 170),

	("village_42a1","Raeth", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_42,0,ai_bhvr_hold,0,(-0.3, 34.3),[], 170),
	
	("village_43a1","Jayek", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(-0.5, 107.9),[], 170),
	("village_43a2","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(-17, 123.6),[], 170),
	("village_43a3","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(-0.2, 120.2),[], 170),
	("village_43a4","New Village", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(-14.8, 113.9),[], 170),
	("village_43b1","Odasan", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(-39.2, 111.2),[], 170),
	("village_43c1","Albruq", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(22.6, 98.6),[], 170),
	("village_43d1","Kurs", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(18.2, 117.5),[], 170),
	("village_43e1","Uelek", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_43,0,ai_bhvr_hold,0,(35.3, 117.3),[], 170),
	
	("village_44a1","Kulum", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_44,0,ai_bhvr_hold,0,(-124.3, 103.2),[], 170),
	("village_44b1","Aldelen", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_44,0,ai_bhvr_hold,0,(-103, 95.4),[], 170),
	("village_44c1","Vindisen", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_44,0,ai_bhvr_hold,0,(-104.4, 80.2),[], 170),
	
	("village_45a1","Fryja", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_45,0,ai_bhvr_hold,0,(-71.2, 93.4),[], 170),
	("village_45a2","Kaelek", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_45,0,ai_bhvr_hold,0,(-79.4, 111.1),[], 170),
	("village_45a3","Jebe", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_45,0,ai_bhvr_hold,0,(-81.6, 97.8),[], 170),
	
	("village_45b1","Buillin", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_45,0,ai_bhvr_hold,0,(-99.8, 109.2),[], 170),
	
	("village_511","Buvran", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-86, -74),[], 170),
	("village_512","Ruldi", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-68, -94),[], 170),
	("village_513","Chelez", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-60, -74),[], 170),
	
	("village_521","Ilvya", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-131.6, -53.3),[], 170),
	("village_522","Istiniar", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-139.8, -41),[], 170),
	("village_523","Epeshe", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-128.3, -32.4),[], 170),
	
	("village_5a1","Dumar", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-112.9, -34.5),[], 170),
	("village_5b1","Fedner", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-64.8, -64.8),[], 170),
	("village_5c1","Dirigsene", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-53.4, -100.9),[], 170),
	("village_5d1","Reveran", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-119.9, -26.4),[], 170),
	("village_5e1","Ibdeles", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-84, -102),[], 170),
	("village_5f1","Eseldi", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-95.1, -47-6),[], 170),
	("village_5g1","Jales", icon_village_a|pf_village, 0, pt_none, fac_kingdom_5,0,ai_bhvr_hold,0,(-106.3, -65.8),[], 170),
	
	("village_51a1","Vera", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_51,0,ai_bhvr_hold,0,(-96.8, -28.5),[], 170),
	("village_51b1","Cheshe", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_51,0,ai_bhvr_hold,0,(-84.2, -24.1),[], 170),
	
	("village_52a1","Glunmar", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_52,0,ai_bhvr_hold,0,(-147.8, -16),[], 170),
	("village_52b1","Runar", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_52,0,ai_bhvr_hold,0,(-155.1, -36.2),[], 170),
	
	("village_53a1","Emer", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-50.6, -53.9),[], 170),
	("village_53a2","Chaeza", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-67.2, -42.8),[], 170),
	("village_53a3","Sarimish", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-44.2, -38.1),[], 170),
	("village_53a4","Shimar", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-39.9, -50.7),[], 170),
	("village_53b1","Pagundur", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_53,0,ai_bhvr_hold,0,(-45.4, -25.5),[], 170),
	
	("village_54a1","Haevran", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_54,0,ai_bhvr_hold,0,(-24.9, -85.6),[], 170),
	("village_54a2","Idza", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_54,0,ai_bhvr_hold,0,(-25.2, -70),[], 170),
	("village_54a3","Emeshadi", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_54,0,ai_bhvr_hold,0,(-9.5, -78.7),[], 170),
	("village_54b1","Udbas", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_54,0,ai_bhvr_hold,0,(-3.9, -59.6),[], 170),
	
	("village_55a1","Serindiar", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_55,0,ai_bhvr_hold,0,(-19, -50.7),[], 170),
	("village_55b1","Saren", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_55,0,ai_bhvr_hold,0,(-1.1, -37.5),[], 170),
	
	("village_611","Ayn Asuadi", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(8, -112),[], 170),
	("village_612","Rushdigh", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(15.8, -91.7),[], 170),
	("village_613","Tilimsal", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(25, -114),[], 170),
	
	("village_621","Sekhtem", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(51, -88.5),[], 170),
	("village_622","Tamnuh", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(55.2, -112.2),[], 170),
	("village_623","Amiyag", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(64.5, -87.6),[], 170),
	
	("village_6a1","Shibal Zumr", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(84.5, -98.4),[], 170),
	("village_6b1","Hawaha", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(3.3, -78.8),[], 170),
	("village_6c1","Mit Nun", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(38, -97.5),[], 170),
	("village_6d1","Mazigh", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(66.3, -75.2),[], 170),
	("village_6e1","Dhibbain", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(69.5, -116.1),[], 170),
	("village_6f1","Qameyyah", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(6, -97.7),[], 170),
	("village_6g1","Hash Kulun", icon_village_a|pf_village, 0, pt_none, fac_kingdom_6,0,ai_bhvr_hold,0,(55.9, -67.7),[], 170),
	
	("village_61a1","Fishara", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_61,0,ai_bhvr_hold,0,(156.8, -106.1),[], 170),
	("village_61a2","Iqbayl", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_61,0,ai_bhvr_hold,0,(150.8, -112.8),[], 170),
	("village_61a3","Shqayet", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_61,0,ai_bhvr_hold,0,(165.7, -119.8),[], 170),
	
	("village_62a1","Tazjunat", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_62,0,ai_bhvr_hold,0,(162.0, -60.7),[], 170),
	
	("village_63a1","Mijayet", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(117.3, -97.6),[], 170),
	("village_63a2","Mawiti", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(124.7, -115.2),[], 170),
	("village_63a3","Abl Nun", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(133.4, -91.7),[], 170),
	("village_63b1","Unriya", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(156.5, -83.9),[], 170),
	("village_63c1","Aab", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(115.4, -63.0),[], 170),
	("village_63d1","Sayn", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_63,0,ai_bhvr_hold,0,(94.1, -118.3),[], 170),
	
	("village_64a1","Uzgha", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_64,0,ai_bhvr_hold,0,(138.6, -69.0),[], 170),
	
	("village_65a1","Habba", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_65,0,ai_bhvr_hold,0,(97.6, -71.7),[], 170),
	("village_65b1","Urq Ann", icon_village_a|pf_village, 0, pt_none, fac_small_kingdom_65,0,ai_bhvr_hold,0,(101.5, -91.9),[], 170),
	
	("centers_end", "END", pf_disabled, 0, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (0, 0), []),
	
	# Exploration
	# ("places_stone_obelisk", "Stone Obelisk", icon_training_ground|pf_is_static|pf_hide_defenders, 0, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (15.6, -43.7), []),
	# ("places_grand_tree", "Grand Tree", icon_training_ground, 0, pt_none, fac_commoners, 0, ai_bhvr_hold, 0, (0, 0), []),
	
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
