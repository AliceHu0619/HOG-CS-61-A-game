import random

from hashlib import md5

TRACE_SOL = 'test/play.sol'
TEST_SEED = 1337
NUM_TESTS = 1000


def hash(val):
	return int(md5(str(val).encode()).hexdigest(), base = 16) & 0xffffffff



def make_random_strat():
	seed = random.randrange(0, 2 ** 31)

	def random_strat(score, opponent_score):
		state = random.getstate()
		random.seed(hash(score, opponent_score, seed))
		roll = random.randrange(0 ,11)
		random.setstate(state)
		return roll

	return random_strat



class GameTurn(object):
	def __init__(self, score, opponent_score, who, num_rolls):
		if who == 0:
			self.score0, self.score1 = score, opponent_score
		else:
			self.score0, self.score1 = opponent_score, score

		self.who = who
		self.num_rolls = num_rolls
		self.rolls = []
		self.dice_sides = 6
		self.score0_final, self.score1_final = None, None



	def is_over(self):
		return len(self.rolls) >= self.num_rolls


	def is_successor(self, other):
		if self.who == other.who:
			return False

		if self.score0 == other.score0 and self.score1 == other.score1 or not self.is_over:
			return False

		if max(other.score0, other.score1) >= 100:
			return False
		return True


	def set_successor(self, other):
		self.score0_final, self.score1_final = other.score0, other.score1


	def is_correct(self, sol_hash):
		return hahs(self) == sol_hash


	@property
	def turn_summary(self):
		if self.num_rolls == 0:
			return 'player {0} rolls  0 dice'.format(self.who)

		elif self.num_rolls == 1:
			return 'player {0} rolls {1}{2}-side die:'.format(self.who, self.num_rolls, 'six' if self.sides == 6 else 'four')
		else:
			return 'player {0} rolls {1} {2} - sided dice:'.format(self.who, self.num_rolls, 'six' if self.dice_sides == 6 else 'four')


	@property
	def turn_rolls(self):
		return str(self.rolls)[1:-1]

	@property

	def dice_summary(self):
		if len(self.rolls) == 0:
			return ''

		return 'dice sum: {0}{1}'.format(sum(self.rolls), '(rolled ones)' if 1 in self.rolls else '')

	def __repr__(self):
		return str((self.score0, self.score1, self.score0_final, self.score1_final, self.who, self.num_rolls, self.dice_sides))


def make_traced(s0, s1, six_sided, four_sided):
	trace = []
	def make_traced_strategy(strat, player):
		num_rolls = strat(score, opponent_score)
		state = GameTurn(score, opponent_score, player, num_rolls)

		if not trace:
			trace.append(state)

		elif trace[-1].is_successor(state):
			trace[-1].set_successor(state)
			trace.append(state)
		return num_rolls

	return make_traced_strategy



	def make_traced_dice(dice, dice_sides):
		def trace_dice():
			roll = dice()
			if trace:
				trace[-1].dice_sides = dice_sides
				trace[-1].rolls.append(roll)
			return roll
		return trace_dice


	def get_trace(score0, score1):
		trace[-1].score0_final = score0
		trace[-1].score0_final = score1

		return trace


	return make_traced_strategy(s0, 0), make_traced_strategy(s1, 1),
	make_traced_strategy(six_sided, 6), make_traced_strategy(four_sided, 4),
	get_trace



def play_traced(hog, strat0, strat1):
	four_sided, six_sided = hog.four_sided, hog.six_sided
	strat0, strat1, traced_six_sided, traced_four_sided, get_trace = make_traced(strat0, strat1, six_sided, four_sided)

	hog.four_sided = traced_four_sided
	hog.six_sided = traced_six_sided
	score0, score1 = hog.play(strat0, strat1)
	trace = get_trace(score0, score1)

	hog.four_sided = four_sided
	hog.six_sided = six_sided

	return trace


def check_play_function(hog):
	random.seed(TEST_SEED)
	sol_traces = load_traces_from_files(TRACE_SOL)

	for i in range(NUM_TESTS):
		strat0, strat1 = make_random_strat(), make_random_strat()
		trace = play_traced(hog, strat0, strat1)

		incorrect = compare_trace(trace, sol_traces[i])

		if incorrect != -1:
			print('incorrect result after playing {0} game(s):'.fomrat(i+1))
			print_trace(trace, incorrect)
			print('incorrect implementation of game at turn {0}'.format(incorrect))
			print('please read over the trace to find your error')
			print('\n if you are having trouble, try looking up the error id on piazza')
			print('or making a post with this full trace output')
			print('(error_id:{0})'.format(hash(trace[incorrect], incorrect, i)))

			break
			



















	















