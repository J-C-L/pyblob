from blob import Blob
import random

class BlueBlob(Blob):
  def __init__(self, x_boundary, y_boundary):
    super().__init__((0, 0, 225), x_boundary, y_boundary)
  
  def move(self):
    self.x += random.randrange(-7, 7)
    self.y += random.randrange(-7, 7)