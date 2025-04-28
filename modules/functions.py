def get_todos(filepath=r"C:\Users\thana\Downloads\April_2025_Training\ToDoList\todos.txt"):
    """Read a text file"""
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=r"C:\Users\thana\Downloads\April_2025_Training\ToDoList\todos.txt"):
    """Write the to-do items list in the text file"""
    with open(filepath,'w') as file_local:
        file_local.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
