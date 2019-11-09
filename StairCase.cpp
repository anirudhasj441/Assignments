#include<iostream>
using namespace std;
class StairCase{
    public:
    void stairCase(int n){
        for(int i=0;i<n;i++){
            printf("\n");
            for(int j=n-1;j>i;j--){
                printf(" ");
            }
            for(int k=0;k<=i;k++){
                printf("#");
            }
        }
    }
};

int main(){
    int n;
    StairCase obj = StairCase();
    printf("enter no of rows:");
    scanf("%d",&n);
    obj.stairCase(n);
}