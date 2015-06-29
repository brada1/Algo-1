# this script checks if bandwidth_manager_test.py is callable externally and if it works well
import sys, os
if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from bandwidth_manager import BandwidthManager

# test example
##BandwidthManager('rcv UDP zxchzrkljhklzrjlkhklzr')
##BandwidthManager('rcv TCP ghljkajklhgjklare')
##BandwidthManager('rcv ICMP ping87.129.54.123')
##BandwidthManager('send')
##BandwidthManager('send')
##BandwidthManager('rcv DNS maps.google.com')
##BandwidthManager('send')
##BandwidthManager('rcv TCP aejkgjkaegaegae')
##BandwidthManager('send')
##BandwidthManager('send')
##BandwidthManager('send')

# test any
while True:
    s = input('')
    if s == 'exit':
        break
    else:
        BandwidthManager(s)
