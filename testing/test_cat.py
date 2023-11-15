class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main

class CatTests(TestCase):

    def test_cat_size_increase_after_eating(self):
        cat = Cat("Ghost")
        self.assertEqual(0, cat.size)
        cat.eat()
        self.assertEqual(1, cat.size)

    def test_if_cat_is_fed_after_eating(self):
        cat = Cat("Ghost")
        self.assertEqual(False, cat.fed)
        cat.eat()
        self.assertEqual(True, cat.fed)

    def test_raising_error_if_cat_already_fed(self):
        cat = Cat("Ghost")
        self.assertEqual(False, cat.fed)
        cat.eat()
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_raising_error_if_hungry_cat_tries_sleeping(self):
        cat = Cat("Ghost")
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_if_cat_is_not_sleepy_after_sleeping(self):
        cat = Cat("Ghost")
        cat.eat()
        cat.sleep()
        self.assertEqual(False, cat.sleepy)

if __name__ == '__main__':
    main()