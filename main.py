import matplotlib.pyplot as plt
from matplotlib import colors

# --- TA FONCTION ---
def afficher_matrice_facile(matrice, liste_couleurs):
    palette = colors.ListedColormap(liste_couleurs)
    plt.imshow(matrice, cmap=palette)
    plt.show()

# --- TES DONNÉES ---
# Une matrice 3x3 (comme dans ton premier essai)
ma_grille = [
    [0, 1, 2],
    [2, 0, 1],
    [1, 2, 0]
]

# On définit que : 0=Noir, 1=Gris, 2=Vert
mes_couleurs = ['black', 'whitesmoke', 'green']

# --- ON LANCE L'AFFICHAGE ---
afficher_matrice_facile(ma_grille, mes_couleurs)

def conversion_état(matrice_animaux, matrice_herbe):
    