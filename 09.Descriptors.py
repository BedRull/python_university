
class MyType(type):
    def __new__(cls, clsName, clsParents, clsAtrDict):
        cls.dict_attributes = clsAtrDict
        print(clsAtrDict)
        return type.__new__(cls, clsName, clsParents, clsAtrDict)

    def someFunc(self, value):
        for i in self.dict_attributes.values():
            if i == value:
                print("success")



class ShowAccess():
    __metaclass__ = MyType
    def __init__(self, value=0):
        self.value = value

    def __set__(self, instance, value):
        pass
        # print(vars(self.__metaclass__).keys())
        # print(instance.__class__.__dict__.keys())

    def __get__(self, owner, value):
        MyType.someFunc(MyType, value)

    def __delete__(self, instance):
        print("__delete__ called")


class Temperature(metaclass=MyType):
    celcius = ShowAccess()
    fahrenheit = ShowAccess()

class TemperatureChild(Temperature):
    pass

temp = Temperature()

temp.celcius = 20
