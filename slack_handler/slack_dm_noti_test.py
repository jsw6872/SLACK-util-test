import requests

# 채널, 보낼 메시지, 
def post_message(token, user_id, message):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": user_id,"text": message}
    )
    return response