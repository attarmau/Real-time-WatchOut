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
p.writeCharacterisitic(notify_handle, b'\x01\x00')


#data storage on a computer

classMyDelegate(btle.DefaultDelegate)
  def__init__(self)
    btle.DefaultDelegate.__init__(self)
def handleNotification(self, cHandle, data):
hex = list()
for a Char in data:
  hex.append(aChar)
SpO2 = hex[2]
HR = hex[4]
localtime = datatime.now().strftime( '%Y-%m-%d%H:%M:%S' )
print(localtime)
print('Your Realtime SpO2:', SpO2)
print('Your Realtime: ', HR)
