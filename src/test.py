from _typeshed import FileDescriptor
import os
os.chdir(os.getcwd())
dirs, files = os.walk()
for dir in dirs:
    print(dir)