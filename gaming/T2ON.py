#! /usr/bin/env python3

#Move a worm across the screen. Beware of borders and self!

import pygame
import random
import time

class Worm:
	"""A worm"""

	def __init__(self,surface,x,y,length,message):
		self.surface=surface
		self.x=x
		self.y=y
		self.length=length
		self.dir_x=0
		self.dir_y=-1
		self.body=[]
		self.crashed=False
		self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		self.message=message
	def key_event(self,event):
		"""Handle key events that affect the worm"""

		if event.key==pygame.K_UP:
			self.dir_x=0
			self.dir_y=-1
		elif event.key==pygame.K_DOWN:
			self.dir_x=0
			self.dir_y=1
		elif event.key==pygame.K_LEFT:
			self.dir_x=-1
			self.dir_y=0
		elif event.key==pygame.K_RIGHT:
			self.dir_x=1
			self.dir_y=0

	def move(self,other):
		"""Move the worm"""

		self.x+=self.dir_x
		self.y+=self.dir_y

		if (self.x,self.y) in other.body or (self.x,self.y) in self.body:
			self.crashed=True

		self.body.insert(0,(self.x,self.y))

		if len(self.body) > self.length:
			self.body.pop()

	def draw(self):
		counter=0
		for x,y in self.body:
			if counter<2:
				self.surface.set_at((int(x),int(y)),(255,255,255))
			else:
				self.surface.set_at((int(x),int(y)),self.color)
			counter+=1

	def gameover(self):
		print(self.message)
#Dimensions

width=640
height=400

screen=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
running=True

#Our worm

growrate=100
snakes=[Worm(screen,width/4,height/2,100,'PLAYER TWO WINS!'),Worm(screen,width*0.75,height/2,100,'PLAYER ONE WINS!')]

#Music track


time.sleep(3)

pygame.init()

pygame.mixer.music.load("scifi.ogg")

pygame.mixer.music.play(-1)

while running:

	screen.fill((0,0,0))
	snakes[0].move(snakes[1])
	snakes[0].draw()
	snakes[1].move(snakes[0])
	snakes[1].draw()

	for snake in snakes:
		if snake.crashed:
			print('Crash!')
			snake.gameover()
			time.sleep(3)
			running=False
		if snake.x <0:
			snake.x=width-1
		elif snake.x>width-1:
			snake.x=0
		elif snake.y<0:
			snake.y=height-1
		elif snake.y>height-1:
			snake.y=0
		if growrate==0:
			snake.length+=20
			
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
			pygame.quit()
		elif event.type==pygame.KEYDOWN:
			if event.key==pygame.K_w and snakes[0].dir_y!=1:
				snakes[0].dir_x=0
				snakes[0].dir_y=-1
			elif event.key==pygame.K_s and snakes[0].dir_y!=-1:
				snakes[0].dir_x=0
				snakes[0].dir_y=1
			elif event.key==pygame.K_a and snakes[0].dir_x!=1:
				snakes[0].dir_x=-1
				snakes[0].dir_y=0
			elif event.key==pygame.K_d and snakes[0].dir_x!=-1:
				snakes[0].dir_x=1
				snakes[0].dir_y=0
			elif event.key==pygame.K_UP and snakes[1].dir_y!=1:
				snakes[1].dir_x=0
				snakes[1].dir_y=-1
			elif event.key==pygame.K_DOWN and snakes[1].dir_y!=-1:
				snakes[1].dir_x=0
				snakes[1].dir_y=1
			elif event.key==pygame.K_LEFT and snakes[1].dir_x!=1:
				snakes[1].dir_x=-1
				snakes[1].dir_y=0
			elif event.key==pygame.K_RIGHT and snakes[1].dir_x!=-1:
				snakes[1].dir_x=1
				snakes[1].dir_y=0
	if growrate==0:
		growrate=100
	pygame.display.flip()
	clock.tick(100)
	growrate-=1
