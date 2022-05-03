# -*- coding: utf-8 -*-

import slack_noti
import inspect

import config

token = config.token
channel = '#일반'


if __name__ == '__main__':
    response = slack_noti.post_message(token,  channel, f'{inspect.getfile(inspect.currentframe())} 실행이 완료 됐습니다.')
    print(response.text)
    print(response.status_code)