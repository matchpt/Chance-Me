```python
import tkinter as tk
from src.student import get_student_data, update_student_data, delete_student_data
from src.recommendation import get_recommendation_data

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("College Admission Guide")
        self.create_student_form()
        self.create_recommendation_form()

    def create_student_form(self):
        student_form = tk.Frame(self.root)
        student_form.pack()

        self.student_id_entry = tk.Entry(student_form)
        self.student_id_entry.pack()

        get_button = tk.Button(student_form, text="Get Student Data", command=self.get_student)
        get_button.pack()

        update_button = tk.Button(student_form, text="Update Student Data", command=self.update_student)
        update_button.pack()

        delete_button = tk.Button(student_form, text="Delete Student Data", command=self.delete_student)
        delete_button.pack()

    def create_recommendation_form(self):
        recommendation_form = tk.Frame(self.root)
        recommendation_form.pack()

        get_button = tk.Button(recommendation_form, text="Get Recommendations", command=self.get_recommendations)
        get_button.pack()

    def get_student(self):
        student_id = self.student_id_entry.get()
        student_data = get_student_data(student_id)
        print(studentMessage.format(student_data))

    def update_student(self):
        student_id = self.student_id_entry.get()
        update_student_data(student_id)
        print(studentMessage.format("Data updated."))

    def delete_student(self):
        student_id = self.student_id_entry.get()
        delete_student_data(student_id)
        print(studentMessage.format("Data deleted."))

    def get_recommendations(self):
        student_id = self.student_id_entry.get()
        recommendation_data = get_recommendation_data(student_id)
        print(recommendationMessage.format(recommendation_data))


if __name__ == "__main__":
    root = tk.Tk()
    UserInterface(root)
    root.mainloop()
```