def sum(x):
    if(x==1):
        return 1
    else:
        return (x+sum(x-1))
x=int(input("Enter number"))
print("Sum of",x,"Natural numbers=",sum(x))

sum(x)