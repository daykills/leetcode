class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j, dirts):
            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
                grid[i][j] = 0
                path.append(dirts)
                dfs(i + 1, j, 'R')
                dfs(i - 1, j, 'L')
                dfs(i, j + 1, 'U')
                dfs(i, j - 1, 'D')
                path.append('E')
   
        
        res = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, '')
                    res.add(''.join(path))
        return len(res)
