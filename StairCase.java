<<<<<<< HEAD
import java.util.Scanner;

class StairCase{
    public void stairCase(int n){
        for(int i=0;i<n;i++){
            System.out.println("");
            for(int j=n-1;j>i;j--){
                System.out.print(" ");
            }
            for(int k=0;k<=i;k++){
                System.out.print("#");
            }
        }
    }

    public static void main(String[] args) {
        StairCase obj = new StairCase();
        Scanner sc = new Scanner(System.in);
        System.out.print("enter no of rows:");
        int n = sc.nextInt();
        obj.stairCase(n);
        sc.close();
    }
=======
import java.util.Scanner;

public class StairCase{


    public static void main(String[] args) {
        StairCase obj = new StairCase();

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        // System.out.println(n);
    }
>>>>>>> 30e85b513a6a8646a88d68bc5e130043d5a19eee
}