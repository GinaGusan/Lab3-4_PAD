import json, xmljson
from lxml.etree import tostring, fromstring, Element

from utils.utils import Employee


emp = Employee(name='name1', surname='surname1', salary='1', department='department1')
print(emp.to_xml_string())

# print(dict(Employee.from_xml(emp, emp.to_xml())['employee']))

print(Employee().from_xml_string(emp.to_xml_string()))

print(emp == Employee().from_xml_string(emp.to_xml_string()))

xml_string = emp.to_xml_string()

json_string = json.dumps(Employee().from_xml_string(xml_string).__dict__)

print(json_string)


