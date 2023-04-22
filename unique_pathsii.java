public class unique_pathsii {
    public static boolean isSafe(int[][] maze,int x,int y){
        if(maze[x][y]==0){
            return true;
        }
        return false;
    }
    public static int count_paths(int x, int y, int m, int n,int[][] maze){
        if((x == m-1)&&(y == n-1)){
            return 1;
        }
        if((x == m)||(y == n)){
            return 0;
        }
        if(isSafe(maze, x, y)){
            int right = count_paths(x, y+1, m, n, maze);
            int down = count_paths(x, y+1, m, n, maze);
            return right+ down;
        }
        else{
            return -1;
        }
    }
    public static void main(String[] args) {
        int[][] maze = {{0,0,0},{0,1,0},{0,0,0}};
        System.out.println(count_paths(0, 0, 3, 3, maze));
    }
}
