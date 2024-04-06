"""A game about Catbus transporting passengers as fast as possible!"""

#	  ____        _    _                 
#	 / ___| __ _ | |_ | |__   _   _  ___ 
#	| |    / _` || __|| '_ \ | | | |/ __|
#	| |___| (_| || |_ | |_) || |_| |\__ \
#	 \____|\__,_| \__||_.__/  \__,_||___/
#
# A game about Catbus transporting passengers as fast as possible!
#
# You do not need to modify this file, though you are certainly
# welcome to read through it. We hope you enjoy and learn a lot
# from working on this project.
#	The CompClub Team


from random import choice, sample, seed

from .constants import CATPACITY, PASSENGERS, STOPS
from .magic import _destinations, _waiting

# Import the code written by the students. They might delete the
# function definition entirely, or do something else crazy, so
# we should try to be helpful if that happens.
try:
	from .status import print_status
	from .move import find_left_stop, find_right_stop
	from .names import input_name_list
	from .onoff import pick_up, drop_off
	from .win import game_is_finished
except ImportError:
	# TODO: Print a helpful error message.
	pass


def main():
	"""The entrypoint to the program."""
	welcome()

	# Initially, the Catbus has no passengers and is at the first stop.
	catbus = {
		'passengers': [],
		'location': STOPS[0],
	}

	# Generate where passengers begin and where they want to go.
	seed()
	for passenger in sample(PASSENGERS, 2 * CATPACITY):
		origin = choice(STOPS)
		_waiting[origin].append(passenger)
		# Make sure their destination is not their origin.
		destination = choice([stop for stop in STOPS if stop != origin])
		_destinations[passenger] = destination

	game(catbus)


def welcome():
	# TODO: A nice, colourful welcome screen.
	pass


def game(catbus):
	"""The main game loop."""
	time = 0
	while True:
		print(f'It is time {time}!')
		# Interpret EOF as quit.
		try:
			while True:
				command = input('/')
				if command.strip() != '':
					break
		except EOFError:
			break

		if command in ('s', 'status'):
			print_status(catbus['passengers'], catbus['location'])
		elif command in ('m', 'map'):
			print(', '.join(STOPS))
		elif command in ('l', 'left'):
			catbus['location'] = find_left_stop(catbus['location'])
			time += 1
		elif command in ('r', 'right'):
			catbus['location'] = find_right_stop(catbus['location'])
			time += 1
		elif command in ('p', 'pickup'):
			passengers = input_name_list()
			for passenger in passengers:
				pick_up(passenger, catbus['passengers'],
				        catbus['location'])
			time += 1
		elif command in ('d', 'dropoff'):
			passengers = input_name_list()
			for passenger in passengers:
				drop_off(passenger, catbus['passengers'],
				         catbus['location'])
			time += 1
		else:
			print('There are a few commands to learn:\n'
			      '    s, status - Print the location and'
			      ' passengers of the Catbus\n'
			      '       m, map - Print the bus route\n'
			      '      l, left - Move the Catbus one stop to the'
				  ' left\n'
			      '     r, right - Move the Catbus one stop to the'
			      ' right\n'
			      '    p, pickup - Pick up passengers\n'
			      '   d, dropoff - Drop off passengers')
		
		if len(catbus['passengers']) > CATPACITY:
			# TODO: What should the behaviour be?
			pass

		if game_is_finished(catbus['passengers']):
			# TODO: A better victory celebration.
			print('You win!')
			return