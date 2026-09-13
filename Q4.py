num = int(input("Enter number: "))
count = 0

if num < 2:
    print(num, "is not prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            count = count + 1

    if count == 0:
        print(num, "is prime number")
    else:
        print(num, "is not prime number")