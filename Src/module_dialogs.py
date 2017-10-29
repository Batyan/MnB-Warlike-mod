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





dialogs = [
	[anyone, "start", 
		[
			(store_conversation_troop, "$g_talk_troop"),

			
			(store_current_hours, ":date"),
			(troop_get_slot, ":last_met", "$g_talk_troop", slot_troop_last_met),
			(try_begin),
				(neq, ":last_met", -1),
				(store_sub, "$g_last_met_hours", ":date", ":last_met"),
				(troop_set_slot, "$g_talk_troop", slot_troop_last_met, ":date"),
			(try_end),
			
			(eq, 0, 1),
		], "Yo_Dawg, yo' ass should not read this!", "close_window", []],
	
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
			(store_current_hours, ":date"),
			(troop_set_slot, "$g_talk_troop", slot_troop_last_met, ":date"),
		]],
	
	[anyone, "start",
		[ 
			(encountered_party_is_attacker),
			(is_between, "$g_talk_troop", lords_begin, lords_end),
		], "{playername}... We meet again, do you have anything to say before I crush you?", "player_lord_greeting_attacked", []],
	
	[anyone, "start", 
		[
			(is_between, "$g_talk_troop", lords_begin, lords_end),
			(troop_slot_eq, "$g_talk_troop", slot_troop_last_met, -1),
			(call_script, "script_troop_get_title_string", "$g_talk_troop"),
			(str_store_string_reg, s11, s0),
			(str_store_troop_name, s10, "$g_talk_troop"),
		], "Hail traveller. It's a pleasure to meet you, I am {s10}, {s11}. What is your name?", "player_lord_greeting", 
		[
			(store_current_hours, ":date"),
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
		[], "I would like to know something.", "lord_ask", []],
	[anyone|plyr, "player_lord_main",
		[], "Let us talk for a bit.", "lord_talk", []],
	[anyone|plyr, "player_lord_main",
		[], "I am here to deliver you my demands !", "player_lord_demands", []],
	[anyone|plyr, "player_lord_main",
		[], "How about we have a duel ?", "duel_ask", []],
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
		[], "Nevermind", "lord_main_return", []],

	[anyone, "lord_rumors",
		[], "Nothing new I'm afraid.", "lord_main_return", []],

	[anyone, "lord_ask_opinion",
		[], "Very well.", "player_lord_ask_opinion", []],

	[anyone|plyr, "player_lord_ask_opinion",
		[], "What do you think of the war ?", "lord_ask_opinion_war", []],
	[anyone|plyr, "player_lord_ask_opinion",
		[], "What do you think of our liege ?", "lord_ask_opinion_liege", []], # our liege as in the leader of the faction
	[anyone|plyr, "player_lord_ask_opinion",
		[], "What do you think of your liege ?", "lord_ask_opinion_leader", []], # His liege as in his direct superior
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

	[anyone, "start",
		[(store_faction_of_party, ":party_faction", "$g_talk_party"),
		 (is_between, ":party_faction", "fac_faction_1", "fac_kingdom_1"),
		 (troop_get_type, reg10, "trp_player"),], "Your money or your life {reg10?lass:lad}!", "bandit_player_talk", []],

	[anyone|plyr, "bandit_player_talk",
		[
			(store_troop_gold,":gold","trp_player"),
			(gt,":gold",500),
		], "Here take it and leave me alone!", "bandit_give_gold",[]],

	[anyone|plyr, "bandit_player_talk",
		[], "Take it if you can!", "bandit_fight", []],

	[anyone, "bandit_give_gold",
		[], "Easy money...", "close_window", 
		[
			(troop_remove_gold,"trp_player",500),
			(leave_encounter),
		]],
	[anyone, "bandit_fight",
		[], "Just how I like it!", "close_window", [(party_set_slot, "$g_talk_party", slot_party_speak_allowed, 0),]],

    [anyone|plyr, "start", [], "Dialog Error. No dialog found.", "close_window", []],
	
	[anyone, "start",
		[
		], "Hello there traveller! [WARNING: INCORRECT DIALOG]", "close_window",
		[
		]],
	
	# [anyone, "event_triggered",
		# [(display_debug_message, "@Event triggered"),], "Hail traveller. It's a pleasure to meet you, what is your name?.", "player_greeting", []],
	# [anyone, "party_relieved",
		# [(display_debug_message, "@Party relieved"),], "Hail traveller. It's a pleasure to meet you, what is your name?.", "player_greeting", []],
	# [anyone, "prisoner_liberated",
		# [(display_debug_message, "@Prisoner liberated"),], "Hail traveller. It's a pleasure to meet you, what is your name?.", "player_greeting", []],
	# [anyone, "enemy_defeated",
		# [(display_debug_message, "@Enemy defeated"),], "Hail traveller. It's a pleasure to meet you, what is your name?.", "player_greeting", []],
	
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
]