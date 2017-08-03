#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/30

import xml.etree.ElementTree as ET
import re

tree=ET.parse('c:\\plant_catalog.xml')
root=tree.getroot()
print(root.tag)


#查询
# for child in root:
#     print(child.tag,'*',child.attrib)
#     # for i in child:
#     #     print(i.tag,i.text)


#修改
# for node in root.findall('PLANT'):
#     # node.text = re.sub("\D", "", node.text)
#     rank=int(node.find('AVAILABILITY').text)
#     if rank > 50 :
#         root.remove(node)
#         #     new_AVAILABILITY=int(node.text)+1
# #     node.text=str(new_AVAILABILITY)
# #
# #
# tree.write('c:\\123.xml')


new_xml=ET.Element("namelist")
name=ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age=ET.SubElement(name,'age',attrib={"checked":"no"})
sex=ET.SubElement(name,"sex")

age.text="33"

name2=ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age=ET.SubElement(name2,'age',attrib={"checked":"no"})
sex=ET.SubElement(name2,"sex")

age.text="34"

et=ET.ElementTree(new_xml)
et.write("c:\\123.xml",encoding="utf-8",xml_declaration=True)