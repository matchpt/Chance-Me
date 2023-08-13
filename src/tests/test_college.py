import unittest
from src.college import College
from src.database.college_data import college_data

class TestCollege(unittest.TestCase):

    def setUp(self):
        self.college = College(college_data)

    def test_get_college_data(self):
        data = self.college.get_college_data()
        self.assertEqual(data, college_data)

    def test_update_college_data(self):
        new_data = {'name': 'Test University', 'location': 'Test City'}
        self.college.update_college_data(new_data)
        self.assertEqual(self.college.data, new_data)

    def test_delete_college_data(self):
        self.college.delete_college_data()
        self.assertEqual(self.college.data, {})

if __name__ == '__main__':
    unittest.main()