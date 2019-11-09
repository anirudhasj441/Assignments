#include<stdio.h>
#include<conio.h>

int utopianTree(int n){
    int height,i;
    height = 0;
    for(i=0;i<=n;i++) {
        if (i==0){
            height +=1;
        }
        else if (i%2==0){
            height +=1;
        }
        else{
            height *= 2;
        }
    }
    return height;
}

int main(){
    int test_case,i;
    int li[100];
    scanf("%d",&test_case);
    for(i=0;i<test_case;i++){
        scanf("%d",&li[i]);
    }
    for(i=0;i<test_case;i++){
        printf("%d\n",utopianTree(li[i]));
    }
    return 0;
}