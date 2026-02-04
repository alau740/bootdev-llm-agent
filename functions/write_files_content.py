import os
def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        print(abs_working_dir, target_file)
        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(file_path): # not a file, safeguard
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(file_path, exist_ok=True)

        with open(file_path, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'



        raise NotImplementedError("Not implemented")

    except Exception as e:
        return f"Error: {e}"