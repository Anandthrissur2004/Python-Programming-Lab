# Import the regular expression module
import re

# Get email address from the user
email = input("Enter your email address: ")

# Get phone number from the user
phone_number = input("Enter your phone number: ")

# Get log text from the user
log_text = input("Enter log text: ")


# Define the regular expression pattern for email validation
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

# Check whether the complete email matches the pattern
if re.fullmatch(email_pattern, email):

    # Display if email is valid
    print("Valid email address")
else:

    # Display if email is invalid
    print("Invalid email address")


# Check whether the phone number contains exactly 10 digits
if re.fullmatch(r"[0-9]{10}", phone_number):

    # Display if phone number is valid
    print("Valid phone number")
else:

    # Display if phone number is invalid
    print("Invalid phone number")


# Find all transaction IDs from the log text
transaction_ids = re.findall(

    # Pattern to identify transaction IDs
    r"\btransaction[\s_-]*id\s*[:=]\s*([A-Za-z0-9_-]+)",

    # Text in which transaction IDs are searched
    log_text,

    # Ignore uppercase and lowercase differences
    flags=re.IGNORECASE,
)

# Check whether any transaction IDs are found
if transaction_ids:

    # Display all extracted transaction IDs separated by commas
    print("Transaction IDs:", ", ".join(transaction_ids))
else:

    # Display message if no transaction IDs are found
    print("No transaction IDs found")
