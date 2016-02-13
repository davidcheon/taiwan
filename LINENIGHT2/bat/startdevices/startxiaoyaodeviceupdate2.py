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
import signal
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
	global monitorstatus
	while monitorstatus:
		time.sleep(600)
		results=executecmd()
		if len(results)==1:
			first=results[0]
			time.sleep(2000)
			results=executecmd()
			if len(results)==1:
				second=results[0]
				if first==second:
					print 'The device<%s> is Down.'%first
					os.system('D:\\david\\LINENIGHT2\\execute\\stopxiaoyao.bat')
#def handler(signum,frame):
#	global monitorstatus
#	monitorstatus=False
#	print 'received a signal %d,monitorstatus:%d'%(signum,monitorstatus)
#monitorstatus=True
#signal.signal(signal.SIGINT,handler)
#signal.signal(signal.SIGTERM,handler)
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
		print '<%d Time>starting device <MEmu_%d>.....---......%d'%(t,i,i)
		while 1:
			print 'changing IP.....'
			os.system('rasdial /disconnect')
			time.sleep(2)
			os.system('rasdial %s %s %s'%(network,netid,netpwd))
			time.sleep(2)
			if checknet():break
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
		tmpcount+=1
		###############start monitor###########################
	#	mthr=threading.Thread(target=startmonitor)
	#	mthr.start()
		##############################################
		iddevice={i:checkresult[0].split('\t')[0]}
		###########push file#############################s
		print 'Device:[%s]'%iddevice
		print '<%d Time>--------%d : MEmu_%d----------'%(t,tmpcount,i)
		source='D:\\david\\LINENIGHT2\\scripts\\loadphonenumbers.sh'
		dst='/sdcard/Download/Execute'
		for ids,device in iddevice.items():
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\"[ ! -d /sdcard/Download/Execute ] && mkdir -p /sdcard/Download/Execute\"'))
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\" [ ! -d /sdcard/Download/AAAA/%d/%d ] && mkdir -p /sdcard/Download/AAAA/%d/%d\"'%(t,ids,t,ids)))
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\"[ ! -d /sdcard/Download/xls/%d/%d ] && mkdir -p /sdcard/Download/xls/%d/%d\"'%(t,ids,t,ids)))
			print '<%d Time>Cleaning all xls files in /sdcard/Download/xls/%d/%d and /sdcard/Download/AAAA/%d/%d of MEmu_%d.'%(t,t,ids,t,ids,i)
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\"rm -rf  /sdcard/Download/xls/%d/%d/*\"'%(t,ids)))
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\"rm -rf /sdcard/Download/AAAA/%d/%d/*\"'%(t,ids)))
			#####################localcomputer/xls/times/computerID/contactsfolder/*.xls################
			localxlsfiles='D:\\david\\LINENIGHT2\\xls\\%d\\*-%d'%(t,ids)
			print '<%d Time>Pushing files<%s> to %s.......'%(t,localxlsfiles,'/sdcard/Download/xls/%d/%d'%(t,ids))
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s push %s %s'%(device,localxlsfiles,'/sdcard/Download/xls/%d/%d'%(t,ids)))
			cmd='D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s push %s %s'%(device,source,dst)
			print '<%d Time>Pushing execute file<%s> to MEmu_%d....'%(t,source,ids)
			print '<%d Time>Stopping market app in MEmu_%d....'%(t,ids)
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell am force-stop com.microvirt.market'%(device))
			time.sleep(2)
			print '<%d Time>Stopping guide app in MEmu_%d.....'%(t,ids)
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell am force-stop com.microvirt.guide'%device)
			time.sleep(2)
			os.system(cmd)
			print '<%d Time>Executing file<%s/loadphonenumbers.sh> in MEmu_%d....'%(t,dst,ids)
		
			#thr=threading.Thread(target=executesh,args=(device,ids,t))
			#thr.start()
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell sh %s %s %d %d %d %d %d'%(device,'/sdcard/Download/Execute/loadphonenumbers.sh',device,ids,t,myapp_delete_time,myapp_load_time,line_tongbu_time))
			###########start execute sh interval time#####################
			#os.system('del /F /S /Q D:\\david\\LINENIGHT\\xls\\%d\\%d\\*%d'%(t,ids,ids))
			#time.sleep(1)


			##########wait and stop and change ip################
		#time.sleep(1120)
		try:
			os.system('mkdir D:\\david\\LINENIGHT2\\screenshot\\%d'%t)
			print '<%d Time> MEmu_%d start grabing whole screen....'%(t,i)
			im=pyscreenshot.grab()
			print '<%d Time>Grab succeed.'%t
			print '<%d Time> MEmu_%d start saving image MEmu_%d.jpg...'%(t,i,i)
			im.save('D:\\david\\LINENIGHT2\\screenshot\\%d\\MEmu_%d.jpg'%(t,i),'jpeg')
			print '<%d Time>Image <MEmu_%d.jpg> saved succeed.'%(t,i)
		except:
			print '<%d Time>MEmu_%d grab or save failed...'%(t,i)
		print '<%d Time>MEmu_%d finished in [%s]'%(t,i,time.ctime())

		os.system('D:\\david\\LINENIGHT2\\execute\\stopxiaoyao.bat')
		time.sleep(6)
	print '<%d Time>Finished in [%s]'%(t,time.ctime())
