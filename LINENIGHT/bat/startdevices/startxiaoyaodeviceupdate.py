#!/usr/bin/python
#! -*- coding:utf-8-*-
import os
import sys,time
import subprocess
import threading
def executecmd():
	s=subprocess.Popen('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe devices',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	result=s.stdout.readlines()
	result=filter(lambda b:b!='',map(lambda a:a.strip('\r\n'),result))
	checkresult=filter(lambda a:a.startswith('127.0.0.1'),result)
	return checkresult
def executesh(device):
	subprocess.call('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell sh %s %s'%(device,'/sdcard/Download/Execute/loadphonenumbers.sh',device),shell=True)
fromid,endid,devices=sys.argv[1:]
try:
	fromid=int(fromid)
	endid=int(endid)
	devices=int(devices)
	if fromid>endid:
		raise Exception()
	if devices>endid-fromid+1:
		devices=endid-fromid+1
except Exception,e:
	print 'invalid start or end id'
	sys.exit(1)
################start devices##############################
tmpcount=0
for i in xrange(fromid,endid+1):
	print 'starting device <MEmu_%d>...........%d'%(i,i)
	subprocess.call(['MEmuConsole.exe', 'MEmu_%d'%i],shell=True)
	tmpcount+=1
	time.sleep(20)
	if tmpcount % devices ==0 or i==endid:
		###########start execute started devices################
		print '='*20
		for ii in xrange(1,20):
			sys.stdout.write('-')
			time.sleep(1)
		print
		checkresult=executecmd()
		print checkresult,devices
		while True:
			if i==endid:
				if devices==1 and len(checkresult)==1:
					break
				if tmpcount%devices==0 and len(checkresult)==devices:
					break
				if len(checkresult)==devices:
					break
				if checkresult!=[] and len(checkresult)==(endid-fromid+1)%devices:
					break
				else:
					print 'some device is down'
					print 'Wait to restarting....'
					for x in xrange(15):
						sys.stdout.write('--')
					print
					os.system('D:\\david\\LINENIGHT\\execute\\stopxiaoyao.bat')
					time.sleep(3)
					if (endid-fromid+1)%devices==0:
						tmp=endid-devices+1
					else:
						tmp=endid-(endid-fromid+1)%devices+1
					print tmp
					for a in xrange(tmp,endid+1):
						print 'starting device <MEmu_%d>....+++.......%d'%(a,a)
						subprocess.call(['MEmuConsole.exe', 'MEmu_%d'%a],shell=True)
						###############poweron nterval time
						time.sleep(20)
					print '='*20
					for ii in xrange(1,20):
						sys.stdout.write('-')
						time.sleep(1)
					print
					checkresult=executecmd()
					time.sleep(15)
					continue
			if len(checkresult)!=devices:
				print 'some device is down.'
				print 'Wait to restarting....'
				for x in xrange(10):
					sys.stdout.write('--')
					time.sleep(1)
				print
				os.system('D:\\david\\LINENIGHT\\execute\\stopxiaoyao.bat')
				time.sleep(3)
				for b in xrange(i-devices+1,i+1):
					print 'starting device <MEmu_%d>..---......%d'%(b,b)
					subprocess.call(['MEmuConsole.exe', 'MEmu_%d'%b],shell=True)
					##########poweron interval time#########
					time.sleep(20)
				print '='*20
				for ii in xrange(1,20):
					sys.stdout.write('-')
					time.sleep(1)
				print
				checkresult=executecmd()
				continue
			else:
				break
		ipport=map(lambda a:a.split('\t')[0],checkresult)
		ipport.sort()
		if i<endid:
			iddevice=dict(zip(xrange(i+1,i+1+devices),ipport))
		else:
			if (endid-fromid+1)%devices!=0:
				iddevice=dict(zip(xrange(endid-(endid-fromid+1)%devices+1,endid+1),ipport))
			else:
				iddevice=dict(zip(xrange(endid-devices+1,endid+1),ipport))
		###########push file#############################s
		print iddevice
		source='D:\\david\\LINENIGHT\\scripts\\loadphonenumbers.sh'
		dst='/sdcard/Download/Execute'
		for ids,device in iddevice.items():
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\"[ ! -d /sdcard/Download/Execute ] && mkdir -p /sdcard/Download/Execute\"'))
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\" [ ! -d /sdcard/Download/AAAA ] && mkdir -p /sdcard/Download/AAAA\"'))
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell su -c %s'%(device,'\"[ ! -d /sdcard/Download/xls ] && mkdir -p /sdcard/Download/xls\"'))
			print 'pushing files<%s> to %s.......'%('D:\\david\\LINENIGHT\\xls\\%d'%ids,'/sdcard/Download/xls')
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s push %s %s'%(device,'D:\\david\\LINENIGHT\\xls\\%d'%ids,'/sdcard/Download/xls'))
			cmd='D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s push %s %s'%(device,source,dst)
			print 'pushing file<%s> to %s....'%(source,device)
			print 'stopping market app in %s....'%(device)
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell am force-stop com.microvirt.market'%(device))
			time.sleep(2)
			print 'stopping guide app in %s.....'%device
			os.system('D:\\"Program Files"\\Microvirt\\MEmu\\adb.exe -s %s shell am force-stop com.microvirt.guide'%device)
			time.sleep(2)
			os.system(cmd)
			print 'executing file<%s/loadphonenumbers.sh> in %s....'%(dst,device)
		
			t=threading.Thread(target=executesh,args=(device,))
			t.start()
			###########start execute sh interval time#####################
			time.sleep(135)
			os.system('del /F /S /Q D:\\david\\LINENIGHT\\xls\\%s'%ids)
			time.sleep(1)


		##########wait and stop and change ip################
		time.sleep(700)
		os.system('D:\\david\\LINENIGHT\\execute\\stopxiaoyao.bat')
		time.sleep(5)
