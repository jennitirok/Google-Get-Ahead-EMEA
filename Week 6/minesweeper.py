class Cell:

  def __init__(self):
    # Initialise all cells in Minefield with 0
    self.value = 0
    self.is_visible = False

class Matrix:

  def __init__(self):
    # Initial Matrix size
    self.rows = 0
    self.cols = 0
    # Will be a two-dimensional array
    self.matrix = []

  def resize(self, rows, cols):
    self.rows = rows
    self.cols = cols

    # Fill each rows and cols with a Cell
    # e.g. [[0,0], [0,0]] for a 2x2 Matrix
    row = []
    for i in range(0, self.rows):
      row = [Cell() for j in range(0, self.cols)]
      self.matrix.append(row)

class Minefield:

  def __init__(self, rows, cols, number_of_mines):
    self.field = Matrix()
    self.field.resize(rows, cols)

    # Start assigning each field with its respective number
    # Check so that number_of_mines do not exceed the size of the field
    if number_of_mines > (rows * cols):
      raise ValueError("Number of Mines cannot exceed the size of field")

  def on_click(self, row, col):
    pass

  def print_minefield(self, show_hidden):
    pass