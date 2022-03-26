# multilevel inheritance

class dad:
    basketball = 1

class son(dad):
    dance = 2
    def indance(self):
        return f'yes i dance {self.dance}'

class grandson(son):
    move = 4
    def run(self):
        return f"i am running {self.move}"

dan = grandson()
jim = son()
print(dan.basketball)
print(dan.indance())