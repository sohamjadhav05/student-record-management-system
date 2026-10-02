# Student Record Management System Using Cloud Database

A web-based Student Record Management System developed as an individual Cloud Computing mini project.

The application allows users to add, view, search, edit, and delete student records. The student data is stored in a cloud-hosted MongoDB Atlas database and accessed through a Python Flask web application.

---

## ☁️ Cloud Computing Area

**Cloud Database**

The project uses **MongoDB Atlas** as the cloud database service.

Student records are stored remotely in MongoDB Atlas instead of being stored only on the local computer.

---

## 🎯 Objective

The objective of this project is to develop a simple cloud-based student record management system that demonstrates how a web application can connect to and manage data stored in a cloud database.

---

## ✨ Features

- Add new student records
- View all student records
- Search students by name or roll number
- Edit existing student records
- Delete student records
- Cloud-based data storage
- Simple and responsive web interface

---

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Database
- MongoDB Atlas
- PyMongo

### Development Tools
- Visual Studio Code
- Git
- GitHub

---

## 🏗️ System Architecture

```text
                Student
                   │
                   ▼
          ┌─────────────────┐
          │  Web Interface  │
          │   HTML / CSS    │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │  Flask Backend  │
          │     Python      │
          └────────┬────────┘
                   │
                PyMongo
                   │
                   ▼
          ┌─────────────────┐
          │  MongoDB Atlas  │
          │  Cloud Database │
          └─────────────────┘

---

## 🔄 Working of the System

1. The user opens the Student Record Management System.
2. The Flask application provides the web interface.
3. The user can add, view, search, edit, or delete student records.
4. Flask communicates with MongoDB Atlas using PyMongo.
5. MongoDB Atlas stores the student information in the cloud.
6. Updated information is retrieved from the cloud database and displayed on the web application.

---

## 📋 Student Information

Each student record contains:

- Student Name
- Roll Number
- Course
- Year
- Email

---

## 🔧 CRUD Operations

The system implements all major CRUD operations:

| Operation | Function |
|-----------|----------|
| Create | Add Student |
| Read | View Students |
| Update | Edit Student |
| Delete | Delete Student |

The system also provides a search feature for finding students by name or roll number.

---

## 📁 Project Structure

```text
student-record-management-system/
│
├── templates/
│   ├── index.html
│   ├── add_student.html
│   ├── students.html
│   ├── search.html
│   └── edit_student.html
│
├── static/
│   └── style.css
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
└── README.md