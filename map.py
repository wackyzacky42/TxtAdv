import world, tiles
from operator import itemgetter

def update_map():
	map_grid = world._world
	# print(map_grid)
	for (x, y), tile in map_grid.iteritems():
		# Run through all entries in _world and replace room names with blank squares or known squares
		if tile == None:
			tile = "   "
		elif tile.been_entered == True:
			tile = "[ ]"
		else:
			tile = "   "
		map_grid[(x, y)] = tile
	# print map_grid
	
	# print(map_grid.items())
	map_grid = sorted(map_grid.items(), key = itemgetter(0,1))
	# print map_grid
	# print (sorted(map_grid, key = itemgetter(0, 1)))
	return map_grid
	
def print_map():
	map_grid = update_map()
	cols_amt = 0
	rows_amt = 0
	print(cols_amt)
	
	for (x, y), tiles in map_grid:
		if x < 1:
			print(cols_amt)
		else:
			pass
		cols_amt += 1
	
	for (x, y), tile in map_grid:
		for x in range(cols_amt):
			if x == cols_amt:
				print (tile)
				x += 1
			else:
				print (tile),
	
	# for x in range((cols_amt)):
		# print(map_grid[(),
		
# create a blank grid based on the dimensions of _world
# check all the tile for the been_entered flag
# draw the tiles that have been visited. leave the others blank

# track which rooms the player's been to
# run through an invisible grid of all possible rooms
# display those rooms in ascii format
# display the player's current location
# add the map option to available_moves