from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTests(TestCase):
    # def test_class_attributes_types(self):
    #     pass

    # def test_classvar_attribute(self):
    #     jeep = Vehicle(200, 390)
    #     self.assertEqual(1.25, jeep.fuel_consumption)
    #     jeep.fuel_consumption = 2.00
    #     self.assertEqual(1.25, jeep.fuel_consumption)

    def test_init_method_attributes(self):
        jeep = Vehicle(200, 390)
        self.assertEqual(200, jeep.fuel)
        self.assertEqual(390, jeep.horse_power)
        self.assertEqual(200, jeep.capacity)
        self.assertEqual(1.25, jeep.fuel_consumption)

    def test_capacity_when_fuel_changes(self):
        jeep = Vehicle(200, 390)
        self.assertEqual(200, jeep.fuel)
        self.assertEqual(200, jeep.capacity)
        jeep.fuel = 300
        self.assertEqual(300, jeep.fuel)
        self.assertEqual(200, jeep.capacity)

    def test_raises_exception_drive_not_enough_fuel(self):
        jeep = Vehicle(200, 390)
        with self.assertRaises(Exception) as ex:
            jeep.drive(300)
        self.assertEqual('Not enough fuel', str(ex.exception))


    def test_fuel_changes_when_drive(self):
        jeep = Vehicle(200, 390)
        jeep.drive(100)
        self.assertEqual(75, jeep.fuel)

    def test_raises_exception_refuel_above_capacity(self):
        jeep = Vehicle(200, 390)
        with self.assertRaises(Exception) as ex:
            jeep.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))


    def test_refuel_adds_fuel(self):
        jeep = Vehicle(200, 390)
        self.assertEqual(200, jeep.capacity)
        jeep.drive(100)
        self.assertEqual(75, jeep.fuel)
        jeep.refuel(124)
        self.assertEqual(199, jeep.fuel)
        jeep.refuel(1)
        self.assertEqual(200, jeep.fuel)

    def test_str_function(self):
        jeep = Vehicle(200, 390)
        self.assertEqual(
            f"The vehicle has 390 horse power with 200 fuel left and 1.25 fuel consumption",
            str(jeep)
        )


if __name__ == "__main__":
    main()