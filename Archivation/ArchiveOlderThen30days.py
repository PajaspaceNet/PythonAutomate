import os
import shutil
import datetime 

def archive_old_files():
    # Define the archive directory
    archive_dir = 'archive'
    os.makedirs(archive_dir, exist_ok=True)

    # Current date for archive name
    current_date = datetime.datetime.now().strftime('%Y%m%d')
    archive_file = f'archive_{current_date}.tar.gz'

    # Move and compress files older than 30 days
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=30)
    for root, dirs, files in os.walk('.'):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                if file_mtime < cutoff_date:
                    shutil.move(file_path, archive_dir)

    # Create a tar.gz archive of the files
    shutil.make_archive(archive_file.replace('.tar.gz', ''), 'gztar', archive_dir)

    # Clean up the archive directory
    shutil.rmtree(archive_dir)

if __name__ == "__main__":
    archive_old_files()
