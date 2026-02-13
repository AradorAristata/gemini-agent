import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        work_absolute_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(work_absolute_path, file_path))
        valid_tar_file = os.path.commonpath([work_absolute_path, target_file]) == work_absolute_path
        if valid_tar_file == False:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            
    
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
        with open(target_file, 'r') as f:
            content = f.read(MAX_CHARS)  # Read up to MAX_CHARS characters
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return content

    except Exception as e:
        return f"Error: {str(e)}"