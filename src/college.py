```python
from src.database.college_data import college_data
from src.utils import CollegeSchema

class College:
    def __init__(self):
        self.college_data = college_data
        self.schema = CollegeSchema()

    def get_college_data(self, college_id):
        college = self.college_data.get(college_id)
        if college:
            return self.schema.dump(college)
        else:
            return None

    def update_college_data(self, college_id, data):
        if college_id in self.college_data:
            self.college_data[college_id].update(data)
            return self.schema.dump(self.college_data[college_id])
        else:
            return None

    def delete_college_data(self, college_id):
        if college_id in self.college_data:
            del self.college_data[college_id]
            return {"message": "College data deleted successfully."}
        else:
            return {"message": "College not found."}

    def add_college_data(self, data):
        new_college_id = max(self.college_data.keys()) + 1
        new_college = self.schema.load(data)
        self.college_data[new_college_id] = new_college
        return self.schema.dump(new_college)
```