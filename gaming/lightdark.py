import curses
import random

def main(stdscr):

	curses.curs_set(False)
	screen_y,screen_x=stdscr.getmaxyx()
	stdscr.nodelay(True)

	attributes='''A_DIM,A_NORMAL,A_BOLD'''.split(",")
	colors='''COLOR_CYAN,COLOR_BLUE,COLOR_GREEN,COLOR_RED,COLOR_MAGENTA,COLOR_RED,COLOR_YELLOW'''.split(",")

	top=int(screen_y/3)
	middle=int(screen_y/3)*2
	bottom=screen_y


	for idx, color in enumerate(colors):
		curses.init_pair(idx+1,eval('curses.%s'%color),curses.COLOR_BLACK)

	c=stdscr.getch()

	drops=[Drop(0,random.randint(0,screen_x-1),stdscr,top,middle,bottom,random.randint(1,4)) for i in range(15)] 

	while c != ord('a'):

		stdscr.clear()
		for drop in drops:
			try:
				drop.display(attributes,screen_x,screen_y)
			except curses.error as e:
				pass
		stdscr.refresh()
		stdscr.getch()



class Drop():

	def __init__(self,y,x,stdscr,top,middle,bottom,speed):
		self.x=x
		self.y=y
		self.stdscr=stdscr
		self.top=top
		self.middle=middle
		self.bottom=bottom
		self.speed=speed

	def display(self,attributes,screen_x,screen_y):
		if self.y <= self.top:
			self.stdscr.addstr(self.y,self.x,'.',curses.color_pair(1)|eval('curses.%s'%attributes[0]))
		elif self.y > self.top and self.y <= self.middle:
			self.stdscr.addstr(self.y,self.x,'|',curses.color_pair(1))
		elif self.y > self.middle and self.y <= self.bottom:
			self.stdscr.addstr(self.y,self.x,'*',curses.color_pair(1)|eval('curses.%s'%attributes[2]))
		self.y+=self.speed

		if self.y >= screen_y:
			self.y=0
			self.x=random.randint(0,screen_x-1)
		curses.napms(5)

curses.wrapper(main)
