import curses

def main(stdscr):
	curses.curs_set(False)
	y,x=stdscr.getmaxyx()
	pad=curses.newpad(int(y/2),int(x/4))
	pady,padx=pad.getmaxyx()
	menu=Menu(pad,pady,padx,stdscr,y,x)
	menu.display('something')
	word='hello world'
	pad.addstr(int(pady/2),int(padx/2)-int(len(word)/2),word)
	with open('test.txt') as file:
		content=[]
		for line in file.readlines():
			if len(content)-1 < y-3:
				if len(line) > int(x/2)-3:
					content.append(line[:int(x/2)-3])
				else:
					content.append(line)
	stdscr.bkgd('.')
	stdscr.refresh()
	pad.refresh(0,0,int(y/2),0,y-1,x-1)
	c=pad.getch()
	pad.clear()
	menu.toggle=False
	while c != ord('a'):
		if c== 66 and menu.slider < pady-7:
			menu.slider+=1
		elif c==65 and menu.slider > 2:
			menu.slider-=1
		elif c == ord('m'):
			menu.toggle=not menu.toggle
		menu.display('Humberto Aragon Meza',content)
		c=pad.getch()

class Menu():

	def __init__(self,pad,y,x,stdscr,windowy,windowx):
		self.pad=pad
		self.y=y
		self.x=x
		self.slider=2
		self.stdscr=stdscr
		self.windowy=windowy
		self.windowx=windowx
		self.toggle=False

	def display(self,text,content=''):
		if self.toggle:
			self.pad.addstr(3,3,'   '.join(content))
			self.pad.box()
			self.pad.addstr(0,4,f'< {text} >')
			self.pad.addch(1,0,'^')
			self.pad.addch(self.y-2,0,'v')
			for i in range(5):
				self.pad.addch(self.slider+i,0,curses.ACS_CKBOARD,curses.A_BOLD)
			self.pad.refresh(0,0,int(self.windowy/2),0,self.windowy-1,self.windowx-1)
		else:
			self.slider=2
			self.pad.clear()
			# Comment these lines out for use in other modules
#			self.stdscr.bkgd('.')
#			self.stdscr.refresh()

if __name__ == '__main__':

	curses.wrapper(main)
