```python
from src.database.student_data import student_data
from src.utils import StudentSchema

class Student:
    def __init__(self):
        self.student_data = student_data
        self.schema = StudentSchema()

    def get_student_data(self, student_id):
        student = [student for student in self.student_data if student['id'] == student_id]
        if student:
            return self.schema.dump(student[0])
        else:
            return 'Student not found', 404

    def update_student_data(self, student_id, data):
        student = [student for student in self.student_data if student['id'] == student_id]
        if student:
            index = self.student_data.index(student[0])
            self.student_data[index] = self.schema.load(data)
            return self.schema.dump(self.student_data[index])
        else:
            return 'Student not found', 404

    def delete_student_data(self, student_id):
        student = [student for student in self.student_data if student['id'] == student_id]
        if student:
            self.student_data.remove(student[0])
            return 'Student removed', 200
        else:
            return 'Student not found', 404
```