import os


def get_files(file_name, search_path):
    for dirpath, dirnames, filenames in os.walk(search_path):
        if file_name in filenames:
            print(os.path.join(dirpath, file_name))


get_files("filename.txt", "/path/to/search")
