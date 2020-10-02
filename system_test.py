import sys

cur_version = sys.version_info

with open('output.txt', 'w') as n_File2:  # Writes to a new file
    if cur_version >= (3, 6):
        n_File2.write(
            "This an acceptable version of Python, version " + str(cur_version[0]) + '.' + str(cur_version[1]) + '.')
    else:
        n_File2.write("Your Python version is to low, it needs to be 3.6 or greater and this is " + str(
            cur_version[0]) + '.' + str(cur_version[1]) + '.')
