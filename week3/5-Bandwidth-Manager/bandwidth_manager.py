from heapq import heappush, heappop
import itertools

class BandwidthManager:

    global container, counter
    container = []
    counter = itertools.count()
        
    def __init__(self, instr):
        self.instr = instr
        if ' ' in instr:
            # set priority to the different protocols
            split = instr.split()
            if split[1] == 'ICMP':
                split[1] = 0
            elif split[1] == 'UDP':
                split[1] = 1
            elif split[1] == 'RTM':
                split[1] = 2
            elif split[1] == 'IGMP':
                split[1] = 3
            elif split[1] == 'DNS':
                split[1] = 4
            elif split[1] == 'TCP':
                split[1] = 5
            BandwidthManager.rcv(self, split[1], split[2])
        else:
            print (BandwidthManager.send(self))

#receives a packet with specified protocol and payload
    def rcv(self, protocol, payload):
        global container, count
        count = next(counter) 
        current = [protocol, count, payload]
        heappush(container, current)

#returns the payload of the packet which should be sent
    def send(self):
        if len(container) > 0:
            return heappop(container)[2]
        else:
            return 'Nothing to send!'
