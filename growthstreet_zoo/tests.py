from zoo import Zoo, Cage, BaseAnimal, Hyena, Gazelle, Wildebeest, Lion
from unittest import TestCase
from unittest.mock import patch


class ZooStory(TestCase):
    """Single systems test to test against the requirements in the README.rst file."""

    def test_requirements(self):
        zoo = Zoo()
        cage1 = Cage()
        cage2 = Cage()

        zoo.add_cage(cage1)
        zoo.add_cage(cage2)

        self.assertEqual(zoo.number_of_cages(), 2)  # At any time, you should be able to find out how many cages are in the zoo.

        lion = Lion()
        hyena = Hyena()
        gazelle = Gazelle()
        wildebeest = Wildebeest()

        cage1.add_animal(lion)
        cage2.add_animal(gazelle)

        self.assertEqual(cage1.contents, [lion])  # Put different animals in the cages
        self.assertTrue(lion.species)  # Each animal should be of a particular species
        self.assertTrue(lion.name)  # Each animal should have a name given to them by the zookeeper

        cage1.add_animal(hyena)
        cage2.add_animal(wildebeest)

        self.assertEqual(cage1.contents, [lion, hyena])  # Find out which animals are in a particular cage
        self.assertEqual(cage2.contents, [gazelle, wildebeest])  # Find out which animals are in a particular cage

        with patch("builtins.print") as mock_print:
            prey_cage = Cage()

            predator = Lion(name='Predator')
            prey = Gazelle(name='Prey')

            prey_cage.add_animal(prey)
            prey_cage.add_animal(predator)

            mock_print.assert_called_once_with("Predator ate Prey")


class ZooUnitTests(TestCase):

    def setUp(self):
        self.zoo = Zoo('The Zoo')
        self.cage = Cage('The Cage')
        self.animal = BaseAnimal('Test')

    def test_zoo_str(self):
        self.assertEqual(str(self.zoo), 'The Zoo')


class CageUnitTests(TestCase):

    def setUp(self):
        self.cage = Cage('The Cage')

    def test_cage(self):
        self.assertEqual(str(self.cage), 'The Cage')


class AnimalUnitTests(TestCase):

    def setUp(self):
        self.cage = Cage('The Cage')
        self.animal = BaseAnimal('Test')

    def test_animal(self):
        self.assertEqual(str(self.animal), 'Test')

if __name__ == '__main__':
    unittest.main()
