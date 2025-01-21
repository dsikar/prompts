#!/usr/bin/env python3

import os
import argparse
from pathlib import Path
from typing import Set, List

class DirectoryTreeGenerator:
    """Generate an ASCII tree representation of a directory structure."""
    
    def __init__(self, ignore_patterns: Set[str], max_depth: int = None):
        """
        Initialize the tree generator with ignore patterns and maximum depth.
        
        Args:
            ignore_patterns: Set of patterns to ignore (e.g., '.git', '__pycache__')
            max_depth: Maximum depth to traverse (None for unlimited)
        """
        self.ignore_patterns = ignore_patterns
        self.max_depth = max_depth
        self.tree_content: List[str] = []

    def should_ignore(self, path: str) -> bool:
        """
        Check if a path should be ignored based on ignore patterns.
        
        Args:
            path: Path to check
            
        Returns:
            bool: True if path should be ignored, False otherwise
        """
        name = os.path.basename(path)
        return any(
            pattern in name or name.endswith(pattern)
            for pattern in self.ignore_patterns
        )

    def generate_tree(self, root_path: str, prefix: str = "", depth: int = 0) -> None:
        """
        Recursively generate the tree structure.
        
        Args:
            root_path: Path to start from
            prefix: Current line prefix for proper indentation
            depth: Current depth in the directory structure
        """
        # Check max depth
        if self.max_depth is not None and depth > self.max_depth:
            return

        # Get directory contents
        try:
            entries = sorted(os.listdir(root_path))
        except PermissionError:
            self.tree_content.append(f"{prefix}├── [Permission Denied]")
            return

        # Process each entry
        for i, entry in enumerate(entries):
            path = os.path.join(root_path, entry)
            
            # Skip if should be ignored
            if self.should_ignore(path):
                continue

            # Determine if this is the last entry
            is_last = i == len(entries) - 1
            
            # Create proper prefix for current entry
            current_prefix = prefix + ("└── " if is_last else "├── ")
            
            # Add entry to tree
            self.tree_content.append(f"{current_prefix}{entry}")
            
            # Recurse into directories
            if os.path.isdir(path):
                next_prefix = prefix + ("    " if is_last else "│   ")
                self.generate_tree(path, next_prefix, depth + 1)

    def save_tree(self, output_file: str) -> None:
        """
        Save the generated tree to a file.
        
        Args:
            output_file: Path to output file
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.tree_content))

def main():
    """Main function to handle command-line arguments and generate the tree."""
    parser = argparse.ArgumentParser(
        description='Generate an ASCII tree structure of a directory'
    )
    parser.add_argument(
        '--path', 
        default='.',
        help='Root path to generate tree from (default: current directory)'
    )
    parser.add_argument(
        '--output',
        default='directory_tree.txt',
        help='Output file name (default: directory_tree.txt)'
    )
    parser.add_argument(
        '--max-depth',
        type=int,
        default=None,
        help='Maximum depth to traverse (default: unlimited)'
    )
    parser.add_argument(
        '--ignore',
        nargs='+',
        default=['.git', '__pycache__', '.pytest_cache', '.venv', 'venv', 'node_modules'],
        help='Patterns to ignore (default: common version control and cache directories)'
    )

    args = parser.parse_args()

    # Convert path to absolute path
    root_path = str(Path(args.path).resolve())
    
    # Create tree generator
    generator = DirectoryTreeGenerator(
        ignore_patterns=set(args.ignore),
        max_depth=args.max_depth
    )
    
    # Generate tree structure starting with root directory name
    root_name = os.path.basename(root_path)
    generator.tree_content.append(root_name)
    generator.generate_tree(root_path)
    
    # Save to file
    generator.save_tree(args.output)
    print(f"Directory tree has been saved to {args.output}")

if __name__ == "__main__":
    main()
