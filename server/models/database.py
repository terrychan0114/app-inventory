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
        else:
            logger.info("Successful connection")
    import pymysql.cursors

    def fetch_data(self, query,args):
        if self.connection is not None:
            try:
                with self.connection.cursor() as cur:
                    if args == "":
                        cur.execute(query)
                    else:
                        cur.execute(query,args)
                    db_result = cur.fetchall()
                    result = {}
                    for db_data in db_result:
                        # logger.info(db_data['lot_number'])
                        result[db_data['lot_number']] = db_data
                    return result
            except TypeError:
                logger.error("Unable to fetch data")
                raise