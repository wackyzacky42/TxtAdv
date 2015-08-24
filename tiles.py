import items, enemies, world, actions, player

class MapTile(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.been_entered = False

	def intro_text(self):
		raise NotImplementedError()

	def modify_player(self, player):
		raise NotImplementedError()
		
	def adjacent_moves(self):
		"""Returns all move actions for adjacent tiles"""
		moves = []
		if world.tile_exists(self.x + 1, self.y):
			moves.append(actions.MoveEast())
		if world.tile_exists(self.x - 1, self.y):
			moves.append(actions.MoveWest())
		if world.tile_exists(self.x, self.y - 1):
			moves.append(actions.MoveNorth())
		if world.tile_exists(self.x, self.y + 1):
			moves.append(actions.MoveSouth())
		return moves
		
	def available_actions(self):
		"""Returns all of the available actions in this room"""
		moves = self.adjacent_moves()
		moves.append(actions.ViewInventory())
		moves.append(actions.ViewMap(self.x, self.y))
		
		return moves
			
class StartingRoom(MapTile):
	def intro_text(self):
		if self.been_entered == False:
			return """
			You find yourself in a cave with a flickering torch on the wall.
			You can make out four paths, each equally dark and foreboding.
			"""
		else:
			return """
			You feel like you've been here before.
			This looks just like the room you started in.
			"""

	def modify_player(self, player):
		# Room has no action on the player
		if self.been_entered == False:
			self.been_entered = True
		else:
			pass

class LootRoom(MapTile):
	def __init__(self, x, y, item):
		self.item = item
		super(LootRoom, self).__init__(x, y)

	def add_loot(self, player):
		player.inventory.append(self.item)

	def modify_player(self, player):
		if self.been_entered == False:
			self.add_loot(player)
			self.been_entered = True
		else:
			pass
		
class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super(EnemyRoom, self).__init__(x, y)

	def modify_player(self, the_player):
		if self.enemy.is_alive():
			the_player.hp = the_player.hp - self.enemy.damage
			print ("%s does %s damage. You have %s HP remaining.\n\n" % (self.enemy.name, self.enemy.damage, the_player.hp))
		
		if self.been_entered == False:
			self.been_entered = True
		else:
			pass
			
	def available_actions(self):
		if self.enemy.is_alive():
			return [actions.Flee(tile = self), actions.Attack(enemy = self.enemy)]
		else:
			# return self.adjacent_moves()
			return super(EnemyRoom, self).available_actions()

class EmptyCavePath(MapTile):
	def intro_text(self):
		return """
		Another unremarkable part of the cave. You must forge onwards.
		"""

	def modify_player(self, player):
		if self.been_entered == False:
			self.been_entered = True
		else:
			pass

class GiantSpiderRoom(EnemyRoom):
	def __init__(self, x, y):
		super(GiantSpiderRoom, self).__init__(x, y, enemies.GiantSpider())

	def intro_text(self):
		if self.enemy.is_alive():
			return """
			A giant spider jumps down from its web in front of you!
			"""
		else:
			return """
			The corpse of a dead spider rots on the ground.
			"""
			
class SnakePitRoom(EnemyRoom):
	def __init__(self, x, y):
		super(SnakePitRoom, self).__init__(x, y, enemies.Snakes())

	def intro_text(self):
		if self.enemy.is_alive():
			return """
			You land in a pile of snakes and they begin to nibble at you!
			"""
		else:
			return """
			A heap of dead snakes dirties the floor.
			"""

class FindDaggerRoom(LootRoom):
	def __init__(self, x, y):
		super(FindDaggerRoom, self).__init__(x, y, items.Dagger())

	def intro_text(self):
		if self.been_entered == False:
			return """
			You notice something shiny on the table in the corner.
			It's a dagger! You pick it up.
			"""
		else:
			return """
			The table in the corner of this room 
			has a distinct outline in the dust layer.
			You've found everything interesting here already.
			"""

class Find5GoldRoom(LootRoom):
	def __init__(self, x, y):
		# current_gold = player.Player.inventory[0].amt
		# print(player.Player.inventory[0].amt)
		super(Find5GoldRoom, self).__init__(x, y, items.Gold(5))

	def add_loot(self, player):
		player.inventory[0] = items.Gold(player.inventory[0].amt + 5)
		# print(player.inventory[0].amt)

	def intro_text(self):
		if self.been_entered == False:
			return """
			You notice a small pile of shinies strewn about a table near the door.
			You found 5 Gold! Congrats!
			"""	
		else:
			return """
			You've already picked this room clean of Gold.
			Carry on, there's nothing to see here.
			"""
		
class LeaveCaveRoom(MapTile):
	def intro_text(self):
		return """
		You see a bright light in the distance...
		...it grows as you get closer! It's sunlight!
		
		Victory is yours!
		"""
		
	def modify_player(self, player):
		if self.been_entered == False:
			self.been_entered = True
		else:
			pass
			
		player.victory = True
		