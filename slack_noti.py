import requests
# message = f'{inspect.getfile(inspect.currentframe())} 실행이 완료 됐습니다.'

# 채널, 보낼 메시지, 
def post_message(token, channel, message):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": message}
    )
    return response