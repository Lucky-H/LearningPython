#! python

"""
@author: "Lucky-H"
@file: person
@date: 2018-08-05
@time: 22:51:15
"""


from person_start import PersonStart


class Person(PersonStart):
    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(bob.name, sue.pay)

    print(bob.last_name())
    sue.give_raise(0.10)
    print(sue.pay)
