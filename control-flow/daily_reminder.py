#Prompt user to input single task

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

#Process task based on priority and time sensitive
def get_reminder(task, priority, time_bound):
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an unspecified priority level"
    
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". consider completing it when you have free time."

    return reminder

#Provide and generate reminder
reminder_message = get_reminder(task, priority, time_bound)
print(f"Reminder: {reminder}")

