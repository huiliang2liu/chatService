# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import time

# Create your models here.
class UserTable(models.Model):
    id=models.AutoField(primary_key=True,blank=True,null=False,verbose_name="用户ID")
    nickname=models.TextField(blank=True,null=False,verbose_name="用户名")
    password=models.TextField(blank=True,null=False,verbose_name="用户密码")
    head=models.TextField(blank=True,null=False,verbose_name="用户头像")
class HxTable(models.Model):
    id=models.IntegerField(primary_key=True,blank=True,null=False,verbose_name="用户ID")
    uuid = models.TextField(blank=True, null=False, verbose_name="环信用户ID")
    created = models.IntegerField(blank=True, null=False, verbose_name="创建时间")
    modified = models.IntegerField(blank=True, null=False, verbose_name="修改时间")
    username = models.TextField(blank=True, null=False, verbose_name="用户名")
    nickname = models.TextField(blank=True, null=False, verbose_name="昵称")
    password = models.TextField(blank=True, null=False, verbose_name="密码")
class TokenTable(models.Model):
    token=models.TextField(primary_key=True,blank=True,null=False,verbose_name="Token")
    id=models.IntegerField(unique=True,blank=True,null=False,verbose_name="用户ID")
    time=models.IntegerField(blank=True,null=False,verbose_name="token生成的时间",default=0)
class FriendTable(models.Model):
    id=models.IntegerField(primary_key=True,blank=True,null=False,verbose_name="用户ID")
    friends=models.TextField(blank=True,null=False,verbose_name="朋友ID")

def get_user(id=0,nickname=""):
    if id:
        try:
            return UserTable.objects.get(id=id)
        except:
            print "id get user error"
            return None
    elif nickname:
        try:
            return UserTable.objects.get(nickname=nickname)
        except:
            print "nickname get user error"
            return None
    return None
def insert_user(nickname,password,head):
    u=get_user(nickname=nickname)
    if u:
        return None
    try:
        u=UserTable.objects.create(nickname=nickname,password=password,head=head)
        return u
    except:
        print "insert user error"
        pass
    return None


def delete_user(id=0):
    try:
        u=get_user(id=id)
        if u:
            u.delete()
            return u
    except:
        print "delete user error"
        pass
    return None
def update_user(id,nickname="",password="",head=""):
    u=get_user(id)
    if u:
        if nickname and password and head:
            if nickname:
                u.nickname = nickname
            if password:
                u.password = password
            if head:
                u.head = head
            try:
                u.save()
            except:
                print "update user error"
    return u
def get_hx_user(id):
    try:
        hx=HxTable.objects.get(id=id)
        if hx:
            return hx
    except:
        print "get hx user error"
        return None
    return None
def insert_hx_user(id,uuid,created,modified,username,nickname,password):
    hx=get_hx_user(id=id)
    if hx:
        None
    try:
        hx=HxTable.objects.create(id=id,uuid=uuid,created=created,modified=modified,username=username,nickname=nickname,password=password)
        return hx
    except:
        print "insert hx user error"
        pass
    return None
def delete_hx_user(id):
    hx=get_hx_user(id=id)
    if hx:
        try:
            hx.delete(hx)
            return hx
        except:
            print "tdelete hx user error"
            pass
    return None
def get_token(id="",token=""):
    if token:
        try:
            token = TokenTable.objects.get(token=token)
            return token
        except:
            print "token get token error"
            pass
    if id:
        try:
            token = TokenTable.objects.get(id=id)
            return token
        except:
            print "id get token error"
            pass
    return None
def insert_token(id,token):
    tok=get_token(id)
    if tok:
        try:
            t=int(time.time()*1000)
            if tok.token==tok:
                tok.time=t
            else:
                tok.token=token
                tok.time = t
            tok.save()
            return tok
        except:
            print "token error"
            pass
    try:
        tok=TokenTable.objects.create(id=id,token=token)
        return tok
    except Exception,e:
        print e
        pass
    return None
def delete_token(id="",token=""):
    if id:
        tok=get_token(id=id)
    else :
        tok=get_token(token=token)
    if tok:
        try:
            tok.delete()
            return tok
        except:
            print "delete token error"
            pass
    return None
def get_friends(id):
    try:
        f_f=FriendTable.objects.get(id=id)
        if f_f:
            return f_f.split(",")
        return None
    except:
        print "朋友数据查询错误"
    return None
def update_friends(id,friend_id):
    f_friends=get_friends(id=id)
    if f_friends:
        f_friends.append(f_friends)
    else:
        f_friends={}
        f_friends.append(f_friends)
    try:
        FriendTable.objects.create(id=id,friends=",".join(f_friends))
        return True
    except:
        print "朋友更新错误"
    return False
def delete_friends(id,friend_id):
    f_friends=get_friends(id=id)
    if f_friends:
        re=f_friends.remove(f_friends)
        if re:
            try:
                if len(f_friends)>0:
                    FriendTable.objects.update(id=id, friends=",".join(f_friends))
                else:
                    FriendTable.objects.get(id=id).delete()
                return True
            except:
                print "删除朋友错误"
            return False
        return False
    return False





