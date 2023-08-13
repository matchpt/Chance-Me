```python
# src/config.py

# Database configuration
DATABASE_CONFIG = {
    'database': 'college_admission_db',
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'port': 5432
}

# File paths for data
STUDENT_DATA_PATH = "src/database/student_data.py"
COLLEGE_DATA_PATH = "src/database/college_data.py"
ADMISSION_DATA_PATH = "src/database/admission_data.py"
RECOMMENDATION_DATA_PATH = "src/database/recommendation_data.py"

# DOM Element IDs
DOM_IDS = {
    'studentForm': '#studentForm',
    'collegeForm': '#collegeForm',
    'admissionForm': '#admissionForm',
    'recommendationForm': '#recommendationForm'
}

# Message Names
MESSAGE_NAMES = {
    'studentMessage': 'studentMessage',
    'collegeMessage': 'collegeMessage',
    'admissionMessage': 'admissionMessage',
    'recommendationMessage': 'recommendationMessage'
}

# Function Names
FUNCTION_NAMES = {
    'get_student_data': 'get_student_data',
    'get_college_data': 'get_college_data',
    'get_admission_data': 'get_admission_data',
    'get_recommendation_data': 'get_recommendation_data',
    'update_student_data': 'update_student_data',
    'update_college_data': 'update_college_data',
    'update_admission_data': 'update_admission_data',
    'update_recommendation_data': 'update_recommendation_data',
    'delete_student_data': 'delete_student_data',
    'delete_college_data': 'delete_college_data',
    'delete_admission_data': 'delete_admission_data',
    'delete_recommendation_data': 'delete_recommendation_data'
}
```