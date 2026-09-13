num = input("Enter a number comma separated: ")

num_list = num.split(",")
num_tuple = tuple(num_list)

print("\n Original List:",num_list)
print("\n Original Tuple:",num_tuple)

print("\n ================================================================")

total_num = len(num_list)

print("\n Total number of elements in the list:", total_num)

print("\n ================================================================")

print("\n First element in the list:", num_list[0])
print("\n Last element in the list:", num_list[-1])

print("\n ================================================================")

print("\n Reversed list:", list(reversed(num_list)))

