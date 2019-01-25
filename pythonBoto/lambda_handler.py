import boto3
import json
client=boto3.client("lambda")

payload={
        "key1":"value1",
        "key2":"va;ue2"
        }
payload=json.dumps(payload)
response=client.invoke(FunctionName="firstlambda",InvocationType="Event",Payload=payload)
print(response)

def lambda_handler(event,context):
	print("hello")
	## uncomment the following lines to send message in a stand alone case
	## if the send message is called from another class or method, don't uncomment them
	token="xoxp"
	recipient="@nath.dwarak89"
	#recipient="dwarak.dnr"
	msg="@nath.dwarak89 Hello from lamda using windows os"
	send_message(token,recipient,msg)


## imports starts here
from slackclient import SlackClient
# imports ends here

## send_message method sends message based on the input params
def send_message(token,recipient,msg):
    try:
        sc = SlackClient(token)
        sc.api_call(
            "chat.postMessage",
            channel=recipient,
            text=msg,
            username="nath.dwarak89"
        )
        print("successful")
    except:
        print("not successful")
    finally:
        print("executed")






