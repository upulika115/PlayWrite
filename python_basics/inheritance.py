from python_basics.constructor import Calculator



class ChildImplem(Calculator):
    num2 = 1000

    def __init__(self):
        Calculator.__init__(self ,100, 30)

    def getCompleteData(self):
        return ChildImplem.num2 + self.num + self.summation()

obj = ChildImplem()
print(obj.getCompleteData())