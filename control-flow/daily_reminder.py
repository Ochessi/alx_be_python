# Prompt user for task details
task = input("Enter your task: ")  # Get task description
priority = input("Priority (high/medium/low): ").lower()  # Get priority level
time_bound = input("Is it time-bound? (yes/no): ").lower()  # Check if time-sensitive

# Process task priority using Match Case (Python 3.10+)
match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task.")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task.")
    case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Invalid priority entered.")

# Modify reminder if the task is time-sensitive
if time_bound == "yes":
    print("That requires immediate attention today!")
else:
    print("You can complete it at your convenience.")    

# Print the reminder
print()
