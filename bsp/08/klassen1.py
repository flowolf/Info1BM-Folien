class MyClass:
  globalClassCount = 0
  def __init__(self, initialData):
    self.data = initialData
    MyClass.globalClassCount += 1

  def getData(self):
    return self.data
  def getClassCount(self):
    return MyClass.globalClassCount



class1 = MyClass(1)
class2 = MyClass(5)

print(class1.getData())
print(class2.getClassCount())

