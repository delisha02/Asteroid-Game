import mysql.connector as myconn

# Function to connect to the MySQL database
def connect_to_database():
    try:
        mydb = myconn.connect(
            host="localhost",
            user="root",
            password="root",
            database="players"
        )
        print("Connected to the database successfully.")
        return mydb
    except myconn.Error as e:
        print("Error connecting to the database:", e)
        return None



# Function to insert username and high score into the database
def insert_player_score(mydb, username, highscore):
    try:
        cursor = mydb.cursor()
        sql = "INSERT INTO users (UserName, HighScore) VALUES (%s, %s)"
        val = (username, highscore)
        cursor.execute(sql, val)
        mydb.commit()
        print("Player score inserted successfully.")
    except myconn.Error as e:
        print("Error inserting users:", e)
    finally:
        if mydb.is_connected():
            cursor.close()

# Function to close the database connection
def close_connection(mydb):
    if mydb.is_connected():
        mydb.close()
        print("Database connection closed.")
