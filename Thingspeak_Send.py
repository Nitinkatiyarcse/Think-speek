import time
import urllib3
import sys
sys.path.append('/home/pi/Adafruit_Python_DHT')
import Adafruit_DHT as dht

#Setup Write API
myAPI = "IJFEB0EFBN0D0DQ2"

while True:
        h,t = dht.read_retry(dht.DHT11,3)
        if isinstance(h, float) and isinstance(t, float):
                res_t='Tp='+str(t)+'*C'
                res_h='Hd='+str(h)+'%'
                baseURL = ('https://api.thingspeak.com/update?api_key=%s' % myAPI)
                http = urllib3.PoolManager()
                f = http.request('GET', baseURL +"&field1=%s&field2=%s" % (t,h))
                f.close()
                print(res_t+'\t'+res_h)
                time.sleep(5)
        else:
                print('Failed to read from DHT')
