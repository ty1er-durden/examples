import os


def search_file(filename):
    """ Find file with requested name """
    for path in os.environ["PATH"].split(os.pathsep):
        candidate = os.path.join(path, filename)
        if os.path.exists(candidate):
            return os.path.abspath(candidate)
    return None
