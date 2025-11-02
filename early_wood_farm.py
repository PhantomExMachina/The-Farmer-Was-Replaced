# Requires helpers.py
# Requires trees and bushes
# This does NOT use sunflowers

from helpers import reset_position
from helpers import grassland

grid = get_world_size()
pattern_counter = 0
skip_tree = 0

reset_position()

# Because I'm OCD
grassland(get_world_size())

while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		if get_pos_x() % 2 == 0:
			if pattern_counter % 2 == 0:
				if skip_tree % 2 == 0:
					plant(Entities.Tree)
					skip_tree += 1
				else:
					plant(Entities.Bush)
					skip_tree -= 1
		else:
			if pattern_counter % 2 == 1:
				if skip_tree % 2 == 0:
					plant(Entities.Tree)
					skip_tree += 1
				else:
					plant(Entities.Bush)
					skip_tree -= 1
		move(North)
	pattern_counter += 1
	skip_tree += 1
	move(East)
  
