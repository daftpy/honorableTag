import sqlite3


class SqlStorage():
    def __init__(self):
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE frames
            (frame int, class string, x int, y int, width int, height int, color string, unique (frame, class, x, y))
        ''')
        self.connection.commit()

    def insert_rect_record(self, frame, t_class, x, y, width, height, color):
        query = 'INSERT INTO frames VALUES (?, ?, ?, ?, ?, ?, ?)'
        params = (frame, t_class, x, y, width, height, color)
        self.cursor.execute(query, params)
        self.connection.commit()
        for row in self.cursor.execute('SELECT * FROM frames'):
            print(row)

    def get_rects(self, frame):
        query = 'SELECT * FROM frames WHERE frame=?'
        t_frame = frame
        self.cursor.execute(query, (t_frame,))
        results = self.cursor.fetchall()
        return results

    def remove_rect(self, rect):
        print('removed')
        query = 'DELETE FROM frames WHERE x=? and y=? and width=? and height=?'
        x = rect.topLeft().x()
        y = rect.topRight().y()
        width = rect.width()
        height = rect.height()
        self.cursor.execute(query, (x, y, width, height))
        self.connection.commit()
