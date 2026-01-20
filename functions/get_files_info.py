import os
def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath() # absolute path
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_path = os.path.commonpath([working_dir_abs, target_dir]) == working_directory # if target_dir falls in absolute dir
    if not os.path.isdir(directory):
        return f'Error: Cannot list "{directory}" as it is not a directory'
    

