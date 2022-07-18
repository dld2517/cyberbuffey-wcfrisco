# Testing a class instance method as well as a static method

class Student:
    name = "A Brady"
    #The class is called Student, when it is initiialized, an object will be created with the
    #class type of Student. The object will be named it's local variable.

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def avg(self):
        # This is an instance method. It is a function. 
        return (self.a + self.b) / 2

    def sum(self):
        # Another instance method
        return (self.a + self.b)
    
    @classmethod
    def info(cls):
        return cls.name


s1 = Student(10,20)
print("Average: ",s1.avg())
print("Sum:     ",s1.sum())
print(s1.info())


