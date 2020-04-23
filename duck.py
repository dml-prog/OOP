class mine:
    def excute(self):
        print("runinng")
        print("duck typing")

class computer:
    def code(self,ide):
        ide.excute
ide =mine()
lp = computer()
lp.code(ide)
