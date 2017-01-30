class Solution(object):
  def islandPerimeter(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    row = len(grid)
    col = len(grid[0])
    count = 0
    for x in range(row):
      for y in range(col):
        if grid[x][y] == 0:
          continue
        if x == 0 or grid[x - 1][y] == 0:
          count += 1
        if x == row - 1 or grid[x + 1][y] == 0:
          count += 1
        if y == 0 or grid[x][y - 1] == 0:
          count += 1
        if y == col - 1 or grid[x][y + 1] == 0:
          count += 1

    return count

grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

print(Solution().islandPerimeter(grid))