import sqlite3


class SQLite():
    def __init__(self):
        self.connect()
    def connect(self):
        self.connection = sqlite3.connect('PATH')
        self.cursor = self.connection.cursor()


    def delet_info(self):
        self.cursor.execute("""DELETE FROM tranzaction_info """)
        self.connection.commit()

    def insert_info_tranzaction(self, value, from_api, to_api, tag):
        self.cursor.execute("INSERT INTO tranzaction_info  VALUES (NULL, ?, ?, ?, ?)", (value, from_api, to_api, tag))
        self.connection.commit()

    def select_total_count_value(self):
        self.cursor.execute(""" SELECT sum(value), tag, count(*) as total_tag From tranzaction_info GROUP BY tag HAVING count(*) > 1""")
        rows = self.cursor.fetchall()
        row = [row for row in rows]
        return row

    
# if __name__ == "__main__":
#     SQLite().select_total_count_value()