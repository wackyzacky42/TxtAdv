class Item(object):
	"""The base class for all items"""
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value
		
	def __str__(self):
		return "%s\n=====\n%s\nValue: %s\n" % (self.name, self.description, self.value)
		
class Gold(Item):
	def __init__(self, amt):
		self.amt = amt
		super(Gold, self).__init__(name = "Gold", description = "A pile of shiny gold coins.", value = self.amt)

class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super(Weapon, self).__init__(name, description, value)
		
	def __str__(self):
		return "%s\n=====\n%s\nValue: %s\nDamage: %s\n" % (self.name, self.description, self.value, self.damage)
		
class Rock(Weapon):
	def __init__(self):
		super(Rock, self).__init__(name = "Rock", description = "A fist-sized rock, suitable for bludgeoning.", value = 0, damage = 5)
		
class Dagger(Weapon):
	def __init__(self):
		super(Dagger, self).__init__(name = "Dagger", description = "A small dagger with some rust. Somewhat more dangerous than a rock.", value = 10, damage = 10)