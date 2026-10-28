import re

email = input("Enter your email address: ")
phone_number = input("Enter your phone number: ")
log_text = input("Enter log text: ")

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
if re.fullmatch(email_pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")

if re.fullmatch(r"[0-9]{10}", phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")

transaction_ids = re.findall(
    r"\btransaction[\s_-]*id\s*[:=]\s*([A-Za-z0-9_-]+)",
    log_text,
    flags=re.IGNORECASE, 
)
if transaction_ids:
    print("Transaction IDs:", ", ".join(transaction_ids))
else:
    print("No transaction IDs found")