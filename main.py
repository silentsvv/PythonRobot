import turing
import AipSpeech
import os
import time
import turing
import json

def main():
    switch = True
    while switch:
        os.system("arecord -D plughw:CARD=Device -r 16000 -c 1 -d 3 -t wav -f S16_LE record.wav")
        time.sleep(0.5)
        info = AipSpeech.get_speak_text()
        if '关闭' in info:
            break
        elif '暂停' in info:
            print('暂停10s')
            time.sleep(10)
            continue
        elif '识别失败' in info:
            continue
        else:
            turingResult = turing.Turn(info)
            turingResult = json.loads(turingResult)
            speak = turingResult['results'][0]['values']
            print(speak)


if __name__ == '__main__':
    main()