from python_zoo import Zoo, ZooCage, ZooAnimal

"""Set up of la simple zoo with two cages for testing."""
z = Zoo("Tom's Test Zoo")
z.add_cage("The Lion Den")
z.add_cage("The Monkey Cage")

lions = z.cages[0]
monkeys = z.cages[1]

monkeys.add_animal("George", "Bonobo")
monkeys.add_animal("Harambe", "Gorilla")
lions.add_animal("Growlr", "Lion")

z.dinner_time("Harambe", "George")
z.dinner_time("Growlr", "George")
z.move_animal("The Lion Den", "The Monkey Cage", "Growlr")
z.dinner_time("Growlr", "George")
