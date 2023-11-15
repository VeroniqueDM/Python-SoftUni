import unittest

from project.train.train import Train


class TrainTests(unittest.TestCase):
    def setUp(self) -> None:
        self.train = Train('Happy Train', 20)

    def test_init_method(self):
        self.assertEqual('Happy Train', self.train.name)
        self.assertEqual(20, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_raise_if_add_to_full_train(self):
        self.train.capacity = 2
        self.train.add('Pesho')
        self.train.add('Desho')
        with self.assertRaises(ValueError) as ex:
            self.train.add('Lala')
        self.assertEqual("Train is full", str(ex.exception))

    def test_raises_if_add_passenger_with_same_name(self):
        self.train.add('Pesho')
        with self.assertRaises(ValueError) as ex:
            self.train.add('Pesho')
        self.assertEqual("Passenger Pesho Exists", str(ex.exception))

    def test_add_passenger_when_valid(self):
        self.assertEqual("Added passenger Pesho", self.train.add('Pesho'))
        self.assertTrue('Pesho' in self.train.passengers)

    def test_raises_if_try_to_remove_passenger_that_doesnt_exist(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove('Pesho')
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_if_passenger_is_removed(self):
        self.train.add('Pesho')
        self.assertEqual("Removed Pesho", self.train.remove('Pesho'))
        self.assertFalse('Pesho' in self.train.passengers)



    #
    # def test_class_attributes(self):
    #     self.assertEqual("Train is full", self.train.TRAIN_FULL )