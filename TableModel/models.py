# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
    id=models.IntegerField(primary_key=True,blank=True,null=False,verbose_name="用户ID")

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
            if tok.token==tok:
                return tok
            else:
                tok.token=token
                tok.save()
                return tok
        except:
            print "token error"
            pass
    try:
        tok=TokenTable.objects.create(id=id,token=token)
        return tok
    except:
        print "insert token error"
        pass
    return None
def delete_token(id):
    tok=get_token(id=id)
    if tok:
        try:
            tok.delete()
            return tok
        except:
            print "delete token error"
            pass
    return None

