import re

def rep1(m):
	return '</ENAMEX>'

def rep2(m):
	return '</ENAMEX> '

fr = open('1.xml','rb')
fw = open('7.xml','wb')

for line in fr:
	in_text = re.sub(r'&lt;','<',line)
	in_text = re.sub(r'&gt;','>',in_text)
	in_text = re.sub(r'</ENAMEX> ',rep1,in_text)
	in_text = re.sub(r'</ENAMEX> ',rep1,in_text)
	in_text = re.sub(r'</ENAMEX>',rep2,in_text)
		
	s_list = list(in_text)
	i,j = 0,0
	
	while i < len(s_list):
		# iterate until a left-angle bracket is found
		if s_list[i] == '<':
			while s_list[i] != '>':
				# pop everything from the the left-angle bracket until the right-angle bracket
				s_list.pop(i)
				
			# pops the right-angle bracket, too
			s_list.pop(i)
		else:
			i=i+1
			
	# convert the list back into text
	join_char=''
	s = join_char.join(s_list)

	fw.write(s)


fr.close()
fw.close()	

