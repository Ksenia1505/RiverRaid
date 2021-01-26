import sqlite3


class Database:
    """База данных"""

    def __init__(self):
        db_name = 'settings.db'
        con = sqlite3.connect(db_name)
        self.cur = con.cursor()

    def get_coordinates(self, object_name):
        """Получение координат объекта по его имени"""
        sql = """SELECT DISTINCT 
                coordinates.x, 
                coordinates.y, 
                coordinates.start_y,
                coordinates.direction
            FROM coordinates 
            INNER JOIN objects ON coordinates.object_id = objects.id 
            WHERE objects.name = '""" + object_name + """' """
        return self.cur.execute(sql).fetchall()
