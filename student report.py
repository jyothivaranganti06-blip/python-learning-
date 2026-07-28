import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="jyothi@26",
    database="school_db"
)
print("database connected successfully")
cursor=conn.cursor()
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)


def add_students(name,subject,marks):
    cursor.execute("INSERT INTO STUDENTS(name,subject,marks) VALUES(%s,%s,%s)",(name,subject,marks))
    conn.commit()
def get_all_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()
def update_marks(name,new_marks):
    cursor.execute("UPDATE students SET marks=%s WHERE name=%s",(new_marks,name))
    conn.commit()

conn.close()