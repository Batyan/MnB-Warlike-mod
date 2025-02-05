from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *





scenes = [

    ###############
    ## Hardcoded ##
	###############
  ("random_scene",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[]),
  ("conversation_scene",0,"encounter_spot", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
    [],[]),
  ("water",0,"none", "none", (-1000,-1000),(1000,1000),-0.5,"0",
    [],[]),
  ("random_scene_steppe",sf_generate|sf_randomize,"none", "none", (0,0),(240,240),-0.5,"0x000000022383d06300070dc000003e3800001dc900001e07",
    [],[], "outer_terrain_steppe"),
  ("random_scene_plain",sf_generate|sf_randomize,"none", "none", (0,0),(240,240),-0.5,"0x000000023383d06300070dc000003e3800001dc900001e07",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow",sf_generate|sf_randomize,"none", "none", (0,0),(240,240),-0.5,"0x000000024383d06300070dc000003e3800001dc900001e07",
    [],[], "outer_terrain_snow"),
  ("random_scene_desert",sf_generate|sf_randomize,"none", "none", (0,0),(240,240),-0.5,"0x000000025383d06300070dc000003e3800001dc900001e07",
    [],[], "outer_terrain_desert_b"),
  ("random_scene_steppe_forest",sf_generate|sf_randomize,"none", "none", (0,0),(240,240),-0.5,"0x00000002a923d06300070dc000003e3800001dc900001e07",
    [],[], "outer_terrain_plain"),
  ("random_scene_plain_forest",sf_generate|sf_randomize,"none", "none", (0,0),(240,240),-0.5,"0x00000002b923d06300070dc000003e3800001dc900001e07",
    [],[], "outer_terrain_plain"),
  ("random_scene_snow_forest",sf_generate|sf_randomize,"none", "none", (0,0),(240,240),-0.5,"0x00000002c923d06300070dc000003e3800001dc900001e07",
    [],[], "outer_terrain_snow"),
  ("random_scene_desert_forest",sf_generate|sf_randomize,"none", "none", (0,0),(240,240),-0.5,"0x00000002d923d06300070dc000003e3800001dc900001e07",
    [],[], "outer_terrain_desert"),
  ("camp_scene",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("camp_scene_horse_track",sf_generate|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x300028000003e8fa0000034e00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("four_ways_inn",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[], "outer_terrain_town_thir_1"),
  ("test_scene",sf_generate,"none", "none", (0,0),(120,120),-100,"0x0230817a00028ca300007f4a0000479400161992",
    [],[], "outer_terrain_plain"),
	
	
	
	
	
	###########
	## Other ##
	###########
	("test_battle", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x000000012c6005630007d9f200000f4d0000735500000288",
		[],[], "outer_terrain_plain"),
	
	("test_battle_plain", sf_generate|sf_randomize, "none", "none", (0,0), (240,240),-0.5,"0x000000022383d06300070dc000003e3800001dc900001e07",
		[],[], "outer_terrain_plain"),
	
	("castle_plain_01_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x0000000334c356a0800615870000575500007f310000359d",
		[],[], "outer_terrain_plain"),
	
	("castle_plain_02_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x00000000324805308005b969000069f300004c1500000248",
		[],[], "outer_terrain_plain"),
	
	("castle_plain_03_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x000000013002d76340053d4f00001c0c0000777d00003fef",
		[],[], "outer_terrain_plain"),
	
	("castle_plain_wood_01_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x0000000332655a630006098400001edc0000246b00007856",
		[],[], "outer_terrain_plain"),
		
	("castle_plain_dark_01_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x00000001b244d2000006098d00005999000033a700007a61",
		[],[], "outer_terrain_plain"),
	
	# # TODO
	# ("castle_forest_01_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x000000013002d763400771d400001c0c0000777d00007a52",
	# 	[],[], "outer_terrain_plain"),
	
	# # TODO
	# ("castle_forest_wood_01_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x0000000332655a630006098400001edc0000246b00007856",
	# 	[],[], "outer_terrain_plain"),
		
	# # TODO
	# ("castle_forest_dark_01_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x00000001b244d2000006098d00005999000033a700007a61",
	# 	[],[], "outer_terrain_plain"),
	
	# TODO
	("castle_sea_01_outside", sf_generate, "none", "none", (0,0), (240,240),-100,"0x00000001360624ca000725c30000203e00003728000071a7",
		[],[], "sea_outer_terrain_1"),
	
	# # TODO
	# ("castle_sea_wood_01_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x0000000334c356a0800615870000575500007f310000359d",
	# 	[],[], "sea_outer_terrain_1"),
	
	# # TODO
	# ("castle_sea_dark_01_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x0000000334c356a0800615870000575500007f310000359d",
	# 	[],[], "sea_outer_terrain_1"),
		
	("castle_steppe_01_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x00000003264b18e30004912200007b7e00006d9e00006880",
		[],[], "outer_terrain_steppe"),
	
	("castle_snow_01_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x0000000040c391af0005fd1100007c4900007ef600007fea",
		[],[], "outer_terrain_snow"),
		
	("castle_snow_02_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x0000000341c0d252800882250000173200005ca30000598f",
		[],[], "outer_terrain_snow"),
		
	("castle_snow_wood_01_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x00000000c7a745630005a16a0000493f00002d040000207f",
		[],[], "outer_terrain_snow"),
	
	("castle_desert_01_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x0000000355e350e30004912200003bf800006d9e00005ab9",
		[],[], "outer_terrain_desert"),
	

	("castle_garden_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x00000002500596228002589600007fa68000600c00004bc1",
		[],[], "outer_terrain_desert"),
	
	("castle_plain_river_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x0000000220040e938007edf10000324780004421000038cf",
		[],[], "outer_terrain_plain"),
	
	("castle_dross_delnoch_outside", sf_generate, "none", "none", (0,0), (240,240),-0.5,"0x0000000240027763800815f500006a510000730c00002ce0",
		[],[], "outer_terrain_snow"),
	


	("meeting_scene_steppe",0,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
		[],[]),
	("meeting_scene_plain",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
		[],[]),
	("meeting_scene_snow",0,"ch_meet_snow_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
		[],[]),
	("meeting_scene_desert",0,"ch_meet_desert_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
		[],[]),
	("meeting_scene_steppe_forest",0,"ch_meet_steppe_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
		[],[]),
	("meeting_scene_plain_forest",0,"ch_meet_plain_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
		[],[]),
	("meeting_scene_snow_forest",0,"ch_meet_snow_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
		[],[]),
	("meeting_scene_desert_forest",0,"ch_meet_desert_a", "bo_encounter_spot", (-40,-40),(40,40),-100,"0",
		[],[]),
		
		
		
	("places_plain_stone_obelisk",sf_generate,"none", "none", (-40,-40),(40,40),-100,"0x0000000239c0115d00087221000042c600005a4300000fa1",
		[],[], "outer_terrain_plain"),
	("places_desert_grand_tree",0,"none", "none", (-40,-40),(40,40),-100,"0x0000000239c0115d00087221000042c600005a4300000fa1",
		[],[], "outer_terrain_desert"),

	
	
	#################
    ## Multiplayer ##
	#################
  ("multi_scene_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000012002a0b20004992700006e54000007fe00001fd2",
    [],[],"outer_terrain_steppe"),
  ("multi_scene_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002e0b20005154500006e540000235600007b55",
    [],[],"outer_terrain_plain"),
  ("multi_scene_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300659630003c8f300003ca000006a8900003c89",
    [],[],"outer_terrain_plain"),
  ("multi_scene_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300494b200048524000059e80000453300001d32",
    [],[],"outer_terrain_plain"),
  ("multi_scene_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130010e0e0005fd84000011c60000285b00005cbe",
    [],[],"outer_terrain_plain"),
  ("multi_scene_8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000020004db18004611400005c918000397b00004c2e",
    [],[],"outer_terrain_plain"),
  ("multi_scene_9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000400032320003c0f300001f9e000011180000031c",   
    [],[],"outer_terrain_snow"),
  ("multi_scene_10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003009cde1000599630000423b00005756000000af",
    [],[],"outer_terrain_plain"),
  ("multi_scene_11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030015f2b000350d4000011a4000017ee000054af",
    [],[],"outer_terrain_plain"),
  ("multi_scene_12",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013003d7e30005053f00003b4e0000146300006e84",
    [],[],"outer_terrain_beach"),
  ("multi_scene_13",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_14",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000040000c910003e8fa0000538900003e9e00005301",
    [],[],"outer_terrain_snow"),
  ("multi_scene_15",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500b1d158005394c00001230800072880000018f",
    [],[],"outer_terrain_desert"),       
  ("multi_scene_16",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000d007abd20002c8b1000050c50000752a0000788c",
    [],[],"outer_terrain_desert"),
  ("multi_scene_17",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002200005000005f57b00005885000046bd00006d9c",
    [],[],"outer_terrain_plain"),
  ("multi_scene_18",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x00000000b00037630002308c00000c9400005d4c00000f3a",
    [],[],"outer_terrain_plain"),
  
  ("random_multi_plain_medium",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000001394018dd000649920004406900002920000056d7",
    [],[], "outer_terrain_plain"),
  ("random_multi_plain_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000013a001853000aa6a40004406900002920001e4f81",
    [],[], "outer_terrain_plain"),
  ("random_multi_steppe_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x0000000128601ae300063d8f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),
  ("random_multi_steppe_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x000000012a00d8630009fe7f0004406900002920001e4f81",
    [],[], "outer_terrain_steppe"),

  ("multiplayer_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
]
