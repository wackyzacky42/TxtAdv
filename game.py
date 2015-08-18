import world, tiles, map
from player import Player


def play():
	# Calls the load_tiles() method from the world module, creating the game grid.
	world.load_tiles()
	# Creates a variable named "player" that's an instance of the Player() class in the player module.
	player = Player()
	# Finds the name of the room at the player's starting location and assigns it to the variable "room".
	room = world.tile_exists(player.location_x, player.location_y)
	# Prints the intro text for the player's starting room.
	print(room.intro_text())
	# Repeats the game loop as long as the player is alive and hasn't won.
	while player.is_alive() and not player.victory:
		# Updates the "room" variable based on the player's current location.
		room = world.tile_exists(player.location_x, player.location_y)
		# Calls the modify_player() method from the room the player is currently in.
		# This applies whatever room effect will hit the player, if any.
		room.modify_player(player)
		map.update_map()
		# Check the While conditions again in case the modify_player() method killed the player
		# or caused them to win.
		if player.is_alive() and not player.victory:
			# Print out the UI for choosing an action.
			print("Choose an action:")
			print("=================")
			# Finds a list of the available actions in the room the player is currently in.
			available_actions = room.available_actions()
			# Prints all the available actions individually in a list.
			for action in available_actions:
				print(action)
			# Asks for the player's input and assigns it to the "action_input" variable.
			action_input = raw_input("\nAction: ")
			# Loops through all the available actions and compares the player's input
			# to the action's hotkey. If they match, the do_action() method is called to execute the action.
			for action in available_actions:
				if action_input == action.hotkey:
					player.do_action(action, **action.kwargs)
					break

# If game.py is called directly in the command line, then execute the play() method
if __name__ == "__main__":
	play()