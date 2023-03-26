#collect oCare Pro 100 Watch data from 
from bluepy import btle
from datatime import datatime 
import csv
service_uuid = '1822'
address = 'd6:7c:c2:48:4e:06'
p = btle.Peripheral(address, btle.ADDR_TYPE_RANDOM)
p.setDelegate(MyDelegate())
svc = p.get.ServiceByUUID(servic_uuid)
notify = svc.getCharacteristics()[0]
notify_handle = notify.getHandle() + 1                               
