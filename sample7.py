##
##  It is Python OOP Tutorial 6: Property Decorators
#  - Getters, Setters, and Deleterss usage and subclass usage
##
class Employee:
    raise_amt  = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@company.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete NAme!')
        self.first = None
        self.last = None


emp_1 = Employee ('John','Smith' )


emp_1.fullname = 'Corey Schafer'
#
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname


# emp_2 = Employee ('Test','User')


# print("Employee Name lenght : {}".format(emp_1.__len__()))
# print(emp_1.__repr__())