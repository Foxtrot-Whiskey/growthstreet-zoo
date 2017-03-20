"""You are a zoo keeper. Write a set of objects that simulates a simple zoo."""
import itertools
from name_generator import GenerateNameMixin


class Zoo(GenerateNameMixin):
    """Creates a Zoo object with a name and an empty list for cages."""

    def __init__(self, name=None):
        """Zoo is created with a name."""
        super().__init__(name)
        self.cages = []

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


class Cage(GenerateNameMixin):
    """Creates a ZooCage object with a cage_name.

       Possibility to extend a BaseCage class that would have a 'prefferred' contents. e.g a gazelle cage that
       prevented gazelles being eaten in their preferred cage as they have hiding places or whatever.
       """

    newid = itertools.count()

    def __init__(self, name=None, zoo=None):
        """Cage is created with a name and an empty list for contents."""
        super().__init__(name)
        self.id = next(Cage.newid)
        self.contents = []
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
        self.eat_all_prey(animal)

    def eat_all_prey(self, new_animal):
        """When a  new animal enters a cage, check whether any animals in the cage should be eaten and eat them."""
        live_animals = [animal for animal in self.contents if animal.status == animal.STATUS_ALIVE]
        for animal in live_animals:
            new_animal.is_eaten_by(animal)


class BaseAnimal(GenerateNameMixin):
    """Base Class for animals in the zoo.

    Designed to be subclassed with an unimplemented method to actually create
    the animal.
    """

    STATUS_ALIVE = 'AL'
    STATUS_DEAD = 'DE'

    COMPETITION_MAP = {}

    def __init__(self, name=None, cage=None):
        """Zoo animals have names, species, cages and are created 'Alive'."""
        super().__init__(name)
        self.status = self.STATUS_ALIVE
        if cage:
            self.cage = cage

    def __str__(self):
        """Human readable string returned when the class object is printed."""
        return self.name

    def __repr__(self):
        """Class representation, returned when class object is called."""
        return '<%s: %s (%s)>' % (self.__class__.__name__, self, self.species)

    def is_eaten_by(self, animal):
        """Print a string indicating what an instance of an animal is eaten by."""
        self.prey = self.COMPETITION_MAP[self.species]
        if animal.species in self.prey:
            animal.status = animal.STATUS_DEAD
            print("{} ate {}.".format(self.name, animal.name))


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
