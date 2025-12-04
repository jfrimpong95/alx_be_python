def safe_divide(numerator, denominator):
    """Safely divide two numbers, handling errors."""

    # Convert inputs to numbers
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Non-numeric input."

    # Perform division safely
    try:
        result = num / den
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def safe_divide(numerator, denominator):
    """Safely divide two numbers, handling errors."""

    # Convert inputs to numeric values
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    # Perform the division
    try:
        result = num / den
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
