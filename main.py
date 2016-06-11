import pygame
from pygame.locals import *
import sys

white = (255, 255, 255)

class Game(object):

	def main(self, screen):
	
		clock = pygame.time.Clock()
		
		game_exit = False
		
		while not game_exit:
			dt = clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
					game_exit = True
			
			screen.fill(white)
			pygame.display.update()

if __name__ == "__main__":
	pygame.init()
	screen_width = 800
	screen_height = 600
	screen_size = (screen_width, screen_height)
	screen = pygame.display.set_mode(screen_size)
	Game().main(screen)
			