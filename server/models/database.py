import pymysql.cursors
import datetime

class Database:
    def __init__(self, host, user,password,db,charset="utf8mb4"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset

    def connect(self):
        self.connection = pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             db=self.db,
                             charset=self.charset,
                             cursorclass=pymysql.cursors.DictCursor)
    
    # def insert(self,)