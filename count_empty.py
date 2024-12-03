import os

# Folder path to search for files
folder_path = 'res_rt'

# Iterate through all files in the folder
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        
        # Initialize a counter for empty lines in the current file
        empty_line_count = 0
        
        # Open the file and count empty lines
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if not line.strip():  # If the line is empty or contains only whitespace
                        empty_line_count += 1
            
            # Output the file name and its empty line count
            print(f'{file_name}: {empty_line_count} empty lines')

        except Exception as e:
            print(f"Could not read file {file_path}: {e}")
