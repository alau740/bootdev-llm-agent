import os
# this is similar to get_files_info
def get_file_content(working_directory, file_path):
        if os.path.commonpath([working_directory, file_path]) != working_directory:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path): # not a file
             return f'Error: File not found or is not a regular file: "{file_path}"'
        