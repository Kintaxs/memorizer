import sqlite3
import time

class DictSql():
    def __init__(self):
        self.lang_conn = sqlite3.connect('sql/db/langdao-ec.db')
        self.lang_cursor = self.lang_conn.cursor()
        self.my_conn = sqlite3.connect('sql/db/my_vol.db')
        self.my_cursor = self.my_conn.cursor()

    def search(self, search_vol):

        result = self.lang_cursor.execute('SELECT EXISTS(SELECT * FROM vocabulary WHERE name = ?)', (search_vol, ))

        for i in result:
            exist_flag = i[0]
            break

        if exist_flag == 1:
            result = self.lang_cursor.execute('SELECT * FROM vocabulary WHERE name = ?', (search_vol, ))

            for i in result:
                print('')
                print(i[1], '\n')
                print(i[2].decode(), '\n')
            return 1
        else:
            print('The volcabulary is not exist!')
            return 0

    def add(self, search_vol):

        if self.search(search_vol) == 0:
            return 0

        self.my_cursor.execute('SELECT EXISTS(SELECT * FROM vocabulary WHERE name = ?)', (search_vol, ))

        if(self.my_cursor.fetchone()[0] == 0):
            self.my_cursor.execute('select count(*) from vocabulary')
            count = self.my_cursor.fetchone()[0] + 1
            self.my_cursor.execute("insert into vocabulary(id, name, date, forget) values(?, ?, ?, 1)", (count, search_vol, int(time.time())))
            self.my_conn.commit()
        else:
            print('The DB already have the word.')

        return 1

    def list_all(self):
                               
        self.my_cursor.execute('select * from vocabulary')
        results = self.my_cursor.fetchall()
        for result in results:
            print(result)

    def __del__(self):
        self.lang_conn.close()
        self.my_conn.close()
