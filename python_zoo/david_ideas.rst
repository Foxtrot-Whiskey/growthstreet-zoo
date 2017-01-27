#Ideas:

  DONE - add .pyc files to .gitignore 
  - documentation file. i.e. how to find the number of cages in the zoo.
  - If you put prey and predator in the same cage, then all the prey should be eaten by the predator.
  DONE - Make class names shorter. See smurf case
  DONE - remove "kind" from classes
  DONE - add __str__ and __repr__ method to all classes
  - Make 'super' BaseAnimal class. Extend other animals from it.
  

george = Prey("George", "Bonobo")
monkeys.add_animal(george)


  monkeys_cage.add_prey("George", "Bonobo")
  monkeys_cage.add_predator("Harambe", "Gorilla")
  lions_cage.add_apex_predator("Growlr", "Lion")

  z.dinner_time(harambe, george)
  z.dinner_time("Growlr", "George")
  z.move_animal(lion_cage, monkey_cage, growlr)
  z.dinner_time("Growlr", "George")
