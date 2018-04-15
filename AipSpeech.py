from aip import AipSpeech
import json
import turing

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_speak_text():
    APP_ID = '11038342'
    API_KEY = 'MqYI3MKxTwhffA1WoGtbveu3'
    SECRET_KEY = 'CbK8o3NqfzH6LpKO2m5M2WnViEfKH61z'

    try:
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        # 识别本地文件
        result = client.asr(get_file_content('record.wav'), 'wav', 16000, {
            'dev_pid': '1536',
        })
        return result['result'][0]
    except Exception:
        print("识别失败")
        return "识别失败"

if __name__ == '__main__':
    get_speak_text()
