
large = 0

for i in range(3):
    print("Enter number ", i+1, ":")
    num = int(input())
    if(num > large):
        large = num

print("The largest number is:", large)