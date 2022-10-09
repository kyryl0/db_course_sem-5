import sqlite3
from client_class import Client

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE clients (
            first text,
            last text,
            address text
            )""")


def insert_cli(cli):
    with conn:
        c.execute("INSERT INTO clients VALUES (:first, :last, :address)",
                  {'first': cli.first, 'last': cli.last, 'address': cli.address})


def get_clis_by_name(lastname):
    c.execute("SELECT * FROM clients WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_address(cli, address):
    with conn:
        c.execute("""UPDATE clients SET address = :address
                    WHERE first = :first AND last = :last""",
                  {'first': cli.first, 'last': cli.last, 'address': address})


def remove_cli(cli):
    with conn:
        c.execute("DELETE from clients WHERE first = :first AND last = :last",
                  {'first': cli.first, 'last': cli.last})


cli_1 = Client('Dima', 'Jones', '123 Main St, Houston, TX')
cli_2 = Client('Alex', 'Salzer', '125 Santa Claus Rd, Anchorage, AK')
cli_3 = Client('Nate', 'Salzer', '128 Mary Ln, Los Angeles, CA')
cli_4 = Client('Irina', 'Molnar', '132 St, New York City, NY')
cli_5 = Client('Ky', 'Newman', "127 Hollywood Ln, Sacramento, CA")

insert_cli(cli_1)
insert_cli(cli_2)
insert_cli(cli_3)
insert_cli(cli_4)
insert_cli(cli_5)

clis = get_clis_by_name('Molnar')
print(clis)

update_address(cli_2, '30004 Santa Claus Rd, Anchorage, AK')
remove_cli(cli_1)

clis = get_clis_by_name('Salzer')
print(clis)

conn.close()
