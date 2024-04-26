import os

def list_files_in_drive(drive_path):
    try:
        # List all files in the specified drive
        file_list = []
        for root, dirs, files in os.walk(drive_path):

            # It start searching from first to last on a ranking basis.
            # "i" is a tuple in which there is a root, list of directories and list of file which is retured by root, dirs and files.

            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Specify the drive path (e.g., 'C:' for the C drive)
drive_path = '/home/nag2mani/code/Github'

# List all files in the specified drive
files_in_drive = list_files_in_drive(drive_path)

# Print the list of files
for file_path in files_in_drive:
    print(file_path)

