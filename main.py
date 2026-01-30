import matplotlib.pyplot as plt
from matplotlib import colors
import entities as en 

def afficher_matrice(matrice_animaux, matrice_herbe, liste_couleurs):
    nouvelle_matrice = conversion_état(matrice_animaux, matrice_herbe)
    palette = colors.ListedColormap(liste_couleurs)
    plt.imshow(nouvelle_matrice, cmap=palette)
    plt.show()

def conversion_état(matrice_animaux, matrice_herbe):
    matrice = [[0 for k in range(len(matrice_animaux[0]))] for i in range(len(matrice_animaux))]
    for r in range(len(matrice_animaux[0])):
        for c in range(len(matrice_animaux[0])):
            if isinstance(matrice_animaux[r][c], en.Wolf) :
                matrice[r][c] = 3
            elif isinstance(matrice_animaux[r][c], en.Sheep) :
                matrice[r][c] = 1
    for r in range(len(matrice_herbe[0])):
        for c in range(len(matrice_herbe[0])):
            if isinstance(matrice_animaux[r][c], en.Grass) and matrice[r][c] == 0 :
                if matrice_animaux[r][c].temps_repousse == 0 :
                    matrice[r][c] = 2
    return matrice



mes_couleurs = ['almond', 'whitesmoke', 'green', 'black']

