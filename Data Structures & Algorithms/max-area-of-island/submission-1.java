class Solution {
    private int dfs(int r, int c, int ROWS, int COLS, int[][] grid) {
        if (r < 0 || r >= ROWS || c < 0 || c >= COLS || grid[r][c] == 0) {
            return 0;
        }

        grid[r][c] = 0;
        int res = 1;

        res += dfs(r + 1, c, ROWS, COLS, grid);
        res += dfs(r - 1, c, ROWS, COLS, grid);
        res += dfs(r, c + 1, ROWS, COLS, grid);
        res += dfs(r, c - 1, ROWS, COLS, grid);

        return res;
    }
    
    public int maxAreaOfIsland(int[][] grid) {
        int ROWS = grid.length;
        int COLS = grid[0].length;
        int res = 0;

        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (grid[i][j] == 1) {
                    res = Math.max(res, dfs(i, j, ROWS, COLS, grid));
                }
            }
        }

        return res;
    }
}
