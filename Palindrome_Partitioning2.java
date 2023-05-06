public class Palindrome_Partitioning2 {
    public static int[][] t=new int[2001][2001];
    public static boolean isPalindrome(String s,int i,int j){
        while(i<=j){
            if(s.charAt(i)!=s.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    public static int solve(String s, int i,int j){
        if(i>=j || isPalindrome(s,i,j)){
            return 0;
        }
        if(t[i][j]!=-1){
            return t[i][j];
        }
        int mn=Integer.MAX_VALUE;
        for(int k=i;k<=j-1;k++){
            //int tempans=1+solve(s, i, k)+solve(s, k+1, j);
            //left partitio
            if(isPalindrome(s, i, k)){
                int tempans=1+solve(s,k+1, j);
                mn=Math.min(tempans,mn);
            }
        }
        return t[i][j]=mn;
    }
    public static void main(String[] args) {
        String s="nitik";
        for(int i=0;i<=s.length();i++){
            for(int j=0;j<=s.length();j++){
                t[i][j]=-1;
            }
        }
        System.out.println(solve(s,0,s.length()-1));
    }
}
