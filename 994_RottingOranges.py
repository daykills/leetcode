class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        min_used = 0
        queue = []
        fresh = 0
        m, n = len(grid), len(grid[0])
        dirts = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        #add all rotten oranges into the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
                    
        #bfs
        while fresh and queue:
            size = len(queue)
            
            for i in range(size):
                curRow, curCol = queue.pop(0)
                      
                for diffRow, diffCol in dirts:
                    newRow = curRow + diffRow
                    newCol = curCol + diffCol
                    if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
                        fresh -= 1
          
            min_used += 1
            
        return min_used if fresh == 0 else -1
                
