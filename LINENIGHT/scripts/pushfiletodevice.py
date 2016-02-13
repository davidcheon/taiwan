#!/usr/bin/python
#!-*- coding:utf-8 -*-
import subprocess
import sys,os,time
def executecmd():
	cmddevices='D:\\download\\Genymotion\\tools\\adb.exe devices'
	p=subprocess.Popen	(cmddevices,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	result=p.stdout.readlines()
	result=filter(lambda b:b!='',map(lambda a:a.strip('\r\n'),result))
	checkresult=filter(lambda a:a.startswith('192.168.'),result)
	return checkresult
#################getdevices####################################################
checkresult=executecmd()
startid,endid=sys.argv[1:]
try:
	startid=int(startid)
	endid=int(endid)
except Exception,e:
	print 'invalid start or end'
	sys.exit(3)
while True:
	if len(checkresult)!=endid-startid+1:
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
iddevice=dict(zip(xrange(startid,endid+1),ipport))
#####################pushfile#####################################################
source='D:\\david\\LINENIGHT\\scripts\\loadphonenumbers.sh'
dst='/sdcard/Download/Execute'
for ids,device in iddevice.items():
	os.system('D:\\download\\Genymotion\\tools\\adb.exe -s %s shell su -c %s'%(device,'\"mkdir -p /sdcard/Download/Execute\"'))
	os.system('D:\\download\\Genymotion\\tools\\adb.exe -s %s shell su -c %s'%(device,'\"mkdir -p /sdcard/Download/AAAA\"'))
	os.system('D:\\download\\Genymotion\\tools\\adb.exe -s %s shell su -c %s'%(device,'\"mkdir -p /sdcard/Download/xls\"'))
	os.system('D:\\download\\Genymotion\\tools\\adb.exe -s %s push %s %s'%(device,'D:\\david\\LINENIGHT\\xls\\%d'%ids,'/sdcard/Download/xls'))
	print 'pushing files <%s> to %s.....'%('D:\\david\\LINENIGHT\\xls\\%d'%ids,'/sdcard/Download/xls')
	cmd='D:\\download\\Genymotion\\tools\\adb.exe -s %s push %s %s'%(device,source,dst)
	print 'pushing file<%s> to %s....'%(source,device)
	os.system(cmd)
	print 'executing file<%s/loadphonenumbers.sh> in %s....'%(dst,device)
	os.system('D:\\download\\Genymotion\\tools\\adb.exe -s %s shell sh %s %s'%(device,'/sdcard/Download/Execute/loadphonenumbers.sh',device))
	os.system('del /F /S /Q D:\\david\\LINENIGHT\\xls\\%d'%ids)
	time.sleep(1)
