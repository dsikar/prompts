#!/usr/bin/env python3

import os
import sys

def generate_directory_tree(startpath):
    """
    Generates an ASCII tree structure of the directory starting from startpath.

    Args:
        startpath (str): The path to the directory to generate the tree for.

    Returns:
        str: An ASCII string representation of the directory tree.
    """
    tree_str = ""
    prefix = ""

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree_str += '{}{}/\n'.format(indent, os.path.basename(root))
        sub_indent = ' ' * 4 * (level + 1)

        # Sort directories and files alphabetically for consistent output
        sorted_items = sorted(dirs + files)

        for i, item in enumerate(sorted_items):
            if i == len(sorted_items) - 1:
                # Last item in the list, use a different tree branch character
                tree_str += '{}{}`-- {}\n'.format(sub_indent, '└──', item)
            else:
                tree_str += '{}{}|-- {}\n'.format(sub_indent, '├──', item)

    return tree_str

if __name__ == "__main__":
    # Get the root directory from command line arguments, or use current directory if none provided
    if len(sys.argv) > 1:
        root_dir = sys.argv[1]
    else:
        root_dir = '.'  # Current directory

    # Normalize the path to handle relative or absolute paths
    root_dir = os.path.abspath(root_dir)

    if not os.path.isdir(root_dir):
        print(f"Error: '{root_dir}' is not a valid directory.")
        sys.exit(1)

    print(f"Directory tree for: {root_dir}\n")
    tree = generate_directory_tree(root_dir)
    print(tree)
