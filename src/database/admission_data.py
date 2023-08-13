import pandas as pd
from src.utils import load_data

class AdmissionData:
    def __init__(self):
        self.admission_data = load_data('admission_data.csv')

    def get_admission_data(self):
        return self.admission_data

    def update_admission_data(self, updated_data):
        self.admission_data = updated_data
        self.admission_data.to_csv('admission_data.csv', index=False)

    def delete_admission_data(self, student_id):
        self.admission_data = self.admission_data[self.admission_data.student_id != student_id]
        self.admission_data.to_csv('admission_data.csv', index=False)