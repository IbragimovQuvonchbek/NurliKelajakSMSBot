import requests
import dotenv
import os
from getToken import get_token

dotenv.load_dotenv()


def send_sms(mobile_phone):
    url = 'https://notify.eskiz.uz/api/message/sms/send'
    callback_url = "http://0000.uz/test.php"
    token = get_token()
    message = '''Diqqat! Endilikda Qorako'l maktabi Kogon shahrida. 
    A'loqa: +998553055566 +998940583838 
    Ijtimoiy tarqmoqlar: https://t.me/nurlikelajakkarakul
    '''
    from_number = "4546"
    headers = {
        'Authorization': f'Bearer {token}',
    }

    data = {
        'mobile_phone': mobile_phone,
        'message': message,
        'from': from_number,
        'callback_url': callback_url
    }

    response = requests.post(url, headers=headers, data=data)

    return response.status_code
