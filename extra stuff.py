import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 10
GAME_HEIGHT = 10

#### Put class definitions here ####
class Rock(GameElement):
	IMAGE = "Rock"
	SOLID = True

class Key(GameElement):
	IMAGE = "Key"
	SOLID = False

	def  interact(self, player):
		PLAYER.inventory.append(self)
		GAME_BOARD.draw_msg("You just acquired a key! Go Save the Princess! but don't forget about the heart!")

class Princess(GameElement):
	IMAGE = "Princess"
	SOLID = True

class DoorClosed(GameElement):
	IMAGE = "DoorClosed"
	SOLID = False

	def  interact(self, player):
		PLAYER.inventory.append(self)
		GAME_BOARD.draw_msg("You Got the Princess! Rock On!")

class DoorOpen(GameElement):
	IMAGE = "DoorOpen"

class Wall(GameElement):
	IMAGE = "Wall"
	SOLID = True
		
class Heart(GameElement):
	IMAGE = "Heart"

	def  interact(self, player):
		PLAYER.inventory.append(self)
		GAME_BOARD.draw_msg("You Ready to Save the Princess!")
	
class Horns(GameElement):
	IMAGE = "Horns"	
	SOLID = True

	def __init__(self):
		GameElement.__init__(self)
		self.last_move = 0
		self.velocity_x = 1
				
	def update(self, dt):
		self.last_move += dt
		if self.last_move > 0.30:
			#self.last_move = 0
			self.board.del_el(self.x, self.y)
			self.x += self.velocity_x
			self.board.set_el(self.x, self.y, self)
			if self.x == 9:
				self.velocity_x = -1
				self.board.del_el(self.x, self.y)
				self.x += self.velocity_x
				self.board.set_el(self.x, self.y, self)
			elif self.x == 0:
				self.velocity_x = 1
				self.board.del_el(self.x, self.y)
				self.x += self.velocity_x
				self.board.set_el(self.x, self.y, self)
				
class Girl(GameElement):
	IMAGE = "Girl"	
	SOLID = True

	def __init__(self):
		GameElement.__init__(self)
		self.last_move = 0
		self.velocity_y = 1
				
	def update(self, dt):
		self.last_move += dt
		if self.last_move > 0.30:
			#self.last_move = 0
			self.board.del_el(self.x, self.y)
			self.y += self.velocity_y
			self.board.set_el(self.x, self.y, self)
			if self.y == 9:
				self.velocity_y = -1
				self.board.del_el(self.x, self.y)
				self.y += self.velocity_y
				self.board.set_el(self.x, self.y, self)
			elif self.y == 0:
				self.velocity_y = 1
				self.board.del_el(self.x, self.y)
				self.x += self.velocity_y
				self.board.set_el(self.x, self.y, self)

class TallTrees(GameElement):
	IMAGE = "TallTree"
	SOLID = True

class ShortTrees(GameElement):
	IMAGE = "ShortTree"

class Character(GameElement):
	IMAGE = "Boy"

	def __init__(self):
		GameElement.__init__(self)
		self.inventory = []
		
	def next_pos(self, direction):
		if direction == "UP":
			return (self.x, self.y-1)
		elif direction == "DOWN":
			return (self.x, self.y+1)
		elif direction == "LEFT":
			return (self.x-1, self.y)
		elif direction == "RIGHT":
			return (self.x+1, self.y)
		return None
		
####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    rock_positions = [
    (1,7),
    (2,7),
    (5,6),
    (4,5),
    (2,4),
    (7,4),
    (8,4),
    (4,2),
    (2,1)
    ]
    rocks = []

    for pos in rock_positions:
    	rock = Rock()
    	GAME_BOARD.register(rock)
    	GAME_BOARD.set_el(pos[0], pos[1], rock)
    	rocks.append(rock)

    # rocks[-1].SOLID = False

    for rock in rocks:
    	print rock


	tall_trees_pos = [
    (8,8),
    (3,5),
    (1,2)
    ]

 	big = []

    for pos in tall_trees_pos:
    	tall = TallTrees()
    	GAME_BOARD.register(tall)
    	GAME_BOARD.set_el(pos[0], pos[1], tall)
    	big.append(tall)

    for tall in big:
    	print tall

    short_trees_pos = [
    (3,8),
    (7,6),
    (7,5),
    (5,1)
    ]

    small = []

    for pos in short_trees_pos:
    	short = ShortTrees()
    	GAME_BOARD.register(short)
    	GAME_BOARD.set_el(pos[0], pos[1], short)
    	small.append(short)

    for short in small:
    	print short

   	global PLAYER
   	PLAYER = Character()
   	GAME_BOARD.register(PLAYER)
   	GAME_BOARD.set_el(1,8, PLAYER)
   	print PLAYER

   	GAME_BOARD.draw_msg("Collect the key to conquer the heart of the Princess! Watch out for the Girl with Horns!")

   	key = Key()
   	GAME_BOARD.register(key)
   	GAME_BOARD.set_el(8,5, key)

   	princess = Princess()
   	GAME_BOARD.register(princess)
   	GAME_BOARD.set_el(8, 1, princess)

   	door_closed = DoorClosed()
   	GAME_BOARD.register(door_closed)
   	GAME_BOARD.set_el(7,1, door_closed)

   	wall = Wall()
   	GAME_BOARD.register(wall)
   	GAME_BOARD.set_el(8,2,wall)

   	heart = Heart()
   	GAME_BOARD.register(heart)
   	GAME_BOARD.set_el(3,1, heart)

   	
# '''
#    	horns_positions = [
#     (1,3),
#     (2,3),
#     (3,3),
#     (4,3),
#     (5,3),
#     (6,3),
#     (7,3),
#     (8,3)
#     ]
    
#     evil_girl = []

#     for pos in horns_positions:
#     	horns_girl = Horns()
#     	GAME_BOARD.register(horns_girl)
#     	GAME_BOARD.set_el(pos[0], pos[1], horns_girl)
#     	evil_girl.append(horns_girl)

#     # while True:
#     # 	for horns_girl in evil_girl:
#     # 		print horns_girl
# '''

	horns_girl = Horns()
    GAME_BOARD.register(horns_girl)
    GAME_BOARD.set_el(1, 3, horns_girl)

    pink_girl = Girl()
    GAME_BOARD.register(pink_girl)
    GAME_BOARD.set_el(6, 1, pink_girl)

def keyboard_handler():
	direction = None

	if KEYBOARD[key.UP]:
		direction = "UP"
	elif KEYBOARD[key.DOWN]:
		direction = "DOWN"
	elif KEYBOARD[key.LEFT]:
		direction = "LEFT"
	elif KEYBOARD[key.RIGHT]:
		direction = "RIGHT"

	if direction:
		next_location = PLAYER.next_pos(direction)
		next_x = next_location[0]
		next_y = next_location[1]

		existing_el = GAME_BOARD.get_el(next_x, next_y)

		if existing_el:
			existing_el.interact(PLAYER)

		if existing_el is None or not existing_el.SOLID:
			GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
			GAME_BOARD.set_el(next_x, next_y, PLAYER)


