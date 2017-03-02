"""You are a zoo keeper. Write a set of objects that simulates a simple zoo."""
import itertools

ANIMAL_STATUS = {
    'AL': 'Alive',
    'DE': 'Dead',
}

ANIMAL_TYPES = {
    'CA': 'Carnivore',
    'OM': 'Omnivore',
    'HE': 'Herbivore',
}

MEAT_QUALITY = {
    'TE': 'Tender',
    'TO': 'Tough',
}

class Zoo(object):
    """Creates a Zoo object with a name and an empty list for cages."""

    newid = itertools.count()

    def __init__(self, name):
        """Zoo is created with a name."""
        self.id = next(Zoo.newid)
        self.name = name
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

    def create_cage(self, cage_name):
        """Create a cage object in a zoo from a cage name."""
        cage = Cage(cage_name)
        self.cages.append(cage)
        return cage

    def remove_cage(self, cage_name):
        """The Zoo should keep track of how many cages are in existence."""
        cage = self.get_cage(cage_name)
        self.zoo_cages -= 1
        cage.__del__()

    def get_cage(self, cage_name):
        """Return cage object from a given cage name."""
        for my_cage in self.cages:
            if my_cage.name == cage_name:
                return my_cage

    def get_animal(self, animal):
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
            self.dinner_time(animal_name, animal.name)

        for animal in move_to.cage_contents:
            self.dinner_time(animal.name, animal_name)

        cage_to.cage_relationships()

        print("{} has been moved from {} to {}".format(
            moved_animal.name, cage_from, cage_to))


class Cage(object):
    """Creates a ZooCage object with a cage_name.

       Possibility to extend a BaseCage class that would have a 'prefferred' contents. e.g a gazelle cage that
       prevented gazelles being eaten in their preferred cage as they have hiding places or whatever.
       """

    newid = itertools.count()

    def __init__(self, cage_name, zoo=None):
        """Cage is created with a name and an empty list for contents."""
        self.id = next(Cage.newid)
        self.name = cage_name
        self.cage_contents = []
        if zoo:
            self.zoo = zoo

    def __str__(self):
        """Human readable string returned when the class object is printed."""
        return self.name

    def __repr__(self):
        """Class representation, returned when class object is called."""
        return '<%s: %s (%s)>' % (self.__class__.__name__, self.name, self.cage_contents)

    def add_animal(self, animal):
        animal.get_competition_score()
        animal.cage = self
        self.cage_contents.append(animal)
        self.predators_eat_prey()

    def predators_eat_prey(self):
        response = '{} ate {}'.format(one_animal, another_animal)
        return(response)

class BaseAnimal(object):
    """Base Class for animals in the zoo.

    Designed to be subclassed with an unimplemented method to actually create
    the animal.
    """

    STATUS_ALIVE = 'AL'
    STATUS_DEAD = 'DE'

    TYPE_HERBIVORE = 'HE'
    TYPE_OMNIVORE = 'OM'
    TYPE_CARNIVORE = 'CA'

    QUALITY_TOUGH = 'TO'
    QUALITY_TENDER = 'TE'

    def __init__(self, name, cage=None):
        """Zoo animals have names, species, cages and are created 'Alive'."""
        self.name = name
        self.status = self.STATUS_ALIVE
        self.species = None
        self.animal_type = None
        self.sit_rep = None
        self.competition_score = None
        self.meat_quality = None
        if cage:
            self.cage = cage

    def __str__(self):
        """Human readable string returned when the class object is printed."""
        return self.name

    def __repr__(self):
        """Class representation, returned when class object is called."""
        return '<%s: %s (%s)>' % (self.__class__.__name__, self, self.species)

    def get_status(self):
        """Return a human readable status code"""
        return ANIMAL_STATUS[self.status]

    def get_type(self):
        """Return a human readable animal type"""
        return ANIMAL_TYPE[self.animal_type]

    def get_quality(self):
        """Return a human readable animal type"""
        return MEAT_QUALITY[self.meat_quality]

    def get_competition_score(self):
        """Identify the correct relationships for a given animal.

        Relationships are calculated based on the TYPE of animal and the quality
        of it's meat.

        For example:
            LIONS are carnivores and eat only TENDER meat.

        Current scores:
            LION = 1
            HYENA = 2
            WILDEBEEST = 3
            GAZELLE = 6

        Lower scores indicate that animals are more likely to eat and less likely to be eaten.
        """
        type_score = next(i for i, v in enumerate(ANIMAL_TYPES) if v == self.animal_type)
        quality_score = next(i for i, v in enumerate(ANIMAL_TYPES) if v == self.animal_type)

        self.competition_score = (type_score + 1) * (quality_score + 1)  # Should be positive in all cases

    def get_weight_adjusted_competition_score(self):
        """Potential to add weight as a multiplier function.

           E.g. weight the competition score of
           each animal by predator_weight/ prey_weight so that heavier prey have their score weighted
           down and are therefore less likely to be eaten. But still occupy the same location in the food
           chain when compared to larger predators.

           For example:
                ELEPHANT_WEIGHT = 1000 Kg
                LION_WEIGHT = 20 Kg
                WEIGHT_MULTIPLIER = 20/1000 * CONSTANT 10
                ADJUSTED_COMPETITION_SCORE = 20 percent of elephants original competitiveness
                """
        raise NotImplementedError

    def get_prey_relationships(self):
        """Undefined method designed to be overridden.

        Potentially - Identify where an animal sits in a food web based on
        it's species/size/weight... Generate a score to represent it's
        location.
        """
        raise NotImplementedError


class Lion(BaseAnimal):
    """Create a Lion."""

    def __init__(self, name):
        super().__init__(name)
        self.species = self.__class__.__name__
        self.animal_type = BaseAnimal.TYPE_CARNIVORE
        self.meat_quality = BaseAnimal.QUALITY_TOUGH


class Hyena(BaseAnimal):
    """Create a Hyena."""

    def __init__(self, name):
        super().__init__(name)
        self.species = self.__class__.__name__
        self.animal_type = BaseAnimal.TYPE_CARNIVORE
        self.meat_quality = BaseAnimal.QUALITY_TENDER


class Wildebeest(BaseAnimal):
    """Create a Wildebeest."""

    def __init__(self, name):
        super().__init__(name)
        self.species = self.__class__.__name__
        self.animal_type = BaseAnimal.TYPE_OMNIVORE
        self.meat_quality = BaseAnimal.QUALITY_TOUGH


class Gazelle(BaseAnimal):
    """Create a Gazelle."""

    def __init__(self, name):
        super().__init__(name)
        self.species = self.__class__.__name__
        self.animal_type = BaseAnimal.TYPE_HERBIVORE
        self.meat_quality = BaseAnimal.QUALITY_TENDER
