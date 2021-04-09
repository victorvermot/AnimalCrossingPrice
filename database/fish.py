import sqlite3

conn = sqlite3.connect(r'database\fishes.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS fish(
       name text,
       price text
)""")

class Fish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def add_fish(self):
        with conn:
            cur.execute("""INSERT INTO fish VALUES (:name, :price)""", 
            {'name': self.name, 'price': self.price})

    def get_fishes():
        cur.execute("SELECT rowid, * FROM fish")
        return cur.fetchall()

    def remove_appart(instance):
        """Takes a class instance and removes all entries tied to it"""
        with conn:
            cur.execute("DELETE from fish WHERE nom = :instance",
            {'instance': instance})


