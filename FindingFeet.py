from array import * #Importing array module
def FindingFeet(): #Defining a func

    n=int(input("Enter The Number Of Elements:"))
    arr=array('i',[])
    for i in range(0,n): #To insert an array elements

        x=int(input("Enter The Element:"))
        arr.append(x) #add element to the end of list

    print("The Elements of array")
    for e in arr:
        print(e,end=' ') # print all the elements of array
    print()
    sum=0 # initializing the value of sum
    for j in range(0,len(arr)): # Loop runs till the length of array
        if arr[j]>=12: #if condition satisfies executes
            feet=arr[j]//12 # Floor division is done
            sum=feet+sum #It get added after every iteration
    print("The Total Sum in Feet is:",sum)


FindingFeet()