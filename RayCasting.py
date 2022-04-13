import pygame
import numpy as np 
from math import sqrt
from os import path
from time import sleep
pygame.mixer.init()
WIDTH,HEIGHT=1200,600
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ray Casting")
WHITE=(255,255,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
SKYBLUE=(100,100,255)
GRAY=(130,130,130)
DARKGRAY=(80,80,80)
GREEN=(0,255,0)
global px,py,pdx,pdy,rot
global vx,vy,hx,hy,vxo,vyo,hxo,hyo,rx,ry 
px,py=25,25
rot=np.pi/4
FPS=36

maze=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1,0,0,0,0,0,0,1],
	  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

global size,stat,posy,jumpstat,squatstat
squatstat=False
jumpstat=False
posy=400
size=600/len(maze)
print(len(maze))
print(len(maze[0]))
stat=False
GUN1=pygame.image.load(path.join('gun.png'))
GUN=pygame.transform.scale(GUN1,(250,300))
GUN_FIRE=[pygame.transform.scale(pygame.image.load(path.join('Gun','1.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','2.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','3.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','4.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','5.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','6.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','7.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','8.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','9.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','10.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','11.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','12.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','13.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','14.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','15.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','16.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','17.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','18.png')),(225,225)),
		  pygame.transform.scale(pygame.image.load(path.join('Gun','19.png')),(225,225)),]
SKY=pygame.transform.scale(pygame.image.load(path.join('sky.png')),(600,600))
FLOOR=pygame.transform.scale(pygame.image.load(path.join('floor.png')),(600,600))
SOUND=pygame.mixer.Sound('sound.mp3')
def draw():
	global px,py,pdx,pdy,rot,color,tvx,tvy,thx,thy,stat,posy,jumpstat,squatstat
	global vx,vy,hx,hy,vxo,vyo,hxo,hyo,rx,ry 
	pdx=np.cos(rot)*3
	pdy=np.sin(rot)*3
	pygame.draw.rect(WIN,GRAY,pygame.Rect(0,0,1200,600))
	x,y=pygame.mouse.get_pos()
	scale=((y-300)/300.0)*200.0
	WIN.blit(SKY,(600,0))
	WIN.blit(FLOOR,(600,300-scale))
	for i in range(len(maze)):
		for j in range(len(maze[i])):
			if maze[i][j]==1:
				pygame.draw.rect(WIN,WHITE,pygame.Rect(j*size,i*size,size-1,size-1))
			elif maze[i][j]==0:
				pygame.draw.rect(WIN,BLACK,pygame.Rect(j*size,i*size,size-1,size-1))
			elif maze[i][j]==2:
				pygame.draw.rect(WIN,BLUE,pygame.Rect(j*size,i*size,size-1,size-1))
			elif maze[i][j]==3:
				pygame.draw.rect(WIN,RED,pygame.Rect(j*size,i*size,size-1,size-1))
	cast_rays()
	pygame.draw.rect(WIN,YELLOW,pygame.Rect(px-3,py-3,6,6))
	pygame.draw.line(WIN,YELLOW,(px,py),(px+5*pdx,py+5*pdy),width=4)
	pygame.draw.line(WIN,BLACK,(895,300),(905,300))
	pygame.draw.line(WIN,BLACK,(900,295),(900,305))
	if stat==False:
		WIN.blit(GUN,(785,posy))
	pygame.display.update()
	
	if posy>410 and jumpstat==False: 
		posy=400
	
	else:
		posy+=0.75
def jump():
	global posy,jumpstat
	for i in range(0,15,1):
		posy=posy-i
		draw()
	for i in range(0,15,1):
		posy=posy+i
		draw()
	jumpstat=False
def cast_rays():
	global px,py,pdx,pdy,rot,color,tvx,tvy,thx,thy,stat
	global vx,vy,hx,hy,vxo,vyo,hxo,hyo,rx,ry 
	x,y=pygame.mouse.get_pos()
	rot1=rot-(np.pi/6)
	if rot1<0:
		rot1+=2.0*np.pi
	if rot1>2.0*np.pi:
		rot1-=2.0*np.pi
	i=1
	for j in range (0,600,1):
		c=int(j/60)
		#Horizontal rays
		if rot1==0 or rot1==np.pi:
			hx=px
			hy=py
		elif rot1<np.pi:
			hy=(int(py/size)+1)*size
			hx= px+(hy-py)*(1/np.tan(rot1))
			hxo=size/np.tan(rot1)
			hyo=size
		else:
			hy=int(py/size)*size
			hx=px+(hy-py)*(1/np.tan(rot1))
			hxo=-size/np.tan(rot1)
			hyo=-size
		for i in range(0,int(600/size),1):
			if hx==px and hy==py:
				break
			if abs(hx)>600 or abs(hy)>600:
				break
			if rot1>0 and rot1<np.pi:
				thx=int(hy/size)
			else:
				thx=int(hy/size)-1
			thy=int(hx/size)
			if thx>=0 and thy>=0 and thx<int(600/size) and thy<int(600/size) and maze[thx][thy]!=0:
				break
			else:
				hx+=hxo
				hy+=hyo
		#pygame.draw.line(WIN,RED,(px,py),(hx,hy))
		#Vertical Lines
		if rot1==np.pi/2 or rot1==3.0*np.pi/2:
			vx=px
			vy=py
		elif rot1<np.pi/2 or rot1>3.0*np.pi/2:
			vx=(int(px/size)+1)*size
			vy=py+(vx-px)*np.tan(rot1)
			vxo=size
			vyo=size*np.tan(rot1)
		else:
			vx=int(px/size)*size
			vy=py+(vx-px)*np.tan(rot1)
			vxo=-size
			vyo=-size*np.tan(rot1)
		for i in range(0,int(600/size),1):
			if vx==px and vy==py:
				break
			if abs(vx)>600 or abs(vy)>600:
				break
			if rot1<np.pi/2 or rot1>3.0*np.pi/2:
				tvy=int(vx/size)
			else:
				tvy=int(vx/size)-1
			tvx=int(vy/size)
			if tvx>=0 and tvy>=0 and tvx<int(600/size) and tvy<int(600/size) and maze[tvx][tvy]!=0:
				
				break
			else:
				vx+=vxo
				vy+=vyo
		#pygame.draw.line(WIN,GREEN,(px,py),(vx,vy),width=4)
		stat1=True
		x,y=pygame.mouse.get_pos()
		if(distance(px,py,hx,hy)<distance(px,py,vx,vy)):
			rx=hx
			ry=hy
			pygame.draw.line(WIN,(155,155,0),(px,py),(rx,ry),width=4)
			h=distance(px,py,rx,ry)
			if h!=0: s=(1/(0.0002*h*(size/25)*np.cos(abs(rot-rot1))))
			x1=thx; y1=thy
			if maze[thx][thy]==2:
				color=(0,0,155)
			elif maze[thx][thy]==3:
				color=(155,0,0)
				if j==300 and y>(300-(s/2)) and y<(300+(s/2)) and stat==True:
					maze[thx][thy]=0
					
			else:
				stat1=False
				color=(0,125,0)
		else:
			rx=vx
			ry=vy
			pygame.draw.line(WIN,(155,155,0),(px,py),(rx,ry),width=4)
			h=distance(px,py,rx,ry)
			if h!=0: s=(1/(0.0002*h*(size/25)*np.cos(abs(rot-rot1))))
			x1=tvx; y1=tvy
			if maze[tvx][tvy]==2:
				color=(0,0,255)
			elif maze[tvx][tvy]==3:
				color=(255,0,0)
				if j==300 and y>(300-(s/2)) and y<(300+(s/2)) and stat==True:
					maze[tvx][tvy]=0
					
			else:
				stat1=False
				color=(0,255,0)
		#pygame.draw.line(WIN,(155,155,0),(px,py),(rx,ry),width=3)
		h=distance(px,py,rx,ry)
		if h!=0: s=(1/(0.0002*h*(size/25)*np.cos(abs(rot-rot1))))
		
		scale=((y-300)/300.0)*200.0
		pygame.draw.rect(WIN,color,pygame.Rect(600+j,300-scale-(s/2),1,s))
		rot1+=(np.pi/(1800.0))
		if rot1<0:
			rot1+=2.0*np.pi
		if rot1>2.0*np.pi:
			rot1-=2.0*np.pi
		i=i+1
		if i>60:
			i=0
def distance(x1,y1,x2,y2):
	return sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
def handle_movement(key):
	global px,py,pdx,pdy,rot,size,jumpstat,squatstat
	global vx,vy,hx,hy,vxo,vyo,hxo,hyo,rx,ry 
	pdx=np.cos(rot)*3
	pdy=np.sin(rot)*3
	x,y=pygame.mouse.get_pos()
	if key[pygame.K_w]:
		px+=pdx
		py+=pdy
		if (maze[int(py/size)][int(px/size)]==1) or (maze[int(py/size)][int(px/size)]==3):
			px-=pdx
			py-=pdy
	if key[pygame.K_s]:
		px-=pdx
		py-=pdy
		if (maze[int(py/size)][int(px/size)]==1) or (maze[int(py/size)][int(px/size)]==3):
			px+=pdx
			py+=pdy
	if key[pygame.K_a]:
		px+=pdy
		py-=pdx
		if (maze[int(py/size)][int(px/size)]==1) or (maze[int(py/size)][int(px/size)]==3):
			px-=pdy
			py+=pdx
	if key[pygame.K_d]:
		px-=pdy
		py+=pdx
		if (maze[int(py/size)][int(px/size)]==1) or (maze[int(py/size)][int(px/size)]==3):
			px+=pdy
			py-=pdx	
	if key[pygame.K_SPACE]:
		jumpstat=True
		jump()	
	if key[pygame.K_LCTRL]:
		pdx=np.cos(rot)*3
		pdy=np.sin(rot)*3
		pygame.draw.rect(WIN,GRAY,pygame.Rect(0,0,1200,600))
		x,y=pygame.mouse.get_pos()
		scale=((y-300)/300.0)*200.0
		WIN.blit(SKY,(600,0))
		WIN.blit(FLOOR,(600,300-scale))
		for i in range(len(maze)):
			for j in range(len(maze[i])):
				if maze[i][j]==1:
					pygame.draw.rect(WIN,WHITE,pygame.Rect(j*size,i*size,size-1,size-1))
				elif maze[i][j]==0:
					pygame.draw.rect(WIN,BLACK,pygame.Rect(j*size,i*size,size-1,size-1))
				elif maze[i][j]==2:
					pygame.draw.rect(WIN,BLUE,pygame.Rect(j*size,i*size,size-1,size-1))
				elif maze[i][j]==3:
					pygame.draw.rect(WIN,RED,pygame.Rect(j*size,i*size,size-1,size-1))
		cast_rays()
		pygame.draw.rect(WIN,YELLOW,pygame.Rect(px-3,py-3,6,6))
		pygame.draw.line(WIN,YELLOW,(px,py),(px+5*pdx,py+5*pdy),width=4)
		pygame.draw.line(WIN,BLACK,(895,300),(905,300))
		pygame.draw.line(WIN,BLACK,(900,295),(900,305))
		#WIN.blit(GUN,(785,425))
		pygame.display.update()
		sleep(1)

	rot=((x+1)/1203.0)*4.0*np.pi
	if rot<0:
		rot+=2.0*np.pi
	if rot>2.0*np.pi:
		rot-=2.0*np.pi

def main():
	global stat
	run=True
	clock=pygame.time.Clock()
	while run:
		clock.tick(FPS)
		draw()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False
			if event.type==pygame.MOUSEBUTTONDOWN:
				SOUND.play()
				stat=True
				for i in range(0,19,1):
					WIN.blit(GUN_FIRE[i],(800,400))
					pygame.display.update()
					draw()
			if event.type==pygame.MOUSEBUTTONUP:
				stat=False
		key=pygame.key.get_pressed()
		handle_movement(key)
	pygame.quit()
if __name__=="__main__":
	main()
