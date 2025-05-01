#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 20:53:50 2025

@author: apm
"""

import tkinter as tk
from tkinter import ttk, messagebox

import numpy as np


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
                
              






class SmartHouseApp:
    def __init__(self, root):
        #taziiiinnnn
        #self.panel=None
        
        self.root = root
        self.root.title("Smart House Manager")
        
        #---------------------------------------------------
        #---------------------------------------------------
        # Group Frame
        
        group_frame = ttk.LabelFrame(root, text="Group Management")
        group_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        
        #sartitr
        ttk.Label(group_frame, text="Group Name:").grid(row=0, column=0, padx=5, pady=5)
        self.group_name_entry = ttk.Entry(group_frame)
        self.group_name_entry.grid(row=0, column=1, padx=5, pady=5)
        #ttk.Button(group_frame, text="Create Group",command=self.create_group).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(group_frame, text="Create Group",command=self.mygroup).grid(row=0, column=2, padx=5, pady=5)




        #---------------------------------------------------
        #---------------------------------------------------
        
        
        # Device Frame
        device_frame = ttk.LabelFrame(root, text="Device Management")
        device_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        ttk.Label(device_frame, text="Group:").grid(row=0, column=0, padx=5, pady=5)
        self.device_group_entry = ttk.Entry(device_frame)
        self.device_group_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(device_frame, text="Type:").grid(row=1, column=0, padx=5, pady=5)
        self.device_type_entry = ttk.Entry(device_frame)
        self.device_type_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(device_frame, text="Name:").grid(row=2, column=0, padx=5, pady=5)
        self.device_name_entry = ttk.Entry(device_frame)
        self.device_name_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(device_frame, text="Add Device").grid(row=3, column=0, columnspan=2, pady=5)


        #---------------------------------------------------
        #---------------------------------------------------
        
        
        # Multiple Device Frame
        devices_frame = ttk.LabelFrame(root, text="Multiple Devices Management")
        devices_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        ttk.Label(devices_frame, text="Group:").grid(row=0, column=0, padx=5, pady=5)
        self.devices_group_entry = ttk.Entry(devices_frame)
        self.devices_group_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(devices_frame, text="Type:").grid(row=1, column=0, padx=5, pady=5)
        self.devices_type_entry = ttk.Entry(devices_frame)
        self.devices_type_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(devices_frame, text="Number:").grid(row=2, column=0, padx=5, pady=5)
        self.devices_name_entry = ttk.Entry(devices_frame)
        self.devices_name_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(devices_frame, text="Add Multiple Devices").grid(row=3, column=0, columnspan=2, pady=5)



        #---------------------------------------------------
        #---------------------------------------------------
        
        # Control Frame
        control_frame = ttk.LabelFrame(root, text="Controls")
        control_frame.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        ttk.Label(control_frame, text="Group:").grid(row=0, column=0, padx=5, pady=5)
        self.control_group_entry = ttk.Entry(control_frame)
        self.control_group_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(control_frame, text="Turn ON Group").grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(control_frame, text="Turn OFF Group").grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(control_frame, text="Check Status").grid(row=1, column=2, padx=5, pady=5)
    
    def mygroup(self):
        
        zarf=self.group_name_entry.get()
        
        a=admin_panel()
        a.create_group(zarf)    
        
        messagebox.showinfo("Success", f'Group "{zarf}" created!')
        
    




if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHouseApp(root)
    root.mainloop()




