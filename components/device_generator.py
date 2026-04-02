from device import Device
from random import random
dDir = []

itemOfDevices = 50
for device in range(0,itemOfDevices):
    dName = "Device_{}".format(device)
    dName = Device(dName)
    dDir.append(dName)

for i in range(0,itemOfDevices):
    seed = random()
    if (seed <= 0.33):
        type = "Lodowka"
    elif (seed >= 0.66):
        type = "Ladowarka"
    else:
        type = "Komputer"
    dDir[i].set_type(type)


for i in range(0,itemOfDevices):
    print(dDir[i].id)