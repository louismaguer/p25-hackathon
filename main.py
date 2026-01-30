import matplotlib.pyplot as plt
from matplotlib import colors
import entities as en 
import grid as gr

# Fonction qui permet de convertir les classes des animaux en entier pour simplifier la matrice
# Cette fonction sert uniquement pour permettre l'affichage dans afficher_matrice
def conversion_etat(matrice_animaux, matrice_herbe):
    matrice = [[0 for k in range(len(matrice_animaux[0]))] for i in range(len(matrice_animaux))]
    for r in range(len(matrice_animaux[0])):
        for c in range(len(matrice_animaux[0])):
            if isinstance(matrice_animaux[r][c], en.Wolf) :
                matrice[r][c] = 3
            elif isinstance(matrice_animaux[r][c], en.Sheep) :
                matrice[r][c] = 1
    for r in range(len(matrice_herbe[0])):
        for c in range(len(matrice_herbe[0])):
            if isinstance(matrice_herbe[r][c], en.Grass) and matrice[r][c] == 0 :
                if matrice_herbe[r][c].temps_repousse == 0 :
                    matrice[r][c] = 2
    return matrice

# Fonction qui permet d'afficher la matrice avec des couleurs
def afficher_matrice(matrice_animaux, matrice_herbe, liste_couleurs):
    nouvelle_matrice = conversion_etat(matrice_animaux, matrice_herbe)
    palette = colors.ListedColormap(liste_couleurs)
    plt.imshow(nouvelle_matrice, cmap=palette)
    plt.show()

mes_couleurs = ['khaki', 'whitesmoke', 'green', 'black']


def main(n):
    animals = []
    herbs = []
    g = gr.init_grid(n)
    animals.append(g.mat)
    herbs.append(g.grass)
    while (gr.update(g) == 1):
        animals.append(g.mat)
        herbs.append(g.grass)
    palette = colors.ListedColormap(mes_couleurs)
    matrices = [conversion_etat(taba, tabb) for (taba, tabb) in zip(animals, herbs)]
    i = 0
    fig, ax = plt.subplots()
    im = ax.imshow(matrices[i], cmap=palette)
    ax.axis("off")
    ax.set_title(f"Tour numéro {i}")

    def on_key(event):
        global i
        if event.key == "right":
            i = min(i + 1, len(matrices) - 1)
        elif event.key == "left":
            i = max(i - 1, 0)
        else:
            return
        im.set_data(matrices[i])
        ax.set_title(f"Tour numéro {i}")
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect("key_press_event", on_key)
    plt.show()

main(en.GRID_SIZE)