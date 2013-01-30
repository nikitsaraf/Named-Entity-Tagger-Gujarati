import xml.etree.ElementTree as ET
import pprint

def prepareDictionary(f):
	tree = ET.parse(f)
	dic = {}
	for elem in tree.iter(tag='ENAMEX'):
		a = elem.attrib
		l = a.values()
		s = ''.join(l)
		t = elem.text
		words = t.split()
		c = 0	
		for word in words:
			if c == 0:
				dic[word] = 'B'+'-'+s
			else:
				dic[word] = 'I'+'-'+s
			c = c + 1
		
	return dic
		

f = open('7.xml','rb');
g = open('1.xml','rb');
h = open('final2.txt','wb');

dic = prepareDictionary(g)


for line in f:
	words = line.split();
	for word in words:
		'''		
		c = 0		
		if word[-1] == '.':
			word = word[0:-1]
			c = 1
		'''		
		word = word.decode("utf-8")
		try:
			value = dic[word]
			word = word.encode('utf-8')
			s = word + ' ' + value + '\n'
		except KeyError:
			word = word.encode('utf-8')
			s = word + ' ' + 'O' + '\n'
		h.write(s)
		'''
		if c==1:
			s = '. O' + '\n\n'
			h.write(s)
		'''
	print line[-1]

