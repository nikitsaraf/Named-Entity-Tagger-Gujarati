#!/usr/bin/env python

"""
A feature extractor for chunking.
Copyright 2010,2011 Naoaki Okazaki.
"""

# Separator of field values.
separator = ' '

# Field names of the input data.
fields = 'w y'

# Attribute templates.
templates = (
    (('w', -2), ),
    (('w', -1), ),
    (('w',  0), ),
    (('w',  1), ),
    (('w',  2), ),
    (('w', -1), ('w',  0)),
    (('w',  0), ('w',  1)),
    (('suf',0), ),
    (('pref',0), ),
    (('len',0), ),
    (('fir',0), ),
    )


import crfutils
def observation(v,c):
	#if len(v['w'][-3:]) == 3:	
	a = v['w'].decode('utf-8')	
	v['suf'] = a[-3:].encode('utf-8')
	#else:
	#	v['suf'] = ''
	#if len(v['w'][0:3]) == 3:	
	v['pref'] = a[0:3].encode('utf-8')
	#else:
	#	v['pref'] = ''	
	if len(a) <= 3:
		v['len'] = '1'
	else:
		v['len'] = '0'
	if c == 0:
		v['fir'] = '1'
	else:
		v['fir'] = '0'
			
def feature_extractor(X):
    
    c = 0
    for x in X:
        observation(x,c)
        c = c +1        

    # Apply attribute templates to obtain features (in fact, attributes)
    crfutils.apply_templates(X, templates)
    if X:
	# Append BOS and EOS features manually
        X[0]['F'].append('__BOS__')     # BOS feature
        X[-1]['F'].append('__EOS__')    # EOS feature

if __name__ == '__main__':
    crfutils.main(feature_extractor, fields=fields, sep=separator)
