def add_greeting(cls):
    def greeting(self):
        print(f"Hello, I am a {self.__class__.__name__}!")
    cls.greeting = greeting
    return cls

@add_greeting
class MyClass:
    pass

obj = MyClass()
obj.greeting()