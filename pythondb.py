import psycopg2


def db_connection():
    try:
        connection = psycopg2.connect(
            dbname="dictdb",
            user="postgres",
            password="AWAD12",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as error:
        print(f"Error: {error}")
        return None


def list_translations(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT english_word, local_translation FROM translations")
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row[0]} -> {row[1]}")
        cursor.close()
    except Exception as error:
        print(f"Error: {error}")


def add_translation(connection, english_word, local_translation):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO translations (english_word, local_translation) VALUES (%s, %s)",
                       (english_word, local_translation))
        connection.commit()
        cursor.close()
        print(f"Added translation: {english_word} -> {local_translation}")
    except Exception as error:
        print(f"Error: {error}")


def delete_translation(connection, english_word):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM translations WHERE english_word = %s", (english_word,))
        connection.commit()
        cursor.close()
        print(f"Deleted translation: {english_word}")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    connection = db_connection()
    if connection is not None:
        print("Connected to the database successfully")
        while True:
            cmd = input(
                "Enter command (list, add, delete, quit): ").strip().lower()
            if cmd == "list":
                list_translations(connection)
            elif cmd == "add":
                english_word = input("Enter English word: ").strip()
                local_translation = input("Enter local translation: ").strip()
                add_translation(connection, english_word, local_translation)
            elif cmd == "delete":
                english_word = input("Enter English word to delete: ").strip()
                delete_translation(connection, english_word)
            elif cmd == "quit":
                break
            else:
                print(
                    "Unknown command. Please enter 'list', 'add', 'delete', or 'quit'.")
        connection.close()
    else:
        print("Failed to connect to the database")
