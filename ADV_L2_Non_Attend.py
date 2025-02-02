#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In The Name of GOD


Created on Sun Feb  2 17:36:37 2025

@author: Ali Pilehvar Meibody


ADV_L2_Non_Attend

pishrafte _ jalaseye2 _ gheyre hozori ha


#----REVIEW ON L1------
human (english) ------(programming language) ---> Machine (0,1 binary)


among prog langs --> Python ( reasons.....)

1-Python  ZABAN
2-IDE  MOHITS TELEGRAM ,... SPYDER



#_---python ----> zaban grammar , vocab

1-->python built in functions (print(),input(),open(),len(),type()) __> hame type data 
2-->keywords ( and , or , as , for , if else , while , ....) dastoor 
3---> harchi benevsii__.unreserved -->rangi nemishe---> esme zarf --> variable name (restriction , 2ssd %^*)

Variables --> 
1-Numbers (int(1,2,3,4), float(1.5), complex(1j)) --> ** * / + - % 
2-string ( --> horof , character, jomle, kalame va va va)
3-Boolean (True , False)

#--------
str

"""
#variabel_name= quot

#1--->assign --> megdhar dehi 
name='ali'
#name=ali ---> avriable name = variabel ali

#2 '2'  --. adad + - , string nemitoni + - 

#2--access  esme variable [index] --> index 0 - ..

name[0] # 'a'
name[1] #'l'


name='alipilehvar'

name[2:8] #[start:end+1:step]   ,default :step ro nanevisi :1
#'ipileh'
name[2:8:2]

#access?? --> bekhater einke kari darim bahash


#change???

name[3]='d'

#TypeError: 'str' object does not support item assignment

#str -->>> bema ejaze nemidan ke megdhar dehi koni item haro


'''
shabahat -- > joftehson tab ehastan

tabe--> ()  print()  input()  if 


farghe 1
puython built in --> barayer hamas print(4) print('salam')
tabe haye --> str function -_> fgth baraye str ha hastan --> adad , ...


farghe2 --> tarigehye sestefade print upper

a='ali'

print(a)

#str function bayad dot bezani
#upper(a) --> xxxx

a.upper()

sevomin nokte---> khoroji mdiahad , emal nemikone
pas ma yek zarf niaz darim

'''

a='ali pilehvar'
a.upper() #'ALI PILEHVAR'
print(a) #ali pilehvar


a2=a.upper()

print(a) #ali pilehvar
print(a2) #ALI PILEHVAR


#azinja be bad man khoroji mziaram ama yadet bashe
#done done bayuad biay zakhriahs koni

a2.lower() #'ali pilehvar'


a.capitalize()
#'Ali pilehvar'

a.title()
#'Ali Pilehvar'

a.replace('l','s')
#asi pisehvar'






c='ali/pilehvar/meibody'
d=' ali pilehvar'




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


'''
CLASSIFICATION DASTE BANDI


str functions --> .()
1--> emal nemikonan , khoroji midan ********

kole in tabe ha 3 no khoroji daran

1--> converter --> hamono taghire jzoi roosh mide

upper()   ali --> ALI
lower()  ALI -->ali
title()
replcae(old,new)
split()
strip()




2-->counter -->  behet adad pas mide ---> 
.find(char)
.count(char)


3--> behet True False --> Checker
is --> aya in hast aya in nis
isupper()
isdigit()
islower()

startwith('b46')
endwith('mo')





'''

name='ali pilehvar'

#a --> find

name.find('a') #0 --> tabeye find b avalin harfi k donbaleshi brese tamam return

name.count('a')  #2


name.isupper() # False

#is upper?? True , False


a=' ali'
 
a[0] #' '

print(len(a)) #4 
#space / a / l / i

#-->tabe e hast k mitone space e chapo ba rasto hazf kone
a=' ali'

b=a.strip() #'ali'

print(b) #'ali'

print(len(b)) #3


a=' ali pilehvar meibody '

a.strip() #'ali pilehvar meibody'

a.rstrip() #' ali pilehvar meibody'
a.lstrip() #'ali pilehvar meibody '

#hjarja space did hazf kone?
a.replace(' ','') #'alipilehvarmeibody'


#a.split()
#--> y chartacteri y chizi midi migi behesh residi ghablio bendaz to ye list

#alisdadsad.dsadsas.dsadas

#split('.')


#alisdadsad
#dsadsas
#dsadas


#in the name of god, i am ali pilehvar , and today

#split(',')

#in the name of god
# i am ali pilehvar 
# and today

#listy pass mide



a='in the name of god, i am ali pm and today'

b=a.split(',')

print(b)
#['in the name of god', ' i am ali pm and today']


#noket nahaee inaro mitoni to ham too ham ham estefade koni

a=' ali pilhvar meibody'

b=a.strip().lower().title().split(' ')

print(b)
#['Ali', 'Pilhvar', 'Meibody']



#=================================
#int
#str ha ro yad grfitm


#int , str baham negah daram yeja chetor???


#iterable --_> iteration 

#elements --> iterable --> List, Tuple, set , dictionary

'''
Iterable
1--> asssignment (meghdar dehi ) element miriszi toosh
2--> access ( chijori b oon element dastressi pedya koni)
3--> change (add, change , remove)
4--> iterable functions



4--> list ,....




* LIST --> ordered, changable , allow duplicated 
*TUPLE--> ordered, unchangable, allow duplciated
*Set --> unordered , unchangable , no duplicated
#Dictionary --> hamoon liste --> bejay eindex , keys





'''


#---------LIST------
#ordereed , changable , allow duplicated

#1--assignment

a=[10,20,30,40,50,60]


a=list(10,20,30,40,50) #errorrrrr

a=list([10,20,30,40,50])

a=['ali',40,True]


#2--> access 

#name='ali'
#name[0]

#name = ['a','l','i']
#name[0]
a=[10,20,30,40,50,60]

a[2] #Out[43]: 30


#3---> change ???
a[2]=10000

print(a)
#[10, 20, 10000, 40, 50, 60]

#str --> nemishe assignment element
#list -_> ejaze mdie--> changable


#------------
#list functions ---> () , fgth bartayelist , .()



a=[10,20,30,40,50,60]

#insert --> add

#add konam 1000

a.insert(1,1000)

#khoroji nadad


#********** str --> in emal mishe , khoroji nmidee

print(a) #[10, 1000, 20, 30, 40, 50, 60]


#--------
#bekham b tahesh ezafer konm?

print(len(a)) #7
#0 -----> 6


a=[10,20,30,40,50,60]
# 0   1   2   3  4  5

a.insert(5,1000)

print(a) #[10, 20, 30, 40, 50, 1000, 60]



a=[10,20,30,40,50,60]
a.insert(6,1000)
print(a) #[10, 20, 30, 40, 50, 60, 1000]

#len --> bad begam kodom idnex ,.....


#---> insert -> vared kon
#add ezafe kond

#append --> ezafe kon b tahesh 
a=[10,20,30,40,50,60]
a.append(10000)

print(a)
#[10, 20, 30, 40, 50, 60, 10000]



#remove --> begi kodomo mikhay remoev koni
#ya behesh index bedi

a=['ali','vahid','hamid','reza']

a.remove('ali')

print(a) #['vahid', 'hamid', 'reza']

a=['ali','vahid','hamid','reza']

a.pop(0)


a=[10,20,30]

b=[40,50]


a.append(b)

print(a)

#[10, 20, 30, [40, 50]]
#kole liusto append karde

a=[10,20,30]

b=[40,50]

a.extend(b)
print(a)

#[10, 20, 30, 40, 50]


'''
list function --> fght vase liustan .()
** emal mishan khoroji nemidan 


.insert(idnex, value)

.append(value) --> value ro ezafe mikone be tahe
.extend(iterable)

.remove() remove element by value
.pop()    remove element by index

.clear() --> remove all element []

del a ---> koel variable hazf mikone


'''

a=[10,20,30,40,20]

a.count(20) # 2  khoroji daran adad mdian emal

a.clear()
#motefgavete
#ba del

del a #--> dleet a ro 
#print(a)
#NameError: name 'a' is not defined

a=[10,20,30,40,20]

a.clear() #khdoe zarfo ba jash dleet nmikone
#Miad toosho khali mikone

print(a) #[]


a=[40,50,10,2]

a.sort()

print(a)
#[2, 10, 40, 50]



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

#===================================
#tuple

#--ordered , unchangable , allow dup-lciated
#hamon liste ha vali change nemitone bokone

#a=[]


a=(10,20,30,40)
a=(40)
print(type(a)) #<class 'int'>


#na man manzoram yek tuple hast ab yek ozv
a=(40,)





a=('ali','hamid','vahid1')


a[2] # 30

a[2]=100

#TypeError: 'tuple' object does not support item assignment


#str --> ejaze change nemide , tuple --> jeaze change nmide
#list --> ejaze dad 

#trick -->

b=list(a)

b.append(1000)

a=tuple(b)

print(a)

#-----------------------
#functiosn haye khdoesho

#tuiple functions

#---> done doen ro tahlil --> b inkar mifhmi va mivini
#-----set




#set --> ordered nist , chnasagbel nist , duplicated ghabol nemikone

#list []
#tuple ()  (,)
#set {}

a={10,20,30}

a={'ali',True,40}

#ordered nis --> yani index nadare
#dasteressi dari?

a[0]
#TypeError: 'set' object is not subscriptable

for i in a:
    print(i)


#taghir ham nmitoni bdi
#->lkisty -->



#--->mohem tarin khasiatesh bnzrm
#-->zmaani k shoma nmitoni duplciated dahste bashi


a={'ali','ali',30,40}

print(a)
#{40, 'ali', 30}



#---> kh jaha to dari ba lits kar mikoni
#koli append , extend , remove , pop +32182347
#-329 --> tahehs nabayd tekrari bashe toosh
#for 

#list --> set --> list


count_list=[]


for i in range(0,10):
    a=i+100
    b=i+200
    
    if a*b==2000:
        
        count_list.append(i+100)
        
    else:
        count_list.append(i+101)
        
        
print(count_list)



        
'''
[101, 102, 103, 104, 105, 106, 107, 108,
 109, 110, 101, 102, 103, 104, 105, 106, 
 107, 108, 109, 110]

'''

print(len(count_list)) #20

myset=set(count_list) #list --> set

print(len(myset)) #10

#10 tash ?? --> tekrari bode

my_final_list=list(myset)
    
print(my_final_list)    
    
    
my_final_list.reverse()

print(my_final_list)    
#[110, 109, 108, 107, 106, 105, 104, 103, 102, 101]



#-----------------
#dictionary
#---> esmesh maloem yeseri chiza hast yersi

#a--List --> ordered, changable , allow duplicated
#b tuple --> list without change
#c--> list --> un list --> unordered, unchanagable , not duplciate


a=[100,200,300,400]

b=(100,200,300,400)

c={100,200,300,400}

#dictionary hamiin liste amaaaa
#bejaye index --> mokhafaf mziari


a=['ali',30,10000]
'''
index     value
0           ali
1          30
2         10000

'''
a[0] # 'ali'
a[1] # 30
a[2] #10000



b={'name':'ali' , 'age':30 , 'balance':1000}

'''
index     value
name          ali
age         30
balance         10000

'''
b['name'] #'ali'
b['age']#30


b['age'] = 40

#-----
'''
str , tuple , set --> element unchangable a[30] -- 


list, dict --> a[30] =   a['name']=


'''


b['year']=1990



#dict functions

b.items()
'''
dict_items([('name', 'ali'), ('age', 40), ('balance', 1000), ('year', 1990)])

'''

b.keys()

# dict_keys(['name', 'age', 'balance', 'year'])

b.values()
#dict_values(['ali', 40, 1000, 1990])



#----------------------------------------
p_code='l100'
name='zara'
price=1000



text="""
----PLUTUS PRODUCT MANAGEMENT------

Product code :  p_code
product name: name
price : price


------
Plutus Co.2025

"""



print(text,name)

#print('salam','khobi')






jomle='salam man ali hastam va man 30 salame'

print(jomle)


a=30

jomle='salam man ali hastam va man a salame'

print(jomle)

#salam man ali hastam va man a salame

#string --> ejaaze mdie beyen hroof va moteghayert

#string --> f string

a=50

jomle=f'salam man ali hastam va man {a} salame'

print(jomle)

#salam man ali hastam va man 30 salame

#lope kalam --> f string --> man yek adad ya value  megdhar az biroon mikham




#=============inja=====
p_code='l100'
name='zara'
price=1000



text=f"""
----PLUTUS PRODUCT MANAGEMENT------

Product code :  {p_code}
product name: {name}
price : {price}


------
Plutus Co.2025

"""

print(text)


'''

----PLUTUS PRODUCT MANAGEMENT------

Product code :  l100
product name: zara
price : 1000


------
Plutus Co.2025

'''

#---->mesale dige---> mahboob va maroof va por karborde

#man mikham 

#man site amazonam 
#codam --> jolom yek foroshandast

#man begam agha shoamre codeto bede
#oon bede
#bad begam esmesho bego
#esmehso bege
#bad begam gheymato bego
#gheymato bege


#bad hamchin chizi nehson bdm
'''
salam in moshakhasate mahsole shoamst
code:
    name:
        price:
            
aya taeed mikonid??
'''


#----in mesasl hamon meal ghableiu amaa
p_code=input('code mahsoole shoma chist?:')
name=input('name mahsoole shoam chist?:')
price=input('gheymate mroede nazaretoon chist?:')


text=f"""
----PLUTUS PRODUCT MANAGEMENT------
product information:
    
    
    
    
Product code :  {p_code}
product name: {name}
price : {price}


------
do you confirm ?

"""

print(text)



#*****---> input harchi jolosh bzni ro str mikone


a=input('priuce chande?')
print(type(a)) #<class 'str'>


a=int(input('priuce chande?'))
print(type(a))
#<class 'int'>
a/4

#** inut hamishe str pas mide



#--------------------
#-->hadadf ine product ro hamaro
#yejoor bede taraf
#hamaro posjhte ham bde


allproductinfo=input('lotfan code, name price ro bede')


print(allproductinfo)
#l100 zara tshirt 4000



allproductinfo=input('lotfan code, name ,price ro b formati k gofte shode benevis ( vba vrigool):')

print(allproductinfo)
#'k100,zara tshirt , 4000'

#str fucton-->split
#split(')


product_list=allproductinfo.split(',')

print(product_list)
#['k100', 'zara tshirt ', ' 4000']

product_list[0] #'k100'
product_list[1]
#-----------------------------------------

#===9843qrehasksudh087rydqpnebyrdi7w9teyredhenni
#i7eruyaes97eryncap8oudfuy0a880numo8sugso8gufmw


allproductinfo=input('lotfan code, name ,price ro b formati k gofte shode benevis ( vba vrigool):')

product_list=allproductinfo.split(',')


product_code=product_list[0]

product_name=product_list[1]

product_price=product_list[2]


text=f'''
----PLUTUS PRODUCT MANAGEMENT------
product information:
  
Product code :   {product_code}
product name: {product_name}
price : {product_price}


------
'''

print(text)


#==========================================


product_list=input('lotfan code, name ,price ro b formati k gofte shode benevis ( vba vrigool):').split(',')
text=f'''
----PLUTUS PRODUCT MANAGEMENT------
product information:
  
Product code :   {product_list[0]}
product name: {product_list[1]}
price : {product_list[2]}


------
'''
print(text)


'''
#----------------------------------------
task1----
biad done done az foroshande code , name , price
hamaro berize too ye list
badesh namayesh bede


task2------

biad done done az foroshande code , name , price --> 3 variable
dictionary konatesh
badesh namayesh bede


task 3-----
code , name , price ---> gheymato 30% kam kone bad namayehs bede

task 4 (optional):
    
4 bar in process ro anjam bde 
kolesho berize too yekdictionary












'''






















