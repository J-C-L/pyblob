import pygame
import random
from blue_blob import BlueBlob
from red_blob import RedBlob
from green_blob import GreenBlob
from orange_blob import OrangeBlob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3
STARTING_GREEN_BLOBS = 5
STARTING_ORANGE_BLOBS = 6

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Blob World')
clock = pygame.time.Clock()

def handle_collisions(blob_list):
    for blob_dict in blob_list:
      for blob in blob_dict.values():
        for other_blob_dict in blob_list:
          for other_blob in other_blob_dict.values():
            if blob == other_blob:
              pass
            else:
              if blob.is_touching(blob, other_blob):
                blob.color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
                        
    return blob_list

def draw_environment(blob_list, with_colisions):
    game_display.fill(WHITE)
    if with_colisions:
      handle_collisions(blob_list)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            blob.draw(game_display)
            if isinstance(blob, OrangeBlob):
              if blob_id == STARTING_ORANGE_BLOBS - 1:
                blob.move_with_mouse(blob_id)
              else:
                blob.follow_leader(blob_id, blob_dict)
            else:
              blob.move()
      
    pygame.display.update()

        
def main(with_colisions = True):
    blue_blobs = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH,HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
    orange_blobs = dict(enumerate([OrangeBlob(WIDTH,HEIGHT) for i in range(STARTING_ORANGE_BLOBS)]))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blobs, red_blobs, green_blobs, orange_blobs], with_colisions)
        clock.tick(20)

if __name__ == '__main__':
    main(with_colisions = True)