"""You are a zoo keeper. Write a set of objects that simulates a simple zoo."""
import itertools
from name_generator import GenerateNameMixin


class Zoo(GenerateNameMixin):
    """Creates a Zoo object with a name and an empty list for cages."""

    def __init__(self, name=None):
        """Zoo is created with a name."""
        super().__init__(name)
        self.cages = []

    def __repr__(self):
        """Class representation, returned when class object is called."""
        animals = [[animal for animal in cage.cage_contents if animal.is_alive] for cage in self.cages]
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

    def __repr__(self):
        """Class representation, returned when class object is called."""
        return '<%s: %s (%s)>' % (self.__class__.__name__, self.name, self.contents)

    def add_animal(self, animal):
        """Add an instance of an animal to a Cage."""
        self.contents.append(animal)
        self.eat_all_prey(animal)

    def eat_all_prey(self, new_animal):
        """When a  new animal enters a cage, check whether any animals in the cage should be eaten and eat them."""
        live_animals = [animal for animal in self.contents if animal.is_alive]
        for animal in live_animals:
            animal.eaten_by_animal(new_animal)
            new_animal.eaten_by_animal(animal)


class BaseAnimal(GenerateNameMixin):
    """Base Class for animals in the zoo.

    Designed to be subclassed with an unimplemented method to actually create
    the animal.
    """

    COMPETITION_MAP = {}

    def __init__(self, name=None, cage=None):
        """Zoo animals have names, species, cages and are created 'Alive'."""
        super().__init__(name)
        self.is_alive = True

    def __repr__(self):
        """Class representation, returned when class object is called."""
        return '<%s: %s>' % (self.__class__.__name__, self)

    def get_prey(self):
        """Recursively get prey from a hash table."""
        self.prey = []
        animal = self.species
        while animal:
            try:
                prey = self.COMPETITION_MAP[animal]
                self.prey.append(prey)
                animal = prey
            except KeyError:
                break

    def eaten_by_animal(self, animal):
        """Print a string indicating what an instance of an animal is eaten by."""
        self.get_prey()
        if animal.species in self.prey:
            animal.is_alive = False
            print("{} ate {}.".format(self.name, animal.name))


class Lion(BaseAnimal):
    """A BaseAnimal instance with properties of a Lion."""

    def __init__(self, name=None):
        """Instantiate object with all properties of the BaseAnimal class and the correct species."""
        super().__init__(name)
        self.species = self.__class__.__name__
        self.COMPETITION_MAP.update({'Lion': 'Hyena',
                                     'Hyena': 'Wildebeest',
                                     'Wildebeest': 'Gazelle'})


class Hyena(BaseAnimal):
    """A BaseAnimal instance with properties of a Hyena."""

    def __init__(self, name=None):
        """Instantiate object with all properties of the BaseAnimal class and the correct species."""
        super().__init__(name)
        self.species = self.__class__.__name__
        self.COMPETITION_MAP.update({'Hyena': 'Wildebeest',
                                     'Wildebeest': 'Gazelle'})


class Wildebeest(BaseAnimal):
    """A BaseAnimal instance with properties of a Wildebeest."""

    def __init__(self, name=None):
        super().__init__(name)
        self.species = self.__class__.__name__
        self.COMPETITION_MAP.update({'Wildebeest': 'Gazelle'})


class Gazelle(BaseAnimal):
    """A BaseAnimal instance with properties of a Wildebeest."""

    def __init__(self, name=None):
        """Instantiate object with all properties of the BaseAnimal class and the correct species."""
        super().__init__(name)
        self.species = self.__class__.__name__
        self.COMPETITION_MAP.update({'Gazelle': ''})
