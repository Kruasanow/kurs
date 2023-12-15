import sqlite3

quotes = [
   {
       "id": 3,
       "author": "Rick Cook",
       "text": "Программирование сегодня — это гонка разработчиков программ, стремящихся писать программы с большей и лучшей идиотоустойчивостью, и вселенной, которая пытается создать больше отборных идиотов. Пока вселенная побеждает.",
       "rating":'5'
   },
   {
       "id": 5,
       "author": "Waldi Ravens",
       "text": "Программирование на С похоже на быстрые танцы на только что отполированном полу людей с острыми бритвами в руках.",
       "rating":'3'
   },
   {
       "id": 6,
       "author": "Mosher's Law of Software Engineering",
       "text": "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.",
       "rating":'2'
   },
   {
       "id": 8,
       "author": "Yoggi Berra",
       "text": "В теории, теория и практика неразделимы. На практике это не так.",
       "rating":'1'
   },

]

about_me = {
    "name": "Вадим",
    "surname": "Шиховцов",
    "email": "vshihovcov@specialist.ru"
}

def create():
    try:
        create_table = """
                        CREATE TABLE IF NOT EXISTS quotes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        author TEXT NOT NULL,
                        text TEXT NOT NULL
                        );
                        """

        conn = sqlite3.connect("s.db")
        cur = conn.cursor()
        cur.execute(create_table)
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception:
        return False

def db_data_addiction():
    try:
        conn = sqlite3.connect("s.db")
        cur = conn.cursor()
        for _ in quotes:
            cur.execute("INSERT INTO quotes (author,text) VALUES (?,?)",(_['author'],_['text']))
            conn.commit()
        cur.close()
        conn.close()
    except Exception:
        print('db failed!')


def get_all_post():
    try:
        conn = sqlite3.connect("s.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM quotes")
        q = cur.fetchall()
        cur.close()
        conn.close()
    except Exception:
        pass
    return q


def get_post_by_id(id):
    try:
        conn = sqlite3.connect("s.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM quotes WHERE id=?;",(id,))
        q = cur.fetchall()
        cur.close()
        conn.close()
    except Exception:
        pass
    return q

def insert_data(i,a,t):
    try:
        conn = sqlite3.connect("s.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO quotes VALUES (?,?,?);",(int(i),str(a),str(t)))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception:
        return False

def delete_data(i):
    try:
        conn = sqlite3.connect("s.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM quotes WHERE id=?;",(int(i),))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception:
        return False

def update_data(i,a,t):
    try:
        conn = sqlite3.connect("s.db")
        cur = conn.cursor()
        cur.execute("UPDATE quotes SET author=?, text=? WHERE id=?;",(str(a),str(t),int(i)))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception:
        return False
