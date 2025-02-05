# program to use stack properties
arrSize=int(input("Enter the size of the stack: "))
arr=[]*arrSize
top=-1

def push(num):
    if len(arr)==arrSize:
        print("Stack is full")
        return
    arr.append(num)
    top+=1
    print("Pushed element is: ",num)

def pop():
    if len(arr)==0:
        print("Stack is empty")
    else:
        print("Popped element is: ",arr.pop())
        top-=1

    # else:
    #     print("Stack is not full")

def peek():
    print("the peek element is :",arr[top])
    
def underflow():
    if len(arr)==0:
        print("Stack is empty")
    else:
        print("Stack is not empty")

exit=False
while True:
    if exit==True:
        break
    print("what do you want to do with the stack? ")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4, Peek")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        num=int(input("Enter the number to push: "))
        push(num)
    elif choice==2:
        pop()
    elif choice==3:
        print("Stack is: ",arr)
    elif choice==4:
        peek()
    elif choice==5:
        exit=True
    else:
        print("Invalid choice")
    
