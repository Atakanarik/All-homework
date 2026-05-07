import sqlite3

# 1. INITIALIZE DATABASE
conn = sqlite3.connect("school.db")
conn.row_factory = sqlite3.Row
db = conn.cursor()

# 2. CREATE SCHEMA
db.executescript('''
    DROP TABLE IF EXISTS grades; DROP TABLE IF EXISTS enrollments;
    DROP TABLE IF EXISTS courses; DROP TABLE IF EXISTS teachers;
    DROP TABLE IF EXISTS students; DROP TABLE IF EXISTS departments;

    CREATE TABLE departments (id INTEGER PRIMARY KEY, name TEXT, building TEXT);
    CREATE TABLE teachers (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, department_id INTEGER, salary REAL);
    CREATE TABLE students (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, gpa REAL);
    CREATE TABLE courses (id INTEGER PRIMARY KEY, code TEXT, title TEXT, teacher_id INTEGER, department_id INTEGER);
    CREATE TABLE enrollments (id INTEGER PRIMARY KEY, student_id INTEGER, course_id INTEGER);
    CREATE TABLE grades (id INTEGER PRIMARY KEY, enrollment_id INTEGER, letter_grade TEXT, final_score REAL);
''')

# 3. INSERT SAMPLE DATA
db.execute("INSERT INTO departments VALUES (1, 'Computer Science', 'Science Hall'), (2, 'English', 'Humanities')")
db.execute("INSERT INTO teachers VALUES (1, 'David', 'Malan', 1, 95000), (2, 'Lisa', 'Adams', 2, 71000)")
db.execute("INSERT INTO students VALUES (1, 'Alice', 'Johnson', 3.8), (2, 'Bob', 'Smith', 3.2)")
db.execute("INSERT INTO courses VALUES (1, 'CS50', 'Intro to CS', 1, 1), (2, 'ENG101', 'College Writing', 2, 2)")
db.execute("INSERT INTO enrollments VALUES (1, 1, 1), (2, 2, 1), (3, 1, 2)")
db.execute("INSERT INTO grades VALUES (1, 1, 'A', 95), (2, 2, 'B', 82), (3, 3, 'A', 92)")
conn.commit()

# 4. RUN ANALYTICS DASHBOARD
print("\n" + "="*40 + "\n   UNIVERSITY DATABASE DASHBOARD\n" + "="*40)

# Query 1: Class Roster with Teacher
print("\n1. Student Rosters & Instructors:")
rows = db.execute('''
    SELECT s.first_name, c.code, t.last_name AS professor
    FROM students s
    JOIN enrollments e ON s.id = e.student_id
    JOIN courses c ON e.course_id = c.id
    JOIN teachers t ON c.teacher_id =
