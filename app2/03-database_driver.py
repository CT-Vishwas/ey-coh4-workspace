import MySQLdb
import MySQLdb.cursors
from MySQLdb import MySQLError

class UserDatabase:
    def __init__(self, host='localhost', user='root', password='root', database='demodb'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        """Connect to MySQL database"""
        try:
            self.connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.database,
                charset='utf8mb4',
                cursorclass=MySQLdb.cursors.DictCursor,
            )
            self.cursor = self.connection.cursor()
            print(f"Connected to {self.database} database successfully")
        except MySQLError as e:
            print(f"Error while connecting to MySQL: {e}")

    def disconnect(self):
        """Close database connection"""
        if self.connection:
            try:
                if self.cursor:
                    self.cursor.close()
            except Exception:
                pass
            try:
                self.connection.close()
            except Exception:
                pass
            print("Database connection closed")

    def create_user(self, username, emailId, phoneNumber):
        """CREATE: Insert a new user"""
        try:
            query = "INSERT INTO User (username, emailId, phoneNumber) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (username, emailId, phoneNumber))
            self.connection.commit()
            print(f"User '{username}' created successfully")
            return self.cursor.lastrowid
        except MySQLError as e:
            print(f"Error creating user: {e}")
            return None

    def read_user(self, user_id):
        """READ: Fetch a user by ID"""
        try:
            query = "SELECT * FROM User WHERE id = %s"
            self.cursor.execute(query, (user_id,))
            result = self.cursor.fetchone()
            if result:
                print(f"User found: {result}")
                return result
            else:
                print(f"No user found with ID {user_id}")
                return None
        except MySQLError as e:
            print(f"Error reading user: {e}")
            return None

    def read_all_users(self):
        """READ: Fetch all users"""
        try:
            query = "SELECT * FROM User"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            print(f"Total users: {len(results)}")
            for user in results:
                print(user)
            return results
        except MySQLError as e:
            print(f"Error reading users: {e}")
            return None

    def update_user(self, user_id, username=None, emailId=None, phoneNumber=None):
        """UPDATE: Modify user information"""
        try:
            updates = []
            params = []
            if username:
                updates.append("username = %s")
                params.append(username)
            if emailId:
                updates.append("emailId = %s")
                params.append(emailId)
            if phoneNumber:
                updates.append("phoneNumber = %s")
                params.append(phoneNumber)
            
            if not updates:
                print("No fields to update")
                return False
            
            params.append(user_id)
            query = f"UPDATE User SET {', '.join(updates)} WHERE id = %s"
            self.cursor.execute(query, params)
            self.connection.commit()
            print(f"User with ID {user_id} updated successfully")
            return True
        except MySQLError as e:
            print(f"Error updating user: {e}")
            return False

    def delete_user(self, user_id):
        """DELETE: Remove a user"""
        try:
            query = "DELETE FROM User WHERE id = %s"
            self.cursor.execute(query, (user_id,))
            self.connection.commit()
            print(f"User with ID {user_id} deleted successfully")
            return True
        except MySQLError as e:
            print(f"Error deleting user: {e}")
            return False


if __name__ == "__main__":
    db = UserDatabase(host='localhost', user='root', password='root', database='demodb')
    db.connect()
    
    print("\n--- CREATE ---")
    db.create_user('John Doe', 'john@example.com', '1234567890')
    db.create_user('Jane Smith', 'jane@example.com', '0987654321')
    
    print("\n--- READ ALL ---")
    db.read_all_users()
    
    print("\n--- READ BY ID ---")
    db.read_user(1)
    
    print("\n--- UPDATE ---")
    db.update_user(1, username='John Updated', emailId='john.updated@example.com', phoneNumber='5555555555')
    
    print("\n--- READ AFTER UPDATE ---")
    db.read_user(1)
    
    print("\n--- DELETE ---")
    db.delete_user(2)
    
    print("\n--- READ ALL AFTER DELETE ---")
    db.read_all_users()
    
    db.disconnect()
