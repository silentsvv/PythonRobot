import requests;
import hashlib;

def Turn(String):
    url = "http://openapi.tuling123.com/openapi/api/v2";
    userId = "silentsvv";
    hl = hashlib.md5();
    hl.update(userId.encode(encoding='utf-8'));
    headers = {
        'content-type': 'application/json'
    }

    body = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": String
            }
        },
        "userInfo": {
            "apiKey": "4a3276fba3344333b9e299c1c74d833e",
            "userId": "8d49d414621cc60ec1bd2807a5cae54c"
        }
    }

    r = requests.post(url, json=body);
    return r.text;
