
"""
In The name of GOD



Created on Sun Mar  9 20:07:22 2025

@author: apm

ADV_L5_Attend


"""


'''

review




human-----python------machine



reserved--------------
python built in fucntions(print,input,type,len,sum,max,min,pow)
(zip,)

https://docs.python.org/3/library/functions.html


keywords--->logic --.codo taghir midan
just if --> 
ifd else-->dorahi
if elif else

halghe ha -->tekrar
for --> iteration -->iterable, reshte,list, dictionary , if (print, count, new_list.append())
while --> sharti bzari bartaye ekhtetam (while true break)



unreserved---------------
sefid-->nemishnasam
numbers (int, float, complex ) --> + - * ** / % ,...
Boolean(True,Flase) , == != < <= > >=  is is not
str ---> quotaton , [index] , [start:end+1:step] ,str functions (.replace().count . upper()) 
iterables--> list, set , dictionary , tuple ---> 
[ indexing (order, adad, keys) , changable , allow duplicated]
listfunction ( .append() , .insert())




psudo code---->


'''


#a=2**3
#a=pow(2,3)

def myppow(numb1,numb2):
    
    answer=numb1**numb2
    return answer

a=myppow(2,3)





answer=input('aya confiorm meikoni? (yes/no):')


answer.upper().strip()

#Yes
#yES
# yes

#--> yes

answer='DBCA'



upper_case=['A','B','C','D'] #....
new_list=[]
upper_to_lowe_dict={'A':'a', 'B':'b','C':'c','D':'d'}


for i in range(0,len(answer)):
    if answer[i] in upper_case:
        new_list.append(upper_to_lowe_dict[answer[i]])
        

new_answer=''.join(new_list)
        


answer.lower()




#layer

#neuron

#interconnection

#optimization



'''


data ---> X ---> khoroji


'''


#from sklearn.neural_network import MLPRegressor
#model=MLPRegressor()
#model.fit(data)


#2 dalil


'''

tooye code khodet yek kario hey mikahy anjam bdi

hale tamrin

price -->farsi
englisi


for i in price:
    
    if i=='0':
        new_list.append('0')
        
        
        #....
        #...
        #>.
        #.....
        
        
        
new_price




def persian-to_english(numb):
    #
    #
    #
    #
    
    
    
    
    
persian_to_english()

#1.1--> behine code bzni
10 bar yuek kario dri hey az aval code nzni
balke yek esmo fght seda bzni

1.2.mitoni harjaeesh moshkel dahste bashe micropsystem
handle kardan , debug kardn hamechish raht tare



#-----------------
2---> ketabkhoej minevisan

code script-->kol tabe bzare
shoma fgth ba ye seda zadan btoonid azash estefade onid




*****HADAF --> BA YEK SEDA ZADAN 200 KHAT CODE EJRA BSHE


yeseri moteghayer ha too in 200 khat codo yejori bzari baghie
taghiresh bdn --> flexible bshe





'''
#----
#----



'''
**hamon ghavnini ro dare k varibale
reserved -->print open 
2
characteri joz _ , faslee *


step1-->besazish 
step2 --> estefade koni --> call sedash koni





#----------------***------------------



vorodiii ----> BOX ---> khoorji



#-------sakhtaneshe-------
def name(voroodi):
    
    badane
    
    
    khoroji




#----estefadash----
name(vorodi)





badane 



'''

#------practical (amali )--> tech 
#vorodi , badane(dastoorat) , khoorji



#---------vorodi dashte abshe ama khoroji na?
#-------------------------------
#1---->vorodi dare khroji nadare

def jam(a,b):
    c=a+b
    print(c)
    
    
    #return None
    
    
    
#tabe
jam(40,10)



#** print ba khoroji frgh dre
#khoroji zamani k
#betooni joloye tabe jae k seda mikoni y zarf bzri megdharesho brizi tozh


d=jam(40,10)

print(d) #None



#vorodi ham khorji

#jam=20

#definition
def jam(a,b):
    c=a+b
    #print(c)
    return c



#call

d=jam(20,30)

#d=tafrigh(20,30) #NameError: name 'tafrigh' is not defined
'''
*******
yek zarfi bname d misaze 
mosavi gharar mide ba (//////)

jam ---> aya jam yek adade?
d=a
d=c
d=jam
jam(

in yek tabe hast

barmigarde bala bbine hamchin tabe ee tarif shode ya na?
(dalile inke migan aval besaz, ghabel call ham baayd bzarisj
 )


m,ibine jam hast ytek tabast


jam(a,b) mige a v ab ro migire

a=20
b=30

c=a+b --> c =50


#-->a=20 , b=30 , c=50 
#print(c) --> print mikone

hanooz too dele tabeast 

return mirese barmigrde
be hamonaj k call shode

d=jam(20,30)

d=c

d=50

d-->50


'''


def jam(a,b):
    c=a+b
    print(c) #[print khoroji nist yek dastoore
    return c



#call

d=jam(20,30)



#3------vorodi ndshte bashs ekhoroji dahsste baahe>

def pi():
    return 3.14

a=pi()

#a=3.14




#4--na vorodi na khoroji?

def welcome():
    print('salam khosh amadi')
    
    
    
welcome()


a=welcome()

print(a)



#-------tabe beszi
#1---> na vorodi na khoorji welcome()
#2--->vorodi nadashgte bashe khoroji dashte bashe pi() -->3.14
#3-->vorodi dashte bashe khoroji nadashtebashe jam(a,b):print return None
#******4-->ham vorodi ham khoroji --> jam(a,b):..... return 


def myfunction(vorodi1,vorodi2):
    answer=vorodi1+vorodi2
    #print
    
    return answer




def jam(a,b):
    c=a+b
    print(c)
    return c


#input is for educational purposes
#90%


a=input('salam adade avaleto bede:')
b=input('adade dovometo bede:')

jam(float(a),float(b))



jam(20,10)



#--------------------------
#telegram send.message()

#teleghram(@...)
#@....
import telegram
telegram.id='sudshdgasuih'
telegram.password='dhidsahah'
telegram.login()


telegram.send_message('salam code mahsooleto begoo:')

a=telegram.context()

database=[]


if a in database:
    print('4000')
    
else:
    print('mojodi nadaram')







#---------------


a=input('salam code mahsooleto begoo:')


database=[]


if a in database:
    print('4000')
else:
    print('ma nadarim mojood')




#-------------------------------------


def jam(a,b):
    c=a+b
    return c

d=jam(50,100)




#print(c) #NameError: name 'c' is not defined

#a=50
#b=100
#c=a+b
#return c


#tamam e variable hye dakhele yek tabe 

#barbaran

#zarfaro msihkone

#ZARFA HAYE MOVAGHATAN




#tamam evaribales haye dakhele yek tabe -[-.local hastan]
#MOVAGHAT SKAHTE SHODAN
#BIROONESGH RETURN MIRESE TAMAAAM
#DG DASTRESSI NDRI



#global

def jam(a,b):
    global c
    c=a+b
    return c

#global variable


#a , b , c ,... -->tahvil mide
#beshkoen zrafar (rmeove)
#on zarfi k globale ro nmishkone

d=jam(50,100)


print(c)








#----------------

def jam(a,b):
    c=a+b
    return c



jam(10) #TypeError: jam() missing 1 required positional argument: 'b'

jam(10,20,30) #TypeError: jam() takes 2 positional arguments but 3 were given



#default

#ghanone newton

#f=m*a

#jesm * a


#mass , acc ---> BOX --> force



def newton_second(mass,acc):
    
    '''
    this funciton is for calculation of the force
    based on second law of newton
    
    parameters:
        mass : float
        acc : acceleration float
        
    return (output):
        force --> float 
        force= mass* acceleration
        
    '''
    
    force=mass*acc
    
    return force




zarf=newton_second(5,20)

#fght jerme

newton_second(5)
#pish farz






#mass granehs 9.8 --.a

#mass * 9.8


def gravity(mass):
    
    force=mass*9.8
    
    return force


gravity(5)

gravity(5,10)

#TypeError: gravity() takes 1 positional argument but 2 were given



def general(mass,acc=9.8):
    
    force=mass*acc
    return force


general(5,20)


general(5)


#(vordoi1,borodi2)  tabe at hatman bayad dotaro begire
#(vorodi1,vorodi=default1) tbe at fght bayad yek vorodi bgire 


#default ro hatman akhar bzarr




def general(mass,acc):
    
    force=mass*acc
    return force




general(10,20)

general(mass=10,acc=20)




#-----

def jam(a,b):
    
    c=a+b
    return c


jam(10,20)

jam(a=10,b=20)




def jam(a,b,/):
    
    c=a+b
    return c



jam(10,20)

jam(a=10,b=20) #TypeError: jam() got some positional-only arguments passed as keyword arguments: 'a, b'


#/ --> ghabliaa fght bayad khaliii bzarishon



def jam(*,a,b):
    c=a+b
    return c


jam(10,20) #TypeError: jam() takes 0 positional arguments but 2 were given

jam(a=10,b=20)
 




#combined


def jam(a,b,/,*,c,d):
    
    answer=a+b+c+d
    
    return answer



jam(10,20,c=30,d=40)


#-----------------------------------------------------



#----task--------

#getting_information()
#confirmation()
#print_factor()


import telegram
telegram.id='sudshdgasuih'
telegram.password='dhidsahah'
telegram.login()


def greeting():
    username=telegram.username
    timtime.now()
    
    #if time <123 : zohr bekheyr
    #> zohr 
    
    #shab
    
    
    print('salam khosh amadi jhanam? dar khedmatam?')



def ai_support():
    
    answer=telegram.context()
    
    khoroji=ai_response(answer)
    
    telegram.send_message(khoroji)
    
    
    ai_support()
    
    

def ai_response(text):
    
    #-----
    #---
    #----
    #-------
    #----model vasl koni
    #response
    pass
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    



telegram.send_message('salam code mahsooleto begoo:')

a=telegram.context()

database=[]


if a in database:
    print('4000')
    
else:
    print('mojodi nadaram')













