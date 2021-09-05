"""Starter code for the Rectangle Sum Problem (Get Ahead)."""

# In the signature below we use type hints. The python runtime doesn't
# enforce them, but they are a great way to make code more understandable.
# To learn more: https://docs.python.org/3/library/typing.html
from typing import List
from dataclasses import dataclass


# Behind the scenes, the dataclass decorator adds boilerplate methods (__init__,
# __eq__, __repr__, etc) for this struct-like class.
@dataclass
class Coord:
  """Coordinates for one cell in the input."""
  x: int
  y: int


@dataclass
class Rect:
  """Specification of a rectangle based on two of its corners."""
  top_left: Coord
  bottom_right: Coord


@dataclass
class Result:
  """The result should contain the optimal sum and a rectangle with that sum.."""
  sum: int
  rectangle: Rect


# The class definitions above are there to help with data representation;
# you only need to add your implementation in this function.
def get_largest_sum(shape: List[List[int]]) -> Result:
  """Returns the largest possible sum and coordinates for that sum from any rectangle in the input."""
  largest_result = Result(sum=0, rectangle=Rect(Coord(0, 0), Coord(0, 0)))
  prev_row_largest_sums: List[Result] = []

  # Iterate over all rows
  for y_index, row in enumerate(shape):
    curr_row_largest_sums: List[Result] = []
    row_sum = 0

    for x_index, cell in enumerate(row):
      # Keep track of the sum of numbers on this row so far
      row_sum += cell
      curr_result = Result(
          sum=row_sum,
          rectangle=Rect(
              top_left=Coord(x=0, y=y_index),
              bottom_right=Coord(x=x_index, y=y_index)))

      if len(prev_row_largest_sums) > x_index:
        prev_result = prev_row_largest_sums[x_index]
        curr_result.sum += prev_result.sum
        curr_result.rectangle.top_left = prev_result.rectangle.top_left

      # Store the sum for the next iteration
      curr_row_largest_sums.append(curr_result)
      
      # Check if this is the highest-sum rectangle seen so far
      if curr_result.sum > largest_result.sum:
        largest_result = curr_result
    prev_row_largest_sums = curr_row_largest_sums

  del shape
  return largest_result