from requests import post

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
