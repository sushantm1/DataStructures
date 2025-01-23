#include<stdio.h>
int main(){
    int arr[]={1,2,3,4,5};
    int val=0;
    int size=sizeof(arr)/sizeof(arr[0]);
    printf("the current array is. ");
    for(int i=0;i<size;i++){
        printf("%d, ",arr[i]);
    } 
    printf("\nplease enter the value = ");
    int index=0;
    scanf("%d",&val);
    for(int i=0;i<size;i++){
        if(arr[i]==val){
            // index=i;
            for(int j=i;j<size;j++){
                arr[j]=arr[j+1];
            }
            break;
        }
    }
    printf("the new array is. ");
    arr[size--];
    for(int i=0;i<size;i++){
        printf("%d, ",arr[i]);
    } 
    return 0;
}