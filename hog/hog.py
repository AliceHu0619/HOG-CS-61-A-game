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



def play(strategy0, strategy1, score0 = 0, score1 = 0, dice = six_sided, goal
= GOAL_SCORE, say = silence );
	player = 0
	while True:
		if score0 >= goal or score1 > goal:
			break
		if player == 0:
			num = strategy0(score0, score1)
			score0 += take_turn(num, score1,dice)
		else:
			num = strategy1(score1, score0)
			score1 += take_turn(num, score0, dice)

		if is_swap(score0, score1):
			score0, score1 = score1, score0

		player = other(player)
		say = say(score0, score1)

	return score0, score1




def say_scores(score0, score1):
	print('player 0 now has', score0, 'and player1 now has', score1)
	return say_scores


def announce_lead_changes(previous_leader = None):
	>>> f0 = announce_lead_changes()
	>>> f1 = f0(5, 0)
	>>> f2 = f1(5,12)
	>>> f3 = f2(8,12)
	>>> f4 = f3(8, 13)
	>>> f4 = f4(15,13)


	def say(score0, score1):
		if score0 > score1:
			leader = 0
		elif score1 > score0:
			leader = 1
		else:
			leader = None

		if leader != None and leader != previous_leader:
			print('player', leader, 'take the lead by', abs(score0- score1))

		return announce_lead_changes(leader)

	return say


def both(f, g):
	>>> h0 = both(say_scores, announce_lead_changes())
	>>> h1 = h0(10, 0)
	>>> h2 = h1(10, 6)
	>>> h3 = h2(6, 18)


	def say(score0, score1):
		return both(f(score0, score1), g(score0, score1))

	return say




def announce_highest(who, previous_high = 0, previous_score = 0):
	>>> f0 = announce_highest(1)
	>>> f1 = f0(11, 0)
	>>> f2 = f1(11, 1)
	>>> f3 = f2(20, 1)
	>>> f4 = f3(5, 20)
	>>> f5 = f4(20, 40)
	>>> f6 = f5(20, 55)

	assert who == 0 or who == 1, 'the who argument shoud indicate a player'

	def say(score0, score1):
		if who == 0:
			gain = score0 - previous_score
			new_score = score0

		else:
			gain = score1 - previous_score
			new_score = score1


		new_high = previous_high

		if gain > previous_high:
			new_high = gain
			print('{} {} ! That is the biggest gain yet for player{}'.format(gain, 'point' if gain > 1 else 'point', who) )
		return announce_highest(who, new_high, new_score)
	return say_scores


def always_roll(n):
	>>> strategy  = always_roll(5)
	>>> strategy(0, 0)
	5
	>>> strategy(99, 99)
	5

	def strategy(score, opponent_score):
		return n
	return strategy



def make_averaged(fn, num_samples = 1000):
	>>> dice = makte_test_dice(4,2,5,1)
	>>> average_dice = make_averaged(dice, 1000)
	>>> average_dice()



	def process(*args):
		tot = 0

		for _ in range(num_samples):
			tot += fn(*args)

		return tot/num_samples
	return process



def max_scoring_num_rolls(dice = six_sided, num_samples = 1000):
	>>> dice = makte_test_dice(1, 6)
	>>> max_scoring_num_rolls(dice)


	res, max_score = 1, 0

	for i in range(1, 11):
		average_dice = make_average(roll_dice, num_samples)
		score = average_dice(i, dice)

		if score > max_score:
			res, max_score = i, score




def winner(strategy0, strategy1):
	score0, score1 = play(strategy0, strategy1)
	if score0 > score1:
		return 0

	else:
		return 1


def average_win_rate(strategy, baseline = always_roll(4)):
	win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
	win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

	return (win_rate_as_player_0 + win_rate_as_player_1)/2



def run_experiments():
	if True:
		six_sided_max = max_scoring_num_rolls(six_sided)
		print('max scoring num rolls for six_sided dice:', six_sided_max)

	if False:
		print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

	if False:
		print('bacon strategy win rate', average_win_rate(bacon_strategy))


	if False:
		print('final strategy win rate:', average_win_rate(final_strategy))




def bacon_strategy(score, opponent_score, margin = 8, num_rolls = 4):
	gain = free_bacon(opponent_score)
	if gain >= margin:
		return 0

	return num_rolls



def swap_strategy(score, opponent_score, margin = 8, num_rolls = 4):
	gain = free_bacon(opponent_score)
	score += gain

	if gain >= margin and not is_swap(score, opponent_score)::

		return 0

	if is_swap(score, opponent_score) and opponent_score >= score + margin:
		return 0

	return num_rolls



def final_strategy(score, opponent_score):
	if opponent_score > score and is_swap(score + 1, opponent_score):
		return 10

	if score > opponent_score and is_swap(score + 1, opponent_score):
		return 0

	max_roll = max_scoring_num_rolls(num_samples = 100)
	num = swap_strategy(score, opponent_score, 100 - score, max_roll)

	if num == 0:
		return 0

	avg_dice = make_averaged(roll_dice, 100)

	for i in range(1, 4):
		gain = avg_dice(i)
		if score + gain >= 100:
			return i

	margin = opponent_score - score + 1 if opponent_score > score else 6
	return swap_strategy(score, opponent_score, margin, max_roll)

























































