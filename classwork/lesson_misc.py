f = open(r'D:\python_lesson_test.txt')
d = {'UA': "Kyiv"}
print(d['UA'])
print("hello, clossing file")
f.close()

class MgrConTest:
    def __init__(self):
        haa = "12"
        print("Im. here")

    def __enter__(self):
        print("entered")

    def __exit__(self,  *exc_info):
        print("exited")


with MgrConTest() as mrg_test:
    print("Yo man")

ho = MgrConTest()
ho.haa = "sdf"
print(ho.haa)