from unittest import TestCase, main

from project.mammal import Mammal


class MammalTests(TestCase):
    def test_init_method(self):
        mammal = Mammal('Tommy', 'goat', 'mee')
        self.assertEqual('Tommy', mammal.name)
        self.assertEqual('goat', mammal.type)
        self.assertEqual('mee', mammal.sound)
        self.assertEqual('animals', mammal._Mammal__kingdom)

    def test_make_sound(self):
        mammal = Mammal('Tommy', 'goat', 'mee')
        self.assertEqual("Tommy makes mee", mammal.make_sound())

    def test_get_kingdom(self):
        mammal = Mammal('Tommy', 'goat', 'mee')
        self.assertEqual('animals', mammal.get_kingdom())

    def test_info_function(self):
        mammal = Mammal('Tommy', 'goat', 'mee')
        self.assertEqual('Tommy is of type goat', mammal.info())



if __name__ == "__main__":
    main()