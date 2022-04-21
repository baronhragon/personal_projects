#! /usr/bin/env python3

import pygame
import random
import time

class Worm:

	def __init__(self,surface):

		self.surface=surface
		self.x=surface.get_width()/2
		self.y=surface.get_height()/2
		self.length=1
		self.grow_to=50
		self.vx=0
		self.vy=-1
		self.body=[]
		self.crashed=False
		self.color=255,255,0

	def event(self,event):

		"""Handle keyboard events"""

		if event.key==pygame.K_UP:
			self.vx=0
			self.vy=-1

		elif event.key==pygame.K_DOWN:
			self.vx=0
			self.vy=1

		elif event.key==pygame.K_LEFT:
			self.vx=-1
			self.vy=0

		elif event.key==pygame.K_RIGHT:
			self.vx=1
			self.vy=0

	def move(self):

		"""Move the worm"""

		self.x+= self.vx
		self.y+= self.vy

		if (self.x,self.y) in self.body:
			self.crashed=True

		self.body.insert(0,(self.x,self.y))

		if (self.grow_to > self.length):
			self.length +=1

		if len(self.body) > self.length:
			self.body.pop()

	def draw(self):

		for x,y in self.body:
			self.surface.set_at((int(x),int(y)),self.color)

	def position(self):

		return self.x,self.y

	def eat(self):

		self.grow_to+=25


class Food:

	def __init__(self,surface):
		self.surface=surface
		self.x=random.randint(0,surface.get_width())
		self.y=random.randint(0,surface.get_height())
		self.color=255,255,255

	def draw(self):
		pygame.draw.line(self.surface,self.color,(self.x,self.y),(self.x,self.y+20))

	def position(self):
		pos=[]
		for y in range(20):
			pos.append((self.x,self.y+y))
		return pos


w=500
h=500

screen=pygame.display.set_mode((w,h))
clock=pygame.time.Clock()

score=0
worm=Worm(screen)
food=Food(screen)
running=True

while running:

	def tryagain():
		option=input('Do you want to play again?')
		if option=='yes':
			worm=Worm(screen)
			food=Food(screen)
			score=0
			running=True
			time.sleep(3)
			return worm,food,score,running
		else:
			running=False



	screen.fill((0,0,0))
	worm.move()
	worm.draw()
	food.draw()

	if worm.crashed:
		print('Crashed!')
		tryagain()
	elif worm.x <=0 or worm.x >= w-1:
		print('Crashed!')
		tryagain()
	elif worm.y <=0 or worm.y >= h-1:
		print('Crashed!')
		tryagain()
	for p in food.position():
		if worm.position()==p:
			score+=1
			worm.eat()
			print('Score %d'%score)
			food=Food(screen)

	for event in pygame.event.get():

		if event.type==pygame.QUIT:
			running=False
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_SPACE:
				input()
				time.sleep(3)
			else:
				worm.event(event)

	pygame.display.flip()
	clock.tick(240)


