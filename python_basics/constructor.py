
class Calculator:
    num = 100
    #default constructor
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
        print("I am called automatically when object created")
    def getData(self):
        print("I am now execting as a method in class")

    def summation(self):
        return self.num1 + self.num2 +Calculator.num


obj = Calculator(3,10)
obj.getData()
print(obj.num)
print(obj.summation()+ obj.num)

obj1 = Calculator(2,3)
print(obj1.summation())
