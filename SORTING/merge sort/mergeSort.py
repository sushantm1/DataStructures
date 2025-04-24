def merge(arr,start,mid,end):
    i=start
    j=mid+1
   
    newArr=[]
    while i<=mid and j<=end:
        if arr[i]<arr[j]:
            newArr.append(arr[i])
            i+=1
        else:
            newArr.append(arr[j])
            j+=1
    while i<=mid:
        newArr.append(arr[i])
        i+=1
    while j<=end:
        newArr.append(arr[j])
        j+=1
    for i in range(len(newArr)):
        arr[start+i]=newArr[i]

def divide(arr,start,end):
    if start<end:
        mid=(start+end)//2
        divide(arr,start,mid)
        divide(arr,mid+1,end)
        merge(arr,start,mid,end)
    #return arr

arr=[5334,65,64,64,88,21]
length=len(arr)
divide(arr,0,length-1)
print(arr)