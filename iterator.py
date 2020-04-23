class topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <25:
            val = self.num
            self.num+=1
            return val
        else:raise Exception

n = topten()
print(next(n))

for i in n:
    print(i)