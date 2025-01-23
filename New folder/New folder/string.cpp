#include <iostream>
using namespace std;
int main(){
    char s[25];
    // int a;
    cin>>s;
    int count=0;
    for(int i=0;s[i]!='\0';i++){
        count++;
    }
    cout<<count;
    // printf("%d",count);

    return 0;
}