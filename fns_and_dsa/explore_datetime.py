from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)


def calculate_future_date(days):
    """Calculates and displays the future date after adding a number of days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future Date:", formatted_future)


# ---------------- Main Program -----------------

def main():
    print("Exploring Python datetime Module\n")

    # Part 1: Show current date & time
    display_current_datetime()

    # Part 2: Future date calculation
    try:
        number_of_days = int(input("Enter the number of days to add: "))
        calculate_future_date(number_of_days)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
