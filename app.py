#0 get account_id,token from twilio and set in env
# ----twilio_acc,twilio_token
#1 import client from twilio
#2 initialize client
#3 write a function to process msg from client
#4 write a function to send message to client
#6 generate a response
#7 check response in whatsapp
# TWILIO_ACCOUNT_SID = AC1538f27a7380ca6f24797770163b47c2
# TWILIO_AUTH_TOKEN = 835ddcf5a9873ab91b4d1d5d467e73e5
# Api key = e4a4f96789c854d8690960f5ff1dd666




from flask import Flask
from flask import request
from twilio.rest import Client
import os
from marketstack import get_stock_price
app = Flask(__name__)

acc_id = "AC1538f27a7380ca6f24797770163b47c2"
token = "835ddcf5a9873ab91b4d1d5d467e73e5"
twilio_num = 'whatsapp:+14155238886'


client = Client(acc_id, token)
def send_msg(msg,recipient):
    client.messages.create(
        from_= twilio_num,
        body=msg,
        to=recipient
    )

def process_msg(msg):
    response = ""
    if msg == 'hi':
        response = 'Hello!,Welcome to the Stock Market Bot!'
        response += "Type sym:<stock_symbol> to know the Price Details of the Stock"
    elif 'sym:' in msg:
        data = msg.split(":")
        stock_symbol = data[1]
        stock_price = get_stock_price(stock_symbol)
        price_details = stock_price['Price_Details']
        price_details_str = str(price_details)
        response = "The Price Details of stock " +stock_symbol +" is: [IN Dollors] " +price_details_str 
    else:
        response = "Please type hi to get started."
    return response

@app.route('/webhooks',methods = ['POST'])
def webhooks():
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response,sender)
    return "ok",200



if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)