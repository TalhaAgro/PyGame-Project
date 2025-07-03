import pygame
import sys
from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Pixel Game')
        
        self.level=Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill((0,0,0))
            self.level.run()
            
            pygame.display.update()
            self.clock.tick(FPS)
            
            

if __name__=='__main__':
    game=Game()
    game.run()
    

