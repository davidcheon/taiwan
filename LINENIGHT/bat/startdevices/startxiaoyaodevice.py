#!/usr/bin/python
#! -*- coding:utf-8-*-
import os
import sys,time
import subprocess
import threading
fromid,endid=sys.argv[1:]
try:
	fromid=int(fromid)
	endid=int(endid)
except Exception,e:
	print 'invalid start or end id'
	sys.exit(1)
################start devices##############################
for i in xrange(fromid,endid+1):
	print 'starting device <MEmu_%d>....'%i
	subprocess.call(['MEmuConsole.exe', 'MEmu_%d'%i],shell=True)
	time.sleep(5)
##############get decices##################
####waiting for device starting
time.sleep(35)
def executecmd():
	s=subprocess.Popen('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe devices',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	result=s.stdout.readlines()
	result=filter(lambda b:b!='',map(lambda a:a.strip('\r\n'),result))
	checkresult=filter(lambda a:a.startswith('127.0.0.1'),result)
	return checkresult
checkresult=executecmd()
while True:
	if len(checkresult)!=endid-fromid+1:
		print 'some device is down.'
		print 'Wait'
		for x in xrange(5):
			sys.stdout.write('--')
			time.sleep(1)
		print
		checkresult=executecmd()
	else:
		break
ipport=map(lambda a:a.split('\t')[0],checkresult)
ipport.sort()
iddevice=dict(zip(xrange(fromid,endid+1),ipport))
###########push file#############################
def executesh(device):
	subprocess.call('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell sh %s %s'%(device,'/sdcard/Download/Execute/loadphonenumbers.sh',device),shell=True)
source='D:\\david\\LINENIGHT\\scripts\\loadphonenumbers.sh'
dst='/sdcard/Download/Execute'
for ids,device in iddevice.items():
	os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\"[ ! -d /sdcard/Download/Execute ] && mkdir -p /sdcard/Download/Execute\"'))
	os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\" [ ! -d /sdcard/Download/AAAA ] && mkdir -p /sdcard/Download/AAAA\"'))
	os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\"[ ! -d /sdcard/Download/xls ] && mkdir -p /sdcard/Download/xls\"'))
	os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s push %s %s'%(device,'D:\\david\\LINENIGHT\\xls\\%s'%ids,'/sdcard/Download/xls'))
	cmd='D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s push %s %s'%(device,source,dst)
	print 'pushing file<%s> to %s....'%(source,device)
	os.system(cmd)
	print 'executing file<%s/loadphonenumbers.sh> in %s....'%(dst,device)
#	os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell sh %s %s'%(device,'/sdcard/Download/Execute/loadphonenumbers.sh',device))
	#subprocess.call('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell sh %s %s'%(device,'/sdcard/Download/Execute/loadphonenumbers.sh',device),shell=True)
	t=threading.Thread(target=executesh,args=(device,))
	t.start()
	time.sleep(5)
	os.system('del /F /S /Q D:\\david\\LINENIGHT\\xls\\%s'%ids)
	time.sleep(1)




