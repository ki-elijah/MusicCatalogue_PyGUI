import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Song (id INTEGER PRIMARY KEY, song text, artist text, biography text, genre text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM Song")
        rows = self.cur.fetchall()
        return rows

    def insert(self, song, artist, biography, genre):
        self.cur.execute("INSERT INTO Song VALUES (NULL, ?, ?, ?, ?)", (song, artist, biography, genre))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM Song WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, song, artist, biography, genre):
        self.cur.execute("UPDATE Song SET song = ?, artist = ?, biography = ?, genre = ? WHERE id = ?", (song, artist, biography, genre, id))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close

db = Database('catalog.db')
#db.insert("God I look to you","Jenn Johnson","Gospel Artist","Worship")
