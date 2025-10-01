#classe are user defined blueprint or prototypes

class calculator:
    num = 100
    def __init__(self):
        print("called automatically when object is created")

    def getData(self):
        print("methosd and classes")

obj = calculator()
obj.getData()
print(obj.num)