import mysql.connector as mysql  # Коннектор для mysql
from mimesis import Person as Pers  # Библиотека генерации фейковых данных


class MySqlConnection:

    def __init__(self):
        self.db = mysql.connect(host="localhost",  # your host, usually localhost
                                user="admin",  # your username
                                passwd="admin",  # your password
                                db="testDB")  # name of the data base

        #  Создаем экземляр класса  Cursor, с помощью его методов будем работать с запросами и ответами на них
        self.cur = self.db.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Закрывает все подключения """
        self.cur.close()
        self.db.close()

    # Выбираем нужную БД, эту я создал вручную заранее.
    def create_db(self, db_name):
        """
        Creates
        :param db_name: Создание бд
        :return:
        """
        self.cur.execute(f"CREATE DATABASE {db_name};")

    def use_db(self, db_name):
        """ Выбирает используемую бд"""
        self.cur.execute(f"USE {db_name};")

    def add_rows_to_table(self, *args):
        i = 1
        while i < 10:
            # Наполняем тестовую таблицу Persons значениями
            self.cur.execute(f'INSERT INTO Persons(PersonID, FirstName, SecondName, Description) VALUES({i},'
                             f'{Pers().first_name()}", "{Pers().last_name()}","{Pers().occupation()}')
            # Подтверждаем изменения
            self.db.commit()

    def get_table_rows(self, table):
        "Возвращает все строки таблицы"
        self.cur.execute(f"SELECT * FROM {table}")

    def create_table(self, table_name, column):
        """

        :param table_name: имя таблицы
        :param column: принимает список имен столбцов, например - ['id int(5)', 'firstname varchar(20)']
        :return:
        """
        query = f"CREATE TABLE '{table_name}'" + ', '.join(column)
        print(query)
        self.cur.execute(query+';')

    # Закрываем подключение
    def close_all_connections(self):
        self.cur.close()
        self.db.close()