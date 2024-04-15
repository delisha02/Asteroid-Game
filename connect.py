import mysql.connector as myconn

# Function to connect to the MySQL database
def connect_to_database():
    try:
        return myconn.connect(
            host="localhost",
            user="root",
            password="root",
            database="players"
        )
        #print("Connected to the database successfully.")
    except myconn.Error as e:
        print("Error connecting to the database:", e)
        return None

def read(mydb):
    try:
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        for row in result:
            print(row)
    except myconn.Error as e:
        print("Error reading users:", e)
    finally:
        if mydb.is_connected():
            cursor.close()

mydb = connect_to_database()
read(mydb)

# Function to insert username into the database
def insert_player(mydb, username ,highScore):
    try:
        cursor = mydb.cursor()
        # Check if the user already exists
        cursor.execute("SELECT * FROM users WHERE UserName = %s", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            print("User '{}' already exists in the database.".format(username))
        else:
            cursor.execute("INSERT INTO users (UserName ,highScore) VALUES (%s , %s)", (username ,highScore))
            mydb.commit()
            print("Player '{}' inserted successfully.".format(username))
    except myconn.Error as e:
        print("Error inserting user:", e)
    finally:
        if mydb.is_connected():
            cursor.close()

# Function to get the high score of a user
def get_highScore(mydb ,username):
    try:
        cursor = mydb.cursor()
        cursor.execute("SELECT HighScore FROM users WHERE UserName = %s", (username,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    except myconn.Error as e:
        print("Error fetching high score:", e)

# Function to get the highest score of all the users
def get_highestScore(mydb):
    try:
        cursor = mydb.cursor()
        cursor.execute("SELECT MAX(HighScore) FROM users")
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
    except myconn.Error as e:
        print("Error fetching highest score:", e)

highestScore = get_highestScore(mydb)

# Function to update the high score of a user
def update_highScore(mydb, username, new_high_score):
    try:
        cursor = mydb.cursor()
        old_high_score = get_highScore(mydb ,username)
        if old_high_score is None or new_high_score > old_high_score:
            cursor.execute("UPDATE users SET HighScore = %s WHERE UserName = %s", (new_high_score, username))
            mydb.commit()
            print("High score updated successfully for user '{}'.".format(username))
            return new_high_score
        else:
            print("New high score is not greater than the existing high score for user '{}'.".format(username))
            return old_high_score
    except myconn.Error as e:
        print("Error updating high score:", e)
    finally:
        if mydb.is_connected():
            cursor.close()
'''
def clear_table(mydb, users):
    try:
        cursor = mydb.cursor()
        cursor.execute(f"DELETE FROM {users}")
        mydb.commit()
        print("All records deleted from the table successfully.")
    except myconn.Error as e:
        print("Error clearing table:", e)
    finally:
        if mydb.is_connected():
            cursor.close()
'''
#clear_table(mydb, "users")
# Function to close the database connection
def close_connection(mydb):
    if mydb.is_connected():
        mydb.close()
        print("Database connection closed.")

# Close the database connection
close_connection(mydb)
