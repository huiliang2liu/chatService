# -*-   coding:utf-8 -*-
from django.http import HttpResponse as re
import json
def upload(request):
    print request
    if request.method=="get":
        return re(json.dumps({"code":1}))
    myFile = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
    if not myFile:
        return re(json.dumps({"code":0}))
    destination = open("files/{}".format(myFile), 'wb+')  # 打开特定的文件进行二进制的写操作
    for chunk in myFile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()
    return re(json.dumps({"code":0}))
