from db import cursor, conn

class Shoe:
    TABLE_NAME = "shoe"
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
        
        return shoe


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
        cursor.execute(sql, (self.name, self.image, self.description, self.price, self.category_id))
        conn.commit()
        self.id= cursor.lastrowid

        return self.to_dict()



Shoe.create_table()

# shoes = [
#     ("Casual Sneaker","https://backyardshoez.co.ke/wp-content/uploads/2024/04/DSC_4061-450x450.webp", "A stylish casual sneaker", 49.99, 2),
#     ("Running shoes", "https://backyardshoez.co.ke/wp-content/uploads/2023/12/Backyard-Shoez-sneakers25-450x450.webp","black,gray,white size: 36-42", 87.90,2),
#     ("Puma shoes","https://backyardshoez.co.ke/wp-content/uploads/2023/12/Backyard-Shoez-sneakers29-450x450.webp" ,"black,blue,grey,white size: 36-42", 98.54,2),
#     ("Ankle heel boots","https://backyardshoez.co.ke/wp-content/uploads/2023/12/Backyard-Shoez-boots10-450x450.webp","black,blue,grey,white size: 36-42",76.54,3),
#     ("stylish Boots","https://backyardshoez.co.ke/wp-content/uploads/2024/04/DSC_4148-450x450.webp","black,blue,grey,white size: 36-42",67.58,3),
#     ("Boots","https://backyardshoez.co.ke/wp-content/uploads/2024/04/DSC_3845-450x450.webp","black,blue,grey,white size: 36-42",75.23,3),
#     ("Boots","https://backyardshoez.co.ke/wp-content/uploads/2023/12/Backyard-Shoez-boots6-450x450.webp","black,blue,grey,white size: 36-42",78.90,3),
#     ("Boots","https://backyardshoez.co.ke/wp-content/uploads/2024/04/DSC_3882-450x450.webp","black,blue,grey,white size: 36-42",78.90,3),
#     ("Boots","https://backyardshoez.co.ke/wp-content/uploads/2024/01/DSC_2103-450x450.webp","black,blue,grey,white size: 36-42",56.45,3),
#     ("Boots","https://backyardshoez.co.ke/wp-content/uploads/2023/12/Backyard-Shoez-boots3-450x450.webp","black,blue,grey,white size: 36-42",95.55,3),
#     ("Boots","https://backyardshoez.co.ke/wp-content/uploads/2024/04/DSC_3888-450x450.webp","black,blue,grey,white size: 36-42",87.98,3),
#     ("Heels","https://backyardshoez.co.ke/wp-content/uploads/2024/04/DSC_3975-450x450.webp","black,blue,grey,white size: 36-42",90.67,1),
#     ("Heels","https://backyardshoez.co.ke/wp-content/uploads/2024/04/DSC_3800-450x450.webp","black,blue,grey,white size: 36-42",98.78,1),
#     ("Heels","https://backyardshoez.co.ke/wp-content/uploads/2024/03/Backyard-Shoez-chunky-heels-2-450x450.webp","black,blue,grey,white size: 36-42",99.99,1),
#     ("Hiking shoes","https://backyardshoez.co.ke/wp-content/uploads/2024/02/DSC_2633-450x450.webp","black,blue,grey,white size: 36-42",78.88,2),
#     ("Loafers","https://backyardshoez.co.ke/wp-content/uploads/2024/02/DSC_2581-450x450.webp","black,blue,grey,white size: 36-42",78.50,6),
#     ("Sandals","https://backyardshoez.co.ke/wp-content/uploads/2024/03/DSC_3562-450x450.webp","black,blue,grey,white size: 36-42",67.45,4),
#     ("Sneakers","https://backyardshoez.co.ke/wp-content/uploads/2024/01/Backyard-Shoez-sneakers-Banner-women-shoes-jpg.webp","black,blue,grey,white size: 36-42",88.32,2),
#     ("Sketchers","https://backyardshoez.co.ke/wp-content/uploads/2023/12/Backyard-Shoez-sneakers21-450x450.webp","black,blue,grey,white size: 36-42",67.34,2)

# ]

# for shoe in shoes:
#     cursor.execute('''
#         INSERT INTO shoe (name,image, description, price, category_id) VALUES (?, ?, ?, ?, ?)
#     ''', shoe)

# conn.commit()
# # conn.close()