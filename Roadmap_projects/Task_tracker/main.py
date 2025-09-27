import json
from json import JSONDecodeError
import os

# todo:
# 1. functions:
#       - create task
#       - modify task
#       - delete task
#       - change status for task

# 2. json payload: - name of task, deadline, status, notes

def create_task():

    try:
        name = str(input("Enter the name of the taks: ")).capitalize()
        due_date = str(input("Enter the due date: (format: YY:MM:DD)"))
        note = str(input("Enter notes for the task:")).capitalize()

        new_entry = {
            "name": name,
            "due_date": due_date,
            "note": note,
            "status": "New"
        }

        tasks = []

        if os.path.exists("task_db.json") and os.path.getsize("task_db.json") > 0:
            with open('task_db.json', 'r', encoding='utf-8') as f_in:
                try:
                    tasks = json.load(f_in)
                except JSONDecodeError:
                    tasks = []
        
        tasks.append(new_entry)

        with open('task_db.json', 'w', encoding='utf-8') as f_out:
            json.dump(tasks, f_out, indent=4, ensure_ascii=False)

        print("New task successfully saved.")

    except Exception as e:
        print(f"Save task unsuccessful. Error: {e}")

def modify_task():
    
    try:
        modify_task = str(input("Select task by name: ")).lower().strip()

        tasks = []

        if os.path.exists('task_db.json') or os.path.getsize(task_db.json) > 0:
            with open('task_db.json', 'r', encoding='utf-8') as f_in:
                try:
                    tasks = json.load(f_in)
                except JSONDecodeError:
                    tasks = 0

        task = None
        for item in tasks:
            if str(item.get("name", "")).strip().lower() == modify_task:
                task = item
                break
            
        if task.get('name') == modify_task:
            print(f"Name: {task.get('name')}")
            print(f"DueDate: {task.get('due_date')}")
            print(f"Note: {task.get('note')}")
            print(f"Status: {task.get('status')}")

        print("\n")
        print("Select what you wish to modify:")
        print("1. Name")
        print("2. Due date")
        print("3. Note")
        print("4. Status")
        print("Type 'skip' to cancel modification.")
        print("\n")
        to_modify = str(input("select a property you wish to change (1, 2, 3, 4): ")).lower().strip()

        if to_modify not in ['1', '2', '3', '4', 'skip']:
            print("Invalid entry.")
            return

        if to_modify == 'skip':
            return

        match to_modify:
            case '1':
                new_name = str(input("Enter new name: ")).capitalize()
                task['name'] = new_name
            case '2':
                new_duedate = str(input("Enter new due date: "))
                task['due_date'] = new_duedate
            case '3':
                new_note = str(input("Enter new note. "))
                task['note'] = new_note
            case '4':
                new_status = str(input("Enter new status: "))
                task['status'] = new_status

        with open('task_db.json', 'w', encoding='utf-8') as f_out:
            json.dump(tasks, f_out, indent=4, ensure_ascii=False)
    
    except Exception as e:
        print(f"{e}")

def change_status_to_done():

    try:
        selected_task = str(input("Select task by name: ")).strip().lower()

        tasks = []

        if os.path.exists('task_db.json') and os.path.getsize('task_db.json') > 0:
            with open('task_db.json', 'r', encoding='utf-8') as f_in:
                try:
                    tasks = json.load(f_in)
                except JSONDecodeError:
                    tasks = []

        for task in tasks:
            if task['name'].strip().lower() == selected_task:
                task['status'] = 'DONE'

        with open('task_db.json', 'w', encoding='utf-8') as f_out:
            json.dump(tasks, f_out, indent=4, ensure_ascii=False)
        
    except Exception as e:
        print(f"Error: {e}")
    

def delete_task():
    pass



def main():
    
    print("***** Task Tracker Application *****")
    application_on = True
    
    while application_on:
        print("Select an action you wish to perform:")
        print("1. Add new task")
        print("2. Modify task")
        print("3. Change status of task")
        print("4. Delete task")
        print("To exit the application, type 'exit'.")

        #  list currently recorded tasks
        print('\n')
        print("Currently recorded tasks: ")
        with open('task_db.json', 'r') as f:
            if os.path.getsize('task_db.json') == 0:
                print("There is currently no tasks recorded in the application.")
                all_tasks = []
            else:
                all_tasks = json.load(f)
                for idx, task in enumerate(all_tasks, start=1):
                    task_name = task.get('name')
                    status = task.get('status')
                    print(f"{idx}. {task_name} - {status}")


        action = str(input("Action (Select 1, 2, 3, 4): ")).lower()


        if (action) == 'exit':
            print("Goodbye!")
            break

        match action:
            case "1":
                create_task()
            case "2":
                modify_task()
            case "3":
                change_status_to_done()
            case "4":
                delete_task()



if __name__ == '__main__':
    main()