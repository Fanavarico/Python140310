
"""

In The Name of GOD

Created on Wed Feb 19 17:19:43 2025

@author: Ali Pilehvar Meibody


ADV_L3_Attend




"""


'''

Human (english) ---python ----machine (0,1 binary)

python---> vocabs


reserved-----------------
1-python built in functions (---> tabe haye dkaheli)
baraye hame bekar miran
narenji--> () dakheelsh tanzimat ya vorodi
khoroji ya yek amalkardi

print()
print(, , , , , )
input()   [str behet barmugrdone]

int()
float()
str()
list()

max()
min()
sum()

len()
type()


2---keywords----
if else elif for while ,...
manteghi (logic)




unreserved---------------
harchi benevisi-->sefid--.esme zarf

esme zarf( ghavanin , adad bzari avalesh,m chaaracter _ ,...)

esme zarf --> mojtaviat (value)

value -->cchan no


1----numbers-----
1.1.int --> 2 4 5 2323

1.2.float -->ashari .00 

1.3. compelx
1+2j


** * / + - % -->computational operator
=

a+b = c


c= a+b


moghayese -->soal miporsi-->javab behet pas
True False

== auya barabar ahst
>
>=
<
<=
!=

2.Boolean (True , False)


3-->string (reshte ) reshte e az charcter ha

a=' quotation'
a=str('')

a[index] index az 0

a[start:end+1:step]

a[4:9]  4 5 6 7 8  1 done done

a[4:13:2]  4 6 8 10 12

str functions --> functions haee hast k mokhtaese
frgh dre ba python built in function
rnagi nmsihe az biron gozshte nmsihe
dot bezni


name='ali'

name.upper()

emal nmsihe rooye name
khrooji mide-->zkahires


3no khoroji str ufnction1
1-->conveert
upper()  lower() title() capitalize() replace(old,new)

2-->adad mide
.find(characteri k mikhay) -->indexe
.count(characteri mikhay ) -->tedaxdeshp


3--->True False--.check koni
is 
start

islower()  True false
isupepr()
isdigit()


4-chanta chizi zakhrie -> Iterables

List --> changable, ordered, allow duplicated
a=list()
a=[]

a[4:6]
list function
a.insert(index,element)
a.append(element) b tahehs ezaf mikone
a.pop(index)
a.removbe(element)


tuple --> unchanble
a=()
a=(10,)
tuple function
databae -->sql 
a-->tuple -->list change --> tuple


set--> unchanble, unorder , duplicated
a={}
yadetam bashe to esdekham kalameye
duplicated ro hazf kon

list --> koli taghir roosh bdi
badesh --> set()



dictionary-->
index     value
0 
1
2
3



keys    values
mokhafaf


dictt={'key1' : value1 , 'key2':value2}
dictt['key1']

dictt['key1']=new_value

dictt['new_key']=new_value


'''



'''
LOGHAT NAME VASE KHODEMON-------


POROZHE
POROZHE AZ KASI GRFTI
POROZHEYE SHERKAT
IDEA -->STARTUP




FARSI -----> PYTHON




zakhire kardan---> variable (str,...list,functions,...)
namayesh dadan --> print()
begire , voroodi-->input()




'''

# 3 ta chiz begire
# code, name , price
#namayesh bde


code=input('salam codee mahsoleton ro befarmaeed:')
name=input(' name mahsoleton ro befarmaed:')
price=input('gheymate mahsoleton ro befarmaed:')


text=f'''

-----plutus management--------

Product code : {code}
product name: {name}

price:  {price}


'''

print(text)




#======================

p_list=[]

code=input('salam codee mahsoleton ro befarmaeed:')
p_list.append(code)


name=input(' name mahsoleton ro befarmaed:')
p_list.append(name)

price=input('gheymate mahsoleton ro befarmaed:')
p_list.append(price)


#print(p_list)
#['l100', 'nokia', '1000']

text=f'''

-----plutus management--------

Product code : {p_list[0]}
product name: {p_list[1]}

price:  {p_list[2]}


'''

print(text)


#=====================================
p_list=[]
p_list.append(input('salam codee mahsoleton ro befarmaeed:'))
p_list.append(input(' name mahsoleton ro befarmaed:'))
p_list.append(input('gheymate mahsoleton ro befarmaed:'))
text=f'''

-----plutus management--------

Product code : {p_list[0]}
product name: {p_list[1]}

price:  {p_list[2]}


'''

print(text)



#=====================================
code=input('salam codee mahsoleton ro befarmaeed:')
name=input(' name mahsoleton ro befarmaed:')
price=input('gheymate mahsoleton ro befarmaed:')


text=f'''

-----plutus management--------

Product code : {code}
product name: {name}

price:  {price*0.7}


'''

print(text)





'''
a=1000

b= a - (30/100)*a
b= (70/100) * a
b= 0.7 * a



a=1000
b='1000'

print(a==b) #False

print(type(a)) #<class 'int'>
a/10 #100.0

print(type(b)) #<class 'int'>
#b/10 #TypeError: unsupported operand type(s) for /: 'str' and 'int'

#salam/10 -->ssal

b='1000'

c=int(b)

print(c==a) #True
print(type(c)) #<class 'int'>
c/10 # 100.0
'''





#=====================================
code=input('salam codee mahsoleton ro befarmaeed:')
name=input(' name mahsoleton ro befarmaed:')
price=float(input('gheymate mahsoleton ro befarmaed:'))
#'1000' --> 1000.0

text=f'''

-----plutus management--------

Product code : {code}
product name: {name}

price:  {price*0.7}

do you confirm it?
'''

print(text)














'''
LOGHAT NAME VASE KHODEMON-------


POROZHE
POROZHE AZ KASI GRFTI
POROZHEYE SHERKAT
IDEA -->STARTUP




FARSI -----> PYTHON




zakhire kardan---> variable (str,...list,functions,...)
namayesh dadan --> print()
begire , voroodi-->input()
AGAR --> if




'''



print('salam')



print('welcome')


'''

hadaf--> yek khat codetoo
shart bezari
begi agha in khat ro dar yek soorat ejra kon


shart --> oon khat ro shartri krdi

ghbalesh bayad yek chizi benvisi --> if


if shart:
    dastoo1
    dastoor2
    dastoor3


    
    
    
    
    
   
    
if shart:
    in codo boro jolo
    
    
    
shart --> bayad yek chizi bashe k jjavabesh
True ya false bashe


==
>
<
>=
<=
!=


    
'''



print('welcome')


if True:
    print('welcome')



#print('welcome')



if False:
    print('welcome')




a=40
b=10

if a>b:
    print('welcome')
    





print('welcome')




'''



AGAR --> 

agar felan shod felan kon

age nashod chi? -->veelsh kon


just if


#----------
age nashod ham felano kon


aqge shart sahih shode kare 1 kon
age nasahod?-->veelesh kon
if shart:
    kare1
    karre2
    kare32
    kare4
    
    
    
if dorahi --> do rah mikha

age shod kar 1 kon
age nashod (dg nago bikhial) kare 2 ro kon


if shart:
    karhaye1
    ...
    ...
    ...
    
else:
    kare hay edg
    kara
  
    
  
    
  
    
do rahi dari

if shart:
    karfe1
    kare2
    akre3
    
else if shart:
    
    
    else:
        
        
        
else if
elif -->shart 

'''




'''

tooye body (badane) dastoor bedi

if shart:
    d1
    d2
    d3
    d4
    d5
    d5
    d6
    d67
else:
    d1
    d2
    d2
    d34
    
    
shart??

vchanta shart bedi


hatman hameye shartat bayad doros True

and 

if shart1 and shart2:
    
    
    
agar hade aghal yedonash (ya)

or

if shart1 or shart2:
    
    



'''


a=40

if a:
    print('salam')


#sharte -->ag yek variables bezari shart hesab mikone


#aya a None nist?

#ag a none naabshe --> true




a=40

if a:
    print('salam')



a=None

if a:
    print('salam')


#------------------------------
#answer -->

#ali


#age taraf nevesht ali 
#benevis salamn arz shod


'''
masale:
    agar taraf neveshte
    ALI ya ali
    barash benevis welcome
    
doita shart drm
ALI ali

-->
or

if shart1 or shart2:
    dastoor


'''


answer='ali'
answer='ALI'


answer='sdfuhsreiuhyfiudfhsiseruh'
#ali ya #ALI

answer=4243432324


if answer=='ali' or 'ALI':
    print('welcome')
    
    #answer=='ali'
    #'ALI'
    
    
   # if a -->a='ALI' true
   
   
if 'ALI':
    print('welcome')
    

#if a>10 or True:
#    print('salam')
    
    
    
    
    
#dota shart --> or and beyne dota shart 



if answer=='ali' or answer=='ALI':
    print('welcome')












#=====================================


code=input('salam codee mahsoleton ro befarmaeed:')
name=input(' name mahsoleton ro befarmaed:')
price=input('gheymate mahsoleton ro befarmaed:')
#agar taraf faghat adad zade bood inkaro tabdilesh konm b float



if price.isdigit():
    price=float(price)


    text=f'''
    
    -----plutus management--------
    
    Product code : {code}
    product name: {name}
    
    price:  {price*0.7}
    
    
    '''
    
    print(text)
    
    
    



else:
    print('lotfan adad vared konid, dobare emtehan konid')




#====================================

code=input('salam codee mahsoleton ro befarmaeed:')
name=input(' name mahsoleton ro befarmaed:')
price=input('gheymate mahsoleton ro befarmaed:')
#agar taraf faghat adad zade bood inkaro tabdilesh konm b float

#a is not
#a not in


if not price.isdigit():
    print('lotfan adad vared konid, dobare emtehan konid')

else:
    price=float(price)


    text=f'''
    
    -----plutus management--------
    
    Product code : {code}
    product name: {name}
    
    price:  {price*0.7}
    
    
    '''
    
    print(text)
    
















'''
LOGHAT NAME VASE KHODEMON-------


POROZHE
POROZHE AZ KASI GRFTI
POROZHEYE SHERKAT
IDEA -->STARTUP




FARSI -----> PYTHON




zakhire kardan---> variable (str,...list,functions,...)
namayesh dadan --> print()
begire , voroodi-->input()
AGAR --> tooye if ha
    agar khasti yekshrt bzari fght yek gheshri ro kari koni bahash --> just if
    agar na dorahi mikhay bzari --> if else
    agar dorahie ye rahe dgash dobare dorahie if elif elif elif




'''









code=input('salam codee mahsoleton ro befarmaeed:')
name=input(' name mahsoleton ro befarmaed:')
price=input('gheymate mahsoleton ro befarmaed:')
#agar taraf faghat adad zade bood inkaro tabdilesh konm b float

#a is not
#a not in


if not price.isdigit():
    print('lotfan adad vared konid, dobare emtehan konid')

else:
    price=float(price)


    text=f'''
    
    -----plutus management--------
    
    Product code : {code}
    product name: {name}
    
    price:  {price*0.7}
    
    
    '''
    
    print(text)
    


#========================================
#========================================
code=input('salam codee mahsoleton ro befarmaeed:')
name=input(' name mahsoleton ro befarmaed:')
price=input('gheymate mahsoleton ro befarmaed:')


if not price.isdigit():
    print('lotfan adad vared konid, dobare emtehan konid')

else:
    price=float(price)

    text=f'''
    
    -----plutus management--------
    
    Product code : {code}
    product name: {name}
    
    price:  {price*0.7}
    
    
    '''
    
    print(text)

    answer=input('aya information haro taeed mikonid? (yes/no):')
    
    #agar shod --> agar nashod felan karo --> if else
    
    if answer=='yes':
        print('sabt shod')
        
    else:
        print('motasefane sabt nashod, dobare emtehan kon')
        
     
        
a='yes'
b='yes '
b.strip()
print(a==b) 
    
    
c='Yes'

print(a==c)


c='YES'
D='Yes'
e='yeS'
f='yEs'
g='yES'
    
    


#========================================
#========================================
code=input('salam codee mahsoleton ro befarmaeed:')
name=input(' name mahsoleton ro befarmaed:')
price=input('gheymate mahsoleton ro befarmaed:')


if not price.isdigit():
    print('lotfan adad vared konid, dobare emtehan konid')

else:
    price=float(price)

    text=f'''
    
    -----plutus management--------
    
    Product code : {code}
    product name: {name}
    
    price:  {price*0.7}
    
    
    '''
    
    print(text)


    answer=input('aya information haro taeed mikonid? (yes/no):')
    
    #agar shod --> agar nashod felan karo --> if else
    
    if answer.strip().lower()=='yes':
        print('sabt shod')
        
    else:
        print('motasefane sabt nashod, dobare emtehan kon')
        









'''
LOGHAT NAME VASE KHODEMON-------

FARSI -----> PYTHON

zakhire kardan---> variable (str,...list,functions,...)
namayesh dadan --> print()
begire , voroodi-->input()
AGAR --> tooye if ha
    agar khasti yekshrt bzari fght yek gheshri ro kari koni bahash --> just if
    agar na dorahi mikhay bzari --> if else
    agar dorahie ye rahe dgash dobare dorahie if elif elif elif




Python built in functions-----
print() input( ) len() .....


keywords------
if , else , elif , and , or , not


halghe
'''



print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')


#b in kari k shoam bekhay tekrar anjam bdi


#migan shoam niaz b halghe darii

'''

halghe chie tooye python???

while
for




hamashoon

mian injoorie az zzaben C oomde jolo

while





'''



'''
tekrar koniiii

sakhtar


shomarande ee --> in yechizi hast k
b python mige man kojaye halgham
ejaz emid epython k befahme tekrar chie

'''





if a>10:
    print('salam')




#for:
    #dastoor




#----------------------------
'''

1-->shomarande
2--> shart
3--->dastooor
4-->boro halgehye bad


'''

#in adad ro harchi mitoni bzri 
#0 , 5 , 56 

#ta zamani ke in shart dorost bashe
#kare paeen ro bokon (dastoor)
#shart -_> True , False


#ta zamani k in shart True bood kare paeno bokon




i=0

while i<10:
    print('salam')
    
#------- pas chikar bayad konm?


#shart?--->shart gozashti k yeja 
#ke hey mire too micharkhe barmigrde
#sharto check kone nare dg too


i=0
while i<10:
    print('salam')
    i=i+1





#---------------

i=20
while i<10:
    print('salam')
    i=i+1
    
    
     
while i<10:
    print('salam')
    i=i+1



#============
#while -->ino msihnase python
#i , dastoor mishnase na hichii

#while

'''
shomarande= start

while shart:
    dastoorateto midi .....
    yek kari koni k yejor az shart baid biron
    


while---> halghe -->tekrar

1-->shomarande mikhad
2--->shart mikhad k bege ta zamani k (sharte payane halghe)
3-->dasstoor mikhad
4-->yek kar kone k halgeh yeja be payan brse




'''



i=0
while i<10:
    print('salam')
    i=i+1

#i hey taghir nmikone? pas
#gahan too bazi application ha ham
#mitoni az khdoe i ham estefse koni


i=0 #1***
#2**
while i<10 :
    print(i)
    i=i+1


#az 0 ta yeki monde b 10 -->1 done done boro?




#-------sade tar -->rahe sade tar

#range(1**,)
for i in range(0,10,1):
    print(i)


for i in range(0,10,1):
    print('salam')
#$har bar
#ba manteghe i
#i=0 
#salam

#i=1
#salam

for i in range(0,10):
    print('salam')




i=0 
while i<10 :
    print(i)
    i=i+2

'''
0
2
4
6
8
'''



for i in range(0,10,2):
    print(i)
    
'''
0
2
4
6
8

'''



for i in range(10):
    print(i)

#range(end)

#range(start,end)

#range(start,end,step)



#range --> 0 1 2 3 4 5 6 7 8 9 10

#i tooye 0 1 2 3



#range--->

#boro dkahele ye list
#boro dakhele yek str
#broo dakhele set
#dictionary


#varresii

#iteration


#for i in range(0,10)
#[0 1 2 3 4 5 6 7 8 9 10]
#done i=09



a_list=[10,20,30,40,50,60]



for i in a_list:
    print('salam')
    
#iterawtion-->


for i in a_list:
    print(i)





for i in a_list:
    
    if i>30:
        print(i)



'''


tekrar ---> while , for

entehat shart dare, fix --> while


age mikhay iteration koni --> for




'''







'''



task1----> oonjae k mire check mikone
ke taraf adad vared karde ya na
hey done done ta zamani k taraf adad vared karde
hey bege agah adad vared kon


task2--->
age No --> dobare process az aval shoro she
yani code , name , price





'''







       
     
    
