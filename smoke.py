import pygame
from support import import_folder


class Smoke(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.1
        self.image = self.animations['smoke'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

    def import_character_assets(self):
        character_path = 'C:/Users/Mardyson Justin/Desktop/GameProject/GameProject/assets/fire/'
        self.animations = {'smoke': []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations['smoke']
        frame_count = len(animation)

        # loop over the frame index
        if self.frame_index < frame_count:
            self.frame_index += self.animation_speed
            if self.frame_index >= frame_count:
                self.frame_index = frame_count - 1

            image = animation[int(self.frame_index)]
            self.image = image

    def update(self, x_shift):
        self.rect.x += x_shift
        self.animate()
