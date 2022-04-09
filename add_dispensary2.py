import requests
import json
import csv
import time

record = 1
with open('csv2/weedmapsdispensaries_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    headings = next(csv_reader)

    for data in csv_reader:
        if record < 4794:
            record += 1
            continue
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
            "text": "Created with script",
            "attachments": [
                {
                "image": data[13]
                }
            ]
            },
            "properties": {
            "dispensary_hash": data[0],
            "id": data[1],
            "wmid":data[2],
            "name":data[3],
            "address": data[4],
            "city": data[5],
            "region":data[6],
            "state": data[7],
            "postal_code": data[8],
            "phone_number": data[9],
            "email": data[10],
            "description":data[11],
            "intro_body":data[12],
            "reviews_count":data[14],
            "rating":data[15],
            "ranking":data[16],
            "delivery_minimum_order":data[17],
            "delivery_fees":data[18],
            "license_type": data[19],
            "latitude": data[20],
            "longitude": data[21],
            "is_storefront": data[22],
            "has_pickup":data[23],
            "best_of_weedmaps":data[24],
            "has_testing":data[25],
            "is_recreational":data[26],
            "url":data[27],
            "sunday":data[28],
            "monday":data[29],
            "tuesday":data[30],
            "wednesday":data[31],
            "thursday":data[32],
            "friday":data[33],
            "saturday":data[34],
            "is_delivery":data[35],
            "image_name":data[36],
            "website": 'NULL',
            "license_state": 'NULL',
            "license_number": 'NULL',
            },
            "target": {
            "type": "topic",
            "id": "dispensary"
            }
        }
        })
        headers = {
        'X-GetSocial-Access-Token': 'UByV3FaIHgPotmyEaoIxu9c82q_kSFnOaV6ML1y5zBll9oxRivf3YQypbYzyVqwQuKVbaUIJ9CQ4Af23tsa36alj0y8eASlcibpKgwXak0RgeFp7GCwZQ99a7ZBpWLXXtQPd6zbdN4j3BTg8xEHgB5H8ox5HyZVZjx8tBNhUiIU1N-eAHzXOUe8KGk1ZgqPkY1hrCnga0dg-DHNo0oBWq2eduiDlGG8QsFMb4k9fBN4DAf9yyd2WSbQR0fDd3LZdmOxdA0ymp2RcNiyZDifFhIacTrJIQTL0SCs1qxfjOb_NAGh8NIak8PbN2-Ep4oPvh2E01FRkdqYqHK_eKP_l5jtWA28iPI1IFiPLKpysgDe1KMBUiQVGYnAHJ28fimshwyU3Z6e0hPTVO5yA8NryKWZfhMu5fpxH8ImPly8D0UN83IgaXhiN',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        print(f'{record} ADDED')
        record += 1