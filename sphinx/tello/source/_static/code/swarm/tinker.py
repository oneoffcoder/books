import sys
from tello import *

manager = TelloManager()

# infos = manager.get_subnets()
# print(infos)
# print(SubnetInfo.flatten([info.get_ips() for info in infos]))

manager.find_avaliable_tello(1)