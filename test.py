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

emp1 = emp
emp2 = Employee(name='name2', surname='surname2', salary='2', department='department2')

emps = [emp1, emp2]

# my_str = ''
#
# for e in emps:
#     my_str += e.to_xml_string().decode()
#
# print(my_str)

print(Employee().list_to_xml_string(emps))

