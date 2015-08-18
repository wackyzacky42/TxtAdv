import world, tiles

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
	print map_grid
		

# class Map(object):
	# def __init__(self):
		# # stuff that happens on initialization

	# def update(self):
		# # stuff that happens to update the map's known areas

	# def display(self):
		# # stuff that displays the current map


# create a blank grid based on the dimensions of _world
# check all the tile for the been_entered flag
# draw the tiles that have been visited. leave the others blank



# track which rooms the player's been to
# run through an invisible grid of all possible rooms
# display those rooms in ascii format
# display the player's current location
# add the map option to available_moves

if __name__ == "__main__":
	update_map()