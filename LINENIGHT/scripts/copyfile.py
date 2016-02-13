#!/usr/bin/python
#! -*- coding:utf-8 -*-
import sys
import os
import time
import subprocess
def showdevices(result):
	print '#'*15,'<',len(result),'>Devices','#'*15
	for r in result:
		print '%s%s'%(' '*10,r)
	print '#'*40
s=subprocess.Popen('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe devices',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
result=s.stdout.readlines()
result=filter(lambda a:a!='',map(lambda b:b.strip('\r\n'),result))
checkresult=filter(lambda a:a.startswith('127.0.0.1'),result)
checkresult=map(lambda a:a.split('\t')[0],checkresult)
if len(checkresult)<1:
	print 'no devices are on.'
	sys.exit(1)
else:
	src='D:\\Users\\poto'
	dst='/sdcard/Download/poto'
	mkdircmd='mkdir -p %s'%(dst)
	for i in range(0,len(checkresult)):
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c "%s"'%(checkresult[i],mkdircmd))
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s push %s %s'%(checkresult[i],src,dst))
			print '--'*20
			time.sleep(1.5)

showdevices(checkresult)	
