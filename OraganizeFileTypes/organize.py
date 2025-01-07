import os
import shutil

# Define mapping of file extensions to folder names
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".cs", ".php", ".rb"],
    "Others": []  # Catch-all for unclassified files
}

def organize_files(directory):
    """Organizes files in the specified directory into subfolders by type."""
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Create folders for each category if not already present
    for folder in FILE_CATEGORIES.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, file_extension = os.path.splitext(filename)

        # Find the correct folder for the file
        destination_folder = "Others"  # Default folder
        for folder, extensions in FILE_CATEGORIES.items():
            if file_extension.lower() in extensions:
                destination_folder = folder
                break

        # Move the file to the appropriate folder
        destination_path = os.path.join(directory, destination_folder, filename)
        shutil.move(file_path, destination_path)
        print(f"Moved: {filename} -> {destination_folder}")

if __name__ == "__main__":
    target_directory = input("Enter the path of the directory to organize: ").strip()
    organize_files(target_directory)
