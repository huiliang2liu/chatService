import TableModel.models as db
from django.http import HttpResponse as response
import json
def delete_all_user(request):
    try:
        users=db.UserTable.objects.all()
        if users:
            for user in users:
                user.delete()
        tokens=db.TokenTable.objects.all()
        if tokens:
            for token in tokens:
                token.delete()
        hxs=db.HxTable.objects.all()
        if hxs:
            for hx in hxs:
                hx.delete()
        return response(json.dumps({"code":0,"msg":"delete success"}))
    except Exception,e:
        print e
        pass
    return response(json.dumps({"code":1,"msg":"delete error"}))
def all_user(request):
    try:
        users=db.UserTable.objects.all()
        user_lis=[]
        if users:
            for user in users:
                user_lis.append({"password":user.password,"nickname":user.nickname,"head":user.head,"id":user.id})
        return response(json.dumps({"code":0,"users":user_lis}))
    except:
        return response(json.dumps({"code":1,"msg":"db error"}))
def delete_user(request):
    if request.GET:
        id=request.GET["id"]
    else:
        id=request.POST["id"]
    print id
    if id:
        try:
            user=db.UserTable.objects.get(id=id)
            if user:
                nickname=user.nickname
                user.delete()
                try:
                    hx=db.HxTable.objects.get(id=id)
                    if hx:
                        hx.delete()
                except:
                    pass
                try:
                    token=db.TokenTable.objects.get(id=id)
                    if token:
                        token.delete()
                except:
                    pass
                return response(json.dumps({"code":0,"user":{"nickname":nickname}}))
            else:
                return response(json.dumps({"code":1,"msg":"user id error"}))
        except :
            return response(json.dumps({"code":1,"msg":"db error"}))
    return response(json.dumps({"code":1,"msg":"not id"}))
