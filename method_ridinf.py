class A:
    def sum(self):
        print("This is sum")

class B(A):
    def sum(self):
        print("This is inheritated")

a1 = B()
print(a1.sum())