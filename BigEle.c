#include<stdio.h>
#include<conio.h>

int bigElement(int list[],int n){
    int i,j,temp;
    for(i=0;i<=n;i++){
        for (j=i+1;j<=n;j++){
            if(list[i]<list[j]){
                temp = list[i];
                list[i] = list[j];
                list[j] = temp;
            }
        }
    }
    return list[0];
}

int main(int argc, char const *argv[])
{
    int li[100];
    int i,n;
    printf("entre no of elements in array : ");
    scanf("%d",&n);
    printf("Enter values in array!\n");
    for (i=0;i < n;i++){
        scanf("%d",&li[i]);
    }
    // printf("\nsizeof:%d\n",sizeof(li));
    printf("biggest eliment in array is : %d",bigElement(li,n));
    getch();
    printf("\n");
    return 0;
}
