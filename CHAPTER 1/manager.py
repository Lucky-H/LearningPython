#! python

"""
@author: "Lucky-H"
@file: manager
@date: 2018-08-05
@time: 23:08:59
"""


from person import Person


class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def give_raise(self, percent, bouns=0.1):
        Person.give_raise(self, percent + bouns)


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Manager('Sue Jones', 45, 40000)
    print(bob.name, sue.pay)
    print(sue.job)
    print(bob.last_name())
    sue.give_raise(0.10)
    print(sue.pay)
