import json
import urllib.request
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.config import Config

from slack_sdk import WebClient
from slack_bolt import App

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

channel_id = "C057MRN3H0B"
SLACK_BOT_TOKEN = 
SLACK_APP_TOKEN =
SLACK_SIGNING_SECRET = 


app = App(
    # signing_secret = SLACK_SIGNING_SECRET
    token = SLACK_BOT_TOKEN
)

slack_client = WebClient(token = SLACK_BOT_TOKEN)

def post_slack(argStr):
    message = argStr
    send_data = {
        "text": message,
    }
    send_text = json.dumps(send_data)
    request = urllib.request.Request(
        "https://hooks.slack.com/services/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",
        data=send_text.encode('utf-8'),
    )

    with urllib.request.urlopen(request) as response:
        slack_message = response.read()

@app.event("message")
if ~~:
def regex(event_data, message, say):
    user = message["user"]
    text = message["text"]
    say(f"Hi <@{user}>! You said: {text}")
    print(f"{user}: {text}")
    dynamodb = boto3.resource('dynamodb')
    
    # select the table
    table = dynamodb.Table("scholarship")

    # get item from database
    query = {"FilterExpression": Attr('info').contains(message["text"])}
    response = table.scan(**query)
    post_slack(str(response['Items']))
    
    return message["text"]

if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
