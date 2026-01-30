import matplotlib.pyplot as plt
import main as mn
import grid as gr

def simuler_le_grid(mon_grid, nb_tours):
    """
    mon_grid : l'objet que tu as créé (celui qui a .mat)
    nb_tours : le nombre de fois qu'on veut voir l'évolution
    """
    # 1. On active le mode interactif
    plt.ion()
    mes_couleurs = ['khaki', 'whitesmoke', 'green', 'black']
    for i in range(nb_tours):
        # 2. On vide l'écran
        plt.clf() 
        
        # 3. ON AFFICHE : On passe la MATRICE contenue dans le grid
        # On suppose que ta fonction s'appelle afficher_matrice
        mn.afficher_matrice(mon_grid.mat, mon_grid.grass, mes_couleurs)
        
        # 4. ON FAIT ÉVOLUER : On appelle la fonction de ton objet 
        # (Vérifie dans ton fichier grid.py si elle s'appelle update ou evoluer)
        gr.update(mon_grid) 
        
        # 5. On rafraîchit l'image
        plt.title(f"Tour n°{i}") # Petit bonus : affiche le tour en haut
        plt.pause(0.1)
        
    plt.ioff()
    plt.show()