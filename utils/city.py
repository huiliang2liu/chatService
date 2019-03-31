#-*- coding:utf-8 -*-
import xml.sax as sax
from django.http import HttpResponse as response
import json
class Area():
    def __init__(self,name,postcode):
        self.name=name
        self.postcode=postcode
    def to_dict(self):
        return {"name":self.name,"postcode":self.postcode}
class City():
    def __init__(self,name,postcode,areas=[]):
        self.name=name
        self.postcode=postcode
        self.areas=areas
    def to_dict(self):
        ja=[]
        for area in self.areas:
            ja.append(area.to_dict())
        return {"name":self.name,"postcode":self.postcode,"areas":ja}

class Province():
    def __init__(self,shouzimu,quanpin,jianpin,name,postcode,cities=[]):
        self.shouzimu=shouzimu
        self.quanpin=quanpin
        self.jianpin=jianpin
        self.name=name
        self.postcode=postcode
        self.cities=cities
    def to_dict(self):
        ci_dicts=[]
        for city in self.cities:
            ci_dicts.append(city.to_dict())
        return {"name":self.name,"shouzimu":self.shouzimu,"quanpin":self.quanpin,"jianpin":self.jianpin,"postcode":self.postcode,"cities":ci_dicts}
class CityHandler(sax.ContentHandler):
    def __init__(self):
        self.provinces=[]
    def startElement(self, name, attrs):
        if name=="province":
            self.provinces.append(Province(attrs["shouzimu"],attrs["quanpin"],attrs["jianpin"],attrs["name"],attrs["postcode"]))
        elif name=="city":
            self.provinces[-1].cities.append(City(attrs["name"],attrs["postcode"]))
        elif name=="area":
            self.provinces[-1].cities[-1].areas.append(Area(attrs["name"],attrs["postcode"]))
def parse_city():
    parser = sax.make_parser()
    parser.setFeature(sax.handler.feature_namespaces, 0)
    handler = CityHandler()
    parser.setContentHandler(handler)
    parser.parse("files/city.xml")
    return handler.provinces
def parse(request):
    provinces=[]
    for province in parse_city():
        provinces.append(province.to_dict())
    return response(json.dumps({"code":0,"province":parse_city()[0].to_dict(),"size":len(provinces)}))
def card_city(request):
    if request.GET:
        card=request.GET["card"]
    else:
        card=request.POST["card"]
    if card.startswith("430411"):
        return response(json.dumps({"code":1,"city":"湖南省衡阳市耒阳市"}))
    for province in parse_city():
        if(province.postcode.startswith(card[0:2])):
            for city in province.cities:
                if(len(city.areas)>0):
                    if (city.postcode.startswith(card[0:4])):
                        for area in city.areas:
                            if area.postcode.startswith(card[0:6]):
                                return response(json.dumps({"code":0,"city":province.name+city.name+area.name}))
                else:
                    if city.postcode.startswith(card[0:6]):
                        return response(json.dumps({"code":0,"city":province.name+city.name}))
    return response(json.dumps({"code":1,"msg":"not foud card city"}))
def card_sex(request):
    if request.GET:
        card=request.GET["card"]
    else:
        card=request.POST["card"]
    if int(card[-2])%2==0:
        return response(json.dumps({"code":0,"sex":"女"}))
    return response(json.dumps({"code":0,"sex":"男"}))
def card_birthday(request):
    if request.GET:
        card=request.GET["card"]
    else:
        card=request.POST["card"]
    if len(card)==15:
        return response(json.dumps({"code":0,"birthday":card[6:12]}))
    return response(json.dumps({"code":0,"birthday":card[6:14]}))

