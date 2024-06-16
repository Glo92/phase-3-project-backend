from db import cursor, conn

class Shoes:
    TABLE_NAME = "shoes"
    def __init__(self,name,image,description,price,category_id):
        self.id = None
        self.name = name
        self.image = image
        self.description = description
        self.price = price
        self.category_id = category_id
        self.category = None
        pass

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "description": self.description,
            "price": self.price,
            "category": self.category
        }
    
    @classmethod
    def find_all(cls):
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
        
        shoe = cls(row[1], row[2], row[3],row[4], row[5])
        shoe.id = row[0]
        


    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              image VARCHAR NOT NULL,
              description TEXT NOT NULL,
              price DECIMAL NOT NULL,
              category_id INTEGER NOT NULL REFERENCES category(id)
            
            )
           
        """
        cursor.execute(sql)
        conn.commit()
        print("shoe table created")

    def save(self):
        sql = f"""
           INSERT INTO {self.TABLE_NAME} (name,image,description,price,category_id)
           VALUES (?,?,?,?,?)
        """
        cursor.executemany(sql, (self.name, self.image, self.description, self.price, self.category_id))
        conn.commit()
        self.id= cursor.lastrowid

        return self.to_dict()



Shoes.create_table()

shoes = [
    # ("office heels"), ("backend/office-heels.webp"),("black,green,white size: 36-42"),(59.99),( 1),
    ("Running shoes", "backend/images/running-shoes.webp","black,gray,white size: 36-42", 87.90,2),
    ("Puma shoes", "backend/images/puma-shoes.jpeg","black,blue,grey,white size: 36-42", 98.54,2),
    ("Ankle heel boots","backend/images/boot-450x450.jpg","black,blue,grey,white size: 36-42",76.54,3),
    ("stylish Boots","backend/images/boots-1.jpeg","black,blue,grey,white size: 36-42",67.58,3),
    ("Boots","backend/images/boots-2.jpeg","black,blue,grey,white size: 36-42",75.23,3),
    ("Boots","backend/images/boots-3.jpeg","black,blue,grey,white size: 36-42",78.90,3),
    ("Boots","backend/images/boots-3.webp","black,blue,grey,white size: 36-42",78.90,3),
    ("Boots","backend/images/boots-4.webp","black,blue,grey,white size: 36-42",56.45,3),
    ("Boots","backend/images/boots-5.webp","black,blue,grey,white size: 36-42",95.55,3),
    ("Boots","backend/images/boots-6.webp","black,blue,grey,white size: 36-42",87.98,3),
    ("Boots","backend/images/boots-7.webp","black,blue,grey,white size: 36-42",76.76,3),
    ("Boots","backend/images/boots-8.jpg","black,blue,grey,white size: 36-42",77.43,3),
    ("Heels","backend/images/heels-1.jpg","black,blue,grey,white size: 36-42",90.67,1),
    ("Heels","backend/images/heels-2.webp","black,blue,grey,white size: 36-42",98.78,1),
    ("Heels","backend/images/heels-3.webp","black,blue,grey,white size: 36-42",99.99,1),
    ("Hiking shoes","backend/images/hiking-shoes.jpeg","black,blue,grey,white size: 36-42",78.88,2),
    ("Loafers","backend/images/loafers.jpeg","black,blue,grey,white size: 36-42",78.50,6),
    ("Office heels","backend/images/office-heels.webp","black,blue,grey,white size: 36-42",99.90,1),
    ("Office heels","backend/images/office-shoes-1.jpg","black,blue,grey,white size: 36-42",87.90,1),
    ("Sandals","backend/images/sandal-7.webp","black,blue,grey,white size: 36-42",65.45,4),
    ("Sandals","backend/images/sandals-1.jpeg","black,blue,grey,white size: 36-42",75.45,4),
    ("Sandals","backend/images/sandals-3.jpeg","black,blue,grey,white size: 36-42",55.45,4),
    ("Sandals","backend/images/sandals-2.jpeg","black,blue,grey,white size: 36-42",95.45,4),
    ("Sandals","backend/images/sandals-3.webp","black,blue,grey,white size: 36-42",75.45,4),
    ("Sandals","backend/images/sandals-4.webp","black,blue,grey,white size: 36-42",95.45,5),
    ("Sandals","backend/images/sandals-5.webp","black,blue,grey,white size: 36-42",80.45,5),
    ("Sandals","backend/images/sandals-6.webp","black,blue,grey,white size: 36-42",59.45,5),
    ("Sandals","backend/images/sandals-8.webp","black,blue,grey,white size: 36-42",69.45,4),
    ("Sandals","backend/images/sandals-9.webp","black,blue,grey,white size: 36-42",64.45,4),
    ("Sneakers","backend/images/sneakers-1.jpeg","black,blue,grey,white size: 36-42",89.45,2),
    ("Sneakers","backend/images/sneakers-2.jpeg","black,blue,grey,white size: 36-42",67.45,2),
    ("Sneakers","backend/images/skechers-shoes.jpeg","black,blue,grey,white size: 36-42",88.32,2),
    ("Sketchers","backend/images/skechers-shoes.jpeg","black,blue,grey,white size: 36-42",67.34,2)

]
# cursor.executemany("""
#     INSERT INTO shoes (name, image, description,price,category_id ) VALUES (?, ?, ?, ?, ?)
# """, shoes)

# conn.commit()
# conn.close()
for shoe in shoes:
    cursor.execute('''
        INSERT INTO shoes (name,image, description, price, category_id) VALUES (?, ?, ?, ?, ?)
    ''', shoe)

conn.commit()
# conn.close()
# for data in shoes:
#     shoe = Shoes(data)
#     shoe.save()