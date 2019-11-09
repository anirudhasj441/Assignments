import java.util.Map;
import java.util.Scanner;

public class AngryMaster{
    public String angryMaster(int k,int a[]){
        int on_time = 0;
        for (int i=0;i<a.length;i++){
            if (a[i]<=0){
                on_time +=1;
            }
        }
        if(on_time>=k){
            return("NO");
        }
        else{
            return("YES");
        }
    }

    public static void main(String[] args) {
        AngryMaster obj = new AngryMaster();
        Scanner sc = new Scanner(System.in);
        Scanner sc1 = new Scanner(System.in);
        int test_case = sc.nextInt();
        
        for(int i=0;i<test_case;i++){
            String[] nk = sc1.nextLine().split(" ");
            int n = Integer.parseInt(nk[0]);
            int k = Integer.parseInt(nk[1]);
            int[] a = new int[n];
            String[] li = sc1.nextLine().split(" ");
            for(int j=0;j<li.length;j++){
                a[j] = Integer.parseInt(li[j]);
            }
            System.out.println(obj.angryMaster(k, a));
        }
        sc.close();
        sc1.close();
    }
}