import os
from google.genai import types
def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        print(abs_working_dir, target_file)
        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(file_path): # Check to see if the path is a directory
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        print(f"makedir {file_path}")
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        print(f"Opening file {file_path}")
        with open(file_path, "w") as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    
schema_write_files_content = types.FunctionDeclaration(
    name="write_files_content",
    description="Write the file with content passed in as an argument, and writes this to the specified file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)