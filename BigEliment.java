import java.util.Scanner;

public class BigEliment{
    public int bigEliment(int li[]){
       for(int i =0;i<li.length;i++){
           for(int j=i+1;j<li.length;j++){
               if(li[i]<li[j]){
                   int temp = li[i];
                   li[i] = li[j];
                   li[j] = temp;
               }
           }
       }
       return li[0];
    }
    
    public static void main(String[] args) {
        BigEliment obj = new BigEliment();
        Scanner sc = new Scanner(System.in);
        int li[] = new int[5]; 
        System.out.println("enter eliment for list:");
        for(int i=0;i<li.length;i++){
            li[i] = sc.nextInt();
        }
        
        int be = obj.bigEliment(li);
        System.out.println("Bigest eliment from list:"+be);
    }
}