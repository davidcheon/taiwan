#!/usr/bin/python
#! -*- coding:utf-8-*-
import os
import sys,time
import subprocess
import urllib2
import threading
import pyscreenshot
def executecmd():
	s=subprocess.Popen('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe devices',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	result=s.stdout.readlines()
	result=filter(lambda b:b!='',map(lambda a:a.strip('\r\n'),result))
	checkresult=filter(lambda a:a.startswith('127.0.0.1'),result)
	return checkresult
def executesh(device,ids):
	subprocess.call('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell sh %s %s %d'%(device,'/sdcard/Download/Execute/loadphonenumbers.sh',device,ids),shell=True)
fromid,endid=sys.argv[1:]
try:
	fromid=int(fromid)
	endid=int(endid)
	if fromid>endid:
		raise Exception()
except Exception,e:
	print 'invalid start or end id'
	sys.exit(1)
################start devices##############################
tmpcount=0
for i in xrange(fromid,endid+1):
	print 'starting device <MEmu_%d>...........%d'%(i,i)
	print 'changing IP.....'
	#urllib2.urlopen('http://192.168.0.1/Status/wan_button_action.asp?connect=false')
	os.system('rasdial /disconnect')
	time.sleep(5)
	subprocess.call(['MEmuConsole.exe', 'MEmu_%d'%i],shell=True)
	#if tmpcount % devices ==0 or i==endid:
		###########start execute started devices################
	print '='*40
	for ii in xrange(1,40):
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
		os.system('D:\\david\\LINENIGHT\\execute\\stopxiaoyao.bat')
		time.sleep(3)
		print 'starting device <MEmu_%d>....+++.......%d'%(i,i)
		subprocess.call(['MEmuConsole.exe', 'MEmu_%d'%i],shell=True)
		###############poweron nterval time
		print '='*35
		for ii in xrange(1,35):
			sys.stdout.write('-')
			time.sleep(1)
		print
		checkresult=executecmd()
		continue
	tmpcount+=1
	##########################
	iddevice={i:checkresult[0].split('\t')[0]}
	###########push file#############################s
	print iddevice
	print '--------%d : MEmu_%d----------'%(tmpcount,i)
	source='D:\\david\\LINENIGHT\\scripts\\loadphonenumbers.sh'
	dst='/sdcard/Download/Execute'
	for ids,device in iddevice.items():
		os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\"[ ! -d /sdcard/Download/Execute ] && mkdir -p /sdcard/Download/Execute\"'))
		os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\" [ ! -d /sdcard/Download/AAAA ] && mkdir -p /sdcard/Download/AAAA\"'))
		os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\"[ ! -d /sdcard/Download/xls ] && mkdir -p /sdcard/Download/xls\"'))
		print 'cleaning all xls files in /sdcard/Download/xls and /sdcard/Download/AAAA'
		os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\"rm -rf  /sdcard/Download/xls/*\"'))
		os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\"rm -rf /sdcard/Download/AAAA/*\"'))
		print 'pushing files<%s> to %s.......'%('D:\\david\\LINENIGHT\\xls\\%d'%ids,'/sdcard/Download/xls')
		os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s push %s %s'%(device,'D:\\david\\LINENIGHT\\xls\\%d'%ids,'/sdcard/Download/xls'))
		cmd='D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s push %s %s'%(device,source,dst)
		print 'pushing file<%s> to MEmu_%d....'%(source,ids)
		print 'stopping market app in MEmu_%d....'%(ids)
		os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell am force-stop com.microvirt.market'%(device))
		time.sleep(2)
		print 'stopping guide app in MEmu_%d.....'%ids
		os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell am force-stop com.microvirt.guide'%device)
		time.sleep(2)
		os.system(cmd)
		print 'executing file<%s/loadphonenumbers.sh> in MEmu_%d....'%(dst,ids)
		
		t=threading.Thread(target=executesh,args=(device,ids))
		t.start()
		###########start execute sh interval time#####################
		time.sleep(3)
		os.system('del /F /S /Q D:\\david\\LINENIGHT\\xls\\%s'%ids)
		time.sleep(1)


		##########wait and stop and change ip################
	time.sleep(1110)
	try:
		print '<MEmu_%d> start grabing whole screen....'%(i)
		im=pyscreenshot.grab()
		print 'grab succeed.'
		print '<MEmu_%d> start saving image MEmu_%d.jpg...'%(i,i)
		im.save('D:\\david\\LINENIGHT\\screenshot\\MEmu_%d.jpg'%i,'jpeg')
		print 'image <MEmu_%d.jpg> saved succeed.'%i
	except:
		print '<MEmu_%d> grab or save failed...'%i
	print '<MEmu_%d> finished in [%s]'%(i,time.ctime())
#	print 'changing IP.....'
	#urllib2.urlopen('http://192.168.0.1/Status/wan_button_action.asp?connect=false')
#	os.system('rasdial /disconnect')
#	time.sleep(10)
	os.system('D:\\david\\LINENIGHT\\execute\\stopxiaoyao.bat')
	time.sleep(6)
print 'finished in [%s]'%time.ctime()
