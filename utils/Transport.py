import socket
import pickle
import json

from utils.utils import Employee


class TransportListener(object):
    def __init__(self, node_location, neighbours, empLocation):
        self.empLocation = empLocation
        self.neighbours = neighbours
        self.socket = socket.socket()
        self.node_location = node_location
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.node_location.get_tuple())

    def listen(self):
        self.socket.listen(1)
        try:
            while True:
                client_sock, client_address = self.socket.accept()
                self.processRequest(client_sock)
        except socket.error as err:
            print('Socket error', err.args[1])

    def processRequest(self, client_sock):
        employees = json.loads(open(self.empLocation).read())['employees']

        caller = client_sock.recv(256)
        print('Received transport request from ', caller)
        # print('My neighbours are: ', self.neighbours)
        if caller == b'client':
            for neighbour in self.neighbours:
                print('Started a new transport client for ', neighbour)
                transClient = TransportClient()
                transClient.setLocation(neighbour.get_tuple())
                new_employees = transClient.getEmployees(b'maven')
                for employee in new_employees:
                    if employee not in employees:
                        employees.append(employee)
                # employees += new_employees
            em = Employee()
            print(employees[0])
            new_employees = [em.from_dict(emp) for emp in employees]
            pickled_data = pickle.dumps(em.list_to_xml_string(new_employees))
        else:
            pickled_data = pickle.dumps(employees)

        client_sock.send(pickled_data)
        client_sock.close()


class TransportClient(object):
    def __init__(self):
        self.location = None
        self.socket = socket.socket()

    def setLocation(self, location):
        self.location = location

    def getEmployees(self, caller):
        self.socket.connect(self.location)
        self.socket.send(caller)
        new_data = self.socket.recv(1024)
        data = None

        while new_data:
            if data:
                data += new_data
            else:
                data = new_data
            new_data = self.socket.recv(1024)
            if not new_data: break
        # print('here')

        return pickle.loads(data)
