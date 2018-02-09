#!/usr/bin/env python
# -*- coding: utf-8 -*-
from stf_selector.selector import Selector


http_stf = Selector(url='http://172.16.120.59:7100/api/v1/devices', token='a25c793abb854c858fc2e82b8692bf463f64cdf8a92e478d8cf0699fce2384c9')

http_stf.load()
devices = http_stf.find().devices()
# print(devices)
print(len(devices))
list=[]
for device in devices:
            if device.get('remoteConnectUrl') is not None:
                url = device['remoteConnectUrl']
                list.append(str(url))

            else:
                url = device['display']['url'][5:]
                list.append(str(url))
            port = int(url[-4:])
            if port % 2 == 0:
                port += 1
            else:
                pass
            url = url[:-5] + ":" + str(port)

print(url)
print(list)