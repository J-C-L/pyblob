import random
import pygame
import math

class Blob:
    
    def __init__(self, color, x_boundary, y_boundary, size_range=(4,18), movement_range=(-1, 2), stay_within_bounds = True):
        self.size = random.randrange(size_range[0], size_range[1])
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.movement_range = movement_range 
        self.stay_within_bounds = stay_within_bounds
        
    def move(self):
        move_x = random.randrange(self.movement_range[0], self.movement_range[1])
        move_y = random.randrange(self.movement_range[0], self.movement_range[1])
        self.x += move_x
        self.y += move_y
        if self.stay_within_bounds:
          self.check_bounds()
    
    def move_with_mouse(self, blob_id):
        self.x = pygame.mouse.get_pos()[0] + blob_id  
        self.y = pygame.mouse.get_pos()[1] + blob_id 
    
    def follow_leader(self, blob_id, blob_dict):
        self.x = (blob_dict[blob_id + 1].x)
        self.y = (blob_dict[blob_id + 1].y)

    def check_bounds(self):
        if self.x < 0: self.x = 0
        elif self.x > self.x_boundary: self.x = self.x_boundary
        
        if self.y < 0: self.y = 0
        elif self.y > self.y_boundary: self.y = self.y_boundary
    
    def draw(self, game_display):
        pygame.draw.circle(game_display, self.color, [self.x, self.y], self.size)

    def is_touching(self, b1, b2):
      if b1.x == b2.x and b1.y == b2.y:
        return False
      else:
        return math.sqrt((b2.x-b1.x)**2 + (b2.y-b1.y)**2) < (b1.size + b2.size)


