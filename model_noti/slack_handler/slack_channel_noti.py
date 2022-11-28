import requests

# 채널, 보낼 메시지, 
def post_message(token, channel_id, message):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel_id,"text": message}
    )
    return response

# 사진 이미지 보내기
def post_file(token, channel_id, title, file):
    response = requests.post("https://slack.com/api/files.upload",
    headers={"Authorization": "Bearer "+token},
    data={"channels": channel_id,'title': title, "content": file}
    )
    return response
