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

    def update_grass(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat)) :
                if isinstance(self.mat[i][j], en.Grass) :
                    if self.mat[i][j].self.temps_repousse > 0 :
                        self.mat[i][j].self.temps_repousse -= 1
                if self.mat[i][j] == 0 :
                    if np.random.uniform() <= en.GRASS_GROWTH_PROBABILITY :
                        self.mat[i][j] = en.Grass(i,j)

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
    
    def end_simulation(g):
        """
        Docstring for end_simulation
        
        :param g: Grid

        This function returns 1 if all ending conditions are met, 0 if not.
        """
        pass
    


def update(g):
    Grid.update_age(g)
    Grid.update_grass(g)
    Grid.update_sheep(g)
    Grid.update_grass(g)
    Grid.die(g)
    Grid.reproduct_sheep(g)
    Grid.reproduct_wolf(g)

