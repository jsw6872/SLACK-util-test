from slack_handler import slack_channel_noti, slack_dm_noti

from slack_handler import config as slack_config

import datetime

token = slack_config.token
channel_id = slack_config.channel_id
user_id = slack_config.user_id

def main():
  # TODO:
        # crontab으로 매일 자정 한 번씩 프로그램 실행하면 될 것으로 보임
    try:
        start_day = datetime.datetime(2022, 7, 4)
        today = datetime.datetime.now()

        diff_day = (today - start_day).days


        channel_response = slack_channel_noti.post_message(token,  channel_id, f'[Day {diff_day + 1}] 오늘도 화이팅!')
        print(channel_response.text)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
