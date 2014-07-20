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
			(eq, 0, 1),
		], "Yo_Dawg, yo' ass should not read this!", "close_window", []],
	
	[anyone, "start", 
		[
			(is_between, "$g_talk_troop", lords_begin, lords_end),
		], "Hail traveller, my name is {s10}. It's a pleasure to meet you.", "player_greeting", []],
	
	[anyone, "start", 
		[], "Hail traveller. It's a pleasure to meet you, what is your name?.", "player_greeting", []],
	
	[anyone|plyr, "player_greeting",
		[], "My name is {playername}, the pleasure is shared.", "close_window", []],
	[anyone|plyr, "player_greeting",
		[], "Back off peasant!", "close_window", []],

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
		[
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
			(change_screen_trade),
			# (change_screen_trade, "$g_talk_troop"),
		]],
	
	[anyone|plyr, "member_chat_player",
		[], "Nothing.", "close_window",
		[]],
	
	[anyone, "member_chat_end",
		[], "Anything else {My Lord/My Lady}?", "member_chat_player", []],
]