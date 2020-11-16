from _typeshed import FileDescriptor
import os
os.chdir(os.getcwd())
dirs, files = os.walk()
for dir in dirs:
    print(dir)

def test():
    return 1

def test2():
    return True
# add test3
def test3():
    return False

