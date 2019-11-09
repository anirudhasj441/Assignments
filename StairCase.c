#include<stdio.h>
#include<conio.h>

void stairCase(int n){
    int i,j,k;
    for(i=0;i<n;i++){
        printf("\n");
        for(j=n-1;j>i;j--){
            printf(" ");
        }
        for(k=0;k<=i;k++){
            printf("#");
        }
    }
}

int main(){
    int n;
    printf("enter no of rows:");
    scanf("%d",&n);
    stairCase(n);
}