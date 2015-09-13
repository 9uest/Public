#!/usr/bin/env python
#coding:utf-8

# from subprocess import Popen, PIPE, call
import sys,re,os,socket
reload(sys)
sys.setdefaultencoding('utf-8')

def host(filename):
	'''从文件中获取局域网主机名'''
	hostlist = []
	host = open(sys.argv[1])
	f = host.readlines()
	regex = re.compile(r'\\')
	for line in f:
		if regex.findall(line):
			hostlist.append(line.strip())
	host.close()
	return hostlist
def connect(hostlist):
	'''ipc连接并列出C盘'''
	num = 0
	Truehost = {}
	for i in hostlist:
		hostname = i[2:]		
		'''获取主机名全部ip'''
		try:
			host1, host2, ip = socket.gethostbyname_ex(hostname)
			ip = " ".join(ip)
		except:
			ip = " "	
		num = num + 1
		print "####################[ %s ]#######################" %num
		print " "
		print "HOST: [%s]" %i
		print "IP:  [%s]" %ip
		print " "
		con = "net use %s\ipc$ %s /user:%s" %(i,sys.argv[3],sys.argv[2])
		print con
		Dir = "dir %s\c$" %i
		Del = "net use %s /del /y" %i
		print "Connection %s ..." %i
		try:
			con = os.popen(con)
			if  con.readlines():
				print "[+] Ipc Connection Success !!!"
				
				print "Dir Drive [c]"
				Dirlist = os.popen(Dir)
				if  Dirlist.readlines():
					print "[+] Drive C  ACCESS !!!"
					print "Del %s connect ..." %i
					Truehost[i] = ip
					os.popen(Del)
				else:
					print "[-] Drive C  Deny"
			else:
				print "Ipc Connection failure"
		except:
			print "Error"
		print " "
	'''打印 成功连接主机'''
	print "Host %s" %len(hostlist)
	print "All Connection   Host [%s]" %len(Truehost)
	print " "
	for Alivehost in Truehost:
		print str(Alivehost) +"    "+ Truehost[Alivehost]
if __name__ == '__main__':

	if len(sys.argv) == 4:
		hostlist = host(sys.argv[1])
		print "Host [%s]" %len(hostlist)
		connect(hostlist)
	else:
		print "use: net_ipc.py [host.txt] username password"


