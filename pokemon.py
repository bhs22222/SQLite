'''code to execute sql queries by Tianna Zhang 05/09'''
import sqlite3

DATABASE = 'slnx.sqlite'

def print_all_pokemons():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT Name, Speed FROM pokemon;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #Print them nicely

        for pokemon in results:
            print(f"pokemon: {pokemon[0]} Speed : {pokemon[1]}")


if __name__ == "__main__":
    print_all_pokemons()