# Most of these helper functions could use to refactoring - they aren't super modular and need to be refined. reset_position() is probably the most useful here for early farms.

def reset_position():
  # Sets drone position to 0, 0 (Lower left tile)
	current_pos = [get_pos_x(), get_pos_y()]
	
	if current_pos[0] != 0 or current_pos[1] != 0:
		for each in range(current_pos[0]):
			move(West)
		for each in range(current_pos[1]):
			move(South)

def plant_logic(type):
	if type == Entities.Carrot or type == Entities.Pumpkin or type == Entities.Cactus or type == Entities.Sunflower:
		if get_ground_type() != Grounds.Soil:
			till()
	else:
		if get_ground_type() != Grounds.Grassland:
			till()
	if get_entity_type() == type:
		if can_harvest():
			harvest()
			plant(type)
	else:
		harvest()
		plant(type)
		
def grassland(columns=get_world_size(), rows=get_world_size()):
	# Ensures tiles are Grounds.Grassland, leave blank for entire world.
	for i in range(columns):
		for i in range(rows):
			if get_ground_type() != Grounds.Grassland:
				till()
			move(North)
		move(East)
		
def soil(columns=get_world_size(), rows=get_world_size()):
	# Ensures tiles are Grounds.Soil, leave blank for entire world.
	for i in range(columns):
		for i in range(rows):
			if get_ground_type() != Grounds.Soil:
				till()
			move(North)
		move(East)
		
