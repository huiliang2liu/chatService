#-*-  coding:utf-8 -*-
import requests as re
import json

url = 'http://a1.easemob.com/{}/{}/{}'  # 环信地址
orgname = "1141170206178645"
appname = "ceshi"
client_id = "YXA6XjNkACCLEemxkNmYPYg2wQ"
client_secret = "YXA6tHuRiUP5zFeoOvi5YiTw3-ZxHUk"
token = None
"""注册环信使用的用户"""


class RegistXhUser():
    def __init__(self, username, password, nickname):
        self.username = username
        self.password = password
        self.nickname = nickname


"""环信用户"""


class XhUser():
    def __init__(self, entity):
        self.uuid = entity["uuid"]
        self.type = entity["type"]
        self.created = entity["created"]
        self.username = entity["username"]
        self.nickname = entity["nickname"]


def request_url(package,data=None):
    if data:
        request = re.post(url.format(orgname, appname, package), data=data,
                          headers={"Authorization": "Bearer {}".format(get_token())})
    else:
        request = re.get(url.format(orgname, appname, package),
                         headers={"Authorization": "Bearer {}".format(get_token())})
    if request.status_code == 200:
        return request.text
    return None


def get_token():
    if token:
        return token
    request = re.post(url.format(orgname, appname, "token"), data=json.dumps(
        {"grant_type": "client_credentials", "client_id": client_id, "client_secret": client_secret}))
    if request.status_code != 200:
        return None
    token_js = json.loads(request.text)
    return token_js["access_token"]


def regits_hx(regist_user):
    regist_users = [regist_user]
    hxs = regist_hxs(regist_users)
    if (not hxs) or len(hxs) <= 0:
        return None
    return hxs[0]


def regist_hxs(regist_users):
    if (not regist_users) or len(regist_users) <= 0:
        return None
    users = []
    for regist_user in regist_users:
        users.append(
            {"username": regist_user.username, "password": regist_user.password, "nickname": regist_user.nickname})
    request = request_url(json.dumps(users), "users")
    if not request:
        return None
    js = json.loads(request)
    entities = js["entities"]
    if (not entities) or len(entities):
        return None
    hx_user = []
    for entity in entities:
        hx_user.append(XhUser(entity))
    return hx_user
def get_users(size):
    return request_url("users?limit={}".format(size))
def delete_user(username):
    request=re.delete(url.format(orgname, appname, "users/{}".format(username)),
                         headers={"Authorization": "Bearer {}".format(get_token())})
    if request.status_code!=200:
        return None
    print request.text
    return XhUser(json.loads(request.text)["entities"][0])
print delete_user("liuhuiliang910")

