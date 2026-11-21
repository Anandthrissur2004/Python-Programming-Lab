# File name to store book details
file_name = "library.txt"

# Create the file if it does not exist
with open(file_name, "a"):
    pass

# Repeat the menu until the user chooses Exit
while True:

    # Display the menu options
    print("\n1. Add a new book")
    print("2. Search for a book")
    print("3. Generate a report")
    print("4. Exit")

    # Get the user's choice
    choice = input("Enter your choice: ")

    # Option 1: Add a new book
    if choice == "1":

        # Read the file and generate a unique book ID
        with open(file_name, "r") as file:
            book_id = "B" + str(sum(1 for line in file) + 1).zfill(3)

        # Get book details from the user
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        # Open the file in append mode to save book details
        with open(file_name, "a") as file:
            file.write(book_id + "," + title + "," + author + "\n")

        # Display success message
        print("Book", book_id, "added successfully.")

    # Option 2: Search for a book
    elif choice == "2":

        # Get the title or author name to search
        search = input("Enter a title or author to search: ").lower()

        # Initially, assume the book is not found
        found = False

        # Open the file in read mode
        with open(file_name, "r") as file:

            # Read each line from the file
            for line in file:

                # Split the line into ID, title and author
                book_id, title, author = line.strip().split(",", 2)

                # Check whether the search text matches the title or author
                if search in title.lower() or search in author.lower():

                    # Display the matching book details
                    print("ID:", book_id, "Title:", title, "Author:", author)

                    # Mark the book as found
                    found = True

        # Display message if no matching book is found
        if not found:
            print("Book not found.")

    # Option 3: Generate a report
    elif choice == "3":

        # Open the file in read mode
        with open(file_name, "r") as file:

            # Read all book details and store them in a list
            books = [line.strip().split(",", 2) for line in file]

        # Display the total number of books
        print("Total number of books:", len(books))

        # Get the author's name to generate the report
        author_name = input("Enter an author's name: ").lower()

        # Initialize the author's book count
        author_count = 0

        # Check each book in the list
        for book_id, title, author in books:

            # Compare the author name with the entered name
            if author.lower() == author_name:

                # Display the book details
                print("ID:", book_id, "Title:", title, "Author:", author)

                # Increase the count by one
                author_count += 1

        # Display the total books written by this author
        print("Books by this author:", author_count)

    # Option 4: Exit the program
    elif choice == "4":

        # Display goodbye message
        print("Goodbye.")

        # Stop the loop and terminate the program
        break

    # Handle invalid menu choices
    else:

        # Display error message
        print("Invalid choice")
