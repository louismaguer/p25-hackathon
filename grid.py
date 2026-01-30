import entities as en
import numpy as np
import random
from random import sample


class Grid:
    def __init__(self, n):
        self.mat = [[0 for i in range(n)] for i in range(n)]
        self.grass = [[0 for i in range(n)] for i in range(n)]
        self.tour = 0

    # Fonction qui liste les cases adjacentes
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
    
    # Fonction qui met à jour la position du loup, soit en le déplaçant soit en le faisant
    # manger un mouton
    def update_wolf_one_cell(self, i, j):
        wolf_=self.mat[i][j]
        if self.tour > wolf_.turn:
            adj=Grid.list_adj(self,i,j)
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
            wolf_.turn +=1

    # Fonction qui met à jour la position du mouton, soit en le déplaçant soit en le faisant
    # manger de l'herbe
    def update_sheep_one_cell(self, i, j):
        sheep_=self.mat[i][j]
        if self.tour > sheep_.turn:
            adj=Grid.list_adj(self,i,j)
            grass_coos=[k for k in adj if isinstance(self.grass[k[0]][k[1]],en.Grass)]
            if grass_coos:
                nx,ny=random.choice(grass_coos)
                self.mat[i][j]=0
                self.mat[nx][ny]=sheep_
                self.mat[nx][ny].turn = self.tour
                self.grass[nx][ny].temps_repousse=en.GRASS_REGROWTH_TIME
                sheep_.move(nx,ny)
                sheep_.energie += en.SHEEP_ENERGY_FROM_GRASS
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
            sheep_.turn +=1

    # Fonction qui met à jour tous les loups en faisant appel à la fonction update_wolf_one_cell
    def update_wolf(self):
        n = len(self.mat)
        for i in range(n):
            for j in range(n):
                if isinstance(self.mat[i][j], en.Wolf):
                    Grid.update_wolf_one_cell(self,i,j)

    # Fonction qui met à jour tous les mouton en faisant appel à la fonction update_sheep_one_cell
    def update_sheep(self):
        n = len(self.mat)
        for i in range(n):
            for j in range(n):
                if isinstance(self.mat[i][j], en.Sheep):
                    Grid.update_sheep_one_cell(self, i,j)
        
    # Fonction qui met à jour l'état de l'herbe en la regénérant et ajoute aléatoirement de l'herbe
    def update_grass(self):
        for i in range(len(self.grass)):
            for j in range(len(self.grass)) :
                if isinstance(self.grass[i][j], en.Grass) :
                    if self.grass[i][j].temps_repousse > 0 :
                        self.grass[i][j].temps_repousse -= 1
                if self.grass[i][j] == 0 :
                    if np.random.uniform() <= en.GRASS_GROWTH_PROBABILITY :
                        self.grass[i][j] = en.Grass(i,j)

    # Fonction qui tue les moutons et les loups
    def die(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat)) :
                if isinstance(self.mat[i][j], (en.Sheep, en.Wolf)) :
                    if self.mat[i][j].is_dead() :
                        self.mat[i][j] = 0

    # Fonction qui fait apparaitre un nouveau mouton sur une case adjacente au mouton
    # qui lui donne naissance
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
                    self.mat[nx][ny]=en.Sheep(nx,ny,0,en.SHEEP_INITIAL_ENERGY)
                    parents.energie -= en.REPRODUCTION_ENERGY_COST

    # Fonction qui fait apparaitre un nouveau loup sur une case adjacente au loup qui
    # lui donne naissance
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

    # Fonction qui permet de compter l'age des animaux
    def update_age(self):
        n = len(self.mat)
        for i in range(n):
            for j in range(n):
                if isinstance(self.mat[i][j], en.Wolf) or isinstance(self.mat[i][j], en.Sheep):
                    self.mat[i][j].age += 1
        return 0
    
    # Fonction qui arrête la simulation si on est arrivé à la fin
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
            j = 0
            while (not any_animal) and j < n:
                if isinstance(g.mat[i][j], en.Wolf) or isinstance(g.mat[i][j], en.Sheep):
                    any_animal =  True
                j+= 1
            i+=1
        if not any_animal:
            return 1
        return 0
    
# Fonction qui génère une matrice remplie d'herbe à la densité désirée, de manière aléatoire
def herbe_aleatoire(n):
    case=[(line,col) for col in range(n) for line in range(n)]
    proba_grass = 0.3
    nb_grass=int(n**2*proba_grass)
    grass=sample(case,nb_grass)
    matrice_herbe=[[0]*n for _ in range(n)]
    for (i,j) in grass :
        matrice_herbe[i][j]=en.Grass(i,j)
    return matrice_herbe

# Fonction qui génère une matrice remplie du nombre de loups et de moutons désiré, de manière aléatoire
def animaux_aleatoire(n):
    matrice_animaux = [[0]*n for _ in range(n)]
    case=[(line,col) for col in range(n) for line in range(n)]
    nb_sheep = 50
    nb_wolf = 10 
    echantillon = sample(case, nb_sheep + nb_wolf)
    for (i,j) in echantillon[:50] :
        matrice_animaux[i][j] = en.Sheep(i,j,0, en.SHEEP_INITIAL_ENERGY)
    for (i,j) in echantillon[50:] :
        matrice_animaux[i][j] = en.Wolf(i,j,0, en.WOLF_INITIAL_ENERGY)
    return matrice_animaux

# Fonction qui met à jour la grille
def update(g):
    Grid.update_age(g)
    Grid.update_grass(g)
    Grid.update_sheep(g)
    Grid.update_wolf(g)
    Grid.die(g)
    Grid.reproduct_sheep(g)
    Grid.reproduct_wolf(g)
    g.tour += 1
    return Grid.end_simulation(g)

def init_grid(n):
    g = Grid(n)
    mat_an = animaux_aleatoire(n)
    mat_he = herbe_aleatoire(n)
    g.mat = mat_an
    g.grass = mat_he
    return g

