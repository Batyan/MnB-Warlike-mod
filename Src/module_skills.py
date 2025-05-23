from header_common import *
from header_skills import *





skills = [
  ("trade","Trade",sf_base_att_cha|sf_effects_party,10,"Every level of this skill reduces your trade penalty. (Party skill)"),
  ("leadership","Leadership",sf_base_att_cha,10,"Every point reduces troop wages by 2%% and increase troops morale by 10%%. (Leader skill)"),
  ("prisoner_management", "Prisoner Management",sf_base_att_cha,10,"Every level of this skill increases maximum number of prisoners by +5 + 10%% of your party size and reduces the penalties of having prisoners in your party. (Leader skill)"),
  ("reserved_1","Reserved Skill 1",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."),
  ("reserved_2","Reserved Skill 2",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."),
  ("reserved_3","Reserved Skill 3",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."),
  ("reserved_4","Reserved Skill 4",sf_base_att_cha|sf_inactive,10,"This is a reserved skill."),
  ("persuasion","Persuasion", sf_base_att_cha,10, "This skill helps you make other people accept your point of view. It also lowers the minimum level of relationship needed to get NPCs to do what you want. (Personal skill)"),
  ("engineer","Engineer",sf_base_att_int|sf_effects_party,10,"This skill allows you to construct siege equipment and fief improvements more efficiently. (Party skill)"),
  ("first_aid", "First Aid",sf_base_att_int|sf_effects_party,10,"Heroes regain 5%% per skill level of hit-points lost during mission. (Party skill)"),
  ("surgery","Surgery",sf_base_att_int|sf_effects_party|sf_inactive,10,"Each point to this skill gives a 4%% chance that a mortally struck party member will be wounded rather than killed. (Party skill)"),
  ("wound_treatment","Wound Treatment",sf_base_att_int|sf_effects_party,10,"Party healing speed is increased by 20%% per level of this skill. (Party skill)"),
  ("inventory_management","Inventory Management",sf_base_att_int,10,"Increases inventory capacity by +6 per skill level. (Leader skill)"),
  ("spotting","Spotting",sf_base_att_int|sf_effects_party,10,"Party seeing range is increased by 10%% per skill level. (Party skill)"),
  ("pathfinding","Path-finding",sf_base_att_int|sf_effects_party,10,"Party map speed is increased by 3%% per skill level. (Party skill)"),
  ("tactics","Tactics",sf_base_att_int|sf_effects_party,10,"Every two levels of this skill increases starting battle advantage by 1, also increases party morale. (Party skill)"),
  ("tracking","Tracking",sf_base_att_int|sf_effects_party,10,"Tracks become more informative. (Party skill)"),
  ("trainer","Trainer",sf_base_att_int|sf_inactive,10,"Every day, each hero with this skill adds some experience to every other member of the party whose level is lower than his/hers. Experience gained goes as: {0,4,10,16,23,30,38,46,55,65,80}. (Personal skill)"),
  ("trainer_2","Trainer",sf_base_att_int,10,"This skill helps you train and recruit new troops more quickly for a lower price. Trains hero companions' weapon proficiencies. (Personal skill)"),
  ("reserved_6","Reserved Skill 6",sf_base_att_int|sf_inactive,10,"This is a reserved skill."),
  ("reserved_7","Reserved Skill 7",sf_base_att_int|sf_inactive,10,"This is a reserved skill."),
  ("reserved_8","Reserved Skill 8",sf_base_att_int|sf_inactive,10,"This is a reserved skill."),
  ("looting","Looting",sf_base_att_agi|sf_effects_party,10,"This skill increases the amount of loot obtained by 10%% per skill level. (Party skill)"),
  ("horse_archery","Horse Archery",sf_base_att_agi,10,"Reduces damage and accuracy penalties for archery and throwing from horseback. (Personal skill)"),
  ("riding","Riding",sf_base_att_agi,10,"Enables you to ride horses of higher difficulty levels and increases your riding speed and manuever. (Personal skill)"),
  ("athletics","Athletics",sf_base_att_agi,10,"Improves your running speed. (Personal skill)"),
  ("shield","Shield",sf_base_att_agi,1,"Reduces damage to shields (by 8%% per skill level) and improves shield speed and coverage. (Personal skill)"),
  ("weapon_master","Weapon Master",sf_base_att_agi,10,"Makes it easier to learn weapon proficiencies. Decreases the weapon proficiencies decay over time. (Personnal skill)"),
  ("reserved_9","Reserved Skill 9",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."),
  ("reserved_10","Reserved Skill 10",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."),
  ("reserved_11","Reserved Skill 11",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."),
  ("reserved_12","Reserved Skill 12",sf_base_att_agi|sf_inactive,10,"This is a reserved skill."),
  ("intimidation","Intimidation",sf_base_att_str,10,"This skill helps you make other people fear you and submit to your point of view. (Personal skill)"),
  ("power_draw","Power Draw",sf_base_att_str,10,"Lets character use more powerful bows. Each point to this skill (up to four plus power-draw requirement of the bow) increases bow damage by 14%%. (Personal skill)"),
  ("power_throw","Power Throw",sf_base_att_str,10,"Each point to this skill increases throwing damage by 10%%. (Personal skill)"),
  ("power_strike","Power Strike",sf_base_att_str,10,"Each point to this skill increases melee damage by 8%%. (Personal skill)"),
  ("ironflesh","Ironflesh",sf_base_att_str,10,"Each point to this skill increases hit points by +2. (Personal skill)"),
  ("reserved_14","Reserved Skill 14",sf_base_att_str|sf_inactive,10,"This is a reserved skill."),
  ("reserved_15","Reserved Skill 15",sf_base_att_str|sf_inactive,10,"This is a reserved skill."),
  ("reserved_16","Reserved Skill 16",sf_base_att_str|sf_inactive,10,"This is a reserved skill."),
  ("reserved_17","Reserved Skill 17",sf_base_att_str|sf_inactive,10,"This is a reserved skill."),
  ("reserved_18","Reserved Skill 18",sf_base_att_str|sf_inactive,10,"This is a reserved skill."),
]
