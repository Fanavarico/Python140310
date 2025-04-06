
"""

In The Name of GOD


Created on Sun Apr  6 20:03:05 2025

@author: apm


****************8PROJECT*****************


******task1*********
onjaee k neevshtam ****real_world****
class devcie ro taghir bde
behesh 
#CAMERA, GPIO 100




******task2*********

taske 2 e3 ye shoam in hast ke b
****final**** print ezafe konid harja k print nadasht


*****task3***********
takmil kardane tyabeye **final***











------------------------------
Project_Non_Attend


IOT 

Interner of Things
internete ashya




"""

'''
tozihat------------------------



IOT--> 
1- Device ha vask bashan b yek systeme markazi
2- systeme markazi betoone modiriateshon kone (control)


pas naiz has device ha yek chizi bename board too deleshon bashe
ke vasl she b wifi

hala in devcie ha mitonban , lamp, door, doorbvin, fan ,...


man az tarighe laptabam, vasl sham be oon API company 
dastoor bdm bhsh bgm agha in devicue man bva in moshakhasat (ip)
begma agha b in dastoor bede va roshanesh kon

oon miad vask mishe ( bejaye kilid , kilide electronici dare)





#---------Classification of things in the world-------


tamame chizha do no hastan


1----> devcie------
lamps, door, fan 
inaro mishe dastoor dad, roshan vba kahmosh mishan



2---> sensor-----
dastoori nmishe beheshon dad balke ina baraye nadaze giri hastan
va fght moishe asashoon data gereft





chiz ha --> object 


objecdt yek noe

yek object ye no dg



--> class



class --> object mikeshid biroon




dota chiz dashte basham
device
sensor




class device
class sensor




class device ---> object haye motefavegh bekeshm biron
lamp12 ,lamp2 , lamp3 ,...

'''




class Device:
    
    def __init__(self,topic,mqtt_broker='localhost',port=1883):
        pass








#lamps1=Device()

#mqtt_broker='localhost',port=1883 --> in device 

#LAMP1= Device(topic='')


#-------


#lamp1 --> home 
#group --> hale , ashpazkhonas
#device type --> lamp, door, fan
#name device

#lamp1=Device('home','ashpazkhoone','lamps','lamps134')
    

class Device:
    
    def __init__(self,location,group,device_type,name):
        self.location=location
        self.group=group
        #....
        pass
    
    
'''

adrese

user/desktop/crypto_files


home/ashpazkhoone/lamps/lamps134

'''






class Device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):
        self.topic=topic
        
        self.topic_list=self.topic.split('/')
        
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.device_name=self.topic_list[3]
        
        
        self.mqtt_broker=mqtt_broker
        self.port=port
        
        
        

    
    


a=Device('home/group/device_type/device_name')

a=Device('home/parking/lamps/lamps138')




a.topic
#'home/parking/lamps/lamps138'


mylist=a.topic_list



#==================================
class Device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):
        self.topic=topic
        
        self.topic_list=self.topic.split('/')
        
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.device_name=self.topic_list[3]
        
        
        self.mqtt_broker=mqtt_broker
        self.port=port
        
        


#a1=Device('home/parking/lamps/lamps134',mqtt_broker='455.65.43.11',port=112)


a1=Device('home/parking/lamps/lamps134')


#as1 --> yek object az device ha hast

a1.topic #'home/parking/lamps/lamps134'


#4 ta chiz ro miham


a1.location #'home'
a1.group # 'parking'

a1.device_type #'lamps'
a1.device_name # 'lamps134'


a2=Device('home/kitchen/lamps/lamps987')

a2.location

a2.device_name








#a1=Device(/'''''/)

 
#a1.turn_on()

#a1.tunr_off()


   
a1=Device('home/kitchen/lamps/lamps134') #mqtt_breoker= , port

           
a1.location
a1.group
a1.device_type
a1.device_name


a1.turn_on()
# Turn on , Done !




#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------


class Device:
    def __init__(self,topic):
        self.topic=topic
        
        self.topic_list=self.topic.split('/')
        
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.device_name=self.topic_list[3]
        
        self.status='off'
        


    def turn_on(self):
        #** yek satdori inja hast ke
        #b vaseteye mqtt roshanehs mikone
        
        self.status='on'
        
        print(' Turn on , Done !')
        #dastoori inja bnvisam k bre va roshan kone
 
    
    def turn_off(self):
        self.status='off'
        
        
        print('Turn off, Done!')
  
    
    def get_status(self):
        print(f'your device is {self.status}')


a1=Device('home/kitchen/lamps/lamps1')
a1.location
a1.group #kitchen
a1.device_type  #lamps
a1.device_name #lamps1

a1.get_status() #your device is off




a1.turn_on()

a1.get_status() #your device is on


a1.turn_off()

 
a1.get_status() #your device is off


'''
import Adafruiy_DHT


class Sensor:
    
    def __init__(self,topic,pin=100):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.sensor_type=self.topic_list[2]
        self.sensor_name=self.topic_list[3]
        
    
    def read_sensor(self):
        humidity,temperature=Adafruiy_DHT.red_retry(Adafruiy_DHT.DHT22,self.pin)
        
        if self.sensor_type=='thermoset':
            return temperature
        else:
            return humidity
     


    
a1=Sensor('home/parkings/thermoset/thermo24',pin=31213243414312313241)

zarf=a1.read_sensor()
        
#turn_on()
#turn_off()

#read_sensor        

        
''' 
        


class Sensor:
    
    def __init__(self,topic):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.sensor_type=self.topic_list[2]
        self.sensor_name=self.topic_list[3]
        
    
    def read_sensor(self):
        #import numpy as np
        #a=np.random.unifrom(20,25)
        #return a
        
        return 25
    
    

a1=Sensor('home/parkling/thermoset/thermo456')
a1.location
a1.group #parking
a1.sensor_type
a1.sensor_name

zarf=a1.read_sensor()






#-----dewvice----------
#----sensor------









#*************************************
#*************************************
#*************************************
#------------FROM HERE----------------
#task2 , task3

class Sensor:   
    def __init__(self,topic):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.sensor_type=self.topic_list[2]
        self.sensor_name=self.topic_list[3]
    def read_sensor(self):
        return 25
    


class Device:
    def __init__(self,topic):
        self.topic=topic
        self.topic_list=self.topic.split('/')
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.device_name=self.topic_list[3]
        self.status='off'
        

    def turn_on(self):
        self.status='on'
        print(' Turn on , Done !')
    
    def turn_off(self):
        self.status='off'
        print('Turn off, Done!')
  
    
    def get_status(self):
        print(f'your device is {self.status}')




a1=Device('home/kitchen/lamps/lamps1')

#40 ta device besazi ????
a1=Device('home/kitchen/lamps/lamps1')

a1=Device('home/kitchen/lamps/lamps2')

a1=Device('home/kitchen/lamps/lamps3')

a1=Device('home/kitchen/lamps/lamps4')


a1=Device('home/kitchen/lamps/lamps5')

#nesfehso roshan koni
#nesfeshgo kahmosh koni cv hi?


#done done dastii????


#@class admin_panel-----------


#khone

#HOME --> GROUP

#PAKRING, WC , kitchen , main , room2

'''


groups = {}


groups = 
{
 
 parking : [d1,d2,d3,d4,d5,d6]
 
 kitchen : [d1,d3,d4,d5,d65,]

 
 }


'''

class Admin_panel:
    
    def __init__(self):
        self.groups={}
        
    
    
    def create_group(self,group_name):
        
        if group_name not in self.groups:
            
            self.groups[group_name]=[]
            print(f'groups {group_name} crerated')
            
        else:
            print('your grouyp name is exist already')
            
            

            
   
        
a=Admin_panel()
        
a.groups  #{}


a.create_group('parking')  #groups parking crerated

mygp=a.groups
#{'parking': []}
a.create_group('wc')

a.create_group('room1')


mygp=a.groups

# {'parking': [], 'wc': [], 'room1': []}















class Admin_panel:
    
    def __init__(self):
        self.groups={}
        
    
    
    def create_group(self,group_name):
        
        if group_name not in self.groups:
            
            self.groups[group_name]=[]
            print(f'groups {group_name} crerated')
            
        else:
            print('your grouyp name is exist already')
            
            
            
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            
            self.groups[group_name].append(device)
            
            #print(f' {device.device_name is added to {group_name}')
            
        else:
            print(f'Group {group_name} is not exist')




        
a=Admin_panel()
        
a.groups  #{}


a.create_group('parking')  #groups parking crerated

a.create_group('wc')

a.create_group('room1')


a.groups 


a.groups['parking'] #[]


mydevice=Device(topic='home/kitchen/lamps/lamp123')


a.add_device_to_group('parking',mydevice)

mygp=a.groups


#hey device besazam hey add konm

class Admin_panel:
    
    def __init__(self):
        self.groups={}
        
    
    
    def create_group(self,group_name):
        
        if group_name not in self.groups:
            
            self.groups[group_name]=[]
            print(f'groups {group_name} crerated')
            
        else:
            print('your grouyp name is exist already')
            
            
            
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            
            self.groups[group_name].append(device)
            
            #print(f' {device.device_name is added to {group_name}')
            
        else:
            print(f'Group {group_name} is not exist')


    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            
            self.add_device_to_group(group_name, new_device)
            
            #pritnm ....
            #fdlean device b felan goroh ezaf shod

        else:
            print(f'Group {group_name} is not exist')
        
        
a=Admin_panel()
        
a.groups  #{}


a.create_group('parking')  #groups parking crerated
a.create_group('wc')
a.create_group('room1')
a.groups 

mydevice=Device(topic='home/kitchen/lamps/lamp123')
a.add_device_to_group('parking',mydevice)
a.groups
#{'parking': [<__main__.Device at 0x30f824080>], 'wc': [], 'room1': []}


a.create_device('wc','lamps','lamps23')

a.groups
'''
{'parking': [<__main__.Device at 0x30f824080>],
 'wc': [<__main__.Device at 0x30df9d190>],
 'room1': []}
'''


mygp=a.groups

print(type(mygp)) #<class 'dict'>

mygp.keys() #dict_keys(['parking', 'wc', 'room1'])

parking_list=mygp['parking']

mydevice=parking_list[0]

print(type(mydevice)) #<class '__main__.Device'>


mydevice.location #'home'

mydevice.turn_on() # Turn on , Done !







class Admin_panel:
    
    def __init__(self):
        self.groups={}
        
    
    
    def create_group(self,group_name):
        
        if group_name not in self.groups:
            
            self.groups[group_name]=[]
            print(f'groups {group_name} crerated')
            
        else:
            print('your grouyp name is exist already')
            
            
            
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            
            self.groups[group_name].append(device)
            
            #print(f' {device.device_name is added to {group_name}')
            
        else:
            print(f'Group {group_name} is not exist')


    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            
            self.add_device_to_group(group_name, new_device)
            
            #pritnm ....
            #fdlean device b felan goroh ezaf shod

        else:
            print(f'Group {group_name} is not exist')
        
        
    def create_multiple_devices(self,group_name,device_type,number_of_devices):
        if group_name in self.groups:
            for i in range(1,number_of_devices+1):
                device_name=f'{device_type}{i}'
                
                topic=f'home/{group_name}/{device_type}/{device_name}'
                new_device=Device(topic)
                
                self.add_device_to_group(group_name, new_device)
            
                #print
            
        else:
            pass
        
        
a=Admin_panel()
        
a.groups  #{}


a.create_group('parking')  #groups parking crerated
a.create_group('wc')
a.create_group('room1')


a.groups # {'parking': [], 'wc': [], 'room1': []}


a.create_multiple_devices('parking','lamps',40)

mygp=a.groups 


for group in mygp:
    
    for device in mygp[group]:
        print(device.device_name)


#***************REAL_WORLD******************************

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

class Device:
    def __init__(self,topic,mqtt_broker='localhost',port=1883):
        self.topic=topic
        
        self.topic_list=self.topic.split('/')
        
        self.location=self.topic_list[0]
        self.group=self.topic_list[1]
        self.device_type=self.topic_list[2]
        self.device_name=self.topic_list[3]
        
        
        self.mqtt_broker=mqtt_broker
        self.port=port
        
        
        #self.connect_mqtt()
        #self.setup_gpio()
        
        
    
    def connect_mqtt(self):
        self.mqtt_client=mqtt.client()
        self.mqtt_client.connect(self.mqtt_broker,self.port)
        
        #dar asl yek objecte alakiu tooye pythn ro
        #Miad vasl mikone
        
        #Ketabkhone
        #vasl mikone be yek device vaghe ei k ip port dare
        
        
    def setup_gpio(self):
        
        #agar lamp --> 17
        #agar dar --> 27
        #age fan --> 22
        #GPIO.setup(adad,GPIO.OUT)
        
        if self.devbice_type=='lamps':
            GPIO.setup(17,GPIO.OUT)
            
        elif self.devbice_type=='doors':
            GPIO.setup(17,GPIO.OUT)
            
        elif self.devbice_type=='fans':
            GPIO.setup(22,GPIO.OUT)
            
        #elif ---> 

    def turn_on(self):
        self.send_commands('TURN_ON') 
        print(' Turn on , Done !')
        #dastoori inja bnvisam k bre va roshan kone
        
    
    def turn_off(self):
        self.send_commands('TURN_OFF')
        print('Turn off, Done!')
  
    
    def send_commands(self,command):
        self.mqtt_client.publish(self.topic,command)   
        print('done')


       







#************************************************
#********************FINAL************************

class Admin_panel:
    
    def __init__(self):
        self.groups={}
        
    
    
    def create_group(self,group_name):
        
        if group_name not in self.groups:
            
            self.groups[group_name]=[]
            print(f'groups {group_name} crerated')
            
        else:
            print('your grouyp name is exist already')
            
            
            
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            
            self.groups[group_name].append(device)
            
            #print(f' {device.device_name is added to {group_name}')
            
        else:
            print(f'Group {group_name} is not exist')


    def create_device(self,group_name,device_type,name):
        
        if group_name in self.groups:
            
            topic=f'home/{group_name}/{device_type}/{name}'
            new_device=Device(topic)
            
            self.add_device_to_group(group_name, new_device)
            
            #pritnm ....
            #fdlean device b felan goroh ezaf shod

        else:
            print(f'Group {group_name} is not exist')
        
        
    def create_multiple_devices(self,group_name,device_type,number_of_devices):
        if group_name in self.groups:
            for i in range(1,number_of_devices+1):
                device_name=f'{device_type}{i}'
                
                topic=f'home/{group_name}/{device_type}/{device_name}'
                new_device=Device(topic)
                
                self.add_device_to_group(group_name, new_device)
            
                #print
            
        else:
            pass
        
        
        
    #a1.turn_on_all_in_group('wc')
    
    
    def turn_on_all_in_group(self,group_name):
        
        if group_name in self.groups:
            #yek list behet pas mide
            all_devices=self.groups[group_name]
            
            for device in all_devices:
                device.turn_on()
                
                #print
                
        
        
        else:
            pass
        
    
    
    def turn_off_all_in_group(self,group_name):
        '''
        khamoosh kone
        '''
        
        
    def trun_on_all(self):
        '''hameye device haro roshan kone'''
        pass
        
    def turn_off_all(self):
        '''hameye devcie haro khamosh kone'''
        pass
    
        
#parking

#print kone hameye device haee k onto hastan
#status , off one
    def get_status_in_group(self,group_name):
        
        '''living_room y matn print mikone mige lamp1 on , klamp2 off , lamp3 ,..'''
        pass
    
    
    #20 ta lamp wc, 30 lamp main hall, 40 ta parking
    
    
    def get_status_in_device_type(self,device_type):
        
        ''' device=lamps --> tamame lamp haro status mohem nabashe tooye living rome kojas'''
        pass
    
    
    def create_sensor(self) :
    #bar asase clASS SENSOR argument bzarid
        pass
    
    
    #read_sensor()
    def get_status_sensor_in_group(self,group_name):
        
        '''
        
        sensor haye yek goroh ro biad doone dooen status ro pas bde
        
        '''
        pass
        
        
    
    
    

