class Person:
    """Mega person"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info_ext(self):
        pass

    def print_info(self):
        print("============")
        print("Name:\t", self.name)
        print("Age:\t", self.age)
        self.print_info_ext()
        print("---------------")

