"""
Student Management System
Final Python Project - Internship Weeks 1 to 6

Features:
- Add, view, search, update, and delete student records
- Calculate percentage and grade
- Persistent JSON file storage
- Input validation and exception handling
- OOP: classes, constructor, inheritance, polymorphism, encapsulation, abstraction
"""

import json
from abc import ABC, abstractmethod
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "students.json"


class Person(ABC):
    """Abstract base class for people."""

    def __init__(self, name: str, age: int):
        self.name = name.strip()
        self.age = age

    @abstractmethod
    def get_details(self) -> str:
        """Return formatted details for a person."""


class Student(Person):
    """Student model; demonstrates inheritance and encapsulation."""

    def __init__(self, student_id: str, name: str, age: int, course: str,
                 marks: list[float]):
        super().__init__(name, age)
        self.student_id = student_id.strip().upper()
        self.course = course.strip()
        self._marks = []
        self.marks = marks

    @property
    def marks(self) -> list[float]:
        return self._marks.copy()

    @marks.setter
    def marks(self, values: list[float]) -> None:
        if len(values) != 3:
            raise ValueError("Enter marks for exactly 3 subjects.")
        if any(mark < 0 or mark > 100 for mark in values):
            raise ValueError("Each mark must be between 0 and 100.")
        self._marks = [float(mark) for mark in values]

    @property
    def percentage(self) -> float:
        return sum(self._marks) / len(self._marks)

    @property
    def grade(self) -> str:
        # Polymorphic behavior can be extended in other person types.
        if self.percentage >= 90:
            return "A+"
        if self.percentage >= 80:
            return "A"
        if self.percentage >= 70:
            return "B"
        if self.percentage >= 60:
            return "C"
        if self.percentage >= 50:
            return "D"
        return "F"

    def get_details(self) -> str:
        return (
            f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | "
            f"Course: {self.course} | Marks: {self._marks} | "
            f"Percentage: {self.percentage:.2f}% | Grade: {self.grade}"
        )

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self._marks,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["student_id"], data["name"], int(data["age"]),
            data["course"], data["marks"]
        )


class StudentManagementSystem:
    """Manages student records and persists them to a JSON file."""

    def __init__(self, data_file: Path = DATA_FILE):
        self.data_file = Path(data_file)
        self.students: dict[str, Student] = {}
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        self.load_students()

    def load_students(self) -> None:
        try:
            if self.data_file.exists():
                with self.data_file.open("r", encoding="utf-8") as file:
                    data = json.load(file)
                for item in data:
                    student = Student.from_dict(item)
                    self.students[student.student_id] = student
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print(f"Warning: Could not load saved records: {error}")
            print("Starting with an empty in-memory record list.")

    def save_students(self) -> None:
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        with self.data_file.open("w", encoding="utf-8") as file:
            json.dump(
                [student.to_dict() for student in self.students.values()],
                file, indent=4
            )

    def add_student(self, student: Student) -> None:
        if student.student_id in self.students:
            raise ValueError("A student with this ID already exists.")
        self.students[student.student_id] = student
        self.save_students()

    def search_student(self, student_id: str) -> Student | None:
        return self.students.get(student_id.strip().upper())

    def update_student(self, student_id: str, name: str, age: int,
                       course: str, marks: list[float]) -> bool:
        student = self.search_student(student_id)
        if student is None:
            return False
        student.name = name.strip()
        student.age = age
        student.course = course.strip()
        student.marks = marks
        self.save_students()
        return True

    def delete_student(self, student_id: str) -> bool:
        key = student_id.strip().upper()
        if key not in self.students:
            return False
        del self.students[key]
        self.save_students()
        return True

    def list_students(self) -> list[Student]:
        return sorted(self.students.values(), key=lambda item: item.student_id)


def read_nonempty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def read_age(prompt: str = "Enter age: ") -> int:
    while True:
        try:
            age = int(input(prompt))
            if 3 <= age <= 100:
                return age
            print("Age must be between 3 and 100.")
        except ValueError:
            print("Please enter a whole number for age.")


def read_marks() -> list[float]:
    marks = []
    for subject_number in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {subject_number} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a numeric mark.")
    return marks


def create_student() -> Student:
    student_id = read_nonempty("Enter student ID: ").upper()
    name = read_nonempty("Enter student name: ")
    age = read_age()
    course = read_nonempty("Enter course/department: ")
    marks = read_marks()
    return Student(student_id, name, age, course, marks)


def show_menu() -> None:
    print("\n" + "=" * 48)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 48)
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")


def main() -> None:
    system = StudentManagementSystem()
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        try:
            if choice == "1":
                student = create_student()
                system.add_student(student)
                print("Student added and saved successfully.")

            elif choice == "2":
                students = system.list_students()
                if not students:
                    print("No student records found.")
                else:
                    print("\nSTUDENT RECORDS")
                    for student in students:
                        # Calls the overridden method on each Student object.
                        print(student.get_details())

            elif choice == "3":
                student_id = read_nonempty("Enter student ID to search: ")
                student = system.search_student(student_id)
                print(student.get_details() if student else "Student not found.")

            elif choice == "4":
                student_id = read_nonempty("Enter student ID to update: ")
                if not system.search_student(student_id):
                    print("Student not found.")
                else:
                    name = read_nonempty("Enter new name: ")
                    age = read_age("Enter new age: ")
                    course = read_nonempty("Enter new course/department: ")
                    marks = read_marks()
                    system.update_student(student_id, name, age, course, marks)
                    print("Student updated successfully.")

            elif choice == "5":
                student_id = read_nonempty("Enter student ID to delete: ")
                if system.delete_student(student_id):
                    print("Student deleted successfully.")
                else:
                    print("Student not found.")

            elif choice == "6":
                print("Thank you for using Student Management System.")
                break

            else:
                print("Invalid choice. Please select a number from 1 to 6.")

        except (ValueError, OSError) as error:
            print(f"Operation failed: {error}")


if __name__ == "__main__":
    main()
