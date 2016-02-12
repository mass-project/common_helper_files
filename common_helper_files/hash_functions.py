import hashlib
from .file_functions import read_in_chunks


def md5sum(file_object):
    m = hashlib.md5()
    for data in read_in_chunks(file_object):
        m.update(data)
    return m.hexdigest().lower()
