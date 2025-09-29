import json
from json import JSONDecodeError
import os
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')



def create_task():

    try:
        description = str(input("Enter description for the task:")).capitalize()

        tasks = []

        if os.path.exists("task_db.json") and os.path.getsize("task_db.json") > 0:
            with open('task_db.json', 'r', encoding='utf-8') as f_in:
                try:
                    tasks = json.load(f_in)
                except JSONDecodeError:
                    tasks = []

        new_entry = {
            "id": len(tasks) + 1,
            "description": description,
            "status": "New",
            "created_at": today,
            "updated_at": today,
        }
        
        tasks.append(new_entry)

        with open('task_db.json', 'w', encoding='utf-8') as f_out:
            json.dump(tasks, f_out, indent=4, ensure_ascii=False)

        print("New task successfully saved.")

    except Exception as e:
        print(f"Save task unsuccessful. Error: {e}")



def modify_task():
    
    try:
        modify_task = str(input("Select task by id: ")).lower().strip()

        tasks = []

        if os.path.exists('task_db.json') or os.path.getsize('task_db.json') > 0:
            with open('task_db.json', 'r', encoding='utf-8') as f_in:
                try:
                    tasks = json.load(f_in)
                except JSONDecodeError:
                    tasks = 0

        task = None
        for item in tasks:
            if str(item.get("id", "")).strip().lower() == modify_task:
                task = item
                break
            
        if task.get('id') == modify_task:
            print(f"id: {task.get('id')}")
            print(f"Description: {task.get('description')}")
            print(f"Status: {task.get('status')}")
            print(f"Created at: {task.get('created_at')}")

        print("\n")
        print("Select what you wish to modify:")
        print("1. Description")
        print("2. Status (In progress)")
        print("Type 'skip' to cancel modification.")
        print("\n")
        to_modify = str(input("select a property you wish to change (1, 2): ")).lower().strip()

        if to_modify not in ['1', '2', 'skip']:
            print("Invalid entry.")
            return

        if to_modify == 'skip':
            return

        match to_modify:
            case '1':
                new_description = str(input("Enter new description: ")).capitalize()
                task['description'] = new_description
                task['updated_at'] = today
            case '2':
                task['status'] = "In progress"
                task['updated_at'] = today


        with open('task_db.json', 'w', encoding='utf-8') as f_out:
            json.dump(tasks, f_out, indent=4, ensure_ascii=False)
    
    except Exception as e:
        print(f"{e}")



def change_status_to_done():

    try:
        selected_task = str(input("Select task by id: ")).strip().lower()

        tasks = []

        if os.path.exists('task_db.json') and os.path.getsize('task_db.json') > 0:
            with open('task_db.json', 'r', encoding='utf-8') as f_in:
                try:
                    tasks = json.load(f_in)
                except JSONDecodeError:
                    tasks = []

        for task in tasks:
            if task['id'].strip().lower() == selected_task:
                task['status'] = 'DONE'

        with open('task_db.json', 'w', encoding='utf-8') as f_out:
            json.dump(tasks, f_out, indent=4, ensure_ascii=False)
        
    except Exception as e:
        print(f"Error: {e}")
    

def delete_task():
    
    try:
        tasks = []

        if os.path.exists('task_db.json') and os.path.getsize('task_db.json') > 0:
            with open('task_db.json', 'r', encoding='utf-8') as f_in:
                try:
                    tasks = json.load(f_in)
                except JSONDecodeError:
                    tasks = []
        
        delete_task = str(input("Select which task you wish to delete (by id): ")).strip().lower()

        for task in tasks:
            if task['id'] == delete_task:
                tasks.remove(task)

        with open('task_db.json', 'w', encoding='utf-8') as f_out:
            json.dump(tasks, f_out, indent=4, ensure_ascii=False)
        
    except Exception as e:
        print("Error during the deletion of tasks.")



def list_tasks(status: list):

    tasks = []
    
    if os.path.exists('task_db.json') and os.path.getsize('task_db.json') > 0:
        with open('task_db.json', 'r', encoding='utf-8') as f_in:
            try:
                tasks = json.load(f_in)
            except JSONDecodeError:
                tasks = []
                print("There is no record in the db list.")


    for task in tasks:
        if task['status'] == status:
            print(f"id: {task.get('id')}")
            print(f"Description: {task.get('description')}")
            print(f"Status: {task.get('status')}")
            print(f"Created at: {task.get('created_at')}")


def list_not_done():
    pass


def list_in_progress():
    pass



def main():
    
    print("***** Task Tracker Application *****")
    application_on = True
    
    while application_on:
        print("Select an action you wish to perform:")
        print("1. Add new task")
        print("2. Modify Description / Set task to In progress.")
        print("3. Mark as Done.")
        print("4. Delete task")
        print("5. List all tasks")
        print("6. List all Done tasks.")
        print("7. List all Not Done tasks")
        print("8. List all tasks that are In Progress")
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
                for task in all_tasks:
                    task_id = task['id']
                    status = task['status']
                    description = task['description']
                    print(f"{task_id} - {description} - {status}")


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
            case "5":
                list_tasks()
            case "6":
                list_tasks("done")
            case "7":
                list_tasks("in progress")
            case "8":
                list_tasks("in progress")



if __name__ == '__main__':
    main()