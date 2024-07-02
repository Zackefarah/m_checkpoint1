import psycopg2


def db_connection():
    return psycopg2.connect(
        host="localhost"
    )


def read_dict():
    dbconn = db_connection()
    cur = dbconn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    dbconn.close()
    return rows


while True:  # REPL - Read Execute Program Loop
    cmd = input("Command: ")

    if cmd == "list":

    elif cmd == "quit":
        exit()
    else:
        print("error")
