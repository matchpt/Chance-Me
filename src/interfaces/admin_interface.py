```python
from flask import Flask, render_template, request, redirect, url_for
from src.college import get_college_data, update_college_data, delete_college_data
from src.admission import get_admission_data, update_admission_data, delete_admission_data

app = Flask(__name__)

@app.route('/admin/colleges', methods=['GET', 'POST'])
def manage_colleges():
    if request.method == 'POST':
        college_data = request.form['collegeForm']
        update_college_data(college_data)
        return redirect(url_for('manage_colleges'))

    colleges = get_college_data()
    return render_template('colleges.html', colleges=colleges)

@app.route('/admin/colleges/delete', methods=['POST'])
def delete_college():
    college_id = request.form['collegeId']
    delete_college_data(college_id)
    return redirect(url_for('manage_colleges'))

@app.route('/admin/admissions', methods=['GET', 'POST'])
def manage_admissions():
    if request.method == 'POST':
        admission_data = request.form['admissionForm']
        update_admission_data(admission_data)
        return redirect(url_for('manage_admissions'))

    admissions = get_admission_data()
    return render_template('admissions.html', admissions=admissions)

@app.route('/admin/admissions/delete', methods=['POST'])
def delete_admission():
    admission_id = request.form['admissionId']
    delete_admission_data(admission_id)
    return redirect(url_for('manage_admissions'))

if __name__ == '__main__':
    app.run(debug=True)
```