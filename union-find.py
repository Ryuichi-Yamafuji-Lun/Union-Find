#union find algorithm

class QuickFind():
    def __init__(self):
        self.id = []
    def init_QF(self, N):
        for i in range(N):
            self.id.append(i)

    def connected(self, p, q):
        if self.id[p] == self.id[q]:
            print("T")
        else:
            print("F")
    
    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid

class QuickUnion():
    def __init__(self):
        self.id = []
    
    def init_QU(self, N):
        for i in range(N):
            self.id.append(i)
    
    def root(self, num):
        while num != self.id[num]:
            num = self.id[num]
        return num
    
    def connected(self, p, q):
        if self.root(p) == self.root(q):
            print("T")
        else:
            print("F")
    
    def union(self, p, q):
        root_pid = self.root(p)
        root_qid = self.root(q)
        self.id[root_pid] = root_qid
    
class WeightedQuickUnion():
    def __init__(self):
        self.id = []
        self.sz = []

    def init_WQU(self, N):
        for i in range(N):
            self.id.append(i)
            self.sz.append(1)
    
    def root(self, num):
        while self.id[num] != num:
            num = self.id[num]
        return num
    
    def connected(self, p, q):
        if self.root(p) == self.root(q):
            print("T")
        else:
            print("F")

    def union(self, p, q):
        root_pid = self.root(p)
        root_qid = self.root(q)
        if root_pid == root_qid:
            return
        if (self.sz[root_pid] < self.sz[root_qid]):
            self.id[root_qid] = root_pid
            self.sz[root_qid] += self.sz[root_pid]
        else:
            self.id[root_pid] = root_qid
            self.sz[root_pid] += self.sz[root_qid]

class WeightedQuickUnionwithPathCompression():
    def __init__(self):
        self.id = []
        self.sz = []

    def init_WQU(self, N):
        for i in range(N):
            self.id.append(i)
            self.sz.append(1)
    
    def root(self, num):
        while self.id[num] != num:
            self.id[num] = self.id[self.id[num]]
            num = self.id[num]
        return num
    
    def connected(self, p, q):
        if self.root(p) == self.root(q):
            print("T")
        else:
            print("F")

    def union(self, p, q):
        root_pid = self.root(p)
        root_qid = self.root(q)
        if root_pid == root_qid:
            return
        if (self.sz[root_pid] < self.sz[root_qid]):
            self.id[root_qid] = root_pid
            self.sz[root_qid] += self.sz[root_pid]
        else:
            self.id[root_pid] = root_qid
            self.sz[root_pid] += self.sz[root_qid]

def main():
    print("Quick Find")
    qf = QuickFind()
    qf.init_QF(10)
    qf.connected(2,3)
    qf.union(2,3)
    qf.connected(2,3)
    print("Quick Union")
    qu = QuickUnion()
    qu.init_QU(10)
    qu.connected(2,3)
    qu.union(2,1)
    qu.union(1,5)
    qu.union(3,5)
    qu.connected(2,3)
    print("Weighted Quick Union")
    wqu = WeightedQuickUnion()
    wqu.init_WQU(10)
    wqu.connected(2,3)
    wqu.union(2,1)
    wqu.union(1,5)
    wqu.union(3,5)
    wqu.connected(2,3)
    print("Weighted Quick Union with Path Compression")
    pc = WeightedQuickUnionwithPathCompression()
    pc.init_WQU(10)
    pc.connected(2,3)
    pc.union(2,1)
    pc.union(1,5)
    pc.union(3,5)
    pc.connected(2,3)
main()