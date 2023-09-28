import unittest
from arrs import get, my_slice

class TestArraysFunctions(unittest.TestCase):

    def test_get_existing_index(self):
        array = [1, 2, 3, 4, 5]
        index = 2
        result = get(array, index)
        self.assertEqual(result, 3)

    def test_get_non_existing_index_with_default(self):
        array = [1, 2, 3, 4, 5]
        index = 10
        default_value = 'Not Found'
        result = get(array, index, default_value)
        self.assertEqual(result, default_value)

    def test_get_negative_index(self):
        array = [1, 2, 3, 4, 5]
        index = -2
        result = get(array, index)
        self.assertEqual(result, None)

    def test_my_slice_with_start_and_end(self):
        array = [1, 2, 3, 4, 5]
        start = 1
        end = 4
        result = my_slice(array, start, end)
        self.assertEqual(result, [2, 3, 4])

    def test_my_slice_with_negative_start_and_end(self):
        array = [1, 2, 3, 4, 5]
        start = -3
        end = -1
        result = my_slice(array, start, end)
        self.assertEqual(result, [3, 4])

    def test_my_slice_without_start_and_end(self):
        array = [1, 2, 3, 4, 5]
        result = my_slice(array)
        self.assertEqual(result, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
