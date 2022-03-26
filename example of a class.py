import copy

class animals():
    def breath(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat_food(self):
        print('eating food')


class mammals(animals):
    def feed_young_with_milk(self):
        print('feeding young')


class giraffe(mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves')
    def find_food(self):
        self.move()      #this function is calling another function
        print('i have found food!')
        self.eat_food()
    def dance(self):
        self.move()
        self.move()
        self.move()
        self.move()


class skin:
    def __init__(self,spots):
        self.giraffe_spots = int(spots)


class type:
    def __init__(self,species,number_of_legs,color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color


#brawny,tobo,lambu and papu is the name of 2 giraffe(object)
brawny = giraffe()
papu = giraffe()
tobo = giraffe()
brawny.move()
papu.eat_leaves_from_trees()
tobo.find_food()
brawny.dance()
print('________________')

lambu = skin(100)
print(lambu.giraffe_spots)
print('________________')

harry = type('hippogiraff',6, 'pink')
print('________________')
# imported copy module on top

gene = copy.copy(harry)
print(harry.species)
print(gene.species)
print('________________')

# harry,gene ,billy, carrie are name of the animals

carrie = type('chimera',4,'green polka dots')
billy = type('bogill',0,'paisley')
my_animals = [harry,carrie,billy]
more_animals = copy.copy(my_animals)
print(more_animals[0].species)
print(more_animals[1].species)
print(my_animals[2].species)
print('________________')

my_animals[0].species = 'ghoul'
print(my_animals[0].species)
print(more_animals[0].species)
print('________________')

sally = type('sphinx',4,'sand')
my_animals.append(sally)
print(len(my_animals))
print(len(more_animals))
print('________________')

more_animals = copy.deepcopy(my_animals)
my_animals[0].species = 'wyrm'
print(my_animals[0].species)
print(more_animals[0].species)
