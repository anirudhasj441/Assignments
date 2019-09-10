import java.util.Scanner;

public class Main {
    public int subString(String s) {
        int c = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                s.substring(i, j);
                c++;
            }
        }
        return (c);
    }

    public static void main(String[] args) {
        java.util.Scanner sc = new Scanner(System.in);
        
        System.out.print("enter a string:");
        String str = sc.nextLine();

        Main obj = new Main();

        int res = obj.subString(str);

        System.out.println(res);
    }
}