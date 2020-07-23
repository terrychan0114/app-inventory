import pymysql.cursors
import datetime
from loguru import logger

class Database:
    def __init__(self, host, user,password,db,charset="utf8mb4"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.connection = None

    def open_connection(self):
        
        try:
            if self.connection is None:
               self.connection = pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             db=self.db,
                             charset=self.charset,
                             cursorclass=pymysql.cursors.DictCursor)
        except pymysql.MySQLError as e:
            logger.error(e)
            raise
        else:
            logger.info("Successful connection")