def add_task():
    task = input("Enter your task: ")
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print("✅ Task added successfully!\n")

def show_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            if not tasks:
                print("📭 No tasks yet.\n")
            else:
                print("\n📝 Your Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
                print()
    except FileNotFoundError:
        print("📂 No task file found. Add a task to create one.\n")

def main():
    while True:
        print("📋 To-Do List Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
