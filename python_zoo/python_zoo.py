"""You are a zoo keeper. Write a set of objects that simulates a simple zoo."""

DICTIONARY_OF_PREDATION = {'MONKEY': ['LION', 'CROCODILE', 'PYTHON'],
                           'LION': ['CROCODILE'],
                           'CROCODILE': [],
                           'PYTHON': ['CROCODILE']}

class Zoo:
    """Creates a Zoo object with a name and an empty list for cages."""
    zoo_cages = 1

    def __init__(self, name):
        """Zoo is created with a name."""
        self.name = name
        self.cages = []

    def __str__(self):
        """Human readable string returned when the class object is printed."""
        return self.name

    def __repr__(self):
        """Class representation, returned when class object is called."""
        animals = [[animal for animal in cage if animal.status == 'Alive'] for cage in self.cages]
        return '<%s: %s Cages (%s Animals)>' % (self, len(self.cages), len(animals))

    def add_cage(self, cage):
        """Cage objects are added to a Zoo's cages list."""
        self.cages.append(Cage(self.zoo_cages, cage))
        self.zoo_cages += 1

    def cage(self, cage):
        """Return cage object from a given cage name."""
        for my_cage in self.cages:
            if my_cage.name == cage:
                return my_cage

    def animal(self, animal):
        """Return animal object from a given animals name."""
        for my_cage in self.cages:
            for i in my_cage.cage_contents:
                if i.name == animal:
                    return i

    def move_animal(self, cage_from, cage_to, animal_name):
        """An animal can be moved between cages, but only within a Zoo."""
        move_from = self.cage(cage_from)
        move_to = self.cage(cage_to)
        moved_animal = self.animal(animal_name)

        move_to.cage_contents.append(moved_animal)
        move_from.cage_contents.remove(moved_animal)

        moved_animal.cage = cage_to
        
        for animal in move_to.cage_contents:
            dinner_time(animal_name, animal.name)
        
        for animal in move_to.cage_contents:
            dinner_time(animal.name, animal_name)

        print("{} has been moved from {} to {}".format(
            moved_animal.name, cage_from, cage_to))

    def dinner_time(self, animal_name, food):
        """Zoo animals can be eaten by Lions."""
        eater = self.animal(animal_name)
        dinner = self.animal(food)

        print('I will eat: {}'.format(dinner.name))
        if eater.cage == dinner.cage:
            if dinner.species in DICTIONARY_OF_PREDATION[eater.species]:
                dinner.status = 'Dead'
                dinner.sit_rep = 'I was eaten by a {} called {}'.format(
                    eater.species, eater.name)
                print(dinner.sit_rep)
            else:
                print("A {} cannot eat a {}").format(eater.species, dinner.species)
        else:
            print("{} is in another cage :(".format(dinner.name))


class Cage:
    """Creates a ZooCage object with a cage_name."""

    def __init__(self, cage_id, cage_name):
        """Cage is created with a name and an empty list for contents."""
        self.id = cage_id
        self.name = cage_name
        self.cage_contents = []

    def __str__(self):
        """Human readable string returned when the class object is printed."""
        return '<%s: %s Animals>' % (self, len(self.cage_contents))

    def __repr__(self):
        """Class representation, returned when class object is called."""
        return '<%s: %s (%s)>' % (self.__class__.__name__, self, self.cage_contents)

    def add_animal(self, name, species):
        """Animal objects can be added to a ZooCage's cage_contents list."""
        self.cage_contents.append(Animal(name, species, self.name))


class Animal:
    """Creates a ZooAnimal object."""

    def __init__(self, name, species, cage):
        """Zoo animals have names, species, cages and are created 'Alive'."""
        self.name = name
        self.species = species
        self.cage = cage
        self.status = 'Alive'
        self.sit_rep = None

    def __str__(self):
        """Human readable string returned when the class object is printed."""
        return self.name

    def __repr__(self):
        """Class representation, returned when class object is called."""
        return '<%s: %s (%s)>' % (self.__class__.__name__, self, self.species)
