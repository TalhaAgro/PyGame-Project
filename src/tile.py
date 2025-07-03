from settings import *
import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image= pygame.image.load('assets/Images/imageResources/monsters/raccoon/idle/0.png').convert_alpha()
        self.rect=self.image.get_rect(topleft=pos)
        self.hitbox=self.rect.inflate(0, -3)