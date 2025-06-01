# Prompt user for task details
task = input("Enter your task: ")  # Get task description
priority = input("Priority (high/medium/low): ").lower()  # Get priority level
time_bound = input("Is it time-bound? (yes/no): ").lower()  # Check if time-sensitive

# Process task priority using Match Case (Python 3.10+)
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority entered."

# Modify reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " That requires immediate attention today!"

# Print the reminder
print(reminder)
