class FenwickTree:
    def __init__(self, values):
        self.n = len(values)
        self.tree = [0] * (self.n + 1)

        for index, value in enumerate(values):
            print("beginning")
            print("index = ",index)
            print("value = ", value)
            self.add(index, value)

    def add(self, index, delta):
        i = index + 1

        while i <= self.n:
            print("while-i = ", i)
            self.tree[i] += delta
            i += i & -i
            print("end-while-i = ", i)
            print("=========")



fenwick = FenwickTree([2, 4, 5])
print(fenwick.tree)
