import dmPython
import pymysql


class ConnDB():

    def __init__(self, dbType, dbName, dbPwd, dbUrl,database=None):
        if dbType == 'dm':
            self.conn = dmPython.Connection(dbName, dbPwd, dbUrl)
            self.cur = self.conn.cursor()
        elif dbType == 'mysql':
            self.conn = pymysql.Connection(user=dbName, password=dbPwd, host=dbUrl, database=database)
            self.cur = self.conn.cursor()

    def execute_sql(self, sql):
        self.cur.execute(sql)
        return self.cur


if __name__ == '__main__':
    sql = "select data from lcsz"
    db = ConnDB('dm', 'HCOA', '123456789', '127.0.0.1')
    # db = ConnDB('mysql', 'root', 'root', '127.0.0.1', database='hcitdata')
    result = db.execute_sql(sql)
    print(result)
    while True:
        item = result.fetchone()
        if item is None:
            break
        print(item)

# conn = dmPython.Connection("HCOA","123456789","172.16.12.230")
# cur = conn.cursor()
# cur.execute("select * from SYS_PERSON")
# result = cur.fetchall()
# print(result)