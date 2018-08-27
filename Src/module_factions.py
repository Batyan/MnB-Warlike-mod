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

	("faction_8", "Mercenaries", 0, 0.9, [], []),
	
	# ("faction_8", "Faction 8", 0, 0.9, [], []),
	# ("faction_9", "Faction 9", 0, 0.9, [], []),
	# ("faction_10", "Faction 10", 0, 0.9, [], []),
	
	("kingdom_1", "Swadia", 0, 0.9, [("outlaws",-0.5),], [], 0x8f0000),
	("kingdom_2", "Vaegirs", 0, 0.9, [("outlaws",-0.5),], [], 0x008f00),
	("kingdom_3", "Khergit", 0, 0.9, [("outlaws",-0.5),], [], 0x8f008f),
	("kingdom_4", "Nords", 0, 0.9, [("outlaws",-0.5),], [], 0x008f8f),
	("kingdom_5", "Rhodoks", 0, 0.9, [("outlaws",-0.5),], [], 0x00008f),
	("kingdom_6", "Sarranid", 0, 0.9, [("outlaws",-0.5),], [], 0x928f00),
	
	("small_kingdom_11", "Tevarin", 0, 0.9, [("outlaws",-0.5),], [], 0xB04444), # Heavy Crossbow + Heavy Pikeman
	("small_kingdom_12", "Elberl", 0, 0.9, [("outlaws",-0.5),], [], 0xDD8888), # Guard + Levy Infantry + Heavy Infantry
	("small_kingdom_13", "Dhirim", 0, 0.9, [("outlaws",-0.5),], [], 0xff2700), # Heavy Lancer + Levy Spearman + Lancer + Light Horseman + Horseman + Heavy Bowman?
	("small_kingdom_14", "Gisim", 0, 0.9, [("outlaws",-0.5),], [], 0x660044), # Light Longbowman + Longbowman + Hunter
	("small_kingdom_15", "Ivenn", 0, 0.9, [("outlaws",-0.5),], [], 0xDD0055), # Scout + Light Spearman + Spearman
	("small_kingdom_16", "Tilbaut", 0, 0.9, [("outlaws",-0.5),], [], 0xBB5500), # Mounted Skirmisher + Levy Skirmisher
	("small_kingdom_17", "Uxkhal", 0, 0.9, [("outlaws",-0.5),], [], 0x511515), # Squire + Foot Knight
	
	("small_kingdom_21", "Slezhk", 0, 0.9, [("outlaws",-0.5),], [], 0x554400), # Royal Lancer + Heavy Lancer + Levy Axeman + Hussar + Heavy Hussar
	("small_kingdom_22", "Khudan", 0, 0.9, [("outlaws",-0.5),], [], 0x005500), # Scout + Club Levy + Horseman + Royal Horseman + Light Club Infantry + Club Infantry + Heavy Club Infantry
	("small_kingdom_23", "the Northern Taiga", 0, 0.9, [("outlaws",-0.5),], [], 0x558f55), # Pikeman + Heavy Pikeman + Footman + Heavy Footman + Warrior
	("small_kingdom_24", "Yruma", 0, 0.9, [("outlaws",-0.5),], [], 0x88dd88), # Light Skirmisher + Heavy Skirmisher + Champion + Royal Skirmisher
	("small_kingdom_25", "the Southern Taiga", 0, 0.9, [("outlaws",-0.5),], [], 0x885500), # Heavy Mounted Longbowman + Mounted Longbowman + Longbowman + Royal Longbowman
	
	("small_kingdom_31", "Eastern", 0, 0.9, [("outlaws",-0.5),], [], 0xbb88bb), # Champion + Noble Rider + Tribal Infantry? + Tribal Light Archer? + Tribal Archer?
	("small_kingdom_32", "Warriors of Sungetche", 0, 0.9, [("outlaws",-0.5),], [], 0x996699), # Light Skirmisher + Warrior + Heavy Skirmisher + Noble Skirmisher?
	("small_kingdom_33", "Narra", 0, 0.9, [("outlaws",-0.5),], [], 0x770044), # Light Horse Archer + Light Steppe Cavalry + Heavy Steppe Cavalry
	("small_kingdom_34", "Halmar", 0, 0.9, [("outlaws",-0.5),], [], 0x440077), # Heavy Lancer + Noble Cavalry + Noble Lancer
	("small_kingdom_35", "Uhhun", 0, 0.9, [("outlaws",-0.5),], [], 0x9966ff), # Clansman + Light Horseman + Heavy Horseman + Noble Horseman
	("small_kingdom_36", "Azugan", 0, 0.9, [("outlaws",-0.5),], [], 0x440044), # Heavy Archer + Blade-master + Heavy Infantry + Levy Infantry
	
	("small_kingdom_41", "Pirash", 0, 0.9, [("outlaws",-0.5),], [], 0x14FF8D), # Light Lancer + Mounted Bowman + Armoured Lancer + Heavy Mounted Bowman
	("small_kingdom_42", "Gundig", 0, 0.9, [("outlaws",-0.5),], [], 0x2f8558), # Heavy Longbowman + Light Longbowman + Light Infantry + Heavy Infantry
	("small_kingdom_43", "Wercheg", 0, 0.9, [("outlaws",-0.5),], [], 0xADE9FF), # Skirmisher + Heavy Skirmisher + Light Mounted Skirmisher + Mounted Skirmisher?
	("small_kingdom_44", "Aldelen", 0, 0.9, [("outlaws",-0.5),], [], 0x396C72), # Spearman + Heavy Spearman + Hunter + Crossbowman + Medium Spear Cavalry + Heavy Spear Cavalry
	("small_kingdom_45", "Rizi", 0, 0.9, [("outlaws",-0.5),], [], 0x006bab), # King's Guard + Bowman + Light Spear Cavalry + Spear Cavalry + Heavy Spear Cavalry
	
	("small_kingdom_51", "Highlanders", 0, 0.9, [("outlaws",-0.5),], [], 0x4F5868), # Hunter + Bowman + Heavy Bowman + Sergeant + Highlander
	("small_kingdom_52", "Bezan", 0, 0.9, [("outlaws",-0.5),], [], 0x00255e), # Heroic Horseman + Levy Pikeman + Heavy Horseman + Light Horseman? + Heroic Pikeman
	("small_kingdom_53", "Veluca", 0, 0.9, [("outlaws",-0.5),], [], 0x368afd), # Light Cavalry + Heavy Cavalry + Heroic Cavalry
	("small_kingdom_54", "Jamiche", 0, 0.9, [("outlaws",-0.5),], [], 0xBE9EFF), # Light Spearman + Light Skirmisher + Heavy Spearman + Mounted Crossbow + Heavy Mounted Crossbow + Heroic Mounted Crossbow + Levy Crossbow
	("small_kingdom_55", "Saren", 0, 0.9, [("outlaws",-0.5),], [], 0x6755db), # Mounted Crossbow + Heavy Lancer + Heroic Lancer + Scout + Levy Crossbow
	
	("small_kingdom_61", "Barriye", 0, 0.9, [("outlaws",-0.5),], [], 0x804303), # Light Crossbowman + Levy Horseman + Crossbowman + Noble Horseman?
	("small_kingdom_62", "Sharwa Keep", 0, 0.9, [("outlaws",-0.5),], [], 0xd87a17), # Heavy Archer + Noble Infantry + Levy Spearman + Spearman + Heavy Spearman + Noble Spearman
	("small_kingdom_63", "Sarrdak", 0, 0.9, [("outlaws",-0.5),], [], 0xFFA445), # Heavy Lancer + Cataphract + Levy Infantry + Footman + Warrior + Skirmisher + Sergeant
	("small_kingdom_64", "Uzgha", 0, 0.9, [("outlaws",-0.5),], [], 0x6f6a3e), # Light Horse Archer + Horse Archer + Heavy Horse Archer
	("small_kingdom_65", "Durquba", 0, 0.9, [("outlaws",-0.5),], [], 0x4d4400), # Mounted Skirmisher + Pikeman + Heavy Pikeman + Noble Skirmisher
	
	("kingdoms_end", "Kingdoms End", 0, 0.9, [], []),
	
	("culture_1", "Swadian Culture", 0, 0.9, [], []),
	("culture_2", "Vaegir Culture", 0, 0.9, [], []),
	("culture_3", "Khergit Culture", 0, 0.9, [], []),
	("culture_4", "Nordic Culture", 0, 0.9, [], []),
	("culture_5", "Rhodok Culture", 0, 0.9, [], []),
	("culture_6", "Sarranid Culture", 0, 0.9, [], []),

	("culture_7", "Mercenary Culture", 0, 0.9, [], []),
	
	("cultures_end", "Culture end", 0, 0.9, [("outlaws",-0.5),], []),
	
	("outlaws", "Outlaw", ff_always_hide_label|max_player_rating(-30), 0.9, [], []),
]