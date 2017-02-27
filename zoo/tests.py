from .zoo import Zoo, Cage, BaseAnimal, Hyena, Gazelle, Wildebeest, Lion
import unittest





class ZooSystemTest(unittest.TestCase):

    def setUp(self):
        self.zoo = Zoo('Test Zoo')
        self.cage = self.zoo.create_cage('Test Cage')

    def test_find_out_how_many_cages(self):
        test_zoo = Zoo('The Zoo')
        self.assertTrue(test_zoo.number_of_cages() == 0)
        test_zoo.create_cage('Test Cage')
        self.assertTrue(test_zoo.number_of_cages() == 1)

    def test_find_out_which_animals_in_cage(self):
        self.assertTrue(self.zoo.contents == [])
        test_animal = Hyena()
        self.cage.add_animal(test_animal)
        self.assertTrue(self.zoo.contents == [test_animal])

    def test_predator_eats_prey(self):
        self.assertTrue(False)

    def test_predator_does_not_eat_predator(self):
        self.assertTrue(False)

    def test_prey_does_not_eat_prey(self):
        self.assertTrue(False)

    def test_predator_does_not_eat_prey_that_it_doesnt_like(self):
        self.assertTrue(False)

    def test_create_different_cages(self):
        cage = Cage('Test Cage')
        self.zoo.add_cage(cage)
        self.assertTrue(self.zoo.cages)

    def test_number_of_cages(self):
        cages = self.zoo.number_of_cages()
        self.assertEqual(cages, 1)

    def test_put_animal_in_cage(self):
        self.animal = Gazelle('Test')
        self.cage.add_animal(self.animal)
        self.assertTrue(self.animal in self.cage.cage_contents)

    def test_reference_numbers(self):
        self.assertEqual(self.cage.id, 0)
        self.assertEqual(self.zoo.number_of_cages(), 1)
        self.another_cage = self.zoo.create_cage('Another Test Cage')
        self.assertEqual(self.zoo.number_of_cages(), 2)
        self.assertEqual(self.another_cage.id, 1)

    def test_animal_has_name(self):
        name = self.animal.name
        self.assertTrue(name)

    def test_animal_has_species(self):
        species = self.animal.species
        self.assertTrue(species)

    def test_animals_in_cage(self):
        contents = self.cage.cage_contents
        self.assertTrue(contents)

    def test_predator_prey_relationships(self):
        self.predator = Hyena('Test')
        self.cage.add_animal(self.predator)
        prey_status = self.animal.status
        self.assertTrue(prey_status, 'DE')

    def test_prey_prey_relationships(self):
        one_prey = Gazelle("One Test")
        another_prey = Gazelle("Another Test")
        prey_cage = self.zoo.add_cage(Cage("Prey Cage"))
        prey_cage.add_animal(one_prey)
        prey_cage.add_animal(another_prey)
        self.assertEqual(one_prey.status, 'AL')
        self.assertEqual(another_prey.status, 'AL')


class ZooUnitTests(unittest.TestCase):

    def setUp(self):
        self.zoo = Zoo('The Zoo')
        self.cage = Cage('The Cage')
        self.animal = BaseAnimal('Test')

    def test_zoo_str(self):
        self.assertEqual(str(self.zoo), 'The Zoo')


class CageUnitTests(unittest.TestCase):

    def setUp(self):
        self.cage = Cage('The Cage')

    def test_cage(self):
        self.assertEqual(str(self.cage), 'The Cage')


class AnimalUnitTests(unittest.TestCase):

    def setUp(self):
        self.cage = Cage('The Cage')
        self.animal = BaseAnimal('Test')

    def test_animal(self):
        self.assertEqual(str(self.animal), 'Test')

if __name__ == '__main__':
    unittest.main()
