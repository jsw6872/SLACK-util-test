from db import insert_member_info, select_member_info, db_connector
from slack_handler import slack_channel_noti, slack_dm_noti

from slack_handler import config as slack_config

import datetime

# channel = '#일반'
token = slack_config.token
channel_id = slack_config.channel_id
user_id = slack_config.user_id

def main():
  # TODO:
        # daemon으로 돌릴 시에 while문으로 조회해야하는지, 한번만 출력이 가능하도록, 같은 생일자가 있을 때 어떻게 처리할 것인지
    try:
        conn = db_connector.db_connecter()
        
        now = datetime.datetime.now()
        birth_date = f"{now.strftime('%m')}-{now.day}"
        birth_member_list = select_member_info.select_member_info(conn, birth_date)
        
        if len(birth_member_list) != 0:
            for birth_member_info in birth_member_list:
                birth_member_name = birth_member_info['member_name']
                birth_member_token = birth_member_info['member_id']
                channel_response = slack_channel_noti.post_message(token,  channel_id, f'{birth_member_name}님의 생일입니다. 다들 축하해주세요!!')
                # dm_response = slack_dm_noti.post_message(birth_member_token,  user_id, 'test sentence')

        print(channel_response.text)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()