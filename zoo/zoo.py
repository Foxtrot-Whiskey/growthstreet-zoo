"""You are a zoo keeper. Write a set of objects that simulates a simple zoo."""

ANIMAL_STATUS = (
    ('AL', 'Alive'),
    ('DE', 'Dead'),
)

ANIMAL_TYPES = (
    ('CA', 'Carnivore'),
    ('OM', 'Omnivore'),
    ('HE', 'Herbivore'),
)

MEAT_QUALITY = (
    ('TE', 'Tender'),
    ('TO', 'Tough')
)


class Zoo(object):
    """Creates a Zoo object with a name and an empty list for cages."""

    zoo_cages = 0

    def __init__(self, name):
        """Zoo is created with a name."""
        self.name = name
        self.cages = []

    def __str__(self):
        """Human readable string returned when the class object is printed."""
        return self.name

    def __repr__(self):
        """Class representation, returned when class object is called."""
        animals = [[animal for animal in cage.cage_contents if animal.status == 'Alive'] for cage in self.cages]
        return '<%s: %s Cages (%s Animals)>' % (self.name, len(self.cages), len(animals))

    def add_cage(self, cage_name):
        """Cage objects are added to a Zoo's cages list."""
        self.cages.append(Cage(cage_name))
        self.zoo_cages += 1

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

    instances = 0

    def __init__(self, cage_name, zoo=None):
        """Cage is created with a name and an empty list for contents."""
        self.id = self.instances
        self.name = cage_name
        self.cage_contents = []
        if zoo:
            self.zoo = zoo
        Cage.instances_created += 1

    def __del__(self):
        """Cage can be deleted while keeping track of the total."""
        Cage.instances_created -= 1

    def __str__(self):
        """Human readable string returned when the class object is printed."""
        return '<%s: %s Animals>' % (self, len(self.cage_contents))

    def __repr__(self):
        """Class representation, returned when class object is called."""
        return '<%s: %s (%s)>' % (self.__class__.__name__, self.name, self.cage_contents)

    def cage_relationships(self):
        """If you put prey and predator in the same cage, then all the prey should be eaten by the predator."""
        competition_scores = [animal.get_competition_score() for animal in self.cage_contents]
        predators = [animal for animal in self.cage_contents if animal.competition_score == min(competition_scores)]
        eaten_animals = 0

        for animal in self.cage_contents:
            if animal.competition_score > min(competition_scores) * 2:
                animal.status = animal.STATUS_DEAD
                animal.sit_rep = "I was eaten by {}".format(predators)
                eaten_animals += 1

        return "{} animals eaten".format(eaten_animals)


class BaseSpecies(object):
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
        if cage:
            self.cage = cage

    def __str__(self):
        """Human readable string returned when the class object is printed."""
        return self.name

    def __repr__(self):
        """Class representation, returned when class object is called."""
        return '<%s: %s (%s)>' % (self.__class__.__name__, self, self.species)

    def get_competition_score(self):
        """Identify the correct relationships for a given animal.

        Relationships are calculated based on the TYPE of animal and the quality
        of it's meat.

        For example:
            LIONS are carnivores and eat only TENDER meat.

        Current scores:
            LION = 2
            HYENA = 2
            WILDEBEEST = 4
            GAZELLE = 6

        Lower scores indicate that animals are more likely to eat and less likely to be eaten.
        """
        type_score = next(i for i, v in enumerate(ANIMAL_TYPES) if v[0] == self.animal_type)
        quality_score = next(i for i, v in enumerate(ANIMAL_TYPES) if v[0] == self.animal_type)

        self.competition_score = type_score + 1 * quality_score + 1  # Should be positive in all cases
        return self.competition_score
    
    def get_weight_adjusted_competition_score(self):
        """Potential to add weight as a multiplier function.

           E.g. weight the competition score of
           each animal by predator_weight/ prey_weight so that heavier prey have their score weighted
           down and are there for less likely to be eaten. But still occupy the same space in the food
           chain when compared to larger predators.

           For example:
                ELEPHANT_WEIGHT = 1000 Kg
                LION_WEIGHT = 20 Kg
                WEIGHT_MULTIPLIER = 20/1000 * CONSTANT 10
                ADJUSTED_COMPETITION_SCORE = 20 percent of elephants original competitiveness
                """

    def get_prey_relationships(self):
        """Undefined method designed to be overridden.

        Potentially - Identify where an animal sits in a food web based on
        it's species/size/weight... Generate a score to represent it's
        location.
        """
        raise NotImplementedError


class Lion(BaseSpecies):
    """Create a Lion."""

    BaseSpecies.species = 'Lion'
    BaseSpecies.animal_type = BaseSpecies.TYPE_CARNIVORE
    BaseSpecies.meat_quality = BaseSpecies.QUALITY_TOUGH


class Hyena(BaseSpecies):
    """Create a Hyena."""

    BaseSpecies.species = 'Hyena'
    BaseSpecies.animal_type = BaseSpecies.TYPE_CARNIVORE
    BaseSpecies.meat_quality = BaseSpecies.QUALITY_TOUGH


class Wildebeest(BaseSpecies):
    """Create a Wildebeest."""

    BaseSpecies.species = 'Wildebeest'
    BaseSpecies.animal_type = BaseSpecies.TYPE_OMNIVORE
    BaseSpecies.meat_quality = BaseSpecies.QUALITY_TOUGH


class Gazelle(BaseSpecies):
    """Create a Gazelle."""

    BaseSpecies.species = 'Gazelle'
    BaseSpecies.animal_type = BaseSpecies.TYPE_HERBIVORE
    BaseSpecies.meat_quality = BaseSpecies.QUALITY_TENDER
