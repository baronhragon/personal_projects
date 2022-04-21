import curses
import random

def main(stdscr):

	curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
	UP_ARROW=259
	DOWN_ARROW=258
	LEFT_ARROW=260
	RIGHT_ARROW=261
	ENTER=10
	SPACE=32
	walls=square(0,25,25,55)
	markers=[]
	y,x=stdscr.getmaxyx()
#	curs_y,curs_x=(int(y/2),int(x/2))
	curs_y,curs_x=(0,0)
	zombies=[]
	for i in range(5):
		zombies.append(Zombie(random.randint(0,int(y/2)),int(x/2)+i,stdscr,markers,walls))
	for zombie in zombies:
		zombie.display()
	c=stdscr.getch()
	while c != ord('a'):
		stdscr.clear()
		if c == DOWN_ARROW:
			curs_y+=1
		elif c == UP_ARROW:
			curs_y-=1
		elif c == LEFT_ARROW:
			curs_x-=1
		elif c == RIGHT_ARROW:
			curs_x+=1
		elif c == ENTER:
			markers.append((curs_y,curs_x))
		elif c == ord('w'):
			walls.append((curs_y,curs_x))
		for marker in markers:
			stdscr.addch(marker[0],marker[1],'x',curses.A_BOLD|curses.A_BLINK)
		for wall in walls:
			stdscr.addch(wall[0],wall[1],'#',curses.A_BOLD)
		for zombie in zombies:
			zombie.display()
			zombie.move(walls=walls,target=[(curs_y,curs_x)])
			if zombie.captured():
				markers.pop(0)
		stdscr.move(0,0)
		stdscr.move(curs_y,curs_x)
		stdscr.refresh()

		c=stdscr.getch()

class Zombie:

	def __init__(self,y,x,stdscr,markers,walls):
		self.y=y
		self.x=x
		self.stdscr=stdscr
		self.char='Z'
		self.markers=markers
		self.walls=walls

	def display(self):
		self.stdscr.addstr(self.y,self.x,self.char,curses.A_BOLD|curses.color_pair(1))
		self.stdscr.addstr(self.y+1,self.x,str(self.chase_mode(self.markers)))

	def chase_mode(self,target):
		if target != []:
			return True
		else:
			return False

	def move(self,walls,target=None):
		if target == None or self.markers != []:
			target=self.markers
		else:
			target=target
		if self.chase_mode(target):
			if self.y != target[0][0]:
				distance=target[0][0]-self.y
				if distance < 0 and (self.y-1,self.x) not in self.collides():
					self.y+=-1
				elif distance > 0 and (self.y+1,self.x) not in self.collides():
					self.y+=1
			if self.x != target[0][1]:
				distance=target[0][1]-self.x
				if distance < 0 and (self.y,self.x-1) not in self.collides():
					self.x+=-1
				elif distance > 0 and (self.y,self.x+1) not in self.collides():
					self.x+= 1

	def captured(self):
		if self.markers ==[]:
			return False
		else:
			return (self.y,self.x)==self.markers[0]

	def perimeter(self):
		''' Creates a perimeter around zombie that triggers a flag when
		a wall is near.'''
		ls=[]
		for y in range(self.y-1,self.y+2):
			for x in range(self.x-1,self.x+2):
				ls.append((y,x))
		return ls

	def collides(self):
		list=[]
		for area in self.perimeter():
			if area in self.walls:
				list.append(area)
		return list

def square(starty,stopy,startx,stopx):
	list=[]
	for i in range(starty,stopy):
		for j in range(startx,stopx):
			if (i==starty or i==stopy-1 or j==startx or j==stopx-1):
				list.append((i,j))
			else:
				pass
	return list

curses.wrapper(main)


