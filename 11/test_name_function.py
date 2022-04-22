import unittest

from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('stephen', 'curry')
        self.assertEqual(formatted_name, 'Stephen Curry')


if __name__ == '__main__':
    unittest.main()
