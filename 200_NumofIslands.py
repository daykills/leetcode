class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == '1':
                grid[i][j] = '0'
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j -1)
            else:
                return 0
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j):
                    res += 1
        return res
                    
