"""You are a zoo keeper. Write a set of objects that simulates a simple zoo."""
import itertools
from name_generator import generate_name


class Zoo(object):
    """Creates a Zoo object with a name and an empty list for cages."""

    def __init__(self, name=None):
        """Zoo is created with a name."""
        self.cages = []
        if not name:
            self.name = generate_name()
        else:
            self.name = name

    def __str__(self):
        """Human readable string returned when the class object is printed."""
        return self.name

    def __repr__(self):
        """Class representation, returned when class object is called."""
        animals = [[animal for animal in cage.cage_contents if animal.status == 'AL'] for cage in self.cages]
        return '<%s: %s Cages (%s Animals)>' % (self.name, len(self.cages), len(animals))

    def number_of_cages(self):
        """Return the number of cages in the zoo."""
        return len(self.cages)

    def add_cage(self, cage):
        """Cage objects are added to a Zoo's cages list."""
        self.cages.append(cage)
        return cage


class Cage(object):
    """Creates a ZooCage object with a cage_name.

       Possibility to extend a BaseCage class that would have a 'prefferred' contents. e.g a gazelle cage that
       prevented gazelles being eaten in their preferred cage as they have hiding places or whatever.
       """

    newid = itertools.count()

    def __init__(self, cage_name=None, zoo=None):
        """Cage is created with a name and an empty list for contents."""
        self.id = next(Cage.newid)
        self.contents = []
        if not cage_name:
            self.name = generate_name()
        else:
            self.name = cage_name
        if zoo:
            self.zoo = zoo

    def __str__(self):
        """Human readable string returned when the class object is printed."""
        return self.name

    def __repr__(self):
        """Class representation, returned when class object is called."""
        return '<%s: %s (%s)>' % (self.__class__.__name__, self.name, self.contents)

    def add_animal(self, animal):
        """Add an instance of an animal to a Cage."""
        self.contents.append(animal)
        self.predators_eat_prey()

    def predators_eat_prey(self):
        """Given animals in a cage. Check to see if any of them should be eaten."""
        alive = [animal for animal in self.contents if animal.status == animal.STATUS_ALIVE]
        permutations = itertools.permutations(alive, 2)
        for animal_pair in permutations:
            animal_1 = animal_pair[0]
            animal_2 = animal_pair[1]

            if animal_1.status == animal_1.STATUS_ALIVE and animal_2.status == animal_2.STATUS_ALIVE:
                animal_1.is_eaten(animal_2)
                animal_2.is_eaten(animal_1)


class BaseAnimal(object):
    """Base Class for animals in the zoo.

    Designed to be subclassed with an unimplemented method to actually create
    the animal.
    """

    STATUS_ALIVE = 'AL'
    STATUS_DEAD = 'DE'

    COMPETITION_MAP = {}

    def __init__(self, name=None, cage=None):
        """Zoo animals have names, species, cages and are created 'Alive'."""
        self.status = self.STATUS_ALIVE
        self.species = None
        self.animal_type = None
        self.sit_rep = None
        self.competition_score = None
        self.meat_quality = None
        if not name:
            self.name = generate_name()
        else:
            self.name = name
        if cage:
            self.cage = cage

    def __str__(self):
        """Human readable string returned when the class object is printed."""
        return self.name

    def __repr__(self):
        """Class representation, returned when class object is called."""
        return '<%s: %s (%s)>' % (self.__class__.__name__, self, self.species)

    def is_eaten(self, animal):
        """Return a Boolean indicating whether an instance of an animal is eaten."""
        self.prey = self.COMPETITION_MAP[self.species]
        if animal.species in self.prey:
            animal.status = animal.STATUS_DEAD
            print("{} ate {}.".format(self.name, animal.name))
            return True
        else:
            return False


class Lion(BaseAnimal):
    """Create a Lion."""

    def __init__(self, name=None):
        super().__init__(name)
        self.species = self.__class__.__name__
        self.COMPETITION_MAP.update({'Lion': ['Hyena', 'Wildebeest', 'Gazelle']})

class Hyena(BaseAnimal):
    """Create a Hyena."""

    def __init__(self, name=None):
        super().__init__(name)
        self.species = self.__class__.__name__
        self.COMPETITION_MAP.update({'Hyena': ['Wildebeest', 'Gazelle']})


class Wildebeest(BaseAnimal):
    """Create a Wildebeest."""

    def __init__(self, name=None):
        super().__init__(name)
        self.species = self.__class__.__name__
        self.COMPETITION_MAP.update({'Wildebeest': ['Gazelle']})


class Gazelle(BaseAnimal):
    """Create a Gazelle."""

    def __init__(self, name=None):
        super().__init__(name)
        self.species = self.__class__.__name__
        self.COMPETITION_MAP.update({'Gazelle': []})
