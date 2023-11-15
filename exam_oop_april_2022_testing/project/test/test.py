import unittest

from project.movie import Movie

class MovieTest(unittest.TestCase):
    def setUp(self) -> None:
        self.movie = Movie('EDHO', 2015, 10.5)

    def test_init_method(self):
        self.assertEqual('EDHO', self.movie.name)
        self.assertEqual(2015, self.movie.year)
        self.assertEqual(10.5, self.movie.rating)

    def test_raise_if_name_is_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_raise_if_year_is_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_adding_actor(self):
        self.movie.add_actor('Meryem')
        self.assertTrue('Meryem' in self.movie.actors)
        self.assertEqual("Meryem is already added in the list of actors!", self.movie.add_actor('Meryem'))

    def test_gt_method(self):
        other_movie = Movie('Peaky', 2010, 9.5)
        another_movie = Movie('GoT',2016,11.5)
        self.assertEqual('"EDHO" is better than "Peaky"', self.movie > other_movie)
        self.assertEqual('"GoT" is better than "EDHO"', self.movie > another_movie)

    def test_repr_method(self):
        self.movie.add_actor('Meryem')
        self.movie.add_actor('Lara')
        expected_result = f"Name: EDHO\n" \
               f"Year of Release: 2015\n" \
               f"Rating: 10.50\n" \
               f"Cast: Meryem, Lara"
        self.assertEqual(expected_result, str(self.movie))
