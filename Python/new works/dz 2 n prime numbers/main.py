class Numbers:
    def __init__(self, max):
        self.max = max + 1

    def __iter__(self):
        self.count = 0
        self.ln = 1
        return self

    def __next__(self):
        self.count += 1
        for i in range(self.ln + 1, self.max * self.max):
            delt = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    delt += 1

            if delt <= 2:
                if self.count < self.max:
                    self.ln = i
                    break

        if self.count > self.max:
            raise StopIteration
        return self.ln

a = Numbers(10)

for i in a:
    print(i)