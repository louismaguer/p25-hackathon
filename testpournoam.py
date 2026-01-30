from random import sample
import entities as en

def herbe_aleatoire(n):
    case=[(line,col) for col in range(n) for line in range(n)]
    proba_grass = 0.3
    nb_grass=int(n**2*proba_grass)
    grass=sample(case,nb_grass)
    matrice_herbe=[[0]*n for _ in range(n)]
    for (i,j) in grass :
        matrice_herbe[i][j]=1
    return matrice_herbe

def animaux_aleatoire(n):
    matrice_animaux = [[0]*n for _ in range(n)]
    nb_sheep = 50
    nb_wolf = 10 
    