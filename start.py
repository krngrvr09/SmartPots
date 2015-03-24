import json
import urllib2
import serial
import socket
import sys
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.10.21', 10000)

content = urllib2.urlopen('https://api.forecast.io/forecast/02f2a5a5b445ecc2e97668f0577d2017/28.54,77.27').read()
print content

j=json.loads(content)

cur_prec_prob = j['currently']['precipProbability']
prec_prob_1 = j['hourly']['data'][0]['precipProbability']
prec_prob_2 = j['hourly']['data'][1]['precipProbability']
prec_prob_3 = j['hourly']['data'][2]['precipProbability']
prec_prob_4 = j['hourly']['data'][3]['precipProbability']
prec_prob_5 = j['hourly']['data'][4]['precipProbability']

cur_hum = j['currently']['humidity']
hum_1 = j['hourly']['data'][0]['humidity']
hum_2 = j['hourly']['data'][1]['humidity']
hum_3 = j['hourly']['data'][2]['humidity']
hum_4 = j['hourly']['data'][3]['humidity']
hum_5 = j['hourly']['data'][4]['humidity']

print prec_prob_5

s=serial.Serial('/dev/ttyAMA0', 115200,timeout=5)

while True:
	pattern=[0,0]
	buffer = s.read(s.inWaiting())
	print buffer
	buffer = buffer.split("\r\nend\r\n")
	buffer = [i.lstrip('0') for i in buffer ]
	try:
		buffer = map(int, buffer)
	
		for i in buffer:
			if i<150:
				msg = "+2"
			elif i>150 and i<250:
				if prec_prob_5 < 0.25:
					msg = "-2"
					pattern[0]=1
				if prec_prob_5 > 0.25 and prec_prob_5 < 0.50:
					msg = "-2"
					pattern[0]=2
				if prec_prob_5 > 0.50 and prec_prob_5 < 0.75:
					msg = "-2"
					pattern[0]=3
				else:
					msg = "-2"
					pattern[0]=4
				pattern[1]=1
				#msg = "<250"
			elif i>250 and i<400:
				if prec_prob_5 < 0.25:
					msg="-1"
					pattern[0]=1
				if prec_prob_5 > 0.25 and prec_prob_5 < 0.50:
					msg = "-1"
					pattern[0]=2
				if prec_prob_5 > 0.50 and prec_prob_5 < 0.75:
					msg = "-1"
					pattern[0]=3
				else:
					msg = "-1"
					pattern[0]=4
				pattern[1]=2
				#msg = ">250<400"
			elif i>400 and i<600:
				if prec_prob_5 < 0.25:
					msg = "-1"
					pattern[0]=1
				if prec_prob_5 > 0.25 and prec_prob_5 < 0.50:
					msg = "-1"
					pattern[0]=2
				if prec_prob_5 > 0.50 and prec_prob_5 < 0.75:
					msg = "-1"
					pattern[0]=3
				else:
					msg = "-1"
					pattern[0]=4
				pattern[1]=3
				#msg = ">4<6"
			elif i>600 and i<800:
				if prec_prob_5 < 0.25:
					msg = "-1"
					pattern[0]=1
				if prec_prob_5 > 0.25 and prec_prob_5 < 0.50:
					msg = "-1"
					pattern[0]=2
				if prec_prob_5 > 0.50 and prec_prob_5 < 0.75:
					msg="-1"
					pattern[0]=3
				else:
					msg="-1"
					pattern[0]=4
				pattern[1]=4
				#msg = ">6<8"
			elif i>800 and i<1000:
				if prec_prob_5 < 0.25:
					msg = "+2"
					pattern[0]=1
				if prec_prob_5 > 0.25 and prec_prob_5 < 0.50:
					msg = "+2"
					pattern[0]=2
				if prec_prob_5 > 0.50 and prec_prob_5 < 0.75:
					msg = "+1"
					pattern[0]=3
				else:
					msg="+1"
					pattern[0]=4
				pattern[1]=5
				#msg = "else"
			else:
				break
			try:
				sent = sock.sendto(msg, server_address)
			except AttributeError:
				print "attribute error"
	except ValueError:
		print "valueerror"
	
