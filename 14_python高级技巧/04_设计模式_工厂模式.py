class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


def Teacher():
    pass


class PersonFactory:
    def get_person(self, p_typer):
        if p_typer == 'w':
            return Worker()
        elif p_typer == 's':
            return Student()
        else:
            return Teacher()


pf = PersonFactory()
worker = pf.get_person('w')
stu = pf.get_person('s')
teacher = pf.get_person('t')

