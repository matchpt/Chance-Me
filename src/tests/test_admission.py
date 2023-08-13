import unittest
from src.admission import Admission
from src.database.admission_data import admission_data
from src.student import Student
from src.database.student_data import student_data

class TestAdmission(unittest.TestCase):

    def setUp(self):
        self.admission = Admission()
        self.student = Student()

    def test_get_admission_data(self):
        self.assertEqual(self.admission.get_admission_data(), admission_data)

    def test_update_admission_data(self):
        updated_data = {'student_id': '123', 'college_id': '456', 'admission_status': 'Pending'}
        self.admission.update_admission_data(updated_data)
        self.assertEqual(admission_data[-1], updated_data)

    def test_delete_admission_data(self):
        initial_data_length = len(admission_data)
        self.admission.delete_admission_data(admission_data[0]['id'])
        self.assertEqual(len(admission_data), initial_data_length - 1)

    def test_assess_admission_likelihood(self):
        student_info = student_data[0]
        self.student.update_student_data(student_info)
        likelihood = self.admission.assess_admission_likelihood(self.student)
        self.assertTrue(isinstance(likelihood, float))

if __name__ == '__main__':
    unittest.main()