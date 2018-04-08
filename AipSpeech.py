from aip import AipSpeech;
import turing;

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

if __name__ == '__main__':
    APP_ID = '11038342'
    API_KEY = 'MqYI3MKxTwhffA1WoGtbveu3'
    SECRET_KEY = 'CbK8o3NqfzH6LpKO2m5M2WnViEfKH61z'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    # 识别本地文件
    result = client.asr(get_file_content('16k.wav'), 'wav', 16000, {
        'dev_pid': '1536',
    })

    print(result['result'][0]);
    turing.Turn(result['result'][0]);

    print()
    result2 = client.synthesis('你好百度', 'zh', 1, {
        'vol': 5,
    })

    with open('auido.mp3', 'wb') as f:
            f.write(result2)