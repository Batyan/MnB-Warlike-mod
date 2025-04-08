from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
from module_constants import *





game_menus = [

    ###############
    ## Hardcoded ##
    ###############
    ("start_game_0", menu_text_color(0xFF000000)|mnf_disable_all_keys,
        "{s0}",
        "none",
        [(str_store_string, s0, "str_start_game_introduction_text"),],
        [     
            ("start_female", 
                [
                    (troop_get_type, ":player_gender", "$g_player_troop"),
                    (try_begin),
                        (eq, ":player_gender", tf_female),
                        (disable_menu_option),
                    (try_end),
                ], "Female",
                [
                    (troop_set_type, "$g_player_troop", tf_female),
                    (troop_set_type, "trp_player", tf_female),
                    # (display_message, "@Player is female"),
                    (jump_to_menu, "mnu_start_game_0"),
                ]),
            
            ("start_male", 
                [
                    (troop_get_type, ":player_gender", "$g_player_troop"),
                    (try_begin),
                        (eq, ":player_gender", tf_male),
                        (disable_menu_option),
                    (try_end),
                ], "Male",
                [
                    (troop_set_type, "$g_player_troop", tf_male),
                    (troop_set_type, "trp_player", tf_male),
                    # (display_message, "@Player is male"),
                    (jump_to_menu, "mnu_start_game_0"),
                ]),
            
            ("spacing", [(disable_menu_option),], " _ ", []),

            ("continue", [], "Accept",  
                [
                    (assign, "$g_test_player_troop", -1),
                    (call_script, "script_troop_change_stat_with_template", "$g_player_troop", "trp_current_player"),

                    (assign, "$g_start_game_intro_culture", -1),
                    (assign, "$g_start_game_intro_parents", -1),
                    (assign, "$g_start_game_intro_childhood", -1),
                    (assign, "$g_start_game_intro_aptitude", -1),
                    (assign, "$g_start_game_intro_job", -1),
                    (assign, "$g_start_game_intro_motivation", -1),
                    (assign, "$g_start_game_intro_location", -1),
                    
                    (jump_to_menu, "mnu_start_game_1"),
                ]),

            ("go_back",[],"Back to main menu",
                [
                    (change_screen_quit),
                ]),
        ]),
    
    ("start_game_1", mnf_disable_all_keys,
        "{s0}",
        "none",
        [
            (try_begin),
                (eq, "$g_start_game_intro_culture", -1),
                (eq, "$g_start_game_intro_location", -1),
                (str_store_string, s0, "@You are about to embark in an adventure in Calradia, but first what circumstances have led you to this point?"),
            (else_try),
                (neg|is_between, "$g_test_player_faction", kingdoms_begin, kingdoms_end),

                (try_begin),
                    (eq, "$g_start_game_intro_location", player_starting_7_swadia),
                    (str_store_party_name, s10, "p_town_11"),
                (else_try),
                    (eq, "$g_start_game_intro_location", player_starting_7_vaegir),
                    (str_store_party_name, s10, "p_town_21"),
                (else_try),
                    (eq, "$g_start_game_intro_location", player_starting_7_khergit),
                    (str_store_party_name, s10, "p_town_31"),
                (else_try),
                    (eq, "$g_start_game_intro_location", player_starting_7_nord),
                    (str_store_party_name, s10, "p_town_41"),
                (else_try),
                    (eq, "$g_start_game_intro_location", player_starting_7_rhodok),
                    (str_store_party_name, s10, "p_town_51"),
                (else_try),
                    (eq, "$g_start_game_intro_location", player_starting_7_sarranid),
                    (str_store_party_name, s10, "p_town_61"),
                (try_end),
                (str_store_string, s0, "@You are ready to embark on your adventure. The nearby town of {s10} could be a good place to find early work..."),
            (try_end),
        ],
        [
            ("continue", [], "Continue",
                [
                    (try_begin),
                        (eq, "$g_start_game_intro_culture", -1),
                        (assign, "$g_test_player_troop", "trp_swadian_light_cavalry"),

                        (jump_to_menu, "mnu_start_game_intro_1"),
                    (else_try),
                        (neg|is_between, "$g_test_player_faction", kingdoms_begin, kingdoms_end),
                        (assign, "$g_test_player_faction", "fac_kingdom_1"),

                        (change_screen_return),

                        # (assign, ":banner", banner_scene_props_begin),
                        (troop_set_slot, "$g_player_troop", slot_troop_banner_scene_prop, 0),

                        (str_store_troop_name, s10, "$g_player_troop"),
                        (troop_set_plural_name, "$g_player_troop", s10),

                        (assign, ":starting_town", 0),
                        (try_begin),
                            (eq, "$g_start_game_intro_location", player_starting_7_swadia),
                            (assign, ":starting_town", "p_town_11"),
                        (else_try),
                            (eq, "$g_start_game_intro_location", player_starting_7_vaegir),
                            (assign, ":starting_town", "p_town_21"),
                        (else_try),
                            (eq, "$g_start_game_intro_location", player_starting_7_khergit),
                            (assign, ":starting_town", "p_town_31"),
                        (else_try),
                            (eq, "$g_start_game_intro_location", player_starting_7_nord),
                            (assign, ":starting_town", "p_town_41"),
                        (else_try),
                            (eq, "$g_start_game_intro_location", player_starting_7_rhodok),
                            (assign, ":starting_town", "p_town_51"),
                        (else_try),
                            (eq, "$g_start_game_intro_location", player_starting_7_sarranid),
                            (assign, ":starting_town", "p_town_61"),
                        (try_end),
                        (quest_set_slot, "qst_introduction_default", slot_quest_destination, ":starting_town"),
                        (call_script, "script_start_quest", "qst_introduction_default", -1),
                    (try_end),
                ]),
        ]),
    
    ("start_game_intro_1", mnf_disable_all_keys,
        "{s0}",
        "none",
        [
            (str_store_string, s10, "str_start_game_intro_1"),
            (try_begin),
                (eq, "$g_start_game_intro_culture", -1),
                (str_clear, s11),
            (else_try),
                (is_between, "$g_start_game_intro_culture", cultures_begin, cultures_end),
                (store_sub, ":offset", "$g_start_game_intro_culture", cultures_begin),

                (store_add, ":str", "str_start_game_intro_1_choice_swadian", ":offset"),
                (str_store_string, s11, ":str"),
            (try_end),

            (str_store_string, s0, "@{s10}^^{s11}"),
        ],
        [
            ("choice_swadian", 
                [(try_begin),(eq, "$g_start_game_intro_culture", "fac_culture_1"),(disable_menu_option),(try_end),], "In the plains of Swadia",
                [
                    (assign, "$g_start_game_intro_culture", "fac_culture_1"),
                    (jump_to_menu, "mnu_start_game_intro_1"),
                ]),
            ("choice_vaegir", 
                [(try_begin),(eq, "$g_start_game_intro_culture", "fac_culture_2"),(disable_menu_option),(try_end),], "In the Vaegir tundra",
                [
                    (assign, "$g_start_game_intro_culture", "fac_culture_2"),
                    (jump_to_menu, "mnu_start_game_intro_1"),
                ]),
            ("choice_khergit", 
                [(try_begin),(eq, "$g_start_game_intro_culture", "fac_culture_3"),(disable_menu_option),(try_end),], "In the Khergit steppes",
                [
                    (assign, "$g_start_game_intro_culture", "fac_culture_3"),
                    (jump_to_menu, "mnu_start_game_intro_1"),
                ]),
            ("choice_nordic", 
                [(try_begin),(eq, "$g_start_game_intro_culture", "fac_culture_4"),(disable_menu_option),(try_end),], "On the Nordic coasts",
                [
                    (assign, "$g_start_game_intro_culture", "fac_culture_4"),
                    (jump_to_menu, "mnu_start_game_intro_1"),
                ]),
            ("choice_rhodok", 
                [(try_begin),(eq, "$g_start_game_intro_culture", "fac_culture_5"),(disable_menu_option),(try_end),], "In the Rhodok hills",
                [
                    (assign, "$g_start_game_intro_culture", "fac_culture_5"),
                    (jump_to_menu, "mnu_start_game_intro_1"),
                ]),
            ("choice_sarranid", 
                [(try_begin),(eq, "$g_start_game_intro_culture", "fac_culture_6"),(disable_menu_option),(try_end),], "In the Sarranid deserts",
                [
                    (assign, "$g_start_game_intro_culture", "fac_culture_6"),
                    (jump_to_menu, "mnu_start_game_intro_1"),
                ]),
            ("choice_foreign", 
                [(try_begin),(eq, "$g_start_game_intro_culture", "fac_culture_7"),(disable_menu_option),(try_end),], "In a far away land",
                [
                    (assign, "$g_start_game_intro_culture", "fac_culture_7"),
                    (jump_to_menu, "mnu_start_game_intro_1"),
                ]),

            ("continue", 
                [
                    (try_begin),
                        (eq, "$g_start_game_intro_culture", -1),
                        (disable_menu_option),
                    (try_end),
                ], "Continue",
                [
                    (jump_to_menu, "mnu_start_game_intro_2"),
                ]),
        ]),
    
    ("tutorial", mnf_disable_all_keys,
        "Tutorial",
        "none",
        [],
        [
            ("return", [], "Return",
                [
                    (change_screen_quit),
                ]),
        ]),

    ("reports", 0,
        "Reports",
        "none",
        [],
        [
            ## General reports - displays a large amount of general informations
            # Global report shows party speed, current party size, max party size, prisoners, max prisoners, current morale, party wages
            ("report_global", [(disable_menu_option),], "Global report", []),
            # Personal report shows player traits, player stat boosts, current gold, current renown, current honor rating
            ("report_personal", [(disable_menu_option),], "Personal report", []),

            ## Detailed reports - displays specific informations about a particular topic
            # Displays morale report
            ("report_morale",[(disable_menu_option),],"Morale report",[]),
            # Displays wages for the current party (not fiefs)
            ("report_budget",[],"Budget report",
                [
                    (assign, "$g_process_effects", 0),
                    (start_presentation, "prsnt_budget_report"),
                ]),

            ("resume_travelling",[],"Resume travelling",
                [
                    (change_screen_return),
                ]),
        ]),

    ("camp", mnf_scale_picture,
        "Camp",
        "none",
        [
            (set_background_mesh, "mesh_pic_camp"),
        ],
        [
            ("camp_settings", [], "Customize game settings",
                [(jump_to_menu, "mnu_settings"),]),

            ("camp_debug_settings", [(call_script, "script_cf_debug", debug_all),], "Debug settings",
                [
                    (jump_to_menu, "mnu_debug_settings"),
                ]),
            ("camp_debug_menu", [(call_script, "script_cf_debug", debug_all),], "Debug menu",
                [
                    (jump_to_menu, "mnu_debug_menu"),
                ]),
            ("camp_debug_actions", [(call_script, "script_cf_debug", debug_all),], "Debug actions",
                [
                    (jump_to_menu, "mnu_debug_actions"),
                ]),

            ("camp_actions", [], "Take an action",
                [
                    (jump_to_menu, "mnu_camp_actions"),
                ]),
            
            ("resume_travelling",[], "Dismantle camp",
                [
                    (change_screen_return),
                ]),
        ]),
    
    ###########
    ## Intro ##
    ###########
    ("start_game_intro_2", mnf_disable_all_keys,
        "{s0}",
        "none",
        [
            (str_store_string, s10, "str_start_game_intro_2"),

            (troop_get_type, reg10, "$g_player_troop"),
            (try_begin),
                (eq, "$g_start_game_intro_parents", -1),
                (str_clear, s11),
            (else_try),
                (store_add, ":str", "str_start_game_intro_2_choice_noble", "$g_start_game_intro_parents"),
                (str_store_string, s11, ":str"),
            (try_end),

            (str_store_string, s0, "@{s10}^^{s11}"),
        ],
        [
            ("choice_noble", 
                [(try_begin),(eq, "$g_start_game_intro_parents", player_starting_2_noble),(disable_menu_option),(try_end),], "An impoverished noble",
                [
                    (assign, "$g_start_game_intro_parents", player_starting_2_noble),
                    (jump_to_menu, "mnu_start_game_intro_2"),
                ]),
            ("choice_farmer", 
                [(try_begin),(eq, "$g_start_game_intro_parents", player_starting_2_farmer),(disable_menu_option),(try_end),], "A farmer",
                [
                    (assign, "$g_start_game_intro_parents", player_starting_2_farmer),
                    (jump_to_menu, "mnu_start_game_intro_2"),
                ]),
            ("choice_hunter", 
                [(try_begin),(eq, "$g_start_game_intro_parents", player_starting_2_hunter),(disable_menu_option),(try_end),], "A hunter",
                [
                    (assign, "$g_start_game_intro_parents", player_starting_2_hunter),
                    (jump_to_menu, "mnu_start_game_intro_2"),
                ]),
            ("choice_artisan", 
                [(try_begin),(eq, "$g_start_game_intro_parents", player_starting_2_artisan),(disable_menu_option),(try_end),], "An artisan",
                [
                    (assign, "$g_start_game_intro_parents", player_starting_2_artisan),
                    (jump_to_menu, "mnu_start_game_intro_2"),
                ]),
            ("choice_court_advisor", 
                [(try_begin),(eq, "$g_start_game_intro_parents", player_starting_2_advisor),(disable_menu_option),(try_end),], "A court advisor",
                [
                    (assign, "$g_start_game_intro_parents", player_starting_2_advisor),
                    (jump_to_menu, "mnu_start_game_intro_2"),
                ]),
            ("choice_trader", 
                [(try_begin),(eq, "$g_start_game_intro_parents", player_starting_2_trader),(disable_menu_option),(try_end),], "A travelling merchant",
                [
                    (assign, "$g_start_game_intro_parents", player_starting_2_trader),
                    (jump_to_menu, "mnu_start_game_intro_2"),
                ]),
            ("choice_mercenary", 
                [(try_begin),(eq, "$g_start_game_intro_parents", player_starting_2_mercenary),(disable_menu_option),(try_end),], "A veteran warrior",
                [
                    (assign, "$g_start_game_intro_parents", player_starting_2_mercenary),
                    (jump_to_menu, "mnu_start_game_intro_2"),
                ]),
            ("choice_outlaw", 
                [(try_begin),(eq, "$g_start_game_intro_parents", player_starting_2_outlaw),(disable_menu_option),(try_end),], "A wanted outlaw",
                [
                    (assign, "$g_start_game_intro_parents", player_starting_2_outlaw),
                    (jump_to_menu, "mnu_start_game_intro_2"),
                ]),
            ("choice_nomad", 
                [(try_begin),(eq, "$g_start_game_intro_parents", player_starting_2_nomad),(disable_menu_option),(try_end),], "A steppe nomad",
                [
                    (assign, "$g_start_game_intro_parents", player_starting_2_nomad),
                    (jump_to_menu, "mnu_start_game_intro_2"),
                ]),

            ("continue", 
                [
                    (try_begin),
                        (eq, "$g_start_game_intro_parents", -1),
                        (disable_menu_option),
                    (try_end),
                ], "Continue",
                [
                    (jump_to_menu, "mnu_start_game_intro_3"),
                ]),
        ]),
    
    ("start_game_intro_3", mnf_disable_all_keys,
        "{s0}",
        "none",
        [
            (str_store_string, s10, "str_start_game_intro_3"),

            (troop_get_type, reg10, "$g_player_troop"),
            (try_begin),
                (eq, "$g_start_game_intro_childhood", -1),
                (str_clear, s11),
            (else_try),
                (store_add, ":str", "str_start_game_intro_3_choice_street_urchin", "$g_start_game_intro_childhood"),
                (str_store_string, s11, ":str"),
            (try_end),

            (str_store_string, s0, "@{s10}^^{s11}"),
        ],
        [
            ("choice_street_urchin", 
                [(try_begin),(eq, "$g_start_game_intro_childhood", player_starting_3_urchin),(disable_menu_option),(try_end),], "a street urchin",
                [
                    (assign, "$g_start_game_intro_childhood", player_starting_3_urchin),
                    (jump_to_menu, "mnu_start_game_intro_3"),
                ]),

            ("choice_apprentice", 
                [(try_begin),(eq, "$g_start_game_intro_childhood", player_starting_3_apprentice),(disable_menu_option),(try_end),], "a craftsman's apprentice",
                [
                    (assign, "$g_start_game_intro_childhood", player_starting_3_apprentice),
                    (jump_to_menu, "mnu_start_game_intro_3"),
                ]),

            ("choice_stable", 
                [(try_begin),(eq, "$g_start_game_intro_childhood", player_starting_3_stable),(disable_menu_option),(try_end),], "a stable hand",
                [
                    (assign, "$g_start_game_intro_childhood", player_starting_3_stable),
                    (jump_to_menu, "mnu_start_game_intro_3"),
                ]),

            ("choice_farmer", 
                [(try_begin),(eq, "$g_start_game_intro_childhood", player_starting_3_farmer),(disable_menu_option),(try_end),], "a helper in a farm",
                [
                    (assign, "$g_start_game_intro_childhood", player_starting_3_farmer),
                    (jump_to_menu, "mnu_start_game_intro_3"),
                ]),

            ("choice_errand", 
                [(try_begin),(eq, "$g_start_game_intro_childhood", player_starting_3_errand),(disable_menu_option),(try_end),], "an errand {boy/girl}",
                [
                    (assign, "$g_start_game_intro_childhood", player_starting_3_errand),
                    (jump_to_menu, "mnu_start_game_intro_3"),
                ]),

            ("choice_schooled", 
                [(try_begin),(eq, "$g_start_game_intro_childhood", player_starting_3_school),(disable_menu_option),(try_end),], "a school student",
                [
                    (assign, "$g_start_game_intro_childhood", player_starting_3_school),
                    (jump_to_menu, "mnu_start_game_intro_3"),
                ]),

            ("choice_page", 
                [(try_begin),(eq, "$g_start_game_intro_childhood", player_starting_3_page),(disable_menu_option),(try_end),], "a page at a nobleman's court",
                [
                    (assign, "$g_start_game_intro_childhood", player_starting_3_page),
                    (jump_to_menu, "mnu_start_game_intro_3"),
                ]),

            ("continue", 
                [
                    (try_begin),
                        (eq, "$g_start_game_intro_childhood", -1),
                        (disable_menu_option),
                    (try_end),
                ], "Continue",
                [
                    (jump_to_menu, "mnu_start_game_intro_4"),
                ]),
        ]),
    
    ("start_game_intro_4", mnf_disable_all_keys,
        "{s0}",
        "none",
        [
            (str_store_string, s10, "str_start_game_intro_4"),
            (try_begin),
                (eq, "$g_start_game_intro_aptitude", -1),
                (str_clear, s11),
            (else_try),
                (store_add, ":str", "str_start_game_intro_4_choice_generous", "$g_start_game_intro_aptitude"),
                (str_store_string, s11, ":str"),
            (try_end),

            (str_store_string, s0, "@{s10}^^{s11}"),
        ],
        [
            ("choice_generous",
                [(try_begin),(eq, "$g_start_game_intro_aptitude", player_starting_4_generous),(disable_menu_option),(try_end),], "generous",
                [
                    (assign, "$g_start_game_intro_aptitude", player_starting_4_generous),
                    (jump_to_menu, "mnu_start_game_intro_4"),
                ]),

            ("choice_ruthless",
                [(try_begin),(eq, "$g_start_game_intro_aptitude", player_starting_4_ruthless),(disable_menu_option),(try_end),], "ruthless",
                [
                    (assign, "$g_start_game_intro_aptitude", player_starting_4_ruthless),
                    (jump_to_menu, "mnu_start_game_intro_4"),
                ]),
            
            ("choice_caring",
                [(try_begin),(eq, "$g_start_game_intro_aptitude", player_starting_4_caring),(disable_menu_option),(try_end),], "caring",
                [
                    (assign, "$g_start_game_intro_aptitude", player_starting_4_caring),
                    (jump_to_menu, "mnu_start_game_intro_4"),
                ]),
            
            ("choice_charm",
                [(try_begin),(eq, "$g_start_game_intro_aptitude", player_starting_4_charm),(disable_menu_option),(try_end),], "charming",
                [
                    (assign, "$g_start_game_intro_aptitude", player_starting_4_charm),
                    (jump_to_menu, "mnu_start_game_intro_4"),
                ]),
            
            ("choice_shrewd",
                [(try_begin),(eq, "$g_start_game_intro_aptitude", player_starting_4_shrewd),(disable_menu_option),(try_end),], "shrewd",
                [
                    (assign, "$g_start_game_intro_aptitude", player_starting_4_shrewd),
                    (jump_to_menu, "mnu_start_game_intro_4"),
                ]),
            
            ("choice_strong",
                [(try_begin),(eq, "$g_start_game_intro_aptitude", player_starting_4_strong),(disable_menu_option),(try_end),], "strong",
                [
                    (assign, "$g_start_game_intro_aptitude", player_starting_4_strong),
                    (jump_to_menu, "mnu_start_game_intro_4"),
                ]),
            
            ("choice_energy",
                [(try_begin),(eq, "$g_start_game_intro_aptitude", player_starting_4_energy),(disable_menu_option),(try_end),], "full of energy",
                [
                    (assign, "$g_start_game_intro_aptitude", player_starting_4_energy),
                    (jump_to_menu, "mnu_start_game_intro_4"),
                ]),
            
            ("choice_calculating",
                [(try_begin),(eq, "$g_start_game_intro_aptitude", player_starting_4_calculating),(disable_menu_option),(try_end),], "calculating",
                [
                    (assign, "$g_start_game_intro_aptitude", player_starting_4_calculating),
                    (jump_to_menu, "mnu_start_game_intro_4"),
                ]),

            ("continue", 
                [
                    (try_begin),
                        (eq, "$g_start_game_intro_aptitude", -1),
                        (disable_menu_option),
                    (try_end),
                ], "Continue",
                [
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),
        ]),
    
    ("start_game_intro_5", mnf_disable_all_keys,
        "{s0}",
        "none",
        [
            (str_store_string, s10, "str_start_game_intro_5"),
            
            (troop_get_type, reg10, "$g_player_troop"),
            (try_begin),
                (eq, "$g_start_game_intro_job", -1),
                (str_clear, s11),
            (else_try),
                (store_add, ":str", "str_start_game_intro_5_choice_guard", "$g_start_game_intro_job"),
                (str_store_string, s11, ":str"),
            (try_end),

            (str_store_string, s0, "@{s10}^^{s11}"),
        ],
        [
            ("choice_guard",
                [(try_begin),(eq, "$g_start_game_intro_job", player_starting_5_guard),(disable_menu_option),(try_end),], "A city watch",
                [
                    (assign, "$g_start_game_intro_job", player_starting_5_guard),
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),
            
            ("choice_outlaw",
                [(try_begin),(eq, "$g_start_game_intro_job", player_starting_5_outlaw),(disable_menu_option),(try_end),], "A wanted outlaw",
                [
                    (assign, "$g_start_game_intro_job", player_starting_5_outlaw),
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),
            
            ("choice_pickpocket",
                [(try_begin),(eq, "$g_start_game_intro_job", player_starting_5_pickpocket),(disable_menu_option),(try_end),], "A pickpocket in the streets",
                [
                    (assign, "$g_start_game_intro_job", player_starting_5_pickpocket),
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),
            
            ("choice_messenger",
                [(try_begin),(eq, "$g_start_game_intro_job", player_starting_5_messenger),(disable_menu_option),(try_end),], "A messenger",
                [
                    (assign, "$g_start_game_intro_job", player_starting_5_messenger),
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),
            
            ("choice_hunter",
                [(try_begin),(eq, "$g_start_game_intro_job", player_starting_5_hunter),(disable_menu_option),(try_end),], "A game poacher",
                [
                    (assign, "$g_start_game_intro_job", player_starting_5_hunter),
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),
            
            ("choice_farmer",
                [(try_begin),(eq, "$g_start_game_intro_job", player_starting_5_farmer),(disable_menu_option),(try_end),], "A farmer",
                [
                    (assign, "$g_start_game_intro_job", player_starting_5_farmer),
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),
            
            ("choice_merchant",
                [(try_begin),(eq, "$g_start_game_intro_job", player_starting_5_merchant),(disable_menu_option),(try_end),], "A travelling merchant",
                [
                    (assign, "$g_start_game_intro_job", player_starting_5_merchant),
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),
            
            ("choice_mercenary",
                [(try_begin),(eq, "$g_start_game_intro_job", player_starting_5_mercenary),(disable_menu_option),(try_end),], "A mercenary",
                [
                    (assign, "$g_start_game_intro_job", player_starting_5_mercenary),
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),
            
            ("choice_artisan",
                [(try_begin),(eq, "$g_start_game_intro_job", player_starting_5_artisan),(disable_menu_option),(try_end),], "An artisan",
                [
                    (assign, "$g_start_game_intro_job", player_starting_5_artisan),
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),
            
            ("choice_scout",
                [(try_begin),(eq, "$g_start_game_intro_job", player_starting_5_scout),(disable_menu_option),(try_end),], "A scout for the local lord",
                [
                    (assign, "$g_start_game_intro_job", player_starting_5_scout),
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),
            
            ("choice_court",
                [(try_begin),(eq, "$g_start_game_intro_job", player_starting_5_court),(disable_menu_option),(try_end),], "A court assistant",
                [
                    (assign, "$g_start_game_intro_job", player_starting_5_court),
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),
            
            ("choice_beggar",
                [(try_begin),(eq, "$g_start_game_intro_job", player_starting_5_beggar),(disable_menu_option),(try_end),], "A beggar in the streets",
                [
                    (assign, "$g_start_game_intro_job", player_starting_5_beggar),
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),
            
            ("choice_doctor",
                [(try_begin),(eq, "$g_start_game_intro_job", player_starting_5_doctor),(disable_menu_option),(try_end),], "A wandering doctor",
                [
                    (assign, "$g_start_game_intro_job", player_starting_5_doctor),
                    (jump_to_menu, "mnu_start_game_intro_5"),
                ]),

            ("continue", 
                [
                    (try_begin),
                        (eq, "$g_start_game_intro_job", -1),
                        (disable_menu_option),
                    (try_end),
                ], "Continue",
                [
                    (jump_to_menu, "mnu_start_game_intro_6"),
                ]),
        ]),
    
    ("start_game_intro_6", mnf_disable_all_keys,
        "{s0}",
        "none",
        [
            (str_store_string, s10, "str_start_game_intro_6"),
            (try_begin),
                (eq, "$g_start_game_intro_motivation", -1),
                (str_clear, s11),
            (else_try),
                (store_add, ":str", "str_start_game_intro_6_choice_wanderlust", "$g_start_game_intro_motivation"),
                (str_store_string, s11, ":str"),
            (try_end),

            (str_store_string, s0, "@{s10}^^{s11}"),
        ],
        [
            ("choice_wanderlust",
                [(try_begin),(eq, "$g_start_game_intro_motivation", player_starting_6_adventure),(disable_menu_option),(try_end),], "Wanderlust",
                [
                    (assign, "$g_start_game_intro_motivation", player_starting_6_adventure),
                    (jump_to_menu, "mnu_start_game_intro_6"),
                ]),

            ("choice_wealth",
                [(try_begin),(eq, "$g_start_game_intro_motivation", player_starting_6_gold),(disable_menu_option),(try_end),], "Lust for money and power",
                [
                    (assign, "$g_start_game_intro_motivation", player_starting_6_gold),
                    (jump_to_menu, "mnu_start_game_intro_6"),
                ]),

            ("choice_fame",
                [(try_begin),(eq, "$g_start_game_intro_motivation", player_starting_6_glory),(disable_menu_option),(try_end),], "The promise of fame",
                [
                    (assign, "$g_start_game_intro_motivation", player_starting_6_glory),
                    (jump_to_menu, "mnu_start_game_intro_6"),
                ]),

            ("choice_forced",
                [(try_begin),(eq, "$g_start_game_intro_motivation", player_starting_6_forced),(disable_menu_option),(try_end),], "Being forced out of your home",
                [
                    (assign, "$g_start_game_intro_motivation", player_starting_6_forced),
                    (jump_to_menu, "mnu_start_game_intro_6"),
                ]),

            ("choice_revenge",
                [(try_begin),(eq, "$g_start_game_intro_motivation", player_starting_6_revenge),(disable_menu_option),(try_end),], "Personal revenge",
                [
                    (assign, "$g_start_game_intro_motivation", player_starting_6_revenge),
                    (jump_to_menu, "mnu_start_game_intro_6"),
                ]),

            ("choice_loss",
                [(try_begin),(eq, "$g_start_game_intro_motivation", player_starting_6_loss),(disable_menu_option),(try_end),], "The loss of a loved one",
                [
                    (assign, "$g_start_game_intro_motivation", player_starting_6_loss),
                    (jump_to_menu, "mnu_start_game_intro_6"),
                ]),

            ("continue", 
                [
                    (try_begin),
                        (eq, "$g_start_game_intro_motivation", -1),
                        (disable_menu_option),
                    (try_end),
                ], "Continue",
                [
                    (jump_to_menu, "mnu_start_game_intro_7"),
                ]),
        ]),
    
    ("start_game_intro_7", mnf_disable_all_keys,
        "{s0}",
        "none",
        [
            (str_store_string, s10, "str_start_game_intro_7"),
            (try_begin),
                (eq, "$g_start_game_intro_location", -1),
                (str_clear, s11),
            (else_try),
                (store_add, ":str", "str_start_game_intro_7_choice_swadia", "$g_start_game_intro_location"),
                (str_store_string, s11, ":str"),
            (try_end),

            (str_store_string, s0, "@{s10}^^{s11}"),
        ],
        [
            ("choice_swadia",
                [(try_begin),(eq, "$g_start_game_intro_location", player_starting_7_swadia),(disable_menu_option),(try_end),], "Join a caravan to Praven, in the Kingdom of Swadia.",
                [
                    (assign, "$g_start_game_intro_location", player_starting_7_swadia),
                    (jump_to_menu, "mnu_start_game_intro_7"),
                ]),
            ("choice_vaegir",
                [(try_begin),(eq, "$g_start_game_intro_location", player_starting_7_vaegir),(disable_menu_option),(try_end),], "Join a caravan to Reyvadin, in the Kingdom of the Vaegirs.",
                [
                    (assign, "$g_start_game_intro_location", player_starting_7_vaegir),
                    (jump_to_menu, "mnu_start_game_intro_7"),
                ]),
            ("choice_khergit",
                [(try_begin),(eq, "$g_start_game_intro_location", player_starting_7_khergit),(disable_menu_option),(try_end),], "Join a caravan to Tulga, in the Khergit Khanate.",
                [
                    (assign, "$g_start_game_intro_location", player_starting_7_khergit),
                    (jump_to_menu, "mnu_start_game_intro_7"),
                ]),
            ("choice_nord",
                [(try_begin),(eq, "$g_start_game_intro_location", player_starting_7_nord),(disable_menu_option),(try_end),], "Take a ship to Sargoth, in the Kingdom of the Nords.",
                [
                    (assign, "$g_start_game_intro_location", player_starting_7_nord),
                    (jump_to_menu, "mnu_start_game_intro_7"),
                ]),
            ("choice_rhodok",
                [(try_begin),(eq, "$g_start_game_intro_location", player_starting_7_rhodok),(disable_menu_option),(try_end),], "Take a ship to Jelkala, in the Kingdom of the Rhodoks.",
                [
                    (assign, "$g_start_game_intro_location", player_starting_7_rhodok),
                    (jump_to_menu, "mnu_start_game_intro_7"),
                ]),
            ("choice_sarranid",
                [(try_begin),(eq, "$g_start_game_intro_location", player_starting_7_sarranid),(disable_menu_option),(try_end),], "Join a caravan to Shariz, in the Sarranid Sultanate.",
                [
                    (assign, "$g_start_game_intro_location", player_starting_7_sarranid),
                    (jump_to_menu, "mnu_start_game_intro_7"),
                ]),

            ("continue", 
                [
                    (try_begin),
                        (eq, "$g_start_game_intro_location", -1),
                        (disable_menu_option),
                    (try_end),
                ], "Continue",
                [
                    (jump_to_menu, "mnu_start_game_intro_end"),
                ]),
        ]),

    ("start_game_intro_end", mnf_disable_all_keys,
        "In the next screen you will be able to create your own character, keep in mind that due to a technical limitation, you will be unable to spend skill points.",
        "none",
        [],
        [
            ("continue", 
                [], "Continue",
                [
                    (call_script, "script_player_reset_stats"),
                    (call_script, "script_player_apply_starting_choices"),
                    (change_screen_return),
                ]),
        ]),
    
    ############
    ## Quests ##
    ############
    ("quest_introduction_default_meeting", 0,
        "Before you are able to enter the city of {s10} you see a ragged man running towards you.",
        "none",
        [],
        [
            ("wait",
                [], "Wait for the man to approach.",
                [(assign, "$g_intro_quest_stance", 1),(change_screen_return),(start_map_conversation, "trp_intro_generic_peasant"),]),
            ("prepare_weapons",
                [], "Ready your weapons and prepare to strike.",
                [(assign, "$g_intro_quest_stance", 2),(change_screen_return),(start_map_conversation, "trp_intro_generic_peasant"),]),
        ]),


    ###########
    ## Other ##
    ###########
    ("settings", 0,
        "Change the settings",
        "none",
        [],
        [
            ("settings_faction_color",
                [
                    (try_begin),
                        (eq, "$g_normalize_faction_color", 1),
                        (str_store_string, s10, "@consolidated"),
                    (else_try),
                        (str_store_string, s10, "@unique"),
                    (try_end),
                ], "Faction color ({s10})",
                [
                    (val_add, "$g_normalize_faction_color", 1),
                    (val_mod, "$g_normalize_faction_color", 2),
                    (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
                        (call_script, "script_faction_update_color", ":faction_no"),
                    (try_end),
                    (jump_to_menu, "mnu_settings"),
                ]),

            ("settings_autosort_options", [], "Autosort options",
                [
                    (jump_to_menu, "mnu_settings_autosort"),
                ]),

            ("setting_shield",
                [], "Shield painting",
                [(start_presentation, "prsnt_setting_shield_painting"),]),
            ("setting_weather",
                [], "Weather",
                [(start_presentation, "prsnt_setting_weather"),]),
            ("setting_morale",
                [], "Morale",
                [(start_presentation, "prsnt_setting_morale"),]),
            ("setting_death",
                [], "Death",
                [(start_presentation, "prsnt_setting_death"),]),
            ("setting_losing",
                [], "Losing",
                [(start_presentation, "prsnt_setting_losing"),]),
            ("setting_difficulty",
                [], "Difficulty",
                [(start_presentation, "prsnt_setting_difficulty"),]),
            ("setting_misc",
                [], "Misc. settings",
                [(start_presentation, "prsnt_setting_misc"),]),
            ("setting_go_back",
                [], "Go back",
                [(jump_to_menu, "mnu_camp"),]),
        ]),

    ("debug_settings", 0,
        "Change the debug settings",
        "none",
        [],
        [
            ("debug_simple",
                [(try_begin),(eq, "$debug", debug_simple),(disable_menu_option),(try_end),
                ], "Set debug level to simple",
                [(assign, "$debug", debug_simple),(jump_to_menu, "mnu_debug_settings"),]),
            ("debug_economy",
                [(try_begin),(eq, "$debug", debug_economy),(disable_menu_option),(try_end),
                ],"Set debug level to economy",
                [(assign, "$debug", debug_economy),(jump_to_menu, "mnu_debug_settings"),]),
            ("debug_ai",
                [(try_begin),(eq, "$debug", debug_ai),(disable_menu_option),(try_end),
                ],"Set debug level to ai",
                [(assign, "$debug", debug_ai),(jump_to_menu, "mnu_debug_settings"),]),
            ("debug_war",
                [(try_begin),(eq, "$debug", debug_war),(disable_menu_option),(try_end),
                ],"Set debug level to war",
                [(assign, "$debug", debug_war),(jump_to_menu, "mnu_debug_settings"),]),
            ("debug_faction",
                [(try_begin),(eq, "$debug", debug_faction),(disable_menu_option),(try_end),
                ],"Set debug level to faction",
                [(assign, "$debug", debug_faction),(jump_to_menu, "mnu_debug_settings"),]),
            ("debug_trade",
                [(try_begin),(eq, "$debug", debug_trade),(disable_menu_option),(try_end),
                ],"Set debug level to trade",
                [(assign, "$debug", debug_trade),(jump_to_menu, "mnu_debug_settings"),]),
            ("debug_all",
                [(try_begin),(eq, "$debug", debug_all),(disable_menu_option),(try_end),
                ],"Set debug level to all",
                [(assign, "$debug", debug_all),(jump_to_menu, "mnu_debug_settings"),]),
            ("debug_disable",
                [(try_begin),(eq, "$debug", 0),(disable_menu_option),(try_end),
                ],"Disable debug mode",
                [(assign, "$debug", 0),(jump_to_menu, "mnu_debug_settings"),]),
            ("debug_return",
                [], "Go back",
                [(jump_to_menu, "mnu_camp"),]),
        ]),

    ("debug_menu", 0,
        "Debug commands",
        "none",
        [],
        [
            ("debug_disable_ai",
                [(neq, "$g_disable_ai", 1)],"Disable ais",
                [(assign, "$g_disable_ai", 1),(jump_to_menu, "mnu_debug_menu"),]),
            ("debug_enable_ai",
                [(eq, "$g_disable_ai", 1)],"Enable ais",
                [(assign, "$g_disable_ai", 0),(jump_to_menu, "mnu_debug_menu"),]),

            ("debug_disable_faction_ai",
                [(neq, "$g_disable_faction_ai", 1)],"Disable faction ais",
                [(assign, "$g_disable_faction_ai", 1),(jump_to_menu, "mnu_debug_menu"),]),
            ("debug_enable_faction_ai",
                [(eq, "$g_disable_faction_ai", 1)],"Enable faction ais",
                [(assign, "$g_disable_faction_ai", 0),(jump_to_menu, "mnu_debug_menu"),]),


            ("debug_increase_haze",
                [(assign, reg10, "$g_global_haze_amount"),],"Increase Haze ({reg10})",
                [
                    (val_add, "$g_global_haze_amount", 10),
                    (val_min, "$g_global_haze_amount", 100),
                    (assign, reg10, "$g_global_haze_amount"),
                    (display_message, "@Global haze: {reg10}"),
                    (jump_to_menu, "mnu_debug_menu"),
                ]),
            ("debug_decrease_haze",
                [(assign, reg10, "$g_global_haze_amount"),],"Decrease Haze ({reg10})",
                [
                    (val_add, "$g_global_haze_amount", -10),
                    (val_max, "$g_global_haze_amount", 0),
                    (assign, reg10, "$g_global_haze_amount"),
                    (display_message, "@Global haze: {reg10}"),
                    (jump_to_menu, "mnu_debug_menu"),
                ]),
            ("debug_increase_cloud",
                [(assign, reg10, "$g_global_cloud_amount"),],"Increase Cloud ({reg10})",
                [
                    (val_add, "$g_global_cloud_amount", 10),
                    (val_min, "$g_global_cloud_amount", 100),
                    (assign, reg10, "$g_global_cloud_amount"),
                    (display_message, "@Global cloud: {reg10}"),
                    (jump_to_menu, "mnu_debug_menu"),
                ]),
            ("debug_decrease_cloud",
                [(assign, reg10, "$g_global_cloud_amount"),],"Decrease Cloud ({reg10})",
                [
                    (val_add, "$g_global_cloud_amount", -10),
                    (val_max, "$g_global_cloud_amount", 0),
                    (assign, reg10, "$g_global_cloud_amount"),
                    (display_message, "@Global cloud: {reg10}"),
                    (jump_to_menu, "mnu_debug_menu"),
                ]),
            ("debug_return",
                [], "Go back",
                [(jump_to_menu, "mnu_camp"),]),
        ]),

    ("debug_actions", 0,
        "Debug actions",
        "none",
        [],
        [
            ("camp_siege_battle", [(call_script, "script_cf_debug", debug_all),], "Start a siege battle",
                [
                    (jump_to_menu, "mnu_siege_battle_select"),
                ]),
            
            ("camp_test_face_keys", [(call_script, "script_cf_debug", debug_all),], "Test Face Keys",
                [
                    (call_script, "script_troop_get_face_code", "$g_player_troop"),
                    (troop_set_face_keys, "$g_player_troop", s0),
                    (display_message, "@Face key: {s0}"),
                ]),
            
            ("camp_test_battle_plain", [(call_script, "script_cf_debug", debug_all),], "Go to plain battle test",
                [
                    (store_random_in_range, ":scene", "scn_test_battle_plain", castle_scene_begin),
                    (assign, "$g_player_team", 0),
                    (set_jump_mission, "mt_battle_test_plain"),
                    (jump_to_scene, ":scene"),
                    (change_screen_mission),
                ]),
            
            ("camp_test_stats", [(call_script, "script_cf_debug", debug_all),], "Display stats",
                [
                    (jump_to_menu, "mnu_test_stats"),
                ]),
            
            ("camp_test_faction_relations", [(call_script, "script_cf_debug", debug_all),], "Modify faction relations",
                [
                    (jump_to_menu, "mnu_test_faction_relations"),
                ]),
                
            ("camp_test_join_faction", [(call_script, "script_cf_debug", debug_all),], "Join a faction",
                [
                    (store_faction_of_party, "$g_test_player_faction", "$g_player_party"),
                    (jump_to_menu, "mnu_test_faction_join"),
                ]),

            ("go_back",
                [], "Go back",
                [(jump_to_menu, "mnu_camp"),]),
        ]),

    ("test_stats", 0,
        "Display stats",
        "none",
        [],
        [
            ("debug_garrison_size_stats",
                [],"Garrison size stats",
                [
                    (jump_to_menu, "mnu_test_stats"),
                ]),
            ("debug_garrison_wages_stats",
                [],"Garrison wages stats",
                [
                    (jump_to_menu, "mnu_test_stats"),
                ]),

            ("debug_center_taxes_stats",
                [],"Center taxes stats",
                [
                    (jump_to_menu, "mnu_test_stats"),
                ]),
            ("debug_center_trade_stats",
                [],"Center trade stats",
                [
                    (jump_to_menu, "mnu_test_stats"),
                ]),
            ("debug_center_population_stats",
                [],"Center population stats",
                [
                    (jump_to_menu, "mnu_test_stats"),
                ]),
            ("debug_center_wealth_stats",
                [],"Center wealth stats",
                [
                    (jump_to_menu, "mnu_test_stats"),
                ]),

            ("debug_lord_wealth_stats",
                [],"Lord wealth stats",
                [
                    (jump_to_menu, "mnu_test_stats"),
                ]),

            ("debug_return",
                [], "Go back",
                [(jump_to_menu, "mnu_camp"),]),
        ]),
    
    ("test_faction_relations", 0,
        "Modify the faction relations",
        "none",
        [],
        [
            ("faction_1", 
                [
                    (try_begin),
                        (neg|is_between, "$test_faction_1", kingdoms_begin, kingdoms_end),
                        (assign, "$test_faction_1", kingdoms_begin),
                    (try_end),
                    (str_store_faction_name, s10, "$test_faction_1"),
                ], "Faction 1: {s10}",
                [
                    (val_add, "$test_faction_1", 1),
                    (try_begin),
                        (ge, "$test_faction_1", kingdoms_end),
                        (assign, "$test_faction_1", kingdoms_begin),
                    (try_end),
                ]),
            
            ("faction_2", 
                [
                    (try_begin),
                        (neg|is_between, "$test_faction_2", kingdoms_begin, kingdoms_end),
                        (assign, "$test_faction_2", kingdoms_begin),
                    (try_end),
                    (str_store_faction_name, s11, "$test_faction_2"),
                ], "Faction 2: {s11}",
                [
                    (val_add, "$test_faction_2", 1),
                    (try_begin),
                        (ge, "$test_faction_2", kingdoms_end),
                        (assign, "$test_faction_2", kingdoms_begin),
                    (try_end),
                ]),
            
            ("declare_war", 
                [
                    (try_begin),
                        (eq, "$test_faction_1", "$test_faction_2"),
                        (str_store_string, s12, "@Factions are identical!"),
                        (disable_menu_option),
                    (else_try),
                        (store_relation, ":relation", "$test_faction_1", "$test_faction_2"),
                        (lt, ":relation", relation_state_war),
                        (str_store_string, s12, "@Factions are already at war"),
                        (disable_menu_option),
                    (else_try),
                        (str_store_string, s12, "@Declare war"),
                    (try_end),
                ], "{s12}", 
                [
                    (call_script, "script_faction_declare_war_to_faction", "$test_faction_1", "$test_faction_2", -1),
                ]),
            ("make_peace", 
                [
                    (try_begin),
                        (eq, "$test_faction_1", "$test_faction_2"),
                        (str_store_string, s13, "@Factions are identical!"),
                        (disable_menu_option),
                    (else_try),
                        (store_relation, ":relation", "$test_faction_1", "$test_faction_2"),
                        # (lt, ":relation", relation_state_friendly),
                        (gt, ":relation", relation_state_war),
                        (str_store_string, s13, "@Factions are already at peace"),
                        (disable_menu_option),
                    (else_try),
                        (store_relation, ":relation", "$test_faction_1", "$test_faction_2"),
                        (lt, ":relation", relation_state_war),
                        (call_script, "script_war_find_from_participants", "$test_faction_1", "$test_faction_2"),
                        (eq, reg0, -1),
                        (str_store_string, s13, "@Factions are not the main war participants"),
                        (disable_menu_option),
                    (else_try),
                        (str_store_string, s13, "@Make peace"),
                    (try_end),
                ], "{s13}", 
                [
                    (call_script, "script_war_find_from_participants", "$test_faction_1", "$test_faction_2"),
                    (assign, ":storage", reg0),
                    (call_script, "script_faction_make_peace_to_faction", "$test_faction_1", "$test_faction_2", ":storage"),
                    (call_script, "script_war_clean", ":storage"),
                ]),
            ("make_alliance", 
                [
                    (try_begin),
                        (eq, "$test_faction_1", "$test_faction_2"),
                        (str_store_string, s14, "@Factions are identical!"),
                        (disable_menu_option),
                    (else_try),
                        (store_relation, ":relation", "$test_faction_1", "$test_faction_2"),
                        (le, ":relation", relation_state_war),
                        (str_store_string, s14, "@Cannot make allies out of enemies"),
                        (disable_menu_option),
                    (else_try),
                        (store_relation, ":relation", "$test_faction_1", "$test_faction_2"),
                        (ge, ":relation", relation_state_friendly),
                        (str_store_string, s14, "@Factions are already allies"),
                        (disable_menu_option),
                    (else_try),
                        (str_store_string, s14, "@Make an alliance"),
                    (try_end),
                ], "{s14}", 
                [
                    (call_script, "script_faction_create_treaty", "$test_faction_1", "$test_faction_2", sfkt_alliance), # Make allies
                ]),
            
            ("back",[], "Back to camp",
                [
                    (jump_to_menu, "mnu_camp"),
                ]),
        ]),
    
    ("siege_battle_select", mnf_scale_picture,
        "Select a siege scene, cur scene: scene {reg10} {s10}",
        "none",
        [
            (try_begin),
                (neg|is_between, "$g_cur_selected", castle_scene_begin, castle_scene_end),
                (assign, "$g_cur_selected", castle_scene_begin),
            (try_end),

            (store_sub, reg10, "$g_cur_selected", castle_scene_begin),
            (store_add, ":str_id", reg10, "str_castle_name_plain_01"),
            (str_store_string, s10, ":str_id"),
        ],
        [
            ("scene_select_plus", [], "Select next scene",
                [
                    (val_add, "$g_cur_selected", 1),
                    (try_begin),
                        (ge, "$g_cur_selected", castle_scene_end),
                        (assign, "$g_cur_selected", castle_scene_begin),
                    (try_end),
                    (store_sub, reg10, "$g_cur_selected", castle_scene_begin),
                ]),
            
            ("scene_select_minus", [], "Select previous scene",
                [
                    (try_begin),
                        (le, "$g_cur_selected", castle_scene_begin),
                        (assign, "$g_cur_selected", castle_scene_end),
                    (try_end),
                    (val_add, "$g_cur_selected", -1),
                    (store_sub, reg10, "$g_cur_selected", castle_scene_begin),
                ]),
            
            ("camp_test_battle", [], "Jump to battle",
                [
                    (try_begin),
                        (is_between, "$g_cur_selected", castle_scene_begin, castle_scene_end),
                        (set_jump_mission, "mt_battle_test_siege"),
                        (jump_to_scene, "$g_cur_selected"),
                        (change_screen_mission),
                    (else_try),
                        (display_message, "@Invalid scene ID!", 0xee0000),
                    (try_end),
                ]),
            
            ("back",[], "Back to camp",
                [
                    (jump_to_menu, "mnu_camp"),
                ]),
        ]),
    
    ("test_faction_join", mnf_scale_picture,
        "You are lord of {s11}^Join the {s12} as a {s10}",
        "none",
        [
            (str_store_troop_name, s10, "$g_test_player_troop"),
            (store_faction_of_party, ":faction", "$g_player_party"),
            (str_store_faction_name, s11, ":faction"),
            (str_store_faction_name, s12, "$g_test_player_faction"),
        ],
        [
            ("join_next_faction", [], "Next faction",
                [
                    (val_add, "$g_test_player_faction", 1),
                    (try_begin),
                        (ge, "$g_test_player_faction", kingdoms_end),
                        (assign, "$g_test_player_faction", kingdoms_begin),
                    (try_end),
                    (jump_to_menu, "mnu_test_faction_join"),
                ]),
            ("join_previous_faction", [], "Previous faction",
                [
                    (try_begin),
                        (le, "$g_test_player_faction", kingdoms_begin),
                        (assign, "$g_test_player_faction", kingdoms_end),
                    (try_end),
                    (val_add, "$g_test_player_faction", -1),
                    (jump_to_menu, "mnu_test_faction_join"),
                ]),
            ("join_increase_lord", 
                [
                    (faction_get_slot, ":culture", "$g_test_player_faction", slot_faction_culture),
                    (faction_get_slot, ":template_begin", ":culture", slot_faction_template_troops_begin),
                    (store_add, ":template_end", ":template_begin", 7),
                    (try_begin),
                        (ge, "$g_test_player_troop", ":template_end"),
                        (disable_menu_option),
                    (try_end),
                ], "Increase rank",
                [
                    (faction_get_slot, ":culture", "$g_test_player_faction", slot_faction_culture),
                    (faction_get_slot, ":template_begin", ":culture", slot_faction_template_troops_begin),
                    (try_begin),
                        (lt, "$g_test_player_troop", ":template_begin"),
                        (assign, "$g_test_player_troop", ":template_begin"),
                    (else_try),
                        (val_add, "$g_test_player_troop", 1),
                    (try_end),
                    (jump_to_menu, "mnu_test_faction_join"),
                ]),
            ("join_decrease_lord", 
                [
                    (faction_get_slot, ":culture", "$g_test_player_faction", slot_faction_culture),
                    (faction_get_slot, ":template_begin", ":culture", slot_faction_template_troops_begin),
                    # (store_add, ":template_end", ":template_begin", 7),
                    (try_begin),
                        (le, "$g_test_player_troop", ":template_begin"),
                        (disable_menu_option),
                    (try_end),
                ], "Decrease rank",
                [
                    (faction_get_slot, ":culture", "$g_test_player_faction", slot_faction_culture),
                    (faction_get_slot, ":template_begin", ":culture", slot_faction_template_troops_begin),
                    (store_add, ":template_end", ":template_begin", 7),
                    (try_begin),
                        (gt, "$g_test_player_troop", ":template_end"),
                        (assign, "$g_test_player_troop", ":template_end"),
                    (else_try),
                        (val_add, "$g_test_player_troop", -1),
                    (try_end),
                    (jump_to_menu, "mnu_test_faction_join"),
                ]),
            ("join_accept", [], "Join",
                [
                    (call_script, "script_troop_use_template_troop", "$g_player_troop", "$g_test_player_troop"),
                    (party_set_faction, "$g_player_party", "$g_test_player_faction"),
                    (try_for_range, ":unused", 0, 10),
                        (call_script, "script_party_add_reinforcements", "$g_player_party"),
                    (try_end),
                    (troop_set_faction, "$g_player_troop", "$g_test_player_faction"),

                    (display_message, "@Joined!"),
                    (jump_to_menu, "mnu_test_faction_join"),
                ]),
            ("join_accept_no_change", [], "Join (no player change)",
                [
                    (party_set_faction, "$g_player_party", "$g_test_player_faction"),
                    (troop_set_faction, "$g_player_troop", "$g_test_player_faction"),

                    (try_for_range, ":unused", 0, 10),
                        (call_script, "script_party_add_reinforcements", "$g_player_party"),
                    (try_end),

                    (display_message, "@Joined!"),
                    (jump_to_menu, "mnu_test_faction_join"),
                ]),

            ("join_era", [(faction_get_slot, reg10, "fac_kingdom_1", slot_faction_era),], "Increase era (current era: {reg10})",
                [
                    (faction_get_slot, ":era", "fac_kingdom_1", slot_faction_era),
                    (val_add, ":era", 1),
                    (try_begin),
                        (gt, ":era", 10),
                        (assign, ":era", 0),
                    (try_end),
                    (call_script, "script_get_current_day"),
                    (assign, ":current_day", reg0),
                    (try_for_range, ":faction", kingdoms_begin, kingdoms_end),
                        (faction_set_slot, ":faction", slot_faction_era, ":era"),
                        (faction_set_slot, ":faction", slot_faction_era_time, ":current_day"),
                    (try_end),
                    (jump_to_menu, "mnu_test_faction_join"),
                ]),

            ("go_back", [], "Go back",
                [
                    (jump_to_menu, "mnu_camp"),
                ]),
        ]),

    ("camp_actions", mnf_scale_picture,
        "Take an action",
        "none", [],
        [
            ("camp_wait_here", [], "Rest",
                [
                    (rest_for_hours_interactive, 24 * 365, 5, 1),
                    (change_screen_return),
                    (change_screen_map),
                ]),

            ("camp_gather_vassals",
                [
                    (troop_get_slot, ":gathering", "$g_player_troop", slot_troop_gathering),
                    (try_begin),
                        (eq, ":gathering", 0),
                        (str_store_string, s10, "@Off"),
                    (else_try),
                        (str_store_string, s10, "@On"),
                    (try_end),
                ], "Gather vassals ({s10})",
                [
                    (troop_get_slot, ":gathering", "$g_player_troop", slot_troop_gathering),
                    (store_sub, ":gathering", 1, ":gathering"),
                    (troop_set_slot, "$g_player_troop", slot_troop_gathering, ":gathering"),
                    (try_begin),
                        (eq, ":gathering", 0),
                        (display_message, "@Leaving vassals to their business...", text_color_info),
                    (else_try),
                        (display_message, "@Gathering vassals...", text_color_info),
                    (try_end),

                ]),

            ("camp_train_levies", [(disable_menu_option),], "Initiate a training session",
                [
                    # ToDo: training
                    # Training allows player to duel his companions/troops
                    # Also allows to train recruits if player/companion has at least 1 point in trainer
                    # Trained recruits will most likely end up being the troop type trained by the different trainings
                    # Available trainings:
                    #   horseback
                    #   lancing
                    #   spear cavalry (only rhodoks, swadians-iven and nords-rizi)
                    #   ranged (bow or crossbow depending on faction)
                    #   horse archery
                    #   melee fights (shield and sword)
                    #   melee fights (shield and spear)
                    #   melee fights (two handed swords)
                    #   skirmishing (throwing weapons)
                    #   mounted skirmishing (throwing weapons)
                    # (jump_to_menu, "mnu_levy_train"),
                ]),
            
            ("go_back",
                [], "Go back",
                [(jump_to_menu, "mnu_camp"),]),
        ]),

    ("settings_autosort",mnf_scale_picture,
        "Customize the way autosort works",
        "none", [],
        [
            ("autosort_level", 
                [
                    (party_get_slot, ":autosort_options", "$g_player_party", slot_party_autosort_options),
                    (store_and, ":autosort_level", ":autosort_options", autosort_level_flag),

                    (try_begin),
                        (eq, ":autosort_level", autosort_low_level_first),
                        (str_store_string, s11, "@Low level troops first"),
                    (else_try),
                        (eq, ":autosort_level", autosort_high_level_first),
                        (str_store_string, s11, "@High level troops first"),
                    (else_try),
                        (str_store_string, s11, "@No level sorting"),
                    (try_end),
                ], "Set autosort level options: {s11}",
                [
                    (party_get_slot, ":autosort_options", "$g_player_party", slot_party_autosort_options),
                    (store_and, ":autosort_level", ":autosort_options", autosort_level_flag),

                    (assign, ":level_options", autosort_no_sort),
                    (try_begin),
                        (eq, ":autosort_level", autosort_low_level_first),
                        (assign, ":level_options", autosort_high_level_first),
                    (else_try),
                        (eq, ":autosort_level", autosort_high_level_first),
                        (assign, ":level_options", autosort_no_sort),
                    (else_try),
                        (assign, ":level_options", autosort_low_level_first),
                    (try_end),

                    (store_and, ":new_options", ":autosort_options", autosort_level_clearer),
                    (val_or, ":new_options", ":level_options"),

                    (party_set_slot, "$g_player_party", slot_party_autosort_options, ":new_options"),

                    (jump_to_menu, "mnu_settings_autosort"),
                ]),
            ("autosort_culture",
                [
                    (party_get_slot, ":autosort_options", "$g_player_party", slot_party_autosort_options),
                    (store_and, ":autosort_culture", ":autosort_options", autosort_culture_flag),

                    (try_begin),
                        (eq, ":autosort_culture", autosort_foreign_first),
                        (str_store_string, s12, "@Foreign troops first"),
                    (else_try),
                        (eq, ":autosort_culture", autosort_local_first),
                        (str_store_string, s12, "@Local troops first"),
                    (else_try),
                        (str_store_string, s12, "@No culture sorting"),
                    (try_end),
                ], "Set autosort culture options: {s12}",
                [
                    (party_get_slot, ":autosort_options", "$g_player_party", slot_party_autosort_options),
                    (store_and, ":autosort_culture", ":autosort_options", autosort_culture_flag),

                    (assign, ":culture_options", autosort_no_sort),
                    (try_begin),
                        (eq, ":autosort_culture", autosort_foreign_first),
                        (assign, ":culture_options", autosort_local_first),
                    (else_try),
                        (eq, ":autosort_culture", autosort_local_first),
                        (assign, ":culture_options", autosort_no_sort),
                    (else_try),
                        (assign, ":culture_options", autosort_foreign_first),
                    (try_end),

                    (store_and, ":new_options", ":autosort_options", autosort_culture_clearer),
                    (val_or, ":new_options", ":culture_options"),

                    (party_set_slot, "$g_player_party", slot_party_autosort_options, ":new_options"),

                    (jump_to_menu, "mnu_settings_autosort"),
                ]),
            ("autosort_back", [], "Back to camp",
                [
                    (jump_to_menu, "mnu_camp"),
                ]),
        ]),
    
    ("town", mnf_scale_picture,
        "You come near the gates of {s10}^You see the guards looking at you carefully",
        "none",
        [
            (str_store_party_name, s10, "$g_encountered_party"),
            (set_background_mesh, "mesh_pic_camp"),


            (try_begin),
                (call_script, "script_cf_debug", debug_economy|debug_simple),
                (party_get_slot, reg10, "$g_encountered_party", slot_party_wealth),
                (display_message, "@Town wealth : {reg10}"),
                (party_get_slot, reg10, "$g_encountered_party", slot_party_population),
                (party_get_slot, reg12, "$g_encountered_party", slot_party_population_noble),
                (party_get_slot, reg13, "$g_encountered_party", slot_party_population_artisan),
                (party_get_slot, reg14, "$g_encountered_party", slot_party_population_slave),
                (display_message, "@Town population {reg12} noble - {reg13} artisan - {reg10} common - {reg14} slave"),

                (call_script, "script_party_get_wages", "$g_encountered_party"),
                (assign, reg15, reg0),
                (display_message, "@Garrison wages: {reg15}"),

                (call_script, "script_party_get_prefered_wages_limit", "$g_encountered_party"),
                (assign, reg16, reg0),
                (display_message, "@Wanted wages: {reg16}"),

                (call_script, "script_party_get_expected_taxes", "$g_encountered_party"),
                (assign, reg17, reg0),
                (display_message, "@Expected taxes: {reg17}"),

                (call_script, "script_party_get_tax_penalties", "$g_encountered_party"),
                (assign, reg18, reg0),
                (display_message, "@Tax penalties: {reg18}"),

                (party_get_slot, ":total_res", "$g_encountered_party", slot_party_total_resources),
                (str_store_party_name, s12, "$g_encountered_party"),
                
                (assign, reg11, ":total_res"),
                (display_log_message, "@{s12} has {reg11} resources"),

                (party_get_slot, ":party_lord", "$g_encountered_party", slot_party_lord),
                (try_begin),
                    (ge, ":party_lord", 0),
                    (str_store_troop_name, s13, ":party_lord"),
                (else_try),
                    (str_store_string, s13, "@no lord"),
                (try_end),
                (display_message, "@Town lord: {s13}"),

                (party_get_slot, ":party_linked_party", "$g_encountered_party", slot_party_linked_party),
                (try_begin),
                    (ge, ":party_linked_party", 0),
                    (str_store_party_name, s14, ":party_linked_party"),
                (else_try),
                    (str_store_string, s14, "@no linked party"),
                (try_end),
                (display_message, "@Linked party: {s14}"),

                (party_get_slot, reg19, "$g_encountered_party", slot_party_reserved),
                (display_message, "@Reserved! {reg19}"),
            (try_end),
            (try_begin),
                (call_script, "script_cf_debug", debug_economy|debug_trade),
                (try_for_range, ":good", goods_begin, goods_end),
                    (store_sub, ":offset", ":good", goods_begin),

                    (store_add, ":amount_slot", slot_party_ressources_current_amount_begin, ":offset"),
                    (store_add, ":produced_slot", slot_party_item_last_produced_begin, ":offset"),
                    (store_add, ":consumed_slot", slot_party_item_consumed_begin, ":offset"),
                    (store_add, ":production_slot", slot_party_ressources_begin, ":offset"),

                    (party_get_slot, reg10, "$g_encountered_party", ":amount_slot"),
                    (party_get_slot, reg11, "$g_encountered_party", ":produced_slot"),
                    (party_get_slot, reg12, "$g_encountered_party", ":consumed_slot"),
                    (party_get_slot, reg13, "$g_encountered_party", ":production_slot"),
                    # (gt, reg10, 0),
                    (str_store_item_name, s11, ":good"),
                    (str_store_party_name, s12, "$g_encountered_party"),
                    (display_message, "@{s12} - {s11}: {reg10} stored - {reg11} prod - {reg12} cons - {reg13}"),
                (try_end),
                (party_get_slot, reg12, "$g_encountered_party", slot_party_weather_wet),
                (party_get_slot, reg13, "$g_encountered_party", slot_party_weather_heat),
                (display_message, "@{s12} has weather (humidity: {reg12} / heat: {reg13})"),
            (try_end),
        ],
        [
            ("center_enter", [], "Ask permition to enter",
                [
                    (try_begin),
                        (check_quest_active, "qst_introduction_default"),
                        (quest_get_slot, ":destination", "qst_introduction_default", slot_quest_destination),
                        (eq, "$g_encountered_party", ":destination"),
                        (jump_to_menu, "mnu_quest_introduction_default_meeting"),
                    (else_try),
                        (jump_to_menu,"mnu_town_center"),
                    (try_end),
                ]),
            
            ("center_meet_leader", [(disable_menu_option),], "Ask for an audience with the leader of the garrison",
                [
                    #TODO: meet leader
                ]),
            
            ("center_besiege", [], "Besiege the center",
                [
                    (call_script, "script_party_besiege_party", "$g_player_party", "$g_encountered_party"),
                    (jump_to_menu, "mnu_town_siege"),
                ]),
            
            ("center_cheat_switch_faction",
                [
                    (call_script, "script_cf_debug", debug_all),
                    (party_get_slot, ":faction", "$g_encountered_party", slot_party_faction),
                    (store_faction_of_party, ":current_faction", "$g_encountered_party"),
                    (neq, ":faction", ":current_faction"),
                ], "|Cheat| Switch center faction to occupier",
                [
                    (store_faction_of_party, ":current_faction", "$g_encountered_party"),
                    (call_script, "script_center_change_faction", "$g_encountered_party", ":current_faction", 1),
                    (jump_to_menu, "mnu_town"),
                ]),
            
            #ToDo: attack the guards (if villages)
            
            ("center_leave", [], "Leave center",
                [
                    # (leave_encounter),
                    (change_screen_return),
                    (change_screen_map),
                ]),
        ]),
    
    ("town_center", mnf_scale_picture,
        "{s10}",
        "none",
        [
            (set_background_mesh, "mesh_pic_camp"),
            
            (str_store_party_name, s11,"$g_encountered_party"),
            (str_store_string, s10, "@You are inside the walls of the city of {s11}. The streets are busy with merchants and the townsfolk seem well fed."),
        ],
        [
            ("center_keep", [], "Head to the keep",
                [
                    (jump_to_menu,"mnu_town_keep"),
                ]),
            
            ("center_guildmaster", 
                [(disable_menu_option),
                    (party_slot_eq,"$g_encountered_party", slot_party_type, spt_town),
                ], "Speak to the guildmaster",
                [
                    #ToDo: guildmaster
                ]),
            
            ("center_elder",
                [
                    (party_slot_eq,"$g_encountered_party", slot_party_type, spt_village),
                ], "Speak to the village elder",
                [
                    (start_map_conversation, "trp_village_elder"),
                ]),
            
            ("center_market", [], "Go to the marketplace",
                [
                    (jump_to_menu, "mnu_town_market"),
                ]),
            
            ("center_bank", 
                [
                    (call_script, "script_cf_party_has_building", "$g_encountered_party", "itm_building_bank"),
                ], "Go to the bank",
                [
                    (jump_to_menu, "mnu_town_bank"),
                ]),
            
            ("center_inn", 
                [(disable_menu_option),
                    (neg|party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                ], "Go to the inn",
                [
                    #ToDo: inn
                ]),
            
            ("center_tavern", 
                [(disable_menu_option),
                    (party_slot_eq, "$g_encountered_party", slot_party_type, spt_town),
                ], "Go to the tavern",
                [
                    #ToDo: tavern
                ]),
            
            ("center_leave", [], "Leave center",
                [
                    # (leave_encounter),
                    (change_screen_return),
                    (change_screen_map),
                ]),
        ]),
    
    ("town_keep", mnf_scale_picture,
        "You are in the political and military section of the center",
        "none",
        [
            (set_background_mesh, "mesh_pic_camp"),
            
        ],
        [
            ("center_manage_clan", [(party_slot_eq, "$g_encountered_party", slot_party_leader, "$g_player_troop"),(troop_slot_eq, "$g_player_troop", slot_troop_home, "$g_encountered_party"),], "Manage clan",
                [
                    (start_presentation, "prsnt_clan_management"),
                ]),

            ("center_manage", [(party_slot_eq, "$g_encountered_party", slot_party_leader, "$g_player_troop"),], "Manage the center",
                [
                    (jump_to_menu, "mnu_town_manage"),
                ]),
            
            ("center_hall", [(disable_menu_option),], "Go to the main hall",
                [
                    #ToDo: hall
                ]),
            
            ("center_recruit",
                [
                    (store_faction_of_party, ":current_faction", "$g_encountered_party"),
                    (party_get_slot, ":original_faction", "$g_encountered_party", slot_party_faction),
                    (store_troop_faction, ":player_faction", "$g_player_party"),
                    (try_begin),
                        (neq, ":current_faction", ":original_faction"),
                        (neq, ":current_faction", ":player_faction"),
                        (disable_menu_option),
                        (str_store_string, s10, "@Recruitment unavailable due to occupation"),
                    (else_try),
                        (str_store_string, s10, "@Recruit troops"),
                    (try_end),
                ], "{s10}",
                [
                    (assign, "$temp", "$g_encountered_party"),
                    (start_presentation, "prsnt_recruit_from_town_garrison"),
                ]),
            
            ("center_raise_levies", [(neg|party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),], "Raise levies",
                [
                    (jump_to_menu, "mnu_town_raise_levies"),
                ]),
            
            ("center_back", [], "Head back to the center",
                [
                    (jump_to_menu, "mnu_town_center"),
                ]),
            
            ("center_leave", [], "Leave center",
                [
                    # (leave_encounter),
                    (change_screen_return),
                    (change_screen_map),
                ]),
        ]),
    
    ("town_market", mnf_scale_picture,
        "You see all sorts of shops around you^What do you wish to buy?",
        "none",
        [
            (set_background_mesh, "mesh_pic_camp"),
            (call_script, "script_party_update_merchants", "$g_encountered_party"),
            (assign, "$g_trading", 0),
        ],
        [
            ("center_buy_goods",
                [
                    (call_script, "script_cf_party_has_merchant", "$g_encountered_party", merchant_type_goods),
                ], "Buy goods",
                [
                    (assign, "$g_trading", 1),
                    (call_script, "script_cf_party_has_merchant", "$g_encountered_party", merchant_type_goods),
                    (change_screen_trade, reg0),
                ]),
            
            ("center_buy_weapons", 
                [
                    (call_script, "script_cf_party_has_merchant", "$g_encountered_party", merchant_type_weapon),
                ], "Buy weapons",
                [
                    (assign, "$g_trading", 1),
                    (call_script, "script_cf_party_has_merchant", "$g_encountered_party", merchant_type_weapon),
                    (change_screen_trade, reg0),
                ]),
            
            ("center_buy_armors", 
                [
                    (call_script, "script_cf_party_has_merchant", "$g_encountered_party", merchant_type_armor),
                ], "Buy armors",
                [
                    (assign, "$g_trading", 1),
                    (call_script, "script_cf_party_has_merchant", "$g_encountered_party", merchant_type_armor),
                    (change_screen_trade, reg0),
                ]),
            
            ("center_buy_horses", 
                [   
                    (call_script, "script_cf_party_has_merchant", "$g_encountered_party", merchant_type_horse),
                ], "Buy horses",
                [
                    (assign, "$g_trading", 1),
                    (call_script, "script_cf_party_has_merchant", "$g_encountered_party", merchant_type_horse),
                    (change_screen_trade, reg0),
                ]),
            
            ("center_back", [], "Head back to the center",
                [
                    (jump_to_menu, "mnu_town_center"),
                ]),
        ]),

    ("town_bank", mnf_scale_picture,
        "You are in the bank of {s10}.^^You currently have {s11} in the bank.^You are expected to receive {s12} at the end of the fiscal year as interests.",
        "none",
        [
            (str_store_party_name, s10, "$g_encountered_party"),
            (party_get_slot, ":bank_amount", "$g_encountered_party", slot_party_bank_amount),
            (call_script, "script_game_get_money_text", ":bank_amount"),
            (str_store_string_reg, s11, s0),

            (call_script, "script_party_get_bank_interests", "$g_encountered_party", ":bank_amount"),
            (call_script, "script_game_get_money_text", reg0),
            (str_store_string_reg, s12, s0),
            
        ],
        [
            ("bank_deposit_all",
                [
                    (store_troop_gold, ":player_gold", "$g_player_troop"),
                    (try_begin),
                        (le, ":player_gold", 0),
                        (disable_menu_option),
                    (try_end),
                    (call_script, "script_game_get_money_text", ":player_gold"),
                ], "Deposit all ({s0})",
                [
                    (store_troop_gold, ":player_gold", "$g_player_troop"),
                    (party_get_slot, ":current_amount", "$g_encountered_party", slot_party_bank_amount),
                    (val_add, ":current_amount", ":player_gold"),
                    (party_set_slot, "$g_encountered_party", slot_party_bank_amount, ":current_amount"),
                    (troop_remove_gold, "$g_player_troop", ":player_gold"),
                    (jump_to_menu, "mnu_town_bank"),
                ]),
            ("bank_deposit_x10",
                [
                    (store_troop_gold, ":player_gold", "$g_player_troop"),
                    (try_begin),
                        (lt, ":player_gold", 10000),
                        (disable_menu_option),
                    (try_end),
                    (call_script, "script_game_get_money_text", 10000),
                ], "Deposit {s0}",
                [
                    (assign, ":player_gold", 10000),
                    (party_get_slot, ":current_amount", "$g_encountered_party", slot_party_bank_amount),
                    (val_add, ":current_amount", ":player_gold"),
                    (party_set_slot, "$g_encountered_party", slot_party_bank_amount, ":current_amount"),
                    (troop_remove_gold, "$g_player_troop", ":player_gold"),
                    (jump_to_menu, "mnu_town_bank"),
                ]),
            ("bank_deposit",
                [
                    (store_troop_gold, ":player_gold", "$g_player_troop"),
                    (try_begin),
                        (lt, ":player_gold", 1000),
                        (disable_menu_option),
                    (try_end),
                    (call_script, "script_game_get_money_text", 1000),
                ], "Deposit {s0}",
                [
                    (assign, ":player_gold", 1000),
                    (party_get_slot, ":current_amount", "$g_encountered_party", slot_party_bank_amount),
                    (val_add, ":current_amount", ":player_gold"),
                    (party_set_slot, "$g_encountered_party", slot_party_bank_amount, ":current_amount"),
                    (troop_remove_gold, "$g_player_troop", ":player_gold"),
                    (jump_to_menu, "mnu_town_bank"),
                ]),

            ("bank_withdraw",
                [
                    (party_get_slot, ":current_amount", "$g_encountered_party", slot_party_bank_amount),
                    (try_begin),
                        (lt, ":current_amount", 1000),
                        (disable_menu_option),
                    (try_end),
                    (call_script, "script_game_get_money_text", 1000),
                ], "Withdraw {s0}",
                [
                    (party_get_slot, ":current_amount", "$g_encountered_party", slot_party_bank_amount),
                    (val_sub, ":current_amount", 1000),
                    (party_set_slot, "$g_encountered_party", slot_party_bank_amount, ":current_amount"),
                    (troop_add_gold, "$g_player_troop", 1000),
                    (jump_to_menu, "mnu_town_bank"),
                ]),
            ("bank_withdraw_x10",
                [
                    (party_get_slot, ":current_amount", "$g_encountered_party", slot_party_bank_amount),
                    (try_begin),
                        (lt, ":current_amount", 10000),
                        (disable_menu_option),
                    (try_end),
                    (call_script, "script_game_get_money_text", 10000),
                ], "Withdraw {s0}",
                [
                    (party_get_slot, ":current_amount", "$g_encountered_party", slot_party_bank_amount),
                    (val_sub, ":current_amount", 10000),
                    (party_set_slot, "$g_encountered_party", slot_party_bank_amount, ":current_amount"),
                    (troop_add_gold, "$g_player_troop", 10000),
                    (jump_to_menu, "mnu_town_bank"),
                ]),

            ("bank_withdraw_all",
                [
                    (party_get_slot, ":current_amount", "$g_encountered_party", slot_party_bank_amount),
                    (try_begin),
                        (le, ":current_amount", 0),
                        (disable_menu_option),
                    (try_end),
                    (call_script, "script_game_get_money_text", ":current_amount"),
                ], "Withdraw all ({s0})",
                [
                    (party_get_slot, ":current_amount", "$g_encountered_party", slot_party_bank_amount),
                    (party_set_slot, "$g_encountered_party", slot_party_bank_amount, 0),
                    (troop_add_gold, "$g_player_troop", ":current_amount"),
                    (jump_to_menu, "mnu_town_bank"),
                ]),


            ("center_back", [], "Head back to the center",
                [
                    (jump_to_menu, "mnu_town_center"),
                ]),
        ]),
    
    ("town_raise_levies", mnf_scale_picture,
        "How many levies do you wish to raise?^^Available recruits:{s10}",
        "none",
        [
            # (val_max, "$g_num_levies", 0),
            # (assign, reg11, "$g_num_levies"),
            
            (str_clear, s10),
            
            (store_faction_of_party, ":faction", "$g_encountered_party"),
            (faction_get_slot, ":culture", ":faction", slot_faction_culture),
            (faction_get_slot, ":peasant_begin", ":culture", slot_faction_peasant_begin),
            (faction_get_slot, ":common_begin", ":culture", slot_faction_common_begin),
            
            (try_for_range, ":cur_troop", ":peasant_begin", ":common_begin"),
                (troop_get_slot, ":only_faction_1", ":cur_troop", slot_troop_faction_reserved_1),
                (troop_get_slot, ":only_faction_2", ":cur_troop", slot_troop_faction_reserved_2),
                (troop_get_slot, ":no_faction_1", ":cur_troop", slot_troop_faction_not_1),
                (troop_get_slot, ":no_faction_2", ":cur_troop", slot_troop_faction_not_2),
                (try_begin),
                    (this_or_next|eq, ":only_faction_1", -1),
                    (this_or_next|eq, ":only_faction_1", ":faction"),
                    (eq, ":only_faction_2", ":faction"),
                    (neq, ":no_faction_1", ":faction"),
                    (neq, ":no_faction_2", ":faction"),
                    (str_store_troop_name, s11, ":cur_troop"),
                    (str_store_string, s10, "@{s10}^{s11}"),
                (try_end),
            (try_end),
        ],
        [
            ("recruit_increase", [], "Increase number of recruits",
                [
                    (val_add, "$g_num_levies", 1),
                    (jump_to_menu, "mnu_town_raise_levies"),
                ]),
            
            ("recruit_decrease", [], "Decrease number of recruits",
                [
                    (val_add, "$g_num_levies", -1),
                    (jump_to_menu, "mnu_town_raise_levies"),
                ]),
            
            ("recruit_raise", 
                [
                    (val_max, "$g_num_levies", 0),
                    (assign, reg10, "$g_num_levies"),
                    # (store_mul, reg11, "$g_num_levies", train_levies_cost),

                    (store_faction_of_party, ":faction", "$g_encountered_party"),
                    (faction_get_slot, ":culture", ":faction", slot_faction_culture),
                    (faction_get_slot, ":peasant_begin", ":culture", slot_faction_peasant_begin),
                    (faction_get_slot, ":common_begin", ":culture", slot_faction_common_begin),

                    (party_clear, "p_temp_party"),
                    (party_set_faction, "p_temp_party", ":faction"),

                    (assign, ":num_levies", 1000),

                    (call_script, "script_party_add_troops", "p_temp_party", ":peasant_begin", ":common_begin", ":num_levies"),
                    (store_div, ":cost", reg1, ":num_levies"),
                    (val_mul, ":cost", "$g_num_levies"),
                    (val_div, ":cost", 5),
                    (assign, reg11, ":cost"),

                    (call_script, "script_game_get_money_text", ":cost"),
                    (str_store_string_reg, s10, s0),

                    (party_clear, "p_temp_party"),
                    (party_set_faction, "p_temp_party", ":faction"),

                    (call_script, "script_party_add_troops", "p_temp_party", ":peasant_begin", ":common_begin", "$g_num_levies"),

                    (party_set_faction, "p_temp_party", fac_commoners),
                    
                    (store_div, ":min_hours", "$g_num_levies", 10),
                    (val_add, ":min_hours", 1),
                    
                    (store_mul, ":num_levies_5", "$g_num_levies", 5),
                    
                    (store_skill_level, ":trainer", skl_trainer_2, "$g_player_troop"),
                    (store_add, ":div", 20, ":trainer"),
                    
                    (store_mul, ":sub", ":num_levies_5", ":div"),
                    (val_div, ":sub", 40),
                    (store_sub, ":rest_time", ":num_levies_5", ":sub"),
                    (val_div, ":rest_time", 3),
                    
                    (val_max, ":rest_time", ":min_hours"),
                    (assign, reg12, ":rest_time"),
                ], "Recruit {reg10} levies : {s10} ({reg12} days)",
                [
                    (try_begin),
                        (gt, "$g_num_levies", 0),
                        (store_troop_gold, ":total_gold", "$g_player_troop"),
                        # (store_mul, ":total_cost", "$g_num_levies", train_levies_cost),
                        (assign, ":total_cost", reg11),
                        (try_begin),
                            (gt, ":total_gold", ":total_cost"),

                            (distribute_party_among_party_group, "p_temp_party", "$g_player_party"),
                            (troop_remove_gold, "$g_player_troop", ":total_cost"),
                            
                            (party_clear, "p_temp_party"),
                            
                            (store_div, ":min_hours", "$g_num_levies", 10),
                            (val_add, ":min_hours", 1),
                            
                            (store_mul, ":num_levies_5", "$g_num_levies", 5),
                            
                            (store_skill_level, ":trainer", skl_trainer_2, "$g_player_troop"),
                            (store_add, ":div", 20, ":trainer"),
                    
                            (store_mul, ":sub", ":num_levies_5", ":div"),
                            (val_div, ":sub", 40),
                            (store_sub, ":rest_time", ":num_levies_5", ":sub"),
                            (val_div, ":rest_time", 3),
                            
                            (val_max, ":rest_time", ":min_hours"),
                            (assign, reg12, ":rest_time"),
                            (display_message, "@Rest time: {reg12}"),
                            (rest_for_hours, ":rest_time"),
                            
                            (assign, "$g_num_levies", 0),
                        (else_try),
                            (display_message, "@Not enough gold!", text_color_impossible),
                        (try_end),
                    (try_end),
                    (jump_to_menu, "mnu_town_raise_levies"),
                ]),
            
            ("center_back", [], "Head back to the keep",
                [
                    (jump_to_menu, "mnu_town_keep"),
                ]),
        ]),

    ("town_manage", mnf_scale_picture,
        "Here you can manage your center.",
        "none",
        [],
        [
            ("manage_administration", # Allows changing various parameters for the center
                [], "Center administration", [
                    (assign, "$temp", "$g_encountered_party"),
                    (start_presentation, "prsnt_center_administration"),
                ]),

            ("manage_buildings", # View currently built buildings, their conditions, their upkeep
                [], "Manage constructions", [
                    (assign, "$temp", "$g_encountered_party"),
                    (start_presentation, "prsnt_center_constructions"),
                ]),

            ("manage_events", # Organize tournaments, festivals, plan special events
                [(disable_menu_option),], "Manage events", []),

            # Allows automatic training, automatic reinforcements (both ways), set maximum garrison (up to real max)
            ("manage_troops", 
                [], "Manage garrison", [
                    (change_screen_exchange_members, 1, "$g_encountered_party"),
                ]),

            ("manage_return",
                [], "Go back", [(jump_to_menu, "mnu_town_keep"),]),
        ]),
    
    ("town_siege", mnf_scale_picture,
        "You are surrounding the walls of {s10}.^You can see the garrison making preparations on the battlements.",
        "none",
        [
            (str_store_party_name, s10, "$g_encountered_party"),
            (try_for_parties, ":party_no"),
                (neq, ":party_no", "$g_player_party"),
                (call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "$g_player_party"),
                (assign, ":continue", reg0),
                (try_begin),
                    (eq, ":continue", 1),
                    (str_store_party_name, s20, ":party_no"),
                    (display_message, "@{s20} joins the battle on the enemy side"),
                (else_try),
                    (eq, ":continue", 2),
                    (str_store_party_name, s20, ":party_no"),
                    (display_message, "@{s20} joins the battle on your side"),
                (try_end),
            (try_end),
        ],
        [
            ("siege_meeting",
                [ (disable_menu_option),], "Call for a meeting with the commander of the garrison",
                [
                    # ToDo: meeting
                    # Meeting will take place with player and companions/soldiers and garrison commander
                    #   Can chose the number of men to bring
                    #   Bringing high number of men may intimidate but can be considered dishomourable
                    #   Bringing a low number (one) of men show your sincerity and honour
                    # Player can chose to attack the commander
                    #   lose relation with faction, owner of center, family of commander
                    #   lose renown
                    #   lose reputation
                    #   gain morale if at war
                    #   gain relation with member of faction (not honourable ones)
                    # Or to talk
                ]),
            
            ("siege_attack",
                [ ], "Launch the attack",
                [
                    (assign, "$g_enemy", "$g_encountered_party"),
                    (assign, "$g_ally", -1),
                    (assign, "$g_player_team", 1),
                    (assign, "$g_clear_battles", 0),
                    (try_for_parties, ":party_no"),
                        (call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "$g_player_party"),
                        (assign, ":continue", reg0),
                        (try_begin),
                            (eq, ":continue", 1),
                            # (str_store_party_name, s20, ":party_no"),
                            (party_quick_attach_to_current_battle, ":party_no", 1),
                        (else_try),
                            (eq, ":continue", 2),
                            # (str_store_party_name, s20, ":party_no"),
                            (party_quick_attach_to_current_battle, ":party_no", 0),
                        (try_end),
                    (try_end),
                    (jump_to_menu, "mnu_encounter_battle_siege"),
                ]),
            
            ("siege_build_equipement",
                [ (disable_menu_option),], "Build siege equipment",
                [
                    # ToDo: build ladders-siege tower
                ]),
            
            ("siege_cheat_capture",
                [(call_script, "script_cf_debug", debug_all),], "|Cheat| Capture center",
                [
                    (call_script, "script_party_group_defeat_party_group", "$g_player_party", "$g_encountered_party", -1),
                ]),
            
            ("siege_wait",
                [ ], "Wait for some time",
                [
                    (display_message, "@You need to stay close to the besieged center if you wish to keep it besieged."),
                    (change_screen_return),
                ]),
            
            ("siege_leave_army",
                [ (disable_menu_option),], "Leave your army to besiege the center",
                [
                    # ToDo: leave army
                    # Leave most of your army (select a few troops/companions to follow you)
                    # The army will stay around the center to maintain the siege
                    # It will not attack the center by itself
                    # If the army is not big enough, the defenders might sally out and fight the besiegers
                    #   When player arrives, the defenders will go back inside if player army+besieger is too large
                    #   else fight on the field
                    #   If besieging army is defeated in battle, player lose renown (for using bad strategies)
                ]),
            
            ("siege_abandon",
                [ ], "Abandon the siege",
                [
                    (call_script, "script_party_lift_siege", "$g_encountered_party"),
                    (change_screen_return),
                ]),
        ]),
    
    ("siege_camp", mnf_scale_picture,
        "You spot the camp of {s10} surrounding the town of {s11}, you decide to...",
        "none",
        [
            (str_store_party_name, s11, "$g_encountered_party"),
            (party_get_slot, ":leader", "$g_encountered_party_2", slot_party_leader),
            (str_store_troop_name, s10, ":leader"),

            (try_for_parties, ":party_no"),
                (neq, ":party_no", "$g_player_party"),
                (call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "$g_encountered_party_2"),
                (assign, ":continue", reg0),
                (try_begin),
                    (eq, ":continue", 1),
                    (str_store_party_name, s20, ":party_no"),
                    (str_store_party_name, s21, "$g_encountered_party"),
                    (display_message, "@{s20} joins the battle on {s21}'s side"),
                (else_try),
                    (eq, ":continue", 2),
                    (str_store_party_name, s20, ":party_no"),
                    (str_store_party_name, s21, "$g_encountered_party_2"),
                    (display_message, "@{s20} joins the battle on {s21}'s side"),
                (try_end),
            (try_end),
        ],
        [
            ("join_defenders",
                [
                # (str_store_party_name, s11, "$g_encountered_party_2"),
                ], "Sneak past the besieger and help the defenders of {s11}",
                [
                    (select_enemy, 1),
                    (assign, "$g_enemy", "$g_encountered_party_2"),
                    (assign, "$g_ally", "$g_encountered_party"),
                    (assign, "$g_player_team", 0),
                    (assign, "$g_clear_battles", 1),

                    (try_for_parties, ":party_no"),
                        (neq, ":party_no", "$g_player_party"),
                        (call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "$g_encountered_party_2"),
                        (assign, ":continue", reg0),
                        (try_begin),
                            (eq, ":continue", 1),
                            (party_quick_attach_to_current_battle, ":party_no", 0),
                        (else_try),
                            (eq, ":continue", 2),
                            (party_quick_attach_to_current_battle, ":party_no", 1),
                        (try_end),
                    (try_end),

                    (jump_to_menu, "mnu_encounter_battle_siege"),
                ]),
            
            ("join_attackers",
                [
                ], "Join the besiegers attacking the walls",
                [
                    (select_enemy, 0),
                    (assign, "$g_enemy", "$g_encountered_party"),
                    (assign, "$g_ally", "$g_encountered_party_2"),
                    (assign, "$g_player_team", 1),
                    (assign, "$g_clear_battles", 1),

                    (try_for_parties, ":party_no"),
                        (neq, ":party_no", "$g_player_party"),
                        (call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "$g_encountered_party_2"),
                        (assign, ":continue", reg0),
                        (try_begin),
                            (eq, ":continue", 1),
                            (party_quick_attach_to_current_battle, ":party_no", 1),
                        (else_try),
                            (eq, ":continue", 2),
                            (party_quick_attach_to_current_battle, ":party_no", 0),
                        (try_end),
                    (try_end),

                    (jump_to_menu, "mnu_encounter_battle_siege"),
                ]),
            
            ("leave", [], "Leave", 
                [
                    (leave_encounter),
                    (change_screen_return),
                ]),
        ]),
    
    ("simple_encounter", mnf_scale_picture,
        "Simple encounter",
        "none",
        [
            # (set_background_mesh, "mesh_pic_camp"),
            (try_for_parties, ":party_no"),
                (call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "$g_player_party"),
                (assign, ":continue", reg0),
                (try_begin),
                    (eq, ":continue", 1),
                    (str_store_party_name, s20, ":party_no"),
                    (display_message, "@{s20} joins the battle on the enemy side"),
                (else_try),
                    (eq, ":continue", 2),
                    (str_store_party_name, s20, ":party_no"),
                    (display_message, "@{s20} joins the battle on your side"),
                (try_end),
            (try_end),
        ],
        [
            ("encounter_meet_leader", 
                [
                    (party_stack_get_troop_id, ":troop_no", "$g_encountered_party", 0),
                    (str_store_troop_name, s10, ":troop_no"),
                    (party_slot_eq, "$g_encountered_party", slot_party_speak_allowed, 1),], "Meet {s10}",
                [
                    (assign, "$g_talk_party", "$g_encountered_party"),
                    (call_script, "script_setup_party_meeting", "$g_encountered_party"),
                ]),
            
            ("encounter_attack", 
                [
                    (str_store_party_name, s10, "$g_encountered_party"),
                    (store_faction_of_party, ":faction", "$g_encountered_party"),
                    (str_store_faction_name, s11, ":faction"),], "Attack {s10} ({s11})",
                [
                    # Preparation
                    
                    # (try_begin),
                        # (encountered_party_is_attacker),
                        # (assign, "$g_player_team", 1),
                    # (else_try),
                        (assign, "$g_player_team", 1),
                    # (try_end),
                    # (store_sub, ":enemy_team", 1, "$g_player_team"),
                    (assign, "$g_enemy", "$g_encountered_party"),
                    (assign, "$g_ally", -1),
                    (assign, "$g_clear_battles", 0),
                    (try_for_parties, ":party_no"),
                        (call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "$g_player_party"),
                        (assign, ":continue", reg0),
                        (try_begin),
                            (eq, ":continue", 1),
                            # (str_store_party_name, s20, ":party_no"),
                            (party_quick_attach_to_current_battle, ":party_no", 1),
                        (else_try),
                            (eq, ":continue", 2),
                            # (str_store_party_name, s20, ":party_no"),
                            (party_quick_attach_to_current_battle, ":party_no", 0),
                        (try_end),
                    (try_end),
                    (jump_to_menu, "mnu_encounter_battle"),
                ]),
            
            ("encounter_surrender",
                [
                    (try_begin),
                        (neg|encountered_party_is_attacker),
                        (disable_menu_option),
                    (try_end),
                ], "Surrender",
                [
                    (call_script, "script_party_take_player_party_prisoner", "$g_encountered_party"),
                    (leave_encounter),
                    (change_screen_return),
                ]),
            
            ("encounter_leave", 
                [
                    (try_begin),
                        (encountered_party_is_attacker),
                        (disable_menu_option),
                    (try_end),
                ], "Leave",
                [
                    (leave_encounter),
                    (change_screen_return),
                ]),
        ]),
    
    ("double_encounter", mnf_scale_picture,
        "Double encounter",
        "none",
        [
            # (set_background_mesh, "mesh_pic_camp"),

            (try_for_parties, ":party_no"),
                (neq, ":party_no", "$g_player_party"),
                (call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "$g_encountered_party_2"),
                (assign, ":continue", reg0),
                (try_begin),
                    (eq, ":continue", 1),
                    (str_store_party_name, s20, ":party_no"),
                    (str_store_party_name, s21, "$g_encountered_party"),
                    (display_message, "@{s20} joins the battle on {s21}'s side"),
                (else_try),
                    (eq, ":continue", 2),
                    (str_store_party_name, s20, ":party_no"),
                    (str_store_party_name, s21, "$g_encountered_party_2"),
                    (display_message, "@{s20} joins the battle on {s21}'s side"),
                (try_end),
            (try_end),
        ],
        [
            ("encounter_meet_leader",
                [
                    (party_stack_get_troop_id, ":troop_no", "$g_encountered_party", 0),
                    (str_store_troop_name, s10, ":troop_no"),], "Meet {s10}",
                [
                    (assign, "$g_talk_party", "$g_encountered_party"),
                    (call_script, "script_setup_party_meeting", "$g_encountered_party"),
                ]),
            
            ("encounter_meet_leader_2",
                [
                    (party_stack_get_troop_id, ":troop_no", "$g_encountered_party_2", 0),
                    (str_store_troop_name, s10, ":troop_no"),], "Meet {s10}",
                [
                    (assign, "$g_talk_party", "$g_encountered_party_2"),
                    (call_script, "script_setup_party_meeting", "$g_encountered_party_2"),
                ]),
            
            ("encounter_attack",
                [
                    (str_store_party_name, s10, "$g_encountered_party"),
                    (str_store_party_name, s12, "$g_encountered_party_2"),
                    (store_faction_of_party, ":faction", "$g_encountered_party"),
                    (store_faction_of_party, ":faction_2", "$g_encountered_party_2"),
                    (str_store_faction_name, s11, ":faction"),
                    (str_store_faction_name, s13, ":faction_2"),
                    ], "Help {s12} ({s13}) against {s10} ({s11})",
                [
                    # Preparation
                    (assign, "$g_enemy", "$g_encountered_party"),
                    (assign, "$g_ally", "$g_encountered_party_2"),
                    (assign, "$g_player_team", 1),
                    (assign, "$g_clear_battles", 1),
                    (select_enemy, 0),
                    
                    (try_for_parties, ":party_no"),
                        (call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "$g_encountered_party_2"),
                        (assign, ":continue", reg0),
                        (try_begin),
                            (eq, ":continue", 1),
                            # (str_store_party_name, s20, ":party_no"),
                            (party_quick_attach_to_current_battle, ":party_no", 1),
                        (else_try),
                            (eq, ":continue", 2),
                            # (str_store_party_name, s20, ":party_no"),
                            (party_quick_attach_to_current_battle, ":party_no", 0),
                        (try_end),
                    (try_end),
                    
                    (jump_to_menu, "mnu_encounter_battle"),
                ]),
            
            ("encounter_attack_2",
                [
                    (str_store_party_name, s10, "$g_encountered_party_2"),
                    (str_store_party_name, s12, "$g_encountered_party"),
                    (store_faction_of_party, ":faction", "$g_encountered_party"),
                    (store_faction_of_party, ":faction_2", "$g_encountered_party_2"),
                    (str_store_faction_name, s11, ":faction_2"),
                    (str_store_faction_name, s13, ":faction"),
                    ], "Join {s12} ({s13}) against {s10} ({s11})",
                [
                    # Preparation
                    (assign, "$g_enemy", "$g_encountered_party_2"),
                    (assign, "$g_ally", "$g_encountered_party"),
                    (assign, "$g_player_team", 0),
                    (assign, "$g_clear_battles", 1),
                    (select_enemy, 1),
                    
                    (try_for_parties, ":party_no"),
                        (call_script, "script_cf_party_join_battle", ":party_no", "$g_encountered_party", "$g_encountered_party_2"),
                        (assign, ":continue", reg0),
                        (try_begin),
                            (eq, ":continue", 1),
                            # (str_store_party_name, s20, ":party_no"),
                            (party_quick_attach_to_current_battle, ":party_no", 0),
                        (else_try),
                            (eq, ":continue", 2),
                            # (str_store_party_name, s20, ":party_no"),
                            (party_quick_attach_to_current_battle, ":party_no", 1),
                        (try_end),
                    (try_end),
                    
                    (jump_to_menu, "mnu_encounter_battle"),
                ]),
            
            ("encounter_leave", [], "Leave",
                [
                    (leave_encounter),
                    (change_screen_return),
                ]),
        ]),
    
    ("encounter_battle", mnf_scale_picture,
        "Encounter",
        "none",
        [
        ],
        [
            ("battle_charge", [], "Charge the enemy",
                [
                    (set_party_battle_mode),
                    # (encounter_attack),
                    (set_battle_advantage, 0),
                    
                    (call_script, "script_get_battle_scene"),
                    (assign, ":scene", reg0),
                    
                    (set_jump_mission, "mt_battle_field"),
                    (jump_to_scene, ":scene"),
                    
                    (assign, "$g_looted_enemies", 0),
                    (party_clear, "p_battle_released_prisoners"),
                    (jump_to_menu, "mnu_battle_casualties"),

                    (change_screen_mission),
                ]),
        ]),
    
    ("encounter_battle_siege", mnf_scale_picture,
        "Encounter",
        "none",
        [
        ],
        [
            ("battle_charge", [], "Charge the enemy",
                [
                    (set_party_battle_mode),
                    # (encounter_attack),
                    (set_battle_advantage, 0),
                    
                    (party_get_slot, ":scene", "$g_encountered_party", slot_party_siege_scene),
                    
                    (set_jump_mission, "mt_battle_siege"),
                    (jump_to_scene, ":scene"),
                    
                    (assign, "$g_looted_enemies", 0),
                    (party_clear, "p_battle_released_prisoners"),
                    (jump_to_menu, "mnu_battle_casualties"),
                    (change_screen_mission),
                ]),
        ]),
    
    ("battle_casualties", mnf_scale_picture,
        "{s10}",
        "none",
        [
            # (call_script, "script_get_victory_phrase"),
            # (str_store_string_reg, s10, s0),
            (str_store_string, s10, "@The battle is over:^Casualties:"),
            (party_get_num_companions, ":num_player", "p_player_casualties"),
            (try_begin),
                (gt, ":num_player", 0),
                (assign, ":total_dead", 0),
                (assign, ":total_wounded", 0),
                (str_store_string, s10, "@{s10}^^Player casualties:"),
                (party_get_num_companion_stacks, ":num_stacks", "p_player_casualties"),
                (try_for_range, ":cur_stack", 0, ":num_stacks"),
                    (party_stack_get_troop_id, ":cur_troop", "p_player_casualties", ":cur_stack"),
                    (party_stack_get_size, ":stack_size", "p_player_casualties", ":cur_stack"),
                    (party_stack_get_num_wounded, ":cur_wounded", "p_player_casualties", ":cur_stack"),
                    (store_sub, ":cur_dead", ":stack_size", ":cur_wounded"),
                    (val_add, ":total_dead", ":cur_dead"),
                    (val_add, ":total_wounded", ":cur_wounded"),
                    (str_store_troop_name_by_count, s11, ":cur_troop", ":stack_size"),
                    (assign, reg10, ":cur_dead"),
                    (assign, reg11, ":cur_wounded"),
                    (str_store_string, s10, "@{s10}^    {s11}:{reg10? {reg10} dead:}{reg11? {reg11} wounded:}"),
                (try_end),
                (assign, reg12, ":total_dead"),
                (assign, reg13, ":total_wounded"),
                (str_store_string, s10, "@{s10}^  Total: {reg12} dead {reg13} wounded"),
            (try_end),
            
            (party_get_num_companions, ":num_ally", "p_ally_casualties"),
            (try_begin),
                (gt, ":num_ally", 0),
                (assign, ":total_dead", 0),
                (assign, ":total_wounded", 0),
                (str_store_string, s10, "@{s10}^^Ally casualties:"),
                (party_get_num_companion_stacks, ":num_stacks", "p_ally_casualties"),
                (try_for_range, ":cur_stack", 0, ":num_stacks"),
                    (party_stack_get_troop_id, ":cur_troop", "p_ally_casualties", ":cur_stack"),
                    (party_stack_get_size, ":stack_size", "p_ally_casualties", ":cur_stack"),
                    (party_stack_get_num_wounded, ":cur_wounded", "p_ally_casualties", ":cur_stack"),
                    (store_sub, ":cur_dead", ":stack_size", ":cur_wounded"),
                    (val_add, ":total_dead", ":cur_dead"),
                    (val_add, ":total_wounded", ":cur_wounded"),
                    (str_store_troop_name_by_count, s11, ":cur_troop", ":stack_size"),
                    (assign, reg10, ":cur_dead"),
                    (assign, reg11, ":cur_wounded"),
                    (str_store_string, s10, "@{s10}^    {s11}:{reg10? {reg10} dead:}{reg11? {reg11} wounded:}"),
                (try_end),
                (assign, reg12, ":total_dead"),
                (assign, reg13, ":total_wounded"),
                (str_store_string, s10, "@{s10}^  Total: {reg12} dead {reg13} wounded"),
            (try_end),
            
            (party_get_num_companions, ":num_enemy", "p_enemy_casualties"),
            (try_begin),
                (gt, ":num_enemy", 0),
                (assign, ":total_dead", 0),
                (assign, ":total_wounded", 0),
                (str_store_string, s10, "@{s10}^^Enemy casualties:"),
                (party_get_num_companion_stacks, ":num_stacks", "p_enemy_casualties"),
                (try_for_range, ":cur_stack", 0, ":num_stacks"),
                    (party_stack_get_troop_id, ":cur_troop", "p_enemy_casualties", ":cur_stack"),
                    (party_stack_get_size, ":stack_size", "p_enemy_casualties", ":cur_stack"),
                    (party_stack_get_num_wounded, ":cur_wounded", "p_enemy_casualties", ":cur_stack"),
                    (store_sub, ":cur_dead", ":stack_size", ":cur_wounded"),
                    (val_add, ":total_dead", ":cur_dead"),
                    (val_add, ":total_wounded", ":cur_wounded"),
                    (str_store_troop_name_by_count, s11, ":cur_troop", ":stack_size"),
                    (assign, reg10, ":cur_dead"),
                    (assign, reg11, ":cur_wounded"),
                    (str_store_string, s10, "@{s10}^    {s11}:{reg10? {reg10} dead:}{reg11? {reg11} wounded:}"),
                (try_end),
                (assign, reg12, ":total_dead"),
                (assign, reg13, ":total_wounded"),
                (str_store_string, s10, "@{s10}^  Total:{reg12? {reg12} dead:}{reg13? {reg13} wounded:}"),
            (try_end),

            (try_begin),
                (eq, "$g_battle_result", -1),
                (store_random_in_range, reg20, 0, 5), # outcome of the defeat
            (try_end),
        ],
        [
            ("battle_result_defeat_taken_prisoner", [(eq, "$g_battle_result", -1),(lt, reg20, 4),],
                "You are taken prisoner by your oppenents", [
                    (call_script, "script_party_take_player_party_prisoner", "$g_enemy"),

                    (leave_encounter),
                    (change_screen_return),
                ]),

            ("battle_result_defeat_left_for_dead", [(eq, "$g_battle_result", -1),(eq, reg20, 4),],
                "Your enemies believe you dead and leave you lying on the ground", [(rest_for_hours, 2, 1, 0),(change_screen_return),]),

            ("battle_result_loot_enemies", [(eq, "$g_battle_result", 1),(neq, "$g_looted_enemies", 1),], "Loot the fallen enemies",
                [
                    (call_script, "script_party_get_looted_gold", "p_enemy_casualties"),
                    (assign, ":gold", reg0),
                    (call_script, "script_party_group_share_gold", "$g_player_party", ":gold"),

                    (call_script, "script_party_get_loot", "p_enemy_casualties", 1, -1),
                    (assign, ":loot_troop", reg0),
                    (assign, "$g_looted_enemies", 1),
                    (change_screen_loot, ":loot_troop"),
                ]),
            
            ("battle_result_loot_enemies_no_player", [(eq, "$g_battle_result", 1),(neq, "$g_looted_enemies", 1),], "Allow your men to loot the fallen enemies",
                [
                    (call_script, "script_party_get_looted_gold", "p_enemy_casualties"),
                    (assign, ":gold", reg0),
                    (store_sqrt, ":morale", ":gold"),
                    (val_div, ":morale", 50),
                    (val_add, ":morale", 1),
                    (call_script, "script_party_change_morale", "$g_player_party", ":morale"),
                    (call_script, "script_troop_change_relation_with_party_heroes", "$g_player_troop", "p_enemy_casualties", -1),
                    # ToDo: reduce relation with faction and slightly with looted lords

                    (assign, "$g_looted_enemies", 1),
                    (jump_to_menu, "mnu_battle_casualties"),
                ]),
            
            ("battle_result_loot_all", [(eq, "$g_battle_result", 1),(neq, "$g_looted_enemies", 1),], "Loot every fallen soldier",
                [
                    (call_script, "script_party_get_looted_gold", "p_enemy_casualties"),
                    (assign, ":gold", reg0),
                    (call_script, "script_party_get_looted_gold", "p_ally_casualties"),
                    (val_add, ":gold", reg0),
                    (call_script, "script_party_get_looted_gold", "p_player_casualties"),
                    (val_add, ":gold", reg0),
                    (call_script, "script_party_group_share_gold", "$g_player_party", ":gold"),

                    (call_script, "script_troop_change_honor", "$g_player_troop", -1),
                    (call_script, "script_party_change_morale", "$g_player_party", -5),
                    # ToDo: reduce relation with faction and with looted lords (includes allies at a reduced rate)
                    (call_script, "script_troop_change_relation_with_party_heroes", "$g_player_troop", "p_enemy_casualties", -2),
                    (call_script, "script_troop_change_relation_with_party_heroes", "$g_player_troop", "p_ally_casualties", -1),
                    
                    (call_script, "script_party_get_loot", "p_enemy_casualties", 1, -1),
                    (assign, ":loot_troop", reg0),
                    (call_script, "script_party_get_loot", "p_ally_casualties", 0, ":loot_troop"),
                    (call_script, "script_party_get_loot", "p_player_casualties", 0, ":loot_troop"),
                    (assign, "$g_looted_enemies", 1),
                    (change_screen_loot, ":loot_troop"),
                ]),
            
            ("battle_result_manage_prisoners",
                [
                    (eq, "$g_battle_result", 1),
                    (assign, ":continue", 0),
                    (try_begin),
                        (call_script, "script_cf_party_has_prisoners", "$g_enemy"),
                        (assign, ":continue", 1),
                    (else_try),
                        (call_script, "script_cf_party_has_members", "$g_enemy"),
                        (assign, ":continue", 1),
                    (try_end),
                    (eq, ":continue", 1),
                ], "Handle prisoners",
                [
                    (call_script, "script_party_group_transfer_prisoners_to_party", "$g_enemy", "p_battle_released_prisoners", 0),
                    (call_script, "script_party_group_transfer_members_to_prisoners", "$g_enemy", "p_battle_released_prisoners", 1),

                    (change_screen_exchange_with_party, "p_battle_released_prisoners"),
                ]),
            
            ("battle_result_leave", [(eq, "$g_battle_result", 1),], "Leave the battlefield",
                [
                    (try_begin),
                        (eq, "$g_looted_enemies", 0),
                        # ToDo: slightly increase relation with faction
                        (call_script, "script_troop_change_honor", "$g_player_troop", 1),
                    (try_end),

                    (try_begin),
                        (this_or_next|call_script, "script_cf_party_has_prisoners", "p_battle_released_prisoners"),
                        (call_script, "script_cf_party_has_members", "p_battle_released_prisoners"),

                        (call_script, "script_party_group_transfer_prisoners_to_party", "p_battle_released_prisoners", "$g_enemy", 1),
                        (call_script, "script_party_group_transfer_members_to_prisoners", "p_battle_released_prisoners", "$g_enemy", 0),
                    (try_end),
                    
                    (call_script, "script_party_check_prisoners", "$g_player_party"),

                    (call_script, "script_party_group_defeat_party_group", "$g_player_party", "$g_enemy", "$g_ally"),

                    (try_begin),
                        (eq, "$g_clear_battles", 1),
                        (party_leave_cur_battle, "$g_player_party"),
                    (try_end),

                    (leave_encounter),
                    (change_screen_return),
                ]),
            ("error_leave", [(neq, "$g_battle_result", 1),(neq, "$g_battle_result", -1),], "Error! Leave the battle",
                [
                    (leave_encounter),
                    (change_screen_return),
                ]),
        ]),
    
    ("after_battle", mnf_scale_picture,
        "You should not be reading this",
        "none",
        [
            (change_screen_map),
        ],
        [ ]),
    
    # ("visit_place", mnf_scale_picture,
        # "Visit the monument?",
        # "none", [],
        # [ 
            # ("visit_yes", [], "Yes",
            # [
                # (store_sub, ":offset", "$g_encountered_party", "p_places_stone_obelisk"),
                # (store_add, ":scene", ":offset", "scn_places_plain_stone_obelisk"),
                # (set_jump_mission, "mt_visit_place"),
                # (jump_to_scene, ":scene"),
                # (change_screen_mission),
            # ]),
            
            # ("visit_no", [], "No",
            # [
                # (change_screen_return),
            # ]),
        # ]),

    ("player_prisoner_take_action", mnf_scale_picture, 
        "{s10} holds you prisoner, chains holding your arms and legs in place.^^You can see two guards playing cards glancing at you from time to time.^You guess that they are your jailers.",
        "none",
        [
            (troop_get_slot, ":captor", "$g_player_troop", slot_troop_prisoner_of),
            (try_begin),
                (is_between, ":captor", lords_begin, lords_end),
                (str_store_troop_name, s10, ":captor"),
            (else_try),
                (str_store_string, s10, "@Someone"),
            (try_end),
        ],
        [
            ("action_call_guards", [], "Call the guards", [(jump_to_menu, "mnu_player_prisoner_call_guards"),]),
            ("action_insult_guards", [], "Yell insults at the guards", [(jump_to_menu, "mnu_player_prisoner_insult_guards"),]),
            ("action_escape", [], "Try to find a way to escape", [(jump_to_menu, "mnu_player_prisoner_escape"),]),
            ("action_do_nothing", [], "Do nothing", [(change_screen_return),(rest_for_hours, 24, 1, 0),]),
        ]),

    ("player_prisoner_call_guards", mnf_scale_picture, 
        "When you call for them, one of them turns to you, the other sighing.",
        "none",
        [],
        [
            ("action_talk", [], "Talk to the guards", [(jump_to_menu, "mnu_player_prisoner_talk_guards"),]),
            ("action_order_release", [], "Order your release", [(jump_to_menu, "mnu_player_prisoner_order_release"),]),
            ("action_do_nothing", [], "Nevermind", [(jump_to_menu, "mnu_player_prisoner_take_action"),]),
        ]),

    ("player_prisoner_talk_guards", mnf_scale_picture, 
        "They both do not seem interested in talking to you, they tell you to shut up, and they go back to their game.",
        "none",
        [],
        [
            ("action_insult_guards", [], "Yell insults at the guards", [(jump_to_menu, "mnu_player_prisoner_insult_guards"),]),
            ("action_go_back", [], "Nevermind", [(jump_to_menu, "mnu_player_prisoner_take_action"),]),
        ]),
    ("player_prisoner_order_release", mnf_scale_picture, 
        "You order them to release you, but in your current state you cannot do more than.",
        "none",
        [],
        [
            ("action_insult_more", [], "Keep going", [(jump_to_menu, "mnu_player_prisoner_insult_guards_more"),]),
            ("action_go_back", [], "Calm down and stop", [(jump_to_menu, "mnu_player_prisoner_take_action"),]),
        ]),

    ("player_prisoner_insult_guards", mnf_scale_picture, 
        "You yell all sorts of insults at your jailers. They try to ignore you.",
        "none",
        [],
        [
            ("action_insult_more", [], "Keep going", [(jump_to_menu, "mnu_player_prisoner_insult_guards_more"),]),
            ("action_go_back", [], "Calm down and stop", [(jump_to_menu, "mnu_player_prisoner_take_action"),]),
        ]),

    ("player_prisoner_insult_guards_more", mnf_scale_picture, 
        "You keep yelling insults, you seem to find insults that are worst every time a new one comes out of your mouth.^After a while, you can see your jailers gritting their teeth.^A feeling of success is felt in you and it only increases the amount and the loudness of your insults.^^One of them turns at you with a cold stare.",
        "none",
        [],
        [
            ("action_insult_more_and_more", [], "Personaly insult him", [(jump_to_menu, "mnu_player_prisoner_insult_guards_more_and_more"),]),
            ("action_go_back", [], "Calm down and stop", [(jump_to_menu, "mnu_player_prisoner_take_action"),]),
        ]),

    ("player_prisoner_insult_guards_more_and_more", mnf_scale_picture, 
        "You smile, and insult him where it hurts, he gets up his chair, his friend not trying to hold him.^He pauses and seeing the smile on your face he comes to teach you a lesson.",
        "none",
        [],
        [
            ("action_defy_him", [], "Keep smiling, and dare him to come", [(jump_to_menu, "mnu_player_prisoner_guard_teach_lesson"),]),
            ("action_apologise", [], "Try to apologise", [(jump_to_menu, "mnu_player_prisoner_guard_teach_lesson"),]),
        ]),

    ("player_prisoner_guard_teach_lesson", mnf_scale_picture, 
        "He doesn't mind you anymore, you pushed him too much, now you will have to pay the price.",
        "none",
        [],
        [
            ("action_hit_him_first", [], "Try to hit him first", [(jump_to_menu, "mnu_player_prisoner_guard_beating"),]),
            ("action_call_for_help", [], "Call for help as you as you can", [(jump_to_menu, "mnu_player_prisoner_guard_beating"),]),
            ("action_plead_mercy", [], "Plead for mercy", [(jump_to_menu, "mnu_player_prisoner_guard_beating"),]),
        ]),

    ("player_prisoner_guard_beating", mnf_scale_picture, 
        "Your newly found friend unleashes all his anger on you, kicking, punching, in your face, in your stomach, the force is so great you have trouble breathing.^You try to block the hits with your arms, but your chains prevent you from moving.^You try to plead him to stop, but words barely come out of your mouth.^Your strength is drained from your body, you cannot move anymore.",
        "none",
        [],
        [
            ("action_blackout", [], "You feel like you are dying, you close your eyes and all becomes dark", [(troop_set_health, "$g_player_troop", 5),(jump_to_menu, "mnu_player_prisoner_guard_beating_end"),]),
        ]),

    ("player_prisoner_guard_beating_end", mnf_scale_picture, 
        "After a while, you regain consciousness. Your body hurts, but you manage to open your eyes.^You can see the two guards are no longer playing cards, the one that administered your punishment is leaning against a wall, you can see he is still angered but has managed to calm a little.^The other is still sat on the chair, he seems a bit concerned, but it doesn't seem to be about you, he probably had to stop him from killing you.^He stare at his friend in silence.^^You will try to remember to be a bit more careful next time.^You eyes are heavy, you feel like resting a little more...",
        "none",
        [],
        [
            ("action_go_back", [], "Go back", [(change_screen_return),(rest_for_hours, 24, 1, 0),]),
        ]),

    ("player_prisoner_escape", mnf_scale_picture, 
        "{s10}",
        "none",
        [
            (store_troop_health, ":player_health", "$g_player_troop", 0),
            (try_begin),
                (gt, ":player_health", 50),
                (assign, reg10, 1),
                (str_store_string, s10, "@You think of ways to escape your predicament..."),
            (else_try),
                (gt, ":player_health", 20),
                (assign, reg10, 0),
                (str_store_string, s10, "@You feel a bit weak but still think of ways to escape your predicament..."),
            (else_try),
                (assign, reg10, -1),
                (str_store_string, s10, "@In your current conditon you don't think you will be able to move at all, let alone escape."),
            (try_end),
        ],
        [
            ("action_escape_persuade", [(neq, reg10, -1),], "Try to persuade your captors", [(jump_to_menu, "mnu_player_prisoner_escape_persuade"),]),
            ("action_escape_sneak", [(neq, reg10, -1),], "Try to sneak away unnoticed", [(jump_to_menu, "mnu_player_prisoner_escape_sneak"),]),
            ("action_escape_force", [(neq, reg10, -1),], "Try to force your way out", [(jump_to_menu, "mnu_player_prisoner_escape_force"),]),
            ("action_go_back", [], "Perhaps later...", [(jump_to_menu, "mnu_player_prisoner_take_action"),]),
        ]),

    ("player_prisoner_escape_persuade", mnf_scale_picture, 
        "{s10}",
        "none",
        [
            (call_script, "script_troop_escape_chance", "$g_player_troop", -1, escape_type_wits),
            (assign, ":outcome", reg0),
            (try_begin),
                (call_script, "script_cf_debug", debug_simple),
                (display_message, "@Current dialog outcome is {reg0}"),
            (try_end),
            (try_begin),
                (eq, ":outcome", outcome_success),
                (assign, reg10, outcome_success),
                (str_store_string, s10, "@You call your guard to your cell. When nearby you persuade him to open the cell, and promise him gold in exchange for your liberation. After a moment of hesitation, he looks left and right, then, he signals for you to run in a direction with a movement of his hand."),
            (else_try),
                (assign, reg10, outcome_failure),
                (str_store_string, s10, "@You call your guard to your cell. When nearby you persuade him to open the cell, and promise him gold in exchange for your liberation. After a moment of hesitation, he looks left and right, opens the cell door and kicks you in the face.^^You are stunned for a while.^After regaining your senses, you feel tricked and a taste of your own blood."),
            (try_end),
        ],
        [
            ("action_go_back", [(eq, reg10, outcome_failure),], "It did not seem to work all that well...", [
                (store_troop_health, ":player_health", "$g_player_troop"),
                (val_sub, ":player_health", 20),
                (val_max, ":player_health", 5),
                (troop_set_health, "$g_player_troop", ":player_health"),
                (change_screen_return),
                (rest_for_hours, 24, 1, 0),
            ]),
            ("action_free", [(eq, reg10, outcome_success),], "Free at last", [(call_script, "script_player_party_free"),(change_screen_return),]),
        ]),

    ("player_prisoner_escape_sneak", mnf_scale_picture, 
        "You notice the round of the guards. During a shift, you quietly unlock your cell and stealthily move away for your captors.^You did not however notice one young man diligently guarding at his post, a crossbow in his hands. He points it towards you and you freeze.^After a moment of silence, he realises you are not going to try anything. He escorts you to your cell, warning you to never try again, but without hurting you in the process. He might not be so lenient next time.",
        "none",
        [
            (call_script, "script_troop_escape_chance", "$g_player_troop", -1, escape_type_agility),
            (assign, ":outcome", reg0),
            (try_begin),
                (call_script, "script_cf_debug", debug_simple),
                (display_message, "@Current dialog outcome is {reg0}"),
            (try_end),
            (try_begin),
                (eq, ":outcome", outcome_success),
                (assign, reg10, outcome_success),
                (str_store_string, s10, "@You notice the round of the guards. During a shift, you quietly unlock your cell and stealthily move away for your captors."),
            (else_try),
                (assign, reg10, outcome_failure),
                (str_store_string, s10, "@You notice the round of the guards. During a shift, you quietly unlock your cell and stealthily move away for your captors.^You did not however notice one young man diligently guarding at his post, a crossbow in his hands. He points it towards you and you freeze.^After a moment of silence, he realises you are not going to try anything. He escorts you to your cell, warning you to never try again, but without hurting you in the process. He might not be so lenient next time."),
            (try_end),
        ],
        [
            ("action_go_back", [(eq, reg10, outcome_failure),], "It did not seem to work all that well...", [
                (change_screen_return),
                (rest_for_hours, 24, 1, 0),
            ]),
            ("action_free", [(eq, reg10, outcome_success),], "Free at last", [(call_script, "script_player_party_free"),(change_screen_return),]),
        ]),

    ("player_prisoner_escape_force", mnf_scale_picture, 
        "You call your guard to your cell. He closes in, as you gesture to move closer. Once within striking distance, you grab him by the collar and slam his face on the iron bars. He manages to put his arm in front of his face.^You can see the pain and anger in his eyes, this is not going to be pleasant.^^He breaks free from your hold and steps back to regain his footing.^He grabs a nearby club and heads towards you, he is ready to give you your due.^^After a short beating, you stop moving and he loses his rage.^You are left on the ground with pain everywhere.",
        "none",
        [
            (call_script, "script_troop_escape_chance", "$g_player_troop", -1, escape_type_strength),
            (assign, ":outcome", reg0),
            (try_begin),
                (call_script, "script_cf_debug", debug_simple),
                (display_message, "@Current dialog outcome is {reg0}"),
            (try_end),
            (try_begin),
                (eq, ":outcome", outcome_success),
                (assign, reg10, outcome_success),
                (str_store_string, s10, "@You call your guard to your cell. He closes in, as you gesture to move closer. Once within striking distance, you grab him by the collar and slam his face on the iron bars. He falls unconscious and you grab the key to your cell."),
            (else_try),
                (assign, reg10, outcome_failure),
                (str_store_string, s10, "@You call your guard to your cell. He closes in, as you gesture to move closer. Once within striking distance, you grab him by the collar and slam his face on the iron bars. He manages to put his arm in front of his face.^You can see the pain and anger in his eyes, this is not going to be pleasant.^^He breaks free from your hold and steps back to regain his footing.^He grabs a nearby club and heads towards you, he is ready to give you your due.^^After a short beating, you stop moving and he loses his rage.^You are left on the ground with pain everywhere."),
            (try_end),
        ],
        [
            ("action_go_back", [(eq, reg10, outcome_failure),], "It did not seem to work all that well...", [
                (store_troop_health, ":player_health", "$g_player_troop"),
                (val_sub, ":player_health", 90),
                (val_max, ":player_health", 5),
                (troop_set_health, "$g_player_troop", ":player_health"),
                (change_screen_return),
                (rest_for_hours, 24, 1, 0),
            ]),
            ("action_go_back", [(eq, reg10, outcome_success),], "Free at last", [(call_script, "script_player_party_free"),(change_screen_return),]),
        ]),

    ("player_receive_center", mnf_scale_picture, 
        "{s12}",
        "none",
        [
            (set_background_mesh, "mesh_pic_messenger"),

            (str_store_troop_name, s10, reg20),
            (str_store_party_name, s11, reg21),
            (try_begin),
                (troop_slot_eq, "$g_player_troop", slot_troop_vassal_of, reg20),
                (str_store_string, s12, "str_player_receive_center_vassal"),
            (else_try),
                (troop_slot_eq, reg20, slot_troop_vassal_of, "$g_player_troop"),
                (str_store_string, s12, "str_player_receive_center_vassal"),
            (else_try),
                (str_store_string, s12, "str_player_receive_center"),
            (try_end),
        ],
        [
            ("receive_center_refuse", [], "Refuse", [
                (call_script, "script_get_current_day"),
                (assign, "$g_player_last_proposed_vassalage", reg0),
                (change_screen_return),
            ]),
            ("receive_center_accept", [], "Accept", [
                (try_begin),
                    (neg|troop_slot_eq, "$g_player_troop", slot_troop_vassal_of, reg20),
                    (party_set_slot, reg21, slot_party_reserved, "$g_player_troop"),
                    # (call_script, "script_troop_give_center_to_troop", reg20, reg21, "$g_player_troop"),
                    (quest_set_slot, "qst_swear_vassalage_fief", slot_quest_object, reg21),
                    (call_script, "script_start_quest", "qst_swear_vassalage_fief", reg20),
                (else_try),
                    (call_script, "script_troop_give_center_to_troop", reg20, reg21, "$g_player_troop"),
                (try_end),
                (change_screen_return),
            ]),
        ]),
 ]
