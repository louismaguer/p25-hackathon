import entities as en
import numpy as np
import random

class Grid:
    def __init__(self, n):
        self.mat = [[0 for i in range(n)] for i in range(n)]
        self.grass = [[0 for i in range(n)] for i in range(n)]
        self.tour = 0

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
    

    def update_wolf_one_cell(self, i, j):
        wolf_=self.mat[i][j]
        if self.tour > wolf_.turn:
            adj=self.list_adj(self,i,j)
            sheep_coos=[k for k in adj if isinstance(self.mat[k[0]][k[1]],en.Sheep)]
            if len(sheep_coos) > 0:
                nx,ny=random.choice(sheep_coos)
                self.mat[i][j]=0
                self.mat[nx][ny]=wolf_
                self.mat[nx][ny].turn = self.tour
                wolf_.move(nx,ny)
                wolf_.energie += en.WOLF_ENERGY_FROM_SHEEP
            else: 
                Vide=[k for k in adj if self.mat[k[0]][k[1]]==0]
                if len(Vide) > 0: 
                    nx,ny=random.choice(Vide)
                    self.mat[i][j]=0
                    self.mat[nx][ny]=wolf_
                    self.mat[nx][ny].turn = self.tour
                    wolf_.move(nx,ny)
            wolf_.energie -= en.WOLF_ENERGY_LOSS_PER_TURN

    def update_sheep_one_cell(self, i, j):
        sheep_=self.mat[i][j]
        if self.tour > sheep_.turn:
            adj=self.list_adj(self,i,j)
            grass_coos=[k for k in adj if isinstance(self.grass[k[0]][k[1]],en.Grass)]
            if grass_coos:
                nx,ny=random.choice(grass_coos)
                self.mat[i][j]=0
                self.mat[nx][ny]=sheep_
                self.mat[nx][ny].turn = self.tour
                sheep_.move(nx,ny)
                sheep_.energie += en.WOLF_ENERGY_FROM_SHEEP
            else: 
                Vide=[k for k in adj if self.mat[k[0]][k[1]]==0]
                if Vide:
                    for v in Vide: 
                        if v not in grass_coos:
                            nx,ny=random.choice(Vide)
                            self.mat[i][j]=0
                            self.mat[nx][ny]=sheep_
                            self.mat[nx][ny].turn = self.tour
                            sheep_.move(nx,ny)
            sheep_.energie -=en.SHEEP_ENERGY_LOSS_PER_TURN

    def update_wolf(self):
        n = len(self.mat)
        for i in range(n):
            for j in range(n):
                Grid.update_wolf_one_cell(self,i,j)

    def update_sheep(self):
        n = len(self.mat)
        for i in range(n):
            for j in range(n):
                Grid.update_wolf_one_cell(self, i,j)
        

    def update_grass(self):
        for i in range(len(self.grass)):
            for j in range(len(self.grass)) :
                if isinstance(self.grass[i][j], en.Grass) :
                    if self.grass[i][j].temps_repousse > 0 :
                        self.grass[i][j].temps_repousse -= 1
                if self.grass[i][j] == 0 :
                    if np.random.uniform() <= en.GRASS_GROWTH_PROBABILITY :
                        self.grass[i][j] = en.Grass(i,j)

    def die(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat)) :
                if isinstance(self.mat[i][j], (en.Sheep, en.Wolf)) :
                    if self.mat[i][j].isdead(self) :
                        self.mat[i][j] = 0

    def reproduct_sheep(self):
        sheep_coo=[]
        for i in range (len(self.mat)):
            for j in range (len(self.mat)):
                if isinstance(self.mat[i][j],en.Sheep):
                    sheep_coo.append((i,j))
        for (k,l) in sheep_coo:
            parents=self.mat[k][l]
            if parents.can_reprod():
                A=self.list_adj(k,l)
                Vide=[v for v in A if self.mat[v[0]][v[1]]==0]
                if Vide:
                    nx,ny=random.choice(Vide)
                    self.mat[nx][ny]=en.Wolf(nx,ny,0,en.SHEEP_INITIAL_ENERGY)
                    parents.energie -= en.REPRODUCTION_ENERGY_COST

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
    
    def end_simulation(g):
        """
        Docstring for end_simulation
        
        :param g: Grid

        This function returns 1 if all ending conditions are met, 0 if not.
        """
        n = len(g.mat)
        if g.tour >= en.MAX_TURNS:
            return 1
        any_animal = False
        i = 0
        j = 0
        while (not any_animal) and i < n:
            while (not any_animal) and j < n:
                if isinstance(g.mat[i][j], en.Wolf) or isinstance(g.mat[i][j], en.Sheep):
                    any_animal =  True
        if not any_animal:
            return 1
        return 0



def update(g):
    Grid.update_age(g)
    Grid.update_grass(g)
    Grid.update_sheep(g)
    Grid.update_grass(g)
    Grid.die(g)
    Grid.reproduct_sheep(g)
    Grid.reproduct_wolf(g)
    g.tour += 1
    return Grid.end_simulation(g)


