OOP Practice
============

Tom's Zoo
----------

Hi Both,

This is my second submission for review - have a look. The easiest way to see what it can do is probably run the zoo_test.py file. It makes a simple zoo and populates it with two cages and some animals. First it tries to get the monkey Harambe to eat the monkey George. Monkeys don't eat monkeys so this fails with the message "I can't eat a Bonobo". Then it prompts the Lion Growlr to eat the monkey George. Animals cannot eat animals in other cages. So this also fails with the message "George is in another cage :(". Then the Lion "Growlr" is moved from the Lion Cage to the Monkey Cage and the action is repeated. This results in Georges status changing from "Alive" to "Dead" and his sit_rep showing who ate him.

Zoo Game
--------

1.  You are a zoo keeper. Write a set of objects in a language of your choice that simulates a simple zoo.
    You should be able to do the following using the language's command line console:​
    Create different cages in the zoo.  At any time, you should be able to find out how many cages are in the zoo.
    Put different animals in the cages. Each animal should be of a particular species (e.g. 'Lion'), and have a name given to them by the zookeeper (e.g. 'Growler').
    Find out which animals are in a particular cage.
    Some species of animals like eating other species of animals.  For example, lions like eating wildebeest.  If you put prey and predator in the same cage, then all the prey should be eaten by the predator.  (The program should tell you which predator ate which prey.)


Bonus task
----------
2.  Each cage needs a reference number so the zoo keeper doesn't get confused.  Automatically generate a reference number when building each cage.  The first cage should be 1, the second 2, etc.


David's Ideas:
---------------

  - DONE - add .pyc files to .gitignore 
  - DONE - Make class names shorter. See smurf case
  - DONE - remove "kind" from classes
  - DONE - add __str__ and __repr__ method to all classes
  - DONE  - Make 'super' BaseAnimal class. Extend other animals from it.
  - If you put prey and predator in the same cage, then all the prey should be eaten by the predator.
  - documentation file. i.e. how to find the number of cages in the zoo.


  

george = Prey("George", "Bonobo")
monkeys.add_animal(george)


  monkeys_cage.add_prey("George", "Bonobo")
  monkeys_cage.add_predator("Harambe", "Gorilla")
  lions_cage.add_apex_predator("Growlr", "Lion")

  z.dinner_time(harambe, george)
  z.dinner_time("Growlr", "George")
  z.move_animal(lion_cage, monkey_cage, growlr)
  z.dinner_time("Growlr", "George")
