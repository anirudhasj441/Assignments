import java.util.Scanner;

public class UtopianTree{
    public int utopianTree (int n){
        int height = 0;
        for (int i=0;i<=n;i++){
            if (i == 0){
                height += 1;
            }
            else if (i%2==0){
                height += 1;
            }
            else{
                height *=2;
            }
        }
        return(height);
    }

    public static void main(String[] args) {
        UtopianTree obj = new UtopianTree();
        Scanner sc = new Scanner(System.in);
        int test_case = sc.nextInt();
        int[] li= new int[test_case];
        for (int i =0;i<test_case;i++) {
            li[i] = sc.nextInt(); 
        }
        for (int i=0;i<test_case;i++){
            System.out.println(obj.utopianTree(li[i]));
        }
        sc.close();
    }
}