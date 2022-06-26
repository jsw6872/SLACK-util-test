from db import insert_memberinfo, select_member_info
from slack_handler import slack_channel_noti, slack_dm_noti_test

import config

def main():
    try:
        # TODO:
        # 날짜 검색해서 sql 조회 후 메시지화
          # date 받을 때 전처리
        # insert 어떻게 할 것인지
        # daemon으로 돌릴 시에 while문으로 조회해야하는지, 한번만 출력이 가능하도록, 같은 생일자가 있을 때 어떻게 처리할 것인지
        pass
    except Exception as e:
        print(e)
