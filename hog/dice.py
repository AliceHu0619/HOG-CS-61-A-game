from random import randint


def make_fair_dice(sides):
	assert type(sides) == int and sides >= 1, 'illegal value for sides'
	def dice():
		return randint(1, sides)

	return dice

four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)


def make_fair_dice(*outcomes):


	>>> dice = make_fair_dice(1,2,3)
	>>> dice()
	1
	>>>dice()
	2
	>>>dice()
	3
	>>>dice()
	1
	>>>dice()
	2



	assert len(outcomes) > 0, 'you must supply outcomes to make_test_dice'

	for o in outcomes:
		assert type(o) == int and o >= 1, 'outcomes is not a positive integer'

	index = len(outcomes) - 1

	def dice():
		nonlocal index
		index = (index + 1) % len(outcomes)
		return outcomes[index]

	return dice

