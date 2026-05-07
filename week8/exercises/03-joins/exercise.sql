-- Exercise 03: Joins
-- Databases: school.db and library.db

.headers on
.mode column

-- 3.1: Student full name + course title for every enrollment (school.db)
SELECT students.first_name, students.last_name, courses.title
FROM students
JOIN enrollments ON students.id = enrollments.student_id
JOIN courses ON enrollments.course_id = courses.id;

-- 3.2: Course title + teacher's full name (school.db)
SELECT courses.title, teachers.first_name, teachers.last_name
FROM courses
JOIN teachers ON courses.teacher_id = teachers.id;

-- 3.3: Teacher's full name + their department name (school.db)
SELECT teachers.first_name, teachers.last_name, departments.name
FROM teachers
JOIN departments ON teachers.department_id = departments.id;

-- 3.4: Student name, course title, teacher name, letter grade (school.db)
SELECT students.first_name, students.last_name, courses.title, teachers.last_name AS professor, grades.letter_grade
FROM students
JOIN enrollments ON students.id = enrollments.student_id
JOIN courses ON enrollments.course_id = courses.id
JOIN teachers ON courses.teacher_id = teachers.id
JOIN grades ON enrollments.id = grades.enrollment_id;

-- 3.5: Students with NO enrollments (LEFT JOIN) (school.db)
SELECT students.first_name, students.last_name
FROM students
LEFT JOIN enrollments ON students.id = enrollments.student_id
WHERE enrollments.id IS NULL;

-- 3.6: Courses with NO students enrolled (LEFT JOIN) (school.db)
SELECT courses.title, courses.code
FROM courses
LEFT JOIN enrollments ON courses.id = enrollments.course_id
WHERE enrollments.id IS NULL;

-- 3.7: Book title + author's full name (library.db)
SELECT books.title, authors.first_name, authors.last_name
FROM books
JOIN book_authors ON books.id = book_authors.book_id
JOIN authors ON book_authors.author_id = authors.id;

-- 3.8: Genre name + all books in that genre (include empty genres) (library.db)
SELECT genres.name, books.title
FROM genres
LEFT JOIN books ON genres.id = books.genre_id;

-- 3.9: Member full name + every book they borrowed (include non-borrowers) (library.db)
SELECT members.first_name, members.last_name, books.title
FROM members
LEFT JOIN loans ON members.id = loans.member_id
LEFT JOIN books ON loans.book_id = books.id;

-- 3.10 CHALLENGE: Loans with member name, book title, dates (library.db)
--      Use COALESCE to show "Not returned" if return_date is NULL
SELECT members.first_name, members.last_name, books.title, loans.loan_date, 
       COALESCE(loans.return_date, 'Not returned') AS status
FROM loans
JOIN members ON loans.member_id = members.id
JOIN books ON loans.book_id = books.id;
