from blob import Blob

class OrangeBlob(Blob):
  def __init__(self, x_boundary, y_boundary):
    super().__init__((255, 165, 0), x_boundary, y_boundary, size_range = (4,12))
    
  def check_bounds(self):
    if self.x < 0: 
      self.x = 0
    elif self.x > self.x_boundary: 
      self.x = self.x_boundary
    
    if self.y < 0: 
      self.y = 0
    elif self.y > self.y_boundary: 
      self.y = self.y_boundary