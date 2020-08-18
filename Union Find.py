class UnionFind:
    def __init__(self, n):
        self.p = [-1] * n

    def find(self, i):
        if self.p[i] < 0: return i
        self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self, i, j):
        i, j = self.find(i), self.find(j)
        if i == j: return
        if self.p[i] > self.p[j]:
            self.p[i] = j
        elif self.p[j] > self.p[i]:
            self.p[j] = i
        else:
            self.p[i] = j
            self.p[j] -= 1