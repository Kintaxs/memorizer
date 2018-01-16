import sqlite3

class DictSql():
    def __init__(self):
        self.conn = sqlite3.connect('sql/db/langdao-ec.db')
        self.c = self.conn.cursor()

    def search(self, search_vol):

        result = self.c.execute('SELECT EXISTS(SELECT * FROM vocabulary WHERE name = ?)', (search_vol, ))

        for i in result:
            exist_flag = i[0]
            break

        if exist_flag == 1:
            result = self.c.execute('SELECT * FROM vocabulary WHERE name = ?', (search_vol, ))

            for i in result:
                print('index: ',i[0])
                print('name: ',i[1])
                print('meaning: ', i[2].decode())
        else:
            print('the volcabulary is not exist!')

    def __del__(self):
        print('del DictSql')
        self.conn.close()
