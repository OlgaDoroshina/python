from sqlalchemy import create_engine
from sqlalchemy.sql import text
import psycopg2

db_connection_string = "postgresql://postgres:2335108@localhost:5432/mydatabase"


def test_select_student():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from student").fetchall()
    row1 = rows[0]

def test_select_lessons():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from lesson where \"name\" = :name and \"company_id\" >= :company_id")
    params = {
        'name': 'QA',
        'company_id': 86.2
    }
    rows = db.execute(sql_statement, params).fetchall()

    assert len(rows) == 0

def test_insert_company():
    db = create_engine(db_connection_string)
    sql = text("insert into company (\"name\") values (:new_name)")
    rows = db.execute(sql, new_name = 'SkyPro')

def test_insert_student():
    db = create_engine(db_connection_string)
    sql = text("insert into student (first_name, last_name, middle_name, phone, email, birthdate, avatar_url, company_id) values (:new_first_name, :new_last_name, :new_middle_name, :new_phone, :new_email, :new_birthdate, :new_avatar_url, :company_id)")
    rows = db.execute(sql, new_first_name = 'Olga', new_last_name = 'Doroshina', new_middle_name = '-', new_phone = '89199111187', new_email = 'doroshina@mail.ru', new_birthdate = '1989-27-07', company_id = 87.2)

def test_update_student():
    db = create_engine(db_connection_string)
    sql = text("update employee set last_name = :last_name, phone = :phone, email = :mail, avatar_url = :url, is_active = :is_active  where id = :employee_id")
    rows = db.execute(sql, last_name = 'Kluev', phone = '89178858545', mail = 'Kluev@mail.ru', url = '-', employee_id = 19)

def test_delete_student():
    db = create_engine(db_connection_string)
    sql = text("delete from employee where id = :employee_id")
    rows = db.execute(sql, employee_id = 19)

