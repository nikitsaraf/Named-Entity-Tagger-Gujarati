import xml.etree.ElementTree as ET
import sys

def prepareDictionary(f):
	tree = ET.parse(f)
	c = 0
	for elem in tree.iter(tag='ENAMEX'):
		a = elem.attrib
		l = a.values()
		s = ''.join(l)
		c = c + 1
	print c			
	

g = open(sys.argv[1],'rb')

prepareDictionary(g)
