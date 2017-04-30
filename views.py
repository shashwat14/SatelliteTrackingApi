# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:12:16 2017

@author: Shashwat
"""

from __init__ import app
from main import Satellite, Satellites
@app.route('/')
@app.route('/index')
def index():
    aqua = Satellite('http://www.n2yo.com/sat/instant-tracking.php?s=27424&hlat=1.28967&hlng=103.85007&d=300&r=588399124880.8425&tz=GMT+05:30&O=n2yocom&rnd_str=b5ec47c4e4e4721c2e0fa5f3a681e221&callback=', 'aqua', 1690000.)
    aqua.setLocation(aqua.getLocation())
    calipso = Satellite('http://www.n2yo.com/sat/instant-tracking.php?s=29108&hlat=1.28967&hlng=103.85007&d=300&r=1173810753651.1362&tz=GMT+05:30&O=n2yocom&rnd_str=b5ec47c4e4e4721c2e0fa5f3a681e221&callback=', 'callipso', 92.)
    calipso.setLocation(calipso.getLocation())
    cloudsat = Satellite('http://www.n2yo.com/sat/instant-tracking.php?s=29107&hlat=1.28967&hlng=103.85007&d=300&r=1027239537293.5146&tz=GMT+05:30&O=n2yocom&rnd_str=b5ec47c4e4e4721c2e0fa5f3a681e221&callback=', 'cloudsat', 1400.)
    cloudsat.setLocation(cloudsat.getLocation())
    lst = [aqua, calipso, cloudsat]
    s = Satellites(lst)
    #print (aqua.getJson())
    return s.getJson()