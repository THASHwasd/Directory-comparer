# Directory Comparison Tool

A simple yet powerful Python script that compares the contents of two directories and generates detailed reports showing differences and similarities.

## Features

- **Non-recursive comparison**: Compares only the immediate contents of directories (files and folders at the root level)
- **Detailed reporting**: Shows items unique to each directory and common items
- **Summary statistics**: Provides counts and percentages for quick overview
- **Error handling**: Gracefully handles missing directories, permission issues, and other errors
- **Flexible output**: Automatically generates timestamped reports or use custom file paths
- **Cross-platform**: Works on Windows, macOS, and Linux

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)


### Interactive Mode

Run the script directly for interactive input:

```bash
python dir_comparer By Thash.py
```

The script will prompt you for:
- Path to the first directory
- Path to the second directory  
- Output file path (optional - will auto-generate if not provided)

### Programmatic Usage

You can also import and use the functions in your own Python code:

```python
from dir_compare import compare_directories

# Basic comparison with auto-generated output file
success = compare_directories("/path/to/dir1", "/path/to/dir2")

# Comparison with custom output file
success = compare_directories("/path/to/dir1", "/path/to/dir2", "my_report.txt")
```

## Example Output

The tool generates a detailed report like this:

```
============================================================
DIRECTORY COMPARISON REPORT
============================================================
Generated on: 2024-01-15 14:30:22

Directory 1: /home/user/folder1
Directory 2: /home/user/folder2

SUMMARY STATISTICS
------------------------------
Total items in Directory 1: 15
Total items in Directory 2: 12
Common items (in both): 8
Unique to Directory 1: 7
Unique to Directory 2: 4

ITEMS ONLY IN DIRECTORY 1
----------------------------------------
  • document1.txt
  • image.png
  • script.py
  • temp_folder

ITEMS ONLY IN DIRECTORY 2
----------------------------------------
  • backup.zip
  • config.json
  • readme.md

COMMON ITEMS (IN BOTH DIRECTORIES)
---------------------------------------------
  • data.csv
  • main.py
  • requirements.txt
  • utils.py
```

## Use Cases

- **Backup verification**: Ensure backup directories contain the same files as originals
- **Synchronization checking**: Verify if two directories are properly synchronized
- **Migration validation**: Confirm all files were moved correctly during migrations
- **Duplicate detection**: Find differences between similar directory structures
- **Development workflow**: Compare different versions of project directories

## Limitations

- **Non-recursive**: Only compares immediate directory contents, not subdirectories
- **Name-only comparison**: Compares only file/folder names, not contents or metadata
- **No size/date information**: Doesn't include file sizes, modification dates, or other metadata

## Error Handling

The tool handles various error conditions gracefully:

- **Non-existent directories**: Reports if directories don't exist
- **Permission issues**: Handles access denied errors
- **Invalid paths**: Validates that paths point to actual directories
- **File system errors**: Catches and reports other file system related errors

## Development Notes

This tool was originally created as a personal utility and has been enhanced with AI assistance to improve code efficiency, error handling, and documentation quality. The core logic and functionality remain human-designed, while AI contributed to:

- Enhanced error handling and edge case management
- Improved code documentation and comments
- Professional structuring and best practices implementation

## Contributing

Contributions are welcome! Here are some ways you can help:

1. **Bug reports**: Open an issue if you find any bugs
2. **Feature requests**: Suggest new features or improvements
3. **Code contributions**: Submit pull requests for bug fixes or new features
4. **Documentation**: Help improve documentation and examples

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests if applicable
4. Ensure code follows Python best practices
5. Submit a pull request

## Future Enhancements

Potential features for future versions:

- [ ] Recursive directory comparison
- [ ] File content comparison (checksums/hashes)
- [ ] File size and modification date comparison
- [ ] JSON/CSV output formats
- [ ] Command-line argument support
- [ ] Progress bars for large directories
- [ ] Filtering options (ignore patterns, file types)
- [ ] Graphical user interface (GUI)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### Version 1.0.0
- Initial release
- Basic directory comparison functionality
- Text report generation
- Error handling and validation
