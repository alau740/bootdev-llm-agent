import os
MAX_CHARS = 10000 # character limit
# this is similar to get_files_info
def get_file_content(working_directory, file_path):
        if os.path.commonpath([working_directory, file_path]) != working_directory:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path): # not a file, safeguard
             return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # Open the file_path as read only, read up to MAX_CHARS
        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
        if f.read(1): # Read another character to see if there are any remaining
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

