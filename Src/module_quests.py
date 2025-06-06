from header_quests import *

quests = [

    ("introduction_default", "Rest in {s59}", 0,
        "{!}."),
    ("introduction_default_search", "Search for information on the brother's whereabouts", 0,
        "{!}."),
    ("introduction_default_search_1", "Search the village of {s59}", 0,
        "{!}."),
    ("introduction_default_search_2", "Search the village of {s59}", 0,
        "{!}."),
    ("introduction_default_search_3", "Search the village of {s59}", 0,
        "{!}."),

    ("swear_vassalage_fief", "Swear Vassalage to {s62}", qf_random_quest,
        "{!}{s62} proposed that you pledge allegience to him, you would be granted {s11} in exchange."),

    ("persuade_lord_vassalage", "Persuade {s62}", qf_random_quest,
        "{!}Persuade {s62} of becoming the vassal of {s11}."),

    ("visit_center_new_owner", "Visit {s62}", qf_random_quest,
        "{!}As the newly appointed owner of {s62} you should head to the center to make yourself known and arrange the details of your fiefdom."),

    ("village_deliver_grain", "Deliver grain to the village elder of {s59}", qf_random_quest,
        "{!}"),
    ("village_deliver_rare_good", "Deliver {s11} to {s62}", qf_random_quest,
        "{!}"),
    ("village_negociate_trade_arrangement", "Arrange a trade agreement for {s62}", qf_random_quest,
        "{!}"),
    ("village_hunt_notorious_bandit", "Hunt a notorious bandit near {s62}", qf_random_quest,
        "{!}"),
    ("village_persuade_mercenaries_leave", "Persuade troublesome mercenaries to leave {s62}", qf_random_quest,
        "{!}"),
    
    ("quests_end", "Quests End", 0, "{!}."),
]
