# Import Decimal for accurate decimal calculations
# Import InvalidOperation to handle invalid decimal input
from decimal import Decimal, InvalidOperation


# Function to calculate the electricity bill
def calculate_bill(units: Decimal) -> Decimal:

    # Docstring describing the function
    """Calculate the electricity bill."""

    # Check if units are less than or equal to 100
    if units <= 100:
        rate = Decimal("1.50")  # Rs. 1.50 per unit

    # Check if units are less than or equal to 200
    elif units <= 200:
        rate = Decimal("2.50")  # Rs. 2.50 per unit

    # If units are greater than 200
    else:
        rate = Decimal("4.00")  # Rs. 4.00 per unit

    # Calculate and return the total bill
    return units * rate


# Start exception handling
try:

    # Get electricity units from the user
    # strip() removes extra spaces
    units = Decimal(input("Enter electricity units consumed: ").strip())

    # Check whether the input is a finite number
    if not units.is_finite():
        raise ValueError("Units must be a finite number.")

    # Check whether units are negative
    if units < 0:
        raise ValueError("Units cannot be negative.")

# Handle invalid decimal input and value errors
except (InvalidOperation, ValueError) as error:

    # Display the error message
    print(f"Invalid input: {error}")

# Execute this block if no exception occurs
else:

    # Call the function to calculate the bill
    amount = calculate_bill(units)

    # Display electricity units consumed
    print(f"Units consumed: {units}")

    # Display the bill amount with two decimal places
    print(f"Electricity bill: Rs. {amount:.2f}")

# Execute this block whether an error occurs or not
finally:

    # Display completion message
    print("Electricity bill calculation completed.")
