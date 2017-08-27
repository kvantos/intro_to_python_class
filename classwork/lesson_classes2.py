from student import Student
from proffesor import Proffesor

if __name__ == '__main__':

    st1 = Student("Bill", 22)
    st2 = Student("Alice", 24)


    print(st2.name, st2.age)
    print(id(st2))

    st1.print_info()
    st2.print_info()

    st1.accept_task(2)
    st1.accept_test(10)
    st1.print_info()

    st2.accept_multy_tasks(1,2,3,4,5,6)
    st2.print_info()

    prof = Proffesor("Pete", 77)
    prof.print_info()

    # prof.set_salary(100)
    prof.salary = 100
    # prof.groups = ['Math', "Phis", "CS"]
    prof.add_group("DB")
    prof.add_group("CS")
    prof.print_info()
    prof.remove_groups("DB")
    print(prof.groups)

    print(st1)