import unittest
from src.student import Student, get_student_data, update_student_data, delete_student_data
from src.database.student_data import student_data

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student('John Doe', 'johndoe@gmail.com', 'Computer Science', 'MIT')

    def test_get_student_data(self):
        data = get_student_data()
        self.assertEqual(data, student_data)

    def test_update_student_data(self):
        new_data = {'name': 'Jane Doe', 'email': 'janedoe@gmail.com', 'major': 'Data Science', 'preferred_college': 'Stanford'}
        update_student_data(new_data)
        self.assertEqual(student_data['name'], 'Jane Doe')
        self.assertEqual(student_data['email'], 'janedoe@gmail.com')
        self.assertEqual(student_data['major'], 'Data Science')
        self.assertEqual(student_data['preferred_college'], 'Stanford')

    def test_delete_student_data(self):
        delete_student_data()
        self.assertEqual(student_data, {})

if __name__ == '__main__':
    unittest.main()