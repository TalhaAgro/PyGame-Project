import pygame
from settings import *
from player import Player
from tile import Tile

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        self.player = Player((10, 10), [self.visible_sprites], self.obstacle_sprites)
        self.tile=Tile((50,50), [self.visible_sprites, self.obstacle_sprites])
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width=self.display_surface.get_size()[0]//2
        self.half_height=self.display_surface.get_size()[1]//2
        self.offset= pygame.math.Vector2()
    
        self.floor_surf=pygame.image.load('assets/Images/imageResources/world/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0,0))
    
    def custom_draw(self, player):
        
        self.offset.x=player.rect.centerx-self.half_width
        self.offset.y=player.rect.centery-self.half_height
        
        floor_offset_pos=self.floor_rect.topleft-self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)
        
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos=sprite.rect.topleft-self.offset
            self.display_surface.blit(sprite.image, offset_pos)
