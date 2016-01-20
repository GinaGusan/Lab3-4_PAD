import socket
import sys
import pickle

from utils.Discovery import DiscoveryClient
from utils.Transport import TransportClient
from utils.utils import Location, Employee


class Client(object):
    def __init__(self):
        self.discoClient = DiscoveryClient()
        self.transClient = TransportClient()
        self.myLocation = Location('127.0.0.1', 3456)
        self.groupLocation = Location('239.192.1.100', 50000)

    def run(self):
        self.discoClient.send(location=self.groupLocation.get_tuple(), data=self.myLocation)
        maven_location = self.discoClient.receive(ip=self.myLocation.ip, port=self.myLocation.port)
        print('First node is: ', maven_location)

        self.transClient.setLocation(maven_location)
        employees = self.transClient.getEmployees(b'client')

        print(len(employees))
        print(employees)

        # salaries = list(map((lambda x: x['Employee']['salary']), employees))
        # salaries2 = [x['Employee']['salary'] for x in employees]
        # print(salaries)
        # print(salaries2)

        # salary_avg = reduce(lambda x, y: x + y , salaries)


if __name__ == '__main__':
    client = Client()
    client.run()
