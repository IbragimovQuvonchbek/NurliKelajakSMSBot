import os
import requests
import dotenv

dotenv.load_dotenv()


def get_token():
    url = 'https://notify.eskiz.uz/api/auth/login'
    data = {
        'email': os.getenv('GMAIL'),
        'password': os.getenv('PASSWORD'),
    }

    response = requests.post(url, data=data)

    return response.json()['data']['token']


print(get_token())