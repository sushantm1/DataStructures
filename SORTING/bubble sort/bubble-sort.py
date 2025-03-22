def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[56,23,45,78,12,34,67,89,90]
print("Sorted array is: ",bubble_sort(arr)) 


