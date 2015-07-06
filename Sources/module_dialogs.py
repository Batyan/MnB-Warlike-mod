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
			(store_encountered_party, "$g_encountered_party"),
			(store_encountered_party2, "$g_encountered_party_2"),
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
		], "I am {s10}, {s11}. I wish to know your name so that I can write something else than 'someone who dared cross my path' on your grave.", "player_greeting_attacked", 
		[
			(store_current_hours, ":date"),
			(troop_set_slot, "$g_talk_troop", slot_troop_last_met, ":date"),
		]],
	
	[anyone, "start",
		[ 
			(encountered_party_is_attacker),
			(is_between, "$g_talk_troop", lords_begin, lords_end),
		], "{playername}... We meet again, do you have anything to say before I crush you?.", "player_greeting_attacked", []],
	
	[anyone, "start", 
		[
			(is_between, "$g_talk_troop", lords_begin, lords_end),
			(troop_slot_eq, "$g_talk_troop", slot_troop_last_met, -1),
			(call_script, "script_troop_get_title_string", "$g_talk_troop"),
			(str_store_string_reg, s11, s0),
			(str_store_troop_name, s10, "$g_talk_troop"),
		], "Hail traveller. It's a pleasure to meet you, I am {s10}, {s11}. What is your name?", "player_greeting", 
		[
			(store_current_hours, ":date"),
			(troop_set_slot, "$g_talk_troop", slot_troop_last_met, ":date"),
		]],
	
	[anyone, "start", 
		[(le, "$g_last_met_hours", 6),], "Hello again traveller. What is it that you need?", "player_talk_lord", []],
	
	[anyone, "start", 
		[], "Hmm... {playername}, yes? What do you need?", "player_talk_lord", []],
	
	[anyone|plyr, "player_greeting",
		[], "My name is {playername}, the pleasure is shared.", "player_greeting_after", []],
	[anyone|plyr, "player_greeting",
		[], "Back off peasant!", "close_window", []],
	
	[anyone, "player_greeting_after",
		[], "Now... What do you need?", "player_talk_lord", []],
	
	[anyone|plyr, "player_greeting_attacked",
		[], "My name is of no matter to you, now send your dogs so that I can kill them.", "close_window", []],
	[anyone|plyr, "player_greeting_attacked",
		[], "I am {playername}, prepare your men for the battle it shall be interesting.", "close_window", []],
	[anyone|plyr, "player_greeting_attacked",
		[], "I am {playername} and I demand to settle this with a duel.", "duel_request", []],
	
	# Main lord talk (player)
	[anyone|plyr, "player_talk_lord",
		[], "I must take my leave.", "close_window", []],
	
	
	[anyone, "duel_request",
		[], "A duel? You think I will allow you an honourable death? Ah! I will crush you and your pathetic excuse of an army.", "close_window", []],

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
			(call_script, "script_troop_copy_items_from_troop", "trp_temp_troop", "$g_talk_troop"),
			(change_screen_trade, "trp_temp_troop"),
			(troop_clear_inventory, "trp_temp_troop"),
			# (change_screen_trade, "$g_talk_troop"),
		]],
	
	[anyone|plyr, "member_chat_player",
		[], "Nothing.", "close_window",
		[]],
	
	[anyone, "member_chat_end",
		[], "Anything else {My Lord/My Lady}?", "member_chat_player", []],
]