from slack_handler import slack_channel_noti, slack_dm_noti

from slack_handler import config as slack_config

import datetime

token = slack_config.token
channel_id = slack_config.channel_id
user_id = slack_config.user_id
user_token = slack_config.user_token
def main():
    try:


        channel_response = slack_channel_noti.post_message(token,  channel_id, '학습 끝')
        print(channel_response.text)
        with open('val_plot.png', 'rb') as f:
            content = f.read()
            print(f.name)
            channel_img = slack_channel_noti.post_file(user_token, channel_id, f.name, content)
            print(channel_img.text)
        
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
