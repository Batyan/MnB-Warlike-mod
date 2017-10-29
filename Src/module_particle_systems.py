from header_particle_systems import *





particle_systems = [
  
    ###############
    ## Hardcoded ##
	###############
    ("game_rain", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "prtcl_rain",
     500, 0.5, 0.33, 1.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (1, 0.3), (1, 0.3),        #alpha keys
     (1.0, 0.9), (1, 0.9),      #red keys
     (1.0, 0.9), (1, 0.9),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0, 0.75),   (1, 0.5),   #scale keys
     (8.2, 8.2, 0.2),           #emit box size
     (0, 0, -10.0),               #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
    ),
	
    ("game_snow", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_snow_fall_1",
     150, 2, 0.2, 0.1, 30, 20,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 1), (1, 1),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.2, 0.9),   (1.0, 1.0),   #scale keys
     (10, 10, 0.5),           #emit box size
     (0, 0, -5.0),               #emit velocity
     1,                       #emit dir randomness
     200,                       #rotation speed
     0.5                        #rotation damping
    ),
	
    ("game_blood", psf_billboard_3d |psf_randomize_size|psf_randomize_rotation,  "prt_mesh_blood_1",
     500, 0.65, 3, 0.5, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.7), (0.7, 0.7),          #alpha keys
     (0.1, 0.7), (1, 0.7),      #red keys
     (0.1, 0.7), (1, 0.7),       #green keys
     (0.1, 0.7), (1, 0.7),      #blue keys
     (0.0, 0.015),   (1, 0.018),  #scale keys
     (0, 0.05, 0),               #emit box size
     (0, 1.0, 0.3),                #emit velocity
     0.9,                       #emit dir randomness
     0,                         #rotation speed
     0,                         #rotation damping
    ),
    ("game_blood_2", psf_billboard_3d | psf_randomize_size|psf_randomize_rotation ,  "prt_mesh_blood_3",
     2000, 0.6, 3, 0.3, 0, 0,        #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.25), (0.7, 0.1),        #alpha keys
     (0.1, 0.7), (1, 0.7),      #red keys
     (0.1, 0.7), (1, 0.7),       #green keys
     (0.1, 0.7), (1, 0.7),      #blue keys
     (0.0, 0.15),   (1, 0.35),    #scale keys
     (0.01, 0.2, 0.01),             #emit box size
     (0.2, 0.3, 0),                 #emit velocity
     0.3,                         #emit dir randomness
     150,                       #rotation speed
     0,                       #rotation damping
     ),
    
     ("game_hoof_dust", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_dust_1",#prt_mesh_dust_1
     5, 2.0,  10, 0.05, 10.0, 39.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.5), (1, 0.0),        #alpha keys
     (0, 1), (1, 1),        #red keys
     (0, 0.9),(1, 0.9),         #green keys
     (0, 0.78),(1, 0.78),         #blue keys
     (0.0, 2.0),   (1.0, 3.5),   #scale keys
     (0.2, 0.3, 0.2),           #emit box size
     (0, 0, 3.9),                 #emit velocity
     0.5,                         #emit dir randomness
     130,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("game_hoof_dust_snow", psf_billboard_3d|psf_randomize_size, "prt_mesh_snow_dust_1",#prt_mesh_dust_1
     6, 2, 3.5, 1, 10.0, 0.0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 1), (1, 1),        #alpha keys
     (0, 1), (1, 1),        #red keys
     (0, 1),(1, 1),         #green keys
     (0, 1),(1, 1),         #blue keys
     (0.5, 4),   (1.0, 5.7),   #scale keys
     (0.2, 1, 0.1),           #emit box size
     (0, 0, 1),                 #emit velocity
     2,                         #emit dir randomness
     0,                       #rotation speed
     0                        #rotation damping
    ),
     ("game_hoof_dust_mud", psf_billboard_2d|psf_randomize_size|psf_randomize_rotation|psf_2d_turbulance, "prt_mesh_mud_1",#prt_mesh_dust_1
     5, .7,  10, 3, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),        #alpha keys
     (0, .7), (1, .7),        #red keys
     (0, 0.6),(1, 0.6),         #green keys
     (0, 0.4),(1, 0.4),         #blue keys
     (0.0, 0.2),   (1.0, 0.22),   #scale keys
     (0.15, 0.5, 0.1),           #emit box size
     (0, 0, 15),                 #emit velocity
     6,                         #emit dir randomness
     200,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("game_water_splash_1", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_emit_at_water_level, "prtcl_drop",
     20, 0.85, 0.25, 0.9, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 0.5), (1, 0.0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 0.3),   (1.0, 0.18),   #scale keys
     (0.3, 0.2, 0.1),           #emit box size
     (0, 1.2, 2.3),               #emit velocity
     0.3,                       #emit dir randomness
     50,                       #rotation speed
     0.5                        #rotation damping
    ),
    
    ("game_water_splash_2", psf_billboard_3d|psf_randomize_size|psf_randomize_rotation|psf_emit_at_water_level, "prtcl_splash_b",
     30, 0.4, 0.7, 0.5, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 1.0), (1, 0.3),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 0.25),   (1.0, 0.7),   #scale keys
     (0.4, 0.3, 0.1),           #emit box size
     (0, 1.3, 1.1),               #emit velocity
     0.1,                       #emit dir randomness
     50,                       #rotation speed
     0.5                        #rotation damping
    ),

    ("game_water_splash_3", psf_emit_at_water_level , "prt_mesh_water_wave_1",
     5, 2.0, 0, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.03, 0.2), (1, 0.0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 3),   (1.0, 10),   #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
    ),

	###########
	## Other ##
	###########
    ("gourd_smoke", psf_billboard_3d|psf_randomize_size,  "prt_mesh_dust_1",
     500, 3, 15, -0.05, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.0, 0.5),   (1, 1),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0.05),               #emit velocity
     2,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),
	
    ("torch_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     50, 0.35, 0.2, 0.03, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0, 0.15),   (0.4, 0.3),   #scale keys
     (0.04, 0.04, 0.01),      #emit box size
     (0, 0, 0.5),               #emit velocity
     0.0,                       #emit dir randomness
     200,                       #rotation speed
     0.5                        #rotation damping
    ),
    ("fire_glow_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_fire_2",
     2, 0.55, 0.2, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.9), (1, 0),          #alpha keys
     (0.0, 0.9), (1, 0.9),      #red keys
     (0.0, 0.7),(1, 0.7),       #green keys
     (0.0, 0.4), (1, 0.4),      #blue keys
     (0, 2),   (1.0, 2),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),

    ("fire_glow_fixed", psf_billboard_3d|psf_global_emit_dir, "prt_mesh_fire_2",
     4, 100.0, 0.2, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (-0.01, 1.0), (1, 1.0),          #alpha keys
     (0.0, 0.9), (1, 0.9),      #red keys
     (0.0, 0.7),(1, 0.7),       #green keys
     (0.0, 0.4), (1, 0.4),      #blue keys
     (0, 2),   (1.0, 2),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0
    ),

    ("torch_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prtcl_dust_a",
     15, 0.5, 0.2, -0.2, 10.0, 0.1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.25), (1, 0),       #alpha keys
     (0.0, 0.2), (1, 0.1),      #red keys
     (0.0, 0.2),(1, 0.09),      #green keys
     (0.0, 0.2), (1, 0.08),     #blue keys
     (0, 0.5),   (0.8, 2.5),    #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (0, 0, 1.5),               #emit velocity
     0.1                        #emit dir randomness
    ),

    ("torch_fire_sparks", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size,  "prt_sparks_mesh_1",
     10, 0.7, 0.2, 0, 10.0, 0.02,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.66, 1), (1, 0),          #alpha keys
     (0.1, 0.7), (1, 0.7),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.1), (1, 0.1),      #blue keys
     (0.1, 0.05),   (1, 0.05),  #scale keys
     (0.1, 0.1, 0.1),           #emit box size
     (0, 0, 0.9),               #emit velocity
     0.0,                       #emit dir randomness
     0,
     0,
    ),
	
    ("village_fire_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     50, 1.0, 0, -1.2, 25.0, 10.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.7), (1, 0),        #alpha keys
     (0.2, 1.0), (1, 0.9),      #red keys
     (0.2, 0.7),(1, 0.3),       #green keys
     (0.2, 0.2), (1, 0.0),      #blue keys
     (0, 2),   (1, 6),          #scale keys
     (2.2, 2.2, 0.2),           #emit box size
     (0, 0, 0.0),               #emit velocity
     0.0,                       #emit dir randomness
     250,                       #rotation speed
     0.3                        #rotation damping
    ),
	
	("brazier_fire_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     25, 0.5, 0.1, 0.0, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.4), (1.0, 0),        #alpha keys
     (0.5, 1.0), (1.0, 0.9),      #red keys
     (0.5, 0.7),(1.0, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.1, 0.2),   (1.0, 0.5),      #scale keys
     (0.1, 0.1, 0.01),        #emit box size
     (0.0, 0.0, 0.4),                 #emit velocity
     0.0,                       #emit dir randomness
     100,                       #rotation speed
     0.2                        #rotation damping
    ),
	 
	("fire_sparks_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size,  "prt_sparks_mesh_1",
     10, 1.5, 0.2, 0, 3, 10,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.6, 1), (1, 1),          #alpha keys
     (0.1, 0.7), (1, 0.7),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.1), (1, 0.1),      #blue keys
     (0.1, 0.07),   (1, 0.03),    #scale keys
     (0.17, 0.17, 0.01),           #emit box size
     (0, 0, 1),                 #emit velocity
     0.0,                       #emit dir randomness
     0,
     0,
    ),
	
	("cooking_fire_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     25, 0.35, 0.1, 0.03, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.8), (1, 0),        #alpha keys
     (0.5, 0.5*1.0), (1, 0.3*0.9),      #red keys
     (0.5, 0.5*0.7),(1, 0.3*0.3),       #green keys
     (0.5, 0.5*0.2), (1, 0.0),      #blue keys
     (0.1, 0.5),   (1, 1),      #scale keys
     (0.05, 0.05, 0.01),        #emit box size
     (0, 0, 1),                 #emit velocity
     0.0,                       #emit dir randomness
     200,                       #rotation speed
     0.0                        #rotation damping
    ),
	
	("cooking_smoke", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
     4, 4, 0.1, 0, 3, 5, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.2, 0.20), (1.0, 0.0),          #alpha keys
     (0.0, 0.8), (1.0, 1.0),      #red keys
     (0.0, 0.8),(1.0, 1.0),      #green keys
     (0.0, 0.85), (1.0, 1.0),     #blue keys
     (0.0, 0.65),   (1.0, 3.0),        #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0.0, 0.0, 1.2),               #emit velocity
     0.0,                        #emit dir randomness
     0,
     0,
    ),
	
	("food_steam", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_steam_1",
     3, 1, 0, 0, 8.0, 1,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.1), (1, 0),        #alpha keys
     (0.0, 1), (1, 0.1),        #red keys
     (0.0, 1),(1, 0.1),         #green keys
     (0.0, 1), (1, 0.1),        #blue keys
     (0, 0.2),   (0.9, 0.5),      #scale keys
     (0.05, 0.05, 0),          #emit box size
     (0, 0, 0.1),               #emit velocity
     0,                         #emit dir randomness
     100,                       #rotation speed
     0.5,                       #rotation damping
    ),
	
	("night_smoke_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_dust_1",
     5, 10, 1.5, 0, 50, 2,      #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.3, 0.1), (1, 0),        #alpha keys
     (0.5, 0.5), (1, 0.5),      #red keys
     (0.5, 0.5), (1, 0.5),      #green keys
     (0.5, 0.5), (1, 0.6),      #blue keys
     (0, 10),   (1, 10),        #scale keys
     (25, 25, 0.5),               #emit box size
     (0, 1, 0),                 #emit velocity
     2,                        #emit dir randomness
     20,                       #rotation speed
     1                         #rotation damping
    ),
	
	("fire_fly_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_sparks_mesh_1",
     2, 5, 1.2, 0, 50, 7,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.8), (1, 0.2),        #alpha keys
     (0.5, .7), (1, 0.7),      #red keys
     (0.5, 0.8), (1, 0.8),      #green keys
     (0.5, 1), (1, 1),      #blue keys
     (0, 0.1),   (1, 0.1),    #scale keys
     (20, 20, 0.5),             #emit box size
     (0, 0, 0),              #emit velocity
     5,                        #emit dir randomness
     0,                        #rotation speed
     0                         #rotation damping
    ),
	
	("bug_fly_1", psf_billboard_2d | psf_always_emit, "prt_mesh_rose_a",
     20, 8, 0.02, 0.025, 1, 5,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),        #alpha keys
     (0, 0.5), (1, 0.5),      #red keys
     (0, 0.5), (1, 0.5),      #green keys
     (0, 0.5), (1, 0.5),      #blue keys
     (0, 0.25),   (1, 0.25),    #scale keys
     (10, 5, 0.1),             #emit box size
     (0, 0, -0.9),              #emit velocity
     0.01,                        #emit dir randomness
     10,                        #rotation speed
     0,                         #rotation damping
    ),
	
	("flue_smoke_short", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
     15, 1.5, 0.1, -0.0, 10.0, 12, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.0, 0.3), (1, 0),        #alpha keys
     (0.0, 0.2), (1, 0.1),      #red keys
     (0.0, 0.2),(1, 0.09),      #green keys
     (0.0, 0.2), (1, 0.08),     #blue keys
     (0, 1.5),   (1, 7),          #scale keys
     (0, 0, 0),           #emit box size
     (0, 0, 1.5),               #emit velocity
     0.1,                        #emit dir randomness
     150,
     0.8,
    ),
	
    ("flue_smoke_tall", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prtcl_dust_a",
     15, 3, 0.5, -0.0, 15.0, 12,#num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.35), (1, 0),         #alpha keys
     (0.0, 0.3), (1, 0.1),      #red keys
     (0.0, 0.3),(1, 0.1),       #green keys
     (0.0, 0.3), (1, 0.1),      #blue keys
     (0, 2),   (1, 7),        #scale keys
     (0, 0, 0),                 #emit box size
     (0, 0, 1.5),               #emit velocity
     0.1,                       #emit dir randomness
     150,
     0.5,
    ),
	
	("moon_beam_1", psf_billboard_2d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prt_mesh_moon_beam",#prt_mesh_moon_beam
     2, 4, 1.2, 0, 0, 0,          #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 1), (1, 0),            #alpha keys
     (0, 0.4), (1, 0.4),                #red keys
     (0, 0.5), (1, 0.5),                #green keys
     (0, 0.6), (1, 0.6),                #blue keys
     (0, 2),   (1, 2.2),        #scale keys
     (1, 1, 0.2),                 #emit box size
     (0, 0, -2),                     #emit velocity
     0,                            #emit dir randomness
     100,                          #rotation speed
     0.5,                          #rotation damping
    ),
	
	("moon_beam_paricle_1", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size, "prt_sparks_mesh_1",
     10, 1.5, 1.5, 0, 10, 10,            #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 1), (1, 0.0),            #alpha keys
     (0.5, .5), (1, 0.5),           #red keys
     (0.5, 0.7), (1, 0.7),          #green keys
     (0.5, 1), (1, 1),              #blue keys
     (0, 0.1),   (1, 0.1),        #scale keys
     (1, 1, 4),                 #emit box size
     (0, 0, 0),                     #emit velocity
     0.5,                            #emit dir randomness
     0,                            #rotation speed
     0                             #rotation damping
    ),
	
	("fireplace_fire_small", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     25, 0.8, 0.2, -0.1, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0, 0.2),   (1, 0.7),   #scale keys
     (0.2, 0.1, 0.01),      #emit box size
     (0, 0, 0.2),               #emit velocity
     0.1,                       #emit dir randomness
     100,                       #rotation speed
     0.5                        #rotation damping
    ),
	
    ("fireplace_fire_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_fire_1",
     35, 0.6, 0.2, -0.2, 10.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.7),(1, 0.3),       #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0, 0.4),   (1, 1),   #scale keys
     (0.4, 0.2, 0.01),            #emit box size
     (0, 0, 0.4),               #emit velocity
     0.1,                       #emit dir randomness
     100,                       #rotation speed
     0.5                        #rotation damping
    ),
	
	("war_smoke_tall", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_smoke_1",
     5, 12, 0, 0, 7, 7, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 0.25), (1, 0),          #alpha keys
     (0.0, 1), (1, 0.8),      #red keys
     (0.0, 1),(1, 0.8),      #green keys
     (0.0, 1), (1, 0.8),     #blue keys
     (0, 2.2),   (1, 15),        #scale keys
     (0, 0, 0),                 #emit box size
     (0, 0, 2.2),               #emit velocity
     0.1,                        #emit dir randomness
     100,
     0.2,
    ),
	
	("village_fire_smoke_big", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_size|psf_randomize_rotation, "prt_mesh_smoke_1",
     30, 2, 0.3, -1, 50.0, 10.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.5, 0.15), (1, 0),        #alpha keys
     (0.2, 0.4), (1, 0.2),      #red keys
     (0.2, 0.4),(1, 0.2),       #green keys
     (0.2, 0.4), (1, 0.2),      #blue keys
     (0, 6),   (1, 8),          #scale keys
     (2, 2, 1),           #emit box size
     (0, 0, 5),               #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.1                        #rotation damping
    ),
	
	("candle_light", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_candle_fire_1",
     7, 1.1, 0.6, -0.0, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.3, 0.2),   (1, 0.0),    #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0.09),              #emit velocity
     0,                        #emit dir randomness
     0,                        #rotation speed
     0                         #rotation damping
    ),
	
    ("candle_light_small", psf_billboard_3d|psf_global_emit_dir|psf_always_emit, "prt_mesh_candle_fire_1",
     4, 1.1, 0.6, -0.0, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.8), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.6), (1, 0.1),      #green keys
     (0.5, 0.2), (1, 0.0),      #blue keys
     (0.3, 0.13),   (1, 0.0),   #scale keys
     (0.0, 0.0, 0.0),           #emit box size
     (0, 0, 0.06),              #emit velocity
     0,                        #emit dir randomness
     0,                        #rotation speed
     0                         #rotation damping
    ),
	
	("lamp_fire", psf_billboard_3d|psf_global_emit_dir|psf_always_emit|psf_randomize_rotation|psf_randomize_size, "prt_mesh_fire_1",
     10, 0.8, 0.6, -0.0, 10.0, 0.4,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.5, 1.0), (1, 0.9),      #red keys
     (0.5, 0.8), (1, 0.1),      #green keys
     (0.5, 0.4), (1, 0.0),      #blue keys
     (0.3, 0.35), (0.9, 0.5),    #scale keys
     (0.01, 0.01, 0.0),         #emit box size
     (0, 0, 0.35),               #emit velocity
     0.03,                      #emit dir randomness
     100,                       #rotation speed
     0.5,                       #rotation damping
    ),
	
	("dungeon_water_drops", psf_billboard_2d|psf_global_emit_dir|psf_always_emit, "prtcl_rain",
     1, 1, 0.33, 0.8, 0, 0, #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (1.0, 0.2), (1, 0.2),      #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (1.0, 0.8),   (1.0, 0.8),  #scale keys
     (0.05, 0.05, 0.5),         #emit box size
     (0, 0, -5.0),              #emit velocity
     0.0,                       #emit dir randomness
     0,                         #rotation speed
     0,                         #rotation damping
    ),
	
	("gourd_piece_1", psf_randomize_rotation,  "prt_gourd_piece_1",
     15, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1),   (1, 1),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),
    
    ("gourd_piece_2", psf_randomize_size | psf_randomize_rotation,  "prt_gourd_piece_2",
     50, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 1),   (1, 1),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),
	
	("dummy_smoke", psf_billboard_3d|psf_randomize_size,  "prt_mesh_dust_1",
     500, 3, 15, -0.05, 10.0, 0.2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 0.5), (1, 0),        #alpha keys
     (0.1, 0.8), (1, 0.8),      #red keys
     (0.1, 0.7),(1, 0.7),       #green keys
     (0.1, 0.6), (1, 0.7),      #blue keys
     (0.0, 0.7),   (1, 2.2),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0.05),               #emit velocity
     2,                         #emit dir randomness
     10,                        #rotation speed
     0.1,                       #rotation damping
    ),

    ("dummy_straw", psf_randomize_size | psf_randomize_rotation,  "prt_mesh_straw_1",
     500, 1, 2, 0.9, 10, 2,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.1, 1), (1, 1),          #alpha keys
     (0.1, 0.6), (1, 0.6),      #red keys
     (0.1, 0.5),(1, 0.5),       #green keys
     (0.1, 0.4), (1, 0.4),      #blue keys
     (0.0, 0.3),   (1, 0.3),    #scale keys
     (0.2, 0.2, 0.5),           #emit box size
     (0, 0, 0),                 #emit velocity
     2.3,                       #emit dir randomness
     200,                       #rotation speed
     0,                       #rotation damping
    ),
	
	("sea_foam_a", psf_turn_to_velocity | psf_always_emit|psf_randomize_size, "prt_foam_a",
     1, 3.0, 1, 0.0, 0.0, 0.0,     #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0.7, 0.1), (1, 0.0),        #alpha keys
     (1.0, 1.0), (1, 1.0),      #red keys
     (1.0, 1.0), (1, 1.0),      #green keys
     (1.0, 1.0), (1, 1.0),      #blue keys
     (0.0, 4),   (1.0, 4.5),   #scale keys
     (10.0, 1.0, 0),           #emit box size
     (0, 1, 0),                 #emit velocity
     0.0,                       #emit dir randomness
     0,                       #rotation speed
     0.5                        #rotation damping
    ),
	
    ("fall_leafs_a", psf_billboard_2d | psf_always_emit, "prt_mesh_yrellow_leaf_a",
     1, 9, 0, 0.025, 4, 4,      #num_particles, life, damping, gravity_strength, turbulance_size, turbulance_strength
     (0, 1), (1, 1),            #alpha keys
     (0, 0.5), (1, 0.5),        #red keys
     (0, 0.5), (1, 0.5),        #green keys
     (0, 0.5), (1, 0.5),        #blue keys
     (0, 0.25),   (1, 0.25),    #scale keys
     (4, 4, 4),                 #emit box size
     (0, 0.01, -0.9),           #emit velocity
     0.02,                     #emit dir randomness
     15,                       #rotation speed
     0,                        #rotation damping
    ),
	
	###########
	## Other ##
	###########
]
