# The-Todo

https://user-images.githubusercontent.com/27226348/230737157-7273264b-276c-4feb-87c4-3cb384307d99.mov


### Table of Contents

1. [Installation](#installation)
2. [Description of Project](#description)
3. [Customization](#customization)
4. [File Descriptions](#files)
5. [Licensing](#licensing)

## Installation <a name="installation"></a>
To install the app, you can use `pip` :

```bash
pip install the-todo
```

To use the todo, all you have to do is open terminal and type:
```bash
python -m todo
```

The todo app has following options available to manage tasks :

## Description <a name="description"></a>
This is a simple command-line todo app built in Python. It allows you to add, view, mark as completed, and remove tasks from a todo list using a terminal interface.

### Options :
```markdown
1. add  : Add task
2. ls   : View tasks
3. cplt : Mark task as completed
4. rm   : Remove task
5. exit : Exit
```
You can then enter one of these commands to perform an action.

### Examples :

Add a new task :
```bash
todo >> add Buy groceries
Task added successfully!
```

View all tasks :
```bash
todo >> ls
Tasks:
1. Buy groceries
```

Mark a task as completed :
```bash
todo >> cplt 1
Task marked as completed!
```

Remove a task :
```bash
todo >> rm 1
Task removed successfully!
```

## Customization <a name="customization"></a>

By default, the app creates a todo list called "todo" and stores it in a SQLite database at ~/.todos/todo.db. However, you can specify a different name for the list by using the -n or --name option:

```bash
python -m todo --name mylist
```
This will create a new todo list called "mylist" and store it in a SQLite database at ~/.todos/mylist.db.

## File Description <a name="files"></a>

```
.
├── README.md
├── LICENCE : contains MIT LICENCE
├── setup.py : Setup file to create distribution packages
└── todo : The todo package
    ├── __init__.py
    ├── __main__.py 
    ├── todo.py : Todo class with modular code
    └── todo_prompt.py : Todo Prompt
```

## Licensing <a name="licensing"></a>
This app is released under the MIT License. Feel free to use, modify, and distribute it as you like.