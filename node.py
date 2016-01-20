import sys, json

from utils.Discovery import DiscoveryListener
from utils.Transport import TransportListener
from utils.utils import Location


class Node(object):
    def __init__(self, config):
        data = json.loads(open(config).read())
        empLocation = data['empLocation']
        neighbs = data['neighbours']
        self.neighbours = []

        for port in neighbs:
            self.neighbours.append(Location('127.0.0.1', port))

        self.empLocation = empLocation
        self.groupLocation = Location('239.192.1.100', 50000)
        self.myLocation = Location('127.0.0.1', int(data['myLocation']))
        self.discoListener = DiscoveryListener()
        self.transListener = TransportListener(
            neighbours=self.neighbours,
            empLocation=self.empLocation,
            node_location=self.myLocation
        )

    def run(self):
        data = self.discoListener.listen(ip=self.groupLocation.ip, port=self.groupLocation.port)
        print('Received client location: ', data)
        self.discoListener.send(ip=data.ip, port=data.port, data=self.myLocation.get_tuple())

        print('Sent my location. Waiting for transport request')

        self.transListener.listen()


if __name__ == '__main__':
    args = sys.argv
    node = Node(args[1])
    node.run()
