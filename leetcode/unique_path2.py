class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        for x in range(row):
            for y in range(col):
                if obstacleGrid[x][y] == 1:
                    obstacleGrid[x][y] = None
                    continue

                if x == 0 and y == 0:
                    obstacleGrid[x][y] = 1

                if x - 1 >= 0 and obstacleGrid[x - 1][y] is not None:
                    obstacleGrid[x][y] += obstacleGrid[x - 1][y]

                if y - 1 >= 0 and obstacleGrid[x][y - 1] is not None:
                    obstacleGrid[x][y] += obstacleGrid[x][y - 1]
        return obstacleGrid[row - 1][col - 1]

matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]
]
print(Solution().uniquePathsWithObstacles(matrix))