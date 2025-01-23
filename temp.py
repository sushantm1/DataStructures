old_list=[1,2,3,4]
print("The given list is :")
print(old_list)
index=int(input("enter the index to change : "))
final_index=index-1
val=int(input("enter the value : "))
new_length=len(old_list)+1
if index>new_length:
    print("index exceeded.")
else:
    new_list=[1] * new_length
    count,i,j=0,0,0
    print("old ls",old_list)
    while count<(new_length-1):
        if i==final_index:
            # print("1")
            new_list[i]=val
            i+=1
        else:
            # print("2")
            new_list[i]=old_list[j]
            count+=1
            i+=1
            j+=1
    print(new_list)


