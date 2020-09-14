import sqlite3

connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")



def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries (content, date) VALUES (?, ?);", (entry_content, entry_date)
        )


def get_entries():
    # cursor = connection.cursor()
    # cursor.execure("SELECT * FROM entries;")

    # SHORT FORM FOR ^^^
    cursor = connection.execute("SELECT * FROM entries;")
    return cursor