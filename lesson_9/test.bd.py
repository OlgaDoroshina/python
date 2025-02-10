from sqlalchemy import create_engine, text
import psycopg2

db_connection_string = "postgresql://postgres:2335108@localhost:5432/mydatabase"
db = create_engine(db_connection_string)

def test_insert():
    db = create_engine(db_connection_string)
    sql = text("insert into users(\"user_email\") values (:new_user)")
    rows = db.execute(sql, new_user = 'olga27.skypro@gmail.com')
    assert rows[-1] == 'olga27.skypro@gmail.com'

def test_update():
    db = create_engine(db_connection_string)
    sql = text("update users set user_email = :email where user_email = :user_email")
    rows = db.execute(sql, email = 'newolga27.skypro@gmail.com', user_email = 'olga27.skypro@gmail.com')

def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from users where user_email = :email")
    rows = db.execute(sql, email = 'newolga27.skypro@gmail.com')