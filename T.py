import os
import copy
import pygame
import random
import module
import threading

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
WINDOW_SIZE = [800, 550]
winlogo=pygame.image.load(".\winlogo.png")
pygame.display.set_icon(winlogo)
clock = pygame.time.Clock()

font1 = pygame.font.SysFont('freesansbold.ttf', 20)
font2 = pygame.font.SysFont('freesansbold.ttf', 16)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TETRIS")

fps=10
n_r=26
n_c=15

pieces_order=[]
for i in range(10):
	pieces_order.append(random.randint(1,7))

pieces_order2=[]
for i in range(10):
	pieces_order2.append(random.randint(1,7))

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
m2=copy.deepcopy(m)
new_m2=copy.deepcopy(m)

next_block=[]
for n_rows in range(3):
		row_temp=[]
		for n_col in range(3):
			row_temp.append(0)
		next_block.append(row_temp)
next_block_blank=copy.deepcopy(next_block)
next_block2=copy.deepcopy(next_block)
def display(l):
	global fps
	
	#screen.fill(GREY)
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
			pygame.draw.rect(screen,color,[350+(11)*(column),200+(11)*row+MARGIN,10,10])
	clock.tick(fps) 
	pygame.display.flip()

def display2(l):
	global fps

	#screen.fill(GREY)
	#screen.blit(logo,(0,0))
	
	for row in range(0,n_r):
		for column in range(0,n_c):
			color = BLACK
			i=l[row][column]
			if i != 0:
				color=colors[i-1]
			
			pygame.draw.rect(screen,color,[(MARGIN + WIDTH)*(column)+MARGIN+400,(MARGIN + HEIGHT)*row+MARGIN,WIDTH,HEIGHT])
	for row in range(0,3):
		for column in range(0,3):
			color = BLACK
			i=next_block2[row][column]
			if i != 0:
				color=colors[i-1]
			pygame.draw.rect(screen,color,[750+(11)*(column),200+(11)*row+MARGIN,10,10])
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

def preset2(tupl,l,n=1):
	for i in tupl:
		if m2[i[0]][i[1]] == 0:
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

def piece2(point, num, orient,color):
	d=module.new_piece(str(num),point[1],point[0],orient)
	a=preset2(d,new_m2,color)
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
		return False
	c=random.randint(1,len(colors))
	preset(module.new_piece(str(pieces_order[0]),1,1,0),next_block,5)
	while running:
		
		new_m=copy.deepcopy(m)
		p[0]+=1
		
		a = piece(p,num,orient,c)
		if a == -1:
			p[0]-=1
			a=piece(p,num,orient,c)
			m=copy.deepcopy(new_m)
			return True
			break
		display(new_m)
		if p[0]==n_r-1:
			m=copy.deepcopy(new_m)
			return True
			break
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_DOWN]:
			fps=30
		if keystate[pygame.K_UP]:
			orient+=1
			if orient>3:
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

def event2():
	global new_m2,m2,fps, next_block2
	next_block2=copy.deepcopy(next_block_blank)
	orient=0
	fps=10
	num=pieces_order2.pop(0)
	pieces_order2.append(random.randint(1,7))
	running=True
	p=[-1,5]
	if m2[0][5]!=0 or m2[0][6]!=0:
		running=False
		return False
	c=random.randint(1,len(colors))
	preset2(module.new_piece(str(pieces_order2[0]),1,1,0),next_block2,5)
	while running:
		
		new_m2=copy.deepcopy(m2)
		p[0]+=1
		
		a = piece2(p,num,orient,c)
		if a == -1:
			p[0]-=1
			a=piece2(p,num,orient,c)
			m2=copy.deepcopy(new_m2)
			return True
			break
		display2(new_m2)
		if p[0]==n_r-1:
			m2=copy.deepcopy(new_m2)
			return True
			break
		
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_s]:
			fps=30
		if keystate[pygame.K_w]:
			orient+=1
			if orient>3:
				orient-=4
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d and p[1]<n_c-1:
					if new_m2[p[0]+1][p[1]+2]==0:
						p[1]+=1
				if event.key == pygame.K_a and p[1]>0:
					if new_m2[p[0]+1][p[1]-2]==0:
						p[1]-=1


def main():    
	global m, fps
	display(m)
	running=True
	while running:
		a=event1()
		if not(a):
			break
		#Removing perfect Rows
		for i in range(n_r-1):
			if 0 not in m[i]:
				m.pop(i)
				m=[[0]*n_c+[1]]+m

def main2():    
	global m2, fps
	display2(m2)
	running=True
	while running:
		b=event2()
		if not(b):
			break
		#Removing perfect Rows
		for i in range(n_r-1):
			if 0 not in m2[i]:
				m2.pop(i)
				m2=[[0]*n_c+[1]]+m2
'''
if __name__ == "__main__": 
	# creating thread 
	t1 = threading.Thread(target=main) 
	t2 = threading.Thread(target=main2) 
	t1.daemon=True
	t2.daemon=True
	# starting thread 1 
	t1.start() 
	
	# starting thread 2 
	t2.start()
	
	t1.join()
	t2.join()  
	running=True
	while running:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d:
					print('Hello')
	# wait until thread 1 is completely executed 
	
	# wait until thread 2 is completely executed 
	
'''
#main2()
#main()
