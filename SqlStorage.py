import sqlite3
import csv


class SqlStorage():
    def __init__(self):
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE frames
            (frame int, class string, x int, y int, width int,
            height int, color string, unique (frame, class, x, y))
        ''')
        self.connection.commit()

    def insert_rect_record(self, frame, t_class, x, y, width, height, color):
        query = 'INSERT INTO frames VALUES (?, ?, ?, ?, ?, ?, ?)'
        params = (frame, t_class, x, y, width, height, color)
        self.cursor.execute(query, params)
        self.connection.commit()

    def get_rects(self, frame):
        query = 'SELECT * FROM frames WHERE frame=?'
        t_frame = frame
        self.cursor.execute(query, (t_frame,))
        results = self.cursor.fetchall()
        return results

    def get_all_rects(self):
        results = self.cursor.execute('SELECT * FROM frames')
        results = self.cursor.fetchall()
        return results

    def remove_rect(self, rect):
        print('removed')
        query = 'DELETE FROM frames \
            WHERE x=? and y=? and width=? and height=?'
        x = rect.topLeft().x()
        y = rect.topRight().y()
        width = rect.width()
        height = rect.height()
        self.cursor.execute(query, (x, y, width, height))
        self.connection.commit()

    def export_db_to_csv(self, file_name, class_list):
        rows =  self.get_all_rects()
        csv_writer = csv.writer(open(f'{file_name}.csv', 'w', newline=''))
        csv_writer.writerow(class_list)
        csv_writer.writerows(rows)

    def load_csv_to_db(self, file_name):
        with open(f'{file_name}.csv') as f:
            reader = csv.reader(f)
            class_list = next(reader)
            for row in reader:
                self.cursor.execute(
                    "INSERT INTO frames VALUES (?, ?, ?, ?, ?, ?, ?)",
                    row
                )
        return class_list
