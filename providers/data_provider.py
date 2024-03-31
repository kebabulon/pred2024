import sqlite3

class DataProvider:
    con: sqlite3.Connection
    cur: sqlite3.Cursor
    date_rn: str

    @classmethod
    def initialize(self):
        self.con = sqlite3.connect("rooms.db", check_same_thread=False)
        self.cur = self.con.cursor()
        self.create_db()

    @classmethod
    def create_db(self):
        exists = self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='answers'").fetchone()
        if exists:
            return
        # for dates: https://www.sqlite.org/lang_datefunc.html
        # calculate age from byear
        self.cur.execute("create table answers( \
                        id integer not null primary key autoincrement, \
                        date text not null, \
                        ans integer not null \
                        )")

        self.con.commit()

    @classmethod
    def change_ans(self, date, ans):
        self.cur.execute("insert into answers (date, ans) values (?, ?)", (date, ans))

    @classmethod
    def get_ans(self, date):
        result = self.cur.execute("select ans from answers where date = ?", (date,)).fetchone()
        if result:
            return result
