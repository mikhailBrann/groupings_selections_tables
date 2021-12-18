import sqlalchemy

class WorkDb:
    def __init__(self,user_db,password, db_name):
        self.user_db = user_db
        self.password = password
        self.db_name = db_name
        self.engine = sqlalchemy.create_engine(f'postgresql://{self.user_db}:{self.password}@localhost:5432/{self.db_name}')

    def connection(self):
        return self.engine.connect()


music_shop = WorkDb('postgres', '1488', 'music_store_db')