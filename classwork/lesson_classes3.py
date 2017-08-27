import os

class DirectoryChanger:
    def __init__(self, dir):
        self.dir = dir
        self.old_dir = os.getcwd()

    def print_dir(self):
        for item in os.listdir(os.getcwd()):
            print(item)

    def __enter__(self):
        os.chdir(self.dir)
        print("current dir (enter):", os.getcwd())
        self.print_dir()

    def __exit__(self, *exc_info):
        os.chdir(self.old_dir)
        print("current dir (exit):", os.getcwd())
        self.print_dir()

print(os.getcwd())
try:
    with DirectoryChanger(r"C:\tmp") as cd:
        print(os.getcwd())
        raise ValueError("smth went wrong")
except:
    pass

# print(os.getcwd())
# print(os.listdir(r"C:\\"))