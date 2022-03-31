import requests
import json
import csv
import time

with open('csv/delivery_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    headings = next(csv_reader)

    for data in csv_reader:
        print(len(data))
        url = "https://api.getsocial.im/v1/communities/activities"

        payload = json.dumps({
        "activity": {
            "id": "690780X0R99kG7",
            "content": {
            "language": "en",
            "text": "Created with script",
            "attachments": [
                {
                "image": data[16]
                }
            ]
            },
            "properties": {
            "first_name": data[0],
            "last_name": data[1],
            "business_name":data[2],
            "title":data[3],
            "about": data[4],
            "license_state": data[5],
            "license_number": data[6],
            "address": data[7],
            "city": data[8],
            "state": data[9],
            "postal_code": data[10],
            "phone_number": data[11],
            "email": data[12],
            "website": data[13],
            "longitude": data[14],
            "latitude": data[15]
            },
            "target": {
            "type": "topic",
            "id": "delivery"
            }
        }
        })
        headers = {
        'X-GetSocial-Access-Token': 'Od1IaxmUB0_LvBjUKCDZ3-e2KVLIPFB_lQuTg3WdB5jldQLQrhfCmOs8bG-xfeYLpkO8JIIU4Z10I-vljLR5IoAgSDCGzZfvXhHrZ9O32u1WO3iRWNcJGCgzQ1u-cFGKuMTTEn-S6KPBRx1v_rganDwW4CwblY_bPrvoBQNzP9XeUzRhVSszHjiohPw-UGubeB_Smp4Ci4xSwOQnI0SK_64ZT1xTRDznhQ7akKKj4IDgem5yY_e-BzzVAH9_d8zWuayCdZ6iaBOWb7AjwjCC15Yh4zaZc-3J3zJ2VIh0CkTc0_ucYiNwge8j6aY-djHp6UPFwED81fofJNo2wGEnuoVDdCWLrC3yzubvwDPFu4n4cSqVuSygYobeljfVy4V7ehFj1nKvGTyYDTmQc7f9pCZmHtIAdb82aTUV4UqoZb0jSnR9pETYSTs=',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        time.sleep(5)
