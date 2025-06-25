"""
Directory Comparison Tool

A simple Python script to compare the contents of two directories and generate
a detailed report of differences and similarities.

Author: Thash Kunarajah
License: MIT
"""

import os
from pathlib import Path
from datetime import datetime


def get_directory_contents(directory_path):
    """
    Get all files and folders in a directory (non-recursive).
    
    Args:
        directory_path (str): Path to the directory to scan
        
    Returns:
        tuple: (set of item names, error message or None)
    """
    try:
        path = Path(directory_path)
        if not path.exists():
            return None, f"Directory does not exist: {directory_path}"
        
        if not path.is_dir():
            return None, f"Path is not a directory: {directory_path}"
        
        contents = set()
        for item in path.iterdir():
            contents.add(item.name)
        
        return contents, None
    except PermissionError:
        return None, f"Permission denied accessing directory: {directory_path}"
    except Exception as e:
        return None, f"Error reading directory {directory_path}: {str(e)}"


def compare_directories(dir1_path, dir2_path, output_file=None):
    """
    Compare two directories and generate a detailed comparison report.
    
    Args:
        dir1_path (str): Path to the first directory
        dir2_path (str): Path to the second directory
        output_file (str, optional): Path to save the report. If None, uses default naming.
        
    Returns:
        bool: True if comparison was successful, False otherwise
    """
    
    # Set default output file if none provided
    if output_file is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f"directory_comparison_{timestamp}.txt"
    
    # Get contents of both directories
    dir1_contents, dir1_error = get_directory_contents(dir1_path)
    dir2_contents, dir2_error = get_directory_contents(dir2_path)
    
    # Prepare output content
    output_lines = []
    output_lines.append("=" * 60)
    output_lines.append("DIRECTORY COMPARISON REPORT")
    output_lines.append("=" * 60)
    output_lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output_lines.append("")
    output_lines.append(f"Directory 1: {dir1_path}")
    output_lines.append(f"Directory 2: {dir2_path}")
    output_lines.append("")
    
    # Handle errors
    if dir1_error:
        output_lines.append(f"ERROR: {dir1_error}")
        output_lines.append("")
    
    if dir2_error:
        output_lines.append(f"ERROR: {dir2_error}")
        output_lines.append("")
    
    if dir1_error or dir2_error:
        # Write error report and exit
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(output_lines))
            print(f"Error report written to: {output_file}")
            return False
        except Exception as e:
            print(f"Error writing to output file: {e}")
            return False
    
    # Calculate differences and similarities
    only_in_dir1 = dir1_contents - dir2_contents
    only_in_dir2 = dir2_contents - dir1_contents
    common_items = dir1_contents & dir2_contents
    
    # Count totals
    total_dir1 = len(dir1_contents)
    total_dir2 = len(dir2_contents)
    total_common = len(common_items)
    total_different_dir1 = len(only_in_dir1)
    total_different_dir2 = len(only_in_dir2)
    
    # Add summary statistics
    output_lines.append("SUMMARY STATISTICS")
    output_lines.append("-" * 30)
    output_lines.append(f"Total items in Directory 1: {total_dir1}")
    output_lines.append(f"Total items in Directory 2: {total_dir2}")
    output_lines.append(f"Common items (in both): {total_common}")
    output_lines.append(f"Unique to Directory 1: {total_different_dir1}")
    output_lines.append(f"Unique to Directory 2: {total_different_dir2}")
    output_lines.append("")
    
    # Items only in Directory 1
    output_lines.append("ITEMS ONLY IN DIRECTORY 1")
    output_lines.append("-" * 40)
    if only_in_dir1:
        for item in sorted(only_in_dir1):
            output_lines.append(f"  • {item}")
    else:
        output_lines.append("  (No unique items)")
    output_lines.append("")
    
    # Items only in Directory 2
    output_lines.append("ITEMS ONLY IN DIRECTORY 2")
    output_lines.append("-" * 40)
    if only_in_dir2:
        for item in sorted(only_in_dir2):
            output_lines.append(f"  • {item}")
    else:
        output_lines.append("  (No unique items)")
    output_lines.append("")
    
    # Common items
    output_lines.append("COMMON ITEMS (IN BOTH DIRECTORIES)")
    output_lines.append("-" * 45)
    if common_items:
        for item in sorted(common_items):
            output_lines.append(f"  • {item}")
    else:
        output_lines.append("  (No common items)")
    output_lines.append("")
    
    # Write to file
    try:
        # Create directory if it doesn't exist
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output_lines))
        
        print(f"Comparison report successfully written to: {output_file}")
        print(f"Summary: {total_dir1} items in dir1, {total_dir2} items in dir2, {total_common} common, {total_different_dir1 + total_different_dir2} different")
        return True
        
    except Exception as e:
        print(f"Error writing to output file: {e}")
        return False


def main():
    """
    Main function to run the directory comparison tool interactively.
    """
    print("Directory Comparison Tool")
    print("=" * 25)
    print("This tool compares the contents of two directories and generates a report.")
    print()
    
    # Get input directories from user
    directory1 = input("Enter the path to the first directory: ").strip()
    directory2 = input("Enter the path to the second directory: ").strip()
    
    # Optional: Ask for custom output file
    output_choice = input("Enter output file path (or press Enter for default): ").strip()
    output_file = output_choice if output_choice else None
    
    print(f"\nComparing directories:")
    print(f"Directory 1: {directory1}")
    print(f"Directory 2: {directory2}")
    print(f"Output file: {output_file if output_file else 'Auto-generated'}")
    print("\nProcessing...")
    
    # Perform the comparison
    success = compare_directories(directory1, directory2, output_file)
    
    if success:
        print("\nComparison completed successfully!")
    else:
        print("\nComparison failed. Check the error messages above.")


if __name__ == "__main__":
    main()
