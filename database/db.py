import sqlite3

class Database:

    @staticmethod
    def createDb() -> None:
        connection = sqlite3.connect("./database/email_db.db")
        create_table = "CREATE TABLE IF NOT EXISTS EmailDB (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT NOT NULL)"
        connection.execute(create_table)
        connection.commit()
        connection.close()

    @staticmethod
    def emailExists(email: str) -> bool:
        connection = sqlite3.connect("./database/email_db.db")
        cursor = connection.cursor()
        Check ="SELECT * from EmailDB where email=?"
        cursor.execute(Check, (email,))
        response = cursor.fetchone()
        connection.close()
        if response:
            return True
        else:
            return False

    @staticmethod
    def insertEmailInDB(email: str) -> bool:
        # // db query to insert to db
        connection = sqlite3.connect("./database/email_db.db")
        cursor = connection.cursor()
        insert_db ="INSERT INTO EmailDB VALUES (NULL, ?)"
        cursor.execute(insert_db, (email,))
        connection.commit()
        connection.close()

        