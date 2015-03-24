import serial
import re
s=serial.Serial('/dev/ttyAMA0', 115200,timeout=5)


content =  s.read(s.inWaiting())
#print content
#content = content.split("and")
#print content
for i in content:
	try:
		print int(re.match(r'\d+', i).group())
	except AttributeError:
		print "error"
