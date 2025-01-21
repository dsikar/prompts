import os
from pathlib import Path

def print_tree(directory, prefix="", is_last=True):
    """
    Recursively print the directory tree structure in ASCII format.

    :param directory: Path to the directory to print
    :param prefix: String to add before each line to show hierarchy
    :param is_last: Indicates if the current item is the last child of its parent
    """
    # Ensure directory exists
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    # Get the directory name or file name
    name = os.path.basename(directory)
    
    # Define the line prefix for the current level
    connector = "└── " if is_last else "├── "
    print(prefix + connector + name)

    # Prepare for the next level
    new_prefix = prefix + ("    " if is_last else "│   ")
    
    # List contents of the directory
    contents = sorted(os.listdir(directory))
    for index, item in enumerate(contents):
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            # If it's a directory, recurse
            print_tree(path, new_prefix, index == len(contents) - 1)
        else:
            # If it's a file, print it with appropriate prefix
            file_connector = "└── " if index == len(contents) - 1 else "├── "
            print(new_prefix + file_connector + item)

if __name__ == "__main__":
    # Start from the current directory (assumed to be root of GitHub repo)
    root_dir = "."
    print_tree(root_dir)
