from person import Person


class Student(Person):
    """
    Mega student
    """
    NUMBER_OF_TASKS = 37
    NUMBER_OF_TESTS = 12
    TEST_WEIGHT = [1,2,3,4,5,6,7,8,9,10,11,12]

    def __init__(self, name, age):
        super().__init__(name, age)

        self.hw_res = [0] * Student.NUMBER_OF_TASKS
        self.test_res = [0] * Student.NUMBER_OF_TESTS
        self.rank = 0

    def __str__(self):
        return "%s:\n name: %s\n age: %s" % (self.__class__.__name__, self.name, self.age)

#    def print_info(self):
#        super().print_info()
#        print("h\w:\t", self.hw_res)
#        print("test:\t", self.test_res)
#        print("rank:\t", self.rank)
#        print("------------")

    def print_info_ext(self):
        print("h\w:\t", self.hw_res)
        print("test:\t", self.test_res)
        print("rank:\t", self.rank)

    def total_rank(self):
        hw_rank = sum(self.hw_res)
        test_rank = sum([Student.TEST_WEIGHT[i]*self.test_res[i] for i in range(Student.NUMBER_OF_TESTS)])
        self.rank = hw_rank + test_rank

    def accept_task(self, number_of_task):
        self.hw_res[number_of_task - 1] = 1
        self.total_rank()

    def accept_multy_tasks(self, *number_of_task):
        for task_number in number_of_task:
            self.hw_res[task_number - 1] = 1
        self.total_rank()

    def accept_test(self, number_of_test):
        self.test_res[number_of_test - 1] = 1
        self.total_rank()