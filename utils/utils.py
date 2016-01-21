from xml.etree.ElementTree import Element, tostring, fromstring
import xmljson


class Employee(object):
    def __init__(self, name='name1', surname='surname1', salary=200.0, department='departemnt1'):
        self.name = name
        self.surname = surname
        self.department = department
        self.salary = salary

    def from_dict(self, d):
        try:
            emp = Employee(d['name'], d['surname'], d['salary'], d['department'])
            return emp
        except KeyError as err:
            print(err)
            return None

    def to_xml_string(self):
        elem = Element('employee')
        for key, val in self.__dict__.items():
            child = Element(key)
            if key == 'salary':
                val = str(val)
            child.text = val
            elem.append(child)
        return tostring(elem)

    def from_xml_string(self, xml_string):
        xml = fromstring(xml_string)
        d = xmljson.yahoo.data(xml)
        tmp = self.from_dict(dict(d['employee']))
        tmp.salary = float(tmp.salary)
        return tmp

    def list_to_xml_string(self, list_emp):
        root = Element('employees')
        for emp in list_emp:
            elem = Element('employee')
            for key, val in emp.__dict__.items():
                child = Element(key)
                if key == 'salary':
                    val = str(val)
                child.text = val
                elem.append(child)
            root.append(elem)
        return tostring(root)

    def xml_string_to_list(self, xml_string):
        xml = fromstring(xml_string)
        d = xmljson.yahoo.data(xml)
        # print(d['employees']['employee'])
        tmp = list(map((lambda x: self.from_dict(x)), d['employees']['employee']))
        for x in tmp:
            x.salary = float(x.salary)
        return tmp

    def __repr__(self):
        return str(self.name) + ' ' + str(self.surname) + ' ' + str(self.department) + ' ' + str(self.salary)

    def __str__(self):
        return str(self.name) + ' ' + str(self.surname) + ' ' + str(self.department) + ' ' + str(self.salary)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                self.department == other.department and self.name == other.name
            and self.surname == other.surname and self.salary == other.salary)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Location(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def __repr__(self):
        return str(self.ip) + str(self.port)

    def __str__(self):
        return str(self.ip) + ' ' + str(self.port)

    def get_tuple(self):
        touple = (self.ip, self.port)
        return touple
