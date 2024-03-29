import psycopg

db = psycopg.connect("dbname=q1 user=student password=studious")


# function which returns all students in the `students` table
def getAllStudents():
    try:
        with db.cursor() as cursor:
            cursor.execute("SELECT * FROM students")
            return cursor.fetchall()
    except Exception as e:
        print(e)
        return []


# function which adds a student to the `students` table
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        with db.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO students (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s)
            """,
                (first_name, last_name, email, enrollment_date),
            )
            db.commit()
    except Exception as e:
        print(e)
        db.rollback()


# function which updates the email of a student in the `students` table
def updateStudentEmail(student_id, new_email):
    try:
        with db.cursor() as cursor:
            cursor.execute(
                """
                UPDATE students
                SET email = %s
                WHERE student_id = %s
            """,
                (new_email, student_id),
            )
            db.commit()
    except Exception as e:
        print(e)
        db.rollback()


# function which deletes a student from the `students` table
def deleteStudent(student_id):
    try:
        with db.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM students
                WHERE student_id = %s
            """,
                (student_id,),
            )
            db.commit()
    except Exception as e:
        print(e)
        db.rollback()


# event loop for main program execution
while True:
    print("1. Add student")
    print("2. Update student email")
    print("3. Delete student")
    print("4. List all students")
    print("5. Exit")
    choice = input("Enter your choice: ")
    print()

    if choice == "1":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
        addStudent(first_name, last_name, email, enrollment_date)
    elif choice == "2":
        student_id = input("Enter student ID: ")
        new_email = input("Enter new email: ")
        updateStudentEmail(student_id, new_email)
    elif choice == "3":
        student_id = input("Enter student ID: ")
        deleteStudent(student_id)
    elif choice == "4":
        students = getAllStudents()
        print("ID | First Name | Last Name | Email | Enrollment Date")
        for student in students:
            print(" | ".join(map(str, student)))
    elif choice == "5":
        break
    else:
        print("Invalid choice")
    print()
