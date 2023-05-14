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
SLACK_BOT_TOKEN = "xoxb-5256167969204-5262487236836-PPa5PyQ5FzqBwGqKFGDfA8oW"
SLACK_APP_TOKEN = "xapp-1-A057K1BGQ05-5260162177731-895d20c7d5c7cf2758edc8cfac29c0719b292dcf0bff47dac98e8b21457b7f24"
SLACK_SIGNING_SECRET = "65a47903b065eccdf296e029e3bbb079"


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
