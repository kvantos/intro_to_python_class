class A:
    def __init__(self):
        self.attr1 = "muhahahha"

    def foo(self):
        print("Im mega foo")


class B(A):
    """Все я создал класс Б который наследник класса А"""
    # def __init__(self):
    #    self.attr2 = "attrB"

    def __init__(self):
        super().__init__()
        self.attr2 = "attrB"

    def foo(self):
        print("common or garden foo")

b = B()
b.foo()
print(b.attr1)
