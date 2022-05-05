from turtle import st
import pygame
import time
from settings import *

pygame.init()
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

txt = open("game/map.txt", "w", encoding="utf-8")

dec = []
dec_index = 0
mode = 0

image = pygame.image.load('game/textures/file.png').convert_alpha()
image_p2 = pygame.image.load('game/textures/player2.png').convert_alpha()
exit_image = pygame.image.load('game/textures/exit.png').convert_alpha()
wall_image = pygame.image.load('game/textures/walls.png').convert_alpha()
port_image = pygame.image.load('game/textures/portal.png').convert_alpha()
port2_image = pygame.image.load('game/textures/portal2.png').convert_alpha()
butt_image = pygame.image.load('game/textures/button.png').convert_alpha()
grild_image = pygame.image.load('game/textures/grild.png').convert_alpha()
but2_image = pygame.image.load('game/textures/but2.png').convert_alpha()

myfont = pygame.font.SysFont('Comic Sans MS', 35)

def saveGame():
	for i in dec:
		if i[6] == 1:
			startLet = "@"
		elif i[6] == 2:
			startLet = "&"
		txtWrite = startLet + "0"*(3-len(str(i[0]))) + str(i[0]) + " " + "0"*(3-len(str(i[1]))) + str(i[1])\
			+ " " + "0"*(3-len(str(i[2]))) + str(i[2]) + " " + "0"*(3-len(str(i[3]))) +\
			str(i[3]) + " " + "0"*(3-len(str(i[4]))) + str(i[4]) + " " + str(i[5]) + " \n"

		txt.write(txtWrite)

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	win.fill(white)

	keys = pygame.key.get_pressed()
	if keys[pygame.K_n]:
		dec.append([0, 0, 50, 50, 0, 1, 1])
		time.sleep(0.25)
	if keys[pygame.K_e]:
		if dec_index >= len(dec)-1:
			dec_index = 0
		else:
			dec_index += 1
		time.sleep(0.25)
	if keys[pygame.K_q]:
		if mode > 4:
			mode = 0
		else:
			mode += 1
		time.sleep(0.25)

	if mode == 0:
		if keys[pygame.K_UP]:
			dec[dec_index][1] -= speed
		if keys[pygame.K_DOWN]:
			dec[dec_index][1] += speed
		if keys[pygame.K_RIGHT]:
			dec[dec_index][0] += speed
		if keys[pygame.K_LEFT]:
			dec[dec_index][0] -= speed
	if mode == 1:
		if keys[pygame.K_UP]:
			dec[dec_index][1] -= speed
			dec[dec_index][3] += speed
		if keys[pygame.K_DOWN]:
			dec[dec_index][1] += speed
			dec[dec_index][3] -= speed
		if keys[pygame.K_RIGHT]:
			dec[dec_index][0] += speed
			dec[dec_index][2] -= speed
		if keys[pygame.K_LEFT]:
			dec[dec_index][0] -= speed
			dec[dec_index][2] += speed
	if mode == 2:
		if keys[pygame.K_UP]:
			dec[dec_index][3] -= speed
		if keys[pygame.K_DOWN]:
			dec[dec_index][3] += speed
		if keys[pygame.K_RIGHT]:
			dec[dec_index][2] += speed
		if keys[pygame.K_LEFT]:
			dec[dec_index][2] -= speed
	if mode == 3:
		if keys[pygame.K_UP]:
			dec[dec_index][4] += 1
			time.sleep(0.25)
		if keys[pygame.K_DOWN]:
			if i[4] != 0:
				dec[dec_index][4] -= 1
			time.sleep(0.25)
		if keys[pygame.K_RIGHT]:
			if i[5] != 2:
				dec[dec_index][5] += 1
			time.sleep(0.25)
		if keys[pygame.K_LEFT]:
			if i[5] != 1:
				dec[dec_index][5] -= 1
			time.sleep(0.25)
	if mode == 4:
		if keys[pygame.K_UP]:
			if i[6] != 2:
				dec[dec_index][6] += 1
			time.sleep(0.25)
		if keys[pygame.K_DOWN]:
			if i[6] != 1:
				dec[dec_index][6] -= 1
			time.sleep(0.25)

	if keys[pygame.K_TAB]:
		run = False
		saveGame()

	#txtWrite = ""

	try:
		for i in dec:
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

		if mode == 0:
			pygame.draw.rect(win, red, (dec[dec_index][0], dec[dec_index][1], dec[dec_index][2], 5))
			pygame.draw.rect(win, red, (dec[dec_index][0], dec[dec_index][1], 5, dec[dec_index][3]))
			pygame.draw.rect(win, red, (dec[dec_index][0]+dec[dec_index][2]-5, dec[dec_index][1], 5, dec[dec_index][3]))
			pygame.draw.rect(win, red, (dec[dec_index][0], dec[dec_index][1]+dec[dec_index][3]-5, dec[dec_index][2], 5))
		elif mode == 1:
			pygame.draw.rect(win, red, (dec[dec_index][0], dec[dec_index][1], dec[dec_index][2], 5))
			pygame.draw.rect(win, red, (dec[dec_index][0], dec[dec_index][1], 5, dec[dec_index][3]))
		elif mode == 2:
			pygame.draw.rect(win, red, (dec[dec_index][0]+dec[dec_index][2]-5, dec[dec_index][1], 5, dec[dec_index][3]))
			pygame.draw.rect(win, red, (dec[dec_index][0], dec[dec_index][1]+dec[dec_index][3]-5, dec[dec_index][2], 5))
		elif mode == 3:
			textsurface = myfont.render(str(dec[dec_index][4]), False, (0, 0, 0))
			win.blit(textsurface, (dec[dec_index][0], dec[dec_index][1]))

			textsurface1 = myfont.render(str(dec[dec_index][5]), False, (0, 0, 0))
			win.blit(textsurface1, (dec[dec_index][0]+dec[dec_index][2]-20, dec[dec_index][1]))
		elif mode == 4:
			textsurface2 = myfont.render(str(dec[dec_index][6]), False, (0, 0, 0))
			win.blit(textsurface2, (dec[dec_index][0], dec[dec_index][1]))
		#print(mode)

		#txtWrite = "@" + str(dec[dec_index][0]) + " " + str(dec[dec_index][1]) + " " + str(dec[dec_index][2]) + " " +\
		#	str(dec[dec_index][3]) + " " + str(dec[dec_index][4]) + " True\n"
	except:
		None

	#txt.write(txtWrite)
	#print(txtWrite)

	pygame.display.flip()
	clock.tick(fps)
pygame.quit()
txt.close()