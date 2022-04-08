import requests
import config

token = config.token
channel = '#일반'
# message = f'{inspect.getfile(inspect.currentframe())} 실행이 완료 됐습니다.'

# 채널, 보낼 메시지, 
def post_message(token, channel, message):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": message}
    )
    print(response)

def main(message):
    # message = message
    post_message(token, channel, message)

if __name__ == '__main__':
    main()