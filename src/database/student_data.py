import json
from typing import Dict, List

from src.utils import load_json_data

# Load student data from JSON file
student_data: List[Dict] = load_json_data("student_data.json")

def get_student_data() -> List[Dict]:
    """Function to fetch student data"""
    return student_data

def update_student_data(new_data: Dict) -> None:
    """Function to update student data"""
    student_data.append(new_data)
    with open("student_data.json", "w") as json_file:
        json.dump(student_data, json_file)

def delete_student_data(student_id: str) -> None:
    """Function to delete student data"""
    global student_data
    student_data = [student for student in student_data if student["id"] != student_id]
    with open("student_data.json", "w") as json_file:
        json.dump(student_data, json_file)