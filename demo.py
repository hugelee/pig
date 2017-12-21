#!/usr/local/bin/python
#author : lizb
#date : 2017/10/30

import ipip
import sys
import time
sys.path.append('/Users/apple/lzbworkspace/mylib')
reload(sys)
from scapy.all import *

class pig(object):
	"""docstring for pig"""
	def __init__(self):
		super(pig, self).__init__()

	def part_head(self,pkt_msg):
		srcip = pkg_msg[IP].src
		is_tc = pkg_msg[DNS].tc
		is_rd = pkg_msg[DNS].rd
		is_ra = pkg_msg[DNS].ra

	def part_query(selg,pkt_msg):
		pass

	def qtype_A(self, your_qname,your_dnsip='8.8.8.8'):
		self.your_qname = your_qname
		self.your_dnsip = your_dnsip
		pkt = sr1(IP(dst=your_dnsip)/UDP()/DNS(rd=1,qd=DNSQR(qtype=1,qname=your_qname)), verbose=0)
		if pkt and pkt.haslayer('UDP') and pkt.haslayer('DNS'):
			dns = pkt[DNS]
			ancount = dns.ancount
			for i in range(ancount):
				dnsrr = dns.an[i]
				print ipip.get_ip(str(dnsrr.rdata))
				time.sleep(1)		
	def qtype_NS(self, your_qname,your_dnsip='8.8.8.8'):
		self.your_qname = your_qname
		self.your_dnsip = your_dnsip
		pkt = sr1(IP(dst=your_dnsip)/UDP()/DNS(rd=1,qd=DNSQR(qtype=2,qname=your_qname)), verbose=0)
		if pkt and pkt.haslayer('UDP') and pkt.haslayer('DNS'):
			dns = pkt[DNS]
			ancount = dns.ancount
			arcount = dns.arcount
			if ancount:
				print "%s's nameservers are:" % your_qname
				for i in range(ancount):
					dnsrr = dns.an[i]
					ns = dnsrr.rdata
					print ns
			if arcount:
				print "Details about nameservers:"
				for j in range(arcount):
					dnsrr = dns.ar[j]
					ar_ns = dnsrr.rrname
					ar_nsip = dnsrr.rdata
					print "%s\t%s" % (ar_ns, ar_nsip)
	def qtype_CNAME(self, your_qname, your_dnsip='8.8.8.8'):
		self.your_qname = your_qname
		self.your_dnsip = your_dnsip
		pkt = sr1(IP(dst=your_dnsip)/UDP()/DNS(id=1,qd=DNSQR(qtype=5,qname=your_qname)), verbose=0)
		if pkt and pkt.haslayer('UDP') and pkt.haslayer('DNS'):
			dns = pkt[DNS]
			print dns.an.rdata



def usage():
	print "usage:pig www.baidu.com or pig www.baidu.com @119.29.29.29"


mypig = pig()

num_of_argv = len(sys.argv)
if num_of_argv < 2:
	usage()
elif num_of_argv == 2:
	domain = sys.argv[1]
	mypig.qtype_A(domain)
elif num_of_argv == 3:
	if sys.argv[-1] == 'ns':
		domain = sys.argv[1]
		mypig.qtype_NS(domain)	
	elif sys.argv[-1] == 'cname':
		domain = sys.argv[1]
		mypig.qtype_CNAME(domain)
	else:
		domain = sys.argv[1]
		dnsip = sys.argv[2].split('@')[1]
		mypig.qtype_A(domain, dnsip)
elif num_of_argv == 4:
	if sys.argv[-1] == 'ns':
		domain = sys.argv[1]
		dnsip = sys.argv[2].split('@')[1]
		mypig.qtype_NS(domain, dnsip)
	if sys.argv[-1] == 'cname':
		domain = sys.argv[1]
		dnsip = sys.argv[2].split('@')[1]
		mypig.qtype_CNAME(domain, dnsip)
else:
	usage()
	exit(255)





