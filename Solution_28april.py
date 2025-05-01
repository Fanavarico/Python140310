
"""

In The Name of God


Created on Mon Apr 28 18:35:26 2025

@author: apm




-----HADAF-------
IOT --> Internet of Things

Things harf o connect be ye systeme markazi 


Things --> devcie / sensor
device --> man behesh dastoro mdiam
sensor --> balke fght azash data migirm



device/sensor (ip) ----> SHERKAT ---> be man vaslan



Things msiazim
object misazim az yek type
yek object az yek class

object oriented programming (OOP)


Class --> Device
Class --> Sensor




"""


#a=Device(..)
#topic
#topic= /home/livinroom/lamps/lamps104
#a=Device( '/home/livinroom/lamps/lamps104')

#a.location
#a.device

#a1
#a2
#a3=Device(....) --> __init__

#a2.name
#a3.name

#attributes

#a1.turn_on()
#method

class Device:
    def __init__(self,topic):

        self.topic=topic
        self.topic_list=self.topic.split('/')
        
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        
        self.status='off'

        #self.pin=pin

       

    def turn_on(self):
        
        self.status='on'
        '''
        
        mqtt protocol
        GPIO
        
        
        '''
        
        print('now it is turned on')
        
        
    def turn_off(self):
        self.status='off'
        
        #dksjlizjlajsdkdad
        
        print('now it is turned off')
        
    def get_status(self):
        return self.status
        

#dsar , cheragh , fan , dorbin --> Device

#sensor--> thermoset , gaz sanj , ...sanj
#Misanje
#to dastor nmidi 

#aszqsh data mikhay 
#sensor


#a1=Sensor(topic)
#

#a.turn_on()

#sensor--> 
#a.read_data()

import numpy as np

#a=[10,20,30,40,50,60,70]
#a+2
#20 , 30 
#append
#

#numpy.array() --> list
a=np.array([10,20,30,40,50,60,70,80])
#a+2
#a[1]
#a[1:4]
#a[1]=1000


#sin
#cos
#.....


a=np.random.uniform(20,25,(2,))




class Sensor:
    def __init__(self, topic):
        self.topic = topic
        self.topic_list = self.topic.split('/')
        
        self.location=self.topic_list[0]

        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.name = self.topic_list[3]
        #self.pin = pin  # sensor pin
        

    def read_sensor(self):
        #bere KLetabkhe, vasete data ro bgire pas bde
        
        #return
        #return 24
        a=np.random.uniform(18,30,(1,))
        return a
    
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass
    
    





#===============================
#===============================
#===============================
#===============================
#===============================
#===============================

'''
TASK1 ----> DEVCIE RO KAMELAN FAHMIDID VA YE NEGAH MIDNAZID

REAL WORLD

#a=device('dssdadda',18.922.22, 1880)
##a=device('dsaadsdsada')
#mqtt_nbrke and arguments

import library
import library as mokhafaf

#----sklearn , tensorflow

librayr.class.function....


from library import class
from library import ....

class.function()





#a=device('dsaadsdsada')



class Device:

    def __init__(self, topic, mqtt_broker='localhost',port=1883):

        self.topic = topic
        self.topic_list = self.topic.split('/')
        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.name = self.topic_list[3]
        self.port = port
        self.mqtt_broker = mqtt_broker
        self.status = 'off'

        self.connect_mqtt()
        self.setup_gpio()


    def connect_mqtt(self):
        self.mqtt_client.connect(self.mqtt_broker, self.port)
        print(f'{self.name} connected to mqtt')


    def setup_gpio(self):
        if self.device_tye == 'lights':
            GPIO.setup(17, GPIO.OUT)
            print(f'{self.name} connected to gpio')

        elif self.device_type == 'doors':
            GPIO.setup(27, GPIO.OUT)
            print(f'{self.name} connected to gpio')

        elif self.device_type == 'camera':
            GPIO.setup(adad,GPIO.OUT)
            print(f'{self.name} connected to gpio')
            
            
    

'''


#==============================
#==============================
#==============================
#==============================
#==============================
#==============================
#==============================

'''
software
complex ----> dioctionary of data


dictionary

Khoone --> hezaran ja 
har jaa -> hezar ta dveice , sensor

har  device roshn she



dictionary ghararesh bdm --> hadad 

complex --> []



API --> 
application programming interface


server--> 
yek khjat bege server kojas?

server kharidm --> servere man chie va kojas?

software engineering

API 



complexd ---> {}




khoone koli device



aval done done jahasho joda konam
bad too harkodom devicasho

diuctioanry:
    
    {
     
     
     
     key : values
     key : values
     
     
     
     }




groups={
    
    hal : [devcie1,device,sensor1,sensor2]
    
    parking : []
    
    
    ashpazkhane : []
        

        }


groups --> {}

groups[parking] --> liste (havie devica)

groups[parking][0] --. device

groups[parking][0].name .location .turn_on turn_off()



software enginering 


all[step3][layer8][object15][microsystem][][][values]


instagram --> data haro 



esme jahaye khone | listi az device ha bahse
keys   | values
living_room | [d1,d2,d3,d4,d5]
parking | [d1,d2,d3]


groups{
       
      'parking' : [],
      'living_room' : [],
      
 
       }





groups={
       
      'parking' : [d1,d2,d3,d4],
      'living_room' : [],
      
 
       }





admin_panel


groups={
        
        
        
        
        }

jahaye khonamo besaazam

create_group


groups={
        
     group_name : [a1]   
        prkign : [b100]
        
        }



2 ta ravesh vojod dare


a1=Device(/dhome/pakring/,,,,/lamps104')
         
admin_panel.add_device(hall , a1)

admin_panel.create_add(hall , lamps , lamps1)

'''
#a=admin_panel()

#a.create_group(hall)


class admin_panel:
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        if group_name not in self.groups:
        
            self.groups[group_name]=[]
            print('it is done')
            
        else:
            print('duplicated')
        
        
    #b100=Device('home/parking/lamps/lamps1)
    #admin_pnale.add_device(parking,b100)
    
    def add_device_in_group(self,group_name,device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
        
        else:
            print('no group_name')
        
    
    #admin_panel.yekfunction(hall, lamps, lamps1)
    
    def create_device(self,group_name,device_type,device_name):
        
        
        topic=f'home/{group_name}/{device_type}/{device_name}'
        
        new_device=Device(topic)
        
        #self.groups[group_name].append(new_device)
        self.add_device_in_group(group_name, new_device)
            
        
        
        
        
    def create_multiple_device(self,group_name,device_type,number):
        
        '''
        for i in range(1,number+1):
            name=f'{device_type}{i}'
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            self.groups[group_name].append(new_device)
        '''

        for i in range(1,number+1):
            name=f'{device_type}{i}'
            self.create_device(group_name, device_type, name)
        
        
    def turn_on_all_in_groups(self,group_name):
        
        if group_name in self.groups:
            #b liste hall dastresi peyda koni 
            #bad done done roshan koni
            
            #self.groups[group_name] #List
            my_group=self.groups[group_name]
            
            for device in my_group:
                #if isinstance(device, Device):
                
                device.turn_on()
    
    def turn_off_all_in_groups(self,group_name):
        
        if group_name in self.groups:
            #b liste hall dastresi peyda koni 
            #bad done done roshan koni
            
            #self.groups[group_name] #List
            my_group=self.groups[group_name]
            
            for device in my_group:
                #if isinstance(device, Device):
                
                device.turn_off()
                
        #hame gorohaaaa

    def return_all_devices(self):
        
        all_devices=[]
        for group_name in self.groups.keys():
            group_devices=self.groups[group_name]
            #[d1,d3,d4,d5]
            
            all_devices.extend(group_devices)
            
            
       # for name,device_list in self.groups.items(): 
       #     all_devices.extend(device_list)
            
            
  
        return all_devices
            
      #[d1,d2,d3]
        #[a1,a2,a3]
        #[b1,b2b,3]
        #[ [d1,d2,d3] ,[a1,a2,a3] , [b1,b2b,3]     ]
        
        #[ d1,d2,d3 ,a1,a2,a3 , b1,b2b,3     ]
        
        
        
    def turn_on_all_devices(self): 
        all_devices=self.return_all_devices()
        for device in all_devices:
            device.turn_on()
            
            
        
            
    def turn_off_all_devices(self):
        all_devices=self.return_all_devices()
        for device in all_devices:
            device.turn_off()
            
    
    
    def turn_on_device_type(self,device_type):
        #hall, parking ,....
        
        all_device=self.return_all_devices() #hall, parking ,,...
        
        #sensor --> tunr_on()
        #turn_off()
        #status
        #get_status()
        
        
        for device in all_device:
            #if isinstance(device,Device)
            if device.device_type == device_type:
                device.turn_on()
    
    
    
    def get_status_in_groups(self,group_name):
        
        # self.groups[group_name] #liste device haro mide
         
         #for device in self.groups[group_name]:
         #    print(device.status)
             
             #device.get_status() --> status
         
         #on
         #off
         #on
         #off
         
         
        # for device in self.groups[group_name]:
        #     print(f'{device.name} is {device.status}')
         #lamps1 is on
         #lampo2 isd off
         #lamps3 is on
         
         
        status={}
        '''
        
        keys | value
        lamp1 | on
        lamp2 | off
        
        
        
        
        '''
        
        for device in self.groups[group_name]:
            #bejay eprint
            status[device.name]=device.status
            
        return status
    
    
    
    def get_status_in_device_type(self,device_type):
        
        status={}
        
        all_devices=self.return_all_devices()
        
        for device in all_devices:
            if device.device_type==device_type:
                status[device.name]=device.status
                
    
    
    #sensore neveshtan
    
    #device /
    
    #device()
    #addd
    
    
    #create --> namo ,, misakhto ad mikrd
    #aadd_device
    
    #sensor..
    #add_device_in_group
    
    def add_sensor_in_group(self,group_name,sensor):
        self.groups[group_name].append(sensor)
        
        
        
        
    def create_sensor(self,group_name,sensor_type,sensor_name):
        
        topic=f'home/{group_name}/{sensor_type}/{sensor_name}'
        new_sensor=Sensor(topic)
        
        #self.groups[group_name].append(new_sensor)
        self.add_sensor_in_group(group_name, new_sensor)
            
        '''
        hall : [d1,d2,d3,d4,d5,sensor1,d7,d8]


        urn_on()
            turn_off()
            get)status()
    
    

        '''
    def get_data_from_sensor_in_group(self,group_name):
        

        for sensor in self.groups[group_name]:  
            if isinstance(sensor,Sensor):
                status=sensor.read_sensor()
                print('f{sensor.name} is {status}')
        
        
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
     
'''

mysql
sqlite



redis --> RAM
celery


paygahe dade

mysql --> berizid
usere madar --> root
psswordere madsar--> ....




--> user password

---> db


-->db --> mnajmo ee az koli table



#yek table

device  action time

devcie103  turn on   25 april 2:13:43


----- terminal / cmd.exe
command line 


mysql -u username -p password enter --> sql


2----
user password jadid 


3---
database


4--
dastresie kamel ro be oon data base bedid b oon user pass



5---
use esme_database -->

CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_name TEXT,
    action TEXT,
    timestamp TEXT
)

------logs--------
id  device_name     action  time

0    device105      turn on    25 arpil...


#
------logs--------
id  device_name     action  time

0    device105      turn on    25 arpil...
0    device105      turn on    25 arpil...
0    device105      turn on    25 arpil...
0    device105      turn on    25 arpil...
0    device105      turn on    25 arpil...
0    device105      turn on    25 arpil...
0    device105      turn on    25 arpil...
0    device105      turn on    25 arpil...
0    device105      turn on    25 arpil...





.......




'''
import sqlite3
from datetime import datetime




#----database
def log_action(name,action):
        """Log the action into the database."""
        conn = sqlite3.connect("device_logs.db")
        cursor = conn.cursor()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO logs (device_name, action, timestamp) VALUES (?, ?, ?)",
                       (name, action, timestamp))

        conn.commit()
        conn.close()



#mysql -u root -p ali1234
#use device_logs
#select * from logs






def get_logs():
    """Retrieve and display logs."""
    conn = sqlite3.connect("device_logs.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()

    conn.close()

    for log in logs:
        print(f"ID: {log[0]}, Device: {log[1]}, Action: {log[2]}, Time: {log[3]}")

# Call this function to view logs
get_logs()



class Device:
    
    def __init__(self,topic):
        #....
        pass
    
    
    def turn_on(self):
        self.status='on'
        #.....
        print('turn on izs done')
        
        log_action(self.name , 'turn on')
        
    def turn_off(self):
        self.status='off'
        print('....')
        log_action(self.name , 'turn off')
        
        

#---GUI --> narem afzar --> tkinter
'''

Python --> Backend 
infrustructure --> zirsakht minevisim

admin_panel()---> device, groups , turn on  , turn off
hame bayad bian code bznan inke nashdo???


tooye khoone yeki k code balad 
roosh cover rooye codee man bashe
click ba angoshtat oon coda ejra sha



graphiciii khoshgel



------WEBSITE--------
index.html



front ----> html , css , javascript

<<----Hello welcome to my IOT---->>


html.button ( create_group)
html.colour.(Blue)
css.font(Tiemnewromans)
zarf=html.entry(......)



API ----> request
django
flask
fastAPI




backend
admin_panel.create-group(hall)



#-----------------
GUI -->L graphical user interface
-->local , enternet -->laptab , chip ,

chip ---> barname

coveri rooye khdoet


C++ , C# ---> QT

GUI
Graphical user interface
rabete  karbari graphici





#-------
python
tkinter --> GUI



pyqt
pyslide ---> QT





pip install tkinter

'''   

        
        
        
      
    
            
            
        

        
        
        
        
        
        












