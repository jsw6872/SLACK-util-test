import logging
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import slack_handler.config as config

logger = logging.getLogger()
client = WebClient(token=config.token)
channel_id = config.channel_id

result_cvs = client.conversations_members(channel=channel_id)  # USER ID 가져오기

print(result_cvs['members'])