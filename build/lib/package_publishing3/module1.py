class DoMath:

    def __init__(self, do_add=0, do_sub=0):
        self.add = do_add
        self.sub = do_sub

    def fit(self,a=2,b=2):
        if self.add:
            self.answer = a + b
        else:
            self.answer = a - b

    def predict(self):
        return self.answer

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b