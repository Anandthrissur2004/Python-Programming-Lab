file_name = "library.txt"

# Create the file if it does not exist yet.
with open(file_name, "a"):
    pass

while True:
    print("\n1. Add a new book")
    print("2. Search for a book")
    print("3. Generate a report")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        with open(file_name, "r") as file:
            book_id = "B" + str(sum(1 for line in file) + 1).zfill(3)
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        with open(file_name, "a") as file:
            file.write(book_id + "," + title + "," + author + "\n")
        print("Book", book_id, "added successfully.")

    elif choice == "2":
        search = input("Enter a title or author to search: ").lower()
        found = False

        with open(file_name, "r") as file:
            for line in file:
                book_id, title, author = line.strip().split(",", 2)
                if search in title.lower() or search in author.lower():
                    print("ID:", book_id, "Title:", title, "Author:", author)
                    found = True

        if not found:
            print("Book not found.")

    elif choice == "3":
        with open(file_name, "r") as file:
            books = [line.strip().split(",", 2) for line in file]

        print("Total number of books:", len(books))
        author_name = input("Enter an author's name: ").lower()
        author_count = 0

        for book_id, title, author in books:
            if author.lower() == author_name:
                print("ID:", book_id, "Title:", title, "Author:", author)
                author_count += 1

        print("Books by this author:", author_count)

    elif choice == "4":
        print("Goodbye.")
        break

    else:
        print("Invalid choice")
