from header_music import *





tracks = [

	("bogus", "cant_find_this.ogg", 0, 0),
	("mount_and_blade_title_screen", "mount_and_blade_title_screen.ogg", mtf_sit_main_title|mtf_start_immediately, 0),
	("ambushed_by_neutral", "ambushed_by_neutral.ogg", mtf_sit_ambushed|mtf_sit_siege, mtf_sit_fight|mtf_sit_multiplayer_fight),
	
	("fight_1", "fight_1.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
	("fight_2", "fight_2.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
	("fight_3", "fight_3.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),
	("fight_4", "percussion_battery.ogg", mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed, 0),  
	
	("town_neutral", "town_neutral.ogg", mtf_sit_town|mtf_sit_travel, mtf_sit_tavern|mtf_sit_night),
	("travel_neutral", "travel_neutral.ogg", mtf_sit_travel, mtf_sit_town|mtf_sit_tavern|mtf_sit_night),
]
