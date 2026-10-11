import sqlite3

# Connect to SQLite in-memory database[span_3](start_span)[span_3](end_span)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Enable foreign keys constraint[span_4](start_span)[span_4](end_span)
cursor.execute("PRAGMA foreign_keys = ON")

# Create STUDENTS table[span_5](start_span)[span_5](end_span)
cursor.execute("""
CREATE TABLE students(
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    email TEXT
)
""")

# Create COURSES table[span_6](start_span)[span_6](end_span)
cursor.execute("""
CREATE TABLE courses(
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    Credits INTEGER
)
""")

# Create ENROLLMENTS table[span_7](start_span)[span_7](end_span)
cursor.execute("""
CREATE TABLE enrollments(
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    FOREIGN KEY (student_id) REFERENCES students (student_id),
    FOREIGN KEY (course_id) REFERENCES courses (course_id)
)
""")

# Insert data into students[span_8](start_span)[span_8](end_span)
students = [
    (1, "Rishabh Tiwari", "Rishabh@gmail.com"),
    (2, "Ansh Tyagi", "Ansh@gmail.com"),
    (3, "Sushant Singh", "sushant@gmail.com"),
    (4, "Aryan Rawat", "Aryan@gmail.com")
]
cursor.executemany("INSERT INTO students VALUES (?,?,?)", students)

# Insert data into courses[span_9](start_span)[span_9](end_span)
courses = [
    (101, "Python Programming", 3),
    (102, "Database management system", 3),
    (103, "Computer Networks", 2)
]
cursor.executemany("INSERT INTO courses VALUES (?,?,?)", courses)

# Insert data into enrollments[span_10](start_span)[span_10](end_span)
enrollments = [
    (1, 1, 101, "2026-08-20"),
    (2, 1, 102, "2026-08-21"),
    (3, 2, 101, "2026-08-22"),
    (4, 2, 103, "2026-08-22"),
    (5, 3, 102, "2026-08-21")
]
cursor.executemany("INSERT INTO enrollments VALUES (?,?,?,?)", enrollments)

conn.commit()

# Print STUDENTS table[span_11](start_span)[span_11](end_span)
print("\n--- STUDENTS ---")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Print COURSES table[span_12](start_span)[span_12](end_span)
print("\n--- COURSES ---")
cursor.execute("SELECT * FROM courses")
for row in cursor.fetchall():
    print(row)

# Print ENROLLMENTS table[span_13](start_span)[span_13](end_span)
print("\n--- ENROLLMENTS ---")
cursor.execute("SELECT * FROM enrollments")
for row in cursor.fetchall():
    print(row)

# Print Joined Student Course Details[span_14](start_span)[span_14](end_span)
print("\n--- STUDENT COURSE DETAILS ---")
cursor.execute("""
    SELECT 
        s.student_id, 
        s.student_name, 
        c.course_name, 
        e.enrollment_date 
    FROM enrollments e 
    JOIN students s 
        ON e.student_id = s.student_id 
    JOIN courses c 
        ON e.course_id = c.course_id
""")
for row in cursor.fetchall():
    print(row)

# Close connection[span_15](start_span)[span_15](end_span)
conn.close()