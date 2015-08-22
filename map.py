from __future__ import print_function
from operator import itemgetter
import world, tiles, player


def update_map():
	# map_grid = world._world
	map_copy = world._world
	map_grid = []
	# for (x, y), tile in map_grid.iteritems():
	for (x, y), tile in world._world.iteritems():
		# Run through all entries in _world and replace room names with blank squares or known squares
		if tile == None:
			tile = "   "
		#elif (tile.x, tile.y) == (game.player_one.location_x, game.player_one.location_y):
			#tile = "[x]"
		elif tile.been_entered == True:
			tile = "[ ]"
		else:
			tile = "   "
		map_grid.append((x, y, tile))
	map_grid = sorted(map_grid, key = itemgetter(1, 0))
	# print(map_grid)

# adding new stuff!!

	# map_grid = sorted(map_grid.items(), key = itemgetter((1, 0),1))
	
	
	# x_new = 0
	# y_new = 0

	# for (x, y), tile in map_grid:
		# x_new = y
		# y_new = x
		# map_grid[(x, y), tile] = (x_new, y_new), tile
	
	# print (sorted(map_grid, key = itemgetter(0, 1)))
	return map_grid
	
def print_map():
	map_grid = update_map()
	cols_amt = 0
	rows_amt = 0
	
	for (x, y, tile) in map_grid:
		if y < 1:
			cols_amt += 1
		else:
			pass
	
	x_count = 1
	loops = 1
	for (x, y, tile) in map_grid:
		if (x_count/loops) == cols_amt:
			print(tile)
			x_count += 1
			loops += 1
		else:
			print(tile, sep = '', end = '')
			x_count += 1

		
# create a blank grid based on the dimensions of _world
# check all the tile for the been_entered flag
# draw the tiles that have been visited. leave the others blank

# track which rooms the player's been to
# run through an invisible grid of all possible rooms
# display those rooms in ascii format
# display the player's current location
# add the map option to available_moves