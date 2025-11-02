# No sunflowers
# x1 Drone
# Requires helpers.py

from helpers import reset_position
from helpers import grassland

reset_position()
grassland()

while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		move(North)
	move(East)
