from extended_list import IntegerList
from unittest import TestCase, main



class IntegerListTests(TestCase):

    def test_if_add_adds_and_returns_new_list(self):
        int_list = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], int_list.get_data())
        int_list.add(4)
        self.assertEqual([1, 2, 3, 4], int_list.get_data())

    def test_if_valerr_raised_if_add_element_not_integer(self):
        int_list = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], int_list.get_data())
        with self.assertRaises(ValueError) as ex:
            int_list.add('Hi')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_if_ind_is_removed(self):
        int_list = IntegerList(1, 2, 3)
        int_list.remove_index(1)
        self.assertEqual([1, 3], int_list.get_data())
        self.assertEqual(3, int_list.remove_index(1))

    def test_if_index_error_when_index_out_of_range(self):
        int_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            int_list.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_init_takes_only_ints(self):
        int_list = IntegerList(1, 2, 3, 'a', 'ss', 4, [5, 6], 3.23)
        self.assertEqual([1,2,3,4], int_list.get_data())

    def test_if_get_returns_right_element(self):
        int_list = IntegerList(1, 2, 3)
        self.assertEqual(2, int_list.get(1))

    def test_if_index_error_raised_for_get_fun(self):
        int_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            int_list.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_inserting_at_index(self):
        int_list = IntegerList(1, 2, 4)
        int_list.insert(2,3)
        self.assertEqual([1,2,3,4], int_list.get_data())

    def test_error_raised_insert_index_oor(self):
        int_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            int_list.insert(4, 4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_error_raised_insert_wrong_type(self):
        int_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as ex:
            int_list.insert(2, "Hi")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_get_biggest_value(self):
        int_list = IntegerList(1, 2, 3)
        self.assertEqual(3, int_list.get_biggest())

    def test_get_index_function(self):
        int_list = IntegerList(1, 2, 3)
        self.assertEqual(2, int_list.get_index(3))


if __name__ == "__main__":
    main()



