import json
import urllib2

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

print cur_prec_prob
