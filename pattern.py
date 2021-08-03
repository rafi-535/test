def pattern():# Defining a function
    row=int(input("Enter The Number:"))#Giving Input value
    for i in range(1,row+1):#outer loop is to  assign number of * to print
        for j in range(i):#inner loop is to print *
            print('*', end="")# Print stars in one line
        print(i)# to print in a next line
pattern()#function call
