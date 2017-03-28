import os

print(os.getcwd())

# os.chdir('/Users/patir/Documents')

# print(os.getcwd())

# # list of directory
# print(os.listdir())

# os.mkdir("python_practice")
# make serveral directory togethers
# os.makedirs("python/python_practice")

# os.rmdir("a")
# os.removedirs("a/b/c")

# os.rename('test.txt','demo.txt')

# information about file
# print(os.stat('demo.txt'))
# print(os.stat('demo.txt').st_size)
#last modification time
# print(os.stat('demo.txt').st_mtime)
from datetime import datetime

mod_time = os.stat('os_module.py').st_mtime
#human readable format
print(datetime.fromtimestamp(mod_time))

os.chdir('/Users/patir/Documents')
#travel from all the directories
# os.walk()

# for dirpath, dirnames, filenames in os.walk('/Users/patir/Documents'):
# 	print("current path", dirpath)
# 	print("Directories", dirnames)
# 	print("Files", filenames)
# 	print()


#environment variable

print(os.environ.get('HOME'))


