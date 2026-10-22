# Final_project
final project about python programming
# Student Management System

## Project Description
A menu-driven Python application for storing and managing student records. It supports adding, viewing, searching, updating, and deleting students. Each record includes three subject marks, percentage, and grade. Records are saved in a JSON file.

## Features
- Add, list, search, update, and delete student records
- Input validation for age and marks
- Percentage and grade calculation
- Persistent storage using JSON
- Exception handling for invalid inputs and file data
- Object-oriented design

## Technologies Used
- Python 3.10 or newer (uses modern type hints)
- Visual Studio Code
- Git and GitHub
- JSON and Python standard library

## Python Concepts Used
Variables and data types, input/output, operators, type casting, conditions, loops, functions, lists, dictionaries, file handling, JSON, exception handling, classes, objects, constructors, inheritance, polymorphism through method overriding, encapsulation through a property-managed marks field, and abstraction using an abstract base class.

## Folder Structure
```text
Student_Management_System_Project/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── main.py
├── data/
│   └── students.json
├── screenshots/
└── docs/
    └── Final_Project_Report.docx
```

## Installation / Setup
1. Install Python 3.10 or newer.
2. Download or clone this project.
3. Open the project folder in Visual Studio Code.
4. No third-party packages are required.

## How to Run
From the project root, run:

```bash
python src/main.py
```

On some Windows systems, use:

```powershell
py src/main.py
```

Choose an option from the menu. Student records are stored in `data/students.json`.

## Example
```text
================================================
       STUDENT MANAGEMENT SYSTEM
================================================
1. Add student
2. View all students
3. Search student
4. Update student
5. Delete student
6. Exit
Choose an option (1-6): 1
Enter student ID: S101
Enter student name: Asha
Enter age: 20
Enter course/department: CSE
Enter marks for subject 1 (0-100): 90
Enter marks for subject 2 (0-100): 85
Enter marks for subject 3 (0-100): 95
Student added and saved successfully.
```

## Future Improvements
- Add a graphical user interface
- Export reports to CSV or PDF
- Add login and role-based permissions
- Add unit tests and automated GitHub Actions
- Support more subjects and attendance tracking

## GitHub Repository
https://github.com/narendra462/python

Before submission, confirm that the repository link is correct and upload the project files to your repository.

