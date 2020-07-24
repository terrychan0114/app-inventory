import pymysql.cursors
import datetime
from loguru import logger
from server.models.database import Database

def run_query(connection,query):
    try:
        with connection.cursor() as cur:
            
