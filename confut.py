import sqlite3
from time import perf_counter, sleep
import concurrent.futures

def store_movie(film):
    f = open('list.txt','a')
    f.write(film[0] + "\n")
    f.close()
    ### simulate something else on CPU
    sleep(.1)

def main():
    # ensure list is empty
    f = open('list.txt', 'w')
    f.close()

    conn = sqlite3.connect("movies.db")
    db = conn.cursor()


    print("Query: Movies starring Johnny Depp. Results stored in list.txt.")


    db.execute("SELECT movies.title FROM people JOIN stars ON people.id=stars.person_id JOIN movies ON stars.movie_id=movies.id WHERE people.name=?", ("Johnny Depp", ))
    print("Querying database...")
    films = db.fetchall()

    # LINEAR APPROACH
    t1 = perf_counter()

    for film in films:
        f = open('list.txt', 'a')
        f.write(film[0] + "\n")
        f.close()
        ### simulate something else on CPU
        sleep(.1)

    print(f"Linear takes {perf_counter()-t1}")


    f = open('list.txt','w')
    f.close()



    # MULTIPROCESS APPROACH
    t1 = perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(store_movie, films)

    print(f"Concurrent Futures takes {perf_counter() - t1}")


if __name__ == '__main__':
    main()