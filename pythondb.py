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
            "SELECT id, english_word, local_translation FROM translations")
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row[0]}: {row[1]} -> {row[2]}")
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


def add_word(connection):
    english_word = input("Enter English word: ").strip()
    local_translation = input("Enter local translation: ").strip()
    add_translation(connection, english_word, local_translation)


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
                add_word(connection)
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


'''Task 1.9: Comment on an alternative solution for the ITEMS table:
-- An alternative design for the ITEMS table could involve normalizing the contact details further.
-- For instance, instead of storing contact details directly in the ITEMS table, we could create a separate
-- table for each contact type(e.g., EMAIL_CONTACTS, PHONE_CONTACTS) and store references to these tables.
-- This approach would reduce redundancy and improve data integrity by ensuring each contact detail is stored
-- in a table specific to its type. Example SQL for such a design:

-- CREATE TABLE EMAIL_CONTACTS(
    -- id SERIAL PRIMARY KEY,
    -- email VARCHAR(100)
    - -)

--CREATE TABLE PHONE_CONTACTS(
    -- id SERIAL PRIMARY KEY,
    -- phone_number VARCHAR(20)
    - -)

-- CREATE TABLE ITEMS(
    -- id SERIAL PRIMARY KEY,
    -- contact_id INT,
    -- contact_type_id INT,
    -- contact_category_id INT,
    -- email_contact_id INT,
    -- phone_contact_id INT,
    -- FOREIGN KEY(contact_id) REFERENCES CONTACTS(id),
    -- FOREIGN KEY(contact_type_id) REFERENCES CONTACT_TYPES(id),
    -- FOREIGN KEY(contact_category_id) REFERENCES CONTACT_CATEGORIES(id),
    -- FOREIGN KEY(email_contact_id) REFERENCES EMAIL_CONTACTS(id),
    -- FOREIGN KEY(phone_contact_id) REFERENCES PHONE_CONTACTS(id)
    - -)

-- In this alternative design, the ITEMS table contains references to the appropriate contact type tables.
-- This allows for more detailed and structured storage of contact information '''
