import psycopg

db = psycopg.connect("dbname=q1 user=student password=studious")

with db.cursor() as cursor:
    # Reset the students table
    cursor.execute("DROP TABLE IF EXISTS students")
    cursor.execute(
        """
        CREATE TABLE students (
            student_id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            enrollment_date DATE
        )
    """
    )

    initial_data = [
        ("John", "Doe", "john.doe@example.com", "2023-09-01"),
        ("Jane", "Smith", "jane.smith@example.com", "2023-09-01"),
        ("Jim", "Beam", "jim.beam@example.com", "2023-09-02"),
    ]

    # Insert initial data into the students table
    cursor.executemany(
        """
        INSERT INTO students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s)
    """,
        initial_data,
    )

    db.commit()
