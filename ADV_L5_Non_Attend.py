
"""
In The Name of GOD

Created on Mon Mar 10 20:02:39 2025

@author: apm


ADV_L5_Non_Attend


"""

#-----REVIEW-------

'''

human ------------- Python ------- Machine


-----RESERVED WORDS------------------------------- RANGI
Python built in functions --> narenji () , hame hastan amalkard
print() , input() , len() , type() , ....
https://docs.python.org/3/library/functions.html



Keywords-->manteghi daran codo taghir mdian az halate mamol -->banafsh msihan
if , if else , if elif else , halgeh ha (for , while) , def , and or in not is 
https://www.w3schools.com/python/python_ref_keywords.asp



----UNRESERVED WORDS-------------------------------SEFIDS
zarf --> moteghayere--> variable --> save koni

variable type -->
numbers (int,float, complex) , + - * ** / % ,
Bool ( True , False) --> == =! > >= < <=
str (string ) qooutation --> [index] , [start:end+1:step ], str functions upper
a=ali ---> a.upper() , lower(), replace() , count(a),find(a) ,isdigit() islower()

Iterables ( chnat element) -> list, set, tuple dictionary
[index],....
3 ta nokte deghta ---> (orderin [index] , changable , allow duplicated)




'''

print()
input()
len()
type()

abs(-4)

max(4,6)

min(4,6)

sum([10,20,30])


pow(2,3) #2**3

int(4.6) #4
float(4) #4.0
str()
complex()
bool()
list()
tuple()
set()
dict()


mylist=[True,True,True,True,False]

#all() any()

#jofteshon true false
#vorodi -_>koli shart kmigire

#all-->ag hame treu bashe true pas mdie 

#any -_> age fght yedone true bashe true pas mide


all(mylist)  #False
any(mylist) #True

open()
range()
round(4.3)
sorted([10,100,20,3]) #[3, 10, 20, 100]
reversed()

sorted(['zahan','ali']) # ['ali', 'zahan']

#sorted(['zahan','ali','ZHn','Ali',100,4,39])


sorted(['zahan','ali','ZHn','Ali'])

#['Ali', 'ZHn', 'ali', 'zahan']


#-----------------------------------------------------
#psudo code --> shebhe code -->

#man gom mikonam

'''

psudo code

#1--->varede website beshe


url --> (lancxhand.ir)

request .get(url)



#2-->html ro begiram

text --> 14000 kalame tooshe


#3-->text center


#4--> oon cjomle ro bekesham biroon


#5-->texte -->adado bekeshi biuroon


#6---> database zakhire konam 


#7-->vasl sham b teelgram b yekj bot a zbot be id khdoam messag ebedame

#8---in karo har 12 saat anjam bedam




#---------------(1)----------------------
microsystem 
microservice
capsool haee ---> function --> 1ish 

codet khana tar mishe
ghabele fahm tar mishe
organziation , chidemane awli ee dare
yeja bugg dasht mifhmi 

-->ke --> shma be soorate tabe benevbisi k hamroghe doos dasti azash estefade koni
codeto kootah mikone
efficient (be sarfe )



#-------(2)---------------
mikhjaym az baghie estefade konim


'''


a='ali pilehvar'

a.count('a')



def my_count(name,character):
    count=0
    for i in range(0,len(name)):
        if name[i]==character:
            count=count+1
    
    return count

my_count('ali pilehvar','a') # 2


#-------------
#answe

answer=input('aya etelaat ro taeed mikonid? )(yes , no)?')

#if answer=='yes':
    #print('agha ateed shod')
    
    
#answer= yes
#Yes
#YES

#answer.strip().lower()


#.lower()


#----------
upper_case=['A','B','C','D','E']#.......

upper_to_lower_dict={'A':'a','B':'b','C':'c'}#....


new_list=[]

for i in range(0,len(answer)):
    if answer[i] in upper_case:
        new_list.append(upper_to_lower_dict[answer[i]])


new_answr=''.join(new_list)


#---------------------
answer.lower()



#-------
#from sklearn.neural_network import MLPClassifier
#model=MLPClassifier()
#model.fit(data)


'''

Tbabe 

psudo code (shebhe code) --.capsoole , BOX




voroodi --> BOX ---->khorojii


def name(vooroodi):
    
    badane (psudocode)
    
    khoroji
    
    
    
    


**name -->ghavanin dare


a=20
name=ali

avalesh
character _ 
newton_law 

khaana --> tabe at chiue chikaras?

vorodi ----> BOX ---> Khorji 




def name(vooroodi):
    badaner
    khorji
    
    
def name(vooroodi1,vorodi2,vorodi3):
    badaner
    khorji
    


#khoroji , print chie 




TABE FUNCTION
1-voorodi
2-badane
3--khoroji



badane niaze
vorodi , khoroji optioanl



real world -->vorodi, khoorji


'''

#---------
#---> vorodi dare amma khoroji nadare 1

def jam(a,b):
    c=a+b
    print(c)
    
    
    #return
    #return None

    
    
#sedash konm 
jam(10,20)

jam(10)
#TypeError: jam() missing 1 required positional argument: 'b'
  
jam(10,20,30)
#TypeError: jam() takes 2 positional arguments but 3 were given


#tafrigh(10,20) #NameError: name 'tafrigh' is not defined


jam(10,20)

#vorodi 
#khoroji ndre

#***print---> dastoooore khoroji nist


d=jam(10,20)


#vorodi dare ham khorji

def jam(a,b):
    c=a+b
    
    #print
    return c




d=jam(10,20)


def jam(a,b):
    c=a+b
    print(c)
    
    #print
    return c


d=jam(10,20)

#---vorodi ndshte bashe khorji ashte abshe? (3)


def pi():
    return 3.14


d=pi()

d=3.14



#-------
#na vorodi na khorji

def welcome():
    print('salam khosh amaadid')
    
    
    
welcome()

d=welcome()

#----------

def jam(a,b):
    c=a+b
    print(c)
    #return
    #return None
    
d=jam(50,100)
   

print(d) #None
    
    
def jam(a,b):
    c=a+b
    return c


d=jam(50,100)

print(d)


def jam(a,b):
    c=a+b
    print(c)
    return c

d=jam(50,100)






#persian _ to _english

#d=persian_to_english(4000)


def jam(a,b):
    c=a+b
    return c


#jam()





def jam(number1,number2):
    answer=number1+number2
    return answer


#jam()



def jam(number1,number2):
    '''
    tabeye jam baraye in ast ke 
    do adad be soorate float bedid va in tabe besooraTe
    float in do adad ra jam mikonand va aps midahand
    
    
    '''
    
    answer=number1+number2
    return answer



#-----------------------



def jam(number1,number2):
    '''
    tabeye jam baraye in ast ke 
    do adad be soorate float bedid va in tabe besooraTe
    float in do adad ra jam mikonand va aps midahand
    
    
    '''
    
    answer=number1+number2
    return answer



def jam(a,b):
    c=a+b
    return c



number1=input('adade 1 ro bede')
number2=input('adade 2 ro bede')
d=jam(float(number1),float(number2))



d=jam(10,20)


#------------
#telergam

#moshtariu code 45

#beri begardi 
#ag bodop begi gehymatesho


import telegram 

telegram.bot(id=20234327)
telegram.bot_password('sahjgdksagh')
telegram.run_bot()

telegram.send_message('salam codi k mikhahid ro bedid:')


product_code=telegram.context()

database=[]


if product_code in database:
    
    telegram.send_messsage('gheymate mahsoleton hast 4500')
    
else:
    telegram.send_message('mahsoole shoma dar anbar mojood nnist')
    
    

#bot
#filtershekan
#Internet
#password
#useret hast ,.....
#configure





product_code=input('codeto begooo')

database=[]


if product_code in database:
    
    telegram.send_messsage('gheymate mahsoleton hast 4500')
    
else:
    telegram.send_message('mahsoole shoma dar anbar mojood nnist')
    
    

#------------------



