class Employee: 
    def __init__ (self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {} {} {}'.format (self.first,self.last,self.pay,self.email)

emp_1 = Employee('james','gardener',45000) 
emp_2 = Employee('Trinity','Chuks', 65000)

emp_1.fullname()
print(emp_1.fullname())



class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def get_full_info(self):
        return 'First Name: {}\n Last Name: {}\n Salary: {}\n Email: {}'.format(
            self.first, self.last, self.pay, self.email)

emp_1 = Employee('James', 'Gardener', 45000)
emp_2 = Employee('Trinity', 'Chuks', 65000)

# Displaying employee information
print("Employee 1:")
print(emp_1.get_full_info())

print("\nEmployee 2:")
print(emp_2.get_full_info())
