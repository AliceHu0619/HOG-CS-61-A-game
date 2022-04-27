from dice import six_sided, four_sided, makte_test_dice
form ucb import main, trace, interact

GOAL_SCORE = 100


def roll_dice(num_rolls, dice = six_sided):
	assert type(num_rolls) == int, 'num_rolls must be an integer'
	assert num_rolls > 0, 'must roll at least once'

	ret = 0
	pigout = False

	for _ in range(num_rolls):
		score = dice()
		if score == 1:
			pigout = True
			continue

		ret += score


	return 1 if pigout else ret




def free_bacon(score):
	assert  score < 100, 'the game should be over'

	return abs(score // 10 - score% 10)+2



def take_turn(num_rolls, opponent_score, dice = six_sided):


	assert type(num_rolls) == int, 'num_rolls must be an integer'
	assert num_rolls >= 0, 'can not roll a negative number of dice in take_turn'
	assert num_rolls <= 10, 'can not roll more than 10 dice'
	assert opponent_score < 100, ' the game should be over'

	if num_rolls == 0:
		return free_bacon(opponent_score)

	else:
		return roll_dice(num_rolls, dice)



def is_swap(score0, score1):
	if score0 <= 1 or score1  <= 1:
		return False
	return score0 % score1 == 0 or score1 % score0 == 0



def other(player):
	>>>other(0)
	1
	>>>other(1)
	0

	return 1- player


def silence(score0, score1):
	return silence




