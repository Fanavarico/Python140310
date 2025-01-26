#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In The Name of GOD
Created on Sun Jan 26 17:39:51 2025

@author: Ali Pilehvar Meibody



ADV_L2_Attend




Review on L1----------
human---python----machine(binary0,1)


python -->language grammar and vocabs

reserved words
1---> python built in funciton (print(), input(), len() , type())
2--->keywords --> (if,else,for , while)
3---> unreserved words --> variables (moteghayer,zarf)
zarf baraye chi? --> zakhrie konan
1-numbers (int(0,1,2,3,4,), float(1.451),complex(1j))
** * / + -
a=b a ro bzar b (dastoore)
moghayese --
moghayese-->soal beporsi
==
a==b --> aya a barabnar hast ba b?? -->True False
>
<
>=
<=


2-Boolean (True, False)
3-string( 'a','34','ali','welcome to the new world')



"""

#strings------
#qutation
#ali 'ali'
#name 'name'

a='alipilehvarmeibody'

#python built in function --> 
print(a)
#alipilehvarmeibody

len(a) # 18
b=len(a)
print(len(a))
#nemitoni
v=print(len(a))
print(v) #None

type(a) #str



#-------STRING HA -------
#1---> access peyda konam be element ha 

a='alipilehvarmeibody'


#mikhay bgi masalan mikham b 5omin harfesh brsm

#too tamame python adad az 0 shoro mishe na az 1
#index--->0

#5omi -->< 1 2 3 4 5*

#indexe 0 index1 indexe 2 indexe 3 indexe(4)


#indexe 4 ro mikham ( 5omin kalamro)

#mige az kodom zarf? esmesho --> a
#mige berakte bzar adade indxo tosh bzar

#aqccess

a[4] #'i'

#a l i p i l e h v a r

#0 1 2 3 4 5 6 7 8 9 10

a[0] #'a'


#chnata access --> az indexe 3 ta indexe 6

#start, end ---> end -1

#in python in any ranges ,start is included , but end is excluded

#az 3 ta 10

a[3:10] #kheyr
#'pilehva'

#age to az 43 ta 10 mikhay

a[3:11] #--> az 3 ta 10
#'pilehvar'


#bahse rnage az start - endc default = 1

#******
#(start,end,step) --> start to end-1 step step

a[3:11:1]
# 'pilehvar'
#ch bnvisi ch naneviusi mojhem nis

a[3:11:2]
#'plha'


#----baraye asoonie kar 

a[0:11]
#'alipilehvar'

a[:11] #age adad nazari mifhme k manzoret az 0 hast
#'alipilehvar'


a[5:18]
#'lehvarmeibody'

a[5:] #mifahme manzoret ta akahre

#------------------

a[5:18:0]
#ValueError: slice step cannot be zero


#---------------
#2--> access mikonim k chi she?
#man yad grfrtm b y string avred sham 
#access konam k chi???

a='alipilehvarmeibody'
a[4]='p'
#TypeError: 'str' object does not support item assignment
a[5]='L'
#TypeError: 'str' object does not support item assignment

#man ag bkham yeseri kara rooye str am konam chika rkonm?

#python--> esmehso gozashte [str functions]

#kalameye a o mikhay avazesh kjoni --> bzoorg kjoni
#function-->box behem bnedew behet pas midma


#bzoorg kardan --> upper

#str function 
#python built in funciton

#**1---> python built in funciton ha baaraye hamand mesle print(4) print('salam')
#**2---> tarigehye emaleshoon


#kolan tabe ha tooye python esmo minevisi () too paranetz mitooni oon value ro bdi

print('salam')

len(a)


#upper -->

#upper(a) #NameError: name 'upper' is not defined

#tabe ha baraye hame nistah hamegani nsitan
#tarigheye emalehson ham dfargh mikone

#Mige bejaye inke to parantez bzari , aval oono bnvis
#roosh dot bezan

a.upper()
#rooye zarfe 1 --> tabeye upper ro ejra kon

#'ALIPILEHVARMEIBODY'


#lower

b='ALI'

b.lower()
#'ali'


#---> nokteye badi -->
#str function , list function , set funciton ,...

#python built in function --> khdoesho minevisio parantez
#str va list funciton --> dot bezanio

#str vs  list function

#str function --> khoroji midan --> ono zakhrie mikoni , hich taghiri roye asli nemidan
#list funciton ha--> taghir midan va khoroji nmidn


a='ali pilehvar'

a.upper()
# 'ALI PILEHVAR'


print(a)
#ali pilehvar



#pas str fucntion ha aslio taghir nmidn
#balke khoroji midan


a='ali pilehvar'

#aval --> access

a[4]
a[4].upper()
# 'P'


b=a.upper()

print(a) #ali pilehvar
print(b) #ALI PILEHVAR


'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Converts the elements of an iterable into a string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning

'''



a='ali pilehvar'
a.upper()
a.lower()
a.capitalize()
a.title()
a.replace('p','P')
# 'ali Pilehvar'

a.replace('a','s')
#'sli pilehvsr'


#'Ali pilehvar'

a='in the name of god'

a.title()
# 'In The Name Of God'


#man mikham i haro behsmoram

a.count('i')
# 2


count=0
for i in range(0,len(a)):
    if a[i]=='i':
        count=count+1
print(count)
#2

a='alipilehvar'
a.find('p')
#3

a.find('i')
#2
#ta peyda mikone behet pas mdie , edame to ignore mikone



#--------
'''

str functions

1-->convert  bozorg mikone(upper) kkochik mikone(lower) avale harf(capitalize) , title mikone
2--> mige adad pas mdie , chanta a daram , agah a kojass v, count , find
3--> check mikone--> true false mide --> kheyli moheman


'''

#islower -->

a='ali'
a.islower() #True

a='Ali'
a.islower() # False


#================================
#-----variables------
#Numbers (int, float, complex) computational operators (** * = + ) , comparison operators (== > <)
#boolean
#str (access (index[]),str functions (1-convert ,2-number 3-tru false))

#20 ta adad
#5 ta esm

#-----> iterable ha --->
#list, tuple , set , dictionary

#---> 4 ta yekar mikonan --> tedade ziadi variable too deleshon mriizi


#list --> ordered , changable , allow duplicated
#tuple--> ordered , unchangable , allow duplicated
#set --> unordered, unchangable , no duplicated
#dict --> order-->index nadare ,  dictionary

#hadafe har 4 --> chanta varibales dakhelesho bashe
#1----> assign (chijori tarifeshon konim)
#2--> access (dastressi)
#3-->chijori taghir
#4-->tabe haye dkaheli daran?



#-----list-------
a=[10,20,30,40,50,60]

a=['ali','reza','vahid','hamid']

a=[10,'ali',True,1j]

a=[[10,20,30],[40,50,60],['ali','hamid','vahid']]


#daghighan mese str mimone
a='ali'

a[2]
#'i'


a=['a','l','i']
a[2]
#'i'


a=[10,20,30,40,50,60]
a[4] #50

a[2:6]
# [30, 40, 50, 60]
#[start:end(exlude):step]

#----> access krdm k chi???
#50 ro bokonam 100
a[4]=100

print(a)
#[10, 20, 30, 40, 100, 60]


a='alipilehvar'
a[4]='b'
#TypeError: 'str' object does not support item assignment


#list support item assignment --> for changing the item
#first access then change !



a=[10,20,30,40,50,60,70,80]

#ezafe konam behesh

a.insert(3,1000)

print(a)
#[10, 20, 30, 1000, 40, 50, 60, 70, 80]
#emal krd tooye khode a

'''
flashback

a='salam'
a.upper() #zkahrie mikrdi yeja 

print(a)
#salam

str function emal nemikone khroji mide

list function emal mikone khoroji nemide

'''

#REPLACE
#INSERT--> gharar mide , jaygozin nemikone

a=[10,20,30,40,50,60,70]

len(a) #7

#0 - 6 
#7
a.insert(7,10000)

print(a)

#naram ebgardma tahesh chi
#qagha b tahesh ezafe kon

#kalameye englisi -->tahesh ezafe kon-->
#append

a=[10,20,30,40,50,60,70]

a.append(2000)

print(a)
#[10, 20, 30, 40, 50, 60, 70, 2000]


a=['ali','hamid','vahid']
#remove
#chio mikhay remove
#ye adad daram yue value 

a.remove('ali')

print(a)
#['hamid', 'vahid']

a=['ali','hamid','vahid']

a.pop(0)
#'ali'


#-------
#.append() #value
#.insert( , ) #index , value
#.remove() #value
#.pop() #index

'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

'''

a=[10,20,2,3]
a.sort()

print(a)
#[2, 3, 10, 20]
a.reverse()

print(a)
#[20, 10, 3, 2]


a=[10,20,30,40,50,60,70]

b=a

print(a)
#[10, 20, 30, 40, 50, 60, 70]
print(b)
#[10, 20, 30, 40, 50, 60, 70]


a.append(1000)

print(a)
#[10, 20, 30, 40, 50, 60, 70, 1000]


print(b)
#[10, 20, 30, 40, 50, 60, 70, 1000]


#a=b 
#ta taheshh bahatam......


#har taghiri roo a beshe roo b ham anjam mishe



#mikhjay fght fght 

a=[10,20,30]
b=a.copy()


a.append(1000)

print(a)
#[10, 20, 30, 1000]

print(b)
#[10, 20, 30]

#yani barabar gharar ndadi , copy grfti
#pas ta tahesh ykbare copy grfti
#dg har taghiri roye a bdi rooye b emalk nmishe


#========================
#tuple

#list----->
a=[10,20,30]

b=(10,20,30)

b[1] # 20

b[0:2]
#(10, 20)

#functions


b[0]=1000

#TypeError: 'tuple' object does not support item assignment

#str nemizahst
#tuple nmizare


#list mizare

#kalak bezan

c=list(b)

print(c)
#[10, 20, 30]

c[0]=1000

print(c)
#[1000, 20, 30]

b=tuple(c)

print(b)
#(1000, 20, 30)


#tuple-->list taghri dadam --> tuple



a=[100]
a=(100,) #ino yek tuple ba yek ozv
a=(100)#-->ino adad dar nazar migire

#-----------------------------------------
#set --> unordere --> No duplicated 

a={10,20,30}
#index nadareee
a[0]

a={10,20,20}

print(a)
#{10, 20}

a=[10,20,20,20,20,20]
print(a)
#[10, 20, 20, 20, 20, 20]


#-------dictionary


b=[30,'ali','tesla']

#indexe 0 30 mizre
#value badsi troo indexe badi

#jaye index behesh  esme tarafe , sene tarafe
#bejaye index
#dictionarey

a={'age' : 30, 'name' : 'ali' ,'car' : 'tesla'  }


a.items()

#dict_items([('age', 30), ('name', 'ali'), ('car', 'tesla')])

a.keys()
#indexaro mide
#dict_keys(['age', 'name', 'car'])

a.values()
#dict_values([30, 'ali', 'tesla'])


b[1]
# 'ali'


a['name']
#'ali'


a['name'] = 'vahid'


'''
list , dictionary support item assignment ( a[2] = )

str nemizare
tuple nemizare (changable)
set --> order , index ndre

'''

a['year']=1990

#==========================
'''
list functions
append()
insert()
copy()
remove()
pop()
clear()


#------set funcrtion
$------tuple funciton
#-----dictionary function


'''
#=========================

'''
Product management
website , narm afzar aspplciation


BANK Management

...

'''

product_code='l100'
product_name='nvidia'
product_price=20000

text=f"""
plutus product management-------

product code : 
product name :
Total price :

    
do you confirm that?

"""


print(text)


'''

plutus product management-------

product code : 
product name :
Total price :


do you confirm that?
'''


sentence='salam be banke a khosh omadid'

print(sentence)
#salam be banke a khosh omadid


a='PLUTUS'

sentence='salam be banke a khosh omadid'

print(sentence)


a='PLUTUS'

sentence=f'salam be banke {a} khosh omadid'

print(sentence)
#salam be banke PLUTUS khosh omadi

#------------------


product_code='l100'
product_name='nvidia'
product_price=1000

text=f"""
plutus product management-------

product code : {product_code}
product name : {product_name}
Total price : {product_price}

    
do you confirm that?

"""


print(text)

'''

plutus product management-------

product code : l100
product name : nvidia
Total price : 20000


do you confirm that?
'''
#--------------

product_code=input('lotfan code mahsoole khod ra vared konid:')
product_name=input('lotfan name mahsoole khod ra vared konid:')
product_price=input('lotfan gheymate mahsole khod ra vared konid:')

text=f"""
plutus product management-------

product code : {product_code}
product name : {product_name}
Total price : {product_price}

    
do you confirm that?

"""


print(text)

'''
lotfan code mahsoole khod ra vared konid:l200
lotfan name mahsoole khod ra vared konid:nvidia
lotfan gheymate mahsole khod ra vared konid:2000

plutus product management-------

product code : l200
product name : nvidia
Total price : 2000


do you confirm that?

'''

#-------
a=input('lotfan code mahsoole khod ra vared konid:')
b=input('lotfan name mahsoole khod ra vared konid:')
c=input('lotfan gheymate mahsole khod ra vared konid:')

product={'product_code':a , 'product_name':b , 'product_price':c}

print(type(product))
#<class 'dict'>

print(len(product))
#3

print(product.keys())
#dict_keys(['product_code', 'product_name', 'product_price'])

print(product.values())
#dict_values(['l100', 'nvidia', '2000'])





#------------------
a=input('lotfan code mahsoole khod ra vared konid:')
b=input('lotfan name mahsoole khod ra vared konid:')
c=input('lotfan gheymate mahsole khod ra vared konid:')

product={'product_code':a , 'product_name':b , 'product_price':c}

product.keys()
#dict_keys(['product_code', 'product_name', 'product_price'])

product['product_code']
# 'l100'



text=f'''


plutus product management-------

product code : {product['product_code']}
product name : 
Total price : 


do you confirm that?


'''
print(text)




#-------------------------------

a=input('lotfan code mahsoole khod ra vared konid:')
b=input('lotfan name mahsoole khod ra vared konid:')
c=input('lotfan gheymate mahsole khod ra vared konid:')

product={'product_code':a , 'product_name':b , 'product_price':c}



text=f'''


plutus product management-------

product code : {product['product_code']}
product name : {product['product_name']}
Total price : {product['product_price']}
do you confirm that?


'''
print(text)




#---------------------template-------------------
a=input('lotfan code mahsoole khod ra vared konid:')
b=input('lotfan name mahsoole khod ra vared konid:')
c=input('lotfan gheymate mahsole khod ra vared konid:')

product=[a,b,c]

#['l100', 'nvbidia', '10000']


text=f'''


plutus product management-------

product code : {product[0]}
product name : {product[1]}
Total price : {product[2]}
do you confirm that?


'''
print(text)



'''
TASK 0:
az taraf code, name , gheymat bgire
gheymaro 30 darsadesho kam kone 
bad behesh namayesh bede hamaro
    
    
    

TASK1 --->
az admin code , name , gheymat 
berizatesh tooye yek tuple
bad name  ro taghir bede b (harchi delet khast)
bad be soorate bala namayesh bede




Task2 -->
5 bar in karo kone
az admin code , name , gheymat bnegire
kolesho berize tooye yek dictionary

badesh k 5 bar gereft
va oon dictionarey haro berize too yek list


list enahaee man 5 ta dictionary tooshe





Task 3 (optional , advanced):
    
bia paeen



'''
#=========================
products={'p code':[] ,'p name':[] , 'p price':[ ]}

a='l100'
b='nvidia'
c=1000


#products['p code'] = a
#l,isyte khalio avaz krdm ba ye adad
products['p code'].append(a)

products['p code'].append('z200')



products={'p code':[] ,'p name':[] , 'p price':[ ]}
# 5 bar mahsool bgiram 
for i in range(0,5):
    a=input('lotfan code bede:')
    b=input('lotfan name bde:')
    c=input('lotfan gheymat bede :')
    
    products['p code'].append(a)
    products['p name'].append(b)
    products['p price'].append(c)

'''

kode balaro ejra kon
to yek products yek dictionary darish

yek algorithm benevis k az taraf  code mahsool begire
bad behesh gheymat ro namayesh bede



'''
    
    

    







