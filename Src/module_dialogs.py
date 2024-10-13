from header_common import *
from header_dialogs import *
from header_operations import *
from header_parties import *
from header_item_modifiers import *
from header_skills import *
from header_triggers import *
from ID_troops import *
from ID_party_templates import *
from module_constants import *

######################
## GLOBAL VARIABLES ##
######################
# $g_dialog_outcome: 
# 		shared variable to handle dialog outcomes
# 		it must be set in the first matching dialog
# $g_talk_troop:
# 		holds the conversation troop
# $g_talk_party:
# 		holds the conversation party
##



dialogs = [
	################
	# Init dialogs #
	################
	[anyone, "start", 
		[
			(store_conversation_troop, "$g_talk_troop"),

			(call_script, "script_get_current_day"),
			(assign, ":date", reg0),
			(troop_get_slot, ":last_met", "$g_talk_troop", slot_troop_last_met),
			(try_begin),
				(neq, ":last_met", -1),
				(store_sub, "$g_last_met_hours", ":date", ":last_met"),
				(troop_set_slot, "$g_talk_troop", slot_troop_last_met, ":date"),
			(try_end),
			
			(eq, 0, 1),
		], "!ERROR! Should not display", "close_window", []],

	##################
	# Generic Dialog #
	##################
	# [anyone|plyr, "player_leave",
	# 	[], "...", "close_window", [(leave_encounter),]],
	
	#######################
	# Agressive lord talk #
	#######################
	[anyone, "start",
		[ 
			(encountered_party_is_attacker),
			(is_between, "$g_talk_troop", lords_begin, lords_end),
			(troop_slot_eq, "$g_talk_troop", slot_troop_last_met, -1),
			(call_script, "script_troop_get_title_string", "$g_talk_troop"),
			(str_store_string_reg, s11, s0),
			(str_store_troop_name, s10, "$g_talk_troop"),
		], "I am {s10}, {s11}. I wish to know the name I will carve on your grave.", "player_lord_greeting_attacked", 
		[
			(call_script, "script_get_current_day"),
			(assign, ":date", reg0),
			(troop_set_slot, "$g_talk_troop", slot_troop_last_met, ":date"),
		]],
	[anyone, "start",
		[ 
			(encountered_party_is_attacker),
			(is_between, "$g_talk_troop", lords_begin, lords_end),
		], "{playername}... We meet again, do you have anything to say before I crush you?", "player_lord_greeting_attacked", []],

	#############
	# Lord Talk #
	#############	
	[anyone, "start", 
		[
			(is_between, "$g_talk_troop", lords_begin, lords_end),
			(check_quest_active, "qst_swear_vassalage_fief"),
			(quest_slot_eq, "qst_swear_vassalage_fief", slot_quest_giver_troop, "$g_talk_troop"),
		], "Ah {playername}, I was waiting for your arrival. My messenger has delivered the offer then?", "player_lord_offer_vassal", []],
	
	[anyone, "start", 
		[
			(is_between, "$g_talk_troop", lords_begin, lords_end),
			(troop_slot_eq, "$g_talk_troop", slot_troop_last_met, -1),
			(call_script, "script_troop_get_title_string", "$g_talk_troop"),
			(str_store_string_reg, s11, s0),
			(str_store_troop_name, s10, "$g_talk_troop"),
		], "Hail traveller. It's a pleasure to meet you, I am {s10}, {s11}. What is your name?", "player_lord_greeting", 
		[
			(call_script, "script_get_current_day"),
			(assign, ":date", reg0),
			(troop_set_slot, "$g_talk_troop", slot_troop_last_met, ":date"),
		]],
	
	[anyone, "start", 
		[
			(le, "$g_last_met_hours", 6),
			(is_between, "$g_talk_troop", lords_begin, lords_end),
		], "Hello again traveller. What is it that you need?", "player_lord_main", []],
	
	[anyone, "start", 
		[(is_between, "$g_talk_troop", lords_begin, lords_end),
		], "Hmm... {playername}, yes? What do you need?", "player_lord_main", []],
	
	[anyone|plyr, "player_lord_greeting",
		[], "My name is {playername}, the pleasure is shared.", "player_lord_greeting_after", []],
	[anyone|plyr, "player_lord_greeting",
		[], "My name is {playername}, remember it, you will be hearing it a lot.", "player_lord_greeting_after", []],
	[anyone|plyr, "player_lord_greeting",
		[], "Back off peasant!", "close_window", []],
	
	[anyone, "player_lord_greeting_after",
		[], "Now... What do you need?", "player_lord_main", []],
	
	[anyone|plyr, "player_lord_greeting_attacked",
		[], "My name is of no matter to you, now send your dogs so that I can kill them.", "close_window", []],
	[anyone|plyr, "player_lord_greeting_attacked",
		[], "I am {playername}, prepare your men for the battle, it shall be interesting.", "close_window", []],
	[anyone|plyr, "player_lord_greeting_attacked",
		[], "I am {playername} and I demand to settle this with a duel.", "duel_request", []],

	[anyone, "lord_main_return",
		[], "Anything else ?", "player_lord_main", []],
	
	# Main lord talk (player)
	[anyone|plyr, "player_lord_main",
		[
			(store_troop_faction, ":talk_troop_faction", "$g_talk_troop"),
			(call_script, "script_cf_troop_can_join_faction", "$g_player_troop", ":talk_troop_faction"),
		], "My lord, I would ask to become your sworn vassal.", "lord_ask_vassal",
		[
			(call_script, "script_get_player_vassal_outcome", "$g_talk_troop"),
			(assign, "$g_dialog_outcome", reg0),
			(assign, "$g_object_outcome", reg1),
		]],
	[anyone|plyr, "player_lord_main",
		[], "I would like to know something.", "lord_ask", []],
	[anyone|plyr, "player_lord_main",
		[], "Let us talk for a bit.", "lord_talk", []],
	[anyone|plyr, "player_lord_main",
		[], "I am here to deliver you my demands !", "player_lord_demands", []],
	[anyone|plyr, "player_lord_main",
		[], "How about we have a duel ?", "duel_ask", []],
	[anyone|plyr, "player_lord_main",
		[(call_script, "script_cf_debug", debug_all),], "[DEBUG] Debug dialog menu", "lord_debug", []],
	[anyone|plyr, "player_lord_main",
		[], "I must take my leave.", "close_window", []],

	[anyone, "lord_ask",
		[], "Ask away, I will answer if I can.", "player_lord_ask", []],
	[anyone, "lord_talk",
		[], "Of course.", "player_lord_talk", []],

	# [anyone|plyr, "player_lord_ask",
	# 	[], "What are you doing ?.", "lord_whereabouts", []],
	[anyone|plyr, "player_lord_ask",
		[], "I want your opinion on a certain matter.", "lord_ask_opinion", []],
	[anyone|plyr, "player_lord_talk",
		[], "Did you hear any rumors recently?", "lord_rumors", []],
	[anyone|plyr, "player_lord_talk",
		[
			(troop_get_slot, ":lord", "$g_talk_troop", slot_troop_vassal_of),
			(gt, ":lord", 0),
			(str_store_troop_name, s10, ":lord"),
		], "How do you feel about your relation with your lord {s10}?", "lord_become_vassal", []],
	[anyone|plyr, "player_lord_talk",
		[
			(troop_get_slot, ":lord", "$g_talk_troop", slot_troop_vassal_of),
			(eq, ":lord", -1),
		], "Have you considered pledging your loyalty to someone?", "lord_become_vassal", []],
	[anyone|plyr, "player_lord_talk",
		[], "Nevermind", "lord_main_return", []],

	[anyone, "lord_rumors",
		[], "Nothing new I'm afraid.", "lord_main_return", []],

	[anyone, "lord_become_vassal",
		[
			(call_script, "script_troop_get_vassalage_dialog_availability", "$g_talk_troop"),
			(assign, "$g_dialog_outcome", reg0),
			(eq, "$g_dialog_outcome", outcome_failure),
		], "I'd rather not speak of this matter with you.", "lord_main_return", []],
	[anyone, "lord_become_vassal",
		[
			(eq, "$g_dialog_outcome", outcome_neutral),
		], "I don't think this is the right time to speak of this matter. Find me at another time.", "lord_main_return", []],
	# [anyone, "lord_become_vassal",
	# 	[
	# 		(store_troop_faction, ":troop_faction", "$g_talk_troop"),
	# 		(faction_slot_eq, ":troop_faction", slot_faction_leader, "$g_talk_troop"),
	# 		(call_script, "script_get_dialog_lord_opinion", "$g_talk_troop"),
	# 	], "{s0}", "lord_become_vassal_2", []],
	[anyone, "lord_become_vassal",
		[(call_script, "script_get_dialog_lord_opinion", "$g_talk_troop"),], "{s0}", "lord_become_vassal_2", []],

	[anyone, "lord_become_vassal_2", [], "Did you have something in mind?", "lord_become_vassal_propose", []],

	[anyone|plyr, "lord_become_vassal_propose",
		[
			(assign, ":continue", 0),
			(try_begin),
				(call_script, "script_cf_troop_has_event", "$g_talk_troop", event_type_proposed_vassalage),
			(else_try),
				(assign, ":continue", 1),
			(try_end),
			(eq, ":continue", 1),

		], "Would you be interested in becoming my vassal?", "lord_become_vassal_response",
		[
			(quest_set_slot, "qst_persuade_lord_vassalage", slot_quest_object, "$g_player_troop"),
			(call_script, "script_start_quest", "qst_persuade_lord_vassalage", "$g_talk_troop"),
			(quest_set_slot, "qst_persuade_lord_vassalage", slot_quest_value, 0),
		]],
	[anyone|plyr, "lord_become_vassal_propose",
		[
			(call_script, "script_cf_troop_has_event", "$g_talk_troop", event_type_proposed_vassalage),
		], "Have you considered my previous proposition?", "lord_become_vassal_persuasion_begin",
		[
			(quest_set_slot, "qst_persuade_lord_vassalage", slot_quest_object, "$g_player_troop"),
			(call_script, "script_start_quest", "qst_persuade_lord_vassalage", "$g_talk_troop"),
			(quest_set_slot, "qst_persuade_lord_vassalage", slot_quest_value, 0),

			(store_random_in_range, ":rand", 0, "$g_daily_random"),
			(val_div, ":rand", daily_random_max/20),
			(call_script, "script_troop_get_vassalage_availability_score", "$g_talk_troop", "$g_player_troop"),
			(store_add, ":value", reg0, ":rand"),
			(quest_set_slot, "qst_persuade_lord_vassalage", slot_quest_value, ":value"),
			(quest_set_slot, "qst_persuade_lord_vassalage", slot_quest_num_tries, 5),
		]],
	# [anyone|plyr, "lord_become_vassal_propose",
	# 	[
	# 		(troop_get_slot, ":player_lord", "$g_player_troop", slot_troop_vassal_of),
	# 		(gt,  ":player_lord", 0),
	# 		(neq, ":player_lord", "$g_talk_troop"),
	# 		(str_store_troop_name, s10, ":player_lord"),
	# 	], "Would you be interested in becoming the vassal of {s10}?", "lord_become_vassal_response",
	# 	[
	# 		(troop_get_slot, ":player_lord", "$g_player_troop", slot_troop_vassal_of),
	# 		(quest_set_slot, "qst_persuade_lord_vassalage", slot_quest_object, ":player_lord"),
	# 		(call_script, "script_start_quest", "qst_persuade_lord_vassalage", "$g_talk_troop"),
	# 	]],
	# [anyone|plyr, "lord_become_vassal_propose",
	# 	[
	# 		(store_troop_faction, ":player_faction", "$g_player_troop"),
	# 		(is_between, ":player_faction", kingdoms_begin, kingdoms_end),
	# 		(faction_get_slot, ":faction_leader", ":player_faction", slot_faction_leader),
	# 		(gt, ":faction_leader", 0),
	# 		(troop_get_slot, ":player_lord", "$g_player_troop", slot_troop_vassal_of),
	# 		(neq,  ":player_lord", ":faction_leader"),
	# 		(neq, ":faction_leader", "$g_talk_troop"),
	# 		(str_store_troop_name, s10, ":faction_leader"),
	# 	], "Would you be interested in becoming the vassal of {s10}?", "lord_become_vassal_response",
	# 	[
	# 		(store_troop_faction, ":player_faction", "$g_player_troop"),
	# 		(faction_get_slot, ":faction_leader", ":player_faction", slot_faction_leader),
	# 		(quest_set_slot, "qst_persuade_lord_vassalage", slot_quest_object, ":faction_leader"),
	# 		(call_script, "script_start_quest", "qst_persuade_lord_vassalage", "$g_talk_troop"),
	# 	]],
	[anyone|plyr, "lord_become_vassal_propose",
		[], "Nevermind", "lord_main_return", []],

	[anyone, "lord_become_vassal_response",
		[
			(call_script, "script_troop_get_become_vassal_answer", "$g_talk_troop"),
			(assign, "$g_dialog_outcome", reg0),
			(eq, "$g_dialog_outcome", outcome_success),
		], "You've convinced me.", "lord_main_return",
		[
			(quest_get_slot, ":lord", "qst_persuade_lord_vassalage", slot_quest_object),
			(call_script, "script_troop_become_vassal", "$g_talk_troop", ":lord"),
			(call_script, "script_succeed_quest", "qst_persuade_lord_vassalage"),
			(call_script, "script_complete_quest", "qst_persuade_lord_vassalage"),
			(troop_set_slot, "$g_talk_troop", slot_troop_become_vassal_tried, 0),
		]],

	[anyone, "lord_become_vassal_response",
		[
			(eq, "$g_dialog_outcome", outcome_neutral),
		], "I'm not certain about that proposition, I'll need some time to think about it.",
		"lord_become_vassal_undecided", []],

	[anyone, "lord_become_vassal_response",
		[
			(eq, "$g_dialog_outcome", outcome_failure),
		], "I feel your proposition gives me too little and offers you too much. ^Don't speak of this matter to me again.",
		"lord_main_return",
		[
			(call_script, "script_fail_quest", "qst_persuade_lord_vassalage"),
			(call_script, "script_complete_quest", "qst_persuade_lord_vassalage"),
			(troop_set_slot, "$g_talk_troop", slot_troop_become_vassal_tried, become_vassal_try_negative_answer),
			(call_script, "script_get_current_day"),
			(troop_set_slot, "$g_talk_troop", slot_troop_become_vassal_last_try, reg0),
		]],

	[anyone|plyr, "lord_become_vassal_undecided",
		[], "Very well, keep it in mind.", "lord_main_return",
		[
			(quest_get_slot, ":lord", "qst_persuade_lord_vassalage", slot_quest_object),
			(call_script, "script_conclude_quest", "qst_persuade_lord_vassalage"),
			(call_script, "script_complete_quest", "qst_persuade_lord_vassalage"),
			(call_script, "script_troop_change_relation_with_troop", "$g_player_troop", "$g_talk_troop", 2),

			(call_script, "script_troop_add_event", "$g_talk_troop", event_type_proposed_vassalage, "$g_player_troop", ":lord", event_value_proposed_vassalage, -1),
		]],

	[anyone|plyr, "lord_become_vassal_undecided",
		[], "I need you to give me an answer now.", "lord_become_vassal_persuasion_begin",
		[
			(call_script, "script_troop_get_vassalage_availability_score", "$g_talk_troop", "$g_player_troop"),
			(quest_set_slot, "qst_persuade_lord_vassalage", slot_quest_value, reg0),
			(quest_set_slot, "qst_persuade_lord_vassalage", slot_quest_num_tries, quest_persuade_vassalge_max_proposition),

			(call_script, "script_troop_change_relation_with_troop", "$g_player_troop", "$g_talk_troop", -5),
		]],

	[anyone, "lord_become_vassal_persuasion_begin",
		[
			(troop_get_slot, ":vassal_of", "$g_talk_troop", slot_troop_vassal_of),
			(try_begin),
				(ge, ":vassal_of", 0),
				(str_store_string, s10, "@I feel like breaking my current oath with {s11} requires proper consideration."),
			(else_try),
				(str_store_string, s10, "@Swearing an oath is a serious matter that requires proper consideration."),
			(try_end),
		], "Your proposision has some merit but I don't feel I get enough out of it.^{s10}.^^Do you have something to persuade me.", "lord_become_vassal_persuasion_player_loop",
		[]],

	[anyone|plyr, "lord_become_vassal_persuasion_player_loop",
		[], "I would grant you a fief.", "lord_become_vassal_persuasion_grant_fief",
		[
		]],
	[anyone|plyr, "lord_become_vassal_persuasion_player_loop",
		[], "I would promise you a fief.", "lord_become_vassal_persuasion_answer_loop",
		[
			(call_script, "script_troop_become_vassal_promise_fief", "$g_talk_troop"),
		]],
	[anyone|plyr, "lord_become_vassal_persuasion_player_loop",
		[], "I would give you a title of nobility.", "lord_become_vassal_persuasion_answer_loop",
		[
			(call_script, "script_troop_become_vassal_grant_title", "$g_talk_troop"),
		]],
	[anyone|plyr, "lord_become_vassal_persuasion_player_loop",
		[], "I would garrantee your safety and that of your domain.", "lord_become_vassal_persuasion_answer_loop",
		[
			(call_script, "script_troop_become_vassal_promise_safety", "$g_talk_troop"),
		]],
	[anyone|plyr, "lord_become_vassal_persuasion_player_loop",
		[], "I would garrantee your prosperity and improve your financial situation.", "lord_become_vassal_persuasion_answer_loop",
		[
			(call_script, "script_troop_become_vassal_promise_prosperity", "$g_talk_troop"),
		]],
	[anyone|plyr, "lord_become_vassal_persuasion_player_loop",
		[], "I would improve your political standing.", "lord_become_vassal_persuasion_answer_loop",
		[
			(call_script, "script_troop_become_vassal_promise_standing", "$g_talk_troop"),
		]],
	[anyone|plyr, "lord_become_vassal_persuasion_player_loop",
		[], "I would give you many opportunities to prove your worth.", "lord_become_vassal_persuasion_answer_loop",
		[
			(call_script, "script_troop_become_vassal_promise_glory", "$g_talk_troop"),
		]],
	[anyone|plyr, "lord_become_vassal_persuasion_player_loop",
		[], "I would in turn give you opportunities to have your own vassals.", "lord_become_vassal_persuasion_answer_loop",
		[
			(call_script, "script_troop_become_vassal_promise_vassals", "$g_talk_troop"),
		]],
	[anyone|plyr, "lord_become_vassal_persuasion_player_loop",
		[], "If you are not with me, you are against me.", "lord_become_vassal_persuasion_answer_loop",
		[
			(call_script, "script_troop_become_vassal_threaten", "$g_talk_troop"),
		]],
	[anyone|plyr, "lord_become_vassal_persuasion_player_loop",
		[], "Let's leave it at that.", "lord_become_vassal_persuasion_answer_loop",
		[
			(quest_get_slot, ":num_tries", "qst_persuade_lord_vassalage", slot_quest_num_tries),

			(store_mul, ":value_bonus", ":num_tries", 5),
			(store_div, ":relation_bonus", ":num_tries", 2),

            (call_script, "script_quest_add_value", "qst_persuade_lord_vassalage", ":value_bonus"),

			(call_script, "script_troop_change_relation_with_troop", "$g_player_troop", "$g_talk_troop", ":relation_bonus"),

			(quest_set_slot, "qst_persuade_lord_vassalage", slot_quest_num_tries, 0),
		]],

	[anyone, "lord_become_vassal_persuasion_grant_fief",
		[], "I suppose you have a specific one in mind ?.", "lord_become_vassal_persuasion_grant_fief_player_choice",
		[
		]],
	[anyone|plyr|repeat_for_parties, "lord_become_vassal_persuasion_grant_fief_player_choice",
		[
			(store_repeat_object, ":party_repeat"),
			(is_between, ":party_repeat", centers_begin, centers_end),
			(party_slot_eq, ":party_repeat", slot_party_leader, "$g_player_troop"),
			(neg|troop_slot_eq, "$g_player_troop", slot_troop_home, ":party_repeat"),
			(str_store_party_name, s10, ":party_repeat"),
		], "{s10}", "lord_become_vassal_persuasion_answer_loop",
		[
			(store_repeat_object, ":party_repeat"),
			(call_script, "script_troop_become_vassal_grant_fief", "$g_talk_troop", ":party_repeat"),
		]],
	[anyone|plyr, "lord_become_vassal_persuasion_grant_fief_player_choice",
		[], "Nevermind", "lord_become_vassal_persuasion_answer_loop",
		[]],

	[anyone, "lord_become_vassal_persuasion_answer_loop",
		[
			(quest_get_slot, ":num_tries", "qst_persuade_lord_vassalage", slot_quest_num_tries),
			(call_script, "script_troop_get_become_vassal_answer", "$g_talk_troop"),
			(this_or_next|eq, reg0, outcome_failure),
			(le, ":num_tries", 0),
			(le, reg0, outcome_neutral),
		], "I've heard enough, we should stop wasting each others's time.", "lord_main_return",
		[
			(call_script, "script_troop_change_relation_with_troop", "$g_player_troop", "$g_talk_troop", -5),
			(call_script, "script_fail_quest", "qst_persuade_lord_vassalage"),
			(call_script, "script_complete_quest", "qst_persuade_lord_vassalage"),
			(troop_set_slot, "$g_talk_troop", slot_troop_become_vassal_tried, become_vassal_try_failed_persuasion),
			(call_script, "script_get_current_day"),
			(troop_set_slot, "$g_talk_troop", slot_troop_become_vassal_last_try, reg0),
		]],

	[anyone, "lord_become_vassal_persuasion_answer_loop",
		[
			(call_script, "script_troop_get_become_vassal_answer", "$g_talk_troop"),
			(eq, reg0, outcome_success),
		], "You've convinced me.", "lord_main_return",
		[
			(quest_get_slot, ":lord", "qst_persuade_lord_vassalage", slot_quest_object),
			(call_script, "script_troop_become_vassal", "$g_talk_troop", ":lord"),
			(call_script, "script_troop_apply_persuade_vassal_quest", "$g_talk_troop"),
			(call_script, "script_succeed_quest", "qst_persuade_lord_vassalage"),
			(call_script, "script_complete_quest", "qst_persuade_lord_vassalage"),
			(troop_set_slot, "$g_talk_troop", slot_troop_become_vassal_tried, 0),
		]],

	[anyone, "lord_become_vassal_persuasion_answer_loop",
		[(str_store_string, s10, "@Interesting, keep going")], "{s10}.", "lord_become_vassal_persuasion_player_loop",
		[
			(quest_get_slot, ":num_tries", "qst_persuade_lord_vassalage", slot_quest_num_tries),
			(val_sub, ":num_tries", 1),
			(quest_set_slot, "qst_persuade_lord_vassalage", slot_quest_num_tries, ":num_tries"),
		]],

	[anyone, "lord_ask_opinion",
		[], "Very well.", "player_lord_ask_opinion", []],

	[anyone|plyr, "player_lord_ask_opinion",
		[], "What do you think of the war ?", "lord_ask_opinion_war", []],
	[anyone|plyr, "player_lord_ask_opinion",
		[
			(store_troop_faction, ":troop_faction", "$g_talk_troop"),
			(is_between, ":troop_faction", kingdoms_begin, kingdoms_end),
			(store_troop_faction, ":player_faction", "$g_player_troop"),
			(eq, ":troop_faction", ":player_faction"),
			(faction_get_slot, ":leader", ":troop_faction", slot_faction_leader),
			(gt, ":leader", 0),
			(str_store_troop_name, s10, ":leader"),
		], "What do you think of your liege {s10} ?", "lord_ask_opinion_liege", []], # our liege as in the leader of the faction
	[anyone|plyr, "player_lord_ask_opinion",
		[
			(troop_get_slot, ":leader", "$g_talk_troop", slot_troop_vassal_of),
			(gt, ":leader", 0),
			(str_store_troop_name, s10, ":leader"),
		], "What do you think of your lord {s10} ?", "lord_ask_opinion_leader", []], # His liege as in his direct superior
	[anyone|plyr, "player_lord_ask_opinion",
		[], "What do you think of our marshall ?", "lord_ask_opinion_marshall", []],
	# [anyone|plyr, "",
	# 	[], "", "", []],
	# [anyone|plyr, "",
	# 	[], "", "", []],
	# [anyone|plyr, "",
	# 	[], "", "", []],
	[anyone|plyr, "player_lord_ask_opinion",
		[], "Nevermind", "lord_main_return", []],

	[anyone, "lord_ask_opinion_war",
		[], "Same as everyone else, it's a bad, but necessary means to an end.", "lord_main_return", []],
	[anyone, "lord_ask_opinion_liege",
		[], "Nothing you want to hear.", "lord_main_return", []],
	[anyone, "lord_ask_opinion_leader",
		[], "The same as you.", "lord_main_return", []],
	[anyone, "lord_ask_opinion_marshall",
		[], "I don't think we have a marshall do we ?", "lord_main_return", []],
	
	[anyone, "lord_ask_vassal",
		[(eq, "$g_dialog_outcome", vassal_outcome_too_many),], "I'm afraid I have no room for you in my court.", "lord_ask_vassal_too_many", []],
	[anyone, "lord_ask_vassal",
		[(eq, "$g_dialog_outcome", vassal_outcome_unknown),], "I do not know your worth.", "lord_ask_vassal_unknown", []],
	[anyone, "lord_ask_vassal",
		[(eq, "$g_dialog_outcome", vassal_outcome_refused),], "I wouldn't want someone like you on my court.", "lord_main_return", []],
	[anyone, "lord_ask_vassal",
		[(eq, "$g_dialog_outcome", vassal_outcome_no_fief),], "I have room in my court for someone like you, unfortunatly I would not be able to grant you property.", "lord_ask_vassal_no_fief", []],
	[anyone, "lord_ask_vassal",
		[
			(eq, "$g_dialog_outcome", vassal_outcome_accepted),
			(call_script, "script_troop_get_relation_with_troop", "$g_talk_troop", "$g_player_troop"),
			(assign, ":relation", reg0),
			(lt, ":relation", 20),
		], "I think you could make use of your skills.", "lord_ask_vassal_no_fief",
		[
		]],
	[anyone, "lord_ask_vassal",
		[(eq, "$g_dialog_outcome", vassal_outcome_accepted),], "I would be glad to have you in my court.", "lord_ask_vassal_no_fief", []],
	
	[anyone, "lord_ask_vassal_unknown",
		[], "Take the fight to my enemies and prove yourself as a fine leader of men and I might reconsider.", "lord_main_return", []],

	[anyone, "lord_ask_vassal_too_many",
		[], "I'm afraid I have no place for you in my court.", "lord_main_return", []],

	[anyone, "lord_ask_vassal_no_fief", [
		(store_troop_faction, ":troop_faction", "$g_talk_troop"),
		(faction_get_slot, ":faction_leader", ":troop_faction", slot_faction_leader),
		(neq, ":faction_leader", "$g_talk_troop"),
	], "Now, should our liege bestow onto me a fief adequate for your status I could reward you in due time.", "lord_ask_vassal_ready_pledge", []],
	[anyone, "lord_ask_vassal_no_fief", [], "Keep in mind I do generously reward my most loyal followers, if you work hard and make a better name for yourself you will be granted a fief in due time.", "lord_ask_vassal_ready_pledge", []],

	[anyone, "lord_ask_vassal_ready_pledge", [
		(quest_set_slot, "qst_swear_vassalage_fief", slot_quest_object, "$g_object_outcome"),
		(call_script, "script_start_quest", "qst_swear_vassalage_fief", "$g_talk_troop"),
	], "Are you ready to take the oath then?", "player_lord_offer_vassal_answer", []],

	[anyone, "duel_request",
		[], "A duel? You think I will allow you an honourable death? Ah! I will crush you and your pathetic excuse of an army.", "close_window", 
		[(party_set_slot, "$g_talk_party", slot_party_speak_allowed, 0),
		 (encounter_attack),]],
	[anyone, "duel_ask",
		[], "I do not think a duel is what I want right now, did you have anything else in mind ?", "player_lord_main", []],

	[anyone, "player_lord_demands",
		[], "And what are those demands ?", "player_give_demands", []],
	[anyone|plyr, "player_give_demands",
		[], "That you surrender your men and weapons and come quietly with me !", "lord_ask_surrender", []],
	[anyone|plyr, "player_give_demands",
		[], "Nevermind, forget I said anything.", "lord_demands_return", []],

	[anyone, "lord_demands_return", 
		[], "I thought as much.", "player_lord_greeting_after", []],
	[anyone, "lord_ask_surrender",
		[], "Ha! Surely you are stupid if you think I will surrender without a fight.", "close_window", 
		[(party_set_slot, "$g_talk_party", slot_party_speak_allowed, 0),
		 (encounter_attack),]],

	[anyone, "lord_debug",
		[], "DEBUG MENU", "player_lord_debug", []],

	[anyone|plyr, "player_lord_debug",
		[], "Debug party variables", "lord_debug", [
			(call_script, "script_party_get_prefered_wages_limit", "$g_encountered_party"),
			(display_message, "@Wanted wages: {reg0}; Min wages: {reg1}; Max wages: {reg2}"),
			(call_script, "script_party_get_wages", "$g_encountered_party"),
			(display_message, "@Current wages: {reg0}"),
			(store_faction_of_party, ":current_party_faction", "$g_encountered_party"),
			(str_store_faction_name, s10, ":current_party_faction"),
			(display_message, "@Party faction: {s10}"),
			(faction_get_slot, reg10, ":current_party_faction", slot_faction_is_at_war),
			(display_message, "@Faction at war: {reg10}"),
			(party_get_slot, ":leader", "$g_encountered_party", slot_party_leader),
			(try_begin),
				(ge, ":leader", 0),
				(troop_get_slot, ":home", ":leader", slot_troop_home),
				(try_begin),
					(is_between, ":home", centers_begin, centers_end),
					(str_store_party_name, s10, ":home"),
				(else_try),
					(assign, reg10, ":home"),
					(str_store_string, s10, "@-- {reg10} --"),
				(try_end),
				(display_message, "@Home: {s10}"),
				(troop_get_slot, reg10, ":leader", slot_troop_rank),
				(display_message, "@Rank: {reg10}"),
				(store_troop_faction, ":troop_faction", ":leader"),
				(str_store_faction_name, s10, ":troop_faction"),
				(display_message, "@Faction: {s10}"),
				(troop_get_slot, reg10, ":leader", slot_troop_kingdom_occupation),
				(display_message, "@Occupation {reg10}"),
			(try_end),
		]],
	[anyone|plyr, "player_lord_debug",
		[], "Go back", "lord_main_return", []],

	[anyone|plyr, "player_lord_offer_vassal",
		[], "I have yes", "lord_offer_vassal", []],
	[anyone|plyr, "player_lord_offer_vassal",
		[], "Yes, my lord", "lord_offer_vassal", []],
	[anyone|plyr, "player_lord_offer_vassal",
		[], "I don't think I have", "lord_offer_vassal_explain", []],

	[anyone, "lord_offer_vassal",
		[
			(quest_get_slot, ":fief", "qst_swear_vassalage_fief", slot_quest_object),
			(str_store_party_name, s11, ":fief"),
		], "You know then of my offer, your oath of vassalage, with the fief of {s11} to lord over. Are you ready to pledge your oath to me?", "player_lord_offer_vassal_answer", []],
	[anyone, "lord_offer_vassal_explain",
		[
			(quest_get_slot, ":fief", "qst_swear_vassalage_fief", slot_quest_object),
			(str_store_party_name, s11, ":fief"),
			], "That is most unfortunate... To be brief I would like your sword by my side, an offer to pledge your vassalage to me.^On top of this you would be granted the fief of {s11} to lord over. Are you ready to give me your oath?", "player_lord_offer_vassal_answer", []],

	[anyone|plyr, "player_lord_offer_vassal_answer",
		[], "I am, my Lord.", "lord_offer_vassal_accept", []],
	[anyone|plyr, "player_lord_offer_vassal_answer",
		[], "I'm afraid I need more time to think this over.", "lord_offer_vassal_refused", []],
	
	[anyone, "lord_offer_vassal_accept",
		[
			(store_troop_faction, ":troop_faction", "$g_talk_troop"),
			(str_store_faction_name, s11, ":troop_faction"),
			(try_begin),
				(faction_slot_eq, ":troop_faction", slot_faction_leader, "$g_talk_troop"),
				(str_store_string, s10, "@lawful ruler of {s11}"),
			(else_try),
				(faction_slot_eq, ":troop_faction", slot_faction_leader, "$g_talk_troop"),
				(str_store_string, s10, "@vassal of {s11}"),
			(try_end),
		], "Good. Then repeat the words of the oath with me: I swear homage to you as {s10}.", "player_lord_offer_vassal_oath", []],
	
	[anyone|plyr, "player_lord_offer_vassal_oath",
		[
			(store_troop_faction, ":troop_faction", "$g_talk_troop"),
			(str_store_faction_name, s11, ":troop_faction"),
			(try_begin),
				(faction_slot_eq, ":troop_faction", slot_faction_leader, "$g_talk_troop"),
				(str_store_string, s10, "@lawful ruler of {s11}"),
			(else_try),
				(faction_slot_eq, ":troop_faction", slot_faction_leader, "$g_talk_troop"),
				(str_store_string, s10, "@vassal of {s11}"),
			(try_end),
		], "I swear homage to you as {s10}.", "lord_offer_vassal_oath_1", []],
	[anyone|plyr, "player_lord_offer_vassal_oath",
		[], "Excuse me, sir. But I feel I need to think about this.", "lord_offer_vassal_give_up", []],

	[anyone, "lord_offer_vassal_oath_1",
		[], "I will remain as your loyal and devoted {man/follower} as long as my breath remains....", "player_lord_offer_vassal_oath_1", []],
	[anyone|plyr, "player_lord_offer_vassal_oath_1",
		[], "I will remain as your loyal and devoted {man/follower} as long as my breath remains...", "lord_offer_vassal_oath_2", []],
	[anyone|plyr, "player_lord_offer_vassal_oath_1",
		[], "Excuse me, sir. But I feel I need to think about this.", "lord_offer_vassal_give_up", []],

	[anyone, "lord_offer_vassal_oath_2",
		[], "...and I will be at your side to fight your enemies should you need my sword.", "player_lord_offer_vassal_oath_2", []],
	[anyone|plyr, "player_lord_offer_vassal_oath_2",
		[], "...and I will be at your side to fight your enemies should you need my sword.", "lord_offer_vassal_oath_3", []],
	[anyone|plyr, "player_lord_offer_vassal_oath_2",
		[], "Sir, may I ask for some time to think about this?", "lord_offer_vassal_give_up", []],

	[anyone, "lord_offer_vassal_oath_3",
		[], "Finally, I will uphold your lawful claims and those of your legitimate heirs.", "player_lord_offer_vassal_oath_3", []],
	[anyone|plyr, "player_lord_offer_vassal_oath_3",
		[], "Finally, I will uphold your lawful claims and those of your legitimate heirs.", "lord_offer_vassal_oath_end_1", []],
	[anyone|plyr, "player_lord_offer_vassal_oath_3",
		[], "Sir, I must have more time to consider this.", "lord_offer_vassal_give_up", []],

	[anyone, "lord_offer_vassal_oath_end_1",
		[
			(call_script, "script_succeed_quest", "qst_swear_vassalage_fief"),
		], "Very well. You have given me your solemn oath, {playername}. May you uphold it always, with proper courage and devotion.", "lord_offer_vassal_oath_end_2", []],
	[anyone, "lord_offer_vassal_oath_end_2",
		[
			(quest_get_slot, ":fief", "qst_swear_vassalage_fief", slot_quest_object),
			(try_begin),
				(is_between, ":fief", centers_begin, centers_end),
				(str_store_party_name, s11, ":fief"),
				(assign, reg10, 1),
			(else_try),
				(str_clear, s11),
				(assign, reg10, 0),
			(try_end),
		], "Let it be known that from this day forward, you are my sworn {man/follower} and vassal.\
 I give you my protection and grant you the right to bear arms in my name, and I pledge that I shall not deprive you of your life, liberty or properties except by the lawful judgment of your peers or by the law and custom of the land. {reg10?Furthermore I give you the fief of {s11} with all its rents and revenues.:}", "lord_offer_vassal_oath_end_3", []],
	[anyone, "lord_offer_vassal_oath_end_3",
		[], "You have done a wise thing, {playername}. Serve me well and I promise, you will rise high.", "player_lord_offer_vassal_oath_end", []],
	[anyone|plyr, "player_lord_offer_vassal_oath_end",
		[], "I thank you my lord.", "lord_offer_vassal_oath_conclude", []],
	[anyone, "lord_offer_vassal_oath_conclude",
		[], "I have great hopes for you {playername}.\
 I know you shall prove yourself worthy of the trust I have placed in you.", "close_window",
		[
			(quest_get_slot, ":center", "qst_swear_vassalage_fief", slot_quest_object),
			(try_begin),
				(is_between, ":center", centers_begin, centers_end),
				(call_script, "script_troop_give_center_to_troop", "$g_talk_troop", ":center", "$g_player_troop"),
			(else_try),
				(call_script, "script_troop_become_vassal", "$g_player_troop", "$g_talk_troop"),
			(try_end),
			(call_script, "script_complete_quest", "qst_swear_vassalage_fief"),
		]],

	[anyone, "lord_offer_vassal_refused",
		[], "A shame, I had expected more from you... Nevermind, it's probably for the best.", "close_window",
		[
			(quest_get_slot, ":center", "qst_swear_vassalage_fief", slot_quest_object),
			(try_begin),
				(is_between, ":center", centers_begin, centers_end),
				(party_set_slot, ":center", slot_party_reserved, -1),
			(try_end),
			(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "$g_player_troop", -5),
			(call_script, "script_cancel_quest", "qst_swear_vassalage_fief"),
		]],
	[anyone, "lord_offer_vassal_give_up",
		[
			(call_script, "script_fail_quest", "qst_swear_vassalage_fief"),
		], "What are you playing at, {playername}? Go and make up your mind, and stop wasting my time.", "close_window",
		[
			(quest_get_slot, ":center", "qst_swear_vassalage_fief", slot_quest_object),
			(try_begin),
				(is_between, ":center", centers_begin, centers_end),
				(party_set_slot, ":center", slot_party_reserved, -1),
			(try_end),
			(call_script, "script_troop_change_relation_with_troop", "$g_talk_troop", "$g_player_troop", -25),
			(call_script, "script_complete_quest", "qst_swear_vassalage_fief"),
		]],

	###############
	# Bandit talk #
	###############
	[anyone, "start",
		[
			(store_faction_of_party, ":party_faction", "$g_talk_party"),
			(is_between, ":party_faction", "fac_faction_1", "fac_kingdom_1"),
			(encountered_party_is_attacker),
			(troop_get_type, reg10, "$g_player_troop"),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_greetings_aggressive_forest"),
		 ], "{s0}", "bandit_player_talk", []],
	[anyone, "start",
		[
			(store_faction_of_party, ":party_faction", "$g_talk_party"),
			(is_between, ":party_faction", "fac_faction_1", "fac_kingdom_1"),
			(troop_get_type, reg10, "$g_player_troop"),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_greetings_defensive_forest"),
		 ], "{s0}", "bandit_player_talk_aggressive", []],

	[anyone|plyr, "bandit_player_talk",
		[
			(store_troop_gold, ":gold", "$g_player_troop"),
			(gt, ":gold", 500),
			(call_script, "script_game_get_money_text", 500),
			(str_store_string_reg, s10, s0),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_player_give_gold_forest"),
		], "{s0}", "bandit_give_gold",[]],
	[anyone|plyr, "bandit_player_talk",
		[
			(store_troop_gold, ":gold", "$g_player_troop"),
			(gt, ":gold", 1200),
			(val_div, ":gold", 2),
			(call_script, "script_game_get_money_text", ":gold"),
			(str_store_string_reg, s10, s0),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_player_give_gold_half_forest"),
		], "{s0}", "bandit_give_gold_half",[]],
	[anyone|plyr, "bandit_player_talk",
		[
			(store_troop_gold, ":gold", "$g_player_troop"),
			(gt, ":gold", 100),
			(call_script, "script_game_get_money_text", ":gold"),
			(str_store_string_reg, s10, s0),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_player_give_gold_all_forest"),
		], "{s0}", "bandit_give_gold_all",[]],
	[anyone|plyr, "bandit_player_talk",
		[
			(store_troop_gold, ":gold", "$g_player_troop"),
			(le, ":gold", 100),
			(gt, ":gold", 0),
			(call_script, "script_game_get_money_text", ":gold"),
			(str_store_string_reg, s10, s0),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_player_give_gold_low_forest"),
		], "{s0}", "bandit_give_gold_low",[]],
	[anyone|plyr, "bandit_player_talk",
		[
			(store_troop_gold, ":gold", "$g_player_troop"),
			(le, ":gold", 0),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_player_give_gold_nothing_forest"),
		], "{s0}", "bandit_give_gold_nothing",[]],
	[anyone|plyr, "bandit_player_talk",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_player_fight_forest"),], "{s0}", "bandit_fight", []],
	
	[anyone, "bandit_give_gold_low",
		[
			(call_script, "script_troop_get_gold_rating", "$g_player_troop", "$g_talk_troop"),
			(assign, ":estimated_gold", reg0),
			(store_troop_gold, ":gold", "$g_player_troop"),
			(val_mul, ":estimated_gold", 100),
			(val_div, ":estimated_gold", ":gold"),
			(ge, ":estimated_gold", 75),
			(call_script, "script_party_group_calculate_strength", "p_main_party"),
			# We add strength and defense 
			(assign, ":player_strength", reg0),
			(val_add, ":player_strength", reg1),
			(call_script, "script_party_group_calculate_strength", "$g_talk_party"),
			(assign, ":bandits_strength", reg0),
			(val_add, ":bandits_strength", reg1),
			(store_mul, ":ratio", ":bandits_strength", 100),
			(val_div, ":ratio", ":player_strength"),
			(gt, ":ratio", 65),

			(val_add, ":ratio", ":estimated_gold"),
			(val_div, ":ratio", 2),
			(ge, ":ratio", 85),

			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_refuse_low_money_forest"),
		], "{s0}", "bandit_demand_all", []],
	[anyone, "bandit_give_gold_low",
		[
			(store_troop_gold, ":gold", "$g_player_troop"),
			(troop_remove_gold, "$g_player_troop", ":gold"),
			(party_get_slot, ":party_wealth", "$g_talk_party", slot_party_wealth),
			(val_add, ":party_wealth", ":gold"),
			(party_set_slot, "$g_talk_party", slot_party_wealth, ":party_wealth"),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_accept_low_money_forest"),
		], "{s0}.", "close_window", [(leave_encounter),]],
	# ToDo: Bandits can refuse gold, thinking there is more
	[anyone, "bandit_give_gold",
		[
			(assign, ":gold", 500),
			(troop_remove_gold, "$g_player_troop", ":gold"),
			(party_get_slot, ":party_wealth", "$g_talk_party", slot_party_wealth),
			(val_add, ":party_wealth", ":gold"),
			(party_set_slot, "$g_talk_party", slot_party_wealth, ":party_wealth"),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_accept_gold_forest"),
		], "{s0}", "close_window", [(leave_encounter),]],
	[anyone, "bandit_give_gold_half",
		[
			(store_troop_gold, ":gold", "$g_player_troop"),
			(val_div, ":gold", 2),
			(troop_remove_gold, "$g_player_troop", ":gold"),
			(party_get_slot, ":party_wealth", "$g_talk_party", slot_party_wealth),
			(val_add, ":party_wealth", ":gold"),
			(party_set_slot, "$g_talk_party", slot_party_wealth, ":party_wealth"),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_accept_gold_half_forest"),
		], "{s0}", "close_window", [(leave_encounter),]],
	[anyone, "bandit_give_gold_all",
		[
			(store_troop_gold, ":gold", "$g_player_troop"),
			(troop_remove_gold, "$g_player_troop", ":gold"),
			(party_get_slot, ":party_wealth", "$g_talk_party", slot_party_wealth),
			(val_add, ":party_wealth", ":gold"),
			(party_set_slot, "$g_talk_party", slot_party_wealth, ":party_wealth"),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_accept_gold_all_forest"),
		], "{s0}", "close_window", [(leave_encounter),]],
	[anyone, "bandit_give_all",
		[
			(store_troop_gold, ":gold", "$g_player_troop"),
			(troop_remove_gold, "$g_player_troop", ":gold"),
			(party_get_slot, ":party_wealth", "$g_talk_party", slot_party_wealth),
			(val_add, ":party_wealth", ":gold"),
			(party_set_slot, "$g_talk_party", slot_party_wealth, ":party_wealth"),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_accept_all_forest"),
		], "{s0}", "close_window", [(leave_encounter),]],
	[anyone|plyr, "bandit_demand_all",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_player_give_all_forest"),], "{s0}", "bandit_give_all", []],
	[anyone|plyr, "bandit_demand_all",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_player_give_nothing_forest"),], "{s0}", "bandit_fight", []],
	# ToDo: Bandits can let go of player, thinking they gain nothing for robbing
	# Or they can chose to take one of the player's item/companion
	[anyone, "bandit_give_gold_nothing",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_refuse_nothing_forest"),], "{s0}", "close_window", 
		[
			(party_set_slot, "$g_talk_party", slot_party_speak_allowed, 0),
			(encounter_attack),
		]],
	[anyone, "bandit_fight",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_fight_aggressive_forest"),], "{s0}", "close_window", [(party_set_slot, "$g_talk_party", slot_party_speak_allowed, 0),(encounter_attack),]],

	[anyone|plyr, "bandit_player_talk_aggressive",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_fight_forest"),], "{s0}", "bandit_player_attack", []],
	[anyone|plyr, "bandit_player_talk_aggressive",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_recruit_forest"),], "{s0}", "bandit_player_ask_join", []],
	[anyone|plyr, "bandit_player_talk_aggressive",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_rob_forest"),], "{s0}", "bandit_player_rob", []],
	# [anyone|plyr, "bandit_player_talk_aggressive",
	# 	[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_bounty_forest"),], "{s0}", "close_window", []],
	[anyone|plyr, "bandit_player_talk_aggressive",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_nevermind_forest"),], "{s0}", "close_window", [(leave_encounter),]],

	[anyone, "bandit_player_attack",
		[
			(call_script, "script_party_bargain", "p_main_party", "$g_talk_party", 100, bargain_type_strength, -10), 
			(ge, reg0, outcome_neutral), 
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_ask_bargain_forest"),
		], "{s0}", "bandit_player_agressive_bargain", []],
	[anyone, "bandit_player_attack",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_fight_back_forest"),], "{s0}", "close_window", [(party_set_slot, "$g_talk_party", slot_party_speak_allowed, 0),(encounter_attack),]],

	[anyone|plyr, "bandit_player_agressive_bargain",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_attack_no_bargain_forest"),], "{s0}", "close_window", [(party_set_slot, "$g_talk_party", slot_party_speak_allowed, 0),(encounter_attack),]],
	[anyone|plyr, "bandit_player_agressive_bargain",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_attack_recruit_forest"),], "{s0}", "bandit_player_ask_join", []],
	[anyone|plyr, "bandit_player_agressive_bargain",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_attack_rob_forest"),], "{s0}", "bandit_player_rob", []],
	[anyone|plyr, "bandit_player_agressive_bargain",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_attack_ask_surrender_forest"),], "{s0}", "bandit_player_ask_surrender", []],
	[anyone|plyr, "bandit_player_agressive_bargain",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_attack_nevermind_forest"),], "{s0}", "close_window", [(leave_encounter),]],


	[anyone, "bandit_player_ask_surrender",
		[
			(call_script, "script_party_bargain", "p_main_party", "$g_talk_party", 100, bargain_type_strength, -40),
			(assign, "$g_dialog_outcome", reg0),
			(eq, "$g_dialog_outcome", outcome_success),
			(call_script, "script_party_group_take_party_group_prisoner", "p_main_party", "$g_talk_party"),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_surrender_forest"),
		], "{s0}", "close_window", [(leave_encounter),]],
	[anyone, "bandit_player_ask_surrender",
		[(eq, "$g_dialog_outcome", outcome_neutral),(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_surrender_leave_men_forest"),], "{s0}", "bandit_player_ask_surrender_accept_leave_men", []],
	[anyone, "bandit_player_ask_surrender",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_surrender_not_forest"),], "{s0}", "close_window", [(party_set_slot, "$g_talk_party", slot_party_speak_allowed, 0),(encounter_attack),]],
	[anyone, "bandit_player_ask_join",
		[
			(call_script, "script_troop_bargain", "$g_player_troop", "$g_talk_troop", 100, bargain_type_strength, -25), 
			(ge, reg0, outcome_neutral),
			(distribute_party_among_party_group, "$g_talk_party", "p_main_party"),
			(party_clear, "$g_talk_party"),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_ask_join_accept_forest"),
			# ToDo: if neutral outcome, need penalities for recruiting, chance to escape or morale maluses (temporary -5/-10 "trouble making")
		], "{s0}", "close_window", [(leave_encounter),]],
	[anyone, "bandit_player_ask_join",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_ask_join_refuse_forest"),], "{s0}", "close_window", [(party_set_slot, "$g_talk_party", slot_party_speak_allowed, 0),(encounter_attack),]],
	[anyone, "bandit_player_rob",
		[
			(call_script, "script_party_bargain", "p_main_party", "$g_talk_party", 100, bargain_type_strength, -10), 
			(assign, "$g_dialog_outcome", reg0),
			(ge, "$g_dialog_outcome", outcome_neutral), 
			(call_script, "script_party_get_total_wealth", "$g_talk_party", 1),
			(assign, ":gold", reg0),
			(ge, ":gold", 50),
			(try_begin),
				(eq, "$g_dialog_outcome", outcome_neutral),
				(val_div, ":gold", 3),
			(try_end),
			(call_script, "script_party_remove_gold", "$g_talk_party", ":gold"),
			(assign, ":player_gold", reg0),
			(troop_add_gold, "$g_player_troop", ":player_gold"),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_rob_give_all_forest"),
		], "{s0}", "close_window", [(leave_encounter),]],
	[anyone, "bandit_player_rob",
		[
			(ge, "$g_dialog_outcome", outcome_neutral),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_rob_give_item_forest"),
		], "{s0}", "close_window", [
			(troop_clear_inventory, "trp_temp_troop"),
			(call_script, "script_troop_copy_items_from_troop", "trp_temp_troop", "$g_talk_troop"),
			(change_screen_loot, "trp_temp_troop"),
		]],
	[anyone, "bandit_player_rob",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_player_rob_give_not_forest"),], "{s0}", "close_window", [(party_set_slot, "$g_talk_party", slot_party_speak_allowed, 0),(encounter_attack),]],

	[anyone|plyr, "bandit_player_ask_surrender_accept_leave_men",
		[(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_surrender_leave_men_accept_forest"),], "{s0}", "close_window", [

			(call_script, "script_party_take_troop_prisoner", "p_main_party", "$g_talk_troop", "$g_talk_party", 1),
			(call_script, "script_troop_change_honor", "$g_player_troop", 1),
			(party_clear, "$g_talk_party"),
			# ToDo: scatter old party
			(leave_encounter),
		]],
	[anyone|plyr, "bandit_player_ask_surrender_accept_leave_men",
		[
			(call_script, "script_party_group_take_party_group_prisoner", "p_main_party", "$g_talk_party"),
			(call_script, "script_troop_change_honor", "$g_player_troop", -2),
			(call_script, "script_get_bandit_dialog", "$g_talk_party", "str_bandit_defensive_surrender_leave_men_refuse_forest"),
		], "{s0}", "close_window", [
			(leave_encounter),
		]],


	################
	# Patrol talks #
	################
	[anyone, "start",
		[
			(party_get_slot, ":party_type", "$g_talk_party", slot_party_type),
			(eq, ":party_type", spt_patrol),
			(encountered_party_is_attacker),
			(party_get_slot, ":linked_center", "$g_talk_party", slot_party_linked_party),
			(store_faction_of_party, ":party_faction", "$g_talk_party"),
			(try_begin),
				(is_between, ":linked_center", centers_begin, centers_end),
				(party_get_slot, ":lord", ":linked_center", slot_party_lord),
				(is_between, ":lord", lords_begin, lords_end),
				(str_store_troop_name, s10, ":lord"),
			(else_try),
				(is_between, ":party_faction", kingdoms_begin, kingdoms_end),
				(faction_get_slot, ":faction_leader", "$g_talk_party", slot_faction_leader),
				(is_between, ":faction_leader", lords_begin, lords_end),
				(str_store_troop_name, s10, ":faction_leader"),
			(else_try),
				(str_store_faction_name, s11, ":party_faction"),
				(str_store_string, s10, "@the {s11}"),
			(try_end),
		], "Stop, in the name of {s10} ! Surrender your weapons and we won't have to take your life.", "patrol_player_attacked", 
		[]],

	[anyone|plyr, "patrol_player_attacked",
		[
		], "We won't go down without a fight", "close_window",
		[
			(encounter_attack),
		]],

	[anyone, "start", 
		[
			(party_get_slot, ":party_type", "$g_talk_party", slot_party_type),
			(eq, ":party_type", spt_patrol),
			# (party_get_slot, ":linked_center", "$g_talk_party", slot_party_linked_party),
			(store_faction_of_party, ":party_faction", "$g_talk_party"),
			(store_faction_of_party, ":player_faction", "p_main_party"),
			(eq, ":player_faction", ":party_faction"),
			(str_store_troop_name, s10, "trp_player"),
		], "Greetings {s10}, what brings you here ?", "patrol_player_friendly", 
		[]],

	[anyone|plyr, "patrol_player_friendly",
		[
		], "Just passing through.", "close_window",
		[
			(leave_encounter),
		]],

	[anyone, "start",
		[
			(party_get_slot, ":party_type", "$g_talk_party", slot_party_type),
			(eq, ":party_type", spt_patrol),
			(party_get_slot, ":linked_center", "$g_talk_party", slot_party_linked_party),
			(store_faction_of_party, ":party_faction", "$g_talk_party"),
			(try_begin),
				(is_between, ":linked_center", centers_begin, centers_end),
				(party_get_slot, ":lord", ":linked_center", slot_party_lord),
				(is_between, ":lord", lords_begin, lords_end),
				(str_store_troop_name, s10, ":lord"),
			(else_try),
				(is_between, ":party_faction", kingdoms_begin, kingdoms_end),
				(faction_get_slot, ":faction_leader", "$g_talk_party", slot_faction_leader),
				(is_between, ":faction_leader", lords_begin, lords_end),
				(str_store_troop_name, s10, ":faction_leader"),
			(else_try),
				(str_store_faction_name, s11, ":party_faction"),
				(str_store_string, s10, "@the {s11}"),
			(try_end),
		], "These men are under the protection of {s10}. State your business traveller.", "patrol_player_neutral",
		[]],

	[anyone|plyr, "patrol_player_neutral",
		[
		], "Nevermind. You may go.", "close_window",
		[
			(leave_encounter),
		]],

	#################
	# Caravan talks #
	#################
	[anyone, "start",
		[
			(party_get_slot, ":party_type", "$g_talk_party", slot_party_type),
			(eq, ":party_type", spt_caravan),

			(try_begin),
				(call_script, "script_cf_debug", debug_current|debug_economy),
				(str_store_party_name, s10, "$g_encountered_party"),
				(party_get_slot, ":origin_center", "$g_encountered_party", slot_party_linked_party),
				(str_store_party_name, s11, ":origin_center"),
				(party_get_slot, ":mission_objective", "$g_encountered_party", slot_party_mission_object),
				(try_begin),
					(is_between, ":mission_objective", centers_begin, centers_end),
					(str_store_party_name, s12, ":mission_objective"),
				(else_try),
					(str_store_string, s12, "@unknown"),
				(try_end),
				(display_message, "@{s10} from {s11} heading for {s12}"),
			(try_end),

			(call_script, "script_get_dialog_caravan_intro", "$g_encountered_party"),
		], "{s0}", "caravan_player",
		[]],

	[anyone|plyr, "caravan_player", [], "What goods are you trading ?", "caravan_trade", []],

	[anyone|plyr, "caravan_player", [(party_slot_eq, "$g_encountered_party", slot_party_player_shakedown, 1),], "I've changed my mind, I'll take everything from you", "caravan_toll_attack", []],

	[anyone|plyr, "caravan_player",
		[
			(store_troop_faction, ":player_faction", "$g_player_troop"),
			(store_faction_of_party, ":party_faction", "$g_encountered_party"),
			(neq, ":player_faction", ":party_faction"),
			(party_slot_eq, "$g_encountered_party", slot_party_player_shakedown, 0),
		], "This road has a toll, you need to pay up.", "caravan_toll", []],

	[anyone|plyr, "caravan_player",
		[], "Nevermind. You may go.", "close_window",
		[
			(leave_encounter),
		]],

	[anyone, "caravan_trade",
		[(call_script, "script_get_dialog_caravan_trade", "$g_encountered_party"),], "{s0}", "caravan_player", []],

	[anyone, "caravan_toll",
		[(call_script, "script_get_dialog_caravan_toll", "$g_encountered_party"),(eq, 1, 0),], "[INVALID DIALOG]", "close_window", []],
	[anyone, "caravan_toll",
		[(eq, reg0, outcome_success),], "{s0}", "caravan_toll_player_success", []],
	[anyone, "caravan_toll",
		[(eq, reg0, outcome_neutral),], "{s0}", "caravan_toll_player_swear", []],
	[anyone, "caravan_toll",
		[(eq, reg0, outcome_failure),], "{s0}", "caravan_toll_player_failed", []],

	[anyone|plyr, "caravan_toll_player_success", [], "Hand it over and no one gets hurt.", "caravan_toll_pay", []],
	[anyone|plyr, "caravan_toll_player_success", [], "No, I want everything you have and I'll take it from your corpse.", "caravan_toll_attack", []],
	[anyone|plyr, "caravan_toll_player_success", [], "Nevermind, keep your gold.", "caravan_toll_back", []],

	[anyone|plyr, "caravan_toll_player_swear", [], "You have my word.", "caravan_toll_pay", []],
	[anyone|plyr, "caravan_toll_player_swear", [], "I'll just have to take it from your corpse then.", "caravan_toll_attack", []],
	[anyone|plyr, "caravan_toll_player_swear", [], "Nevermind, keep your gold.", "caravan_toll_back", []],

	[anyone, "caravan_toll_pay", [
		(call_script, "script_party_transfer_wealth", "$g_encountered_party", "$g_player_party", reg1, tax_type_none),
		(party_set_slot, "$g_encountered_party", slot_party_speak_allowed, 0),
		(party_set_slot, "$g_encountered_party", slot_party_player_shakedown, 1),
	], "Here is your money, I will not bid you farewell and hope we don't see each other again.", "close_window", []],

	[anyone|plyr, "caravan_toll_player_failed", [], "I'll just have to take it from your corpse then.", "caravan_toll_attack", []],
	[anyone|plyr, "caravan_toll_player_failed", [], "Nevermind, keep your gold.", "caravan_toll_back", []],

	[anyone, "caravan_toll_attack", [], "We won't go down without a fight.", "close_window", [
		(encounter_attack),
	]],
	[anyone, "caravan_toll_back", [], "Fine then, did you have something else in mind ?", "caravan_player", []],

	#################
	# Error dialogs #
	#################
	[anyone, "start",
		[], "Hello there traveller! [WARNING: MISSING DIALOG]", "error_dialog", []],

	[anyone|plyr, "error_dialog", [], "Dialog Error. No dialog found.", "close_window", []],
	
	# [anyone, "event_triggered",
		# [(display_debug_message, "@Event triggered"),], "Hail traveller. It's a pleasure to meet you, what is your name?.", "player_greeting", []],
	# [anyone, "party_relieved",
		# [(display_debug_message, "@Party relieved"),], "Hail traveller. It's a pleasure to meet you, what is your name?.", "player_greeting", []],
	# [anyone, "prisoner_liberated",
		# [(display_debug_message, "@Prisoner liberated"),], "Hail traveller. It's a pleasure to meet you, what is your name?.", "player_greeting", []],
	# [anyone, "enemy_defeated",
		# [(display_debug_message, "@Enemy defeated"),], "Hail traveller. It's a pleasure to meet you, what is your name?.", "player_greeting", []],
	
	###############
	# Member chat #
	###############
	[anyone, "member_chat",
		[
			(store_conversation_troop, "$g_talk_troop"),
			(eq, 0, 1),
		], "!No dialog", "close_window", []],
	[anyone, "member_chat",
		[(troop_equip_items, "$g_talk_troop"), # TEST
		], "Yes {My Lord/My Lady}?", "member_chat_player", []],
	[anyone|plyr, "member_chat_player",
		[
		], "Show me your stats.", "member_chat_end",
		[
			# (change_screen_view_character, "$g_talk_troop"),
			(change_screen_view_character),
		]],
	[anyone|plyr, "member_chat_player",
		[
		], "Show me your items.", "member_chat_end",
		[
			(troop_clear_inventory, "trp_temp_troop"),
			(call_script, "script_troop_copy_items_from_troop", "trp_temp_troop", "$g_talk_troop"),
			(change_screen_loot, "trp_temp_troop"),
		]],
	[anyone|plyr, "member_chat_player",
		[], "Nothing.", "close_window",
		[]],
	[anyone, "member_chat_end",
		[], "Anything else {My Lord/My Lady}?", "member_chat_player", []],

	#################
	# Prisoner chat #
	#################
	[anyone, "prisoner_chat",
		[
			(store_conversation_troop, "$g_talk_troop"),
			(eq, 0, 1),
		], "!No dialog", "close_window", []],
	[anyone, "prisoner_chat",
		[], "What do you want ?", "prisoner_chat_player", []],
	[anyone|plyr, "prisoner_chat_player",
		[], "Stay put", "close_window", []],
	[anyone|plyr, "prisoner_chat_player",
		[(troop_is_hero, "$g_talk_troop"),], "You are free to go", "close_window", [(call_script, "script_troop_freed", "$g_talk_troop", -1),]],
]
