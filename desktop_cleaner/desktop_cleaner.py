import os
import shutil
from datetime import datetime, timedelta

def move_files_older_than_2_days(source_dir, destination_dir):
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Current time
    now = datetime.now()

    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        # Skip directories, only check files
        if os.path.isfile(file_path):
            # Get file's last modified time
            file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            # Check if the file is older than 2 days
            if now - file_mod_time > timedelta(days=2):
                # Move file
                shutil.move(file_path, destination_dir)
                print(f"Moved: {filename}")

# User input for paths
desktop_path = input("Enter the path of your Desktop: ")
destination_path = input("Enter the path for moving old files: ")

# Run the function
move_files_older_than_2_days(desktop_path, destination_path)
