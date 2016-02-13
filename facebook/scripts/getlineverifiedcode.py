#!/usr/bin/python
import subprocess
import sys
import time
def getfiles(path,username,domain):
	cmd='ssh -p 5211 root@sendtea999.com "%s"'%"ls /var/mailbox/{0}/{1}/Maildir/{2}|sort -r".format(domain,username,path)
	sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	results=sp.stdout.readlines()
	rs=map(lambda a:a.strip('\r\n'),results)
	return rs
def getcode(cmd):	
	sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	results=sp.stdout.readlines()
	rs=map(lambda a:a.strip('\r\n\t'),results)
	return filter(lambda a:a!='',rs)
while 1:
	#username,domain=sys.argv[1:]
	email=raw_input('enter the email:')
	email=email.strip()
	params=email.split('@')
	if len(params)!=2:
		print 'invalid email.'
		continue
	username=params[0]
	domain=params[1]
	username=username.strip()
	domain=domain.strip()
	if username==''or domain=='':
		print 'invalid username or domain name.'
		continue
	path='new'
	files={}
	newfiles=getfiles(path,username,domain)
	if len(newfiles)>0:
		files['/var/mailbox/{0}/{1}/Maildir/{2}/'.format(domain,username,path)]=newfiles
	path='cur'
	curfiles=getfiles(path,username,domain)
	if len(curfiles)>0:
		files['/var/mailbox/{0}/{1}/Maildir/{2}/'.format(domain,username,path)]=curfiles
	filepaths=[]
	if files.has_key('/var/mailbox/{0}/{1}/Maildir/new/'.format(domain,username)):
		files['/var/mailbox/{0}/{1}/Maildir/new/'.format(domain,username)].sort(reverse=True)
		filepaths=map(lambda a:'/var/mailbox/{0}/{1}/Maildir/new/'.format(domain,username)+a,files['/var/mailbox/{0}/{1}/Maildir/new/'.format(domain,username)])
	if files.has_key('/var/mailbox/{0}/{1}/Maildir/cur/'.format(domain,username)):
		files['/var/mailbox/{0}/{1}/Maildir/cur/'.format(domain,username)].sort(reverse=True)
		filepaths=filepaths+map(lambda a:'/var/mailbox/{0}/{1}/Maildir/cur/'.format(domain,username)+a,files['/var/mailbox/{0}/{1}/Maildir/cur/'.format(domain,username)])
	print '---------------LINE--------------------------'
	for filename in filepaths[:5]:
		cmd='ssh -p 5211 root@sendtea999.com "%s"'%"grep -i -E 'verification code:|date:' %s"%filename
#		cmd='ssh -p 5211 root@sendtea999.com "%s"'%"sed -n '18,66p' %s"%filename
		rs=getcode(cmd)
		flag=False
		counter=0
		if len(rs)>=2:
			for r in rs:
				if r.startswith('Date:') or r.startswith('Verification code:'):
					counter+=1
			if counter==2:
				print rs[0]
				print rs[1]
			break
	print '---------------------over----------------------------'
	print
