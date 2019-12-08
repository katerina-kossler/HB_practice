"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student-search")
def get_student_form():
    """Searches for student via github username"""

    return render_template("student_search.html")


@app.route("/student", methods=['GET'])
def get_student():
    """Show information about a student."""

    github = request.args.get('github')
    first, last, github = hackbright.get_student_by_github(github)
    graded_projects = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           projects=graded_projects)

    return html


@app.route("/new-student")
def collect_student_info():
    """Collects information about a new student"""

    return render_template('new_student.html')


@app.route("/student-added", methods=['POST'])
def student_add():
    """Adds a new student to the database"""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')
    hackbright.make_new_student(first_name, last_name, github)

    return render_template("student_added.html",
                           github=github)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
