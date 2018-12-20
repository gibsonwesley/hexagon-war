# Import Libraries

import random
from random import shuffle
from random import randint

# Game Menu



# Card Creation

knight_card = "K"
victory_card = "V"
roadbuild_card = "R"
monopoly_card = "M"
payday_card = "P"

d_card = list(knight_card * 14 + victory_card * 5
		 + roadbuild_card * 2 + monopoly_card * 2 + payday_card * 2)
random.shuffle(d_card)

wood_re = "W"
wheat_re = "H"
sheep_re = "S"
brick_re = "B"
ore_re = "O"

# Tile Creation

wood = "W"
wheat = "H"
sheep = "S"
brick = "B"
ore = "O"
desert = "D"

hexes = list(wood * 4 + wheat * 4 + sheep * 4 + brick * 3 + ore * 3)
random.shuffle(hexes)

pips = [5, 2, 6, 3, 8, 10, 9, 12, 11, 4, 8, 10, 9, 4, 5, 6, 3, 11]

tiles = [hexe + str(pip) for hexe,pip in zip(hexes, pips)]
tiles.insert(randint(0, 17), desert)

# Hex Creation
	

# Victory Points

settlement = 1
city = 2
victory_card = 1
longest_road = 2
largest_army = 2

player1_points = 0
player2_points = 0
player3_points = 0
player4_points = 0

# Player Hand
















