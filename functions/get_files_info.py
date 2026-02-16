import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    try:
        work_absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(work_absolute_path, directory))
        valid_tar_dir = os.path.commonpath([work_absolute_path, target_dir]) == work_absolute_path
        if directory == ".":
            print(f"Result for current directory:")
        else:
            print(f"Result for {directory} directory:")
        if valid_tar_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            
    
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
    
        result = ""
        for each in os.listdir(target_dir):
            item_name = "- " + each + ": "
            item_size = "file_size=" + str(os.path.getsize(os.path.join(target_dir, each))) + ","
            item_isdir = "is_dir=" + str(os.path.isdir(os.path.join(target_dir, each)))
            " ".join([item_name, item_size, item_isdir])
            result += " ".join([item_name, item_size, item_isdir]) + "\n"
        return result.strip()

    except Exception as e:
        return f"Error: {str(e)}"