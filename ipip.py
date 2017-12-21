#!/usr/local/bin/python
#coding:utf-8
#author : lizb
#date : 2017/10/30

import urllib2
import json

def get_ip(yourip):
	IPAPI = 'http://freeapi.ipip.net/' + yourip
	res = urllib2.urlopen(IPAPI)
	res = json.load(res)
	location = ''
	for i in res:
		if i:
			location += i	
	output = yourip + "\t" + location
	return output
#	return "{0}\t{1}".format(yourip, location)
