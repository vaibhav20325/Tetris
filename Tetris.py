import os
import copy
import pygame
import random
import module
BLACK = (0, 0, 0)
GREY=(20,20,20)
WHITE = (255, 255, 255)
BLUE=(0,255,255)
GREEN=(43,236,69)
RED=(255,0,0)
YELLOW=(255,255,0)
ORANGE=(255,114,6)
colors=[WHITE,BLUE,GREEN,RED,YELLOW,ORANGE]
WIDTH = 20
HEIGHT = 20
MARGIN = 2

pygame.init()
WINDOW_SIZE = [340, 530]
winlogo=pygame.image.load(".\winlogo.png")
pygame.display.set_icon(winlogo)
clock = pygame.time.Clock()

font1 = pygame.font.SysFont('freesansbold.ttf', 20)
font2 = pygame.font.SysFont('freesansbold.ttf', 16)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TETRIS")

fps=10
n_r=25
n_c=12

pieces_order=[]
for i in range(10):
	pieces_order.append(random.randint(1,7))

m=[]

for n_rows in range(n_r-1):
		row_temp=[]
		for n_col in range(n_c):
			row_temp.append(0)
		row_temp.append(1)
		m.append(row_temp)
m.append([1]*(n_c+1))

new_m=[]
new_m=copy.deepcopy(m)


next_block=[]
for n_rows in range(3):
		row_temp=[]
		for n_col in range(3):
			row_temp.append(0)
		next_block.append(row_temp)
next_block_blank=copy.deepcopy(next_block)

def display(l):
	global fps
	screen.fill(GREY)
	#screen.blit(logo,(0,0))
	
	for row in range(0,n_r):
		for column in range(0,n_c):
			color = BLACK
			i=l[row][column]
			if i != 0:
				color=colors[i-1]
			pygame.draw.rect(screen,color,[(MARGIN + WIDTH)*(column)+MARGIN,(MARGIN + HEIGHT)*row+MARGIN,WIDTH,HEIGHT])
	for row in range(0,3):
		for column in range(0,3):
			color = BLACK
			i=next_block[row][column]
			if i != 0:
				color=colors[i-1]
			pygame.draw.rect(screen,color,[270+(11)*(column),200+(11)*row+MARGIN,10,10])
	clock.tick(fps) 
	pygame.display.flip()


def preset(tupl,l,n=1):
	for i in tupl:
		if m[i[0]][i[1]] == 0:
			continue
		else:
			return (-1)
	for i in tupl:
		l[i[0]][i[1]]=n
					
def piece(point, num, orient,color):
	d=module.new_piece(str(num),point[1],point[0],orient)
	a=preset(d,new_m,color)
	if a == -1:
		return -1

def event1():
	global new_m,m,fps, next_block
	next_block=copy.deepcopy(next_block_blank)
	orient=0
	fps=10
	num=pieces_order.pop(0)
	pieces_order.append(random.randint(1,7))
	running=True
	p=[-1,5]
	if m[0][5]!=0 or m[0][6]!=0:
		running=False
	c=random.randint(1,len(colors))
	preset(module.new_piece(str(pieces_order[0]),1,1),next_block,5)
	while running:
		
		new_m=copy.deepcopy(m)
		p[0]+=1
		
		a = piece(p,num,orient,c)
		if a == -1:
			p[0]-=1
			a=piece(p,num,0,c)
			m=copy.deepcopy(new_m)
			break
		display(new_m)
		if p[0]==n_r-1:
			m=copy.deepcopy(new_m)
			break
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_DOWN]:
			fps=30
		if keystate[pygame.K_UP]:
			oreint+=1
			if oreint>3:
				orient-=4
		'''
		if keystate[pygame.K_RIGHT] and p[1]<n_c-1:
			if new_m[p[0]+1][p[1]+2]==0:
				p[1]+=1
		if keystate[pygame.K_LEFT] and p[1]>0:
			if new_m[p[0]+1][p[1]-2]==0:
				p[1]-=1

		'''
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT and p[1]<n_c-1:
					if new_m[p[0]+1][p[1]+2]==0:
						p[1]+=1
				if event.key == pygame.K_LEFT and p[1]>0:
					if new_m[p[0]+1][p[1]-2]==0:
						p[1]-=1



def main():    
	global m, fps
	display(m)
	running=True
	while running:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
				quit()
		event1()
main()

