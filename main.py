from tasks import add_task, view_tasks, complete_task, delete_task

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Title: ")
        desc = input("Description: ")
        add_task(title, desc)

    elif choice == "2":
        tasks = view_tasks()
        for t in tasks:
            print(t)

    elif choice == "3":
        task_id = int(input("Task ID: "))
        complete_task(task_id)

    elif choice == "4":
        task_id = int(input("Task ID: "))
        delete_task(task_id)

    elif choice == "5":
        break
