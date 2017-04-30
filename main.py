# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 12:56:28 2017

@author: Shashwat
"""
import requests
import time
import json
class Satellite(object):
    
    def __init__(self, link, name, swathe):
        self.link = link
        self.name = name
        self.swathe = swathe
    def fetch(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}          
        json = requests.get(self.link, headers=headers)
        return json
        
    def getLocation(self):
        data = (self.fetch()).json()[0]['pos'][0]['d'].split('|')
        return data
        
    def setLocation(self, data):
        self.lat = float(data[0])
        self.lon = float(data[1])
        self.az = float(data[2])
        self.el = float(data[3])
        self.id = float(data[8])
        self.alt = float(data[6])
        self.time = float(data[9])
    
    def getKVP(self):
        data = {}
        data['name'] = self.name
        data['id'] = self.id
        data['lat'] = self.lat
        data['lon'] = self.lon
        data['alt'] = self.alt
        data['time'] = self.time
        data['swathe'] = self.swathe
        return data
        
class Satellites(object):
    
    def __init__(self, lst):
        self.lst= lst
    
    def getJson(self):
        dic = {}
        for sat in self.lst:
            KVP = sat.getKVP()
            dic[KVP['name']] = KVP
        return json.dumps(dic)
        
aqua = Satellite('http://www.n2yo.com/sat/instant-tracking.php?s=27424&hlat=1.28967&hlng=103.85007&d=300&r=588399124880.8425&tz=GMT+05:30&O=n2yocom&rnd_str=b5ec47c4e4e4721c2e0fa5f3a681e221&callback=', 'aqua', 1690000.)
calipso = Satellite('http://www.n2yo.com/sat/instant-tracking.php?s=29108&hlat=1.28967&hlng=103.85007&d=300&r=1173810753651.1362&tz=GMT+05:30&O=n2yocom&rnd_str=b5ec47c4e4e4721c2e0fa5f3a681e221&callback=', 'callipso', 92.)
cloudsat = Satellite('http://www.n2yo.com/sat/instant-tracking.php?s=29107&hlat=1.28967&hlng=103.85007&d=300&r=1027239537293.5146&tz=GMT+05:30&O=n2yocom&rnd_str=b5ec47c4e4e4721c2e0fa5f3a681e221&callback=', 'cloudsat', 1400.)
while True:
    print ("Fetching data at " + str(time.time()))
    f = open('data.txt', 'w')
    aqua.setLocation(aqua.getLocation())
    calipso.setLocation(calipso.getLocation())
    cloudsat.setLocation(cloudsat.getLocation())
    lst = [aqua, calipso, cloudsat]
    s = Satellites(lst)
    f.write(s.getJson())
    f.close()
    time.sleep(1)
    