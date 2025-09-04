from module_string_names import *
from module_string_faces import *

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
  ("nord_rank_3", "Noble {s0}"),
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
  ("sarranid_rank_2", "Noble {s0}"),
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
  ("nord_rank_3_f", "Noble {s0}"),
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
  ("sarranid_rank_2_f", "Noble {s0}"),
  ("sarranid_rank_3_f", "Noble {s0}"),
  ("sarranid_rank_4_f", "Emira {s0}"),
  ("sarranid_rank_5_f", "Malikah {s0}"),
  ("sarranid_rank_6_f", "Caliphah {s0}"),
  ("sarranid_rank_7_f", "Sultanah {s0}"),

  ("troop_type_begin", "Troop type begin"),

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
  
  # ("party_name_free_1", "Great Wolves"),
  # ("party_name_free_2", "Lone Eagle"),
  # ("party_name_holy_1", "The Holy Ones"),
  # ("party_name_holy_2", "The Chosen Ones"),
  # ("party_name_holy_evil_1", "Chosen Raiders"),
  # ("party_name_evil_1", "Fearless Raiders"),
  # ("party_name_evil_2", "Fearless Warriors"),

  ("help_tax_sell","Taxes applied upon buying goods and items.^Is applied on top of the price of the item, meaning it increases the price at which items are sold.^Mostly affects trade.^^The sell and buy taxes are the least upsetting for the population, provided the are balanced and not exagerated.^It is advised to keep them not too high if one wishes to have trade active."),
  ("help_tax_buy","Taxes applied upon selling goods and items.^Is deducted from the price of the item sold, meaning it decreases the price at which items are bought.^Moslty affects trade.^^The sell and buy taxes are the least upsetting for the population, provided the are balanced and not exagerated.^It is advised to keep them not too high if one wishes to have trade active."),
  ("help_tax_property","Taxes applied at a certain percentage of the size of land property.^Moslty affects property owners, may affect goods production.^^The property tax is a good source of income in well developped cities, it will upset the population quickly if left too high (for they care about their homes).^Most goods are produced using land and increasing the property tax too high may decrease production of these goods."),
  ("help_tax_fixed","Taxes paid by everyone no matter their income.^Mostly affects poorer population.^^Fixed taxes are paid by each and every one living within the city limits.^They mostly affect poorer part of the population as it represents a bigger percentage of their income and may thus decrease population growth."),
  ("help_tax_wealth","Taxes paid based on the income of the person.^Mostly affects good productions and wealthy population.^^Taxes on weath is the fairest tax, and will generaly be accepted by most part of the population, however, land owners and rich merchants do not see fairness to their advantage."),
  ("help_tax_visit", "Taxes paid upon entering the city limits.^Mostly affects travellers and visitors.^^\"You need to pay the visitor's tax, for the priviledge of entering the city of course! What does it matter?\" Is what guards will say to travelers near the gates.^It keeps the population happy because they do not pay the tax, but will decrease the likelyness of receiving visitors as well as impacting trade."),

  ("swadian_faction_small", "County of {s0}"),
  ("swadian_faction_medium", "Duchy of {s0}"),
  ("swadian_faction_large", "Kingdom of {s0}"),
  ("vaegir_faction_small", "County of {s0}"),
  ("vaegir_faction_medium", "Duchy of {s0}"),
  ("vaegir_faction_large", "Kingdom of {s0}"),
  ("khergit_faction_small", "{s0} Tribes"),
  ("khergit_faction_medium", "{s0} Khanate"),
  ("khergit_faction_large", "{s0} Khanate"),
  ("nordic_faction_small", "{s0} Warriors"),
  ("nordic_faction_medium", "{s0} Hold"),
  ("nordic_faction_large", "Kingdom of {s0}"),
  ("rhodok_faction_small", "{s0} Community"),
  ("rhodok_faction_medium", "City of {s0}"),
  ("rhodok_faction_large", "Kingdom of {s0}"), # ToDo: change to election-style name
  ("sarranid_faction_small", "Tribes of {s0}"),
  ("sarranid_faction_medium", "Oasis of {s0}"),
  ("sarranid_faction_large", "{s0} Sultanate"),

  ("outcome_failure", "Failure"),
  ("outcome_neutral", "Neutral"),
  ("outcome_success", "Success"),

  # Building descriptions
  ("building_hunter_camp",      "Sends hunters outside of the village.^^The hunters join fights when defending."),
  ("building_woodcutter_camp",  "Allows for better production of wood.^^Also increases the quality of the wood,^which is sold for more."),
  ("building_mill",             "Allows for the processing of grain into bread.^^The center will no longer have to sell^the grain by itself, instead,^selling the more expensive bread."),
  ("building_fish_pond",        "Adds fishing facilities to the nearby ponds.^^Increases the quality of fish, which is sold for more."),
  ("building_mine",             "Expands the mining equipments.^^Increase the amount of iron mined.^Also increase the quality of the iron,^which is sold for more."),
  ("building_stone_pit",        "Creates a stone pit to gather stones.^^Increase the amount of stones produced.^Also increase the quality of stone,^which is sold for more."),
  ("building_cattle_ranch",     "The cattle ranch increases the amount of cattle produced.^It also increases the quality of the animals, which are sold for more."),
  ("building_farm",             "The farm slightly increases most food type produced.^Includes cabbages, olives, grapes and apples."),
    
  ("building_slaver",           "Allows slaves in the city to work.^^They do not get paid, but their masters do.^Increases prosperity and relation^with the center.^Also gives a small income per slave working."),
  ("building_market",           "Gives traders more room to sell their wares.^^Increases trade gain by 5%."),
  ("building_market_2",         "Better facilities allows traders to sell^their wares more efficiently.^^Increases trade gain by 10%."),
  ("building_fields",           "Expanded fields surrounding the center.^^Increases the capacity to produce grain."),
  ("building_tannery",          "Equipements to facilitate tanning leather.^^Increases the produced ratio of leather."),
  ("building_tavern",           "A place of great importance in a center.^^Increases prosperity by 5%.^Houses mercenaries."),

  ("building_militia_camp",     "Adds a place to train new recruits.^^Increases chance for militia units to be trained.^When fighting a defensive battle,^adds a random number of militia troops."),
  ("building_smithy",           "Presence of a smithy increases the quality^of weapons and helps keep them in shape.^^Increases melee damage by 5% when defending."),
  ("building_stables",          "A healthy home for weary horses.^The stables are a place for breeding ^and caring of horses.^^Allows for more horses to be sold^and they may be sold for profit."),
  ("building_archery_range",    "The archery range is a place of practice for archers.^When defending increases accuracy by 5%."),
  ("building_barrack",          "The barracks are a place of rest and training for soldiers.^Increases the chance for common units to be trained. When defending, adds a random number of common units, trained from the population."),
  ("building_food_store",       "The food stores allows a center to hold more during sieges."),
  ("building_recruitement_camp", "The recruitment camp adds infrastructures^to facilitates recruitment of troops.^^Reduces recruitment cost of troops by 10%."),
  ("building_mason_guild",      "Creates a guild for handling masonry work. ^^Increases construction slots by 1.^Decreases building time by 10%"),

  ("building_barrack_2",        "The improved barracks are a place of rest and training for soldiers.^Increases the chance for veteran units to be trained. When defending, adds a random number of common and veteran units, trained from the population."),
  ("building_smithy_2",         "The improved smithy further increases the quality of weapons.^Increases melee damage by and additionnal 10%."),
  ("building_training_camp",    "The training camp serves as a military training ground.^When defending, increases health of units by an additional 1HP for every 4 points of intelligence. Allows militia units to upgrade to better ones."),
  ("building_training_camp_2",  "The upgraded training camp serves as a military training ground.^When defending, increase health of units by an additional 1HP for every 2 points of intelligence."),
  ("building_workshop",         "The workshop helps reduce the cost and construction time of other buildings by 10%."),
  ("building_fletcher",         "The fletcher increases the number of ammunition produced.^When defending, increases ranged weapons damage by 5%."),
  ("building_archery_range_2",  "The improved archery range is a place for practice for archers.^When defending increases accuracy by an additional 10%."),
  ("building_trading_post",     "The trading post increases profits from trade by 5% and give caravans a small escort."),
  ("building_food_store_2",     "The increased food stores allows a center to hold even more during sieges."),
  ("building_recruitement_camp_2", "Improvements to the recruitment camp.^Add additional buildings and services^to increase the efficiency of the^recruitment processes.^^Further decreases recruitment costs by 15%."),
  ("building_mason_guild_2",    "Improves the mason's guild. ^^Decreases building cost and time by 10%"),
  
  ("building_university",       "The unversity educates the population.^It increases money gained from taxes and trade by 5% each. It also increases population growth by 10%."),
  ("building_slaver_2",         "The improved slaver allows slaves in the city to work harder.^They still don't get paid, but their master do. Increases prosperity and relation with the center. Also give a moderate income per slave working."),
  ("building_market_3",         "The biggest market allows traders to sell their wares like nowhere else.^Increases trade gain by 15%."),
  ("building_temple",           "The temple is a place of meditation and serenity.^It increases the center's prosperity and money gained from all taxes by 10%."),
  ("building_library",          "The library is a building of free education through books, of course not everyone knows how to read.^It increases the center relation with its leader by 1 each month."),
  ("building_order",            "The order is the ultimate military building.^It increases the chance for noble units to be trained."),
  ("building_tavern_2",         "The improved tavern is one of, if not the most important building in a center.^It increases prosperity by 10% and has more room for people to rent."),
  ("building_trading_post_2",   "The improved trading post increases profits from trade by 10% and gives caravans a big escort."),
  ("building_bank",             "The bank gives the capability for citizens to ^lend their money for safekeeping and ^investment.^^Add a special income from bank taxes.^Increase fame by 5^Increase growth by 5^Add the bank features in town."),
  ("building_mason_guild_3",    "Further improves the mason's guild. ^^Increases construction slots by 1.^Decreases building cost by 10%"),

  ("item_taxes_sell", "Town selling taxes: {reg10}%"),
  ("item_taxes_buy", "Town buying taxes: {reg10}%"),

  ("dialog_error", "[ERROR] Incorrect dialog string."),

  ("bandit_greetings_aggressive_forest",    "Welcome {reg10?madam:sir}, care to spare some gold for a group of wary travelers?"),
  ("bandit_greetings_aggressive_looter",    "Your money or your life {reg10?lass:lad}!"),
  ("bandit_greetings_aggressive_mountain",  "Your money or your life {reg10?lass:lad}!"),
  ("bandit_greetings_aggressive_raider",    "I will drink from your skull!"),
  ("bandit_greetings_aggressive_steppe",    "Your money or your life {reg10?lass:lad}!"),
  ("bandit_greetings_aggressive_tundra",    "Your money or your life {reg10?lass:lad}!"),
  ("bandit_greetings_aggressive_desert",    "Your money or your life {reg10?lass:lad}!"),

  ("bandit_greetings_defensive_forest",   "Welcome {reg10?madam:sir}, can I help you?"),
  ("bandit_greetings_defensive_looter",   "Huh? What is it that you want?"),
  ("bandit_greetings_defensive_mountain", "Huh? What is it that you want?"),
  ("bandit_greetings_defensive_raider",   "Huh? What is it that you want?"),
  ("bandit_greetings_defensive_steppe",   "Huh? What is it that you want?"),
  ("bandit_greetings_defensive_tundra",   "Huh? What is it that you want?"),
  ("bandit_greetings_defensive_desert",   "Huh? What is it that you want?"),

  ("bandit_accept_low_money_forest",    "It will have to do I guess..."),
  ("bandit_accept_low_money_looter",    "Ugh... fine... Get lost I don't want to see you again."),
  ("bandit_accept_low_money_mountain",  "Ugh... fine... Get lost I don't want to see you again."),
  ("bandit_accept_low_money_raider",    "Pathetic... Get lost!"),
  ("bandit_accept_low_money_steppe",    "Ugh... fine... Get lost I don't want to see you again."),
  ("bandit_accept_low_money_tundra",    "Ugh... fine... Get lost I don't want to see you again."),
  ("bandit_accept_low_money_desert",    "Ugh... fine... Get lost I don't want to see you again."),

  ("bandit_refuse_low_money_forest",    "You're lousy with gold, it clings with every move you make, let me help you carry it... I insist."),
  ("bandit_refuse_low_money_looter",    "I think you can do better than that, give me everything or pay with your blood !"),
  ("bandit_refuse_low_money_mountain",  "I think you can do better than that, give me everything or pay with your blood !"),
  ("bandit_refuse_low_money_raider",    "Last warning, your entrails are on the line!"),
  ("bandit_refuse_low_money_steppe",    "I think you can do better than that, give me everything or pay with your blood !"),
  ("bandit_refuse_low_money_tundra",    "I think you can do better than that, give me everything or pay with your blood !"),
  ("bandit_refuse_low_money_desert",    "I think you can do better than that, give me everything or pay with your blood !"),

  ("bandit_accept_gold_forest",   "Good day to you."),
  ("bandit_accept_gold_looter",   "Easy money..."),
  ("bandit_accept_gold_mountain", "Easy money..."),
  ("bandit_accept_gold_raider",   "Easy money..."),
  ("bandit_accept_gold_steppe",   "Easy money..."),
  ("bandit_accept_gold_tundra",   "Easy money..."),
  ("bandit_accept_gold_desert",   "Easy money..."),

  ("bandit_accept_gold_half_forest",    "Good day to you."),
  ("bandit_accept_gold_half_looter",    "Easy money..."),
  ("bandit_accept_gold_half_mountain",  "Easy money..."),
  ("bandit_accept_gold_half_raider",    "Easy money..."),
  ("bandit_accept_gold_half_steppe",    "Easy money..."),
  ("bandit_accept_gold_half_tundra",    "Easy money..."),
  ("bandit_accept_gold_half_desert",    "Easy money..."),

  ("bandit_accept_gold_all_forest",   "You bring joy to this old man."),
  ("bandit_accept_gold_all_looter",   "Nice..."),
  ("bandit_accept_gold_all_mountain", "Nice..."),
  ("bandit_accept_gold_all_raider",   "Nice..."),
  ("bandit_accept_gold_all_steppe",   "Nice..."),
  ("bandit_accept_gold_all_tundra",   "Nice..."),
  ("bandit_accept_gold_all_desert",   "Nice..."),

  ("bandit_accept_all_forest",    "Please, accept my most sincere gratitude."),
  ("bandit_accept_all_looter",    "A pleasure doing business with you."),
  ("bandit_accept_all_mountain",  "A pleasure doing business with you."),
  ("bandit_accept_all_raider",    "A pleasure doing business with you."),
  ("bandit_accept_all_steppe",    "A pleasure doing business with you."),
  ("bandit_accept_all_tundra",    "A pleasure doing business with you."),
  ("bandit_accept_all_desert",    "A pleasure doing business with you."),

  ("bandit_refuse_nothing_forest",    "Alas there is no reasoning you..."),
  ("bandit_refuse_nothing_looter",    "Then you pay with your life!"),
  ("bandit_refuse_nothing_mountain",  "Then you pay with your life!"),
  ("bandit_refuse_nothing_raider",    "You'll pay with your blood!"),
  ("bandit_refuse_nothing_steppe",    "Then you pay with your life!"),
  ("bandit_refuse_nothing_tundra",    "Then you pay with your life!"),
  ("bandit_refuse_nothing_desert",    "Then you pay with your life!"),

  ("bandit_fight_aggressive_forest",    "So be it, prepare yourself!"),
  ("bandit_fight_aggressive_looter",    "Just how I like it!"),
  ("bandit_fight_aggressive_mountain",  "Just how I like it!"),
  ("bandit_fight_aggressive_raider",    "Arrrg!"),
  ("bandit_fight_aggressive_steppe",    "Just how I like it!"),
  ("bandit_fight_aggressive_tundra",    "Just how I like it!"),
  ("bandit_fight_aggressive_desert",    "Just how I like it!"),

  ("bandit_player_give_gold_all_forest",    "Here take everything and leave me alone! ({s10})!"),
  ("bandit_player_give_gold_all_looter",    "Here take everything and leave me alone! ({s10})!"),
  ("bandit_player_give_gold_all_mountain",  "Here take everything and leave me alone! ({s10})!"),
  ("bandit_player_give_gold_all_raider",    "Here take everything and leave me alone! ({s10})!"),
  ("bandit_player_give_gold_all_steppe",    "Here take everything and leave me alone! ({s10})!"),
  ("bandit_player_give_gold_all_tundra",    "Here take everything and leave me alone! ({s10})!"),
  ("bandit_player_give_gold_all_desert",    "Here take everything and leave me alone! ({s10})!"),

  ("bandit_player_give_gold_half_forest",   "Take {s10} and be on your way!"),
  ("bandit_player_give_gold_half_looter",   "Take {s10} and be on your way!"),
  ("bandit_player_give_gold_half_mountain", "Take {s10} and be on your way!"),
  ("bandit_player_give_gold_half_raider",   "Take {s10} and be on your way!"),
  ("bandit_player_give_gold_half_steppe",   "Take {s10} and be on your way!"),
  ("bandit_player_give_gold_half_tundra",   "Take {s10} and be on your way!"),
  ("bandit_player_give_gold_half_desert",   "Take {s10} and be on your way!"),

  ("bandit_player_give_gold_forest",    "Take {s10} and be on your way!"),
  ("bandit_player_give_gold_looter",    "Take {s10} and be on your way!"),
  ("bandit_player_give_gold_mountain",  "Take {s10} and be on your way!"),
  ("bandit_player_give_gold_raider",    "Take {s10} and be on your way!"),
  ("bandit_player_give_gold_steppe",    "Take {s10} and be on your way!"),
  ("bandit_player_give_gold_tundra",    "Take {s10} and be on your way!"),
  ("bandit_player_give_gold_desert",    "Take {s10} and be on your way!"),

  ("bandit_player_give_gold_low_forest",    "This is all I have ({s10})."),
  ("bandit_player_give_gold_low_looter",    "This is all I have ({s10})."),
  ("bandit_player_give_gold_low_mountain",  "This is all I have ({s10})."),
  ("bandit_player_give_gold_low_raider",    "This is all I have ({s10})."),
  ("bandit_player_give_gold_low_steppe",    "This is all I have ({s10})."),
  ("bandit_player_give_gold_low_tundra",    "This is all I have ({s10})."),
  ("bandit_player_give_gold_low_desert",    "This is all I have ({s10})."),

  ("bandit_player_give_gold_nothing_forest",    "I don't have any money with me, please let me go."),
  ("bandit_player_give_gold_nothing_looter",    "I don't have any money with me, please let me go."),
  ("bandit_player_give_gold_nothing_mountain",  "I don't have any money with me, please let me go."),
  ("bandit_player_give_gold_nothing_raider",    "I don't have any money with me, please let me go."),
  ("bandit_player_give_gold_nothing_steppe",    "I don't have any money with me, please let me go."),
  ("bandit_player_give_gold_nothing_tundra",    "I don't have any money with me, please let me go."),
  ("bandit_player_give_gold_nothing_desert",    "I don't have any money with me, please let me go."),

  ("bandit_player_fight_forest",    "Take it if you can!"),
  ("bandit_player_fight_looter",    "Take it if you can!"),
  ("bandit_player_fight_mountain",  "Take it if you can!"),
  ("bandit_player_fight_raider",    "Take it if you can!"),
  ("bandit_player_fight_steppe",    "Take it if you can!"),
  ("bandit_player_fight_tundra",    "Take it if you can!"),
  ("bandit_player_fight_desert",    "Take it if you can!"),

  ("bandit_player_give_all_forest",   "Take what you want."),
  ("bandit_player_give_all_looter",   "Take what you want."),
  ("bandit_player_give_all_mountain", "Take what you want."),
  ("bandit_player_give_all_raider",   "Take what you want."),
  ("bandit_player_give_all_steppe",   "Take what you want."),
  ("bandit_player_give_all_tundra",   "Take what you want."),
  ("bandit_player_give_all_desert",   "Take what you want."),

  ("bandit_player_give_nothing_forest",   "Then you'll have a fight!"),
  ("bandit_player_give_nothing_looter",   "Then you'll have a fight!"),
  ("bandit_player_give_nothing_mountain", "Then you'll have a fight!"),
  ("bandit_player_give_nothing_raider",   "Then you'll have a fight!"),
  ("bandit_player_give_nothing_steppe",   "Then you'll have a fight!"),
  ("bandit_player_give_nothing_tundra",   "Then you'll have a fight!"),
  ("bandit_player_give_nothing_desert",   "Then you'll have a fight!"),

  ("bandit_defensive_player_fight_forest",    "Die mongrels!"),
  ("bandit_defensive_player_fight_looter",    "Die mongrels!"),
  ("bandit_defensive_player_fight_mountain",  "Die mongrels!"),
  ("bandit_defensive_player_fight_raider",    "Die mongrels!"),
  ("bandit_defensive_player_fight_steppe",    "Die mongrels!"),
  ("bandit_defensive_player_fight_tundra",    "Die mongrels!"),
  ("bandit_defensive_player_fight_desert",    "Die mongrels!"),

  ("bandit_defensive_player_recruit_forest",    "I'd like you to join me and my group."),
  ("bandit_defensive_player_recruit_looter",    "I'd like you to join me and my group."),
  ("bandit_defensive_player_recruit_mountain",  "I'd like you to join me and my group."),
  ("bandit_defensive_player_recruit_raider",    "I'd like you to join me and my group."),
  ("bandit_defensive_player_recruit_steppe",    "I'd like you to join me and my group."),
  ("bandit_defensive_player_recruit_tundra",    "I'd like you to join me and my group."),
  ("bandit_defensive_player_recruit_desert",    "I'd like you to join me and my group."),

  ("bandit_defensive_player_rob_forest",    "Give me all your belongings and you get to keep your lives."),
  ("bandit_defensive_player_rob_looter",    "Give me all your belongings and you get to keep your lives."),
  ("bandit_defensive_player_rob_mountain",  "Give me all your belongings and you get to keep your lives."),
  ("bandit_defensive_player_rob_raider",    "Give me all your belongings and you get to keep your lives."),
  ("bandit_defensive_player_rob_steppe",    "Give me all your belongings and you get to keep your lives."),
  ("bandit_defensive_player_rob_tundra",    "Give me all your belongings and you get to keep your lives."),
  ("bandit_defensive_player_rob_desert",    "Give me all your belongings and you get to keep your lives."),

  ("bandit_defensive_player_bounty_forest",   "By order of {s10} your lives are now forfeit."),
  ("bandit_defensive_player_bounty_looter",   "By order of {s10} your lives are now forfeit."),
  ("bandit_defensive_player_bounty_mountain", "By order of {s10} your lives are now forfeit."),
  ("bandit_defensive_player_bounty_raider",   "By order of {s10} your lives are now forfeit."),
  ("bandit_defensive_player_bounty_steppe",   "By order of {s10} your lives are now forfeit."),
  ("bandit_defensive_player_bounty_tundra",   "By order of {s10} your lives are now forfeit."),
  ("bandit_defensive_player_bounty_desert",   "By order of {s10} your lives are now forfeit."),

  ("bandit_defensive_player_nevermind_forest",    "Nevermind."),
  ("bandit_defensive_player_nevermind_looter",    "Nevermind."),
  ("bandit_defensive_player_nevermind_mountain",  "Nevermind."),
  ("bandit_defensive_player_nevermind_raider",    "Nevermind."),
  ("bandit_defensive_player_nevermind_steppe",    "Nevermind."),
  ("bandit_defensive_player_nevermind_tundra",    "Nevermind."),
  ("bandit_defensive_player_nevermind_desert",    "Nevermind."),

  ("bandit_defensive_ask_bargain_forest", "We're just a group of weary travelers, surely you do not wish to harm us ?"),
  ("bandit_defensive_ask_bargain_looter", "Wait... I'm sure we can come to an arrangement yes ?"),
  ("bandit_defensive_ask_bargain_mountain", "Wait... I'm sure we can come to an arrangement yes ?"),
  ("bandit_defensive_ask_bargain_raider", "Wait... I'm sure we can come to an arrangement yes ?"),
  ("bandit_defensive_ask_bargain_steppe", "Wait... I'm sure we can come to an arrangement yes ?"),
  ("bandit_defensive_ask_bargain_tundra", "Wait... I'm sure we can come to an arrangement yes ?"),
  ("bandit_defensive_ask_bargain_desert", "Wait... I'm sure we can come to an arrangement yes ?"),

  ("bandit_defensive_fight_back_forest", "Draw your sword mongrel!"),
  ("bandit_defensive_fight_back_looter", "You asked for it!"),
  ("bandit_defensive_fight_back_mountain", "You asked for it!"),
  ("bandit_defensive_fight_back_raider", "You asked for it!"),
  ("bandit_defensive_fight_back_steppe", "You asked for it!"),
  ("bandit_defensive_fight_back_tundra", "You asked for it!"),
  ("bandit_defensive_fight_back_desert", "You asked for it!"),

  ("bandit_defensive_player_attack_no_bargain_forest",    "You don't fool me with your act. Die now!"),
  ("bandit_defensive_player_attack_no_bargain_looter",    "No we can't"),
  ("bandit_defensive_player_attack_no_bargain_mountain",  "No we can't"),
  ("bandit_defensive_player_attack_no_bargain_raider",    "No we can't"),
  ("bandit_defensive_player_attack_no_bargain_steppe",    "No we can't"),
  ("bandit_defensive_player_attack_no_bargain_tundra",    "No we can't"),
  ("bandit_defensive_player_attack_no_bargain_desert",    "No we can't"),

  ("bandit_defensive_player_attack_recruit_forest",   "Join me, fight for me, die for me"),
  ("bandit_defensive_player_attack_recruit_looter",   "Join me, fight for me, die for me"),
  ("bandit_defensive_player_attack_recruit_mountain", "Join me, fight for me, die for me"),
  ("bandit_defensive_player_attack_recruit_raider",   "Join me, fight for me, die for me"),
  ("bandit_defensive_player_attack_recruit_steppe",   "Join me, fight for me, die for me"),
  ("bandit_defensive_player_attack_recruit_tundra",   "Join me, fight for me, die for me"),
  ("bandit_defensive_player_attack_recruit_desert",   "Join me, fight for me, die for me"),

  ("bandit_defensive_player_attack_rob_forest",   "Give me all you have"),
  ("bandit_defensive_player_attack_rob_looter",   "Give me all you have"),
  ("bandit_defensive_player_attack_rob_mountain", "Give me all you have"),
  ("bandit_defensive_player_attack_rob_raider",   "Give me all you have"),
  ("bandit_defensive_player_attack_rob_steppe",   "Give me all you have"),
  ("bandit_defensive_player_attack_rob_tundra",   "Give me all you have"),
  ("bandit_defensive_player_attack_rob_desert",   "Give me all you have"),

  ("bandit_defensive_player_attack_ask_surrender_forest",   "Surrender peacefuly."),
  ("bandit_defensive_player_attack_ask_surrender_looter",   "Surrender peacefuly."),
  ("bandit_defensive_player_attack_ask_surrender_mountain", "Surrender peacefuly."),
  ("bandit_defensive_player_attack_ask_surrender_raider",   "Surrender peacefuly."),
  ("bandit_defensive_player_attack_ask_surrender_steppe",   "Surrender peacefuly."),
  ("bandit_defensive_player_attack_ask_surrender_tundra",   "Surrender peacefuly."),
  ("bandit_defensive_player_attack_ask_surrender_desert",   "Surrender peacefuly."),

  ("bandit_defensive_player_attack_nevermind_forest",   "Forget it, get lost."),
  ("bandit_defensive_player_attack_nevermind_looter",   "Forget it, get lost."),
  ("bandit_defensive_player_attack_nevermind_mountain", "Forget it, get lost."),
  ("bandit_defensive_player_attack_nevermind_raider",   "Forget it, get lost."),
  ("bandit_defensive_player_attack_nevermind_steppe",   "Forget it, get lost."),
  ("bandit_defensive_player_attack_nevermind_tundra",   "Forget it, get lost."),
  ("bandit_defensive_player_attack_nevermind_desert",   "Forget it, get lost."),

  ("bandit_defensive_surrender_forest",   "Very well, we are at your mercy."),
  ("bandit_defensive_surrender_looter",   "Very well, we are at your mercy."),
  ("bandit_defensive_surrender_mountain", "Very well, we are at your mercy."),
  ("bandit_defensive_surrender_raider",   "Very well, we are at your mercy."),
  ("bandit_defensive_surrender_steppe",   "Very well, we are at your mercy."),
  ("bandit_defensive_surrender_tundra",   "Very well, we are at your mercy."),
  ("bandit_defensive_surrender_desert",   "Very well, we are at your mercy."),

  ("bandit_defensive_surrender_leave_men_forest", "Would you allow my men to leave unharmed ?"),
  ("bandit_defensive_surrender_leave_men_looter", "Would you allow my men to leave unharmed ?"),
  ("bandit_defensive_surrender_leave_men_mountain", "Would you allow my men to leave unharmed ?"),
  ("bandit_defensive_surrender_leave_men_raider", "Would you allow my men to leave unharmed ?"),
  ("bandit_defensive_surrender_leave_men_steppe", "Would you allow my men to leave unharmed ?"),
  ("bandit_defensive_surrender_leave_men_tundra", "Would you allow my men to leave unharmed ?"),
  ("bandit_defensive_surrender_leave_men_desert", "Would you allow my men to leave unharmed ?"),

  ("bandit_defensive_surrender_not_forest", "Not without a fight!"),
  ("bandit_defensive_surrender_not_looter", "Not without a fight!"),
  ("bandit_defensive_surrender_not_mountain", "Not without a fight!"),
  ("bandit_defensive_surrender_not_raider", "Not without a fight!"),
  ("bandit_defensive_surrender_not_steppe", "Not without a fight!"),
  ("bandit_defensive_surrender_not_tundra", "Not without a fight!"),
  ("bandit_defensive_surrender_not_desert", "Not without a fight!"),

  ("bandit_defensive_player_ask_join_accept_forest", "You might be worth following, we'll do that then."),
  ("bandit_defensive_player_ask_join_accept_looter", "Well it's not a bad idea, we're with you."),
  ("bandit_defensive_player_ask_join_accept_mountain", "Well it's not a bad idea, we're with you."),
  ("bandit_defensive_player_ask_join_accept_raider", "Well it's not a bad idea, we're with you."),
  ("bandit_defensive_player_ask_join_accept_steppe", "Well it's not a bad idea, we're with you."),
  ("bandit_defensive_player_ask_join_accept_tundra", "Well it's not a bad idea, we're with you."),
  ("bandit_defensive_player_ask_join_accept_desert", "Well it's not a bad idea, we're with you."),

  ("bandit_defensive_player_ask_join_refuse_forest", "Never to you!"),
  ("bandit_defensive_player_ask_join_refuse_looter", "Never to you!"),
  ("bandit_defensive_player_ask_join_refuse_mountain", "Never to you!"),
  ("bandit_defensive_player_ask_join_refuse_raider", "Never to you!"),
  ("bandit_defensive_player_ask_join_refuse_steppe", "Never to you!"),
  ("bandit_defensive_player_ask_join_refuse_tundra", "Never to you!"),
  ("bandit_defensive_player_ask_join_refuse_desert", "Never to you!"),

  ("bandit_defensive_player_rob_give_all_forest", "Robbing the poor and defenseless... here, take it ({reg10})."),
  ("bandit_defensive_player_rob_give_all_looter", "Fine take everything we have ({reg10})."),
  ("bandit_defensive_player_rob_give_all_mountain", "Fine take everything we have ({reg10})."),
  ("bandit_defensive_player_rob_give_all_raider", "Fine take everything we have ({reg10})."),
  ("bandit_defensive_player_rob_give_all_steppe", "Fine take everything we have ({reg10})."),
  ("bandit_defensive_player_rob_give_all_tundra", "Fine take everything we have ({reg10})."),
  ("bandit_defensive_player_rob_give_all_desert", "Fine take everything we have ({reg10})."),

  ("bandit_defensive_player_rob_give_item_forest", "We don't have anything, here take what you want"),
  ("bandit_defensive_player_rob_give_item_looter", "We don't have anything, here take what you want"),
  ("bandit_defensive_player_rob_give_item_mountain", "We don't have anything, here take what you want"),
  ("bandit_defensive_player_rob_give_item_raider", "We don't have anything, here take what you want"),
  ("bandit_defensive_player_rob_give_item_steppe", "We don't have anything, here take what you want"),
  ("bandit_defensive_player_rob_give_item_tundra", "We don't have anything, here take what you want"),
  ("bandit_defensive_player_rob_give_item_desert", "We don't have anything, here take what you want"),

  ("bandit_defensive_player_rob_give_not_forest", "Hah! You'll take nothing without a fight!"),
  ("bandit_defensive_player_rob_give_not_looter", "Hah! You'll take nothing without a fight!"),
  ("bandit_defensive_player_rob_give_not_mountain", "Hah! You'll take nothing without a fight!"),
  ("bandit_defensive_player_rob_give_not_raider", "Hah! You'll take nothing without a fight!"),
  ("bandit_defensive_player_rob_give_not_steppe", "Hah! You'll take nothing without a fight!"),
  ("bandit_defensive_player_rob_give_not_tundra", "Hah! You'll take nothing without a fight!"),
  ("bandit_defensive_player_rob_give_not_desert", "Hah! You'll take nothing without a fight!"),

  ("bandit_defensive_surrender_leave_men_accept_forest", "Of course, your men will be left unharmed."),
  ("bandit_defensive_surrender_leave_men_accept_looter", "Of course, your men will be left unharmed."),
  ("bandit_defensive_surrender_leave_men_accept_mountain", "Of course, your men will be left unharmed."),
  ("bandit_defensive_surrender_leave_men_accept_raider", "Of course, your men will be left unharmed."),
  ("bandit_defensive_surrender_leave_men_accept_steppe", "Of course, your men will be left unharmed."),
  ("bandit_defensive_surrender_leave_men_accept_tundra", "Of course, your men will be left unharmed."),
  ("bandit_defensive_surrender_leave_men_accept_desert", "Of course, your men will be left unharmed."),

  ("bandit_defensive_surrender_leave_men_refuse_forest", "No, they followed you, they will now follow you in jail."),
  ("bandit_defensive_surrender_leave_men_refuse_looter", "No, they followed you, they will now follow you in jail."),
  ("bandit_defensive_surrender_leave_men_refuse_mountain", "No, they followed you, they will now follow you in jail."),
  ("bandit_defensive_surrender_leave_men_refuse_raider", "No, they followed you, they will now follow you in jail."),
  ("bandit_defensive_surrender_leave_men_refuse_steppe", "No, they followed you, they will now follow you in jail."),
  ("bandit_defensive_surrender_leave_men_refuse_tundra", "No, they followed you, they will now follow you in jail."),
  ("bandit_defensive_surrender_leave_men_refuse_desert", "No, they followed you, they will now follow you in jail."),

  ("player_receive_center", "A messenger brings a message for you.^^{s10} wishes to offer you {s11} as a fief under the condition that you become his vassal^^^^Do you accept ?"),
  ("player_receive_center_vassal", "A messenger brings a message for you.^^Your lord {s10} wishes to offer you {s11} as a fief^Refusing would likely reduce your chances of being awarded another for some time.^^^Do you accept ?"),
  ("player_receive_center_vassal_player", "A messenger brings a message for you.^^Your vassal {s10} wishes to offer you {s11} as a fief.^^^Do you accept ?"),
  ("player_receive_center_leader", "A messenger brings a message for you.^^{s10} wishes to grant you {s11} as a fief^Refusing would likely reduce your chances of being awarded another for some time.^^^Do you accept ?"),

  ("quest_description_introduction_default", "After your hard journey to Calradia, take a moment to rest in the town of {s59}."),
  ("quest_description_introduction_default_search", "{s58} had few informations on the whereabouts of his brother {s57}.^^He proposed that you look for answer in the nearby villages."),
  ("quest_description_introduction_default_search_1", "Search the village of {s59} for information on {s58}'s brother."),
  ("quest_description_introduction_default_search_2", "Search the village of {s59} for information on {s58}'s brother."),
  ("quest_description_introduction_default_search_3", "Search the village of {s59} for information on {s58}'s brother."),
  ("quest_description_introduction_waiting", "{s62} is looking for additional leads regarding his missing brother. You aggreed to assist him should he need your help."),
  ("quest_description_introduction_waiting", "You have agreed to help {s62} to confront Cerval Phinius."),

  ("quest_description_swear_vassalage_fief", "{s62} would like to receive your oath of allegience to him{reg60?, you would be granted {s11} in exchange:}."),
  ("quest_description_persuade_lord_vassalage", "Persuade a lord to become your vassal."),
  
  ("quest_description_visit_center_new_owner", "As the newly appointed owner of {s59} you should head to the center to make yourself known and arrange the details of your fiefdom."),

  ("quest_description_village_deliver_grain", "The elder of the village of {s59} asked you to procure 10 items of grain."),
  ("quest_description_village_deliver_rare_good", " "),
  ("quest_description_village_negociate_trade_arrangement", " "),
  ("quest_description_village_hunt_notorious_bandit", " "),
  ("quest_description_village_persuade_mercenaries_leave", " "),
  ("quest_description_end", "{!}QUESTS END"),

  ("party_tax_description_taxes", "Taxes"),
  ("party_tax_description_protection", "Protection taxes"),
  ("party_tax_description_protection_pay", "Protection taxes"),
  ("party_tax_description_vassal", "Vassal taxes"),
  ("party_tax_description_vassal_pay", "Vassal taxes"),
  ("party_tax_description_member", "Faction taxes"),
  ("party_tax_description_member_pay", "Faction taxes"),
  ("party_tax_description_trade", "Trade taxes"),
  ("party_tax_description_visitor", "Visitor's taxes"),
  ("party_tax_description_funds", "Faction funds"),
  ("party_tax_description_funds_pay", "Faction funds"),
  ("party_tax_description_tribute", "Tribute received"),
  ("party_tax_description_tribute_pay", "Tribute payments"),
  ("party_tax_description_occupation", "Center occupations"),
  ("party_tax_description_occupation_pay", "Center occupation"),
  ("party_tax_description_debts", "Debts"),
  ("party_tax_description_debt_collection", "Debt collection"),
  ("party_tax_description_expenses", "Diverse expenses"),
  ("party_tax_description_late_wages", "Old Wages"),
  ("party_tax_description_wages", "Wages"),
  ("party_tax_description_private_expenses", "Personal withdrawal"),
  ("party_tax_description_troops_hiring", "Troops training"),
  ("party_tax_description_troops_nuying", "Troops hiring"),
  ("party_tax_description_troops_selling", "Troops selling"),
  ("party_tax_description_prisoner_ransom", "Prisoner ransom"),
  ("party_tax_description_leader_ransom", "Leader ransom"),
  ("party_tax_description_caravan_wages", "Caravan wages"),
  ("party_tax_description_loot", "Loot"),
  ("party_tax_description_export", "Export taxes"),
  ("party_tax_description_import", "Import taxes"),
  ("party_tax_description_building", "Building costs"),
  ("party_tax_description_building_maintenance", "Building maintenance"),
  ("party_tax_description_bank_investments", "Bank investments"),
  ("party_tax_description_mercenary_contract", "Mercenary contract"),
  ("party_tax_description_mercenary_contract_pay", "Mercenary payments"),
  ("party_tax_description_banditry", "Banditry"),

  ("castle_name_plain_01", "plain_01"),
  ("castle_name_plain_02", "plain_02"),
  ("castle_name_plain_03", "plain_03"),

  ("castle_name_plain_wood_01", "plain_wood_01"),

  ("castle_name_plain_dark_01", "plain_dark_01"),

  ("castle_name_sea_01", "sea_01"),

  ("castle_name_steppe_01", "steppe_01"),

  ("castle_name_snow_01", "snow_01"),
  ("castle_name_snow_02", "snow_02"),

  ("castle_name_snow_wood_01", "snow_wood_01"),

  ("castle_name_desert_01", "desert_01"),

  ("castle_name_garden", "Castle Garden"),
  ("castle_name_plain_river", "Plain & River"),
  ("castle_name_dross_delnoch", "Dross Delnoch"),

  ("playername", "{playername}"),
  ("my_lord|my_lady", "{My Lord/My Lady}"),
  ("my_liege", "My Liege"),

  ("my_king_culture_1", "{My King/My Queen}"),
  ("my_king_culture_2", "{My King/My Queen}"),
  ("my_king_culture_3", "My Khan"),
  ("my_king_culture_4", "{My King/My Queen}"),
  ("my_king_culture_5", "Governor"),
  ("my_king_culture_6", "{My Sultan/My Sultana}"),

  ("start_game_introduction_text", "Welcome to Calradia, a land torn with strife and conflicts.^\
 It is an ideal situation for an ambitious person to climb the ranks of society.^^\
 You will first need to select your character gender."),

  ("start_game_intro_1", "Before you were born, your family lived..."),
  ("start_game_intro_1_choice_swadian", "In the plains of Swadia.^^You do not know when or why your parents left their homeland. You occasionally heard a glimpse of information about the region. But you know your parents didn't like to talk about the subject. Whether forced to leave or compeled to, you only know that there was some nostalgia to their word."),
  ("start_game_intro_1_choice_vaegir", "In the Vaegir tundra.^^You do not know when or why your parents left their homeland. You occasionally heard a glimpse of information about the region. But you know your parents didn't like to talk about the subject. Whether forced to leave or compeled to, you only know that there was some nostalgia to their word."),
  ("start_game_intro_1_choice_khergit", "In the Khergit steppes.^^You do not know when or why your parents left their homeland. You occasionally heard a glimpse of information about the region. But you know your parents didn't like to talk about the subject. Whether forced to leave or compeled to, you only know that there was some nostalgia to their word."),
  ("start_game_intro_1_choice_nord", "On the Nordic coasts.^^You do not know when or why your parents left their homeland. You occasionally heard a glimpse of information about the region. But you know your parents didn't like to talk about the subject. Whether forced to leave or compeled to, you only know that there was some nostalgia to their word."),
  ("start_game_intro_1_choice_rhodok", "In the Rhodok hills.^^You do not know when or why your parents left their homeland. You occasionally heard a glimpse of information about the region. But you know your parents didn't like to talk about the subject. Whether forced to leave or compeled to, you only know that there was some nostalgia to their word."),
  ("start_game_intro_1_choice_sarranid", "In the Sarranid deserts.^^You do not know when or why your parents left their homeland. You occasionally heard a glimpse of information about the region. But you know your parents didn't like to talk about the subject. Whether forced to leave or compeled to, you only know that there was some nostalgia to their word."),
  ("start_game_intro_1_choice_foreign", "In a far away land.^^You occasionally heard about Calradia, a land torn with strife and conflicts. And wondered how different life would be there."),

  ("start_game_intro_2", "Your father was..."),
  ("start_game_intro_2_choice_noble", "An impoverished noble^^You came into the world a {reg10?daughter:son} of declining nobility,\
 owning only the house in which they lived. However, despite your family's hardships,\
 they afforded you a good education and trained you from childhood for the rigors of aristocracy and life at court."),
  ("start_game_intro_2_choice_farmer", "A farmer^^Both your parents had to manage parts of a farm owned by the lord,\
 life was hard and money was scarse, but they tried their best to keep food on the table everyday.\
 You would sometimes help in the fields which made you used to hard labor early on."),
  ("start_game_intro_2_choice_hunter", "A hunter^^You were the {reg10?daughter:son} of a family who lived off the woods,\
 doing whatever they needed to make ends meet. Hunting, woodcutting, making arrows,\
 even a spot of poaching whenever things got tight. Winter was never a good time for your family\
 as the cold took animals and people alike, but you always lived to see another dawn,\
 though your brothers and sisters might not be so fortunate."),
  ("start_game_intro_2_choice_artisan", "An artisan^^Born in a large city from talented craftsmen,\
 your parents provided you with a comfortable life. Work was hard for them but they were able to afford you a good education."),
  ("start_game_intro_2_choice_court_advisor", "A court advisor^^You were the {reg10?daughter:son} of favored advisors of the local lord,\
 your family was not wealthy, but you had enough to live well enough and had the priviledge of interacting with nobility."),
  ("start_game_intro_2_choice_trader", "A travelling merchant^^You were born the {reg10?daughter:son} of travelling merchants,\
 always moving from place to place in search of a profit. Although your parents were wealthier than most\
 and educated you as well as they could, you found little opportunity to make friends on the road,\
 living mostly for the moments when you could sell something to somebody."),
  ("start_game_intro_2_choice_mercenary", "A veteran warrior^^As a child, your family scrabbled out a meagre living from your father's wages\
 as a guardsman to the local lord. It was not an easy existence, and you were too poor to get much of an\
 education. You learned mainly how to defend yourself on the streets, with or without a weapon in hand."),
  ("start_game_intro_2_choice_outlaw", "A wanted outlaw^^As the {reg10?daughter:son} of a thief, you had very little 'formal' education.\
 Instead you were out on the street, begging until you learned how to cut purses, cutting purses\
 until you learned how to pick locks, all the way through your childhood.\
 Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways."),
  ("start_game_intro_2_choice_nomad", "A steppe nomad^^You were a child of the steppe, born to a tribe of wandering nomads who lived\
 in great camps throughout the arid grasslands.\
 Like the other tribesmen, your family revered horses above almost everything else, and they taught you\
 how to ride almost before you learned how to walk."),

  ("start_game_intro_3", "You started to learn about the world almost as soon as you could walk and talk. You spent your early life as..."),
  ("start_game_intro_3_choice_street_urchin", "A street urchin^^As a {reg10?girl:boy} growing out of childhood,\
 you took to the streets, doing whatever you must to survive.\
 Begging, thieving and working for gangs to earn your bread, you lived from day to day in this violent world,\
 always one step ahead of the law and those who wished you ill."),
  ("start_game_intro_3_choice_apprentice", "A craftsman's apprentice^^As a {reg10?girl:boy} growing out of childhood,\
 you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your\
 new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as\
 you wished to stay."),
  ("start_game_intro_3_choice_stable_hand", "A stable hand^^As a {reg10?girl:boy} growing out of childhood,\
 you helped care for horses at a local stable. You learned to care for their needs and tend their wounds,\
 the owner even gave you valuable riding lessons."),
  ("start_game_intro_3_choice_farmer", "A helper in a farm^^As a {reg10?girl:boy} growing out of childhood,\
 you helped doing manual labor at the farm. At your young age you could not do as much as the adult, but you tried your best picking crops and\
 carrying smaller loads."),
  ("start_game_intro_3_choice_errand_boy", "An errand {boy/girl}^^As a {reg10?girl:boy} growing out of childhood,\
 you ran errands for just about anybody. Transporting goods, delivering messages, you were willing to do almost any job for some pocket change."),
  ("start_game_intro_3_choice_schooled", "A school student.^^As a {reg10?girl:boy} growing out of childhood,\
 you were given the opportunity and time to study various subjects in a school. With an eagerness to learn you rigorously studied history, mathematics and even medicine."),
  ("start_game_intro_3_choice_page", "A page at a nobleman's court.^^As a {reg10?girl:boy} growing out of childhood,\
 you were sent to live in the court of one of the nobles of the land.\
 There, your first lessons were in humility, as you waited upon the lords and ladies of the household.\
 But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict\
 and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords."),

  ("start_game_intro_4", "As you got recognition, you started becoming known for being..."),
  ("start_game_intro_4_choice_generous", "Generous"),
  ("start_game_intro_4_choice_ruthless", "Ruthless"),
  ("start_game_intro_4_choice_caring", "Caring"),
  ("start_game_intro_4_choice_charm", "Charming"),
  ("start_game_intro_4_choice_shrewd", "Shrewd"),
  ("start_game_intro_4_choice_strong", "Strong"),
  ("start_game_intro_4_choice_energy", "Full of energy"),
  ("start_game_intro_4_choice_calculating", "Calculating"),

  ("start_game_intro_5", "During your early adulthood you became..."),
  ("start_game_intro_5_choice_guard", "A city watch^^Though the distinction felt sudden to you,\
 seeing the effects of banditry on the common people you got hired into the city guards.\
 Peacekeeping, checking permits and being vigilant during the night were among your duties to the city.\
 The pay was meagre for a job you thought necessary, but someone had to do it."),
  ("start_game_intro_5_choice_outlaw", "A wanted outlaw^^Though the distinction felt sudden to you,\
 you were tired of toiling the land for meagre pay. You decided that taking things from others was easier.\
 Once you had become an outlaw there was no way back, only the promise of the gallows were you to get caught."),
  ("start_game_intro_5_choice_pickpocket", "A pickpocket in the streets^^Though the distinction felt sudden to you,\
 you started operating in the business of picking pockets.\
 You had to stalk your target while waiting for the opportune moment and somedays you were unlucky and had to go to bed hungry."),
  ("start_game_intro_5_choice_messenger", "A messenger^^Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg10?woman:man}, and the whole world seemed to change around you.\
 An opportunity arose to deliver a letter in exchange for gold, and then another.\
 You became know as a reliable {reg10?woman:man} that could deliver information between two places as fast as your feet could carry you.\
 Life on the road was not easy, and you nearly became prey to bandits on multiple occasions.\
 But your knowledge of the land and your quick feet always carried you through to your destination."),
  ("start_game_intro_5_choice_hunter", "A game poacher^^Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg10?woman:man}, and the whole world seemed to change around you.\
 Dissatisfied with common men's desperate scrabble for coin, you took to your local lord's own forests\
 and decided to help yourself to its bounty, laws be damned. You hunted stags, boars and geese and sold\
 the precious meat under the table. You cut down trees right under the watchmen's noses and turned them into\
 firewood that warmed many freezing homes during winter. All for a few silvers, of course."),
  ("start_game_intro_5_choice_farmer", "A farmer^^Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg10?woman:man}, and the whole world seemed to change around you.\
 You went and started a simple life of farming. It is hard work and the taxes felt overbearing at times,\
 but the routine of the days kept you busy and fed most of the time."),
  ("start_game_intro_5_choice_merchant", "A travelling merchant^^Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg10?woman:man}, and the whole world seemed to change around you.\
 Heeding the call of the open road, you travelled from village to village buying and selling what you could.\
 It was not a rich existence, but you became a master at haggling even the most miserly elders into\
 giving you a good price. Soon, you knew, you would be well-placed to start your own trading empire..."),
  ("start_game_intro_5_choice_mercenary", "A mercenary.^^Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg10?woman:man}, and the whole world seemed to change around you.\
 You signed on with a mercenary company and travelled far from your home. The life you found was rough and\
 ready, marching to the beat of strange drums and learning unusual ways of fighting.\
 There were men who taught you how to wield any weapon you desired, and plenty of battles to hone your skills.\
 You were one of the charmed few who survived through every campaign in which you marched."),
  ("start_game_intro_5_choice_artisan", "An artisan^^Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg10?woman:man}, and the whole world seemed to change around you.\
 You pursued a career as a smith, crafting items of function and beauty out of simple metal.\
 As time wore on you became a master of your trade, and fine work started to fetch fine prices.\
 With food in your belly and logs on your fire, you could take pride in your work and your growing reputation."),
  ("start_game_intro_5_choice_scout", "A scout for the local lord^^Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg10?woman:man}, and the whole world seemed to change around you.\
 You ended up as a scout in the army of the local lord, a good eye and constant vigilance was required to aquire information while remaining undetected.\
 Knowing when to run away was a necessity to avoid getting into fights with unfavorable odds and learning the way of the land vital to successfully escaping one."),
  ("start_game_intro_5_choice_court", "A court assistant^^Though the distinction felt sudden to you,\
 you became a {reg10?woman:man} that was capable of reading and writing.\
 The minor courts were always in need of learned {reg10?women:men} to handle affairs.\
 You learned the ins and outs of politics, how to govern a fief, to talk to foreign envoys, you even had to make minor military decisions.\
 You led a comfortable life, even if dealing with nobility was always a headache."),
  ("start_game_intro_5_choice_beggar", "A beggar in the streets^^Though the distinction felt sudden to you,\
 not out of choice, but out of circumstance, you ended up begging on the streets of a great city to sustain yourself.\
 you wandered the streets envying the wealthier citizens. A feeling of injustice, despair and anger rose in you as you felt left out, abandonned by society.\
 Every day was a struggle, however, you learned to run away when needed, to take the blows when blame fell on you and to look tough to prevent your few posessions from being stolen."),
  ("start_game_intro_5_choice_doctor", "A wandering doctor^^Though the distinction felt sudden to you,\
 somewhere along the way you had become a {reg10?woman:man}, and the whole world seemed to change around you.\
 You packed your few belongings and went out into the world to share your knowledge of medicine.\
 You helped those in need, accepting lodging and food as payment for your services.\
 Though your scientific methods were not always welcome, you did not give up on helping others."),

  ("start_game_intro_6", "Soon everything changed and you decided to strike out on your own as an adventurer. What made you take this decision was..."),
  ("start_game_intro_6_choice_wanderlust", "Wanderlust.^^Only you know exactly what caused you to give up your old life and become an adventurer.\
 You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of\
 wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the\
 freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back..."),
  ("start_game_intro_6_choice_wealth", "Lust for money and power.^^Only you know exactly what caused you to give up your old life and become an adventurer.\
 To everyone else, it's clear that you're now motivated solely by personal gain.\
 You want to be rich, powerful, respected, feared.\
 You want to be the one whom others hurry to obey.\
 You want people to know your name, and tremble whenever it is spoken.\
 You want everything, and you won't let anyone stop you from having it..."),
  ("start_game_intro_6_choice_fame", "The promise of fame.^^Only you know exactly what caused you to give up your old life and become an adventurer.\
 Tales of heroes and kings, fabled battlefields and ancient myths. You knew the stories but wanted to experience them yourself,\
 become the hero of the land, the one who will be remembered for years to come."),
  ("start_game_intro_6_choice_forced", "Being forced out of your home.^^Only you know exactly what caused you to give up your old life and become an adventurer.\
 However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone\
 now, and you must face the fact that you're out in the wide wide world. Alone to sink or swim..."),
  ("start_game_intro_6_choice_revenge", "Personal revenge.^^Only you know exactly what caused you to give up your old life and become an adventurer.\
 Still, it was not a difficult choice to leave, with the rage burning brightly in your heart.\
 You want vengeance. You want justice. What was done to you cannot be undone,\
 and these debts can only be paid in blood..."),
  ("start_game_intro_6_choice_loss", "The loss of a loved one.^^Only you know exactly what caused you to give up your old life and become an adventurer.\
 All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so\
 painful. Perhaps your new life will let you forget,\
 or honour the name that you can no longer bear to speak..."),

  ("start_game_intro_7", "You arrived in Calradia, and decided to..."),
  ("start_game_intro_7_choice_swadia", "You came by caravan through the heartland of Calradia. Green shoots of wheat, barley and oats are beginning to push through the dark soil of the rolling hills, and on the lower slopes of the snowcapped mountains, herds of cattle and sheep are grazing on the spring grass. Occasionally, too, you catch sight of one of the great warhorses that are the pride of the Swadian nobility. The land here is rich -- but also troubled, as the occasional burnt-out farm bears witness. You keep a wide berth of the forests, where desperate men have taken refuge, and it is some relief when you crest a ridge and catch sight of the great port of Praven, its rooftops made golden by the last rays of the setting sun."),
  ("start_game_intro_7_choice_vaegir", "You have come through the Vaegir highlands, a plateau exposed to the bitter winds from the north. The land here is frozen for most of the year, but the forests are rich with fur-bearing game, and the rivers are teaming with fish. The riches of the land draw the traders, but the traders in turn draw bandits. You saw the occasional dark figure mounted on a shaggy pony, watching the passage of your caravan from a snowy ridge, and were glad when the spires of Reyvadin came into view across the wide valley of the Boluk river."),
  ("start_game_intro_7_choice_khergit", "You came with a caravan, crossing the mountains that border Calradia on the north and east, bringing spices from faraway lands to trade for wool and salt. The passes were still choked with snow, and it was hard going, but at last you crested a ridge and saw before you the Calradian steppes. On some hillsides the thin grass of spring was already turning yellow, but the lower slopes of the mountains were still a vibrant green. Herds of sheep and tawny steppe ponies drifted across them like clouds, testifying to the wealth of the Khergit khans. From time to time small groups of horsemen would follow your caravan from a distance, perhaps sizing up how well you could defend the wealth you carried, so it was with some relief that you saw the towers of Tulga rising up from the plains."),
  ("start_game_intro_7_choice_nord", "You took passage with a trading longship, carrying gyrfalcons from the furthest reaches of the north to be bartered for linen and wool. It sailed early in the season, but the master reckoned that the risks of drifting ice and later winter storms could be justified by arriving ahead of the Sea Raiders, who by April would be sailing forth from their island lairs to ravage Calradia's coasts. It was some relief when your ship came in sight of the delta of the Vyl and Boluk rivers, and a short while later, rowed past tidal flats and coastal marshes to the city of Sargoth, home to the Sea Raiders' distant kinsmen, the Nordic lords, who a few generations ago had carved themselves a kingdom in this rich but troubled land."),
  ("start_game_intro_7_choice_rhodok", "You came by ship, skirting the cliffs where the Rhodok highlands meet the sea. Much of the coastline was obscured by tendrils of fog that snaked down the river valleys, but occasionally you caught sight of a castle watchtower rising above the mists -- and on one occasion, a beacon fire burning to warn of an enemy warband. You knew that you were relatively safe at sea, as you were too far south to risk encountering the sea raiders who trouble the coasts of the Nordic lands, but it was still a relief to reach the Selver estuary, gateway to the port of Jelkala, and see a Rhodok galley riding at anchor, its pennants fluttering in the evening breeze."),
  ("start_game_intro_7_choice_sarranid", "You came with a caravan, crossing the great desert to the east of Calradia. The bedouin guides chose your route carefully, leapfrogging through treacherous dune fields and across empty gravel plains to low-lying oases rich with orchards and date palms. Your great fear was that the caravan might lose its way and perish of thirst. The small bands of raiders who hovered just out of bowshot, waiting to pick off stragglers, were oddly a comfort -- at least water could be no more than a day's ride away. It was a great relief when the mountains came into view, and on the evening of the following day you crested a rocky pass and in the distance could make out the sea, and the towers of Shariz silhouetted against the sunset."),

  ("attribute_strength", "STR"),
  ("attribute_agility", "AGI"),
  ("attribute_intelligence", "INT"),
  ("attribute_charisma", "CHA"),

  ("skill_trade","Trade"),
  ("skill_leadership","Leadership"),
  ("skill_prisoner_management", "Prisoner Management"),
  ("skill_reserved_1","Reserved Skill"),
  ("skill_reserved_2","Reserved Skill"),
  ("skill_reserved_3","Reserved Skill"),
  ("skill_reserved_4","Reserved Skill"),
  ("skill_persuasion","Persuasion"),
  ("skill_engineer","Engineer"),
  ("skill_first_aid", "First Aid"),
  ("skill_surgery","Surgery"),
  ("skill_wound_treatment","Wound Treatment"),
  ("skill_inventory_management","Inventory Management"),
  ("skill_spotting","Spotting"),
  ("skill_pathfinding","Path-finding"),
  ("skill_tactics","Tactics"),
  ("skill_tracking","Tracking"),
  ("skill_trainer","Trainer"),
  ("skill_trainer_2","Trainer"),
  ("skill_reserved_6","Reserved Skill"),
  ("skill_reserved_7","Reserved Skill"),
  ("skill_reserved_8","Reserved Skill"),
  ("skill_looting","Looting"),
  ("skill_horse_archery","Horse Archery"),
  ("skill_riding","Riding"),
  ("skill_athletics","Athletics"),
  ("skill_shield","Shield"),
  ("skill_weapon_master","Weapon Master"),
  ("skill_reserved_9","Reserved Skill"),
  ("skill_reserved_10","Reserved Skill"),
  ("skill_reserved_11","Reserved Skill"),
  ("skill_reserved_12","Reserved Skill"),
  ("skill_intimidation","Intimidation"),
  ("skill_power_draw","Power Draw"),
  ("skill_power_throw","Power Throw"),
  ("skill_power_strike","Power Strike"),
  ("skill_ironflesh","Ironflesh"),
  ("skill_reserved_14","Reserved Skill"),
  ("skill_reserved_15","Reserved Skill"),
  ("skill_reserved_16","Reserved Skill"),
  ("skill_reserved_17","Reserved Skill"),
  ("skill_reserved_18","Reserved Skill"),

  ("proficiency_one_handed_weapon", "One Handed Weapons"),
  ("proficiency_two_handed_weapon", "Two Handed Weapons"),
  ("proficiency_polearm", "Polearms"),
  ("proficiency_archery", "Archery"),
  ("proficiency_crossbow", "Crossbows"),
  ("proficiency_throwing", "Throwing"),

  ("attribute_strength_description", "Every point adds +1 to hit points. The following skills can not be developed beyond 1/3 of Strength: Ironflesh, Power Strike, Power Throw, Power Draw, Intimidation."),
  ("attribute_agility_description", "Each point gives you five weapon points and slightly increases foot movement speed on the battlefield. The following skills can not be developed beyond 1/3 of Agility: Weapon Master, Shield, Athletics, Riding, Horse Archery, Looting."),
  ("attribute_intelligence_description", "Every point to intelligence immediately gives one extra skill point. The following skills can not be developed beyond 1/3 of Intelligence: Trainer, tracking, Tactics, Path-finding, Spotting, Inventory Management, Wound Treatment, First Aid, Engineer."),
  ("attribute_charisma_description", "Each point increases the amount of shared experience gained after combat by 2%. The following skills can not be developed beyond 1/3 of Charisma: Persuasion, Prisoner Management, Leadership, Trade"),

  ("skill_trade_description","Every level of this skill reduces your trade penalty. (Party skill)"),
  ("skill_leadership_description","Every point reduces troop wages by 2%. (Leader skill)"),
  ("skill_prisoner_management_description", "Every level of this skill increases maximum number of prisoners by +5 + 10% of your party size and reduces the penalties of having prisoners in your party. (Leader skill)"),
  ("skill_reserved_1_description","Reserved Skill"),
  ("skill_reserved_2_description","Reserved Skill"),
  ("skill_reserved_3_description","Reserved Skill"),
  ("skill_reserved_4_description","Reserved Skill"),
  ("skill_persuasion_description","This skill helps you make other people accept your point of view. It also lowers the minimum level of relationship needed to get NPCs to do what you want. (Personal skill)"),
  ("skill_engineer_description","This skill allows you to construct siege equipment and fief improvements more efficiently. (Party skill)"),
  ("skill_first_aid_description", "Heroes regain 5% per skill level of hit-points lost during mission. (Party skill)"),
  ("skill_surgery_description","Each point to this skill gives a 4% chance that a mortally struck party member will be wounded rather than killed. (Party skill)"),
  ("skill_wound_treatment_description","Party healing speed is increased by 20% per level of this skill. (Party skill)"),
  ("skill_inventory_management_description","Increases inventory capacity by +6 per skill level. (Leader skill)"),
  ("skill_spotting_description","Party seeing range is increased by 10% per skill level. (Party skill)"),
  ("skill_pathfinding_description","Party map speed is increased by 3% per skill level. (Party skill)"),
  ("skill_tactics_description","Every two levels of this skill increases starting battle advantage by 1 and party morale by 10%. (Party skill)"),
  ("skill_tracking_description","Tracks become more informative. (Party skill)"),
  ("skill_trainer_description","Every day, each hero with this skill adds some experience to every other member of the party whose level is lower than his/hers. Experience gained goes as: {0,4,16,23,30,38,46,55,65,80}. (Personal skill)"),
  ("skill_trainer_2_description","This skill helps you train and recruit new troops faster and for a lower price. Trains hero companions' weapon proficiencies. (Personal skill)"),
  ("skill_reserved_6_description","Reserved Skill"),
  ("skill_reserved_7_description","Reserved Skill"),
  ("skill_reserved_8_description","Reserved Skill"),
  ("skill_looting_description","This skill increases the amount of loot obtained by 10% per skill level. (Party skill)"),
  ("skill_horse_archery_description","Reduces damage and accuracy penalties for archery and throwing from horseback. (Personal skill)"),
  ("skill_riding_description","Enables you to ride horses of higher difficulty levels and increases your riding speed and manuever. (Personal skill)"),
  ("skill_athletics_description","Improves your running speed. (Personal skill)"),
  ("skill_shield_description","Reduces damage to shields (by 8% per skill level) and improves shield speed and coverage. (Personal skill)"),
  ("skill_weapon_master_description","Makes it easier to learn weapon proficiencies. Decreases the weapon proficiencies decay over time. (Personnal skill)"),
  ("skill_reserved_9_description","Reserved Skill"),
  ("skill_reserved_10_description","Reserved Skill"),
  ("skill_reserved_11_description","Reserved Skill"),
  ("skill_reserved_12_description","Reserved Skill"),
  ("skill_intimidation_description","This skill helps you make other people fear you and submit to your point of view. (Personal skill)"),
  ("skill_power_draw_description","Lets character use more powerful bows. Each point to this skill (up to four plus power-draw requirement of the bow) increases bow damage by 14%. (Personal skill)"),
  ("skill_power_throw_description","Each point to this skill increases throwing damage by 10%. (Personal skill)"),
  ("skill_power_strike_description","Each point to this skill increases melee damage by 8%. (Personal skill)"),
  ("skill_ironflesh_description","Each point to this skill increases hit points by +2. (Personal skill)"),
  ("skill_reserved_14_description","Reserved Skill"),
  ("skill_reserved_15_description","Reserved Skill"),
  ("skill_reserved_16_description","Reserved Skill"),
  ("skill_reserved_17_description","Reserved Skill"),
  ("skill_reserved_18_description","Reserved Skill"),

  ("proficiency_one_handed_weapon_description", "One Handed Weapons: Covers usage of one hander swords, axes and blunt weapons."),
  ("proficiency_two_handed_weapon_description", "Two Handed Weapons: Covers usage of two handed swords, great axes and mauls."),
  ("proficiency_polearm_description", "Polearms: Covers usage of pole weapons like spears, lances, staffs, etc."),
  ("proficiency_archery_description", "Archery: Covers usage of bows."),
  ("proficiency_crossbow_description", "Crossbows: Covers usage of crossbows."),
  ("proficiency_throwing_description", "Throwing: Covers usage of thrown weapons like javelins, darts, stones, etc."),

] + names + faces
