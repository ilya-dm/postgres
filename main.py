import psycopg2 as pg

conn = pg.connect(dbname='test_db', user='test',
                  password='1234')
students = list()


def create_db():
    sql = input("Введите текст запроса:")
    with pg.connect(dbname='test_db', user='test',
                    password='1234') as conn:
        cur = conn.cursor()
        cur.execute(sql)


def add_students(course_id, students):
    with pg.connect(dbname='test_db', user='test',
                    password='1234') as conn:
        cur = conn.cursor()

        for student in students:
            cur.execute("""insert into student(id, name, gpa, birth) values (%s, %s, %s, %s); """, (student['id'],
                                                                                                    student['name'],
                                                                                                    student['gpa'],
                                                                                                    student['birth']))
            cur.execute("""insert into 
            student_course (student_id, course_id) values (%s, %s)""", (student['id'], course_id))
        conn.commit()
        cur.execute("""select s.id, s.name, c.name from student_course sc
                    join student s on s.id = sc.student_id 
                    join course c on c.id = sc.course_id""")
        data = cur.fetchall()

    return data


def get_students(course_id):
    with pg.connect(dbname='test_db', user='test',
                    password='1234') as conn:
        cur = conn.cursor()
        cur.execute("""select s.id, s.name, c.name from student_course sc
                            join student s on s.id = sc.student_id 
                            join course c on c.id = sc.course_id
                            where sc.course_id =%s""", (course_id,))
        data = cur.fetchall()
    return data


def add_student(id, name, gpa, birth):
    person = {'id': id, 'name': name, 'gpa': gpa, 'birth': birth}
    students.append(person)
    return students


def get_student(student_id):
    with pg.connect(dbname='test_db', user='test',
                    password='1234') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM student where id=%s', student_id)
        data = cur.fetchall()
    return data

def add_course(id, name):
    with pg.connect(dbname='test_db', user='test',
                    password='1234') as conn:
        cur = conn.cursor()
        cur.execute("""insert into 
                   course (id, name) values (%s, %s)""", (id, name))
        conn.commit()
        cur.execute("""select * from course where id =%s""", (id,))
        data = cur.fetchall()
    return data


if __name__ == '__main__':
    students = [{'id': 17, 'name': 'Oleg', 'gpa': 3.5, 'birth': None}]
    print(add_student(88, 'Vova', 4.5, '4.01.2000'))
    #print(add_course(7, 'programming'))
