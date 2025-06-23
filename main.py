tasks = []
## Adds new task to list.
def addNewTask():
    print("Add to list:")
    task = input()
    tasks.append(task)

## Deletes task from list based on user number selection. If number doesn't exist then we return an error message.
def deleteTask():
    displayCurrentTasks()
    try:
        if len(tasks) == 0:
            print("Your list is currently empty")
            
        
        elif len(tasks) > 0:
            print("Which task would you like to delete?")
            task = int(input("Select task number: "))
            tasks.pop(task)

        else:
            print(f"Task {task} does not exist.")

    except:
        print("Task does not exist")

## Displays our full list with its listed index.
def displayCurrentTasks():
    if len(tasks) == 0:
        print("Your list is currently empty")
        
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks):
            print(f"{index}. {task}")

if __name__ == "__main__":

    print("To-Do List V1 :")
    while True:
        print("\n Select an option")
        print("--------------------------")
        print("1. Add new task")
        print("2. Delete task")
        print("3. Display list")
        print("4. Quit")

        choice = input("Select an option \n")

        if(choice == "1"):
            addNewTask()

        elif(choice == "2"):
            deleteTask()

        elif(choice == "3"):
            displayCurrentTasks()

        elif(choice == "4"):
            print("Till next time.")
            False

        else:
            print("Invalid selection. Please choose again")
            

