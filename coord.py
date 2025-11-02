# Script by mmonroe@PhantomDevOps
# Script scales with square world sizes.

def coord(x=0, y=0):
  
	# Sanitation - helps prevent needless movement wth values greater than world size. (Doesn't work with negative values)
	if x > get_world_size():
		x = x % get_world_size()
	if y > get_world_size():
		y = y % get_world_size()
	if x == get_world_size():
		x = 0
	if y == get_world_size():
		y = 0
		
	current_pos_x = get_pos_x()
	current_pos_y = get_pos_y()
	x = x - current_pos_x
	y = y - current_pos_y

	if x >= 0:
		for i in range(x):
			move(East)
	else:
		x = (x * x) ** 0.5
		for i in range(x):
			move(West)
			
	if y >= 0:
		for i in range(y):
			move(North)
	else:
		y = (y * y) ** 0.5
		for i in range(y):
			move(South)
