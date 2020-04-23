from abc import ABC,abstractmethod
class student:
    @abstractmethod
    def process(self):
        pass
class laptop:
    def lap1(self):
        print("Solving Bugs")

class programmer:
    def work(self,com):
        print("Cool this is ruuning")
        com.lap1()

com1 = laptop()
prog1= programmer()
prog1.work(com1)