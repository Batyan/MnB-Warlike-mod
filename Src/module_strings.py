




strings = [

    ###############
    ## Hardcoded ##
	###############
  ("no_string", "NO STRING!"),
  ("empty_string", " "),
  ("yes", "Yes."),
  ("no", "No."),
  ("blank_string", " "),
  ("ERROR_string", "{!}ERROR!!!ERROR!!!!ERROR!!!ERROR!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!ERROR!!!ERROR!!!!!"),
  ("noone", "no one"),
  ("s0", "{!}{s0}"),
  ("blank_s1", "{!} {s1}"),
  ("reg1", "{!}{reg1}"),
  ("s50_comma_s51", "{!}{s50}, {s51}"),
  ("s50_and_s51", "{s50} and {s51}"),
  ("s52_comma_s51", "{!}{s52}, {s51}"),
  ("s52_and_s51", "{s52} and {s51}"),
  ("s5_s_party", "{s5}'s Party"),

  ("given_by_s1_at_s2", "Given by {s1} at {s2}"),
  ("given_by_s1_in_wilderness", "Given by {s1} whilst in the field"),
  ("s7_raiders", "{s7} Raiders"),

  ("bandits_eliminated_by_another", "The troublesome bandits have been eliminated by another party."),
  ("msg_battle_won","Battle won! Press tab key to leave..."),
  ("tutorial_map1","You are now viewing the overland map. Left-click on the map to move your party to that location, enter the selected town, or pursue the selected party. Time will pause on the overland map if your party is not moving, waiting or resting. To wait anywhere simply press and hold down the space bar."),

  ("change_color_1", "{!}Change Color 1"),
  ("change_color_2", "{!}Change Color 2"),
  ("change_background", "{!}Change Background Pattern"),
  ("change_flag_type", "{!}Change Flag Type"),
  ("change_map_flag_type", "{!}Change Map Flag Type"),
  ("randomize", "Randomize"),
  ("sample_banner", "{!}Sample banner:"),
  ("sample_map_banner", "{!}Sample map banner:"),
  ("number_of_charges", "{!}Number of charges:"),
  ("change_charge_1",       "{!}Change Charge 1"),
  ("change_charge_1_color", "{!}Change Charge 1 Color"),
  ("change_charge_2",       "{!}Change Charge 2"),
  ("change_charge_2_color", "{!}Change Charge 2 Color"),
  ("change_charge_3",       "{!}Change Charge 3"),
  ("change_charge_3_color", "{!}Change Charge 3 Color"),
  ("change_charge_4",       "{!}Change Charge 4"),
  ("change_charge_4_color", "{!}Change Charge 4 Color"),
  ("change_charge_position", "{!}Change Charge Position"),
  ("choose_position", "{!}Choose position:"),
  ("choose_charge", "{!}Choose a charge:"),
  ("choose_background", "{!}Choose background pattern:"),
  ("choose_flag_type", "{!}Choose flag type:"),
  ("choose_map_flag_type", "{!}Choose map flag type:"),
  ("choose_color", "{!}Choose color:"),
  ("accept", "{!}Accept"),
  ("charge_no_1", "{!}Charge #1:"),
  ("charge_no_2", "{!}Charge #2:"),
  ("charge_no_3", "{!}Charge #3:"),
  ("charge_no_4", "{!}Charge #4:"),
  ("change", "{!}Change"),
  ("color_no_1", "{!}Color #1:"),
  ("color_no_2", "{!}Color #2:"),
  ("charge", "Charge"),
  ("color", "Color"),
  ("flip_horizontal", "Flip Horizontal"),
  ("flip_vertical", "Flip Vertical"),
  ("hold_fire", "Hold Fire"),
  ("blunt_hold_fire", "Blunt / Hold Fire"),

##  ("tutorial_camp1","This is training ground where you can learn the basics of the game. Use A, S, D, W keys to move and the mouse to look around."),
##  ("tutorial_camp2","F is the action key. You can open doors, talk to people and pick up objects with F key. If you wish to leave a town or retreat from a battle, press the TAB key."),
##  ("tutorial_camp3","Training Ground Master wishes to speak with you about your training. Go near him, look at him and press F when you see the word 'Talk' under his name. "),
##  ("tutorial_camp4","To see the in-game menu, press the Escape key. If you select Options, and then Controls from the in-game menu, you can see a complete list of key bindings."),
##  ("tutorial_camp6","You've received your first quest! You can take a look at your current quests by pressing the Q key. Do it now and check the details of your quest."),
##  ("tutorial_camp7","You've completed your quest! Go near Training Ground Master and speak with him about your reward."),
##  ("tutorial_camp8","You've gained some experience and weapon points! Press C key to view your character and increase your weapon proficiencies."),
##  ("tutorial_camp9","Congratulations! You've finished the tutorial of Mount&Blade. Press TAB key to leave the training ground."),

##  ("tutorial_enter_melee", "You are entering the melee weapon training area. The chest nearby contains various weapons which you can experiment with. If you wish to quit this tutorial, press TAB key."),
##  ("tutorial_enter_ranged", "You are entering the ranged weapon training area.  The chest nearby contains various ranged weapons which you can experiment with. If you wish to quit this tutorial, press TAB key."),
##  ("tutorial_enter_mounted", "You are entering the mounted training area. Here, you can try different kinds of weapons while riding a horse. If you wish to quit this tutorial, press TAB key."),

#  ("tutorial_usage_sword", "Sword is a very versatile weapon which is very fast in both attack and defense. Usage of one handed swords are affected by your one handed weapon proficiency. Focus on the sword and press F key to pick it up."),
#  ("tutorial_usage_axe", "Axe is a heavy (and therefore slow) weapon which can deal high damage to the opponent. Usage of one handed axes are affected by your one handed weapon proficiency. Focus on the axe and press F key to pick it up."),
#  ("tutorial_usage_club", "Club is a blunt weapon which deals less damage to the opponent than any other one handed weapon, but it knocks you opponents unconscious so that you can take them as a prisoner. Usage of clubs are affected by your one handed weapon proficiency. Focus on the club and press F key to pick it up."),
#  ("tutorial_usage_battle_axe", "Battle axe is a long weapon and it can deal high damage to the opponent. Usage of battle axes are affected by your two handed weapon proficiency. Focus on the battle axe and press F key to pick it up."),
#  ("tutorial_usage_spear", "Spear is a very long weapon which lets the wielder to strike the opponent earlier. Usage of the spears are affected by your polearm proficiency. Focus on the spear and press F key to pick it up."),
#  ("tutorial_usage_short_bow", "Short bow is a common ranged weapon which is easy to reload but hard to master at. Usage of short bows are affected by your archery proficiency. Focus on the short bow and arrows and press F key to pick them up."),
#  ("tutorial_usage_crossbow", "Crossbow is a heavy ranged weapon which is easy to use and deals high amount of damage to the opponent. Usage of crossbows are affected by your crossbow proficiency. Focus on the crossbow and bolts and press F key to pick them up."),
#  ("tutorial_usage_throwing_daggers", "Throwing daggers are easy to use and throwing them takes a very short time. But they deal light damage to the opponent. Usage of throwing daggers are affected byyour throwing weapon proficiency. Focus on the throwing daggers and press F key to pick it up."),
#  ("tutorial_usage_mounted", "You can use your weapons while you're mounted. Polearms like the lance here can be used for couched damage against opponents. In order to do that, ride your horse at a good speed and aim at your enemy. But do not press the attack button."),

##  ("tutorial_melee_chest", "The chest near you contains some of the melee weapons that can be used throughout the game. Look at the chest now and press F key to view its contents. Click on the weapons and move them to your Arms slots to be able to use them."),
##  ("tutorial_ranged_chest", "The chest near you contains some of the ranged weapons that can be used throughout the game. Look at the chest now and press F key to view its contents. Click on the weapons and move them to your Arms slots to be able to use them."),
##
##  ("tutorial_item_equipped", "You have equipped a weapon. Move your mouse scroll wheel up to wield your weapon. You can also switch between your weapons using your mouse scroll wheel."),

  ("tutorial_ammo_refilled", "Ammo refilled."),
  ("tutorial_failed", "You have been beaten this time, but don't worry. Follow the instructions carefully and you'll do better next time.\
 Press the Tab key to return to to the menu where you can retry this tutorial."),

  ("tutorial_1_msg_1","{!}In this tutorial you will learn the basics of movement and combat.\
 In Mount&Blade: Warband, you use the mouse to control where you are looking, and W, A, S, and D keys of your keyboard to move.\
 Your first task in the training is to locate the yellow flag in the room and move over it.\
 You can press the Tab key at any time to quit this tutorial or to exit any other area in the game.\
 Go to the yellow flag now."),
  ("tutorial_1_msg_2","{!}Well done. Next we will cover attacking with weapons.\
 For the purposes of this tutorial you have been equipped with bow and arrows, a sword and a shield.\
 You can draw different weapons from your weapon slots by using the scroll wheel of your mouse.\
 In the default configuration, scrolling up pulls out your next weapon, and scrolling down pulls out your shield.\
 If you are already holding a shield, scrolling down will put your shield away instead.\
 Try changing your wielded equipment with the scroll wheel now. When you are ready,\
 go to the yellow flag to move on to your next task."),
  ("tutorial_1_msg_3","{!}Excellent. The next part of this tutorial covers attacking with melee weapons.\
 You attack with your currently wielded weapon by using your left mouse button.\
 Press and hold the button to ready an attack, then release the button to strike.\
 If you hold down the left mouse button for a while before releasing, your attack will be more powerful.\
 Now draw your sword and destroy the four dummies in the room."),
  ("tutorial_1_msg_4","{!}Nice work! You've destroyed all four dummies. You can now move on to the next room."),
  ("tutorial_1_msg_5","{!}As you see, there is an archery target on the far side of the room.\
 Your next task is to use your bow to put three arrows into that target. Press and hold down the left mouse button to notch an arrow.\
 You can then fire the arrow by releasing the left mouse button. Note the targeting reticule in the centre of your screen,\
 which shows you the accuracy of your shot.\
 In order to achieve optimal accuracy, let fly your arrow when the reticule is at its smallest.\
 Try to shoot the target now."),
  ("tutorial_1_msg_6","{!}Well done! You've learned the basics of moving and attacking.\
 With a little bit of practice you will soon master them.\
 In the second tutorial you can learn more advanced combat skills and face armed opponents.\
 You can press the Tab key at any time to return to the tutorial menu."),

  ("tutorial_2_msg_1","{!}This tutorial will teach you how to defend yourself with a shield and how to battle armed opponents.\
 For the moment you are armed with nothing but a shield.\
 Your task is not to attack, but to successfully protect yourself from harm with your shield.\
 There is an armed opponent waiting for you in the next room.\
 He will try his best to knock you unconscious, while you must protect yourself with your shield\
 by pressing and holding the right mouse button.\
 Go into the next room now to face your opponent.\
 Remember that you can press the Tab key at any time to quit this tutorial or to exit any other area in the game."),
  ("tutorial_2_msg_2","{!}Press and hold down the right mouse button to raise your shield. Try to remain standing for twenty seconds. You have {reg3} seconds to go."),
  ("tutorial_2_msg_3","{!}Well done, you've succeeded in defending against an armed opponent.\
 The next phase of this tutorial will pit you and your shield against a force of enemy archers.\
 Move on to the next room when you're ready to face an archer."),
  ("tutorial_2_msg_4","{!}Defend yourself from arrows by raising your shield with the right mouse button. Try to remain standing for twenty seconds. You have {reg3} seconds to go."),
  ("tutorial_2_msg_5","{!}Excellent, you've put up a succesful defence against the archer.\
 There is a reward waiting for you in the next room."),
  ("tutorial_2_msg_6","{!}In the default configuration,\
 the F key on your keyboard is used for non-violent interaction with objects and humans in the gameworld.\
 To pick up the sword on the altar, look at it and press F when you see the word 'Equip'."),
  ("tutorial_2_msg_7","{!}A fine weapon! Now you can use it to deliver a bit of payback.\
 Go back through the door and dispose of the archer you faced earlier."),
  ("tutorial_2_msg_8","{!}Very good. Your last task before finishing this tutorial is to face the maceman.\
 Go through the door now and show him your steel!"),
  ("tutorial_2_msg_9","{!}Congratulations! You have now learned how to defend yourself with a shield and even had your first taste of combat with armed opponents.\
 Give it a bit more practice and you'll soon be a renowned swordsman.\
 The next tutorial covers directional defence, which is one of the most important elements of Mount&Blade: Warband combat.\
 You can press the Tab key at any time to return to the tutorial menu."),

  ("tutorial_3_msg_1","{!}This tutorial is intended to give you an overview of parrying and defence without a shield.\
 Parrying attacks with your weapon is a little bit more difficult than blocking them with a shield.\
 When you are defending with a weapon, you are only protected from one direction, the direction in which your weapon is set.\
 If you are blocking upwards, you will parry any overhead swings coming against you, but you will not stop thrusts or attacks to your sides.\
 Either of these attacks would still be able to hit you.\
 That's why, in order to survive without a shield, you must learn directional defence.\
 Go pick up the quarterstaff by pressing the F key now to begin practice."),
  ("tutorial_3_msg_2","{!}By default, the direction in which you defend (by clicking and holding your right mouse button) is determined by the attack direction of your closest opponent.\
 For example, if your opponent is readying a thrust attack, pressing and holding the right mouse button will parry thrust attacks, but not side or overhead attacks.\
 You must watch your opponent carefully and only initiate your parry AFTER the enemy starts to attack.\
 If you start BEFORE he readies an attack, you may parry the wrong way altogether!\
 Now it's time for you to move on to the next room, where you'll have to defend yourself against an armed opponent.\
 Your task is to defend yourself successfully for twenty seconds with no equipment other than a simple quarterstaff.\
 Your quarterstaff's attacks are disabled for this tutorial, so don't worry about attacking and focus on your defence instead.\
 Move on to the next room when you are ready to initiate the fight."),
  ("tutorial_3_msg_3","{!}Press and hold down the right mouse button to defend yourself with your staff after your opponent starts his attack.\
 Try to remain standing for twenty seconds. You have {reg3} seconds to go."),
  ("tutorial_3_msg_4","{!}Well done, you've succeeded this trial!\
 Now you will be pitted against a more challenging opponent that will make things more difficult for you.\
 Move on to the next room when you're ready to face him."),
  ("tutorial_3_msg_5","{!}Press and hold down the right mouse button to defend yourself with your staff after your opponent starts his attack.\
 Try to remain standing for twentys seconds. You have {reg3} seconds to go."),
  ("tutorial_3_msg_6","{!}Congratulations, you still stand despite the enemy's best efforts.\
 The time has now come to attack as well as defend.\
 Approach the door and press the F key when you see the text 'Next level'."),

  ("tutorial_3_2_msg_1","{!}Your staff's attacks have been enabled again. Your first opponent is waiting in the next room.\
 Defeat him by a combination of attack and defence."),
  ("tutorial_3_2_msg_2","{!}Defeat your opponent with your quarterstaff."),
  ("tutorial_3_2_msg_3","{!}Excellent. Now the only thing standing in your way is one last opponent.\
 He is in the next room. Move in and knock him down."),
  ("tutorial_3_2_msg_4","{!}Defeat your opponent with your quarterstaff."),
  ("tutorial_3_2_msg_5","{!}Well done! In this tutorial you have learned how to fight ably without a shield.\
 Train hard and train well, and no one shall be able to lay a stroke on you.\
 In the next tutorial you may learn horseback riding and cavalry combat.\
 You can press the Tab key at any time to return to the tutorial menu."),

  ("tutorial_4_msg_1","{!}Welcome to the fourth tutorial.\
 In this sequence you'll learn about riding a horse and how to perform various martial exercises on horseback.\
 We'll start by getting you mounted up.\
 Approach the horse, and press the 'F' key when you see the word 'Mount'."),
  ("tutorial_4_msg_2","{!}While on horseback, W, A, S, and D keys control your horse's movement, not your own.\
 Ride your horse and try to follow the yellow flag around the course.\
 When you reach the flag, it will move to the next waypoint on the course until you reach the finish."),
  ("tutorial_4_msg_3","{!}Very good. Next we'll cover attacking enemies from horseback. Approach the yellow flag now."),
  ("tutorial_4_msg_4","{!}Draw your sword (using the mouse wheel) and destroy the two targets.\
 Try hitting the dummies as you pass them at full gallop -- this provides an extra challenge,\
 but the additional speed added to your blow will allow you to do more damage.\
 The easiest way of doing this is by pressing and holding the left mouse button until the right moment,\
 releasing it just before you pass the target."),
  ("tutorial_4_msg_5","{!}Excellent work. Now let us try some target shooting from horseback. Go near the yellow flag now."),
  ("tutorial_4_msg_6","{!}Locate the archery target beside the riding course and shoot it three times with your bow.\
 Although you are not required to ride while shooting, it's recommended that you try to hit the target at various speeds and angles\
 to get a feel for how your horse's speed and course affects your aim."),
  ("tutorial_4_msg_7","{!}Congratulations, you have finished this tutorial.\
 You can press the Tab key at any time to return to the tutorial menu."),
# Ryan END

  ("tutorial_5_msg_1","{!}TODO: Follow order to the flag"),
  ("tutorial_5_msg_2","{!}TODO: Move to the flag, keep your units at this position"),
  ("tutorial_5_msg_3","{!}TODO: Move to the flag to get the archers"),
  ("tutorial_5_msg_4","{!}TODO: Move archers to flag1, infantry to flag2"),
  ("tutorial_5_msg_5","{!}TODO: Enemy is charging. Fight!"),
  ("tutorial_5_msg_6","{!}TODO: End of battle."),

  ("trainer_help_1", "{!}This is a training ground where you can learn the basics of the game. Use W, A, S, and D keys to move and the mouse to look around."),
  ("trainer_help_2", "{!}To speak with the trainer, go near him, look at him and press the 'F' key when you see the word 'Talk' under his name.\
 When you wish to leave this or any other area or retreat from a battle, you can press the TAB key."),

  ("custom_battle_1", "{!}Lord Haringoth of Swadia is travelling with his household knights when he spots a group of raiders preparing to attack a small hamlet.\
 Shouting out his warcry, he spurs his horse forward, and leads his loyal men to a fierce battle."),
  ("custom_battle_2", "{!}Lord Mleza is leading a patrol of horsemen and archers\
 in search of a group of bandits who plundered a caravan and ran away to the hills.\
 Unfortunately the bandits have recently met two other large groups who want a share of their booty,\
 and spotting the new threat, they decide to combine their forces."),
  ("custom_battle_3", "{!}Lady Brina is leading the defense of her castle against a Swadian army.\
 Now, as the besiegers prepare for a final assault on the walls, she must make sure the attack does not succeed."),
  ("custom_battle_4", "{!}When the scouts inform Lord Grainwad of the presence of an enemy war band,\
 he decides to act quickly and use the element of surprise against superior numbers."),
  ("custom_battle_5", "{!}Lord Haeda has brought his fierce huscarls into the south with the promise of plunder.\
 If he can make this castle fall to him today, he will settle in these lands and become the ruler of this valley."),

  ("finished", "(Finished)"),

  ("delivered_damage", "Delivered {reg60} damage."),
  ("archery_target_hit", "Distance: {reg61} yards. Score: {reg60}"),
  
  ("use_baggage_for_inventory","Use your baggage to access your inventory during battle (it's at your starting position)."),
##  ("cant_leave_now","Can't leave the area now."),
  ("cant_use_inventory_now","Can't access inventory now."),
  ("cant_use_inventory_arena","Can't access inventory in the arena."),
  ("cant_use_inventory_disguised","Can't access inventory while you're disguised."),
  ("cant_use_inventory_tutorial","Can't access inventory in the training camp."),
  ("1_denar", "1 denar"),
  ("reg1_denars", "{reg1} denars"),
  ("january_reg1_reg2", "January {reg1}, {reg2}"),
  ("february_reg1_reg2", "February {reg1}, {reg2}"),
  ("march_reg1_reg2", "March {reg1}, {reg2}"),
  ("april_reg1_reg2", "April {reg1}, {reg2}"),
  ("may_reg1_reg2", "May {reg1}, {reg2}"),
  ("june_reg1_reg2", "June {reg1}, {reg2}"),
  ("july_reg1_reg2", "July {reg1}, {reg2}"),
  ("august_reg1_reg2", "August {reg1}, {reg2}"),
  ("september_reg1_reg2", "September {reg1}, {reg2}"),
  ("october_reg1_reg2", "October {reg1}, {reg2}"),
  ("november_reg1_reg2", "November {reg1}, {reg2}"),
  ("december_reg1_reg2", "December {reg1}, {reg2}"),

  ("back", "Back"),
  ("start_map", "Start Map"),

  ("party_morale_is_low", "Morale of some troops are low!"),
  ("weekly_report", "Weekly Report"),
  ("has_deserted_the_party", "has deserted the party."),
  ("have_deserted_the_party", "have deserted the party."),

  ("space", " "),
  ("s1_reg1", "{!}{s1} ({reg1})"),
  ("s1_reg2", "{!}{s1} ({reg2})"),
  ("s1_reg3", "{!}{s1} ({reg3})"),
  ("s1_reg4", "{!}{s1} ({reg4})"),
  ("s1_reg5", "{!}{s1} ({reg5})"),
  ("s1_reg6", "{!}{s1} ({reg6})"),
  ("s1_reg7", "{!}{s1} ({reg7})"),
  ("s1_reg8", "{!}{s1} ({reg8})"),
  ("s1_reg9", "{!}{s1} ({reg9})"),
  ("reg13", "{!}{reg13}"),
  ("reg14", "{!}{reg14}"),
  ("reg15", "{!}{reg15}"),
  ("reg16", "{!}{reg16}"),
  ("reg17", "{!}{reg17}"),
  ("reg18", "{!}{reg18}"),
  ("reg19", "{!}{reg19}"),
  ("reg20", "{!}{reg20}"),
  ("reg21", "{!}{reg21}"),
 
  ("number_of_troops_killed_reg1", "Number of troops killed: {reg1}"),
  ("number_of_troops_wounded_reg1", "Number of troops wounded: {reg1}"),
  ("number_of_own_troops_killed_reg1", "Number of friendly troops killed: {reg1}"),
  ("number_of_own_troops_wounded_reg1", "Number of friendly troops wounded: {reg1}"),
  
  
  
  
  
  ###########
  ## Other ##
  ###########
	
  # Male ranks
	("kingdom_rank_0", "Knight {s0}"),
	("kingdom_rank_1", "Knight {s0}"),
	("kingdom_rank_2", "Baron {s0}"),
	("kingdom_rank_3", "Viscount {s0}"),
	("kingdom_rank_4", "Count {s0}"),
	("kingdom_rank_5", "Duke {s0}"),
	("kingdom_rank_6", "Marshall {s0}"),
	("kingdom_rank_7", "King {s0}"),
	
	("khergit_rank_0", "Chieftain {s0}"),
	("khergit_rank_1", "Chief {s0}"),
	("khergit_rank_2", "War Chief {s0}"),
	("khergit_rank_3", "War Lord {s0}"),
	("khergit_rank_4", "Noyan {s0}"),
	("khergit_rank_5", "Az Khan {s0}"),
	("khergit_rank_6", "Il-Khan {s0}"),
	("khergit_rank_7", "{s0} Khan"),
	
	("nord_rank_0", "Berserker {s0}"),
	("nord_rank_1", "Veteran {s0}"),
	("nord_rank_2", "Noble {s0}"),
	("nord_rank_3", "Lesser Thane {s0}"),
	("nord_rank_4", "Thane {s0}"),
	("nord_rank_5", "Jarl {s0}"),
	("nord_rank_6", "Marshall {s0}"),
	("nord_rank_7", "King {s0}"),
	
	("rhodok_rank_0", "Patrician {s0}"),
	("rhodok_rank_1", "Burgher {s0}"),
	("rhodok_rank_2", "Elder {s0}"),
	("rhodok_rank_3", "Leader {s0}"),
	("rhodok_rank_4", "Gaffer {s0}"),
	("rhodok_rank_5", "Warden {s0}"),
	("rhodok_rank_6", "Marshall {s0}"),
	("rhodok_rank_7", "Governor {s0}"),
	
	("sarranid_rank_0", "{s0}"),
	("sarranid_rank_1", "Mamluke {s0}"),
	("sarranid_rank_2", "Lesser Noble {s0}"),
	("sarranid_rank_3", "Noble {s0}"),
	("sarranid_rank_4", "Emir {s0}"),
	("sarranid_rank_5", "Malik {s0}"),
	("sarranid_rank_6", "Caliph {s0}"),
	("sarranid_rank_7", "Sultan {s0}"),

  # Female ranks
  ("kingdom_rank_0_f", "Knight {s0}"),
  ("kingdom_rank_1_f", "Knight {s0}"),
  ("kingdom_rank_2_f", "Baroness {s0}"),
  ("kingdom_rank_3_f", "Viscountess {s0}"),
  ("kingdom_rank_4_f", "Countess {s0}"),
  ("kingdom_rank_5_f", "Duchess {s0}"),
  ("kingdom_rank_6_f", "Marshall {s0}"),
  ("kingdom_rank_7_f", "Queen {s0}"),
  
  ("khergit_rank_0_f", "Chieftain {s0}"),
  ("khergit_rank_1_f", "Chief {s0}"),
  ("khergit_rank_2_f", "War Chief {s0}"),
  ("khergit_rank_3_f", "War Lord {s0}"),
  ("khergit_rank_4_f", "Noyan {s0}"),
  ("khergit_rank_5_f", "Az Khan {s0}"),
  ("khergit_rank_6_f", "Il-Khan {s0}"),
  ("khergit_rank_7_f", "{s0} Khan"),
  
  ("nord_rank_0_f", "Berserker {s0}"),
  ("nord_rank_1_f", "Veteran {s0}"),
  ("nord_rank_2_f", "Noble {s0}"),
  ("nord_rank_3_f", "Lesser Thane {s0}"),
  ("nord_rank_4_f", "Thane {s0}"),
  ("nord_rank_5_f", "Jarl {s0}"),
  ("nord_rank_6_f", "Marshall {s0}"),
  ("nord_rank_7_f", "Queen {s0}"),
  
  ("rhodok_rank_0_f", "Patrician {s0}"),
  ("rhodok_rank_1_f", "Burgher {s0}"),
  ("rhodok_rank_2_f", "Elder {s0}"),
  ("rhodok_rank_3_f", "Leader {s0}"),
  ("rhodok_rank_4_f", "Gaffer {s0}"),
  ("rhodok_rank_5_f", "Warden {s0}"),
  ("rhodok_rank_6_f", "Marshall {s0}"),
  ("rhodok_rank_7_f", "Governor {s0}"),
  
  ("sarranid_rank_0_f", "{s0}"),
  ("sarranid_rank_1_f", "Mamluke {s0}"),
  ("sarranid_rank_2_f", "Lesser Noble {s0}"),
  ("sarranid_rank_3_f", "Noble {s0}"),
  ("sarranid_rank_4_f", "Emir {s0}"),
  ("sarranid_rank_5_f", "Malik {s0}"),
  ("sarranid_rank_6_f", "Caliph {s0}"),
  ("sarranid_rank_7_f", "Sultan {s0}"),

	
	("swadian_name_1", "Gallagus"),
	("swadian_name_2", "Klargus"),
	("swadian_name_3", "Mirchaud"),
	("swadian_name_4", "Richard"),
	("swadian_name_5", "Thibault"),
	("swadian_name_6", "Thiel"),
	("swadian_name_7", "Marcus"),
	("swadian_name_8", "Charles"),
	("swadian_name_9", "Romulus"),
	("swadian_name_10", "Luis"),
	("swadian_name_11", "Quintilus"),
	("swadian_name_12", "Edward"),
	("swadian_name_13", "Salius"),
	("swadian_name_14", "Gartimer"),
	("swadian_name_15", "Herald"),
	("swadian_name_16", "Haringoth"),
	("swadian_name_17", "Clais"),
	("swadian_name_18", "Deglan"),
	("swadian_name_19", "Tredian"),
	("swadian_name_20", "Grainwad"),
	("swadian_name_21", "Ryis"),
	("swadian_name_22", "Plais"),
	("swadian_name_23", "Stamar"),
	("swadian_name_24", "Meltor"),
	("swadian_name_25", "Beranz"),
	("swadian_name_26", "Rafard"),
	("swadian_name_27", "Regas"),
	("swadian_name_28", "Devlian"),
	("swadian_name_29", "Rafarch"),
	("swadian_name_30", "Rochabarth"),
	("swadian_name_31", "Despin"),
	("swadian_name_32", "Montewar"),
	("swadian_name_33", "Pechnack"),
	("swadian_name_34", "Baldur"),
	("swadian_name_35", "Copart"),
	("swadian_name_36", "Fouckard"),
	("swadian_name_37", "Turias"),
	("swadian_name_38", "Verrier"),
	("swadian_name_39", "Harlaus"),
	("swadian_name_40", "Herlard"),
	("swadian_name_41", "Julius"),
	("swadian_name_42", "Tulius"),
	("swadian_name_43", "Julian"),
	("swadian_name_44", "Kilian"),
	("swadian_name_45", "Maximilian"),
	("swadian_name_46", "Maximus"),
	# ("swadian_name_47", ""),
	# ("swadian_name_48", ""),
	# ("swadian_name_49", ""),
	# ("swadian_name_50", ""),
	# ("swadian_name_51", ""),
	# ("swadian_name_52", ""),
	# ("swadian_name_53", ""),
	# ("swadian_name_54", ""),
	# ("swadian_name_55", ""),
	# ("swadian_name_56", ""),
	# ("swadian_name_57", ""),
	# ("swadian_name_58", ""),
	# ("swadian_name_59", ""),
	# ("swadian_name_60", ""),
	# ("swadian_name_61", ""),
	# ("swadian_name_62", ""),
	# ("swadian_name_63", ""),
	# ("swadian_name_64", ""),
	# ("swadian_name_65", ""),
	# ("swadian_name_66", ""),
	# ("swadian_name_67", ""),
	# ("swadian_name_68", ""),
	# ("swadian_name_69", ""),
	
	("vaegir_name_1", "Yaroglek"),
	("vaegir_name_2", "Vuldrat"),
	("vaegir_name_3", "Naldera"),
	("vaegir_name_4", "Meriga"),
	("vaegir_name_5", "Khavel"),
	("vaegir_name_6", "Doru"),
	("vaegir_name_7", "Belgaru"),
	("vaegir_name_8", "Ralcha"),
	("vaegir_name_9", "Vlan"),
	("vaegir_name_10", "Mleza"),
	("vaegir_name_11", "Nelag"),
	("vaegir_name_12", "Crahask"),
	("vaegir_name_13", "Bracha"),
	("vaegir_name_14", "Druli"),
	("vaegir_name_15", "Marmun"),
	("vaegir_name_16", "Gastya"),
	("vaegir_name_17", "Harish"),
	("vaegir_name_18", "Taisa"),
	("vaegir_name_19", "Valishin"),
	("vaegir_name_20", "Rudin"),
	("vaegir_name_21", "Kumipa"),
	("vaegir_name_22", "Ralchad"),
	("vaegir_name_23", "Guro"),
	("vaegir_name_24", "Opnik"),
	("vaegir_name_25", "Vuloi"),
	("vaegir_name_26", "Kobyla"),
	("vaegir_name_27", "Gottorp"),
	("vaegir_name_28", "Pasch"),
	("vaegir_name_29", "Valdym"),
	("vaegir_name_30", "Dernyek"),
  ("vaegir_name_31", "Vern"),
  ("vaegir_name_32", "Raldym"),
  ("vaegir_name_33", "Igldaf"),
  ("vaegir_name_34", "Aethrod"),
  ("vaegir_name_35", "Geal"),
  # ("vaegir_name_36", ""),
  # ("vaegir_name_37", ""),
  # ("vaegir_name_38", ""),
  # ("vaegir_name_39", ""),
  # ("vaegir_name_40", ""),
	# ("vaegir_name_41", ""),
	
	("khergit_name_1", "Sanjar"),
	("khergit_name_2", "Alagur"),
	("khergit_name_3", "Tonju"),
	("khergit_name_4", "Belir"),
	("khergit_name_5", "Asugan"),
	("khergit_name_6", "Brula"),
	("khergit_name_7", "Imirza"),
	("khergit_name_8", "Urumuda"),
	("khergit_name_9", "Kramuk"),
	("khergit_name_10", "Chaurka"),
	("khergit_name_11", "Sebula"),
	("khergit_name_12", "Tulug"),
	("khergit_name_13", "Nasugei"),
	("khergit_name_14", "Urubay"),
	("khergit_name_15", "Hugu"),
	("khergit_name_16", "Tansugai"),
	("khergit_name_17", "Tirida"),
	("khergit_name_18", "Ulusamai"),
	("khergit_name_19", "Karaban"),
	("khergit_name_20", "Akadan"),
	("khergit_name_21", "Dundush"),
	("khergit_name_22", "Khun"),
	("khergit_name_23", "Liraz"),
	("khergit_name_24", "Hyun"),
	("khergit_name_25", "Daman"),
	("khergit_name_26", "Dustum"),
	("khergit_name_27", "Saliz"),
	("khergit_name_28", "Herei"),
	("khergit_name_29", "Humai"),
  ("khergit_name_30", "Gensis"),
  ("khergit_name_31", "Sangai"),
  ("khergit_name_32", "Aleshtur"),
  ("khergit_name_33", "Manshai"),
  ("khergit_name_34", "Lin"),
  # ("khergit_name_35", ""),
  # ("khergit_name_36", ""),
  # ("khergit_name_37", ""),
  # ("khergit_name_38", ""),
  # ("khergit_name_39", ""),
  # ("khergit_name_40", ""),
	# ("khergit_name_41", ""),
	
	("nordic_name_1", "Ragnar"),
	("nordic_name_2", "Lethwin"),
	("nordic_name_3", "Aedin"),
	("nordic_name_4", "Irya"),
	("nordic_name_5", "Olaf"),
	("nordic_name_6", "Reamald"),
	("nordic_name_7", "Turya"),
	("nordic_name_8", "Gundur"),
	("nordic_name_9", "Harald"),
	("nordic_name_10", "Knudarr"),
	("nordic_name_11", "Haeda"),
	("nordic_name_12", "Turegor"),
	("nordic_name_13", "Logarson"),
	("nordic_name_14", "Aeric"),
	("nordic_name_15", "Faarn"),
	("nordic_name_16", "Bulba"),
	("nordic_name_17", "Rayeck"),
	("nordic_name_18", "Dirigun"),
	("nordic_name_19", "Marayirr"),
	("nordic_name_20", "Gearth"),
	("nordic_name_21", "Surdun"),
	("nordic_name_22", "Gerlad"),
	("nordic_name_23", "Thorir"),
	("nordic_name_24", "Hagar"),
	("nordic_name_25", "Ingmar"),
	("nordic_name_26", "Ydnor"),
	("nordic_name_27", "Rolnack"),
	("nordic_name_28", "Jorund"),
	("nordic_name_29", "Jonulf"),
	("nordic_name_30", "Borg"),
	("nordic_name_31", "Aelle"),
	("nordic_name_32", "Bjorn"),
	("nordic_name_33", "Thorbjorn"),
	("nordic_name_34", "Harik"),
	("nordic_name_35", "Horik"),
	("nordic_name_36", "Hagvar"),
	("nordic_name_37", "Floki"),
	("nordic_name_38", "Borgen"),
	("nordic_name_39", "Jorgen"),
  ("nordic_name_40", "Erik"),
  ("nordic_name_41", "Uldin"),
  ("nordic_name_42", "Uthred"),
  ("nordic_name_43", "Vlok"),
  # ("nordic_name_44", ""),
  # ("nordic_name_45", ""),
  # ("nordic_name_46", ""),
  # ("nordic_name_47", ""),
	# ("nordic_name_48", ""),
	
	("rhodok_name_1", "Graveth"),
	("rhodok_name_2", "Kastor"),
	("rhodok_name_3", "Matheas"),
	("rhodok_name_4", "Gutlans"),
	("rhodok_name_5", "Laruqen"),
	("rhodok_name_6", "Raichs"),
	("rhodok_name_7", "Reland"),
	("rhodok_name_8", "Tarchias"),
	("rhodok_name_9", "Gharmall"),
	("rhodok_name_10", "Talbar"),
	("rhodok_name_11", "Rimusk"),
	("rhodok_name_12", "Falsevor"),
	("rhodok_name_13", "Etrosq"),
	("rhodok_name_14", "Kurnias"),
	("rhodok_name_15", "Tellrog"),
	("rhodok_name_16", "Tribidan"),
	("rhodok_name_17", "Gerluchs"),
	("rhodok_name_18", "Fudreim"),
	("rhodok_name_19", "Nealcha"),
	("rhodok_name_20", "Fraichin"),
	("rhodok_name_21", "Trimbau"),
	("rhodok_name_22", "Reichsin"),
	("rhodok_name_23", "Jemun"),
	("rhodok_name_24", "Cirec"),
	("rhodok_name_25", "Bargas"),
	("rhodok_name_26", "Holmun"),
	("rhodok_name_27", "Mandavir"),
	("rhodok_name_28", "Chalbau"),
	("rhodok_name_29", "Caenlin"),
	("rhodok_name_30", "Haidos"),
  ("rhodok_name_31", "Henry"),
  ("rhodok_name_32", "Faendric"),
  ("rhodok_name_33", "Romulus"),
  ("rhodok_name_34", "Robin"),
  ("rhodok_name_35", "Bunduk"),
  # ("rhodok_name_36", ""),
  # ("rhodok_name_37", ""),
  # ("rhodok_name_38", ""),
  # ("rhodok_name_39", ""),
  # ("rhodok_name_40", ""),
	# ("rhodok_name_41", ""),
	
	("sarranid_name_1", "Hakim"),
	("sarranid_name_2", "Uqais"),
	("sarranid_name_3", "Hamezan"),
	("sarranid_name_4", "Atis"),
	("sarranid_name_5", "Nuwas"),
	("sarranid_name_6", "Mundhalir"),
	("sarranid_name_7", "Ghanawa"),
	("sarranid_name_8", "Nuam"),
	("sarranid_name_9", "Dhiyul"),
	("sarranid_name_10", "Lakhem"),
	("sarranid_name_11", "Ghulassen"),
	("sarranid_name_12", "Azadun"),
	("sarranid_name_13", "Quryas"),
	("sarranid_name_14", "Amdar"),
	("sarranid_name_15", "Hiwan"),
	("sarranid_name_16", "Muhnir"),
	("sarranid_name_17", "Ayyam"),
	("sarranid_name_18", "Raddoun"),
	("sarranid_name_19", "Tilimsan"),
	("sarranid_name_20", "Dhashwal"),
	("sarranid_name_21", "Biliya"),
	("sarranid_name_22", "Shabn"),
	("sarranid_name_23", "Hildalir"),
	("sarranid_name_24", "Sanshub"),
	("sarranid_name_25", "Ughaln"),
	("sarranid_name_26", "Waldin"),
	("sarranid_name_27", "Dulya"),
	("sarranid_name_28", "Jiahem"),
	("sarranid_name_29", "Halmir"),
	("sarranid_name_30", "Mashkir"),
	("sarranid_name_31", "Abdal"),
	# ("sarranid_name_32", ""),
  # ("sarranid_name_33", ""),
  # ("sarranid_name_34", ""),
  # ("sarranid_name_35", ""),
  # ("sarranid_name_36", ""),
  # ("sarranid_name_37", ""),
  # ("sarranid_name_38", ""),
  # ("sarranid_name_39", ""),
  # ("sarranid_name_40", ""),
	# ("sarranid_name_41", ""),
	
	("names_end", "NAMES_END"),
	
	("troop_type_infantry", "Infantry"),
	("troop_type_spearman", "Spearman"),
	("troop_type_pikeman", "Pikeman"),
	("troop_type_skirmisher", "Skirmisher"),
	("troop_type_shock_infantry", "Shock Infantry"),
	("troop_type_archer", "Archer"),
	("troop_type_crossbow", "Crossbowman"),
	("troop_type_cavalry", "Cavalry"),
	("troop_type_lancer", "Lancer"),
	("troop_type_horse_archer", "Horse Archer"),
	("troop_type_mounted_skirmisher", "Mounted Skirmisher"),
	
	("weight_very_light", "Very light"),
	("weight_light", "Light"),
	("weight_medium", "Medium"),
	("weight_heavy", "Heavy"),
	("weight_very_heavy", "Armoured"),
	
	("troop_quality_peasant", "Levy"),
	("troop_quality_common", "Common"),
	("troop_quality_veteran", "Veteran"),
	("troop_quality_elite", "Elite"),
	("troop_quality_noble", "Noble"),
	
	("era_name_0", "First Age"),
	("era_name_1", "Second Age"),
	("era_name_2", "Third Age"),
	("era_name_3", "Fourth Age"),
	("era_name_4", "Fifth Age"),
	("era_name_5", "Sixth Age"),
	("era_name_6", "Seventh Age"),
	("era_name_7", "Eighth Age"),
	("era_name_8", "Ninth Age"),
	("era_name_9", "Tenth Age"),
	
	("party_name_free_1", "Great Wolves"),
	("party_name_free_2", "Lone Eagle"),
	("party_name_holy_1", "The Holy Ones"),
	("party_name_holy_2", "The Chosen Ones"),
	("party_name_holy_evil_1", "Chosen Raiders"),
	("party_name_evil_1", "Fearless Raiders"),
	("party_name_evil_2", "Fearless Warriors"),


  ("help_tax_sell","Taxes applied upon buying goods and items.^Is applied on top of the price of the item, meaning it increases the price at which items are sold.^Mostly affects trade.^^The sell and buy taxes are the least upsetting for the population, provided the are balanced and not exagerated.^It is advised to keep them not too high if one wishes to have trade active."),
  ("help_tax_buy","Taxes applied upon selling goods and items.^Is deducted from the price of the item sold, meaning it decreases the price at which items are bought.^Moslty affects trade.^^The sell and buy taxes are the least upsetting for the population, provided the are balanced and not exagerated.^It is advised to keep them not too high if one wishes to have trade active."),
  ("help_tax_property","Taxes applied at a certain percentage of the size of land property.^Moslty affects property owners, may affect goods production.^^The property tax is a good source of income in well developped cities, it will upset the population quickly if left too high (for they care about their homes).^Most goods are produced using land and increasing the property tax too high may decrease production of these goods."),
  ("help_tax_fixed","Taxes paid by everyone no matter their income.^Mostly affects poorer population.^^Fixed taxes are paid by each and every one living within the city limits.^They mostly affect poorer part of the population as it represents a bigger percentage of their income and may thus decrease population growth."),
  ("help_tax_wealth","Taxes paid based on the income of the person.^Mostly affects good productions and wealthy persons.^^Taxes on weath is the fairest tax, and will generaly be accepted by most part of the population, however, land owners and rich merchants do not see fairness to their advantage."),
  ("help_tax_visit", "Taxes paid upon entering the city limits.^Mostly affects travellers and visitors.^^\"You need to pay the visitor's tax, for the priviledge of entering the city of course! What does it matter?\" Is what guards will say to travelers near the gates.^It keeps the population happy because they do not pay the tax, but will decrease the likelyness of receiving visitors."),

  # Building descriptions
  ("building_hunter_camp",      "The hunter camp periodicaly sends hunters to hunt outside of the village. The hunters will join the fight when defending the village."),
  ("building_woodcutter_camp",  "The woodcutter camp allows for more wood to be produced. It also increases the quality of the wood, which is sold for more."),
  ("building_mill",             "The mill allows for the processing of grain into bread. The center will no longer have to sell the grain by itself, instead selling the more expensive bread."),
  ("building_fish_pond",        "The fish pond allows for more fish caught. It also increases the quality of fish, which is sold for more."),
  ("building_mine",             "The mine increases the amount of iron mined from the village. It also increases the quality of the iron, which is sold for more."),
  ("building_stone_pit",        "The stone pit increases the amount of stones produced by the village. Is also increases the quality of stone, which is sold for more."),
  ("building_cattle_ranch",     "The cattle ranch increases the amount of cattle produced. It also increases the quality of the animals, which are sold for more."),
  ("building_farm",             "The farm slightly increases most food type produced. Includes cabbages, olives, grapes and apples."),
    
  ("building_slaver",           "The slaver allows slaves in the city to work. They do not get paid, but their masters do. Increases prosperity and relation with the center. Also gives a small income per slave working."),
  ("building_market",           "The market allows traders to sell more efficiently their wares. Increases trade gain by 5%%."),
  ("building_market_2",         "The bigger market allows traders to sell more efficiently their wares. Increases trade gain by 10%%."),
  ("building_fields",           "The fields increases the capacity to produce grain."),
  ("building_tannery",          "The tannery allows leather production."),
  ("building_tavern",           "The tavern is a place of great importance in a center. It increases prosperity by 5%% and attracts small groupes of mercenaries."),

  ("building_militia_camp",     "The militia camp increases chance for militia units to be trained. When defending, it also adds a random number of militia troops hastly trained from the population."),
  ("building_smithy",           "The smithy increases the quality of weapons and helps keep them in shape. Increases melee damage by 5%% when defending."),
  ("building_stables",          "The stables are a place for breeding. It allows for more horses to be sold and they may be sold for profit."),
  ("building_archery_range",    "The archery range is a place of practice for archers. When defending increases accuracy by 5%%."),
  ("building_barrack",          "The barracks are a place of rest and training for soldiers. Increases the chance for common units to be trained. When defending, adds a random number of common units, trained from the population."),
  ("building_food_store",       "The food stores allows a center to hold more during sieges."),
  ("building_recruitement_camp", "The recruitement camp, for each reinforcements, trains 10%% of additionnal units of higher rank."),

  ("building_barrack_2",        "The improved barracks are a place of rest and training for soldiers. Increases the chance for veteran units to be trained. When defending, adds a random number of common and veteran units, trained from the population."),
  ("building_smithy_2",         "The imporved smithy further increases the quality of weapons. Increases melee damage by and additionnal 10%%."),
  ("building_training_camp",    "The training camp serves as a military training ground. When defending, increases health of units by an additional 1HP for every 4 points of intelligence. Allows militia units to upgrade to better ones."),
  ("building_training_camp_2",  "The upgraded training camp serves as a military training ground. When defending, increase health of units by an additional 1HP for every 2 points of intelligence."),
  ("building_workshop",         "The workshop helps reduce the cost and construction time of other buildings by 5 to 10%%."),
  ("building_fletcher",         "The fletcher increases the number of ammunition produced. When defending, increases ranged weapons damage by 5%%."),
  ("building_archery_range_2",  "The improved archery range is a place for practice for archers. When defending increases accuracy by an additional 10%%."),
  ("building_trading_post",     "The trading post increases profits from trade by 5%% and give caravans a small escort."),
  ("building_food_store_2",     "The increased food stores allows a center to hold even more during sieges."),
  ("building_recruitement_camp_2", "The improved recruitement camp, for each reinforcements, trains 20%% of additional units of higher rank."),
  
  ("building_university",       "The unversity educates the population. It increases money gained from taxes and trade by 5%% each. It also increases population growth by 10%%."),
  ("building_slaver_2",         "The improved slaver allows slaves in the city to work harder. They still don't get paid, but their master do. Increases prosperity and relation with the center. Also give a moderate income per slave working."),
  ("building_market_3",         "The biggest market allows traders to sell their wares like nowhere else. Increases trade gain by 15%%."),
  ("building_temple",           "The temple is a place of meditation and serenity. It increases the center's prosperity and money gained from all taxes by 10%%."),
  ("building_library",          "The library is a building of free education through books, of course not everyone knows how to read. It increases the center relation with its leader by 1 each month."),
  ("building_order",            "The order is the ultimate military building. It increases the chance for noble units to be trained."),
  ("building_tavern_2",         "The improved tavern is one of, if not the most important building in a center. It increases prosperity by 10%% and has more room for people to rent."),
  ("building_trading_post_2",   "The improved trading post increases profits from trade by 10%% and gives caravans a big escort."),
]
