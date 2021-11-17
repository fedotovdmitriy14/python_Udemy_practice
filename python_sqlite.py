import csv
import sqlite3


con = sqlite3.connect('../db.sqlite')
cur = con.cursor()



def actors():
        actor_list = []
        for row in cur.execute('SELECT * FROM actors'):
                actor_list.append(row)


        with open('./actors.csv', 'a', newline="", encoding='UTF-8') as f:
                sc = csv.writer(f)
                sc.writerows(actor_list)

        # cur.copy_from('./actors.csv', 'data_actor', sep=',')







def writers():
        writer_list = []
        for row in cur.execute('SELECT * FROM writers'):
                writer_list.append(row)

        with open('./writers.csv', 'a', newline="", encoding='UTF-8') as f:
                sc = csv.writer(f)
                sc.writerows(writer_list)


def movies():
        movies_list = []
        for row in cur.execute('SELECT * FROM movies'):
                movies_list.append(row)

        with open('./movies.csv', 'a', newline="", encoding='UTF-8') as f:
                sc = csv.writer(f)
                sc.writerows(movies_list)


actors()
writers()
movies()