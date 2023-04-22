public class tribonacci {
    public static int[]t=new int[31];
    public static int tribo(int n){
        if(n==0){
            return t[n]=0;
        }
        if(n==1){
            return t[n]=1;
        }
        if(n==2){
            return t[n]=1;
        }
        if(t[n]!=-1){
            return t[n];
        }
        return t[n]=tribo(n-1)+tribo(n-2)+tribo(n-3);
    }
}
