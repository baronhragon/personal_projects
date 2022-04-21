
#! /usr/bin/env python3

''' Todo list:

	* Display character on screen (CHECK)
	* Move character on screen with keyboard input (CHECK)
	* Make interactive object for player //Tree// (CHECK)
	* Display tree on screen (CHECK)
	* Randomize tree location (CHECK)
	* Have tree health (CHECK)
	* Make player interact with tree (CHECK)
	* Make tree disappear after health depleted (CHECK)
	* Have player pickup wood (CHECK)
	* Have player store wood in inventory (CHECK)
	* Have chest to store wood (CHECK)
	* Display chest on screen (CHECK)
	* Interact player with chest (CHECK)
	* Have chest and player inventory limit (CHECK)
	* Inventory TUI for chest and player (CHECK)

	===============================================

	Extra credits:

	* Made player place wood on ground to plant new tree
	* Made player pick up wood from chest
	* Had player and chest not go to negative values with player input

 '''

import curses
import random

def main(stdscr):
	curses.curs_set(False)
	lines,cols=stdscr.getmaxyx()
	y_pos= int(lines/2)
	x_pos= int(cols/2)
	player=Player('@',y_pos,x_pos,stdscr)
	chest=Chest(lines,cols,stdscr)
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)

	def forest(list):
		for t in list:
			t.is_player_near((player.y,player.x))
			t.display(lines,cols)

	# Initialize trees array, full of Tree() objects with randomized
	# positions

	trees=[]

	for i in range(10):
		trees.append(Tree(random.randint(0,y_pos-1),
					random.randint(0,x_pos-1),stdscr))


	# Main game loop for input and display of characters on screen

	player.display()
	stdscr.addstr(0,x_pos,f'{player.y}:{lines},{player.x}:{cols}')
	forest(trees)
	chest.display()
	stdscr.refresh()
	c=stdscr.getkey()

	while (c != 'a'):
		stdscr.clear()
		stdscr.refresh()

		if c=='KEY_UP' and player.y > 0:
			player.y-=1
		elif c=='KEY_DOWN' and player.y < lines-1:
			player.y+=1
		elif c == 'KEY_LEFT' and player.x > 0:
			player.x-=1
		elif c=='KEY_RIGHT' and player.x < cols-1:
			player.x+=1
		elif c=='c':
			for t in trees:
				if t.player_near:
					t.health-=1
		elif c=='p':
		# 'p' is used to pickup wood from ground and chest
			if chest.player_near and chest.inventory > 0:
				player.inventory += 1
				chest.inventory -= 1
			else:
				for t in trees:
					if t.player_near and t.health <= 0 and player.inventory >= 5:
						stdscr.addstr(1,x_pos,'Inventory full')
					elif t.player_near and t.health <= 0:
						player.inventory+=1
						stdscr.addstr(1,x_pos,'Player picked up wood')
						trees.remove(t)
					elif t.player_near and t.health > 0:
						stdscr.addstr(1,x_pos,
									'The tree is rooted to the ground dummy!')
		elif c=='d':
		# 'd' is used to drop wood on ground and create tree in player
		# position or to drop wood in chest
			if chest.player_near and player.inventory > 0:
				chest.inventory += 1
				stdscr.addstr(1,x_pos,'Stored wood in chest')
				player.inventory -= 1
			elif chest.player_near and player.inventory == 0:
				stdscr.addstr(1,x_pos,'No wood in inventory')
			elif player.inventory > 0:
				trees.append(Tree(player.y,player.x,stdscr))
				player.inventory -= 1

		# Try block gets around the wrapper function from curses library,
		# it lets the program print to the bottom right edge of the screen,
		# but characters disappear from screen when player is at that position

		try:
			chest.is_player_near((player.y,player.x))
			forest(trees)
			stdscr.addstr(0,0,'Player: %s/%s wood'
						%(player.inventory,player.inventory_limit))
			stdscr.addstr(1,0,'Chest: %s/%s wood'
						%(chest.inventory,chest.inventory_limit))
			chest.display()
			player.display()
			stdscr.addstr(0,x_pos,f'{player.y}:{lines},{player.x}:{cols}')

		except curses.error as e:
			pass

		c=stdscr.getkey()

class Player():

	def __init__(self,char,y,x,stdscr):
		self.char = char
		self.y = y
		self.x = x
		self.stdscr = stdscr
		self.inventory = 0
		self.inventory_limit = 5

	def display(self):
		attributes = curses.A_REVERSE|curses.A_BLINK
		self.stdscr.addstr(self.y,self.x,self.char,attributes)

class Tree():

	def __init__(self,y,x,stdscr):
		self.y = y
		self.x = x
		self.triggers = self.perimeter()
		self.stdscr = stdscr
		self.health = 10
		self.player_near = False

	def display(self,max_y,max_x):
		''' Displays a 'T' for a live tree and a '=' for a fallen tree.'''
		if self.health > 0:
			self.stdscr.addstr(self.y,self.x,'T',curses.color_pair(1))
			if self.player_near:
				if self.y+1 == max_y:
					self.stdscr.addstr(self.y-1,self.x,str(self.health))
				elif self.x+len(str(self.health))>= max_x:
					self.stdscr.addstr(self.y+1,self.x-len(str(self.health)),
								str(self.health))
				else:
					self.stdscr.addstr(self.y+1,self.x,str(self.health))
		else:
			self.stdscr.addstr(self.y,self.x,'=',curses.color_pair(1))

	def perimeter(self):
		''' Creates a perimeter around tree that triggers display of health
			if player is near.'''
		ls=[]
		for y in range(self.y-1,self.y+2):
			for x in range(self.x-1,self.x+2):
				ls.append((y,x))
		return ls


	def is_player_near(self,player_coords):
		''' Checks whether player is near tree and switches player_near flag
			on or off.'''
		if player_coords in self.triggers:
			self.player_near = True
		else:
			self.player_near = False

class Chest():
	def __init__(self,lines,cols,stdscr):
		self.y = int(lines/2) + 10
		self.x = int(cols/2) + 10
		self.stdscr = stdscr
		self.inventory = 0
		self.inventory_limit = 10
		self.triggers = self.perimeter()
		self.player_near = False

	def display(self):
		self.stdscr.addstr(self.y+2,self.x,str(self.player_near))
		self.stdscr.addstr(self.y,self.x,'M')

	def perimeter(self):
		ls=[]
		for y in range(self.y-1,self.y+2):
			for x in range(self.x-1,self.x+2):
				ls.append((y,x))
		return ls

	def is_player_near(self,player_coords):
		if player_coords in self.triggers:
			self.player_near = True
		else:
			self.player_near = False

curses.wrapper(main)
