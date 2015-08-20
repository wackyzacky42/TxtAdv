# Creates a dictionary "_world"  variable that will hold all the coordinates and room names of the map.
_world = {}

# test!

def load_tiles():
	"""Parses a file that describes the world space into the _world object"""
	# Opens the map.txt file as read-only and assigns it the variable "f"
	with open('resources/map.txt', 'r') as f:
		# Uses the readlines method on the open file to create a list variable, where each line of the file is
		# a single entry in the list. From this we can get the number of rows in our map grid.
		rows = f.readlines()
	# Checks the number of entries in the "rows" variable and assigns that number to the "rows_amt" variable.
	# This gives us the number of rows in our map grid.
	rows_amt = len(rows)
	# Looks at the first entry in our "rows" list, breaks it apart at each TAB, and counts the amount of words it has.
	# This gives us the amount of columns in our map grid. It assumes all rows are the same length.
	cols_amt = len(rows[0].split('\t'))
	# Starts a loop that goes from 0 to the amount of entries in our "rows" variable, minus 1 (0-8).
	for y in range(rows_amt):
		# Breaks apart each given row at the TAB and assigns these individual words to a "cols" list variable.
		# This gives us the column entries of our current row.
		cols = rows[y].split('\t')
		# Starts a loop that goes from 0 to the value of our "cols_amt" variable, minus 1 (0-4)
		for x in range(cols_amt):
			# Cycles through each column entry in that specific row and replaces all the "\n" entries with an empty string.
			# The readlines() method automatically puts "\n" in for blank lines, so we need to get rid of them.
			tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
			# Checks the name of the tile and assigns it to the "_world" dictionary.
			# The current (x, y) coord is used for the key, the method version of tile_name (from the 'tiles' module)
			# is used for the dictionary entry's value.
			_world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

def tile_exists(x, y):
	# From the "_world" dict, returns the value for the given (x, y) key.
	return _world.get((x, y))