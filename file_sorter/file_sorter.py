import os
import shutil

# User input for paths
source_folder = input("Enter the path of the source folder: ")
base_dest_folder = input("Enter the base path for destination folders: ")

# Define destination folders based on user input
dest_folders = {
    'images': os.path.join(base_dest_folder, 'moved_images'),
    'pdf': os.path.join(base_dest_folder, 'moved_documents', 'moved_pdf'),
    'word': os.path.join(base_dest_folder, 'moved_documents', 'moved_word'),
    'other': os.path.join(base_dest_folder, 'moved_other')
}

# Create destination folders if they don't exist
for folder in dest_folders.values():
    if not os.path.exists(folder):
        os.makedirs(folder)

# Extensions mapping to folder names
image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.webp', '.tiff', '.tif', '.psd']
document_extensions = ['.pdf', '.docx', '.doc', '.odt', '.rtf', '.txt']

# Create a dictionary that maps extensions to the appropriate folder
file_mappings = {ext: 'images' for ext in image_extensions}
file_mappings.update({ext: 'pdf' for ext in ['.pdf']})
file_mappings.update({ext: 'word' for ext in ['.docx', '.doc', '.odt', '.rtf', '.txt']})

# Function to move files to the respective folder
def move_file(file_path, file_type):
    destination_folder = dest_folders.get(file_type, dest_folders['other'])
    destination_path = os.path.join(destination_folder, os.path.basename(file_path))

    # Check if the file already exists and skip it if it does
    if os.path.exists(destination_path):
        print(f"File {os.path.basename(file_path)} already exists in the destination. Skipping.")
        return

    shutil.move(file_path, destination_path)

# Process the files and directories in the source folder
for item in os.listdir(source_folder):
    item_path = os.path.join(source_folder, item)
    if os.path.isfile(item_path):
        extension = os.path.splitext(item)[1].lower()
        file_type = file_mappings.get(extension, 'other')
        move_file(item_path, file_type)

print("Files have been sorted and moved.")
