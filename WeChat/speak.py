# coding=utf-8
import json
import itchat
import pygame
import time
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.parse import quote_plus
IS_PY3 = True
API_KEY = 'u04w4xRq9W47rtGY8LliFePl'
SECRET_KEY = '3zb2LfynjY68W1GHkFiHvDspz9lQzFUO'

# 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
PER = 1
# 语速，取值0-15，默认为5中语速
SPD = 5
# 音调，取值0-15，默认为5中语调
PIT = 5
# 音量，取值0-9，默认为5中音量
VOL = 5
# 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
AUE = 3

FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
FORMAT = FORMATS[3]

CUID = "123456PYTHON"

TTS_URL = 'http://tsn.baidu.com/text2audio'


class DemoError(Exception):
    pass


"""  TOKEN start """

TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选


def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print('token http response http code : ' + str(err.code))
        result_str = err.read()
    if (IS_PY3):
        result_str = result_str.decode()

    result = json.loads(result_str)
    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not SCOPE in result['scope'].split(' '):
            raise DemoError('scope is not correct')
        return result['access_token']
    else:
        raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')


"""  TOKEN end """


TEXT = ["Today is not easy, tomorrow will be more difficult, \
        but the day after tomorrow will be fantastic!.Please believe in yourself!",
        "您的台灯已打开!","您的台灯已关闭",
        "欲穷千里目，更上一层楼。",
        "I was designed mainly for the last gruadtion based on the raspberrypi. 请多多指教！",
        "昨夜西风凋碧树，独上高楼，望断天涯路，此第一境也，衣带渐宽终不悔，为伊消得人憔悴，此第二境也，\
        众里寻他千百度，蓦然回首，那人却在灯火阑珊处，此第三境也。",
        "When you paly,play hard.When you study,study hard."]
def speak(text):
    print("请求时间：%s" % time.asctime())
    token = fetch_token()
    tex = quote_plus(text)
    params = {'tok': token, 'tex': tex, 'per': PER, 'spd': SPD, 'pit': PIT, 'vol': VOL, 'aue': AUE, 'cuid': CUID,
              'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数

    data = urlencode(params)
    req = Request(TTS_URL, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result = f.read()

        headers = dict((name.lower(), value) for name, value in f.headers.items())
        print("请求返回时间：%s" % headers['date'])
        print("请求文件类型：%s" % headers['content-type'])

        save_file = 'result.' + FORMAT
        with open(save_file, 'wb') as of:
            of.write(result)
            print("成功保存至：%s" % save_file)
            pygame.mixer.pre_init(frequency=16000)
            pygame.mixer.init()
            pygame.mixer.music.load("result.mp3")
            pygame.mixer.music.play()

    except URLError as err:
        print('asr http response http code : ' + str(err.code))

#speak(TEXT[1])
def moment(Timestamp):
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(Timestamp))
    return t


@itchat.msg_register(itchat.content.TEXT)
def replay(msg):
    if msg['FromUserName'] == "@1bcd511740e6f63b4e42b0b3fea8bf02886af4964bfe11f38944a13090daa703":
        print("{0} from:{1} 备注:{2}".format(moment(\
            msg['CreateTime']), msg['User']['NickName'], msg['User']['RemarkName']))
        print("content:%s" % msg.text)
        
        with open("/home/pi/wechat/message.txt",'a') as file:
            file.write("{0} from:{1} 备注:{2}".format(moment(\
                msg['CreateTime']), msg['User']['NickName'], msg['User']['RemarkName'])+"\r\n"+msg.text+"\r\n")

        with open("/home/pi/wechat/log.txt",'w') as file:
            file.write(msg.text)
            
        if msg.text == '开灯':
            print('灯已打开')
            itchat.send('灯已打开', toUserName=msg['FromUserName'])
        elif msg.text == '关灯':
            print('灯已关闭')
            itchat.send('灯已关闭', toUserName=msg['FromUserName'])
        else:
            #itchat.send(msg.text, toUserName=msg['FromUserName'])
            index = "收到来自{0}的消息".format(msg['User']['NickName'] if msg['User']['RemarkName'] == '' \
                                        else msg['User']['RemarkName'])
            speak(index + msg.text)


print(itchat.__version__)
itchat.auto_login(hotReload=True)
itchat.run()

