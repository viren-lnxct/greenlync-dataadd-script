import requests
import json
import csv
import time
record = 1
with open('csv2/weedmaps_doctors_data.csv') as csv_file:
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
            "text": "Doctor",
            "attachments": [
                {
                "image": data[17]
                }
            ]
            },
            "properties": {
            "wm_doctors_id": data[0],
            "name": data[1],
            "address": data[2],
            "state": data[3],
            "city": data[4],
            "postal_code": data[5],
            "doctor_type": data[6],
            "email": data[7],
            "facebook": data[8],
            "sunday":data[9],
            "monday":data[10],
            "tuesday":data[11],
            "wednesday":data[12],
            "thursday":data[13],
            "friday":data[14],
            "saturday":data[15],
            "image_name":data[16],
            "instagram":data[18],
            "latitude":data[19],
            'license_type':data[20],
            'longitude':data[21],
            'ranking':data[22],
            'rating':data[23],
            'review_count':data[24],
            'phone_number':data[25],
            'timezone':data[26],
            'twitter':data[27],
            'url':data[28],
            'website':data[29],
            'year_in_practice':'NULL',
            'speciality':'NULL',
            'license_state':'NULL',
            'license_number':'NULL',
            'consulting_office_visit_fees':'NULL',
            'consulting_office_videocall_fees':'NULL',
            "telehealth":'false',
            "in_person":'false',
            'insurance':'false',
            "military_veteran_discount": 'false',
            "MMC": 'false',
            "MMC_physical": 'false',
            "MMC_digital": 'false',
            "payment_credit_debit": 'false',
            "payment_android_pay": 'false',
            "payment_applepay": 'false',
            "payment_paypal": 'false',
            "payment_venmo": 'false',
            "fee_initial_consultation": 'false',
            },
            "target": {
            "type": "topic",
            "id": "doctors"
            }
        }
        })
        headers = {
        'X-GetSocial-Access-Token': 'MTWsqStym82kptB4LaEF4MIAIma5co0KE7NhEXA-YhkqB7DCNkekPgGCImALZJdCWWNmJOinN7W2HFGIRJbqAZ4J9z6uHj_AdDWkO0Sa9P1cn0seghDMYZrlh071Wp0wMiLC7Ey9JmQd2sPrs6t-NlfvWfMHw2JblFNyRSRO5sp9gxlwI1JRrT4MYBUM3oj6NVKI9pRLiyyeRqZnXZJe3gmZdGMO3c_21eI0SbBFBNdLoBi6p_rwcFVi8IQ1oXVQLKriMJP88FTLyldLCDNy57lWkUZbsxVphBJVrtZLx-3SielA6w83PagGuMyQ8VocwNOfD-0S_zBhYDTL6xcoNm3fDdGLjiHLPrY2Ul2mF7SyiquL3KfROLBHMlaVUhbnHqCa4_o2tmgTs4Fqn_NPNYewQ-9gRypP-ZXQRJ56yx6suopGCtE=',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
        print(f'{record} added')
        record += 1
        time.sleep(2)
