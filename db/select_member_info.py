import pymysql
import pymysql.cursors

import config

DB_ADDRESS = config.DB_ADDRESS
DB_USER = config.DB_USER
DB_PASSWORD = config.DB_PASSWORD

def db_connecter():
  conn = pymysql.connect(host=DB_ADDRESS, port=3306, user=DB_USER,password=DB_PASSWORD, 
                         db='birh_noti_test', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
  return conn

def select_member_info(conn, date):
    with conn.cursor() as cursor:
        sql = '''
            SELECT 
                *
            FROM
                member_info
            WHERE
                member_birth = %s
        '''

        cursor.execute(sql, date)
        member_info = cursor.fetchall()

    return member_info