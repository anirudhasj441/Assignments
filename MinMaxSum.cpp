#include<iostream>
using namespace std;
class MinMaxSum{
    public:
    int min_sum = 0;
    int max_sum = 0;
    void minMaxSum(int li[]){
        for(int i=0;i<5;i++){
            for(int j=i;j<5;j++){
                if(li[i]>li[j]){
                    int temp = li[i];
                    li[i] = li[j];
                    li[j] = temp;
                }
            }
        }
        for(int i=0;i<4;i++){
            min_sum += li[i];
        }
        for(int i=1;i<5;i++){
            max_sum += li[i];
        }
        printf("%d ",min_sum);
        printf("%d ",max_sum);
    }
};

int main(){
    MinMaxSum obj = MinMaxSum();
    int li[100];
    for(int i=0;i<5;i++){
        scanf("%d",&li[i]);
    }
    obj.minMaxSum(li);
}