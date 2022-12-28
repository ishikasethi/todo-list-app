def get_todos(filename='todos.txt'):
    """Documentation of a function for <help file>
    This function reads the text from a text line and returns a list of todos.
    """
    with open(filename, 'r') as file1:
        todolist = file1.readlines()
    return todolist


def write_todos(todolist, filename='todos.txt'):
    with open(filename, 'w') as file:
        file.writelines(todolist)


if __name__ == "__main__":
    print("testing space for functions.py file")
    print(get_todos())
