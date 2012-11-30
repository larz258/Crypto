'''
Crypto - Substitution Cipher
Copyright 2012 Lars Schweighauser

This work is licensed under the Creative Commons 
Attribution-NonCommercial-ShareAlike 3.0 United States License. 
To view a copy of this license, 
visit http://creativecommons.org/licenses/by-nc-sa/3.0/us/ 
or send a letter to Creative Commons, 
444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
'''

import sys
import os
vers = str(sys.version)

if vers[0] == "2":

	if vers[2] == "7":
		os.system("python2.7 BIN/Crypto_Python2.py")
		
	else:
		print ("I don't support Python " + vers[0:5:1] + "\n")
		
elif vers[0] == "3":

	if vers[2] == "0":
		os.system("python3.0 BIN/Crypto_Python3.py")

	elif vers[2] == "3":
		os.system("python3.3 BIN/Crypto_Python3.py")

	else:
		print ("I don't support Python " + vers[0:5:1] + "\n")
		
else:
	print ("I don't support Python " + vers[0:5:1] + "\n")
