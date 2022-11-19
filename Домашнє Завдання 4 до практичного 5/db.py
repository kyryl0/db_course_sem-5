import preprocessing
import sqlite3
conn = sqlite3.connect('words.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS words (
            word_id integer primary key,
            pos_type text,
            word text)
        """)

c.execute("""CREATE TABLE IF NOT EXISTS pos (
            pos_type text)
        """)
c.execute("""CREATE TABLE IF NOT EXISTS inflections (
            word_id integer,
            inflected_form text,
            FOREIGN KEY (word_id) REFERENCES words (word_id))
        """)
conn.commit()

pos = set([v[0] for v in preprocessing.words.values() if v[0] is not None])
for i in pos:
     c.execute("INSERT INTO pos VALUES (?)", (i,))
     conn. commit()

pos = set([v[0] for v in preprocessing.words.values() if v[0] is not None])
for i in pos:
    c.execute("INSERT INTO pos VALUES (?)", (i,))
    conn. commit()

i = 1
for k, v in preprocessing.words.items():
    c.execute("INSERT INTO words VALUES (?, ?, ?)", (i, v[0], k))
    for inf in v[1]:
        c.execute("INSERT INTO inflections VALUES (?, ?)", (i, inf))
        i +=1
        conn.commit()
