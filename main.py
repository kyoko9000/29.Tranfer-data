class A():
    def __init__(self):
        super(A, self).__init__()
        self.send()

        print("receive A3: ", self.cc)
    def send(self):
        print("send A1")
        v = (6, 5, 7)
        b = B(index=v)
        b.receive(index=v)
        self.cc = b.receive(index=v)
        print("receive A2: ", self.cc)

class B():
    def __init__(self, index):
        super(B, self).__init__()
        t = index
        print("receive A4: ", t)

    def receive(self, index):
        self.a = index
        print("receive A1: ", self.a)
        n = 2
        return n
A()