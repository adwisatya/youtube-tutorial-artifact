import json
import urllib.request
import urllib.parse

def lambda_handler(event, context):
    chat_id = ""
    telegram_token = ""
    print(event['body'])
    def get_url_urllib(url,chat_id,text):
        with urllib.request.urlopen(url+"?chat_id="+str(chat_id)+"&text="+urllib.parse.quote_plus(text)) as response:
            return response.read()
    response = get_url_urllib("https://api.telegram.org/bot"+telegram_token+"/sendMessage",chat_id,"New "+json.loads(event['body'])['event_type']+" coming, please check:"+json.loads(event['body'])['repository']['homepage'])
    return {
        'statusCode': 200,
        'body': "ok"
    }
