from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import requests
from template import msg_template
import configparser
import time


while True:


    config = configparser.ConfigParser()
    config.read('config.ini')

    # Initialize a Slack WebClient
    client = WebClient(token=config['SLACK']['SLACK_OAUTH_TOKEN'])

    # Define the channel ID where you want to send the message
    channel_id = config['SLACK']['CHANNEL_ID']

    try:
        url = "https://gold-rates-india.p.rapidapi.com/api/gold-rates"

        headers = {
            "X-RapidAPI-Key": config['RapidAPI']['RAPID_API_KEY'],
            "X-RapidAPI-Host": "gold-rates-india.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        arr = response.json()['GoldRate']
        out_arr = []
        cities = ['Pune','Jalgaon']

        for i in arr:
            if i['city'] in cities:
                print(i)
                out_arr.append(i)
                
        # Send a message to the specified channel
        for data in out_arr:
            #msg = "Gold Rate in {cityname} \n Ten Grams 22 Carat : {carat22} \n Ten Grams 24 Carat : {carat24}".format(cityname = data['city'], carat22 = data['TenGram22K'], carat24 = data['TenGram24K'])
            
            response = client.chat_postMessage(channel=channel_id, blocks=msg_template(cityname = data['city'], carat22 = data['TenGram22K'], carat24 = data['TenGram24K']))
            print("Message sent successfully:", response["ts"])
    except SlackApiError as e:
        print("Error sending message:", e)
    time.sleep(3600)


