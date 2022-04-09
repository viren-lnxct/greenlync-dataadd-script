import requests
import json
import csv
import time
    
url = "https://api.getsocial.im/v1/communities/activities"

payload = json.dumps({
"activity": {
    "id": "690780X0R99kG7",
    "content": {
    "language": "en",
    "text": "Memes",
    "attachments": [
        {
        "image": 'file:///home/ubuntu/Memes/1.-2020-weed-meme-2.jpg'
        }
    ]
    },
    "target": {
    "type": "topic",
    "id": "memes"
    }
}
})
headers = {
'X-GetSocial-Access-Token': 'ePXX4Tr9R9W4yJOx5Ll9LwOoVUHtdTbKEQtyly-GBve6MfYe26SaXjOhnXvbwuBzg08EscCn9vUduHuh9Lyk7RVYWPjZUVXbpiUnLqeXwty9nSZMLFn1Tw9gVNR1vveZeEdot4DGrwq55akxuMRCAMWqBh6hltqAywWUNDudXKswE32FYt_F1cJiJyUvlalQII96KjBiQYcdhsjX6rK7Q7EtPsXG5oF5FmnZeTknaWzGqFoFGld387ckfFMoKoJwF4nqhzDWwGoEJwnR8EP8V8E9Z4BNwHBSLdsEvk6WO_aZHxl20G4UwPO0SqKJHJSDEoYNW0fnUfyvW_Ciw7_sv5_GdJyjzSgvsiqZx5s9IexzXUQdj9GybmM3cpgIEEZo71VNCVTEAoBqegqg9j7El2-YLr7l-T9y9-LCWTMVfAE9Ji78oRCK-FeJvNukP-prF1cpY00=',
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
