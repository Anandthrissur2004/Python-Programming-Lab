word = str(input("Enter a word: "))

print("\n 1. Character Replacement")
print(" 2. String Reversal")
print(" 3. String Palindrome")
print(" 4. Character Frequency")
print(" 5. Word Frequency")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        char = str(input("Enter character to replace: "))
        new_char = str(input("Enter new character: "))
        print(word.replace(char, new_char))

    case 2:
        print(word[::-1])

    case 3:
        if word == word[::-1]:
            print(word, "is a palindrome")
        else:
            print(word, "is not a palindrome")

    case 4:
        char = str(input("Enter character to find frequency: "))
        print("Frequency of", char, "is:", word.count(char))

    case 5:
        word_to_find = str(input("Enter word to find frequency: "))
        print("Frequency of", word_to_find, "is:", word.count(word_to_find))

    case _:
        print("Invalid choice")
