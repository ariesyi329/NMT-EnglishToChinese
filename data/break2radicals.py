#!/usr/bin/python

import sys
from cjklib import characterlookup

cjk = characterlookup.CharacterLookup('C')

def break2radicals(unic):
	
	radicals = True
	
	#check if there are residuals in characters (some characters are radicals themselves)
	try:
		cjk.getCharacterKangxiRadicalResidualStrokeCount(unic)
	except:
		radicals = False

	if radicals:
		radicals_list = []
		unic_radicals = cjk.getDecompositionEntries(unic)
		for unic_radical in unic_radicals[0]:
			if type(unic_radical) is tuple:
				radicals_list.append(unic_radical[0])
		return ' '.join(radicals_list)
	else:
		return unic


for line in sys.stdin:
	unic = line.decode('utf-8')
	unic = unic.strip()
	unic_list = unic.split(' ')
	unic_new = ' '.join(break2radicals(i).encode('utf-8') for i in unic_list)
	print unic_new

