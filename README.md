# Backup Script with Timestamp

## Overview
This Python script automates file backup by copying files from a source folder to a destination folder. If a file with the same name already exists in the destination, it appends a timestamp to the new copy to prevent overwriting.

## Features
- Copies files from a source folder to a destination folder.
- Prevents overwriting by appending a timestamp to duplicate filenames.
- Uses Python's built-in `os`, `shutil`, and `datetime` modules.

## Prerequisites
- Python 3.x installed on your system.

## Usage
1. Update the `source_folder` and `destination_folder` variables in the script:
   ```python
   source_folder = r"C:\Users\Ankit Anand\OneDrive\Documents\DevOps\assignments\Source"
   destination_folder = r"C:\Users\Ankit Anand\OneDrive\Documents\DevOps\assignments\Destination"
   ```
2. Run the script:
   ```bash
   python backup_script.py
   ```

## Example
If `file.txt` exists in both source and destination:
- The script will copy it as `2025-02-10-14-30-00 - file.txt` in the destination.

## License
This project is licensed under the MIT License.

## Author
Ankit Anand

## Image
![Alt text](https://github.com/ankitanand200193/PythonAssignement/blob/b1935eb54d7a8d0ae3817888f730709c6103f929/backup%20screenshot.png)

![Alt text](https://github.com/ankitanand200193/PythonAssignement/blob/b1935eb54d7a8d0ae3817888f730709c6103f929/destination_folder.png)
