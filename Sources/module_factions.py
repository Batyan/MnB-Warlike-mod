from header_factions import *





factions = [
    
	###############
	## Hardcoded ##
	###############
    ("no_faction", "No Faction", 0, 0.9, [], []),
    ("commoners", "Commoners", 0, 0.9, [], []),
	
    ("player_faction", "Player Faction", 0, 0.9, [("outlaws",-0.5),], []),
	("faction_1", "Forest Bandits", 0, 0.9, [], []),
	("faction_2", "Bandits", 0, 0.9, [], []),
	("faction_3", "Mountain Bandits", 0, 0.9, [], []),
	("faction_4", "Sea Raiders", 0, 0.9, [], []),
	("faction_5", "Steppe Bandits", 0, 0.9, [], []),
	("faction_6", "Tundra Bandits", 0, 0.9, [], []),
	("faction_7", "Desert Bandits", 0, 0.9, [], []),
	
	# ("faction_8", "Faction 8", 0, 0.9, [], []),
	# ("faction_9", "Faction 9", 0, 0.9, [], []),
	# ("faction_10", "Faction 10", 0, 0.9, [], []),
	
	("kingdom_1", "Kingdom of Swadia", 0, 0.9, [("outlaws",-0.5),], [], 0x8f0000),
	("kingdom_2", "Kingdom of Vaegirs", 0, 0.9, [("outlaws",-0.5),], [], 0x008f00),
	("kingdom_3", "Khergit Khanate", 0, 0.9, [("outlaws",-0.5),], [], 0x8f008f),
	("kingdom_4", "Kingdom of Nords", 0, 0.9, [("outlaws",-0.5),], [], 0x008f8f),
	("kingdom_5", "Kingdom of Rhodoks", 0, 0.9, [("outlaws",-0.5),], [], 0x00008f),
	("kingdom_6", "Sarranid Sultanate", 0, 0.9, [("outlaws",-0.5),], [], 0x928f00),
	
	("small_kingdom_11", "County of Tevarin", 0, 0.9, [("outlaws",-0.5),], [], 0xB04444), # Heavy Crossbow + Heavy Pikeman
	("small_kingdom_12", "County of Elberl", 0, 0.9, [("outlaws",-0.5),], [], 0xDD8888), # Swordmaster
	("small_kingdom_13", "Duchy of Dhirim", 0, 0.9, [("outlaws",-0.5),], [], 0xFF5555), # Heavy Lancer + Levy Spearman
	("small_kingdom_14", "County of Gisim", 0, 0.9, [("outlaws",-0.5),], [], 0x660044), # Longbowman + Heavy Longbowman
	("small_kingdom_15", "Grand County of Ivenn", 0, 0.9, [("outlaws",-0.5),], [], 0xDD0055), # Scout + Light Spearman + Spearman
	("small_kingdom_16", "County of Tilbaut", 0, 0.9, [("outlaws",-0.5),], [], 0xBB5500), # Mounted Skirmisher + Levy Skirmisher
	("small_kingdom_17", "County of Uxkhal", 0, 0.9, [("outlaws",-0.5),], [], 0x550000), # Squire + Foot Knight
	
	("small_kingdom_21", "County of Slezhk", 0, 0.9, [("outlaws",-0.5),], [], 0x554400), # Royal Lancer + Heavy Lancer + Levy Axeman
	("small_kingdom_22", "County of Khudan", 0, 0.9, [("outlaws",-0.5),], [], 0x005500), # Scout + Club Levy + Horseman + Royal Cavalry
	("small_kingdom_23", "Duchy of the Northern Taiga", 0, 0.9, [("outlaws",-0.5),], [], 0x558f55), # Champion + Pikeman + Heavy Pikeman + Royal Longbowman + Longbowman
	("small_kingdom_24", "County of Yruma", 0, 0.9, [("outlaws",-0.5),], [], 0x88dd88), # Light Skirmisher + Heavy Skirmisher
	("small_kingdom_25", "Duchy of the Southern Taiga", 0, 0.9, [("outlaws",-0.5),], [], 0x885500), # Heavy Mounted Bowman
	
	("small_kingdom_31", "Eastern Tribes", 0, 0.9, [("outlaws",-0.5),], [], 0xbb88bb), # Champion
	("small_kingdom_32", "Warriors of Sungetche", 0, 0.9, [("outlaws",-0.5),], [], 0x996699), # Light Skirmisher + Warrior + Light Spearman + Heavy Spearman + Heavy Slirmisher
	("small_kingdom_33", "Narra Khanate", 0, 0.9, [("outlaws",-0.5),], [], 0x770044), # Scout + Light Steppe Cavalry + Heavy Steppe Cavalry
	("small_kingdom_34", "Halmar Khanate", 0, 0.9, [("outlaws",-0.5),], [], 0x440077), # Heavy Lancer + Noble Cavalry + Noble Lancer
	("small_kingdom_35", "Uhnun Tribes", 0, 0.9, [("outlaws",-0.5),], [], 0x9966ff), # Clansman + Noble Rider
	("small_kingdom_36", "Tribes of Azugan", 0, 0.9, [("outlaws",-0.5),], [], 0x440044), # Heavy Archer + Blade-master
	
	("small_kingdom_41", "Pirash Warriors", 0, 0.9, [("outlaws",-0.5),], [], 0x14FF8D), # Light Lancer + Mounted Bowman
	("small_kingdom_42", "Gundig Warriors", 0, 0.9, [("outlaws",-0.5),], [], 0x00E5FF), # Heavy Longbowman + Light Longbowman
	("small_kingdom_43", "Wercheg Raiders", 0, 0.9, [("outlaws",-0.5),], [], 0xADE9FF), # Skirmisher + Heavy Skirmisher
	("small_kingdom_44", "Aldelen Warriors", 0, 0.9, [("outlaws",-0.5),], [], 0x396C72), # Spearman + Heavy Spearman + Hunter + Crossbowman
	("small_kingdom_45", "Rizi Hold", 0, 0.9, [("outlaws",-0.5),], [], 0x00A793), # King's Guard + Bowman + Spear Cavalry + Heavy Spear Cavalry
	
	("small_kingdom_51", "Highlanders", 0, 0.9, [("outlaws",-0.5),], [], 0x4F5868), # Hunter + Bowman + Heavy Bowman + Sergeant
	("small_kingdom_52", "Bezan Community", 0, 0.9, [("outlaws",-0.5),], [], 0x267CFF), # Heroic Rider + Levy Pikeman
	("small_kingdom_53", "City of Veluca", 0, 0.9, [("outlaws",-0.5),], [], 0xA3B8FF), # Light Cavalry + Heavy Cavalry + Heroic Cavalry
	("small_kingdom_54", "City of Jamiche", 0, 0.9, [("outlaws",-0.5),], [], 0xBE9EFF), # Light Spearman + Light Skirmisher + Heavy Spearman
	("small_kingdom_55", "Saren Community", 0, 0.9, [("outlaws",-0.5),], [], 0x746BFF), # Mounted Crossbowman + Lancer + Heavy Lancer
	
	("small_kingdom_61", "Oasis of Barriye", 0, 0.9, [("outlaws",-0.5),], [], 0x804303), # Light Crossbowman + Levy Horseman
	("small_kingdom_62", "Defenders of Sharwa Keep", 0, 0.9, [("outlaws",-0.5),], [], 0xB38A5F), # Heavy Archer
	("small_kingdom_63", "Sarrdak Sultanate", 0, 0.9, [("outlaws",-0.5),], [], 0xFFA445), # Heavy Lancer + Cataphract
	("small_kingdom_64", "Tribes of Uzgha", 0, 0.9, [("outlaws",-0.5),], [], 0x968F57), # Light Horse Archer + Horse Archer + Heavy Horse Archer
	("small_kingdom_65", "Great Tribes of Durquba", 0, 0.9, [("outlaws",-0.5),], [], 0x7A6C00), # Mounted Skirmisher + Pikeman + Heavy Pikeman + Noble Skirmisher
	
	("kingdoms_end", "Kingdoms End", 0, 0.9, [], []),
	
	("culture_1", "Swadian Culture", 0, 0.9, [("outlaws",-0.5),], []),
	("culture_2", "Vaegir Culture", 0, 0.9, [("outlaws",-0.5),], []),
	("culture_3", "Khergit Culture", 0, 0.9, [("outlaws",-0.5),], []),
	("culture_4", "Nordic Culture", 0, 0.9, [("outlaws",-0.5),], []),
	("culture_5", "Rhodok Culture", 0, 0.9, [("outlaws",-0.5),], []),
	("culture_6", "Sarranid Culture", 0, 0.9, [("outlaws",-0.5),], []),
	
	("cultures_end", "Culture end", 0, 0.9, [("outlaws",-0.5),], []),
	
	("outlaws", "Outlaw", ff_always_hide_label|max_player_rating(-30), 0.9, [], []),
]
