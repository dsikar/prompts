import os

def print_tree(path, level=0):
  """
  Prints an ASCII tree representation of the directory structure.

  Args:
    path: The path to the directory to print.
    level: The current indentation level.
  """
  indent = "  " * level
  print(f"{indent}{os.path.basename(path)}/")

  for item in os.listdir(path):
    item_path = os.path.join(path, item)
    if os.path.isdir(item_path):
      print_tree(item_path, level + 1)

# Get the root directory of the current repository
root_dir = os.path.dirname(os.path.abspath(__file__)) 

print_tree(root_dir)
