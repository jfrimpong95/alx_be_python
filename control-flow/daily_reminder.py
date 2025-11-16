# daily_reminder.py

# Prompt user for task information
task = input("Enter your task for today: ")
priority = input("Enter the task priority (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = f"Reminder for your task: '{task}'"

# Use match-case to modify the reminder based on priority
match priority:
    case "high":
        reminder += " [High Priority]"
    case "medium":
        reminder += " [Medium Priority]"
    case "low":
        reminder += " [Low Priority]"
    case _:
        reminder += " [Unknown Priority]"

# Use if statement to modify the message if the task i
