public class house_robber {
    public static int[] t=new int[101];
    public static int robbing(int[] arr,int i,int n){
        if(i>n-1){
            return t[i]=0;
        }
        if(i==n-1){
            return t[i]=arr[i];
        }
        if(t[i]!=-1){
            return t[i];
        }
        return t[i]=Math.max(arr[i]+robbing(arr, i+2, n),arr[i+1]+robbing(arr, i+3, n));
    }
    public static void main(String[] args) {
        int[] arr={1,2,3,1};
        //int[] arr={2,7,9,3,1};
        int n=arr.length;
        for(int i=0;i<n+1;i++){
            t[i]=-1;
        }
        System.out.println(robbing(arr,0,n));
    }
}
