from django.http import HttpResponse as response
import json
import TableModel.models as db
import time
import requests
url = 'http://a1.easemob.com/1141170206178645/ceshi/'

def login(request):
    if request.GET:
        js=json.loads(request.GET["m"])
    else:
        js=json.loads(request.POST["m"])
    name=js["name"]
    password=js["pas"]
    if name and password:
        u=db.get_user(nickname=name)
        if u:
            if u.password==password:
                hx_u=db.get_hx_user(id=u.id)
                t=time.time()
                to=db.insert_token(id=u.id,token=u.nickname+str(int(round(t*1000))))
                ujs={"code":0,"token":to.token,"hx":{"nickname":hx_u.nickname,"pass":hx_u.password}}
            else:
                ujs = {"code": 1, "msg": "password error"}
        else:
            ujs = {"code": 2, "msg": "user is not found"}
    else:
        ujs={"code":3,"msg":"name or pass is empty"}
    return response(json.dumps(ujs))
def regist(request):
    if request.GET:
        js=json.loads(request.GET["m"])
    else:
        js=json.loads(request.POST["m"])
    name=js["name"]
    password=js["pas"]
    if name and password:
        u = db.get_user(nickname=name)
        if u:
            ujs={"code":4,"msg":"user is exist"}
        else:
            u=db.insert_user(nickname=name,password=password,head="http://cdn.duitang.com/uploads/item/201411/09/20141109222431_58P5J.thumb.700_0.png")
            head={"Content-Type":"application/json"}
            hx_js={"username":u.nickname,"password":u.password,"nickname":u.nickname}
            r_hx=requests.post(url+"users",data=json.dumps(hx_js),headers=head)
            if r_hx.status_code==400:
                ujs={"code":5,"msg":"hx error"}
            else:
                hx_js=json.loads(r_hx.text)
                entity=hx_js["entities"][0]
                print u.id
                hx_u =db.insert_hx_user(id=u.id,uuid=entity["uuid"],created=entity["created"],modified=entity["modified"],username=u.nickname,nickname=u.nickname,password=u.password)
                if hx_u:
                    print u.id
                    to = db.insert_token(id=u.id, token=u.nickname + str(int(round(time.time() * 1000))))
                    if to:
                        ujs = {"code": 0, "token": to.token, "hx": {"nickname": hx_u.nickname, "pass": hx_u.password}}
                    else:
                        ujs = {"code": 1, "msg": "insert token error"}
                else:
                    ujs={"code":1,"msg":"insert hx error"}

    else:
        ujs={"code":6,"msg":"username or pass is empty"}
    return response(json.dumps(ujs))
def detail(request):
    if request.GET:
        token=request.GET["token"]
    else:
        token=request.POST["token"]
    if token:
        to=db.get_token(token=token)
        if to:
            u=db.get_user(id=to.id)
            if u:
                ujs={"code":0,"user":{"name":u.nickname,"head":u.head}}
            else:
                ujs={"code":1,"msg":"not found user"}
        else:
            ujs={"code":1,"msg":"token error"}
    else:
        ujs={"code":1,"msg":"token is empty"}
    return response(json.dumps(ujs))