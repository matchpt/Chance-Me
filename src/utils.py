```python
import json
from src.database import student_data, college_data, admission_data, recommendation_data

def load_data(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f)

def get_student_data():
    return load_data(student_data)

def get_college_data():
    return load_data(college_data)

def get_admission_data():
    return load_data(admission_data)

def get_recommendation_data():
    return load_data(recommendation_data)

def update_student_data(data):
    save_data(student_data, data)

def update_college_data(data):
    save_data(college_data, data)

def update_admission_data(data):
    save_data(admission_data, data)

def update_recommendation_data(data):
    save_data(recommendation_data, data)

def delete_student_data():
    save_data(student_data, {})

def delete_college_data():
    save_data(college_data, {})

def delete_admission_data():
    save_data(admission_data, {})

def delete_recommendation_data():
    save_data(recommendation_data, {})
```