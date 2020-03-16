import mysql.connector as mysql     # Коннектор для mysql
from mimesis import Person as Pers  # Библиотека генерации фейковых данных


class MySqlConnection:
    """ Initializing object of a class, you create new connection. This one should be stored in variable, if you going
     to use it in future """

    def __init__(self):
        self.db = mysql.connect(host="localhost",  # your host, usually localhost
                                user="admin",    # your username
                                passwd="admin",  # your password
                                db="testDB")     # name of the data base

        #  Создаем экземляр класса  Cursor, с помощью его методов будем работать с запросами и ответами на них
        self.cur = db.cursor()

    # Выбираем нужную БД, эту я создал вручную заранее.
    def create_db(self, db_name):
        """
        Creates
        :param db_name: Создание
        :return:
        """
        self.cur.execute(f"CREATE DATABASE {db_name}")

    def use_db(self, db_name):
        self.cur.execute(f"USE {db_name}")

    def add_rows_to_table(self, *args):

        i = 1
        while i < 10:
            # Наполняем тестовую таблицу Persons значениями
            self.cur.execute(f'INSERT INTO Persons(PersonID, FirstName, SecondName, Description) VALUES({i},'
                    f' "{Pers().first_name()}", "{Pers().last_name()}","{Pers().occupation()}")')
            i += 1
        # Подтверждаем изменения
            self.db.commit()
    # Получаем все строки таблицы Persons
            cur.execute("SELECT * FROM Persons")

    # Выводим все строки
    for row in cur.fetchall():
        print(row)
    # Закрываем подключение
    cur.close()
    db.close()



