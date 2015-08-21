from player import Player

class Action(object):
	def __init__(self, method, name, hotkey, **kwargs):
		self.method = method
		self.hotkey = hotkey
		self.name = name
		self.kwargs = kwargs
		
	def __str__(self):
		return "%s: %s" % (self.hotkey, self.name)
		
class MoveNorth(Action):
	def __init__(self):
		super(MoveNorth, self).__init__(method = Player.move_north, name = "Move north", hotkey = 'n')
		
class MoveSouth(Action):
	def __init__(self):
		super(MoveSouth, self).__init__(method = Player.move_south, name = "Move south", hotkey = 's')
		
class MoveEast(Action):
	def __init__(self):
		super(MoveEast, self).__init__(method = Player.move_east, name = "Move east", hotkey = 'e')
		
class MoveWest(Action):
	def __init__(self):
		super(MoveWest, self).__init__(method = Player.move_west, name = "Move west", hotkey = 'w')
		
class ViewInventory(Action):
	"""Prints out the player's inventory"""
	def __init__(self):
		super(ViewInventory, self).__init__(method = Player.print_inventory, name = "View inventory", hotkey = 'i')
		
class ViewMap(Action):
	"""Prints out the portion of the map the player has previouly explored"""
	def __init__(self):
		super(ViewMap, self).__init__(method = Player.print_map, name = "View map", hotkey = 'm')
		
class Attack(Action):
	def __init__(self, enemy):
		super(Attack, self).__init__(method = Player.attack, name = "Attack", hotkey = 'a', enemy = enemy)
		
class Flee(Action):
	def __init__(self, tile):
		super(Flee, self).__init__(method = Player.flee, name = "Flee", hotkey = 'f', tile = tile)