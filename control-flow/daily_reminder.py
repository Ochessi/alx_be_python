task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        reminder = f"{task} is a high priority task."
    case "medium":
        reminder = f"{task} is a medium priority task."
    case "low":
        reminder = f"{task} is a low priority task."
    case _:
        reminder = "Invalid priority entered!"

if time_bound == "yes":
    reminder += " It is also time-bound."
else:
    reminder += " Finish it when you can."

print(reminder)                            