class MaxSizeList:
    maxSize = 0

    def __init__(self, val):
        self.maxSize = val
        self.list = []

    def push(self, value):
        print "pushing " + value + ", Len = " + str(len(self.list)) + " with maxsize = " + str(self.maxSize)
        if len(self.list) < self.maxSize:
            self.list.append(value)
        elif len(self.list) >= self.maxSize:
            self.list.pop(0)
            self.list.append(value)

    def get_list(self):
        print(self.list)