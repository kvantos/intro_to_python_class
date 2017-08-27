from person import Person

class Proffesor(Person):
    """Mega Proffesor"""
    def __init__(self, name, age):
        super().__init__(name, age)
        self._salary = 0
        self._groups = []
        self.awards = []

#    def get_salary(self):
#        return self._salary

#    def set_salary(self, salary):
#        if salary < 0:
#            raise ValueError("Yo man, salary cant be negative.")
#        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Yo man, salary cant be negative.")
        self._salary = salary

    @property
    def groups(self):
        return self._groups

#    @groups.setter
#    def groups(self, groups):
#        if len(groups) > 3:
#            raise ValueError("Yo man, professor is not iron man")
#        self._groups = groups

    def add_group(self, group):
        if len(self._groups) == 3:
            raise ValueError("Yo man, professor is not iron man")
        self._groups.append(group)

    def remove_groups(self, group):
        if len(self._groups) == 0:
            raise ValueError("Yo man, nothing to remove")
        self._groups.remove(group)

#    def print_info(self):
#        super().print_info()
#        print("salary:\t", self.salary)
#        print("groups:\t", len(self.groups))
#        print("awards:\t", len(self.awards))
#        print("++++++++++++")

    def print_info_ext(self):
        print("salary:\t", self._salary)
        print("groups:\t", len(self.groups))
        print("awards:\t", len(self.awards))

