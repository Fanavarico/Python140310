
"""

In The Name of GOD

@author: Ali Pilehvar Meibody


ADV_L3_NON_ATTEND



python-------> vocabs, grammer

reserved words:
    python built in functions (print(),input(),len(),type())
    keywords if , else, elif , for , while , .....
    
unserved:
    esme zarf->variable -->value miriz dakhele zarf
    variables (value)
    1.numbers (1.1.int, 1.2.float , 1.3.complex)
    2.bool (True,False)
    3.str 
    
    
str---->str functions -->function hae k baraye str


a='alipilehvar'
type(a) -->str

len(a)--->11

#index 0 

a[0] -->a

a[1]-->l

a[2:7]  --> 2 3 4 5 6

a[2:8:2] -> 2 4 6 

a[2]='b' #change nmitoni

koli str function

print()
upper() XXXXXX


name='ali'
dot mizadi
fgth baraye str -->str function

name='ali'

name.upper() -->emal nemikrd
name hamoon ali

khrooji midad--->y zarf mziahsti va zakhire mikrdi


new=name.upper()

name->ali
new-->ALI


3 no
yeseeri convert --> upper() , lower() , title() ,replace('old','new')
adad-->.count('a')  , .find('a')
true false --> islower()  isupper()  isdigit()


#------yek zarf , int, str ,.....
ag chanta chiz bekhay--->iterables ha



----LIST-----
a=[10,20,30,40]
a=['ali',10,20]

a[0] --.10

a[1:3:2]

a[0] = 'vahid'

list function

a.insert(2,'vahid')
a.append('vahid')
a.remove('ali')
a.pop(2)
a.clear()  --? []

khroji nmidad-->mostaghim emal mishod

list--> ordereed, changable , duplicated

--->tuple -->changable nist
a=(10,20)

a=('ali','vahid',30,False)

a=(10,)


a[1]

a[1]=taghir dade nemishod


b=list(a)
b.;insert(......)
c=tuple(b)





---->set
a={1,2,3,4,5}
ordered nabodo--> index to dg nadashti
a[1] -> 1 chie??



-->dictionary
bejaye index to mitoni mokhafaf bezari
a={'year':1399 , 'name':'ali'}

#bejaye index
a['year'] -->1399


a.items() -->

a.keys() -->tamame mokhafaf

a.values() --> magadir

a['new']=new_value




"""

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

#---------------------------------------------

p_list=[]

a=input('code mahsoole shoma chist?:')
p_list.append(a)

b=input('name mahsoole shoam chist?:')
p_list.append(b)

c=input('gheymate mroede nazaretoon chist?:')
p_list.append(c)





text=f"""
----PLUTUS PRODUCT MANAGEMENT------
product information:
    
  
Product code :  {p_list[0]}
product name: {p_list[1]}
price : {p_list[2]}


------
do you confirm ?

"""

print(text)

#---------------------------------------------
p_list=[]

p_list.append(input('code mahsoole shoma chist?:'))
p_list.append(input('name mahsoole shoam chist?:'))
p_list.append(input('gheymate mroede nazaretoon chist?:'))



text=f"""
----PLUTUS PRODUCT MANAGEMENT------
product information:
    
  
Product code :  {p_list[0]}
product name: {p_list[1]}
price : {p_list[2]}


------
do you confirm ?

"""

print(text)

#---------------------------------------------


p_dict={}
p_code=input('code mahsoole shoma chist?:')
p_name=input('name mahsoole shoam chist?:')
p_price=input('gheymate mroede nazaretoon chist?:')

p_dict['product code']=p_code
p_dict['product name']=p_name
p_dict['price']=p_price

#{'product code': 'l100', 
#'product name': 'nvidia', 
#'price': '1000'}


text=f"""
----PLUTUS PRODUCT MANAGEMENT------
product information:
    
  
Product code :  {p_dict['product code']}
product name: {p_dict['product name']}
price : {p_dict['price']}


------
do you confirm ?

"""

print(text)

#---------------------------------------------
code=input('lotfan code mahsol bede:')
name=input('lotfan name mahsol bede:')
#price=int(input('lotfan gheymate mahsool bede'))
price=float(input('lotfan gheymate mahsool bede'))

text=f"""
product information
------plutus management-----
product code :  {code}
product name : {name}
total price : {price*0.7}

do you confirm?
"""

print(text)



#-------------------------
'''
a=1000


b=(a/100) *30

print(b) #300.0


b= a - (a/100)*30

b= a -  30/100 * a
b=a - 0.3*a

b=0.7 * a
'''


'''

a=input('gheymato bede:')

print(a) #1000

print(type(a)) #<class 'str'>

#1000
#'1000'

a=1000

a/5 #200.0


b='1000'
b/5
'''



code=input('lotfan code mahsol bede:')
name=input('lotfan name mahsol bede:')
#price=int(input('lotfan gheymate mahsool bede'))
price=input('lotfan gheymate mahsool bede')



if price.isdigit():
    price=float(price)
    text=f"""
    product information
    ------plutus management-----
    product code :  {code}
    product name : {name}
    total price : {price*0.7}

    do you confirm?
    """

    print(text)

else:
    print('mojadad emtehan konid')


#==============================================
'''
REVIEW 


zarf --> int, str, list, dict
.function -> str.function() list.function()

faghat-->baraye zakhire sazie badan bahash kar koni



---------------
FARSI ----> modire porozhe / sherkati / porozhe
startup -->idea

farsieee --->barname nevis --> PYTHON



zakhire --> variables (zarf) --->yedone int,float / str 
list (taghjir) , database (tuple) , dictionary
set 

bozorg koni,kochik koni , beshmori, fdonbale chizi , taghiri roye str-->str function
taghiri roye list --> list.fucntion()



#-------KALAMATE FARSIO --> PYTHON------------------------
zakhire ---> variables (taghireshn bdi -->function -.str.function(upper,lower),list.function(insert,append))

andazeye chizio bbini --> len()

namayesh bedii ---> print()

begirii ---> input() --> [str]


#-----------shart bezarii------
AGAR ---> AGAR OOMAD --> check koni , agar , ---> [[[if]]]


agar felan bod felan karo kon, ag nabod velesh kon [if khali]
age felan bod felan karo kon, ag nabood yekare dg kon [if else] (dorahi)

age felan shdo felan karo kon

if shart:
    kare1
elif sharte dg:
    kare dg
    


IF --->



agar felan[f1] shod  felan[d1] kon
agar nashod?-->bnaramn mohem nis boro 

if f1:
    d1
    
    
    True---> ejra mikone
    False ejra nemikone
    
    
if shart:
    dstooor

'''

'''
=
+
-
*
**
/

dastoore mohaseb



'''
a=20

c=a+b

'''
==
>
<
=>
<=
!=


dastoor nis--> soale??



'''

a==20 # True

a>10 #True







sen=int(input('salam senet cheghadre?'))


if sen>18:
    print('shoma mojazi')
    

'''


pas if khali-->age felan shod felan kon
ag nshod chi? -->bikhiallll



if shart:
    dastoor1
    dastoor2
    dastoor3
    

'''





a=10

if a>20:
    print('ok')
    print('hi ok')
    
    
    

print('hello')

'''
ok
hello
'''



'''


pas if khali-->age felan shod felan kon
ag nshod chi? -->bikhiallll


dorahi --> age shod inkaro kon (k1)
age nashod onkaro kon (k2)



if else



if shart:
    kare1
    kare2
    kare3
    kare4
else:
    kara
    krara
    kara
    kara



'''


sen=int(input('senet cheghadre'))

if sen>18:
    
    print('shoma mojazi')
    
else:
    print('mojaz nisti')



#=======================================

code=input('lotfan code mahsol bede:')
name=input('lotfan name mahsol bede:')
price=input('lotfan gheymate mahsool bede')

b=price.isdigit()


if b:
    print('ok')



#----------------------------------------


a=input('salam esmeto begoo:')

if a:
    print('salam')


b=None

if b:
    print('salam')
    
#--------------------------------------

'''

if shart:
    dastor1
    dastor2
    dastor3
    .....
    
else:
    dastoore5
    dastoore6
    dastoore7
    .....
    
    
dota halat
ya mikhay ham in hsart va ham oon shart -_> har joftesh bayad true she


and 

if sharte1 and sharte2:
    
    
    
age mikhay begi hadeaghal yekish, yani fght yedonash 

or


if sharte 1 or sharte2:




'''



name='ali'

age=18

#age bishtar az 1 harf bdo esmehs balaye 15 salehs bod bnvsi khosh omdoi

#age --> if 
#if -->

if len(name)>1 and age>15:
    print('salam')

#---------------

#AGAR taraf neevshte hi ya nevesht bye (yekodom hadeghal
#benevis ok


respond=input('beenvis:')

if respond=='hi' or'bye':
    print('ok')


#if respond=='hi' or True:


respond=input('beenvis:')

if respond=='hi' or respond=='bye':
    print('ok')

#-----------------------------------------

code=input('lotfan code mahsol bede:')
name=input('lotfan name mahsol bede:')
price=input('lotfan gheymate mahsool bede')

if price.isdigit():
    price=float(price)
    text=f'''
    
    ----plutus management----
    ///////Information///////
    
    product code: {code}
    product name: {name}
        
        Total price: {price*0.7}
        
    
    '''
    print(text)
    
    
    
    
    
    

else:
    print('adad vared konid, lotfan mojadadan emtehan konid')
    






#-----------------------------------------



code=input('lotfan code mahsol bede:')
name=input('lotfan name mahsol bede:')
price=input('lotfan gheymate mahsool bede')



if not price.isdigit():
    print('mojadad emtehan konid')
else:
    price=float(price)
    text=f'''
    
    ----plutus management----
    ///////Information///////
    
    product code: {code}
    product name: {name}
        
        Total price: {price*0.7}
        
    
    '''
    print(text)
    
    answer=input('do you confirm your product information? (yes or no):')
    
    new_answer=answer.strip()
    
    final_answer=new_answer.lower()
    
    
    if final_answer=='yes':
        print('it is confirmed , thanks')
    else:
        print('ok try again')
    
    
    




answer='yes'
#it is confirmed , thanks

answer=' yes'
#ok try again


answer='Yes'

#'Yes'=='yes' #False




if answer=='yes':
    print('it is confirmed , thanks')
    
else:
    print('ok try again')
    
    

a=' ali'

b='ali '

c=' ali '

a.strip()#'ali'
b.strip()#'ali'
c.strip()#'ali'


#Yes
#YEs
#YES
#YeS
#yes


#--->yes



#answer.lower()
#answer=='yes'


#answer.upper()
#answer=='YES'

#==========================
code=input('lotfan code mahsol bede:')
name=input('lotfan name mahsol bede:')
price=input('lotfan gheymate mahsool bede')

if not price.isdigit():
    print('mojadad emtehan konid')
else:
    price=float(price)
    text=f'''
    ----plutus management----
    ///////Information///////
    
    product code: {code}
    product name: {name}
        
        Total price: {price*0.7}
        
    
    '''
    print(text)
    
    answer=input('do you confirm your product information? (yes or no):')

    if answer.strip().lower()=='yes':
        print('it is confirmed , thanks')
    else:
        print('ok try again')



'''
Task1---------------

hamon aval k taraf price ro mizane
check kone digit dare ya na
age na --> bejaye inke bege mojadad emtehan kon
ta zamani k taraf doros gheymat vared kone ,
hey azash price bekhad



TASK2--------------
bad azinkie takm,il kardi

bia too no -->
agte taraf zad no--> dobare soalaro az aval beporse
ta zamani k taraf bezane yes





TASK3 (ADVANCED)-------
har dotaye ghablio anjam bede
ama tedad talashe namovafagh ro hesab kone
ag ishtar aza 3 bar
yek code mahsole moshabe ro 
hey gof na -->bege mojadad emtehan kon





'''
    
    




