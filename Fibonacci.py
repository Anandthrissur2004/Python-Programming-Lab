#Program to Fibonacci Series
a=0 
b=1 
i=0

num = int(input("Enter till number: "))

print("\nFibonacci Series: ")
while(i<num):
    print(" ",a)
    c = a+b
    a = b
    b = c
    i= i+1


