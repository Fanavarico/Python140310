
"""
Created on Sun Apr 27 18:25:18 2025

In The Name of God

@author: apm



IOT

Internet of Things


IOT --> Tamame devcie ha --> Control markazi vasl she ( ma hedaytesh konim)



Things --> 1-Device 2-Sensor


Devcie --> dastor bedi , roshan , khamosh koni , . trun on , turn off
sensor--> dastor nmidi , fght azash chizi migiri




device,sensor --> IP (adade kahse khodeshon) , PIN

-----> markazi ( sherkati hs k sakhte )


--> API (Application programming interface) --> data o

ketabkhone ha behesh dastresi 

man in the middle --> 



yek shey besazi --> shey geraee
Object oriented programming (OOP)

devcie --> class
sensor--> class

"""


#topic='home/living_room/lamps/lamp1\'

#device(topic)
#device.group
#device.name

#device.turn_on()

#device.status
#device.get_status()


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
        
        '''
        
        print('now it is turned on')
        
        
    def turn_off(self):
        self.status='off'
        
        #dksjlizjlajsdkdad
        
        print('now it is turned off')
        
    def get_status(self):
        return self.status
        
    
    

#home/livbing_room/thermosets/thermo1

#a=Sensor(topic)

#sensor.location

#sensor.read_sensor()

import numpy as np
#a=list[10,20,30,40,50,60,70,80,90,100]
#a+100
#a[0]


#b=np.array([10,20,30,40,50,60,70,80,90,100])
#b+100
#b[0]



#np.arange(10,110,10)

#np.random.uniform()

class Sensor:
    def __init__(self, topic):
        self.topic = topic
        self.topic_list = self.topic.split('/')
        
        self.location=self.topic_list[0]

        self.group = self.topic_list[1]
        self.device_type = self.topic_list[2]
        self.name = self.topic_list[3]
        #self.pin = pin  # sensor pin
        
        self.status=self.read_sensor()

        

    def read_sensor(self):
        a=np.random.uniform(21,25,(1,))
        #return 24
        return a

    def turn_on(self):
        pass
    
    def turn_off(self):
        pass


'''
TASK1 ----> DEVCIE RO KAMELAN FAHMIDID VA YE NEGAH MIDNAZID

REAL WORLD



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

#a=devcie()
#a=device()

#class --> ADMIN PANEL 

'''


groups= {
    
    
    
    
    
    
    
    }





esme jahaye khone | listi az device ha bahse
keys   | values
living_room | [d1,d2,d3,d4,d5]
parking | [d1,d2,d3]


fard---> group hasho ebsaze 
khoenye man , 1 , 2 ,3 ghemsat o dare
hame inaro dictioanry groups 


groups{
       
      'parking' : [],
      'living_room' : [],
      
 
       }


#harja ch device hae toshe



groups={
       
      'parking' : [d1,d2,d3,d4],
      'living_room' : [],
      
 
       }


a=groups[key] --> value --> []

b=a[0] --> device 

b.location
b.turn_on()


a=ADMIN_PANEL()
groups={}




a.create_group(hal) -->
groups={
        hal : [d1]
        
        }









delan_device=Device(....)
a.add_device_to_group(hal,felanm device)

groups={
        hal : [device]
        
        }




delan_device=Device(....)
a.create_device_in_group(hal,esm, type ,)

device -->

groups={
        hal : [device]
        
        }


a.cretae_multiple_group(hal, esm , type , 40)



groups={
        hal : [device,d2,d3,d4,d5,d6,]
        
        }



a.turn_on_all_device_in_group(hal)


groups={
        hal : [device,d2,d3,d4,d5,d6,]
        
        }

d1.turn_on()




'''

class admin_panel():
    
    #nam , name khanevadegi , shoamreye karbari , .....
    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'group {group_name} is created')
            
        else:
            print('your name is dublicated')
            
    #biroon 
    #a.add_xevice(esmegroup , device)
    def add_device_to_group(self,group_name,device):

        if group_name in self.groups:
            self.groups[group_name].append(device)

        else:
            print('your group is not created')
            
            
    #devic deham khodesh besazze
    
    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            self.add_device_to_group(group_name, new_device)
            #F'DEVICE IS CREATE'
           # F'device {device.name} is created'
            
        else:
            print('your group is not created')
    
    
    def create_multiple_devices(self,group_name,device_type,number_of_devcies):
        
        if group_name in self.groups:
            
            for i in range(1,number_of_devcies+1):
                #number=10 -> 1,2,3,4,5,6,7,8,9,10 -->i
                
                device_name=f'{device_type}{i}'
                
                topic=f'home/{group_name}/{device_type}/{device_name}'
                
                new_device=Device(topic)
                
                self.add_device_to_group(group_name, new_device)
                

                '''
                device_name=f'{device_type}{i}'
                
                self.create_device(group_name,device_type,device_name)

                '''

            
        else:
            print('')
            
            
            
            
    def turn_on_all_in_groups_approach1(self,group_name):
        
        if group_name in self.groups:
            #b liste hall dastresi peyda koni 
            #bad done done roshan koni
            
            #self.groups[group_name] #List
            my_group=self.groups[group_name]
            
            for device in my_group:
                #if isinstance(device, Device):
                
                device.turn_on()
                
                #print.....
            
            
            
            
            
        else:
            print('we dont have such a group')
            
          
            
          
    def return_all_device_in_group(self,group_name):
        
        all_device_in_gp=self.groups[group_name]
        
        return all_device_in_gp


    def turn_on_all_in_groups(self,group_name):
        
        if group_name in self.groups:
            all_device=self.return_all_device_in_group(group_name)
            
            for device in all_device:
                device.turn_on()
                
            
            
        else:
            print('we dont have such a group')
    
    
    def turn_off_all_in_groups(self,group_name):
        
        if group_name in self.groups:
            
            all_device=self.return_all_device_in_group(group_name)
            for device in all_device:
                device.turn_off()
                
            
        else:
            print('we dont have such a gorup')
        



    def return_all_devices(self):
        all_devices=[]
        
        for group_name in self.groups.keys():
            
            devices=self.gorups[group_name]
            
            all_devices.extend(devices)
            
        
        return all_devices
    '''
    all_devices=[]
    
    
    a=[d1`,d2,d3,d4]
    
    b=[d10,d20,d30,d40]
     
all_devcies.append(a)
.append(b)

  
all_devcies=[[d1`,d2,d3,d4] , [d10,d20,d30,d40]  ]   


all_devices.extend(a)

all_devcies=[d1,d2,d3,d4 ,d10,d20,d30,d40  ]

    '''
    



   

  
            

        
    #hame device
    def turn_on_all(self):
        
        all_devices=self.return_all_devices()
        
        for device in all_devices:
            device.turn_on()
            
            
            
    def turn_off_all(self):
        all_devices=self.return_all_devcies()
        for device in all_devices:
            device.turn_off()
        


    def get_status_in_group(self,group_name):
        
        my_devcies=self.return_all_device_in_group(group_name)
        
        
        '''
        for device in my_devcies:
            print(device.status)
        '''
        
        '''
        for device in my_devcies:
        
            print(f'device is {device.status}')
        '''
            
        '''
        for device in my_devcies:
        
            print(f'{device.name} is {device.status}')
            
        '''
        
        status={}
        
        for device in my_devcies:
            
            status[device.name]=device.status
        
             #device.get_status()
        
        return status
    
        '''
        
        lamp1 : on
        lamp2 : off
        lamp3 : on
        
        
        '''
        
        
        
        
        
        '''
        status={
            
            esm_devcie : on
            esme_devcie : off
            
            
            
            
            }
        
        return status
        
        
        '''
        
        
    def get_status_in_device_type(self,device_type):
        
        all_devices=self.return_all_devices()
        
        status={}
        
        for device in all_devices: 
            if device.device_type == device_type:
                #print(f'{device.name} is {device.status}')
                #status[device.name]=device.status
                
                status[f'{device.name} in {device.group}']=device.status
                
   
        return status
    
    
    
    
    '''
    a.get_status_in_device_type(lamps)
    
    all_devices=az hame jaa hall, parking
    
    for devcie in all_device 
    device.devcie type== lamps
    
    status
    
    
    lmaps1 = on
    lamps2 = off
    lamps3 = on
    
    
    lamps in hall = on
    lamps2 in wc = off
    lamps3 in parking = off
    
    
    
    '''
    
    def get_status_in_device_type(self,device_type):
        all_devices=self.return_all_devices()
        
        status={}
        
        for device in all_devices: 
            if device.device_type == device_type:
                #print(f'{device.name} is {device.status}')
                #status[device.name]=device.status
                
                status[f'{device.name} in {device.group}']=device.status
                
                
                
        return status
    
    


       #hall = [d1,d2,d3,s1,s3,]
       #addA_device ( device, hall)
       #create_device(hall, fan , fan103)
       
       
    def add_sensor_in_group(self,group_name,sensor):

        self.groups[group_name].append(sensor)
        
        #add_device_in_group
        
        
    def create_sensor(self,group_name,sensor_name,sensor_type):
        
        topic=f'home/{group_name}/{sensor_type}/{sensor_name}'
        new_sensor=Sensor(topic)
        
        self.add_sensor_in_group(group_name,new_sensor)
        
        
    #def create_multiple_sesnor()



    #def TURN_on_sensor_....
    #sensor --> data mitoni begiri
    #turn on , turn off , device, devcie type , groupo XXXXXX
    
    #read_sesnor
    #hall = [d1,d1,d3,d4,s1,s2,s3]
    
    
        
    def get_data_from_sensor_in_group(self,group_name):
        
        mydevices=self.groups[group_name]
        
        for device in mydevices:
            #ghhablesh tashkhis bedii k 
            #devciet inja sensore ya device
            #ag sensor--> read_sensor()
            if isinstance(device,Sensor):
                sensor_data=device.read_sensor()
                print(f'{device.name} is {sensor_data}')
                
            
        
           
                
'''

-----DATA BASE--------

DATA BASE


mysql -->


Terminal --> black window


mysql -u root -p (password)  enter

varede MYSQL 

2---> user besazid --> passs

3---> data base besaziid

4--> user/pass , dastresi b database bedid

5--> tooye data base --> yek table besazid

cmd.exe 
terminal 

command line 





             
       
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    device_name TEXT,
    action TEXT,
    timestamp TEXT
)

    
esme table --> logs


id      device_name   action       time

0        lamps1        turn off    ///
1
2
3
4
5
6
7
8



mysql-connect-python

sqlite3


'''
import sqlite3

from datetime import datetime


def log_action(name,action):
        """Log the action into the database."""
        conn = sqlite3.connect("device_logs.db")
        cursor = conn.cursor()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO logs (device_name, action, timestamp) VALUES (?, ?, ?)",
                       (name, action, timestamp))

        conn.commit()
        conn.close()




class Device:
    #def __init__(self,topic,pin):
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
        
        log_action(self.name,'turn on')
        

    def turn_off(self):
        self.status='off'
        log_action(self.name,'turn_off')
     
        
     



#================================================

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



#=======================================
'''


Infrustructure msiazim




----> BACKEND poshte ghazias


a=admin_panel()

a.create_group('hall')




TASVIR MIKHAY



---> Backend , infrsutrture




----------------
rooye website
backend --> python
front ---> HTML , css , Javascript

hall --> user neveshte 
az html ----> python   a.create_group(hall)


rabete beyne barname hat

rabete ye barname ee

application programming interface

API

django 
flask
fastapi

ip --> 148l.79.323.22

DNS --> 
domain --> 

plutusplutus.com
----> 148l.79.323.22



148l.79.323.22 --> port




def create_group(group_name):
    kario anjam mide
    
    
    
    
====html=========
zarf=....... user 

184.22.22.22 send zarf //group
184.22.22.22/group
openai.com/api/
prompt


group --> esme --> ip/group/12340987







====python=======
django 
flask
fastapi


@/group/password (api_key)

def create_group():
   
    
   
@/device_management/12340987
class












Narm afzar (GUI)
sait 
python

GUI -->
graphcial user injterface --> applciation baz mishe

bejaye inek code bzne ye safs k resho mikoen

C / C++ --> QT -->

python -->
tkinter


pyqt --> sherkate dgas
pyslide --> QT





--------SMART HOUSE MANAGEMENT-------


----GROUP MANAGEMENT---------
GROUP -----------
{{{{{CREATE GROUP}}}}}



----DEVICE MANAGEMENT-------
GROUP -------
DEVCIE---TYPE---
NAME .......

{{CREATE}}


----MULTIPLE------
GROUP....
DEVCIE TYPE ....
MNUMBER

{CRREATE}




-----STATUS-------
GHROUP .....
{STATU}







'''


















            
            
    






    