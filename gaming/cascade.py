import curses
import random

def main(stdscr):

	curses.curs_set(False)
	screen_y,screen_x=stdscr.getmaxyx()

	attributes='''A_ALTCHARSET,A_BLINK,A_BOLD,A_DIM,A_INVIS,A_NORMAL,A_PROTECT,A_REVERSE,A_STANDOUT,A_UNDERLINE,A_HORIZONTAL,A_LEFT,A_LOW,A_RIGHT,A_TOP,A_VERTICAL,A_CHARTEXT'''.split(",")

	colors='''COLOR_CYAN,COLOR_BLUE,COLOR_GREEN,COLOR_MAGENTA,COLOR_RED,COLOR_WHITE,COLOR_YELLOW'''.split(",")


	for idx,color in enumerate(colors):
		curses.init_pair(idx+1,eval('curses.%s'%color),curses.COLOR_BLACK)

	for y in range(screen_y):
		for x in range(screen_x-1):

			stdscr.addstr(y,x,chr(random.randint(33,126)),curses.color_pair(random.randint(1,len(colors)))|eval('curses.%s'%random.choice(attributes)))

	stdscr.box()

	stdscr.getch()

curses.wrapper(main)
