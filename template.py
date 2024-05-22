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
                    "image_url": "https://images.unsplash.com/photo-1610375461246-83df859d849d?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                    "alt_text": "gold_img"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "You have a new update:\n*Gold Rate Today : {city}*".format(city=cityname.upper())
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
