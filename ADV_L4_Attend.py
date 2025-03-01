"""
In The Name of God

Created on Sun Feb 23 17:27:59 2025

@author: apm


ADV_L4_Attend



"""


'''

review


human ----- python ---- machine


python --> zaban kalamat 



reserved-------
1-python built in function ( print(),input(),len(),)
max() min() pow() abs()
narenji


2-keywords -->dastooor
banafsh msihan



unreserved---------
sefid---> esme zarf

variables
1-numbers (int.float.complex)
** * / + -

== > < != --> True False
2-Bool

3-Str --> reshte qoutation
a=..
a[index]
a[start:end+1:step]
a.str function -->khoroji midadan , taghir emal nmikrd
a.upper()  a.lower() a.replace()
a.find('a')  a.count('b')
a.isupper()


4-iterables --> chanta variables
4.1. list --> ordered, changable , allow duplicated
a=[el1,el2,el3]
a[index]
a[start:end+1:step]

a[index]=new_value

list.functin
a.insert(index,element)
a.append(element)
a.remove(element)
a.pop(index)
a.clear() --> []


4.2. tuple --> data base --> 
ordered, unchangable , allow duplciated
a=(el1,el2,el3,el4)
a=(el1,)

a[index]

a[index] === XXXXX

a--> list(a) ->a[index] --> tuple(a)


4.3. set --> unordered(index ndre) , unchangable , duplciated

-->duplciated (tekrari hazf koni)
a={10,2,30,40,50}
a[chi mikhay bzri?] -->access --> taghir bdi


4.4. dictionary
mese list
ordered[bejay eindex , key] , changable , allow duplciated
b=[value1,value2]
b[0]

a={'key1':'value1' , 'key2':'value2'}
a['key1']

#change
a['key1']='new_value'


a['new_key']='new_value'







'''





sen=int(input('salam seneto begoo:'))


if sen>20:
    print('salam')






print('khodafez')




'''
KEYWORDS----------------

SHARTIIII------------

just if

age in shart treu shod kare  1 ro bokon


shart --> az chizaee mese == =! > <
tbae ---> str function isupper()


age true --.dastoor1
age falae --> dastoroo ejra nmikone



if shart:
    dastoore1


#yek dastoor?


if shart:
    dastoore1
    dastoore2
    dastoore3
    dastoore4
    dastoore5
    dastoore6
    dastoore7
    dastoore8
    dastoore9
    
    


#yek shart?


har dota shart bayad true beshe
va

if shart1 and shart2:
    daastooor1
    dastoor2
    ....
    
    
#hadeghal yekdomesh true bshe
ya 

    
if shart1 or shart2:
    dastoor1
    dstoor2
    
    
    
#just IF
--> age shart TRUE bodo --> dastooro ejra kon
age true nabdo ? -->bema che 
    
    
    
    
age shart True bood dastore 1 ro ejra kon

age nabod (FGalsae)---> hich
    
if sen>20:
    pritn(salam)





---> dorahi besazi

shart (condition)



age true bood -->kare 1
age false bood -->kare 2


if else



if shart:
    dastor1
    
else:
    dastoor2
    


'''


sen=int(input('salam seneto begoo:'))



if sen>20:
    print('salam')

else:
    print('shoma mojaz nisti')



#----

sen=int(input('salam seneto begoo:'))
if sen>20:
    print('salam')

else:
    print('shoma mojaz nisti')
     
print('khodafez')




#-------------------
sen=int(input('salam seneto begoo:'))


if sen>20:
    print('salam')

elif sen>18:
    print('2 sal dg toam bozorg mishgi')
    
    
    
#>20 --> salam

#19-->2sal dg toam bzoorg mishi

# 15 ---> hichi nminevise

sen=int(input('salam seneto begoo:'))


if sen>20:
    print('salam')
    
elif sen>18:
    print('2 sal dg toam bozorg mishi')
    
else:
    print('shoma mojaz nistid')

#>20 --> salam

#19 --> 2 sal dg toam bzoorg mishi
#<18 ---> shoam mojaz nistid




#============

sen=int(input('salam seneto begoo:'))


if sen>18:
    print('salam')


elif sen>16:
    print('2 sal dg toam bozorg mishgi')
    

print('moafagh bashi')






code=input('salam code mahsool:')
name=input('salam name mahsool:')
price=input('salam  gheymate mahsool:')

#== > < >= <= 
#==True

#tavabe estefade koni -> miad check mikone
#isdigit()  -->True 
if price.isdigit():
    text=f'''
    
    ------plutus-------
    product code: {code}
    product name: {name}
    
    Total Price : {price*0.7}
    
    '''
    
    answer=input('do you confirm that ? (yes/no) :')
    
    
    if answer.lower().strip()=='yes':
        print('submit shod')
        
    elif answer.lower().strip()=='no':
        print(' chera yes nazadi? che chizi moshkel dare')
    else:
        print('javabe shoma na yese na no , yes ya no avred konid')
    
    
    '''
    
    if answer=='yes':
        print('submit shod')
    
    
    if answer=='no':
        print('chra nist')
        
    '''
    
    
    
    
    #-------------
    '''
    
    if answer=='yes':
        print('submit shod')
    
    
    
    
    
    if answer=='no':
        print('chra nist')
        
        
    else:
        print('shoma bayad yes ya no bnvisid')
        
        
        
        
    '''
    
    
    

else:
    print('motasefane ghalat adad vared krdid jaye price')







#---------------------
'''
------reserved------------
------------keywords--------------

gozare haye sharti----

    --just if
    -- if else
    - if elif 
    - if elif else
    
  
    
--------halghe-------
While-----
for-------


    
  
'''


'''
while--->


shomarande besaze i , j , k , --->zarf kocholo
0 --> ta ye adad hey bre ziadesh kone


i= #adade avalie -->  

while shart:
    
    dastooori k mikhay adi nabashe, halghe
    
    khateme 
    
    
    
shorooo
while shart:
    dastoor
    khateme




shart --> shart and or not ,.....
dastooor 
khateme va ....



'''


i=0
while i<10:
    print('salam')
    
    i=i+1

#---> 10 ta salam 



'''

i=0

while i<10 --> True --> salam --> i=0+1=1

i<10 --> True --------> salam --> i=1+1=2

i<10 --> True --------> salam --> i=2+1=3

i<10 --> True --------> salam --> i=3+1=4

i<10 --> True --------> salam --> i=4+1=5

i<10 --> True --------> salam --> i=5+1=6

i<10 --> True --------> salam --> i=6+1=7

i<10 --> True --------> salam --> i=7+1=8

i<10 --> True --------> salam --> i=8+1=9

i<10 --> True --------> salam --> i=9+1=10

i<10 -> 10<10 --> False --> miad biroon


edameye koodoooo

'''



i=0

while i<10:
    print('salam')
    i=i+1
    


print('hi hi hi')



#----------
#rahatesh koni

i=0

while i<10:
    print('salam')
    i=i+1
    



#i ?? estefade krdm? naaaa
#ama whiel baraye

i=0

while i<10:
    print(i)
    i=i+1
    
    
    
i=0

while i<10:
    a=i
    b=i+1
    c=b*a
    i=i+1
    
    

    
    
    
    
'''

i=start
while i<end:
    dastooooor
    i=i+step
    


for i in range(start,end,step):
    dastooor
    
    
'''

#beri dakhele ye chizi


# range () --> 



'''

mantegh mese while


i=0 --> anjam mide ssaatoor
i=1 --> dnajam mdie
i=2



...



[ , , ,, , ,, ,  ] i o hey mizre


range(0,10) --> |0,1,2,3,4,5,6,7,8,9|



for i in range()



for i in |0,1,2,3,4,5,6,7,8,9|


for i in anyh iterables ??


a=[]
dictionary
tuple



'''



users=[10,20,30,40,50,60]

for i in users:
    print(i)


'''

i-->10   , print(i) --> print(10 )--->10
i-->20  , print(i) -->print(20)-->20


30 , 40 , 50 ,60


10
20
30
40
50
60


'''

users=[10,20,30,40,50,60]

for i in users:
    print('salam')

'''

10 -->dastoor
20 -->dastooor
30 dastooor
40 dastooor
50 dastooor
60 dastoooor


dastoor--> i --> salam




salam
salam
salam
salam
salam
salam


'''
for i in users:
    print('salam')
    
'''
salam
salam
salam
salam
salam
salam
'''
    
    
    
    
    
    

for i in users:
    print(i)

#be ezaye har i tooye users i ro print mikone

'''
10
20
30
40
50
60

'''




#0 1 2 3 4 5 




users=[10,20,30,40,50,60]

for i in users:
    print(i)

'''

i--> 10    print(i) --> 10


'''

users=[10,20,30,40,50,60]

for i in users:
    print(users[i])
    

'''
i-->10 , print ( users[10])



'''


users=[10,20,30,40,50,60]

for i in users:
    print(users.index(i))
    
'''
0
1
2
3
4
5
'''



users=[10,20,30,40,50,60]

#i --> 0 1 2 3 4 5 

for i in range(0,len(users)):
    print(i)

'''
0
1
2
3
4
5
'''

    
for i in range(0,len(users)):
    print(users[i])

'''
10
20
30
40
50
60

'''




#---while
#-----for


#pass
#continue
#break

#pass


for i in range(0,10):
    pass
    


#pass , break, contrinue --> for , while (if) 
    

for i in range(0,10):
    
    print(i)
    


for i in range(0,10):
    
    print(i)
    
    if i ==5:
        break

'''
0
1
2
3
4
5

'''

for i in range(0,10):
    if i ==5:
        break
    
    print(i)
    
'''
0
1
2
3
4

'''
for i in range(0,10):
    
    print(i)
    
    
    
for i in range(0,10):

    if i ==5:
        continue
    
    print(i)

'''
0
1
2
3
4
---->nmist
6
7
8
9

'''
for i in range(0,10):
    print(i)
    if i ==5:
        continue
    
'''
0
1
2
3
4
5
6
7
8
9

'''



'''
pass--> nime kare

break--> tooye for, while  -->if --behesh resid bepare biron az kole halghe
edame nade beshkoon

continue--> edame bede
bepar skip ignore kon


'''


#----------FOR KARBORDI---------

#--> for 
#dzakhele ye iterable -->iteration
#miri tak tak migrdiish 


p_list=[10,20,30,40,50,60]



for i in p_list:
    print(i)

#---> i ewlementate
#-->i et indexas


for i in range(len(p_list)):
    print(p_list[i])


'''
10
20
30
40
50
60

'''


#----> check koni --> agaro shorot --> if

#i==
#len(i)
#i/2

#i%2==0
#i%2!=0

#i=='vahid'

#1---> ya mikhay beshmorii too ye list
#2->jodash koni
#3--->hazf konim


'''

iteration in list
checdk teh condition 
        1-count
        2-seperation
        3-remove
        
    
for
if
    1-
    2-
    3-
    
'''


'''

dar yek list check kon harkodom balaye 25 bashe adad
beshmor
'''


p_list=[10,20,30,40,50,60]


for i in p_list:
    if i>25:
        print(i)
        
        
        
        
        
        

#---> for i in range(len(p_list))
#i--> p_list[i]




p_list=[10,20,30,40,50,60]

count=0


for i in p_list:
    if i>25:
        count=count+1
        


print(count) #4

# in count -->tedade element haye tooye listete ke
#shartet true shode

#i>25 --> 4 ta az elemnet haye tooye listam
#bozporgtar az 25
        
    
p_list=[10,20,30,40,50,60]

count=0


for i in p_list:
    if i>35:
        count=count+1
        print(i)
        
        

#joda konm
#iteration for
#if --> cxheck
#--> 1count
#2-->true nahmori ->


p_list=[10,20,30,40,50,60]

mylist=[]

for i in p_list:
    if i>25:
        
        #i --> i oon elementie k i>25
        
        mylist.append(i)
        
        


print(mylist)
#[30, 40, 50, 60]





#3--->
p_list=[10,20,30,40,50,60]

for i in p_list:
    if i>25:
        #i --> i oon elementie k i>25
        p_list.remove(i)



print(p_list)


#i --> 0 1 2 3 4 5


p_list=[10,20,30,40,50,60]

for i in range(len(p_list)):   
    #if i>25:
    if p_list[i]>25:
        p_list.remove(p_list[i])
        
        





p_list=[10,20,30,40,50,60]

mylist=[]

for i in p_list:
    if i<25:
        
        #i --> i oon elementie k i>25
        
        mylist.append(i)
        
        
print(mylist)



#------


#--------------(1)-----------------------
p_list=[10,20,30,40,50,60]
count=0
mylist=[]
removed_list=[]

for i in p_list:
    
    if i>25:
        
        print(i)
        count=count+1
        mylist.append(i)
        
    else:
        removed_list.append(i)
        
        
#p_list=[10,20,30,40,50,60]

#p_list=[100000,20,30,40,50,60]


#i=p_list[0]

#while i<p_list[-1]:
    
    













listt = [10, 20, 30, 40]

mylist=[]

for i in listt:
    if i>30:
        #mylist.append(i)
        listt.append(i)
        
        
    
    
    
    
#while



    
    

#-------------(2)-------------------
p_list=[10,20,30,40,50,60]
count=0
mylist=[]
removed_list=[]

for i in range(len(p_list)):
    #0 1 2 3 4
    if p_list[i]>25:
        print(p_list[i])
        count=count+1
        mylist.append(p_list[i])
        
    else:
        removed_list.append(p_list[i])




i=0
count=0
mylist=[]

while i<len(p_list):
    if p_list[i]>25:
        print(p_list[i])
        count=count+1
        mylist.append(p_list[i])
        
    else:
        removed_list.append(p_list[i])
    
    
    i=i+1



#------ta zamani ke
#while tue



#while True:
    
#    print('salam')



#begam ta abad anjam bede magar inke ??



#while true:
    #dastoooor
    
    #shart -->if
    #break
    
    
    
#aksaran


'''


agah ta zamani k taraf felan nkrde felan kon


ta zamani k trf felan mikone felan kon


while true --->hey tekrar she
bi shartt bdone choono chera
maagr ine felan bshe dg ejra

'''


#-------------------------------------------
p_list1=[10,20,30]
p_list2=[40,50,60]
p_list3=['ali','vahid','reza']

for i in p_list1,p_list2,p_list3:
    print(i[2])
#-------------------------------------------



code=input('salam code mahsool:')
name=input('salam name mahsool:')
price=input('salam  gheymate mahsool:')


#true

#ta zamani k adad vared nakarde

#adad vared nakardan = True

#not isdigit()
#varede halgeh nmish
while not price.isdigit():
    
    print('shoma bayad adad vared konid')
    price=input('lotfan gheymate mahsool ro besorate adad bezanid:')
    




price=float(price)

text=f'''

------plutus-------
product code: {code}
product name: {name}

Total Price : {price*0.7}

'''

print(text)






#man mikham hey price --> 
#ta zamani k trf doros adad vared nakarde 
#hey azash price bgirm

#magar inek adad vared kone







code=input('salam code mahsool:')
name=input('salam name mahsool:')

while True:
    price=input('salam  gheymate mahsool:')
    
    if price.isdigit():
        break
    
    print('lotfan adad vared kon !!!')
    
  
price=float(price)

text=f'''

------plutus-------
product code: {code}
product name: {name}

Total Price : {price*0.7}

'''

print(text)






'''

TASK1---->

answer---> = agah confrim mikoni ya na
ta zamani k trf 
ag zad yes bege syubmit
age zad no 
ta zamani k yes bzne hey azash dobare
name code price 





TASK2--->
default 

price ghabl az hamechii
ag trf price ro farsi zad
bayad in ghabool kone
va englisi namayuesh bde


code : n100
name: nvidia
price ۱۳۰۰


price=float(price)
ba float na
ba yek reshte code ghable float

a='۱۰۰۰'

tabdilesh kon b

1000

khodet bdone komak az itn floay






'''









