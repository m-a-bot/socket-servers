import sqlite3


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

def adapt_point(point):
    return f"{point.x};{point.y}"
sqlite3.register_adapter(Point, adapt_point)


def convert_point(s):
    x, y = map(float, s.split(b";"))
    return Point(x, y)

sqlite3.register_converter("point", convert_point)

p = Point(5.0, 10)
con = sqlite3.connect("test.db",
detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.execute("CREATE TABLE if not exists test(p point)")
cur.execute("INSERT INTO test(p) VALUES(?)", (p,))
cur.execute("SELECT p FROM test")
print("with declared types:", cur.fetchall())
con.commit()