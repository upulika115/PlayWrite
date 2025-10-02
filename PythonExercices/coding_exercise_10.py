class BasicCalculator:

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2


obj1 = BasicCalculator(10, 5)
obj1.addition()
print("Addition:", "{}{}{}".format(obj1.num1, "+", obj1.num2), "=", obj1.addition())

obj2 = BasicCalculator(10, 5)
obj2.subtraction()
print("Subtraction:", "{}{}{}".format(obj1.num1, "-", obj1.num2), "=", obj1.subtraction())

obj3 = BasicCalculator(10, 5)
obj3.multiplication()
print("Multiplication:", "{}{}{}".format(obj1.num1, "*", obj1.num2), "=", obj1.multiplication())

obj4 = BasicCalculator(10, 5)
obj4.division()
print("Division:", "{}{}{}".format(obj1.num1, "/", obj1.num2), "=", obj1.division())

