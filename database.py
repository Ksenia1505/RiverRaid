import sqlite3


class Database:
    def __init__(self):
        db_name = 'settings.db'
        con = sqlite3.connect(db_name)
        self.cur = con.cursor()

    def get_coordinates(self, object_name):
        sql = """SELECT DISTINCT 
                coordinates.x, 
                coordinates.y, 
                coordinates.start_y 
            FROM coordinates 
            INNER JOIN objects ON coordinates.object_id = objects.id 
            WHERE objects.name = '""" + object_name + """' """
        return self.cur.execute(sql).fetchall()
