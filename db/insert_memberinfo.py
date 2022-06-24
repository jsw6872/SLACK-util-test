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

def insert_member_info(conn):
    cursor = conn.cursor()
    sql = '''
        INSERT INTO member_info(member_id, member_name, member_birth)
            values (%s, %s, %s);
    '''
    member_id = input("member_id를 입력해주세요 : ")
    member_name = input("이름을 입력해주세요 : ")
    member_birth = input("생년월일을 입력해주세요 (ex: 1999-06-23) : ")

    cursor.execute(sql, (member_id, member_name, member_birth))
    
    conn.commit()

    conn.close()

