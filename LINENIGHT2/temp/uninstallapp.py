#!/usr/bin/python
#! -*- coding:utf-8-*-
import os
import sys,time
import subprocess
def executecmd():
	s=subprocess.Popen('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe devices',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	result=s.stdout.readlines()
	result=filter(lambda b:b!='',map(lambda a:a.strip('\r\n'),result))
	checkresult=filter(lambda a:a.startswith('127.0.0.1'),result)
	return checkresult
fromid,endid=sys.argv[1:]
try:
	fromid=int(fromid)
	endid=int(endid)
	if fromid>endid:
		raise Exception()
except Exception,e:
	print 'invalid input.'
	sys.exit(1)
################start devices##############################
for i in xrange(fromid,endid+1):
	print 'starting device <MEmu_%d>.....---......'%(i)
	subprocess.call(['MEmuConsole.exe', 'MEmu_%d'%i],shell=True)
	print '='*30
	for ii in xrange(1,31):
		sys.stdout.write('-')
		time.sleep(1)
	print
	checkresult=executecmd()
	print checkresult
	while checkresult==[] or len(checkresult)!=1:
		print 'some device is down or more'
		print 'Wait to restarting....'
		for x in xrange(5):
			sys.stdout.write('---')
			time.sleep(1)
		print
		os.system('D:\\david\\LINENIGHT2\\execute\\stopxiaoyao.bat')
		time.sleep(3)
		print 'starting device <MEmu_%d>....+++.......%d'%(i,i)
		subprocess.call(['MEmuConsole.exe', 'MEmu_%d'%i],shell=True)
		###############poweron nterval time
		print '='*30
		for ii in xrange(1,31):
			sys.stdout.write('-')
			time.sleep(1)
		print
		checkresult=executecmd()
		continue
	##############################################
	iddevice={i:checkresult[0].split('\t')[0]}
	###########push file#############################s
	print 'Device:[%s]'%iddevice
	for ids,device in iddevice.items():
		print 'uninstalling TongXunLu...'
		os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s uninstall com.ceynweining.view.activity'%device)
		time.sleep(2)
		print 'uninstalling 1Mobile...'
		os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s uninstall me.onemobile.android'%device)
		time.sleep(2)
		print 'uninstalling TaiBackup...'
		os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s uninstall com.keramidas.TitaniumBackup'%device)
		time.sleep(2)
	os.system('D:\\david\\LINENIGHT2\\execute\\stopxiaoyao.bat')
	time.sleep(2)
print 'Finished in [%s]'%(time.ctime())
