import pymysql
import pymysql.cursors

def select_member_info(conn, date):
    with conn.cursor() as cursor:
        sql = '''
            SELECT 
                *
            FROM
                member_info
            WHERE
                right(member_birth, 5) = %s
        '''

        cursor.execute(sql, date)
        member_info = cursor.fetchall()

    return member_info