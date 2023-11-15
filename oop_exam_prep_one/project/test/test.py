import unittest



from project.pet_shop import PetShop

class PetShopTests(unittest.TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop('PetShop')

    def test_pet_shop_init(self):
        name = 'PetShop'
        pet_shop = PetShop(name)
        self.assertEqual(name, pet_shop.name)
        self.assertEqual({}, pet_shop.food)
        self.assertEqual([], pet_shop.pets)

    def test_raises_adding_negative_food(self):
        name = 'PetShop'
        pet_shop = PetShop(name)
        with self.assertRaises(ValueError) as ex:
            pet_shop.add_food('dog food',0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_if_new_food_and_quantity_added(self):
        name = 'PetShop'
        pet_shop = PetShop(name)
        self.assertEqual("Successfully added 20.00 grams of dog food.",pet_shop.add_food('dog food', 20))
        self.assertTrue('dog food' in pet_shop.food)
        self.assertEqual(20, pet_shop.food['dog food'])

    def test_add_and_raise_add_pet_same_name(self):
        self.assertEqual("Successfully added Tommy.", self.pet_shop.add_pet('Tommy'))
        self.assertTrue('Tommy' in self.pet_shop.pets)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet('Tommy')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_raise_when_pet_name_not_in_petstore(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet('cat food','Tommy')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet(self):
        self.pet_shop.add_pet('Tommy')
        self.assertEqual('You do not have cat food', self.pet_shop.feed_pet('cat food', 'Tommy'))
        self.pet_shop.add_food('cat food', 50)
        self.assertEqual("Adding food...", self.pet_shop.feed_pet('cat food', 'Tommy'))
        self.assertEqual(1050, self.pet_shop.food['cat food'])
        self.assertEqual("Tommy was successfully fed", self.pet_shop.feed_pet('cat food', 'Tommy'))
        self.assertEqual(950, self.pet_shop.food['cat food'])
    def test_repr_method(self):
        self.pet_shop.add_pet('Tommy')
        self.pet_shop.add_pet('Ghost')
        expected = f'Shop PetShop:\n' \
               f'Pets: Tommy, Ghost'
        self.assertEqual(expected, str(self.pet_shop))

if __name__ == '__main__':
    unittest.main()
