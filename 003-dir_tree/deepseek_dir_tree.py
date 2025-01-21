import os

def generate_tree(directory, prefix=""):
    """
    Recursively generates an ASCII tree structure for the given directory.
    
    Args:
        directory (str): The directory to generate the tree for.
        prefix (str): Prefix for formatting (used internally for recursion).
    
    Returns:
        None
    """
    # List all items in the directory
    items = os.listdir(directory)
    items.sort()  # Sort alphabetically for consistent output

    for i, item in enumerate(items):
        # Skip the .git directory to avoid cluttering the tree
        if item == ".git":
            continue

        # Construct the full path of the item
        path = os.path.join(directory, item)

        # Determine if this is the last item in the directory
        is_last = (i == len(items) - 1)

        # Print the current item with appropriate prefix
        print(prefix + ("└── " if is_last else "├── ") + item)

        # If the item is a directory, recursively generate its tree
        if os.path.isdir(path):
            generate_tree(path, prefix + ("    " if is_last else "│   "))

if __name__ == "__main__":
    # Start generating the tree from the current directory
    print(".")
    generate_tree(".")
