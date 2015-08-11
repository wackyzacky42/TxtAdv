import items, world, random

class Player(object):
	inventory = [items.Gold(15), items.Rock()]
	hp = 100
	location_x, location_y = (2, 4)
	victory = False
	
	def is_alive(self):
		return self.hp > 0
		
	def print_inventory(self):
		print("\n\nInventory:")
		print("==========\n")
		for item in self.inventory:
			print(item)
		print("")
			
	def move(self, dx, dy):
		self.location_x += dx
		self.location_y += dy
		print(world.tile_exists(self.location_x, self.location_y,).intro_text())
		
	def move_north(self):
		self.move(dx = 0, dy = -1)
		
	def move_south(self):
		self.move(dx = 0, dy = 1)
		
	def move_east(self):
		self.move(dx = 1, dy = 0)
		
	def move_west(self):
		self.move(dx = -1, dy = 0)
	
	def attack(self, enemy):
		best_weapon = None
		max_dmg = 0
		for i in self.inventory:
			if isinstance(i, items.Weapon):
				if i.damage > max_dmg:
					max_dmg = i.damage
					best_weapon = i
					
		print("\n\nYou use %s against %s!" % (best_weapon.name, enemy.name))
		enemy.hp -= best_weapon.damage
		if not enemy.is_alive():
			print("You killed the %s!" % (enemy.name))
			print("You have %s HP remaining.\n\n" % (self.hp))
		else:
			print("%s's HP is %s." % (enemy.name, enemy.hp))
			
	def do_action(self, action, **kwargs):
		action_method = getattr(self, action.method.__name__)
		if action_method:
			action_method(**kwargs)
			
	def flee(self, tile):
		"""Moves the player randomly to an adjacent tile"""
		available_moves = tile.adjacent_moves()
		r = random.randint(0, len(available_moves) - 1)
		self.do_action(available_moves[r])