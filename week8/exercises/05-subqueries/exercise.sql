-- Exercise 05: Subqueries
-- Databases: school.db and library.db

.headers on
.mode column

-- 5.1: Students with GPA above the average (school.db)
SELECT first_name, last_name, gpa 
FROM students 
WHERE gpa > (SELECT AVG(gpa) FROM students);

-- 5.2: Students enrolled in CS50 (use subquery) (school.db)
SELECT first_name, last_name 
FROM students 
WHERE id IN (
    SELECT student_id 
    FROM enrollments 
    WHERE course_id = (SELECT id FROM courses WHERE code = 'CS50')
);

-- 5.3: Students NOT enrolled in CS50 (school.db)
SELECT first_name, last_name 
FROM students 
WHERE id NOT IN (
    SELECT student_id 
    FROM enrollments 
    WHERE course_id = (SELECT id FROM courses WHERE code = 'CS50')
);

-- 5.4: Courses taught by the highest-paid teacher (school.db)
SELECT title, code 
FROM courses 
WHERE teacher_id = (SELECT id FROM teachers ORDER BY salary DESC LIMIT 1);

-- 5.5: Students enrolled in 3 or more courses (subquery in FROM) (school.db)
SELECT first_name, last_name 
FROM students
JOIN (
    SELECT student_id, COUNT(*) AS count
    FROM enrollments
    GROUP BY student_id
) AS enrollment_counts ON students.id = enrollment_counts.student_id
WHERE enrollment_counts.count >= 3;

-- 5.6: Members who borrowed more than 2 books (library.db)
SELECT first_name, last_name 
FROM members 
WHERE id IN (
    SELECT member_id 
    FROM loans 
    GROUP BY member_id 
    HAVING COUNT(*) > 2
);

-- 5.7: Books with more pages than average (library.db)
SELECT title, pages 
FROM books 
WHERE pages > (SELECT AVG(pages) FROM books);

-- 5.8: Students with at least one grade (EXISTS) (school.db)
SELECT first_name, last_name 
FROM students
WHERE EXISTS (
    SELECT 1 
    FROM enrollments 
    JOIN grades ON enrollments.id = grades.enrollment_id
    WHERE enrollments.student_id = students.id
);

-- 5.9: Courses with no grades recorded (NOT EXISTS) (school.db)
SELECT title 
FROM courses
WHERE NOT EXISTS (
    SELECT 1 
    FROM enrollments 
    JOIN grades ON enrollments.id = grades.enrollment_id
    WHERE enrollments.course_id = courses.id
);

-- 5.10 CHALLENGE: Course(s) with the most enrollments (no LIMIT) (school.db)
-- Find courses where the count equals the maximum count found in the enrollment table
SELECT title 
FROM courses 
WHERE id IN (
    SELECT course_id 
    FROM enrollments 
    GROUP BY course_id 
    HAVING COUNT(*) = (
        SELECT MAX(count) 
        FROM (SELECT COUNT(*) AS count FROM enrollments
