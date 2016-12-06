class MyNum:
    def __init__(self):
        print ('Calling __init__')
        self.val = 0
        self.abc = 1


instance = MyNum()
print(instance.val)
print(instance.abc)