import os
import subprocess

# Learning purposes only
def run_python_file(working_directory, file_path, args=None):
    print(f"{working_directory}, {file_path}, {args}")
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        print(abs_working_dir, target_file)
        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path): # Check to see if the path is a file
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not str.endswith('.py', [file_path]): # Extra check for python file
            f'Error: "{file_path}" is not a Python file'

        command = ["python", abs_working_dir] # build command
        command.extend(args) # Extend command with any args passed to the function


        process = subprocess.run(command, cwd=working_directory, text=True, timeout=30, capture_output=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"{process.stdout}, {process.stderr}")



    except Exception as e:
        return f"Error: executing Python file: {e}"
    