import os
from config import MAX_CHARS
from google.genai import types
# this is similar to get_files_info
def get_file_content(working_directory, file_path):
        try:
            abs_working_dir = os.path.abspath(working_directory)
            target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
            print(abs_working_dir, target_file)
            if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
                return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            if not os.path.isfile(target_file): # not a file, safeguard
                return f'Error: File not found or is not a regular file: "{file_path}"'

            # Open the file_path as read only, read up to MAX_CHARS
            with open(target_file, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                # After reading the first MAX_CHARS...
                if f.read(1): # Read another character to see if there are any remaining
                    file_content_string += (
                            f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                        )
                return file_content_string
        except Exception as e:
             return f"Error: {e}"
        
schema_get_files_content = types.FunctionDeclaration(
    name="get_files_content",
    description="Gets the contents of the specified file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to file, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

