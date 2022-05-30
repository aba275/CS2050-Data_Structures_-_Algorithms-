class midterm():
    def func(self,a, b):
        if b == 0:
            return 0
        elif b == 1:
            return a
        else:
            return a + func(a, b-1)