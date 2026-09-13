from collections import Counter

dic1 = {'Ameesha': 90, 'Riya': 80, 'Sanya': 70, 'Kriti': 60, 'Alia': 50}

print("\n Original Dictionary:", dic1)

#sort list by values
print("\n Sort list by keys:", sorted(dic1.items()))

#merge two dictionaries
dic2 = {'Aarav': 85, 'Vivaan': 75, 'Aditya': 65}
print("\n ================================================================")
print("\n Original Dictionary 1:", dic1)
print("\n Original Dictionary 2:", dic2)
print("\n Merge two dictionaries:", {**dic1, **dic2})

print("\n ================================================================")
#frequency counting of words in a string
print("\n Frequency counting of words in a string:")
fruits = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
freq = Counter(fruits)
print("\n Frequency of each word:", freq)

print("\n ================================================================")
#identifying the most common and unique elements in a list
print("\n Identifying the most common and unique elements in a list:")
set_1 = [1, 2, 3, 4, 5, 1, 2, 3, 1]
set_2 = [1, 2, 3, 4, 5, 6, 7, 8]

print("\n Set 1:", set_1)
print("\n Set 2:", set_2)

common = set(set_1) & set(set_2)
unique = set(set_1) ^ set(set_2)

print("\n Common elements:", common)
print("\n Unique elements:", unique)
