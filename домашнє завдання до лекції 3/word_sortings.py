import sqlite3
from words_classes import Words

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE words (
            word_id,
            word,
            structure,
            part_of_speech
            )""")


def insert_word(wor):
    with conn:
        c.execute("INSERT INTO words VALUES (:id, :word, :struct, :pos)",
                  {'id': wor.id, 'word': wor.word, 'struct': wor.struct, 'pos': wor.pos})


def sort_words_by_id_desc():
    c.execute("SELECT * FROM words ORDER BY word_id DESC")
    return c.fetchall()

def get_words_by_pos(pos):
    c.execute("SELECT * FROM words WHERE part_of_speech=:part_of_speech", {'part_of_speech': pos})
    return c.fetchall()

def get_words_by_struct(a, b):
    c.execute("SELECT * FROM words WHERE structure=:structure AND part_of_speech=:part_of_speech", {'structure': a, 'part_of_speech': b})
    return c.fetchall()

wor_1 = Words('1', 'стіл', 'R0F4', 'іменник')
wor_2 = Words('2', 'столик', 'R0S4F6', 'іменник')
wor_3 = Words('3', 'мати', 'R0F3', 'іменник')
wor_4 = Words('4', 'мати', 'R0F3', 'дієслово')



insert_word(wor_1)
insert_word(wor_2)
insert_word(wor_3)
insert_word(wor_4)


print("Відсортовані за спаданням id:\n" + str(sort_words_by_id_desc()))
print("Усі дієслова з таблиці words:\n" + str(get_words_by_pos('дієслово')))
print("Слова зі структурою R0S4F6 та POS іменник:\n" + str(get_words_by_struct('R0S4F6', 'іменник')))


conn.close()
