#!/usr/bin/python
#! -*- coding:utf-8-*-
import os
import sys,time
import subprocess
import urllib2
import threading
import pyscreenshot
import ConfigParser
import commands
nets={
	'1to8':['75902856@hinet.net','wnykvscy'],
	'9to16':['75902854@hinet.net','thnqrvnx'],
	'17to24':['75902855@hinet.net','cqedqvna']
}
def executecmd():
	s=subprocess.Popen('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe devices',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	result=s.stdout.readlines()
	result=filter(lambda b:b!='',map(lambda a:a.strip('\r\n'),result))
	checkresult=filter(lambda a:a.startswith('127.0.0.1'),result)
	return checkresult
def executesh(device,ids,t):
	subprocess.call('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell sh %s %s %d %d'%(device,'/sdcard/Download/Execute/loadphonenumbers.sh',device,ids,t),shell=True)
def checknet():
	cmd='ping www.baidu.com -n 1'
	s=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	result=s.stdout.readlines()
	return len(result)>1
def startdevice(id):
	os.system('memuconsole MEmu_%d'%id)
def startmonitor():
	while 1:
		print status
		time.sleep(5)

fromid,endid,starttime,endtime,network=sys.argv[1:]
while 1:
	network=network.strip('\r\n ')
	if not nets.has_key(network):
		network=raw_input('network is wrong,\nplease enter the network(1to8,9to16,17to24):')
		continue
	else:
		netid=nets[network][0]
		netpwd=nets[network][1]
		break
try:
	fromid=int(fromid)
	endid=int(endid)
	starttime=int(starttime)
	endtime=int(endtime)
	flag=False
	if fromid>endid or starttime>endtime:
		raise Exception('invalid input')
	cf=ConfigParser.ConfigParser()
	#cf.read('D:\\david\\LINENIGHT2\\config\\setting.conf')
	#emulator_start_time=cf.getint('emulator_setting','waiting_start_time')
	#myapp_delete_time=cf.getint('myapp_setting','delete_time')
	#myapp_load_time=cf.getint('myapp_setting','load_time')
	#line_tongbu_time=cf.getint('line_setting','tongbu_time')
except Exception,e:
	print e
	sys.exit(1)
################start devices##############################
for t in xrange(starttime,endtime+1):
	print 'Executing <%d time>......'%t
	tmpcount=0
	for i in xrange(fromid,endid+1):
		status=False
		print '<%d Time>starting device <MEmu_%d>.....---......%d'%(t,i,i)
		print 'changing IP.....'
		time.sleep(2)
		#subprocess.call(['MEmuConsole.exe', 'MEmu_%d'%i],shell=True)
	#	os.system('memuconsole MEmu_%d'%i)
		thr=threading.Thread(target=startdevice,args=(i,))
		thr.start()
		cf.read('D:\\david\\LINENIGHT2\\config\\setting.conf')
		emulator_start_time=cf.getint('emulator_setting','waiting_start_time')
		myapp_delete_time=cf.getint('myapp_setting','delete_time')
		myapp_load_time=cf.getint('myapp_setting','load_time')
		line_tongbu_time=cf.getint('line_setting','tongbu_time')
		#if tmpcount % devices ==0 or i==endid:
			###########start execute started devices################
		print '%s<WaitintTime:%d Second>%s'%('='*9,emulator_start_time,'='*9)
		print '='*emulator_start_time
		for ii in xrange(1,emulator_start_time+1):
			sys.stdout.write('-')
			time.sleep(1)
		print
		checkresult=executecmd()
		print checkresult
		while checkresult==[] or len(checkresult)!=1:
			print 'some device is down'
			print 'Wait to restarting....'
			for x in xrange(5):
				sys.stdout.write('---')
				time.sleep(1)
			print
			os.system('D:\\david\\LINENIGHT2\\execute\\stopxiaoyao.bat')
			time.sleep(3)
			print '<%d Time>starting device <MEmu_%d>....+++.......%d'%(t,i,i)
			#subprocess.call(['MEmuConsole.exe', 'MEmu_%d'%i],shell=True)
			thr2=threading.Thread(target=startdevice,args=(i,))
			thr2.start()
			print '%s<WaitintTime:%d Second>%s'%('='*9,emulator_start_time,'='*9)
			###############poweron nterval time
			print '='*emulator_start_time
			for ii in xrange(1,emulator_start_time+1):
				sys.stdout.write('=')
				time.sleep(1)
			print
			checkresult=executecmd()
			continue
		######################monitor#######################
		if not flag:
			mthr=threading.Thread(target=startmonitor)
			mthr.start()
			flag=True
		##############################################
		print 'waiting to change status'
		print '-'*30
		for x in xrange(30):
			sys.stdout.write('-')
			time.sleep(1)
		print
		status=True
		os.system('D:\\david\\LINENIGHT2\\execute\\stopxiaoyao.bat')
		time.sleep(6)
