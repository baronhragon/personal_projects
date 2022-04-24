# **Program Descriptions**

## _T2ON.py_

This game is inspired by Tron. You operate player1 with WASD and player 2 with the arrow keys. For every loop, each players tail grows, making it difficult to maneuver and avoid the other opponent.

## _cascade.py_

This is just a tech demo of various attributes from curses module for python.

## _game.py_

This is a sample demo of a game that utilizes the curses module. The idea is that the '@' is the player. The "T"s are trees and they spawn randomly in the leftmost quadrant of the playing window. The "M" is a chest which switches to True when the player is near. Trees show their health when player approaches and you can chop trees by pressing 'c' and you can pick up wood by pressing 'p'.You can drop wood in the chest by standing close to it and pressing 'd' or you can place wood on the ground to place a new Tree. You can also pick up wood from chest with 'p'. Player inventory and chest inventory is displayed on the top left hand corner. Arrow keys move the player and 'a' quits the game.

## _lightdark.py_

This program is a common rain simulator program. I made it also in curses and I wanted the rain to change shape as well as color depending on the position of the object at a given moment.

## _chase.py_

The idea behind this program was to create a simple AI from scratch. I wanted to implement collision detection as well as AI. You can place markers on the ground by pressing 'Enter' and the "Zombies" will follow it and if there is no marker on the ground, they will follow the player. You can place walls by pressing 'w'. You quit the game by pressing 'a'.

## _mapeditor.py_

While I was working on making the game, I figured that I needed a faster way of making game maps. That where the idea behind this program came from. At first it welcomes the player and you are presented with a grid of dots. You can place an object at any given position. You can switch between objects by pressing 'm', placing the cursor on the desired object and pressing 'm' again. Once you are finished, you can save the file by pressing 's', giving it a name and pressing enter. Press 'q' to quit.

## _proto.py_

Similar to game.py, it uses the same conventions only that this one pops up a menu when you press 'm'. The idea is to make it scrollable.

## _map.py_

This program imports the map done by the map editor and utilices collisions based on the type of object it encounters. You move the player with WASD and you collide with walls, but not with windows or doors. If you want to edit the current map, create the new map in mapeditor.py and save it as "map.txt". 
