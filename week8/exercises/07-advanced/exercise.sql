-- Exercise 07: Advanced SQL
-- Databases: school.db and library.db

.headers on
.mode column

-- 7.1: Create an index on students.gpa, then EXPLAIN QUERY PLAN
CREATE INDEX idx_students_gpa ON students(gpa);

EXPLAIN QUERY PLAN
SELECT * FROM students WHERE gpa > 3.5;

-- 7.2: Create view 'enrollment_details', then query for 'A' grades
CREATE VIEW enrollment_details AS
SELECT s.first_name, s.last_name, c.title, g.letter_grade
FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c ON e.course_id = c.id
JOIN grades g ON e.id = g.enrollment_id;

SELECT * FROM enrollment_details WHERE letter_grade = 'A';

-- 7.3: Create view 'course_statistics' with count and avg final score
CREATE VIEW course_statistics AS
SELECT c.title, COUNT(e.id) AS student_count, ROUND(AVG(g.final), 1) AS avg_score
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
LEFT JOIN grades g ON e.id = g.enrollment_id
GROUP BY c.id;

SELECT * FROM course_statistics;

-- 7.4: Insert a new student (newstudent@school.edu, 2024, NULL gpa)
INSERT INTO students (first_name, last_name, email, enrollment_year, gpa)
VALUES ('New', 'Student', 'newstudent@school.edu', 2024, NULL);

-- 7.5: Update student id=17 (Quinn Moore) to set gpa = 3.22
UPDATE students SET gpa = 3.22 WHERE id = 17;

-- 7.6: Preview and then DELETE all grades with letter_grade = 'F'
-- Step 1: SELECT to preview
SELECT * FROM grades WHERE letter_grade = 'F';

-- Step 2: DELETE
DELETE FROM grades WHERE letter_grade = 'F';

-- 7.7: Transaction to enroll student 1 in course 13 + add grade record
BEGIN TRANSACTION;
INSERT INTO enrollments (student_id, course_id, enrollment_date)
VALUES (1, 13, DATE('now'));

INSERT INTO grades (enrollment_id, letter_grade)
VALUES (last_insert_rowid(), NULL);
COMMIT;

-- 7.8: Transaction: decrease available_copies for book 3, insert loan (library.db)
BEGIN TRANSACTION;
UPDATE books 
SET available_copies = available_copies - 1 
WHERE id = 3 AND available_copies > 0;

INSERT INTO loans (member_id, book_id, loan_date, due_date)
VALUES (1, 3, DATE('now'), DATE('now', '+14 days'));
COMMIT;

-- 7.9: EXPLAIN QUERY PLAN comparison
-- Version A:
EXPLAIN QUERY PLAN
SELECT * FROM teachers WHERE salary * 1.1 > 90000;

-- Version B:
EXPLAIN QUERY PLAN
SELECT * FROM teachers WHERE salary > 90000 / 1.1;

-- Your explanation of the difference:
-- Version A performs a "Full Table Scan" because the mathematical operation on the column 
-- prevents SQLite from using an index on 'salary'. 
-- Version B is "Search" or "Index" friendly because the column remains isolated on one side 
-- of the operator, allowing the engine to utilize B-Tree indexing.

-- 7.10 CHALLENGE: Create compound index for enrollments(student_id, course_id)
CREATE UNIQUE INDEX idx_student_course_enroll ON enrollments(student_id, course_id);
