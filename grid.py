import numpy as np
import entities as en

class Grid:
    def __init__(self, n):
        self.mat = [[None for i in range(n)] for i in range(n)]

    def list_adj(self, i, j):
        ans = []
        n = len(self.mat)
        if (i - 1) >= 0:
            ans.append((i - 1, j))
        if (j - 1) >= 0:
            ans.append((i, j - 1))
        if (i + 1) < n:
            ans.append((i + 1, j))
        if (j + 1) < n:
            ans.append((i, j + 1))
        return ans
    

    def update_wolf(self, i, j):
        pass

    def update_sheep(self, i, j):
        pass

    def update_grass(self, i, j):
        pass

    def die(self):
        pass

    def reproduct_sheep(self):
        pass

    def reproduct_wolf(self):
        pass

    def update_age(self):
        n = len(self.mat)
        for i in range(n):
            for j in range(n):
                if isinstance(self.mat[i][j], en.Wolf) or isinstance(self.mat[i][j], en.Sheep):
                    self.mat[i][j].age += 1
        return 0


