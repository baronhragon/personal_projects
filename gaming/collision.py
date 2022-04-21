import curses

def main(stdscr):
    curses.curs_set(False)
    y, x = stdscr.getmaxyx()
    walls = square(0, 20, 0, 20)
    player_y = int(y / 2)
    player_x = int(x / 2)
    player = Player(player_y, player_x, stdscr, walls)
    c = stdscr.getch()
    while c != ord('x'):
        if c == ord('w') and (player.y - 1, player.x) not in player.collides():
            player.y -= 1
        else:
            if c == ord('s') and (player.y + 1, player.x) not in player.collides():
                player.y += 1
            elif c == ord('a') and (player.y, player.x - 1) not in player.collides():
                player.x -= 1
            elif c == ord('d') and (player.y, player.x + 1) not in player.collides():
                player.x += 1
            elif c == ord('h'):
                walls.remove(player.collides()[1])
            for wall in walls:
                stdscr.addstr(wall[0], wall[1], '%')

        player.display()
        c = stdscr.getch()
        stdscr.clear()


class Player:

    def __init__(self, y, x, stdscr, walls):
        self.y = y
        self.x = x
        self.stdscr = stdscr
        self.walls = walls
        self.debug = False

    def display(self):
        if self.debug:
            for space in self.perimeter():
                self.stdscr.addstr(space[0], space[1], '%', curses.A_DIM)

            for thing in self.collides():
                self.stdscr.addstr(thing[0], thing[1], '!', curses.A_BOLD)

            self.stdscr.addstr(str(self.collides()))
        self.stdscr.addstr(self.y, self.x, '@', curses.A_BOLD)
        self.stdscr.refresh()

    def perimeter(self):
        ls = []
        for i in range(self.y - 1, self.y + 2):
            for j in range(self.x - 1, self.x + 2):
                ls.append((i, j))
        return ls

    def collides(self):
        list = []
        for area in self.perimeter():
            if area in self.walls:
                list.append(area)

        return list

    def move(self, key):
        if key == ord('w') and (self.y - 1, self.x) not in self.collides():
            self.y -= 1
        elif key == ord('s') and (self.y + 1, self.x) not in self.collides():
            self.y += 1
        elif key == ord('a') and (self.y, self.x - 1) not in self.collides():
            self.x -= 1
        elif key == ord('d') and (self.y, self.x + 1) not in self.collides():
            self.x += 1


def square(starty, stopy, startx, stopx):
    list = []
    for i in range(starty, stopy):
        for j in range(startx, stopx):
            if i == starty or i == stopy - 1 or j == startx or j == stopx - 1:
                list.append((i, j))

    return list


if __name__ == '__main__':
    curses.wrapper(main)
# okay decompiling collision.pyc
