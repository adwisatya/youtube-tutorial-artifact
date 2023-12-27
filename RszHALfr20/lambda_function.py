import json
from botocore.vendored import requests
import urllib.request
import os

def lambda_handler(event, context):
    # TODO implement
    def send_reply(chat_id,content):
        try:
            response = requests.get("https://api.telegram.org/bot"+os.environ['BOT_KEY']+"/sendmessage?chat_id="+str(chat_id)+"&text="+content)
        except Exception as e:
            pass
    try:
        raw_data = json.loads(event['body'])
    except Exception as e:
        print(e)
        return {
            'statusCode': 200,
            'body': "no message"
        }        
    try:
        index = raw_data['message']
        index = "message"
    except Exception as e:
        print(e)
        index = "my_chat_member"
    try:
        chat_id = raw_data[index]['chat']['id']
    except Exception as e:
        print(e)
        return {
            'statusCode': 200,
            'body': "no message"
        }
    try:
        username = raw_data[index]['chat']['username']
    except Exception as e:
        print(e)
        username = raw_data[index]['new_chat_member']['user']['username']
    try:
        message = raw_data[index]['text'].strip()
    except Exception as e:
        print(e)
        return {
            'statusCode': 200,
            'body': "no message"
        }
    if "/start" in message and len(message) < 20:
        content = "Selamat datang di bot TanyaChatGPT \n\nBot ini akan membantu anda dalam bertanya ke ChatGPT langsung dari telegram."
        send_reply(chat_id,content)
        return {
            'statusCode': 200,
            'body': "ok"
        }
    else:
        pass
    try:
        response = requests.post('https://chatgpt.aryya.id/api/chat/completions', json={
            "model": "gpt-3.5-turbo",
            "messages":[
                {"role":"system","content":message}
            ],
            "temperature":0.7
        },headers={
            "Content-Type":"application/json",
            "Authorization": "Bearer "+ os.environ['CHATGPT_ARYYA_KEY']
        })
        message = response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(e)
        pass
    content = urllib.request.quote(message)
    send_reply(chat_id,content)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

