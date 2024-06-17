from db import cursor,conn

class User:
    TABLE_NAME = "users"

    def __init__(self,name,phone,email,password):
        self.id = None
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        pass

    def save(self):
        sql = f"""
           INSERT INTO {self.TABLE_NAME} (name,phone,email,password)
           VALUES (?,?,?,?)
        """
        cursor.execute(sql,(self.name,self.phone,self.email,self.password))
        conn.commit()
        self.id = cursor.lastrowid

        return self
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "password": self.password
        }
    
    @classmethod
    def find_user_by_email(cls,email):
        sql = """
            SELECT * FROM {cls.TABLE_NAME}
            WHERE email = ?
        """

        row = cursor.execute(sql,(email)).fetchone()
        return cls.row_to_instance(row)


    @classmethod
    def row_to_instance(cls,row):
        if row == None:
            return None
        user = cls(row[1],row[2],row[3],row[4])
        user.id = row[0]
        return user


    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               phone TEXT NOT NULL UNIQUE,
               email TEXT NOT NULL UNIQUE,
               password VARCHAR NOT NULL
            
            )
        """
        cursor.execute(sql)
        conn.commit()
        print("Users table created")


User.create_table()