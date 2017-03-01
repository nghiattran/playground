import math

w,h = 20, 16
circleX,circleY,r = 9, 6, 5
x1,y1,x3,y3 = 16, 14, 8, 14

w,h = 11, 11
circleX,circleY,r = 5, 5, 5
x1,y1,x3,y3 = 4, 4, 7, 4

def distance(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  return math.sqrt((x1 - x2)** 2 + (y1 - y2)** 2)

def vector(p1, p2):
  x1, y1 = p1
  x3, y3 = p2
  return (x1 + x3) / 2, (y1 + y3) / 2

def printSquare(grid, p1, p3):
  x1, y1 = p1
  x3, y3 = p3

  center = int((x1 + x3) / 2), int((y1 + y3) / 2 )
  grid[center[0]][center[1]] = '#'

def printGrid(grid):
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      # dist = distance((x, y), (circleX,circleY))
      # if dist <= r:
      #   grid[y][x] = '#'
      dist1 = distance((x, y), (x1, y1))
      dist3 = distance((x, y), (x3, y3))
      if dist1 + dist3 < d1 + d2:
        grid[x][y] = '#'
      print(grid[y][x], end='')
    print()

grid = [['.'] * w for i in range(h)]

printGrid(grid)
