import numpy as np
import entities as en
import random

class Grid:
    def __init__(self, n):
        self.mat = [[0 for i in range(n)] for i in range(n)]
        self.grass = [[0 for i in range(n)] for i in range(n)]

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
        wolf_=self.mat[i][j]
        adj=self.list_adj(self,i,j)
        sheep_coos=[k for k in adj if isinstance(self.mat[k[0]][k[1]],en.Sheep)]
        if sheep_coos:
            nx,ny=random.choice(sheep_coos)
            self.mat[i][j]=0
            self.mat[nx][ny]=wolf_
            wolf_.move(nx,ny)
            wolf_.energie += en.WOLF_ENERGY_FROM_SHEEP
        else: 
            Vide=[k for k in adj if self.mat[k[0]][k[1]]==0]
            if Vide: 
                nx,ny=random.choice(Vide)
                self.mat[i][j]=0
                self.mat[nx][ny]=wolf_
                wolf_.move(nx,ny)
        wolf_.energie -=en.WOLF_ENERGY_LOSS_PER_TURN

    def update_sheep(self, i, j):
        pass

    def update_grass(self, i, j):
        for p in range(len(self.mat)):
            for q in range(len(self.mat)) :
                if self.mat[pq] == 0 :
                    if np.random.uniform() <= en.GRASS_GROWTH_PROBABILITY :
                        self.mat[p,q] = en.Grass()
        pass

    def die(self):
        pass

    def reproduct_sheep(self):
        pass

    def reproduct_wolf(self):
        wolf_coo=[]
        for i in range (len(self.mat)):
            for j in range (len(self.mat)):
                if isinstance(self.mat[i][j],en.Wolf):
                    wolf_coo.append((i,j))
        for (k,l) in wolf_coo:
            parents=self.mat[k][l]
            if parents.can_reprod():
                A=self.list_adj(k,l)
                Vide=[v for v in A if self.mat[v[0]][v[1]]==0]
                if Vide:
                    nx,ny=random.choice(Vide)
                    self.mat[nx][ny]=en.Wolf(nx,ny,0,en.WOLF_INITIAL_ENERGY)
                    parents.energie -= en.REPRODUCTION_ENERGY_COST

    def update_age(self):
        n = len(self.mat)
        for i in range(n):
            for j in range(n):
                if isinstance(self.mat[i][j], en.Wolf) or isinstance(self.mat[i][j], en.Sheep):
                    self.mat[i][j].age += 1
        return 0


