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
	("small_kingdom_13", "Dhirim", 0, 0.9, [("outlaws",-0.5),], [], 0x644330), # Heavy Lancer + Levy Spearman + Lancer + Light Horseman + Horseman + Heavy Bowman?
	("small_kingdom_14", "Gisim", 0, 0.9, [("outlaws",-0.5),], [], 0xD35DB2), # Light Longbowman + Longbowman + Hunter
	("small_kingdom_15", "Ivenn", 0, 0.9, [("outlaws",-0.5),], [], 0xDD0055), # Scout + Light Spearman + Spearman + Levy Spearman + Foot Knight
	("small_kingdom_16", "Tilbaut", 0, 0.9, [("outlaws",-0.5),], [], 0xBB5500), # Mounted Skirmisher + Levy Skirmisher
	("small_kingdom_17", "Burglen", 0, 0.9, [("outlaws",-0.5),], [], 0x8a3656), # Squire + Foot Knight
	
	("small_kingdom_21", "Slezhk", 0, 0.9, [("outlaws",-0.5),], [], 0xcbdb5e), # Royal Lancer + Heavy Lancer + Levy Axeman + Hussar + Heavy Hussar
	("small_kingdom_22", "Khudan", 0, 0.9, [("outlaws",-0.5),], [], 0xC4A285), # Scout + Club Levy + Horseman + Royal Horseman + Light Club Infantry + Club Infantry + Heavy Club Infantry
	("small_kingdom_23", "the Northern Taiga", 0, 0.9, [("outlaws",-0.5),], [], 0x466346), # Pikeman + Heavy Pikeman + Footman + Heavy Footman + Warrior
	("small_kingdom_24", "Yruma", 0, 0.9, [("outlaws",-0.5),], [], 0x88dd88), # Light Skirmisher + Heavy Skirmisher + Champion + Royal Skirmisher
	("small_kingdom_25", "the Southern Taiga", 0, 0.9, [("outlaws",-0.5),], [], 0x885500), # Heavy Mounted Longbowman + Mounted Longbowman + Longbowman + Royal Longbowman
	
	("small_kingdom_31", "Eastern", 0, 0.9, [("outlaws",-0.5),], [], 0xbb88bb), # Champion + Noble Rider + Tribal Infantry? + Tribal Light Archer? + Tribal Archer?
	("small_kingdom_32", "Warriors of Sungetche", 0, 0.9, [("outlaws",-0.5),], [], 0x997A99), # Light Skirmisher + Warrior + Heavy Skirmisher + Noble Skirmisher?
	("small_kingdom_33", "Narra", 0, 0.9, [("outlaws",-0.5),], [], 0x7e0041), # Light Horse Archer + Light Steppe Cavalry + Heavy Steppe Cavalry
	("small_kingdom_34", "Halmar", 0, 0.9, [("outlaws",-0.5),], [], 0x6D00C1), # Heavy Lancer + Noble Cavalry + Noble Lancer
	("small_kingdom_35", "Uhhun", 0, 0.9, [("outlaws",-0.5),], [], 0x9966ff), # Clansman + Light Horseman + Heavy Horseman + Noble Horseman
	("small_kingdom_36", "Azugan", 0, 0.9, [("outlaws",-0.5),], [], 0x6755db), # Heavy Archer + Blade-master + Heavy Infantry + Levy Infantry
	
	("small_kingdom_41", "Pirash", 0, 0.9, [("outlaws",-0.5),], [], 0x14FF8D), # Light Lancer + Mounted Bowman + Armoured Lancer + Heavy Mounted Bowman
	("small_kingdom_42", "Gundig", 0, 0.9, [("outlaws",-0.5),], [], 0x2f8558), # Heavy Longbowman + Light Longbowman + Light Infantry + Heavy Infantry
	("small_kingdom_43", "Wercheg", 0, 0.9, [("outlaws",-0.5),], [], 0xADE9FF), # Skirmisher + Heavy Skirmisher + Light Mounted Skirmisher + Mounted Skirmisher?
	("small_kingdom_44", "Aldelen", 0, 0.9, [("outlaws",-0.5),], [], 0x396C72), # Spearman + Heavy Spearman + Hunter + Crossbowman + Medium Spear Cavalry + Heavy Spear Cavalry
	("small_kingdom_45", "Rizi", 0, 0.9, [("outlaws",-0.5),], [], 0x0061ab), # King's Guard + Bowman + Light Spear Cavalry + Spear Cavalry + Heavy Spear Cavalry
	
	("small_kingdom_51", "Highlanders", 0, 0.9, [("outlaws",-0.5),], [], 0x4F5868), # Hunter + Bowman + Heavy Bowman + Sergeant + Highlander
	("small_kingdom_52", "Bezan", 0, 0.9, [("outlaws",-0.5),], [], 0x4F6C99), # Heroic Horseman + Levy Pikeman + Heavy Horseman + Light Horseman? + Heroic Pikeman
	("small_kingdom_53", "Veluca", 0, 0.9, [("outlaws",-0.5),], [], 0x005566), # Light Cavalry + Heavy Cavalry + Heroic Cavalry
	("small_kingdom_54", "Jamiche", 0, 0.9, [("outlaws",-0.5),], [], 0xBE9EFF), # Light Spearman + Light Skirmisher + Heavy Spearman + Mounted Crossbow + Heavy Mounted Crossbow + Heroic Mounted Crossbow + Levy Crossbow
	("small_kingdom_55", "Saren", 0, 0.9, [("outlaws",-0.5),], [], 0x74DBD2), # Mounted Crossbow + Heavy Lancer + Heroic Lancer + Scout + Levy Crossbow
	
	("small_kingdom_61", "Barriye", 0, 0.9, [("outlaws",-0.5),], [], 0x804303), # Light Crossbowman + Levy Horseman + Crossbowman + Noble Horseman?
	("small_kingdom_62", "Sharwa Keep", 0, 0.9, [("outlaws",-0.5),], [], 0xd87a17), # Heavy Archer + Noble Infantry + Levy Spearman + Spearman + Heavy Spearman + Noble Spearman
	("small_kingdom_63", "Sarrdak", 0, 0.9, [("outlaws",-0.5),], [], 0xFFBF7F), # Heavy Lancer + Cataphract + Footman + Warrior + Skirmisher + Sergeant
	("small_kingdom_64", "Uzgha", 0, 0.9, [("outlaws",-0.5),], [], 0x6f6a3e), # Light Horse Archer + Horse Archer + Heavy Horse Archer
	("small_kingdom_65", "Durquba", 0, 0.9, [("outlaws",-0.5),], [], 0xbd6123), # Mounted Skirmisher + Pikeman + Heavy Pikeman + Noble Skirmisher
	
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

	("war_storage_1", "War storage 1", 0, 0.9, [], []),
	("war_storage_2", "War storage 2", 0, 0.9, [], []),
	("war_storage_3", "War storage 3", 0, 0.9, [], []),
	("war_storage_4", "War storage 4", 0, 0.9, [], []),
	("war_storage_5", "War storage 5", 0, 0.9, [], []),
	("war_storage_6", "War storage 6", 0, 0.9, [], []),
	("war_storage_7", "War storage 7", 0, 0.9, [], []),
	("war_storage_8", "War storage 8", 0, 0.9, [], []),
	("war_storage_9", "War storage 9", 0, 0.9, [], []),
	("war_storage_10", "War storage 10", 0, 0.9, [], []),
	("war_storage_11", "War storage 11", 0, 0.9, [], []),
	("war_storage_12", "War storage 12", 0, 0.9, [], []),
	("war_storage_13", "War storage 13", 0, 0.9, [], []),
	("war_storage_14", "War storage 14", 0, 0.9, [], []),
	("war_storage_15", "War storage 15", 0, 0.9, [], []),
	("war_storage_16", "War storage 16", 0, 0.9, [], []),
	("war_storage_17", "War storage 17", 0, 0.9, [], []),
	("war_storage_18", "War storage 18", 0, 0.9, [], []),
	("war_storage_19", "War storage 19", 0, 0.9, [], []),
	("war_storage_20", "War storage 20", 0, 0.9, [], []),
	("war_storage_21", "War storage 21", 0, 0.9, [], []),
	("war_storage_22", "War storage 22", 0, 0.9, [], []),
	("war_storage_23", "War storage 23", 0, 0.9, [], []),
	("war_storage_24", "War storage 24", 0, 0.9, [], []),
	("war_storage_25", "War storage 25", 0, 0.9, [], []),
	("war_storage_26", "War storage 26", 0, 0.9, [], []),
	("war_storage_27", "War storage 27", 0, 0.9, [], []),
	("war_storage_28", "War storage 28", 0, 0.9, [], []),
	("war_storage_29", "War storage 29", 0, 0.9, [], []),
	("war_storage_30", "War storage 30", 0, 0.9, [], []),
	("war_storage_31", "War storage 31", 0, 0.9, [], []),
	("war_storage_32", "War storage 32", 0, 0.9, [], []),
	("war_storage_33", "War storage 33", 0, 0.9, [], []),
	("war_storage_34", "War storage 34", 0, 0.9, [], []),
	("war_storage_35", "War storage 35", 0, 0.9, [], []),
	("war_storage_36", "War storage 36", 0, 0.9, [], []),
	("war_storage_37", "War storage 37", 0, 0.9, [], []),
	("war_storage_38", "War storage 38", 0, 0.9, [], []),
	("war_storage_39", "War storage 39", 0, 0.9, [], []),
	("war_storage_40", "War storage 40", 0, 0.9, [], []),

	("war_storage_end", "War storage end", 0, 0.9, [], []),
]