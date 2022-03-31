import requests
import json
import csv
import time

with open('csv/doctor_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    headings = next(csv_reader)

    for data in csv_reader:
        print(data)
        url = "https://api.getsocial.im/v1/communities/activities"

        payload = json.dumps({
        "activity": {
            "id": "690780X0R99kG7",
            "content": {
            "language": "en",
            "text": "Created with script",
            "attachments": [
                {
                "image": data[32]
                }
            ]
            },
            "properties": {
            "first_name": data[0],
            "last_name": data[1],
            "about": data[2],
            "clinic_name": data[3],
            "year_in_practice": data[4],
            "speciality": data[5],
            "license_state": data[6],
            "license_number": data[7],
            "address": data[8],
            "city": data[9],
            "state": data[10],
            "postal_code": data[11],
            "phone_number": data[12],
            "email": data[13],
            "website": data[14],
            "consulting_office_visit_fees": data[15],
            "consulting_office_videocall_fees": data[16],
            "telehealth": data[17],
            "in_person": data[18],
            "insurance": data[19],
            "military_veteran_discount": data[20],
            "MMC": data[21],
            "MMC_physical": data[22],
            "MMC_digital": data[23],
            "payment_credit_debit": data[24],
            "payment_android_pay": data[25],
            "payment_applepay": data[26],
            "payment_paypal": data[27],
            "payment_venmo": data[28],
            "fee_initial_consultation": data[29],
            "longitude": data[30],
            "latitude": data[31]
            },
            "target": {
            "type": "topic",
            "id": "doctors"
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
