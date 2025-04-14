# Initialize lists
checklist = []
completed_tasks = []
incomplete_tasks = []

# Step 1: Start of the day - create checklist
num_tasks = int(input("How many tasks do you want to add to your checklist today? "))

print("\nEnter your tasks:")
for i in range(num_tasks):
    task = input(f"Task {i+1}: ")
    checklist.append(task)

# Step 2: End of the day - review tasks
print("\nNow let's review your tasks.")
for task in checklist:
    status = input(f"Did you complete this task? '{task}' (yes/no): ").strip().lower()
    if status == 'yes':
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

# Step 3: Show results
print("\n✅ Completed Tasks:")
for task in completed_tasks:
    print(f"- {task}")

print("\n❌ Incomplete Tasks:")
for task in incomplete_tasks:
    print(f"- {task}")