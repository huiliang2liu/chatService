# -*-   coding:utf-8 -*-
from django.http import HttpResponse as re
import time
import json
def upload(request):
    print request
    if request.method=="get":
        return re(json.dumps({"code":1}))
    myFile = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
    if not myFile:
        return re(json.dumps({"code":0}))
    with open("files/{}".format(myFile), 'wb') as destination:
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
    return re(json.dumps({"code":0}))
