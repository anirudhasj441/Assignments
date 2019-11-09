#include<iostream>
using namespace std;
class UtopianTree{
    public:
    int utopianTree(int n){
        int height = 0;
        for(int i=0;i<=n;i++){
            if(i==0){
                height +=1;
            }
            else if(i%2==0){
                height +=1;
            }
            else{
                height *=2;
            }
        }
        return height;
    }
};

int main(){
    UtopianTree obj = UtopianTree();
    int li[] = {};
    int test_case,i;
    cin>>test_case;
    for(i=0;i<test_case;i++){
        cin>>li[i];
    }
    for(i=0;i<test_case;i++){
        cout<<obj.utopianTree(li[i])<<endl;
    }
    return 0;
}