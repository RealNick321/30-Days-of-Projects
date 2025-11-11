import string
import dataclasses
to_do_list = []

def main():
    quit = False
    
    while quit == False:
        command = str.upper(input("What is your desire? "))
        if command == "HELP":
            print("I'm sorry you're having trouble. There are five commands you can give. 1. Add Task_Name_Here 2. Remove Task_Name_Here 3. Done Task_Name_Here 4. List All 5. Quit")
            print("#2 removes the task completely. #3 will keep task on to do list but cross it out. #4 will list all tasks on to-do list. #5 will quit program")
        command = command.split(" ")
        if command[0] == "ADD":
            add_task(command)
            continue
        if command[0] == "REMOVE":
            remove_task(command)
            continue
        if command[0] == "DONE":
            done_task(command)
            continue
        if command[0] == "LIST":
            list_all()
            continue
        if command[0] == "QUIT":
            exit()
        else:
            print("Unrecognized command. Please type help for available commands")
            continue


def add_task(task: string) -> list:
    del task[0]
    task = " ".join(task)
    to_do_list.append(task)
    return to_do_list

def remove_task(task: list) -> list:
    bool = False

def done_task(task: list) -> list:
    bool = False

def list_all() -> list:
    for i in range(len(to_do_list)):
        print(i + 1,":", to_do_list[i])
    return 



if __name__ == "__main__":
    main()