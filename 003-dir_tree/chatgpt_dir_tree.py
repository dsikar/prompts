import os

def generate_tree(directory, indent=""):
    """
    Recursively generates an ASCII tree structure for the given directory.
    
    :param directory: The directory to list files from.
    :param indent: The indentation string for nested directories/files (default is an empty string).
    :return: None
    """
    # Check if the provided directory exists
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    # List the contents of the directory, including subdirectories
    try:
        # Get all items (files/folders) in the directory
        items = os.listdir(directory)
    except PermissionError:
        print(f"Error: Permission denied for accessing {directory}.")
        return

    # Iterate over the items in the directory
    for i, item in enumerate(sorted(items)):
        # Get the full path of the item
        item_path = os.path.join(directory, item)
        
        # Print the item, adding indentation for nested structures
        # If it's the last item in the list, use "└──", else use "├──"
        if i == len(items) - 1:
            print(f"{indent}└── {item}")
            # If it's a directory, recurse into it
            if os.path.isdir(item_path):
                generate_tree(item_path, indent + "    ")
        else:
            print(f"{indent}├── {item}")
            # If it's a directory, recurse into it
            if os.path.isdir(item_path):
                generate_tree(item_path, indent + "│   ")

if __name__ == "__main__":
    # Run the tree generation from the current directory
    print("Generating ASCII Tree Structure of the Repository:")
    generate_tree(os.getcwd())  # Start from the current working directory

