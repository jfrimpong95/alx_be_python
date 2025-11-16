# daily_reminder.py

# Prompt user for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder = f"'{task}'"

# Use match-case to process priority
match priority:
    case "high":
        reminder += " is a high priority task"
    case "medium":
        reminder += " is a medium priority task"
    case "low":
        reminder += " is a low priority task"
    case _:
        reminder += " has an unknown priority level"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", reminder)
print\s*\(\s*f?['\"]Reminder:\s*

