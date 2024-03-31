import sqlite3
from providers.cancer_provider import CancerProvider


class DataProvider:
    con: sqlite3.Connection
    cur: sqlite3.Cursor
    cancer_provider: CancerProvider
    patient_id: int
    med_id: int

    @classmethod
    def initialize(self):
        self.con = sqlite3.connect("cancerai.db", check_same_thread=False)
        self.cur = self.con.cursor()
        self.create_db()
        self.cancer_provider = CancerProvider()

    @classmethod
    def create_db(self):
        exists = self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='patient'").fetchone()
        if exists:
            return
        # for dates: https://www.sqlite.org/lang_datefunc.html
        # calculate age from byear
        self.cur.execute("create table patient( \
                        id integer not null primary key autoincrement, \
                        first_name text not null, \
                        last_name text not null, \
                        byear text not null \
                        )")

        self.cur.execute("create table med( \
                        id integer not null primary key autoincrement, \
                        first_name text not null, \
                        last_name text not null \
                        )")

        self.cur.execute("create table result( \
                        id integer not null primary key autoincrement, \
                        patient_id integer not null, \
                        med_id integer not null, \
                        cancer text not null, \
                        result text not null, \
                        comment text not null, \
                        date text not null \
                        )")

        self.cur.execute("insert into patient (first_name, last_name, byear) values ('Имя', 'Фамилий', '01-01-2000')")
        self.cur.execute("insert into med (first_name, last_name) values ('Имя2', 'Фамилий2')")

        self.con.commit()

    @classmethod
    def verify_login(self, check_patient_id, check_med_id):
        exists = self.cur.execute("SELECT 1 FROM patient WHERE id = ? \
                                    UNION ALL \
                                    SELECT 1 FROM med WHERE id = ?", (check_patient_id, check_med_id)).fetchall()
        if len(exists) < 2:
            return False
        self.patient_id = check_patient_id
        self.med_id = check_med_id
        return True

    @classmethod
    def get_patient_info(self):
        result = self.cur.execute("select first_name, last_name, byear from patient where id = ?", (self.patient_id,)).fetchone()
        if result:
            return result

    @classmethod
    def get_patient_results(self):
        result = self.cur.execute("select date, med_id, cancer, result, comment from result where patient_id = ?", (self.patient_id,)).fetchmany()
        if result:
            return result

    @classmethod
    def get_med_info(self):
        result = self.cur.execute("select first_name, last_name from med where id = ?", (self.med_id,)).fetchone()
        if result:
            return result

    @classmethod
    def cancer_predict(self):
        pass