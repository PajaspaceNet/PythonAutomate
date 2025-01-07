# File Organizer Script

This Python script organizes files in a specified directory into categorized folders based on their file types. It's designed to make managing cluttered directories simple and efficient.

## How the Script Works

### File Type Configuration
- The script uses a dictionary called `FILE_CATEGORIES` to define mappings between file extensions and folder names.
- Example:
  - Images: `.jpg`, `.png`, `.gif`
  - Documents: `.pdf`, `.docx`, `.txt`

### Folder Creation and File Movement
- The script automatically creates folders corresponding to the categories if they do not already exist.
- Files are moved to the appropriate folders based on their extensions.

### Universal Handling
- Files with extensions not defined in `FILE_CATEGORIES` are moved to the `Others` folder.

### Usage
1. Run the script.
2. Input the path of the directory you want to organize.
3. The script will handle the rest—organizing files into categorized folders.

## Example Categories
Here are the default categories defined in the script:

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`
- **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx`
- **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`
- **Videos**: `.mp4`, `.mkv`, `.mov`, `.avi`, `.wmv`
- **Archives**: `.zip`, `.rar`, `.tar`, `.gz`, `.7z`
- **Code**: `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.cs`, `.php`, `.rb`
- **Others**: Any file type not listed above.

## Requirements
- Python 3.x
- `shutil` and `os` modules (pre-installed with Python)

## Notes
- Ensure the target directory is accessible and not write-protected.
- The script skips directories and organizes only files.

## Contribution
Feel free to fork the repository, suggest improvements, or submit pull requests to enhance the script.
