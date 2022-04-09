import requests
import json
import csv
import time
record = 1
with open('csv2/weedmaps_brands_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    headings = next(csv_reader)

    for data in csv_reader:
        count = 0
        for d_value in data:
            if d_value == '':
                data[count] = "NULL"
            count += 1
        url = "https://api.getsocial.im/v1/communities/activities"

        payload = json.dumps({
        "activity": {
            "id": "690780X0R99kG7",
            "content": {
            "language": "en",
            "text": "Brand",
            "attachments": [
                {
                "image": data[5]
                }
            ]
            },
            "properties": {
            "brand_id": data[0],
            "about": data[1],
            "facebook":data[2],
            "favourite_count":data[3],
            "image_name": data[4],
            "instagram": data[6],
            "name": data[7],
            "rating": data[8],
            "review_count": data[9],
            "slug": data[10],
            "twitter": data[11],
            "url": data[12],
            "website": data[13],
            "title": 'NULL',
            "license_number": 'NULL',
            "license_state": 'NULL',
            "address": 'NULL',
            "city": 'NULL',
            "state": 'NULL',
            "postal_code": 'NULL',
            "phone_number": 'NULL',
            "email": 'NULL',
            "longitude": 'NULL',
            "latitude": 'NULL'
            },
            "target": {
            "type": "topic",
            "id": "brand"
            }
        }
        })
        headers = {
        'X-GetSocial-Access-Token': 'eArQJ37jMwLKin65d1vmewV9a0jPp6oxu5goCs4kL41C8Ogp3KLt84wdXMSnTyLpNf0VA4P6jcfPpIYrAeFxzD4YLf9ubzlGL5SUxzW1906P6eHGJ1iPTwGQiKkg9wxInyFxhURh8BSz8eDjmkjeNTnjD2slT9pr5pjsLj4H3ceHQJXUnqB_sdK78Ep50UIPL-chQQYu5xSoPixiydVR7AHYqabqRM-FGff7AVMHKhw5MC-iRDNIQfJGDWAbweQrnJQFw5zio-w5pgOAk1YTPTNLIIkTl4kIM1aBbvtVbGCFenGRdJETyr6HcsAtZh0JHeN_686NOLkUHDbQGOD6fdNdJddu3N-iFuGfFGmlSLphLlliE9wEJdeRmrNdM-Er03Zd8LGoB4J3YzwIPCcCS3RMnnVOcMBAxlftMIyc6vV-624wius6',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        print(f'{record} added')
        record += 1
        # time.sleep(2)