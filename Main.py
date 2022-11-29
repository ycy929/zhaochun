import json
import os
import random
from hashlib import md5

import requests

pwd = os.path.dirname(os.path.abspath(__file__)) + os.sep

headers = {
    "os": "android",
    "phone": "HuaWei|P30|12",
    "appVersion": "38",
    "Sign": "111111",
    "cl_ip": "192.168.1.3",
    "User-Agent": "okhttp/3.14.9",
    "Content-Type": "application/json;charset=utf-8"
}


def getMd5(text: str):
    return md5(text.encode('utf-8')).hexdigest()


def getDeviceId():
    ret = ""
    for i in range(36):
        num = random.randint(0, 9)
        letter = chr(random.randint(97, 122))  # 取小写字母
        Letter = chr(random.randint(65, 90))  # 取大写字母
        s = str(random.choice([num, letter, Letter]))
        ret += s
    return ret


def parseUserInfo():
    allUser = ''
    if os.path.exists(pwd + "user.json"):
        with open(pwd + "user.json", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                allUser = allUser + line + '\n'
    else:
        return json.loads(os.environ.get("USERS", ""))
    return json.loads(allUser)


def save(uid, token):
    url = 'http://sxbaapp.zcj.jyt.henan.gov.cn/interface/clockindaily.ashx'

    d = "{\"dtype\":3,\"uid\":" + "\"" + uid + "\"}" + token
    headers["sign"] = getMd5(d)

    res = requests.post()


def getToken():
    url = 'http://sxbaapp.zcj.jyt.henan.gov.cn/interface/token.ashx'
    res = requests.post(url, headers=headers)
    print('请求token:', res.json()["data"]["token"])
    return 'b41681c919f1fe1551421751bf13a1d11891671131e415d1'
    # return res.json()["data"]["token"]


def login(user, password, deviceId, token):
    d = '{\"phone\":\"' + user["phone"] + "\",\"password\":" + "\"" + password + "\"," + \
        "\"dtype\":6,\"dToken\":" + "\"" + deviceId + "\"}" + token
    headers["sign"] = getMd5(d)

    data = '{\"phone\":\"' + user["phone"] + "\",\"password\":" + "\"" + password + "\"," + \
           "\"dtype\":6,\"dToken\":" + "\"" + deviceId + "\"}"

    url = 'http://sxbaapp.zcj.jyt.henan.gov.cn/interface/relog.ashx'
    res = requests.post(url, headers=headers, data=json.dumps(data))
    # return res.json()["data"]["uid"]
    return "123"


def prepareSign(user):
    if not user["enable"]:
        return

    token = getToken()
    password = getMd5(user["password"])
    deviceId = getDeviceId()

    uid = login(user, password, deviceId, token)

    uid = "123"

    resp = save(uid, token)


if __name__ == '__main__':
    users = parseUserInfo()

    for user in users:
        prepareSign(user)
