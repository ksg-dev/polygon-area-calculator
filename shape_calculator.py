class Rectangle:
  def __init__(self, width, height):
    self._width = width
    self._height = height

  def __str__(self):
    return f"Rectangle(width={self._width}, height={self._height})"

  def get_width(self):
    return self._width
  
  def set_width(self, width):
    self._width = width

  def get_height(self):
    return self._height
  
  def set_height(self, height):
    self._height = height

  def get_area(self):
    area = self._width * self._height
    return area

  def get_perimeter(self):
    perimeter = 2 * self._width + 2 * self._height
    return perimeter

  def get_diagonal(self):
    diagonal = (self._width ** 2 + self._height ** 2)**.5
    return diagonal

  def get_picture(self):
    picture = ""
    
    if self._width > 50:
      return "Too big for picture."
    elif self._height > 50:
      return "Too big for picture."
    else:
      count = self._height
      line = "*" * self._width
      while count:
        picture += line + '\n'
        count += -1
        
      
    return picture

  def get_amount_inside(self, shape):
    wide = self._width // shape._width
    tall = self._height // shape._height
    return wide * tall
    

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(width=side, height=side)
    

  def __str__(self):
    return f"Square(side=w={self._width}, h={self._height})"
  
  def get_side(self):
    return self._width, self._height
  
  def set_side(self, width):
    self._width = width
    self._height = width

  def set_height(self, height):
    self._height = height
    self._width = height
    

  def set_width(self, width):
    self._width = width
    self._height = width
    
  
  

  