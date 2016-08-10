import sys
from xml.dom.minidom import parse


##########################################
##             XML Library              ##
##          Author: Jason Walsh         ##
##                                      ##
##########################################



def load_xml(s0): #load filename
	xmlFile = parse('Drivers.xml')
	return xmlFile
		
def xml_nodelist_pull_tag(s0,s1):#pull tagged element from nodelist
	list = s0.getElementsByTagName(s1)
	combine = ''
	if list.length > 0:
		for el in list:
			if el.hasChildNodes():
				if is_empty(el.childNodes[0].nodeValue) == False:
					if is_empty(combine) == False:
						combine+=','
					combine+=el.childNodes[0].nodeValue
	return combine
	
