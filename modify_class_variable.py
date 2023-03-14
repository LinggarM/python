class MyClass:
    class_var = 0

    def __init__(self, instance_var):
        self.instance_var = instance_var
        MyClass.class_var += 1
        self.class_var = MyClass.class_var

obj1 = MyClass('obj1')
obj2 = MyClass('obj2')
obj1.class_var = 100
print(obj1.class_var, obj2.class_var)  # output: 100 3