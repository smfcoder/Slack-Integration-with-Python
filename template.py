import json

def msg_template(cityname,carat22,carat24):
    print(cityname,carat22,carat24)
    blocks = [ 
                {
                    "type": "image",
                    "title": {
                        "type": "plain_text",
                        "text": "Gold",
                        "emoji": True
                    },
                    "image_url": "https://img.etimg.com/thumb/width-1200,height-900,imgsize-1305151,resizemode-75,msid-109452169/wealth/invest/gold-prices-today-gold-jewellery-rates-of-tanishq-malabar-gold-joyalukkas-kalyan-jewellers.jpg",
                    "alt_text": "gold_img"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "You have a new update:\n*Gold Rate Today - {city}*".format(city=cityname.upper())
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": "24 Carat (10 grams) :{carat_24}".format(carat_24=carat24)
                        },
                        {
                            "type": "mrkdwn",
                            "text": "22 Carat (10 grams) :{carat_22}".format(carat_22=carat22)
                        }
                    ]
                }
            ]

    return(json.dumps(blocks))
