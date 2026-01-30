import numpy as np

class Grid:
    def __init__(self, n):
        self.mat = np.zeros((n,n), dtype=np.int)
        self.age = 0

    def list_adj(self, i, j):
        pass

