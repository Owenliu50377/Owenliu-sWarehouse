class pile:
    def __init__(self):
        self.one = []

    def __len__(self):
        return len(self.one)

    def empty(self):
        return len(self.one) == 0

    def push(self, e):
        self.one.append(e)

    def top(self):
        if self.empty():
            print('stack is empty')
        else:
            return self.one[self.__len__() - 1]

    def pop(self):
        if self.empty():
            print('stack is empty')
        else:
            return self.one.pop()


class problem:
    def __init__(self, d, a, b, c):
        self.d = d
        self.a = a
        self.b = b
        self.c = c

    def get_d(self):
        return self.d

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c


def Hanoi(d):
    a = 'A'
    b = 'B'
    c = 'C'
    p = pile()
    p.push(problem(d, a, b, c))
    while len(p) != 0:
        currentProblem = p.top()
        p.pop()
        if currentProblem.get_d() == 1:
            print(currentProblem.get_a(), '-->', currentProblem.get_c())
        else:
            p.push(problem(currentProblem.get_d() - 1, currentProblem.get_b(), currentProblem.get_a(),
                           currentProblem.get_c()))
            p.push(problem(1, currentProblem.get_a(), currentProblem.get_b(), currentProblem.get_c()))
            p.push(problem(currentProblem.get_d() - 1, currentProblem.get_a(), currentProblem.get_c(),
                           currentProblem.get_b()))


n = int(input('input an integer:'))
Hanoi(n)
