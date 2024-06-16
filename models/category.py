from db import cursor,conn

class Category:
    TABLE_NAME = "category"


    def __init__(self,name) -> None:
        self.id = None
        self.name = name
        pass

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
    

    @classmethod
    def get_all(cls):
        sql = f"""
           SELECT * FROM {cls.TABLE_NAME}

        """
        rows = cursor.execute(sql).fetchall()

        return [
            cls.row_to_instance(row).to_dict() for row in rows
        ]

    @classmethod
    def row_to_instance(cls,row):
        if row == None:
            return None
        
        
        category = cls(row[1])
        category.id = row[0]

        return category
       



    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL 
            )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"category table created")


    
    def save(self):
        sql = f"""
           INSERT INTO {self.TABLE_NAME} (name)
           VALUES (?)
        
        """
        cursor.execute(sql,(self.name,))
        conn.commit()
        self.id = cursor.lastrowid
   
Category.create_table()
# heels = Category("Heels")
# heels.save()

# sneakers = Category("Sneakers")
# sneakers.save()

# boots =Category("Boots")
# boots.save()

# sandals = Category("Sandals")
# sandals.save()

# flats = Category("Flats")
# flats.save()

# loafers = Category("Loafers")
# loafers.save()

# slippers = Category("Slippers")
# slippers.save()