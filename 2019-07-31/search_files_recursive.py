import os


def get_file(name, path):
    for o in os.listdir(path):
        full_path = path + os.sep + o
        if os.path.isdir(full_path):
            get_file(name, full_path)
        elif o == name:
            print(full_path)


get_file("filename.txt", "/path/to/search")
