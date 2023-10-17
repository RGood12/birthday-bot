from requests import post
from bd.secrets import *

# function to send (text) message to the group me
def send_message(msg, bot_id):
    data = {
        'bot_id' : bot_id,
        'text'   : msg,
    }
    post('https://api.groupme.com/v3/bots/post', json=data)

# function to send message w/ pic attachment to the groupme
def send_picture(msg, bot_id, pic_url):
    data = {
        'bot_id'      : bot_id,
        'text'        : msg,
        'attachments' : [
          {
              'type'  : 'image',
              'url'   : pic_url,
          }
        ]
    }
    post('https://api.groupme.com/v3/bots/post', json=data)

def send_message_mention(msg, bot_id, gmID, name_len):
    message = {
        "bot_id": bot_id,
        "text": msg,
        "attachments": [
            {
        "type": "mentions",
        "user_ids": [f"""{gmID}"""],
        "loci": [
            [0, name_len]
                ]
            }
        ]
    }
    post('https://api.groupme.com/v3/bots/post', json=message)

def combined(msg, bot_id, gmID, name_len, pic_url):
    data = { 
        'bot_id'      : bot_id,
        'text'        : msg,
        'attachments' : [ 
          {   
              'type'  : 'image',
              'url'   : pic_url,
          },   
          {   
        "type": "mentions",
        "user_ids": [f"""{gmID}"""],
        "loci": [
            [0, name_len]
                ]   
            }   

        ]   
    }   
    post('https://api.groupme.com/v3/bots/post', json=data)

def gm_image_service(pic):

    data = open(pic, 'rb').read()
    res = post(url='https://image.groupme.com/pictures',
                    data=data,
                    headers={'Content-Type': 'image/jpeg',
                             'X-Access-Token': access_token})
    res = res.content

    # Convert bytes data to a string
    data_str = res.decode('utf-8')

    # Find the index of 'picture_url'
    start_index = data_str.find('"picture_url":"') + len('"picture_url":"')
    end_index = data_str.find('"', start_index)

    # Extract 'picture_url' value
    pic_url = data_str[start_index:end_index]
    return pic_url
