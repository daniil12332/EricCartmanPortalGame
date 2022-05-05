from re import X
import pygame
from settings import *

pygame.init()
pygame.font.init()
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("game")
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Comic Sans MS', 22)

image = pygame.image.load('game/textures/file.png').convert_alpha()
image_p2 = pygame.image.load('game/textures/player2.png').convert_alpha()
wall_image = pygame.image.load('game/textures/walls.png').convert_alpha()	
exit_image = pygame.image.load('game/textures/exit.png').convert_alpha()
port_image = pygame.image.load('game/textures/portal.png').convert_alpha()
port2_image = pygame.image.load('game/textures/portal2.png').convert_alpha()
butt_image = pygame.image.load('game/textures/button.png').convert_alpha()
grild_image = pygame.image.load('game/textures/grild.png').convert_alpha()
but2_image = pygame.image.load('game/textures/but2.png').convert_alpha()

txt = open("game/map.txt", "r", encoding="utf-8")
txt2 = open("game/map1.txt", "r", encoding="utf-8")
game = list(txt.read())

#engine_class = game()

new_image = pygame.transform.scale(image, (50, 50))
new_image_p2 = pygame.transform.scale(image_p2, (50, 50))

def Rect(x, y, w, h, color, mode, enable):
	if enable:
		if mode == 25:
			#pygame.draw.rect(win, color, (x, y, w, h))

			new_port_image = pygame.transform.scale(port_image, (w, h))
			win.blit(new_port_image, (x, y))
		elif mode == 26:
			#pygame.draw.rect(win, color, (x, y, w, h))

			new_port2_image = pygame.transform.scale(port2_image, (w, h))
			win.blit(new_port2_image, (x, y))
		elif mode == 27:
			#pygame.draw.rect(win, color, (x, y, w, h))

			new_exit_image = pygame.transform.scale(exit_image, (w, h))
			win.blit(new_exit_image, (x, y))
		elif mode == 2:
			#pygame.draw.rect(win, color, (x, y, w, h))

			new_butt_image = pygame.transform.scale(butt_image, (w, h))
			win.blit(new_butt_image, (x, y))
		elif mode == 3:
			#pygame.draw.rect(win, color, (x, y, w, h))

			new_but2_image = pygame.transform.scale(but2_image, (w, h))
			win.blit(new_but2_image, (x, y))
		elif mode == 4:
			#pygame.draw.rect(win, color, (x, y, w, h))

			new_grild_image = pygame.transform.scale(grild_image, (w, h))
			win.blit(new_grild_image, (x, y))
		else:
			new_wall_image = pygame.transform.scale(wall_image, (w, h))
			win.blit(new_wall_image, (x, y))
	return x, y, w, h, mode, enable
dec1 = []
otherDec1 = []
index = 0
for i in game:
	if i == "@":
		if game[index+21] == "1":
			predec1 = True
		elif game[index+21] == "2":
			predec1 = False
		dec1.append([int(game[index+1])*100+int(game[index+2])*10+int(game[index+3]),\
			int(game[index+5])*100+int(game[index+6])*10+int(game[index+7]),\
			int(game[index+9])*100+int(game[index+10])*10+int(game[index+11]),\
			int(game[index+13])*100+int(game[index+14])*10+int(game[index+15]),\
			int(game[index+17])*100+int(game[index+18])*10+int(game[index+19]), predec1])
	if i == "&":
		if game[index+21] == "1":
			predec1 = True
		elif game[index+21] == "2":
			predec1 = False
		otherDec1.append([int(game[index+1])*100+int(game[index+2])*10+int(game[index+3]),\
			int(game[index+5])*100+int(game[index+6])*10+int(game[index+7]),\
			int(game[index+9])*100+int(game[index+10])*10+int(game[index+11]),\
			int(game[index+13])*100+int(game[index+14])*10+int(game[index+15]),\
			int(game[index+17])*100+int(game[index+18])*10+int(game[index+19]), predec1])
	index += 1

x2 = 0
y2 = 0

dec = dec1
otherDec = otherDec1
run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	index = 0
	for i in dec1:
		dec1[index][0] += x - x2
		dec1[index][1] += y - y2
		index += 1

	index = 0
	for i in otherDec1:
		otherDec1[index][0] += x - x2
		otherDec1[index][1] += y - y2
		index += 1

	x2 = x
	y2 = y

	win.fill(white)
	textsurface = myfont.render(str(x) + ", " + str(y), False, (0, 0, 0))
	#print(setings.object("hi"))
	isRight = True
	isUp = True
	isDown = True
	isLeft = True

	ends_liUp=[]
	ends_liDown=[]
	ends_liRight=[]
	ends_liLeft=[]
	
	dec = dec1
	otherDec = otherDec1

	

	#ENGINE

	#engine_class.engine()

	But1 = False

	if but1:
		But1 = False
	else:
		But1 = True


	#dec2 = [Rect(x+50, y+50, 700, 50, green, 0, True),
	#	   Rect(x+50, y+50, 50, 500, green, 0, True),
	#	   Rect(x+50, y+500, 700, 50, green, 0, True),
	#	   Rect(x+700, y+50, 50, 500, green, 0, True),
	#	   Rect(x+200, y+400, 500, 5, green, 0, True),
	#	   Rect(x+175, y+300, 5, 100, lightRed, 4, True),
	#	   Rect(x+100, y+300, 75, 5, lightRed, 4, True),
	#	   Rect(x+175, y+400, 75, 5, lightRed, 4, True),
	#	   Rect(x+250, y+50, 50, 500, lightRed, 4, True),
	#	   Rect(x+100, y+200, 150, 5, lightRed, 0, but1)]

	#dec = dec2

	for i in dec:
		if i[5]:
			if i[4] == 25:
				#pygame.draw.rect(win, color, (x, y, w, h))

				new_port_image = pygame.transform.scale(port_image, (i[2], i[3]))
				win.blit(new_port_image, (i[0], i[1]))
			elif i[4] == 26:
				#pygame.draw.rect(win, color, (x, y, w, h))

				new_port2_image = pygame.transform.scale(port2_image, (i[2], i[3]))
				win.blit(new_port2_image, (i[0], i[1]))
			elif i[4] == 27:
				#pygame.draw.rect(win, color, (x, y, w, h))

				new_exit_image = pygame.transform.scale(exit_image, (i[2], i[3]))
				win.blit(new_exit_image, (i[0], i[1]))
			elif i[4] == 2:
				#pygame.draw.rect(win, color, (x, y, w, h))

				new_butt_image = pygame.transform.scale(butt_image, (i[2], i[3]))
				win.blit(new_butt_image, (i[0], i[1]))
			elif i[4] == 3:
				#pygame.draw.rect(win, color, (x, y, w, h))

				new_but2_image = pygame.transform.scale(but2_image, (i[2], i[3]))
				win.blit(new_but2_image, (i[0], i[1]))
			elif i[4] == 4 or i[4] == 6:
				#pygame.draw.rect(win, color, (x, y, w, h))

				new_grild_image = pygame.transform.scale(grild_image, (i[2], i[3]))
				win.blit(new_grild_image, (i[0], i[1]))
			else:
				new_wall_image = pygame.transform.scale(wall_image, (i[2], i[3]))
				win.blit(new_wall_image, (i[0], i[1]))

				#Rect(x+125, y+350, 25, 25, lightRed, 2, but1),
				#Rect(x+125, y+350, 25, 25, lightRed, 3, But1),
				#Rect(x+100, y+100, 25, 25, lightRed, 27, True)]

	for i in otherDec:
		if i[5]:
			if i[4] == 25:
				#pygame.draw.rect(win, color, (x, y, w, h))

				new_port_image = pygame.transform.scale(port_image, (i[2], i[3]))
				win.blit(new_port_image, (i[0], i[1]))
			elif i[4] == 26:
				#pygame.draw.rect(win, color, (x, y, w, h))

				new_port2_image = pygame.transform.scale(port2_image, (i[2], i[3]))
				win.blit(new_port2_image, (i[0], i[1]))
			elif i[4] == 27:
				#pygame.draw.rect(win, color, (x, y, w, h))

				new_exit_image = pygame.transform.scale(exit_image, (i[2], i[3]))
				win.blit(new_exit_image, (i[0], i[1]))
			elif i[4] == 2:
				#pygame.draw.rect(win, color, (x, y, w, h))

				new_butt_image = pygame.transform.scale(butt_image, (i[2], i[3]))
				win.blit(new_butt_image, (i[0], i[1]))
			elif i[4] == 3:
				#pygame.draw.rect(win, color, (x, y, w, h))

				new_but2_image = pygame.transform.scale(but2_image, (i[2], i[3]))
				win.blit(new_but2_image, (i[0], i[1]))
			elif i[4] == 4:
				#pygame.draw.rect(win, color, (x, y, w, h))

				new_grild_image = pygame.transform.scale(grild_image, (i[2], i[3]))
				win.blit(new_grild_image, (i[0], i[1]))
			else:
				new_wall_image = pygame.transform.scale(wall_image, (i[2], i[3]))
				win.blit(new_wall_image, (i[0], i[1]))

	for i in dec:
		if 275 <= i[1]+i[3] and 274+50 >= i[1] and 374+50 >= i[0] and 376 <= i[0]+i[2] and i[5]:
			isUp = False
		if 276 <= i[1]+i[3] and 275+50 >= i[1] and 374+50 >= i[0] and 376 <= i[0]+i[2] and i[5]:
			isDown = False
		if 276 <= i[1]+i[3] and 274+50 >= i[1] and 375+50 >= i[0] and 376 <= i[0]+i[2] and i[5]:
			isRight = False
		if 276 <= i[1]+i[3] and 274+50 >= i[1] and 374+50 >= i[0] and 375 <= i[0]+i[2] and i[5]:
			isLeft = False

		if i[0] < 400 and i[0]+i[2] > 400 and 275-(i[1]+i[3]) >= 0 and i[5] and i[4] != 4:
			ends_liUp.append(275-(i[1]+i[3]))
			isPUp = i[4]
		if i[0] < 400 and i[0]+i[2] > 400 and i[1]-275 > 0 and i[5] and i[4] != 4:
			ends_liDown.append(i[1]-275)
			isPDown = i[4]
		if i[1] < 300 and i[1]+i[3] > 300 and 375-(i[0]+i[2]) >= 0 and i[5] and i[4] != 4:
			ends_liLeft.append(375-(i[0]+i[2]))
			isPLeft = i[4]
		if i[1] < 300 and i[1]+i[3] > 300 and i[0]-375 > 0 and i[5] and i[4] != 4:
			ends_liRight.append(i[0]-375)
			isPRight = i[4]

	for i in otherDec:
		if 274 <= i[1]+i[3] and 276+50 >= i[1] and 376+50 >= i[0] and 374 <= i[0]+i[2] and (i[4] == 2 or i[4] == 3) and i[5]:
			if but1_1 == False and but1 == False:
				but1 = True
				i[4] = 2
			elif but1_1 == False and but1 == True:
				but1 = False
				i[4] = 3
			but1_1 = True
		elif (i[4] == 2 or i[4] == 3) and i[5]:
			but1_1 = False
		if 274 <= i[1]+i[3] and 276+50 >= i[1] and 376+50 >= i[0] and 374 <= i[0]+i[2] and i[4] == 27 and i[5] and lvl == 1:
			#run = False
			game = list(txt2.read())
			dec1 = []
			otherDec1 = []
			index = 0
			for i in game:
				if i == "@":
					if game[index+21] == "1":
						predec1 = True
					elif game[index+21] == "2":
						predec1 = False
					dec1.append([int(game[index+1])*100+int(game[index+2])*10+int(game[index+3]),\
						int(game[index+5])*100+int(game[index+6])*10+int(game[index+7]),\
						int(game[index+9])*100+int(game[index+10])*10+int(game[index+11]),\
						int(game[index+13])*100+int(game[index+14])*10+int(game[index+15]),\
						int(game[index+17])*100+int(game[index+18])*10+int(game[index+19]), predec1])
				if i == "&":
					if game[index+21] == "1":
						predec1 = True
					elif game[index+21] == "2":
						predec1 = False
					otherDec1.append([int(game[index+1])*100+int(game[index+2])*10+int(game[index+3]),\
						int(game[index+5])*100+int(game[index+6])*10+int(game[index+7]),\
						int(game[index+9])*100+int(game[index+10])*10+int(game[index+11]),\
						int(game[index+13])*100+int(game[index+14])*10+int(game[index+15]),\
						int(game[index+17])*100+int(game[index+18])*10+int(game[index+19]), predec1])
				index += 1
			#x = 0
			#y = 0
			player = 2
			port1Up = False
			port1Down = False
			port1Left = False
			port1Right = False

			port2Up = False
			port2Down = False
			port2Left = False
			port2Right = False

			lvl += 1



	#END ENGINE


	if port1Up:
		ports1=Rect(x+port1Up_x, y+port1Up_y, 100, 25, blue, 25, True)
	if port1Down:
		ports1=Rect(x+port1Down_x, y+port1Down_y, 100, 25, blue, 25, True)
	if port1Left:
		ports1=Rect(x+port1Left_x, y+port1Left_y, 25, 100, blue, 25, True)
	if port1Right:
		ports1=Rect(x+port1Right_x, y+port1Right_y, 25, 100, blue, 25, True)

	if port2Up:
		ports2=Rect(x+port2Up_x, y+port2Up_y, 100, 25, red, 26, True)
	if port2Down:
		ports2=Rect(x+port2Down_x, y+port2Down_y, 100, 25, red, 26, True)
	if port2Left:
		ports2=Rect(x+port2Left_x, y+port2Left_y, 25, 100, red, 26, True)
	if port2Right:
		ports2=Rect(x+port2Right_x, y+port2Right_y, 25, 100, red, 26, True)

	keys = pygame.key.get_pressed()
	try:
		if 274 <= ports1[1]+ports1[3] and 276+50 >= ports1[1] and 376+50 >= ports1[0] and 374 <= ports1[0]+ports1[2]:
			if port2Up:
				x = 350 - port2Up_x
				y = 275 - port2Up_y - 30
			if port2Down:
				x = 350 - port2Down_x
				y = 275 - port2Down_y + 55
			if port2Left:
				x = 350 - port2Left_x - 5
				y = 275 - port2Left_y - 25
			if port2Right:
				x = 350 - port2Right_x + 80
				y = 275 - port2Right_y - 25
	except:
		None

	try:
		if 274 <= ports2[1]+ports2[3] and 276+50 >= ports2[1] and 376+50 >= ports2[0] and 374 <= ports2[0]+ports2[2]:
			if port1Up:
				x = 350 - port1Up_x
				y = 275 - port1Up_y - 30
			if port1Down:
				x = 350 - port1Down_x
				y = 275 - port1Down_y + 55
			if port1Left:
				x = 350 - port1Left_x - 5
				y = 275 - port1Left_y - 25
			if port1Right:
				x = 350 - port1Right_x + 80
				y = 275 - port1Right_y - 25
	except:
		None

	if keys[pygame.K_w] and isUp:
		y += speed
	if keys[pygame.K_s] and isDown:
		y -= speed
	if keys[pygame.K_a] and isLeft:
		x += speed
	if keys[pygame.K_d] and isRight:
		x -= speed


	if keys[pygame.K_UP]:
		pygame.draw.line(win, blue, (400, 275), (400, 275-min(ends_liUp)))
		if keys[pygame.K_q] and isPUp == 0:
			port1Up = True
			port1Down = False
			port1Right = False
			port1Left = False
			port1Up_x = 350-x
			port1Up_y = 275-min(ends_liUp)-y-25
		if keys[pygame.K_e] and isPUp == 0:
			port2Up = True
			port2Down = False
			port2Right = False
			port2Left = False
			port2Up_x = 350-x
			port2Up_y = 275-min(ends_liUp)-y-25
	if keys[pygame.K_DOWN]:
		pygame.draw.line(win, blue, (400, 325), (400, min(ends_liDown)+275))
		if keys[pygame.K_q] and isPDown == 0:
			port1Up = False
			port1Down = True
			port1Right = False
			port1Left = False
			port1Down_x = 350-x
			port1Down_y = 275+min(ends_liDown)-y
		if keys[pygame.K_e] and isPDown == 0:
			port2Up = False
			port2Down = True
			port2Right = False
			port2Left = False
			port2Down_x = 350-x
			port2Down_y = 275+min(ends_liDown)-y
	if keys[pygame.K_LEFT]:
		pygame.draw.line(win, blue, (375, 300), (375-min(ends_liLeft), 300))
		if keys[pygame.K_q] and isPLeft == 0:
			port1Up = False
			port1Down = False
			port1Right = False
			port1Left = True
			port1Left_x = 375-min(ends_liLeft)-x-25
			port1Left_y = 250-y
		if keys[pygame.K_e] and isPLeft == 0:
			port2Up = False
			port2Down = False
			port2Right = False
			port2Left = True
			port2Left_x = 375-min(ends_liLeft)-x-25
			port2Left_y = 250-y
	if keys[pygame.K_RIGHT]:
		pygame.draw.line(win, blue, (425, 300), (min(ends_liRight)+375, 300))
		if keys[pygame.K_q] and isPRight == 0:
			port1Up = False
			port1Down = False
			port1Right = True
			port1Left = False
			port1Right_x = 375+min(ends_liRight)-x
			port1Right_y = 250-y
		if keys[pygame.K_e] and isPRight == 0:
			port2Up = False
			port2Down = False
			port2Right = True
			port2Left = False
			port2Right_x = 375+min(ends_liRight)-x
			port2Right_y = 250-y

	index = 0
	for i in dec:
		if i[4] == 5:
			dec[index][5] = but1
		index += 1

	if keys[pygame.K_r]:
		x = 0
		y = 0
	if keys[pygame.K_TAB]:
		run = False



	#pygame.draw.rect(win, red, (375, 275, 50, 50))
	if player == 1:
		win.blit(new_image, (375, 275))
	else:
		win.blit(new_image_p2, (375, 275))
	if debug:
		win.blit(textsurface, (0,0))
	#win.blit(new_empty_image, (50, 50))
	pygame.display.flip()
	clock.tick(fps)
pygame.quit()
txt.close()