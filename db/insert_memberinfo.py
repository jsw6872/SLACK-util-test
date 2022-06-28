import pymysql
import pymysql.cursors

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

