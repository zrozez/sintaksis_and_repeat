class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f'My name is {self.name}')

person1 = Person('Jack')
person2 = Person('John')
person3 = Person('Bobik')

def func(*args):
    for i in args:
        try:
            i.show_name()
        except:
            return 'У данного аргумента нет имени'
func(person1, person2, person3)