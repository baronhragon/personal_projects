import curses
from collision import Player

def main(stdscr):
	filename='map.txt'
	y,x=stdscr.getmaxyx()
	curses.curs_set(False)

	def objects(chr):
		y,x=stdscr.getmaxyx()
		list=[]
		for i in range(0,y+1):
			for j in range(0,x+1):
				c=stdscr.inch(i,j)
				if c == ord(chr):
					list.append((i,j))
		return list


	with open(filename) as file:
		map=file.readlines()

	map=map[:-1]

	for line in map:
		stdscr.addstr(line)

	walls=objects('#')
	windows=objects('o')
	doors=objects('+')

	player=Player(2,2,stdscr,walls)
	player.display()
	c=stdscr.getch()

	while c != ord('q'):
		stdscr.clear()
		for line in map:
			stdscr.addstr(line)
		walls=objects('#')
		windows=objects('o')
		doors=objects('+')
		player.move(c)
		player.display()

		c=stdscr.getch()

class Door():

	def __init__(self,y,x):
		self.y=y
		self.x=x
		self.open=False

	def open_close(self):
		self.open=not self.open

curses.wrapper(main)
