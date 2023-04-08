#!/Users/aarsh/miniconda3/envs/py11/bin/python
import os
import sqlite3
import cmd
import argparse
from termcolor import colored
from .todo import Todo

todo_name = 'todo'

parser = argparse.ArgumentParser(description="A simple command-line todo app.")
# parser = argparse.ArgumentParser()
parser.add_argument('--name', '-n', help='Name of the to-do list')
args = parser.parse_args()

if args.name:
    todo_name = args.name

if not os.path.exists(f"{os.path.expanduser('~')}/.todos"):
    os.mkdir(f"{os.path.expanduser('~')}/.todos")

sqlite_path = f"{os.path.expanduser('~')}/.todos/{todo_name}.db"

# Create database and table if they don't exist
todo = Todo(sqlite_path)


def clear_terminal():
    # Check if the operating system is Windows
    if os.name == 'nt':
        # Use the 'cls' command to clear the terminal
        os.system('cls')
    # For Unix-based systems (Linux, macOS)
    else:
        # Use the 'clear' command to clear the terminal
        os.system('clear')


print(colored("""
     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄    ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ 
    █       █       █  █      ██       █
    █▄     ▄█   ▄   █  █  ▄    █   ▄   █
      █   █ █  █ █  █  █ █ █   █  █ █  █
      █   █ █  █▄█  █  █ █▄█   █  █▄█  █
      █   █ █       █  █       █       █
      █▄▄▄█ █▄▄▄▄▄▄▄█  █▄▄▄▄▄▄██▄▄▄▄▄▄▄█
""", "yellow"))

print(colored("Options", "white"))
print(colored("1. add  : Add task", "green"))
print(colored("2. ls   : View tasks", "blue"))
print(colored("3. cplt : Mark task as completed", "magenta"))
print(colored("4. rm   : Remove task", "yellow"))
print(colored("5. exit : Exit", "red"))


class TodoPrompt(cmd.Cmd):
    prompt = colored("\ntodo >> ", "cyan")

    def do_add(self, sub_commands):
        sub_commands = sub_commands.split()
        if sub_commands:
            todo.add_task(" ".join(sub_commands))
        else:
            task = input(colored("Enter task: ", "green"))
            todo.add_task(task)
        print(colored("Task added successfully!", "green"))

    def do_ls(self, sub_commands):
        tasks = todo.get_tasks()
        if len(tasks) == 0:
            print(colored("No tasks found.", "red"))
        else:
            print(colored("Tasks:", "blue"))
            for task in tasks:
                if task[2]:
                    print(
                        colored(f"{task[0]}. {task[1]} (completed)", "green"))
                else:
                    print(f"{task[0]}. {task[1]}")

    def do_complete(self, sub_commands):
        sub_commands = sub_commands.split()
        if sub_commands:
            todo.complete_task(sub_commands[0])
        else:
            task_id = input(colored("Enter task ID: ", "magenta"))
            todo.complete_task(task_id)
        print(colored("Task marked as completed!", "magenta"))

    do_cplt = do_complete

    def do_rm(self, sub_commands):
        sub_commands = sub_commands.split()
        if sub_commands and sub_commands[0].strip().lower() in ('all', '*'):
            todo.remove_all()
            print(colored("All tasks removed successfully!", "yellow"))
        elif sub_commands:
            todo.remove_task(sub_commands[0].strip().lower())
            print(colored("Task removed successfully!", "yellow"))
        else:
            task_id = input(colored("Enter task ID to remove: ", "yellow"))
            todo.remove_task(task_id)
            print(colored("Task removed successfully!", "yellow"))

    def do_help(self, sub_commands):
        print(colored("Options", "white"))
        print(colored("1. add  : Add task", "green"))
        print(colored("2. ls   : View tasks", "blue"))
        print(colored("3. cplt : Mark task as completed", "magenta"))
        print(colored("4. rm   : Remove task", "yellow"))
        print(colored("5. exit : Exit", "red"))

    def do_clear(self, sub_commands):
        clear_terminal()

    def do_exit(self, sub_commands):
        print(colored("Exiting program...", "red"))
        exit()

    def default(self, sub_commands):
        print(colored("Invalid command. Try again.", "red"))


try:
    TodoPrompt().cmdloop()
except KeyboardInterrupt:
    print(colored("\nExiting program...", "red"))
