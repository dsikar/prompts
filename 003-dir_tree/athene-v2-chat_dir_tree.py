import os
import sys

# Function to generate the ASCII tree structure
def generate_tree(path, prefix='', is_last=False, level=0):
    """
    Recursively generates an ASCII tree structure for the given path.

    :param path: Current directory path
    :param prefix: Prefix for the current level of the tree
    :param is_last: Boolean indicating if the current item is the last in the list
    :param level: Current level of the tree (depth)
    """
    # Get the base name of the current directory/file
    base_name = os.path.basename(path)
    
    # Determine the prefix for the current item
    if is_last:
        print(f"{prefix}└── {base_name}")
        new_prefix = f"{prefix}    "
    else:
        print(f"{prefix}├── {base_name}")
        new_prefix = f"{prefix}│   "

    # If the path is a directory, recurse into it
    if os.path.isdir(path):
        children = sorted(os.listdir(path))
        last_child = children[-1] if children else None
        for child in children:
            child_path = os.path.join(path, child)
            generate_tree(child_path, new_prefix, is_last=(child == last_child), level=level + 1)

# Main function to start the tree generation from the root directory
def main():
    """
    Main function to start the tree generation.
    """
    # Get the root directory (current working directory)
    root_dir = os.getcwd()
    
    # Print the root directory name
    print(f"Directory: {root_dir}\n")
    
    # Generate the tree starting from the root directory
    generate_tree(root_dir, level=0)

# Entry point of the script
if __name__ == "__main__":
    main()
