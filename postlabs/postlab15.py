import sqlite3

# Connect to database
conn = sqlite3.connect('student_record.db')
cursor = conn.cursor()

# Create student table
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    Enrollment INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

# Create subject table (linked to student)
cursor.execute('''
CREATE TABLE IF NOT EXISTS subject_enrollment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Enrollment INTEGER,
    Subject TEXT NOT NULL,
    Mark INTEGER NOT NULL,
    FOREIGN KEY (Enrollment) REFERENCES student(Enrollment)
)
''')

# Insert students
students = [
    (92301733016, 'ASHUTOSH KUMAR SINGH'),
    (92301733017, 'HARSH VISHALBHAI TRIVEDI'),
    (92301733027, 'VIRAJ PRAKASHBHAI VAGHASIYA')
]
cursor.executemany('INSERT OR IGNORE INTO student (Enrollment, name) VALUES (?, ?)', students)

# Insert multiple subjects per student
subjects = [
    (92301733016, 'PWP', 95),
    (92301733016, 'DBMS', 88),
    (92301733017, 'PWP', 85),
    (92301733017, 'OS', 90),
    (92301733027, 'PWP', 90),
    (92301733027, 'CN', 92)
]
cursor.executemany('''
INSERT INTO subject_enrollment (Enrollment, Subject, Mark)
VALUES (?, ?, ?)
''', subjects)

conn.commit()

# Fetch all subjects for a student
cursor.execute('''
SELECT student.name, subject_enrollment.Subject, subject_enrollment.Mark
FROM student
JOIN subject_enrollment ON student.Enrollment = subject_enrollment.Enrollment
''')
records = cursor.fetchall()
print("📚 Student Subject Records:")
for record in records:
    print(record)

# Close connection
conn.close()