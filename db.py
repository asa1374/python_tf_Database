import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')
    def create(self):
        sql = """
            CREATE TABLE IF NOT EXISTS MEMBER(
                USERID VARCHAR(10) PRIMARY KEY,
                PASSWORD VARCHAR(10),
                PHONE VARCHAR(10),
                REGDATE DATE DEFAULT CURRENT_TIMESTAMP 
            );
        """
        print('쿼리 체크 : {}'.format(sql))
        self.conn.execute(sql)
        self.conn.commit()

    def insert_many(self):
        data = [('lee','1','010-1234-1212')
            ,('kim','1','010-3687-8957')
            ,('park','1','010-5787-1852')]
        sql = """
            INSERT INTO MEMBER(USERID, PASSWORD, PHONE)
            VALUES (?,?,?)
        """
        self.conn.executemany(sql,data)
        self.conn.commit()

    def fetch_one(self,userid):
        sql = """
            SELECT * FROM MEMBER WHERE USERID LIKE ?
        """
        cursor = self.conn.execute(sql, userid)
        row = cursor.fetchone()
        print('조회한 정보 상세 {}'.format(row))
        return row

    def fetch_all(self):
        sql = """
            SELECT * FROM MEMBER
        """
        cursor = self.conn.execute(sql)
        rows = cursor.fetchone()
        return rows

    def count_all(self):
        sql = """
            SELECT COUNT(*) FROM MEMBER
        """
        cursor = self.conn.execute(sql)
        count = cursor.fetchone()
        print('전체 회원수 {}명'.format(count))
        return count
    def update(self):
        pass

    def remove(self):
        pass

    def drop_table(self):
        sql = """
            DROP TABLE MEMBER
        """
        self.conn.execute(sql)
        self.conn.commit()

    def login(self,userid,password):
        sql = """
            SELECT * FROM MEMBER
            WHERE USERID LIKE ?
            AND PASSWORD LIKE ?
        """
        data = [userid,password]
        cursor = self.conn.execute(sql,data)
        row = cursor.fetchone()
        print('로그인 성공 정보 {}'.format(row))













