
from car_manager import Car

from unittest import TestCase, main



class CarTests(TestCase):

    def test_constructor_method(self):
        car = Car('BMW', 'X5', 15, 150)
        self.assertEqual("BMW", car.make)
        self.assertEqual("X5", car.model)
        self.assertEqual(15, car.fuel_consumption)
        self.assertEqual(150, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_make_setter(self):
        car = Car('BMW', 'X5', 15, 150)
        car.make = 'Mercedes'
        self.assertEqual('Mercedes', car.make)

    def test_make_setter_exception(self):
        car = Car('BMW', 'X5', 15, 150)
        with self.assertRaises(Exception) as ex:
            car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter(self):
        car = Car('BMW', 'X5', 15, 150)
        car.model = 'X6'
        self.assertEqual('X6', car.model)

    def test_model_setter_exception(self):
        car = Car('BMW', 'X5', 15, 150)
        with self.assertRaises(Exception) as ex:
            car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter(self):
        car = Car('BMW', 'X5', 15, 150)
        self.assertEqual(15, car.fuel_consumption)
        car.fuel_consumption = 10
        self.assertEqual(10, car.fuel_consumption)

    def test_fuel_consumption_setter_exception_zero(self):
        car = Car('BMW', 'X5', 15, 150)
        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_setter_exception_negative(self):
        car = Car('BMW', 'X5', 15, 150)
        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter(self):
        car = Car('BMW', 'X5', 15, 150)
        self.assertEqual(150, car.fuel_capacity)
        car.fuel_capacity = 100
        self.assertEqual(100, car.fuel_capacity)

    def test_fuel_capacity_setter_exception_zero(self):
        car = Car('BMW', 'X5', 15, 150)
        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_exception_negative(self):
        car = Car('BMW', 'X5', 15, 150)
        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = -2
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))
    def test_fuel_amount_setter(self):
        car = Car('BMW', 'X5', 15, 150)
        self.assertEqual(0, car.fuel_amount)
        car.fuel_amount = 10
        self.assertEqual(10, car.fuel_amount)

    def test_fuel_amount_setter_exception(self):
        car = Car('BMW', 'X5', 15, 150)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_under_capacity(self):
        car = Car('BMW', 'X5', 15, 150)
        car.refuel(50)
        self.assertEqual(50, car.fuel_amount)

    def test_refuel_over_capacity(self):
        car = Car('BMW', 'X5', 15, 150)
        car.refuel(200)
        self.assertEqual(150, car.fuel_amount)

    def test_refuel_with_zero(self):
        car = Car('BMW', 'X5', 15, 150)
        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!",str( ex.exception))

    def test_refuel_with_negative(self):
        car = Car('BMW', 'X5', 15, 150)
        with self.assertRaises(Exception) as ex:
            car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))


    def test_drive_enough_fuel(self):
        car = Car('BMW', 'X5', 15, 150)
        car.fuel_amount = 30
        car.drive(200)
        self.assertEqual(0, car.fuel_amount)
        car.fuel_amount = 50
        car.drive(300)
        self.assertEqual(5, car.fuel_amount)

    def test_drive_raise_exception_not_enough_fuel(self):
        car = Car('BMW', 'X5', 15, 150)
        car.fuel_amount = 30
        with self.assertRaises(Exception) as ex:
            car.drive(250)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

if __name__ == "__main__":
    main()

