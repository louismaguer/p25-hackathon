import numpy as np
import entities as en
import random

class Grid:
    def __init__(self, n):
        self.mat = [[0 for i in range(n)] for i in range(n)]

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
    
    def update(self):
        pass

    def update_wolf(self, i, j):
        Wolf=self.mat[i][j]
        adj=self.list_adj(self,i,j)
        Sheep=[k for k in adj if isinstance(self.mat[k[0]][k[1]],en.Sheep)]
        if Sheep:
            nx,ny=random.choice(Sheep)
            self.mat[i][j]=0
            self.mat[nx][ny]=Wolf
            Wolf.move(nx,ny)
        else: 
            Vide=[k for k in adj if self.mat[k[0]][k[1]]==0]

    def update_sheep(self, i, j):
        pass

    def update_grass(self, i, j):
        pass