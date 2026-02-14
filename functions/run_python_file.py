import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        work_absolute_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(work_absolute_path, file_path))
        valid_tar_file = os.path.commonpath([work_absolute_path, target_file]) == work_absolute_path
        if valid_tar_file == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            
    
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
    
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        
        command = ["python", target_file]
        if args:
            command.extend(args)
        result = subprocess.run(command, cwd=work_absolute_path, capture_output=True, text=True, timeout=30)
        output_str = ""
        if result.returncode != 0:
            output_str += f"Process exited with code {result.returncode}\nSTDERR: {result.stderr}"
        if result.stdout == "" and result.stderr == "":
            output_str += "No output produced."
        else:
            output_str += f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        return output_str

    except Exception as e:
        return f"Error: executing Python file: {str(e)}"