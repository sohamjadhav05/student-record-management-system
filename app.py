from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB Atlas connection
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

# Database
db = client["student_records"]

# Students collection
students_collection = db["students"]


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- ADD STUDENT ----------------

@app.route("/add", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        student = {
            "name": request.form["name"],
            "roll_number": request.form["roll_number"],
            "course": request.form["course"],
            "year": request.form["year"],
            "email": request.form["email"]
        }

        students_collection.insert_one(student)

        return redirect(url_for("view_students"))

    return render_template("add_student.html")


# ---------------- VIEW STUDENTS ----------------

@app.route("/students")
def view_students():

    students = list(students_collection.find())

    return render_template(
        "students.html",
        students=students
    )

# ---------------- SEARCH STUDENT ----------------

@app.route("/search")
def search_student():

    query = request.args.get("query", "").strip()

    students = []

    if query:

        students = list(
            students_collection.find(
                {
                    "$or": [
                        {"name": {"$regex": query, "$options": "i"}},
                        {"roll_number": {"$regex": query, "$options": "i"}}
                    ]
                }
            )
        )

    return render_template(
        "search.html",
        students=students,
        query=query,
        searched=bool(query)
    )

# ---------------- EDIT STUDENT ----------------

@app.route("/edit/<student_id>", methods=["GET", "POST"])
def edit_student(student_id):

    student = students_collection.find_one(
        {"_id": ObjectId(student_id)}
    )

    if not student:
        return "Student not found", 404

    if request.method == "POST":

        updated_student = {
            "name": request.form["name"],
            "roll_number": request.form["roll_number"],
            "course": request.form["course"],
            "year": request.form["year"],
            "email": request.form["email"]
        }

        students_collection.update_one(
            {"_id": ObjectId(student_id)},
            {"$set": updated_student}
        )

        return redirect(url_for("view_students"))

    return render_template(
        "edit_student.html",
        student=student
    )

# ---------------- DELETE STUDENT ----------------

@app.route("/delete/<student_id>")
def delete_student(student_id):

    students_collection.delete_one(
        {"_id": ObjectId(student_id)}
    )

    return redirect(url_for("view_students"))


if __name__ == "__main__":
    app.run(debug=True)