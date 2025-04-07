
"""
In The Name of GOD



Attend Project 2025

reated on Mon Apr  7 20:16:32 2025

@author: apm


**********************************
-----------task------------


task1-------------------
jaee k neveshtam #*************REAL WORLD********************
boro device ro vardar va taghir bede
bayad 'camera' ba code 100 ro support kone




task2-----------------

*****final structure******
print haro mibnevfgsi

ba f string ---> nmeshon bede bamn k tamame tavabe ro bedoni dare chiak rmikone



task3----------------
*****final structure******

tabe haye khali ro tozihatehso dadam ro
takmil konid




**********************************



"""


'''
IOT

Internet of Things
internete ashya

1- device ha bayad vask beshan be yek systeme markazi ( board dahste bashan b wifi vasl bashan)
2- systeme markazi betoone modirizateshon kone (control)



tamame Things b do ghesmate
1-devcie --> behjesh dastoor mdiidm mese lamp, door, fan 
2-sensor---> thermo (damaro begir) , gas , camera (tasavir ro begiri)




che sensor ch device bayad roosh board dahste bashe
b yek company vasete vasl bashe
va ma az tarighe API , Ketabkhon ee az python 
lapabe khodemon ro vasl konim




things---> koli chiz darfim
felan chiz device
az noe device

type esh devbice



typesh sensore


objecxti bekeshi brion az yek type

objecti bekeshi biron az yek class

class Device 

a1=device(lamp1)
a2=device(lamp2)
a3=device(door1)




3 APPROACH

Psudocode

function based

object oriented programming (class, object)



OOP --> class misazam






'''


class device:
    def __init__(self):
        pass
    
    

#a1=device(vorodi1,vorodi2,vorodi3)
#

#location --> home
#kojaye khone? ---> group
#type --> lamps , door
#lamps1
#lamps1380


class device:
    def __init__(self,location,group,device_type,name):
        pass
    

a1=device('home','parking','lamps','lamps11')





#==================================

#users.apm/desktop/data.csv

#LOCATION/group/type/name


class device:
    def __init__(self,topic):
        pass
    

#topic --> location/group/type/name

a1=device(topic='home/parking/lamps/lamps11')


#--------------------------------------


class device:
    def __init__(self,topic):
        
        self.topic=topic
        
        self.topic.split('/')
        
        pass
    

#topic --> location/group/type/name

a1=device(topic='home/parking/lamps/lamps11')


a='home/parking/lamps/lamps11'

b=a.split('/')

b[0] #'home'





class device:
    def __init__(self,topic):
        
        self.topic=topic
        
        self.topic_list=self.topic.split('/')
        
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        
        
    
    
a1=device(topic='home/parking/lamps/lamps1380')
    
    
print(type(a1))  #<class '__main__.device'>
    
a1.location #'home'
a1.group #'parking'
a1.device_type # 'lamps'
a1.name # 'lamps1380'


a2=device('home/room1/door/door1')
    
a2.location  #'home'
a2.group #'room1'
a2.device_type  #'door'
a2.name # 'door1'

    
 
#connect b mqtt , gpio

#dota ketabkhonas k behet ejaze mide
#K VASL SHI B YEK DEVICE VAGHEY PHYSICI




import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO 


class device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):
        
        self.topic=topic
        
        self.topic_list=self.topic.split('/')
        
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        
        self.mqtt_broker=mqtt_broker
        self.port=port
        
        #self.connect_mqtt()
        #self.setup_gpio()
        
        
    def connect_mqtt(self):
        self.mqtt_client=mqtt.client()
        
        self.mqtt_client.connect(self.mqtt_broker,self.port)
        
    
    def setup_gpio(self):
        
        #GPIO.setup(adad,GPIO.OUT)
        #age lamp --> 17
        #ag dar --> 27
        #ag fan --> 22
        
        #---->
        if self.device_type=='lamps':
            GPIO.setup(17,GPIO.OUT)
        
        elif self.device_type=='doors':
            GPIO.setup(27,GPIO.OUT)
            
        elif self.device_type=='fans':
            GPIO.setup(22,GPIO.OUT)
            
        #elif self.device_type..
            
    
            

a1=device(topic='home/parking/lamps/lamps100',mqtt_broker='189.11.39.114',port=1883)


a1.location #home
a1.group #parking
a1.device_type #lamps
a1.name #lamps1000

#--> mqtt / gpio --> amadeye amade

#a1.turn_on() ---> in roshanesh mikard

#a1.turn_off() ---> khamoshesh mikard
    




#a1.read_sensor()
#



class Sensor:
    
    def __init__(self,topic,pin=100):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.sensor_type=self.topic_list[2]
        self.name=self.topic_list[3]
        
    #def tunr_on
    def read_sensor(self):
        #import numpy
        #a=numpy.uniform(20,25)
        #return a
        
        return 25
        
        
a1=Sensor('home/paking/thermosets/thermo100',pin=431723689473674626392267349727)

a1.location #home
a1.group # 
a1.sensor_type #thermosets

a1.read_sensor()    # 25











#-------azinja b bad task2, task3 ------



class Device:
    def __init__(self,topic):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        
        self.status='off'
        
 
    def turn_on(self):
        self.status='on'
        print('turn on successfully')
        

    def turn_off(self):
        self.status='off'
        print('turn off successfully')

a1=Device('home/kitchen/lamps/lamps1')
a1.location #home
a1.group #kitchen
a1.device_type #lamps
a1.name #Lamps1

a1.status #'off'

a1.turn_on() #turn on successfully

a1.status # 'on'
     
        


class Sensor:
    
    def __init__(self,topic,pin=100):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.sensor_type=self.topic_list[2]
        self.name=self.topic_list[3]
    def read_sensor(self):
        return 25
    
    
    
    
a1=Device('home/kitchen/lamps/lamps1')


#40 ta dveice mikham bsazam

a1=Device('home/kitchen/lamps/lamps1')
a2=Device('home/kitchen/lamps/lamps2')
a3=Device('home/kitchen/lamps/lamps4')

a4=Device('home/kitchen/lamps/lamps4')

a4=Device('home/kitchen/lamps/lamps1')


#for i in range

'''


groups = {
    
    keys : values
    
    key1 : value1
    
    key2 : value2
    
    key1 : [balue1,vb alue,balue2]
    
    
    
    
    
    }



khgone --> khoen koli ghesmat dare
koli group

hall, room , wc, parking, kictchen ,....



groups={
        
    'parking' : [device1,device2,devcie3,devcie4,]
    
    'room1' : [device1,device2, sensoir1]

        
        
        
        }


'''




class admin_panel:
    
    def __init__(self):
        self.groups={}
        
        



a1=admin_panel()

    
    
    
a1.groups     #{}
    
    
    
class admin_panel:
    
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):

        self.groups[group_name]=[]
        
        print(f'group {group_name} is created')
        
a1=admin_panel()
  
a1.groups   # {}

a1.create_group('parking')   #group parking is created

a1.groups
# {'parking': []}

a1.create_group('WC') 

a1.create_group('room1') 
   
mygp=a1.groups   
        
class admin_panel:
    
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        
        if group_name not in self.groups:

            self.groups[group_name]=[]
            
            print(f'group {group_name} is created')
        
        else:
            
            print('your group name is existed already')
        
        
    def add_device_to_group(self,group_name,new_device):
        
        if group_name in self.groups:
            
            self.groups[group_name].append(new_device)
            
            #print(f'{device.name} is added to {group_name})
            
        else:
            
            print(f'group {group_name} is not exist')
        
        
    
a1=admin_panel()
  
a1.groups   # {}

a1.create_group('parking')   #group parking is created

a1.groups
# {'parking': []}

a1.create_group('WC') 

a1.create_group('room1') 
mygp=a1.groups 
    
    
    
new_device=Device('home/parking/lamps/lamps1')

 
a1.add_device_to_group('parking',new_device )


mygp=a1.groups 

new_device=Device('home/parking/lamps/lamps2')

 
a1.add_device_to_group('parking',new_device )

mygp=a1.groups 


parking_list=mygp['parking']

first_device=parking_list[0]
second_device=parking_list[1]


first_device.location
first_device.name# 'lamps1'

second_device.name #'lamps2'


class admin_panel:
    
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        
        if group_name not in self.groups:

            self.groups[group_name]=[]
            
            print(f'group {group_name} is created')
        
        else:
            
            print('your group name is existed already')
        
        
    def add_device_to_group(self,group_name,new_device):
        
        if group_name in self.groups:
            
            self.groups[group_name].append(new_device)
            
            #print(f'{device.name} is added to {group_name})
            
        else:
            
            print(f'group {group_name} is not exist')
        
        
        
    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            
            self.add_device_to_group(group_name,new_device)
            #print...
            
        else:
            
            print(f'group {group_name} is not exist')
            
a1=admin_panel()
  


a1.create_group('parking')   #group parking is created


a1.create_group('WC') 

a1.create_group('room1') 



a1.create_device('parking','lamps' ,'lamps134' )   


a1.groups

# {'parking': [<__main__.Device at 0x12fb82900>], 'WC': [], 'room1': []}
 
 
mydevice=a1.groups['parking'][0]

type(mydevice)#__main__.Device


mydevice.name # 'lamps134'

mydevice.turn_on()


mydevice.status #'on'



class admin_panel:
    
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        
        if group_name not in self.groups:

            self.groups[group_name]=[]
            
            print(f'group {group_name} is created')
        
        else:
            
            print('your group name is existed already')
        
        
    def add_device_to_group(self,group_name,new_device):
        
        if group_name in self.groups:
            
            self.groups[group_name].append(new_device)
            
            #print(f'{device.name} is added to {group_name})
            
        else:
            
            print(f'group {group_name} is not exist')
        
        
        
    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            
            self.add_device_to_group(group_name,new_device)
            #print...
            
        else:
            
            print(f'group {group_name} is not exist')
            
            
            
            
            
    def create_multiple_devices(self,group_name,device_type,number_of_devices):
        
        if group_name in self.groups:
            for i in range(1,number_of_devices+1):
                topic=f'home/{group_name}/{device_type}/{device_type}{i}'
                new_device=Device(topic)
                
                self.add_device_to_group(group_name, new_device)
                
                #print...
                

        else:
            pass
            
            
a1=admin_panel()


a1.create_group('parking')   #group parking is created


a1.create_group('WC') 

a1.create_group('room1') 

a1.create_multiple_devices('parking', 'lamps', 40)    
            
mygp=a1.groups 





#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))

#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))
#&&(*&@(!#!*(&^(*!&@IUREHWKDHSIUHDUHKUSDHJJUAHSKAJ))))

#_____TASK1_______
#*******************************************
#*************REAL WORLD********************

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO 

class device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):
        
        self.topic=topic
        
        self.topic_list=self.topic.split('/')
        
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        
        self.mqtt_broker=mqtt_broker
        self.port=port
        
        #self.connect_mqtt()
        #self.setup_gpio()
        
        
    def connect_mqtt(self):
        self.mqtt_client=mqtt.client()
        
        self.mqtt_client.connect(self.mqtt_broker,self.port)
        
    
    def setup_gpio(self):
        
        #GPIO.setup(adad,GPIO.OUT)
        #age lamp --> 17
        #ag dar --> 27
        #ag fan --> 22
        
        #---->
        if self.device_type=='lamps':
            GPIO.setup(17,GPIO.OUT)
        
        elif self.device_type=='doors':
            GPIO.setup(27,GPIO.OUT)
            
        elif self.device_type=='fans':
            GPIO.setup(22,GPIO.OUT)
            
        #elif self.device_type..
            
        
    def turn_on(self):
        
        #niaz daram b yek code inja k vasl she va
        #b device aslie man bege agha kahmois sho lotfan
        self.mqtt_client.publish(self.topic,'TURN_ON')
        #AGHA INJA BAYADF YEK ALGORITHEM BASZHE VASL SHE
        
        print('turn on successfully')
        
        
        
    def turn_off(self):
        
        self.mqtt_client.publish(self.topic,'TURN_OFF')


        print('turn off successfully')
    
    
    
    
a1=device(topic='home/parking/lamps/lamps100',mqtt_broker='189.11.39.114',port=1883)


a1.location #home
a1.group #parking
a1.device_type #lamps
a1.name #lamps1000


a1.turn_on() #turn on successfully


#topic= home/parking/thermosets/thermo100 , pin=2398373987198739173217


import Adafruiy_DHT

class Sensor:
    
    def __init__(self,topic,pin=100):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.sensor_type=self.topic_list[2]
        self.name=self.topic_list[3]
        
    #def tunr_on
    def read_sensor(self):
        
        humidity, temperature=Adafruiy_DHT.read_retry(Adafruiy_DHT.DHT22,self.pin)
        
        if self.sensor_type=='thermosets':
            return temperature
        else:
            return humidity



a1=Sensor('home/paking/thermosets/thermo100',pin=431723689473674626392267349727)







#___TASK2 & TASK3
#*******************************************
#**********FINAL STRUCTURE***************** 
class Device:
    def __init__(self,topic):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.name=self.topic_list[3]
        
        self.status='off'
        
 
    def turn_on(self):
        self.status='on'
        print('turn on successfully')
        

    def turn_off(self):
        self.status='off'
        print('turn off successfully')


class Sensor:
    def __init__(self,topic,pin=100):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.sensor_type=self.topic_list[2]
        self.name=self.topic_list[3]
    def read_sensor(self):
        return 25





class admin_panel:
    
    def __init__(self):
        self.groups={}
        
        
    def create_group(self,group_name):
        
        if group_name not in self.groups:

            self.groups[group_name]=[]
            
            print(f'group {group_name} is created')
        
        else:
            
            print('your group name is existed already')
        
        
    def add_device_to_group(self,group_name,new_device):
        
        if group_name in self.groups:
            
            self.groups[group_name].append(new_device)
            
            #print(f'{device.name} is added to {group_name})
            
        else:
            
            print(f'group {group_name} is not exist')
        
        
        
    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            
            self.add_device_to_group(group_name,new_device)
            #print...
            
        else:
            
            print(f'group {group_name} is not exist')
            
            
            
            
            
    def create_multiple_devices(self,group_name,device_type,number_of_devices):
        
        if group_name in self.groups:
            for i in range(1,number_of_devices+1):
                topic=f'home/{group_name}/{device_type}/{device_type}{i}'
                new_device=Device(topic)
                
                self.add_device_to_group(group_name, new_device)
                
                #print...
                

        else:
            pass
        
        
    def turn_on_devices_in_group(self,group_name):
        
        if group_name in self.groups:
            
            devices_list=self.groups[group_name]
            
            for device in devices_list:   
                device.turn_on()
            
            
            
            
        else:
            pass
    
    
    def turn_off_devices_in_group(self,group_name):
        '''
        khamoosh kone
        '''
        
        
        
        
        
        
    def trun_on_all(self):
        '''hameye device haro roshan kone
        tooo hame group ha 
        
        
        '''
        pass
        
    def turn_off_all(self):
        '''hameye devcie haro khamosh kone'''
        pass
    
        

    def get_status_in_group(self,group_name):
        
        '''living_room y matn print mikone mige lamp1 on , klamp2 off , lamp3 ,..'''
        pass
    
    
    
    
    def get_status_in_device_type(self,device_type):
        
        ''' device=lamps --> tamame lamp haro status mohem nabashe tooye living rome kojas'''
        pass
    
    
    #create_device
    
    #create_sensor.....
    
    def create_sensor(self) :
    #bar asase clASS SENSOR argument bzarid
        pass
    
    
    #read_sensor()
    def get_status_sensor_in_group(self,group_name):
        
        '''
        
        sensor haye yek goroh ro biad doone dooen status ro pas bde
        
        '''
        pass
        
    
    
        
        
        
        
            