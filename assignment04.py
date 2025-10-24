class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def edit(self, new_description, new_priority):
        self.description = new_description
        self.priority = new_priority

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{status}] {self.description} (Priority: {self.priority})"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)
        print("Task added successfully!")

    def edit_task(self, index, new_description, new_priority):
        if 0 <= index < len(self.tasks):
            self.tasks[index].edit(new_description, new_priority)
            print("Task updated successfully!")
        else:
            print("Invalid task number!")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid task number!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task}")

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Mark Task as Completed")
    print("4. View Tasks")
    print("5. Exit")

def main():
    todo = ToDoList()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            desc = input("Enter task description: ")
            priority = input("Enter priority (High/Medium/Low): ")
            todo.add_task(desc, priority)

        elif choice == '2':
            try:
                index = int(input("Enter task number to edit: "))
                new_desc = input("Enter new description: ")
                new_priority = input("Enter new priority (High/Medium/Low): ")
                todo.edit_task(index, new_desc, new_priority)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            try:
                index = int(input("Enter task number to mark completed: "))
                todo.mark_task_completed(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            todo.view_tasks()

        elif choice == '5':
            print("Exiting... Have a productive day!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
