
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance.connect()
        return cls._instance

    def connect(self):
        engine = create_engine('URI')
        self.Session = sessionmaker(bind=engine)

    def get_session(self):
        return self.Session()
