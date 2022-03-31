from flask import Flask, request, redirect
from flask import jsonify
from waitress import serve
from bd.secrets import port, bot_id
from bd.groupme import send_message
from bd.calculations import all_bdays
from bd.responses import bb1_response, bb2_response, bb3_response
import requests, re

app = Flask(__name__)


@app.route('/short', methods=['GET'])
def shortener():
    return redirect("http://www.google.com")


@app.route('/bdaybot', methods=['POST'])
def bot_response():
    data = request.get_json()
    data = {k.lower(): v for k, v in data.items()}
    
    if data['name'] != 'Birthday Bot':
        
        if re.match(r"^@(birthdaybot|bb) (menu|help)", data['text']):
            send_message("MENU\n------\n\
[1.] Type \"@bb 1\" or \"@bb next birthday\" for the next buddy birthday\n\
[2.] Type \"@bb 2\" or \"@bb birthdays this month\" to list any buddy birthdays this month\n\
[3.] Type \"@bb 3 [month]\" or \"@bb birthdays in [month]\" to list all buddy birthdays in the given month\n\
[4.] Type \"@bb 4\" or \"@bb all birthdays\" to list all buddy birthdays", bot_id)
            
        if re.match(r"@bb (1|next birthday)", data['text']):
            bb1_response()
        if re.match(r"@bb (2|birthdays this month)", data['text']):
            bb2_response()
        if re.match(r"@bb 3 *", data['text']):
            try:
                bb3_response(str(data['text']))
            except:
                send_message("Hmm, I didn't quite catch the month. Be sure to type the month name, not month digit.", bot_id)
        if re.match(r"@bb birthdays in *", data['text']):
            try:
                bb3_response(str(data['text']))
            except:
                send_message("Hmm, I didn't quite catch the month. Be sure to type the month name, not month digit.", bot_id)
        if re.match(r"@bb (4|all birthdays)", data['text']):
            send_message(all_bdays(), bot_id)

    return "1"

if __name__ == '__main__':
    # you sould put the port in a config file
    serve(app, host='0.0.0.0', port = port)
