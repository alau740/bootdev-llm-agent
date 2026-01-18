import os
def get_files_info(working_directory, directory="."):
    file_path = os.path.abspath() # absolute path
    target_dir = os.path.normpath(os.path.join(file_path, directory))
    valid_path = os.path.commonpath([file_path, target_dir]) == working_directory
    pass

