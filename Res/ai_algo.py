def canRecruit : int => bool
def getLordToFollow : int => int
def getMissionPartySizeMultiplier : int => int
def getAttackOrDefendTarget : int => int, int
def keepFollowing : int, int => bool
def keepAttacking : int, int => bool
def keepDefending : int, int => bool
def getClosestCenter : int, int => int
bool $g_disable_ai
int mission, missionObject, behavior, behaviorObject
int party_no, leader, home
bool at_war, prepare_war
int num_vassals, following, num_threats, army_prosperity, party_size, max_party_size, 
int ideal_party_size =
	max_party_size
	* max((
		25
		+ sqrt(
			num_threats
			+ prepare_war ? 2 : 0
			* 1000
			+ army_prosperity *10)),
		100)
	/100

int current_mission_minimum_party_size_multiplier

int tm_none = 0, tm_recruit = 1, tm_gather = 2, tm_prepare = 3, tm_follow = 4, tm_attack = 5, tm_defend = 6
int tb_none = 0, tb_move = 1, tb_follow = 2, tb_patrol = 3

def process_mission : 
	if($g_disable_ai == True)
		# do nothing
	else
		current_mission_minimum_party_size_multiplier = getMissionPartySizeMultiplier(leader)
		if(canRecruit(party_no) && party_size < ideal_party_size * current_mission_minimum_party_size_multiplier)
			mission = tm_recruit
		
		else if(mission == tm_none)
			if (at_war || prepare_war)
				if (num_vassals > 0 && following < num_vassals)
					mission = tm_gather
				else
					mission = tm_prepare
			else 
				mission = tm_none
		else if (mission == tm_gather)
			if(following == num_vassals)
				mission = tm_prepare
		else if (mission == tm_prepare)
			int following
			if(num_vassals <= 2)
				following = getLordToFollow(leader)
				mission = tm_follow
				missionObject = following
			if(!following)
				mission, missionObject = getAttackOrDefendTarget(leader)
		else if (mission == tm_follow)
			if(!keepFollowing(leader, missionObject))
				mission = tm_none
		else if (mission == tm_attack)
			if(!keepAttacking(leader, missionObject))
				mission = tm_none
		else if (mission == tm_defend)
			if(!keepDefending(leader, missionObject))

def process_ai : 
	if($g_disable_ai == True)
		# do nothing
		behavior = tb_none
	else
		if(mission == tm_none)
			if(at_war && num_threats == 0)
				process_peace_ai(party_no)
			else
				behavior = tb_patrol
				behaviorObject = home
		else if (mission == tm_recruit)
			behavior = tb_move
			if(party_size < ideal_party_size / 3)
				behaviorObject = getClosestCenter(party_no, tm_recruit)
			else if (party_size > ideal_party_size)
				process_mission(party_no)
			else
				behaviorObject = home
		else if (mission == tm_gather)
			behavior = tb_follow
			behaviorObject = home
		else if (mission == tm_prepare)
			behavior = tb_follow
			behaviorObject = home
		else if (mission == tm_follow)
		else if (mission == tm_attack)
		else if (mission == tm_defend)