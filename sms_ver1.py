import conf                           #importing wifi-module information"""
from boltiot import Email, Bolt,Sms    #"""from bolt library importing importing specific files """
import json, time

mybolt=Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SSID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
k=0
c,t=0,0
while True:
  mybolt.digitalWrite('0','LOW')
  response = mybolt.digitalRead('0')
  data=json.loads(response)
  m=(int(data['value']))
  try:
    if  m != k :
      k = m
      c=1
      if k == 1 :
        g = sms.send_sms("Door Closed")
      else :
        g = sms.send_sms("Alarm! Door open")
    else :
      if (k!=1) :
        c+=1
        if(c >= 10):
          t+=1
          g = sms.send_sms("Door open for "+ str(t*10) +"seconds")
          c=0
  except Exception as e:
        print ("Error",e)
  time.sleep(0.65)
