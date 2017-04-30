# SatelliteTrackingApi
noaa = Satellite('http://www.n2yo.com/sat/instant-tracking.php?s=28654&hlat=1.28967&hlng=103.85007&d=300&r=265692351376.14594&tz=GMT+05:30&O=n2yocom&rnd_str=49b2795dfd48ba0b32a576e5b0685fbc&callback=', 'noaa18', 100)
noaa.setLocation(noaa.getLocation())
lst = [aqua, calipso, cloudsat, noaa]
