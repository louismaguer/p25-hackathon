# Configuration initiale
GRID_SIZE = 30
INITIAL_SHEEP = 50
INITIAL_WOLVES = 10
INITIAL_GRASS_COVERAGE = 0.3
#30% de la grille
# Énergie
SHEEP_INITIAL_ENERGY = 20
WOLF_INITIAL_ENERGY = 40
SHEEP_ENERGY_FROM_GRASS = 15
WOLF_ENERGY_FROM_SHEEP = 35
SHEEP_ENERGY_LOSS_PER_TURN = 1
WOLF_ENERGY_LOSS_PER_TURN = 2 # Les loups perdent plus d'énergie
# Reproduction
SHEEP_REPRODUCTION_THRESHOLD = 50
WOLF_REPRODUCTION_THRESHOLD = 80
REPRODUCTION_ENERGY_COST = 20
# Âge
SHEEP_MAX_AGE = 50
# Tours avant mort naturelle
WOLF_MAX_AGE = 40
# Herbe
GRASS_GROWTH_PROBABILITY = 0.08
GRASS_REGROWTH_TIME = 7
# Simulation
MAX_TURNS = 500 # Nombre maximum de tours

class Sheep :
    def __init__(self, position_x: int, position_y: int, age: int, energie:int):
        self.position_x = position_x
        self.position_y = position_y
        self.age = age
        self.energie = energie
        self.turn = -1
    
    # Fonction renvoyant un booléen pour savoir si le mouton meurt
    def is_dead(self):
        return self.energie <= 0 or self.age >= SHEEP_MAX_AGE
    
    # Fonction renvoyant un booléen pour savoir si le mouton peut se reproduire
    def can_reprod(self):
        return self.energie >= SHEEP_REPRODUCTION_THRESHOLD
    
    # Fonction qui met à jour la position du mouton
    def move(self, i: float, j: float):
        self.position_x = i
        self.position_y = j

class Wolf :
    def __init__ (self, position_x: int,position_y:int,age:int,energie:int):
        self.position_x=position_x
        self.position_y=position_y
        self.age=age
        self.energie=energie
        self.turn = -1
    
    # Fonction renvoyant un booléen pour savoir si le loup meurt
    def is_dead(self):
        return self.energie<=0 or self.age>=WOLF_MAX_AGE
    
    # Fonction renvoyant un booléen pour savoir si le loup peut se reproduire
    def move(self, i: float, j: float):
        self.position_x = i
        self.position_y = j   

    # Fonction qui met à jour la position du loup
    def can_reprod(self,grid):
        return self.energie>=WOLF_REPRODUCTION_THRESHOLD

class Grass :
    def __init__(self, position_x: int, position_y: int, temps_repousse: int=0):
        self.position_x = position_x
        self.position_y = position_y
        self.temps_repousse = temps_repousse # = 0 : l'herbe est vivante /
                                                  # = d (> 0) : l'herbe se régénère dans d cycles