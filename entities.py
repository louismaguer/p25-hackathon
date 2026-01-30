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
    def _init_(self, position_x: float, position_y: float, age: int, energie:int):
        self.position_x = position_x
        self.position_y = position_y
        self.age = age
        self.energie = energie
    
    def is_dead(self):
        return self.energie <= 0 or self.age >= SHEEP_MAX_AGE
    
    def can_reprod(self):
        if 'case adjacente de vide' and self.energie >= SHEEP_REPRODUCTION_THRESHOLD :
            return Sheep('x adjacent', 'y adjacent', 0, SHEEP_INITIAL_ENERGY)
    
    def can_eat(self):''

class Wolf :
    def _init_ (self, position_x: float,position_y:float,age:int,energie:int):
        self.position_x=position_x
        self.position_y=position_y
        self.age=age
        self.energie=energie
    
    def is_dead(self):
        return self.energie<=0 or self.age>=WOLF_MAX_AGE
    
    def move(self,grid):
        list_adj = grid.list_adj(self.position_x, self.position_y)

    def can_eat(self,grid):
        return #mouton a coté
    def can_reprod(self,grid):
        if '''case adjacent libre''' and self.energie>=WOLF_REPRODUCTION_THRESHOLD:
            return Wolf('nx','ny',0,WOLF_INITIAL_ENERGY)


    pass

class Grass :
    pass
