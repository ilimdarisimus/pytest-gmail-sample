from api.lib.mysql_db_connection import MySqlConnection as DB
from mimesis import Food as Foo


class TestMysqlSampleDb:

    def test_db(self):
        random_name = Foo().drink()
        db = DB()
        db.create_db(random_name)
        db.use_db(random_name)
        db.create_table('New_Table', ['id int(5)', 'var varchar(21)'])
        db.close_all_connections()


