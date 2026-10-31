
from decimal import Decimal, InvalidOperation


def calculate_bill(units: Decimal) -> Decimal:
    """Calculate the electricity bill."""
    if units <= 100:
        rate = Decimal("1.50")
    elif units <= 200:
        rate = Decimal("2.50")
    else:
        rate = Decimal("4.00")

    return units * rate


try:
    units = Decimal(input("Enter electricity units consumed: ").strip())

    if not units.is_finite():
        raise ValueError("Units must be a finite number.")

    if units < 0:
        raise ValueError("Units cannot be negative.")

except (InvalidOperation, ValueError) as error:
    print(f"Invalid input: {error}")

else:
    amount = calculate_bill(units)
    print(f"Units consumed: {units}")
    print(f"Electricity bill: Rs. {amount:.2f}")

finally:
    print("Electricity bill calculation completed.")
