#!/usr/bin/python
import sys
import os
fromid,endid,filenames=sys.argv[1:]
try:
	fromid=int(fromid)
	endid=int(endid)
	filenames=filenames.split('+')
	if fromid>endid or fromid<1 or endid>26:
		raise Exception()
	if len(filenames)<1:
		raise Exception()
except:
	print 'invalid input'
	sys.exit(1)
for ip in xrange(fromid,endid+1):
	print '%s%d%s'%('='*15,ip,'='*15)
	for filename in filenames:
		toip='\\\\192.168.1.%d\\%s'%(ip+100,filename.replace(':',''))
		print 'Copying %s to %s'%(filename,toip)
		os.system('xcopy /Y /E /I  %s %s'%(filename,toip))
		print '-'*40
	print
	
