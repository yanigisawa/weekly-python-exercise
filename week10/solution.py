# This week, we're going to start to work on a small application that detects whether files have been changed or otherwise tampered with. The aim here isn't to compete with such systems as Tripwire, but rather to work a bit with hashing, data storage, and reporting.

# This exercise will extend over several weeks. This week, we'll start the process by writing a program that collects information about files, and creates a data structure from that information.

# In other words: You should write a function, get_file_info, that takes a single argument, "pathname," the name of a directory. The program will then go through each of the files in that directory, as well as in any subdirectories, and will calculate the SHA-1 of that file.

# The program should then produce (and print) a data structure -- a list of dictionaries -- in which each dictionary will contain the following information:
# full path and filename
# file timestamp
# SHA-1 of the file's contents

# This exercise combines a number of different things:
# The use of os.walk to go through an entire directory/tree structure
# The use of os.stat to retrieve information about files
# The calculation of a hash function (SHA-1, in this case) on a file's contents
# I'll be back on Monday with a solution and discussion.

# Reuven
import os
import hashlib
BLOCKSIZE = 65536

def get_file_info(pathname):
    all_files = []
    for root, _, files in os.walk(pathname, topdown=False):
        for name in files:
            full_path = os.path.join(root, name)

            hasher = hashlib.sha1()
            with open(full_path, 'rb') as afile:
                buf = afile.read(BLOCKSIZE)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = afile.read(BLOCKSIZE)
            file_info = {
                'filename': full_path,
                'sha1': hasher.hexdigest()
            }
            print(os.path.join(root, name))
            all_files.append(file_info)

    return all_files