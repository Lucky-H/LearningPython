#! python

"""
@author: "Lucky-H"
@file: person_start
@date: 2018-08-05
@time: 21:13:21
"""


class PersonStart:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job


if __name__ == '__main__':
    bob = PersonStart('Bob Smith', 42, 30000, 'software')
    sue = PersonStart('Sue Jones', 45, 40000, 'hardware')
    print(bob.name, sue.pay)
    print(bob.name.split()[-1])
    sue.pay *= 1.10
    print(sue.pay)
