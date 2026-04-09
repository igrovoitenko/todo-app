def add_task():
    task = input("Введите задачу: ").strip()
    
    if task == "":
        print("Задача не может быть пустой")
        return
    with open("tasks.txt", "a") as file:
        file.write("[ ] " + task + "\n")
    print("Задача добавлена")
    
def show_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        
    if len(tasks) == 0:
        print("Список задач пуст")
        return
    else:
        print("\nВаши Задачи: ")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")
            
def delete_task():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        
    for i, task in enumerate(tasks, start=1):
        print(i, "-", task.strip())
    try:    
        num = int(input("Какую задачу удалить: "))
    except:
        print("Введите число!")
        return
    
    confirm = input("Удалить? (да/нет): ")
    if 1 <= num <= len(tasks):

        if confirm == "да":
            tasks.pop(num - 1)
            print("Удалено")
        else:
            print("Отмена")
                        
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        
def mark_done():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    
    for i, task in enumerate(tasks, start=1):
        print(i, "-", task.strip())
        
    num = int(input("Какую задачу отметить выполненой: "))
    
    if 1 <= num <= len(tasks):
        tasks[num - 1] = tasks[num - 1].replace("[ ]", "[x]")     
    
        with open("tasks.txt", "w") as file:
            file.writelines(tasks) 
    if "[x]" in tasks[num - 1]:        
        print("Задача выполнена")
    else:
        tasks[num - 1] = tasks[num - 1].replace("[ ]", "[x]")
        
def search_task():
    search = input("Что найти: ")
    
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()       
    found = False      
    
    for task in tasks:
        if search in task:
            print("Найдено:", task.strip())
            found = True
    
    if not found:
        print("Ничего не найдено")
   
while True:
    print("\n1 - Добавить задачу")
    print("2 - Показать задачу")
    print("3 - Удалить задачу")
    print("4 - Отметить выполненую задачу")
    print("5 - Найти задачу")
    print("6 - Выход")
    
    choice = input("Выбор: ")
    
    if choice == "1":
        add_task()
        
    elif choice == "2":
        show_tasks()
        
    elif choice == "3":
        delete_task()
        
    elif choice == "4":
        mark_done()
    
    elif choice == "5":
        search_task()
    
    elif choice == "6":
        break