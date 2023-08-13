import json
from src.utils import load_data

# Define the schema for college data
CollegeSchema = {
    "id": str,
    "name": str,
    "location": str,
    "acceptance_rate": float,
    "average_SAT_score": int,
    "average_ACT_score": int,
    "tuition": int,
    "majors": list
}

# Load the college data from a JSON file
college_data = load_data("college_data.json")

def get_college_data():
    """
    Function to fetch college data
    """
    return college_data

def update_college_data(new_data):
    """
    Function to update college data
    """
    global college_data
    college_data = new_data
    with open("college_data.json", "w") as json_file:
        json.dump(college_data, json_file)

def delete_college_data(id):
    """
    Function to delete college data
    """
    global college_data
    college_data = [college for college in college_data if college["id"] != id]
    with open("college_data.json", "w") as json_file:
        json.dump(college_data, json_file)