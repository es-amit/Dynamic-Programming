public class min_cost_climbing {
    public static int[] t=new int[1000];
    public static int stairs(int[] arr,int n){
        if(n<0){
            return t[n]= 0;
        }
        if(n==1||n==0){
            return t[n]=0;
        }
        if(t[n]!=-1){
            return t[n];
        }
        return t[n]=Math.min(arr[n-1]+stairs(arr, n-1),arr[n-2]+ stairs(arr, n-2));

    }
    
    public static void main(String[] args) {
        //int [] arr={10,15,20};
        int[] arr={1,100,1,1,1,100,1,1,100,1};
        for(int i=0;i<arr.length+1;i++){
            t[i]=-1;
        }
        System.out.println(stairs(arr, arr.length));
    }
}
