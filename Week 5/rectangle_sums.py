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
  del shape
  return Result(sum=0, rectangle=Rect(Coord(0, 0), Coord(0, 0)))