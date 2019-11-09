import java.util.Scanner;

class MinMaxSum{
    public void minMaxSum(int[] li){
        int min_sum = 0;
        int max_sum = 0;
        for(int i=0;i<li.length;i++){
            for(int j=i;j<li.length;j++){
                if(li[i]>li[j]){
                    int temp = li[i];
                    li[i] = li[j];
                    li[j] = temp;
                }
            }
        }
        for(int i=0;i<li.length-1;i++){
            min_sum += li[i];
        }
        for(int i=1;i<li.length;i++){
            max_sum += li[i];
        }
        System.out.print(min_sum+" ");
        System.out.print(max_sum+" ");
    }

    public static void main(String[] args) {
        MinMaxSum obj = new MinMaxSum();
        Scanner sc = new Scanner(System.in);
        String ar[] = sc.nextLine().split(" ");
        int li[] = new int[ar.length];
        for(int i=0;i<ar.length;i++){
            li[i] = Integer.parseInt(ar[i]);
        }
        obj.minMaxSum(li);
        sc.close();
    }
}