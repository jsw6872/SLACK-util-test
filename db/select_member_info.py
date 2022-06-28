import pymysql
import pymysql.cursors

import config

DB_ADDRESS = config.DB_ADDRESS
DB_USER = config.DB_USER
DB_PASSWORD = config.DB_PASSWORD

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