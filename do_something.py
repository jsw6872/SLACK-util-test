# -*- coding: utf-8 -*-

import slack_channel_noti
import slack_dm_noti_test
import inspect

import config

token = config.token
channel = '#일반'
user_id = config.user_id


if __name__ == '__main__':
    channel_response = slack_channel_noti.post_message(token,  channel, f'{inspect.getfile(inspect.currentframe())} 실행이 완료 됐습니다.')
    dm_response = slack_dm_noti_test.post_message(token,  user_id, f'{inspect.getfile(inspect.currentframe())} 실행이 완료 됐습니다.')
    print(channel_response.text)
    print(channel_response.status_code)