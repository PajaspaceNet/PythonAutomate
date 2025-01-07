# Archive Old Files Script

This Python script automates the process of archiving files that are older than 30 days. It moves outdated files into a designated folder, compresses them into a `.tar.gz` archive, and then cleans up temporary data to keep the workspace tidy.

## How the Script Works

### Core Functionality
- **Archiving Directory**:
  - The script creates an `archive` directory (if it doesn't already exist) to temporarily hold old files.
- **File Selection**:
  - Files older than 30 days are identified based on their last modified timestamp.
  - These files are moved into the `archive` directory.
- **Compression**:
  - The selected files are compressed into a `.tar.gz` archive named with the current date (e.g., `archive_20250107.tar.gz`).
- **Cleanup**:
  - After compression, the temporary `archive` directory is removed to free up space.

### Key Features
- **Automated File Management**:
  - Automatically detects and processes files based on their modification dates.
- **Date-Stamped Archives**:
  - Ensures that each archive is uniquely named with the date it was created.
- **Tidiness**:
  - Keeps the working directory clean by removing processed files and temporary folders.

## Usage
1. Place the script in the directory you want to clean up.
2. Run the script using Python:
   ```bash
   python archive_old_files.py
   ```
3. The script will create an archive containing all files older than 30 days in the current directory.

## Requirements
- Python 3.x
- Modules used:
  - `os`
  - `shutil`
  - `datetime`

## Notes
- The script processes all files in the current directory and its subdirectories.
- Ensure you have write permissions for the directory where the script runs.
- Existing archives with the same name will be overwritten.

## Example
If today is **January 7, 2025**, and you have files last modified before **December 8, 2024**, the script will:
1. Move those files into a temporary `archive` folder.
2. Create a compressed archive named `archive_20250107.tar.gz`.
3. Delete the `archive` folder after compression.

## Contribution
Feel free to fork the repository, suggest improvements, or submit pull requests to enhance the functionality of the script.
