from hog import GOAL_SCORE

def check_strategy_roll(score, opponent_score, num_rolls):
	>>> check_strategy_roll(10, 20, num_rolls= 100)
	>>> check_strategy_roll(20,10, num_rolls = 0.1)
	>>> check_strategy_roll(0, 0, num_rolls = None)

	msg = 'strategy({}, {}) return {}'.format(score, opponent_score,num_rolls)

	assert type(num_rolls) == int, msg + '(not an integer)'
	assert 0 <= num_rolls <= 10 , msg + '(invalid num of rolls)'




def check_strategy(strategy, goal = GOAL_SCORE):
	>>> def fail_15_20(score, opponent_score):
	...		if score != 15 or opponent_score != 20:
	...			return 5
	...

