#class Person:
#    pass

#class Person:
#    def __init__(self, name, job, pay): # Constructor takes three arguments
#        self.name = name # Fill out fields when created
#        self.job = job # self is the new instance object
#        self.pay = pay

class Person:
    def __init__(self, name, job=None, pay=0): # Normal function args
        self.name = name
        self.job = job
        self.pay = pay

    #def lastName(self):  # Behavior methods
    #   return self.name.split()[-1]  # self is implied subject

    #def giveRaise(self, percent):
    #   self.pay = int(self.pay * (1 + percent))


    #def __repr__(self):  # Added method
    #    return '[Person: %s, %s]' % (self.name, self.pay)

#bob = Person('Bob Smith') # Test the class
#sue = Person('Sue Jones', job='dev', pay=100000) # Runs __init__ automatically
#print(bob.name, bob.pay) # Fetch attached attributes
#print(sue.name, sue.pay) # sue's and bob's attrs differ


if __name__ == '__main__': # When run for testing only
    # self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)

#    name = 'Bob Smith'  # Simple string, outside class
#     name.split()  # Extract last name
#     >>> ['Bob', 'Smith']#
#    name.split()[-1]  # Or [1], if always just two parts
#     >>>'Smith'
#     pay = 100000 # Simple variable, outside class
#     >>> pay *= 1.10 # Give a 10% raise
#     >>> print('%.2f' % pay) # Or: pay = pay * 1.10, if you like to type
#     110000.00

    # print(bob.name.split()[-1]) # Extract object's last name
    # sue.pay *= 1.10 # Give this object a raise
    # print('%.2f' % sue.pay)

    #print(bob.lastName(), sue.lastName())  # Use the new methods
    #sue.giveRaise(.10)  # instead of hardcoding
    #print(sue.pay)
    #print (sue)
