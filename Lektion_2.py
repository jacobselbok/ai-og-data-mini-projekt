import sqlite3
from sqlite3 import Error

# Opgave 1
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
connection = create_connection("school.db")

# Opgave 2
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    
student_db = "CREATE TABLE IF NOT EXISTS Students(student_id INTEGER, name TEXT NOT NULL, major TEXT NOT NULL)"
execute_query(connection, student_db)
courses_db = "CREATE TABLE IF NOT EXISTS Courses(course_id INTEGER, course_name TEXT NOT NULL, instructor TEXT NOT NULL)"
execute_query(connection, courses_db)

# Opgave 3
student_records = """
INSERT INTO
  Students (student_id, name, major)
VALUES
  (2, 'James', 'AI'),
  (5, 'Leila', 'Software'),
  (7, 'Brigitte', 'Medicin'),
  (11, 'Mike', 'IT'),
  (12, 'Elizabeth', 'Hardware');
"""
execute_query(connection, student_records)
courses_records = """
INSERT INTO
  Courses (course_id, course_name, instructor)
VALUES
  (22, 'Data extraction', 'Martin'),
  (27, 'Data manipulation', 'Victor'),
  (34, 'Data noise', 'Adam'),
  (35, 'Data mishaps', 'Anders'),
  (37, 'Data problems', 'Ruben');
"""
execute_query(connection, courses_records)

# Opgave 4
enrollments_db = "CREATE TABLE IF NOT EXISTS Enrollments(enrollments_id INTEGER, student_id INTEGER, course_id INTEGER)"
execute_query(connection, enrollments_db)
enrollments_records = """
INSERT INTO
  Enrollments (enrollments_id, student_id, course_id)
VALUES
  (41, 2, 22),
  (42, 2, 27),
  (43, 5, 22),
  (44, 5, 34),
  (45, 5, 35),
  (46, 7, 22),
  (47, 7, 37),
  (48, 11, 22),
  (49, 12, 27),
  (50, 12, 35);
"""
execute_query(connection, enrollments_records)

# Opgave 5
#Vælger alle kurser som en specific studerende er tilmeldt
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

query = """
SELECT
  Students.name,
  Courses.course_name
FROM
  Students
JOIN
  Enrollments ON Students.student_id = Enrollments.student_id
JOIN
  Courses ON Enrollments.course_id = Courses.course_id
WHERE
  Students.student_id = 5;
"""
results = execute_read_query(connection, query)
for result in results:
    print(result)

#Vælger alle studerende der er tilmeldt et specifikt kursus.
query = """
SELECT
  Students.name,
  Courses.course_name
FROM
  Courses
JOIN
  Enrollments ON Courses.course_id = Enrollments.course_id
JOIN
  Students ON Enrollments.student_id = Students.student_id
WHERE
  Courses.course_id = 22;
"""
results = execute_read_query(connection, query)
for result in results:
    print(result)