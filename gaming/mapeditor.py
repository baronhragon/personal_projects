import curses

def main(stdscr):
	curses.curs_set(False)
	curses.init_pair(1,curses.COLOR_YELLOW,curses.COLOR_BLACK)
	y,x=stdscr.getmaxyx()
	cursor=Cursor(int(y/2),int(x/2),stdscr)
	coords=[]
	objects={'wall':'#','window':'o','door':'+','erase':'.'}
	menu=Menu(4,20,objects,stdscr)
	for i in range(y):
		for j in range(x-2):
			coords.append((i,j))
	chars=['.' for x in range(len(coords))]
	stdscr.addstr(int(y/2),int(x/2),'WELCOME',curses.color_pair(1))
	menu.display(' ')
	c=stdscr.getch()
	curses.curs_set(True)
	while c != ord('q'):
		stdscr.clear()
		stdscr.move(int(y/2),int(x/2))
		if c==259 and cursor.y>0:
			if menu.options > 0 and menu.toggle:
				menu.options-=1
			else:
				cursor.y-=1
		elif c==258 and cursor.y<y-1:
			if menu.options < len(menu.list)-1 and menu.toggle:
				menu.options+=1
			else:
				cursor.y+=1
		elif c==260 and cursor.x>0 and menu.toggle==False:
			cursor.x-=1
		elif c==261 and cursor.x<x-2 and menu.toggle==False:
			cursor.x+=1
		elif c == ord('m'):
			menu.toggle=not menu.toggle
		elif c == 10:
			chars[coords.index((cursor.y,cursor.x))]=menu.return_char()
		for idx,coord in enumerate(coords):
			stdscr.addstr(coord[0],coord[1],chars[idx],curses.color_pair(1))
		stdscr.refresh()
		filename=menu.display(c)
		payload=parse_char(chars,y,x)
		if filename:
			with open(str(filename),'w') as file:
				file.write(payload)
		stdscr.move(cursor.y,cursor.x)
		c=stdscr.getch()

class Cursor():

	def __init__(self,y,x,stdscr):
		self.y=y
		self.x=x
		self.stdscr=stdscr

class Menu():

	def __init__(self,y,x,list,stdscr):
		self.y=y
		self.x=x
		self.list=list
		self.pad=curses.newpad(self.y,self.x)
		self.stdscr=stdscr
		self.toggle=False
		self.options=0

	def display(self,key):
		y,x=self.stdscr.getmaxyx()
		name=''
		if self.toggle:
			op=list(self.list.keys())
			self.pad.clear()
			for idx,item in enumerate(op):
				if op.index(item) < len(self.list.keys())-2:
					self.pad.addstr(idx,0,item)
				else:
					self.pad.addstr(idx,0,item)
			self.pad.addstr(self.options,0,op[self.options],curses.A_REVERSE)
			self.pad.refresh(0,0,0,0,y-1,x-1)
		elif key== ord('s') and self.toggle==False:
			curses.echo(True)
			self.pad.addstr(0,0,'name of file: ')
			self.pad.move(1,0)
			self.pad.refresh(0,0,0,0,y-1,x-1)
			filename=[]
			f=self.pad.getch()
			self.pad.clear()
			while f != 10:
				self.pad.clear()
				filename.append(chr(f))
				name=''.join(filename)
				self.pad.addstr(1,0,name)
				self.pad.refresh(0,0,0,0,y-1,x-1)
				self.pad.clear()
				f=self.pad.getch()
		self.pad.clear()
		self.stdscr.refresh()
		return name

	def return_char(self):
		return self.list[list(self.list.keys())[self.options]]

def parse_char(char_list,y,x):
	string=''
	counter=0
	for i in range(y-1):
		string+='\n'
		for j in range(x-2):
			if char_list[counter]=='.':
				string+=' '
			else:
				string+=char_list[counter]
			counter+=1
	return string


curses.wrapper(main)
