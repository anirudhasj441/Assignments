#include<stdio.h>
#include<conio.h>
void minMaxSum(int li[]){
    int i,j,min_sum,max_sum,temp;
    min_sum = 0;
    max_sum = 0;
    for(i=0;i<5;i++){
        for(j=i;j<5;j++){
            if(li[i]>li[j]){
                temp = li[i];
                li[i] = li[j];
                li[j] = temp;
            }
        }
    }
    for(i=0;i<5-1;i++){
        min_sum += li[i];
    }
    for(i=1;i<5;i++){
        max_sum += li[i];
    }
    printf("%d ",min_sum);
    printf("%d ",max_sum);
}

int main(){
    int i;
    int arr[100];
    for(i=0;i<5;i++){
        scanf("%d",&arr[i]);
    }
    minMaxSum(arr);
}