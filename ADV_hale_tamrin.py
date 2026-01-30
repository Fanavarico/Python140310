
"""

حل تمرین

Created on Sat Mar  1 17:32:06 2025

@author: apm




"""



'''

REVIEW-----------


Reserved----------------------
python built in function ( print() ,input() [str] ,
                          len() , type())

keywords---->
if --> just if (yek shart ro ebsanji)
if else --> do rahi baz koni
if elif else --> dorarahi , dorahi 

[ag chanat shart --> or , and , not , in]

halghe--->
iteration --> for 
sharti bezari ta oon shartt --> while




def--->
class--->




'''


code=input('lotfan codet bede')
name=input('lotfan name mahsolo')
price=input('lotfan price ro bde')

price='۱۲۳۴'

#function (amalakrd) ---> farsi ---> englisi


# function --> BOX

# farsi---> BOX --> englisi tahvil begiram


#vorodim-->adade farsie
#calcualtion --> farsio for --> if --> list-->float
#khroojiam -->ye adade ke englisi



def persian_digit_to_english_digit(persian_numb):
    new_numb=[]
    
    if persian_numb.isdigit():
        
        for digit in persian_numb:
            if digit=='۰':
                new_numb.append('0')
                
            elif digit=='۱':
                new_numb.append('1')
                
            elif digit=='۲':
                new_numb.append('2')
                
            elif digit=='۳':
                new_numb.append('3')
                
            elif digit=='۴':
                new_numb.append('4')
                
            elif digit=='۵':
                new_numb.append('5')
                
            elif digit=='۶':
                new_numb.append('6')
                
            elif digit=='۷':
                new_numb.append('7')
                
            elif digit=='۸':
                new_numb.append('8')
                
            elif digit=='۹':
                new_numb.append('9')
                
        khali=''
        
        newnumb=khali.join(new_numb)
        
        
        english_numb=float(newnumb)
        
        #print(english_numb)

        return english_numb

    else:
        return None
    
    
    
    
    
    
    
    
    
    
    
    
    
    








new_price=[]

if price.isdigit():
    for digit in price:
        if digit=='۰':
            new_price.append('0')
            
        elif digit=='۱':
            new_price.append('1')
            
        elif digit=='۲':
            new_price.append('2')
            
        elif digit=='۳':
            new_price.append('3')
            
        elif digit=='۴':
            new_price.append('4')
            
        elif digit=='۵':
            new_price.append('5')
            
        elif digit=='۶':
            new_price.append('6')
            
        elif digit=='۷':
            new_price.append('7')
            
        elif digit=='۸':
            new_price.append('8')
            
        elif digit=='۹':
            new_price.append('9')
            
    khali=''
    
    newprice=khali.join(new_price)
    
    
    price=float(newprice)
    
    #*** TypeError: sequence item 0: expected str instance, int found
    

            
else:
    print('please insert digits')       

print(price)

print(new_price)


#if price digit dare ya nadare
#ag dashte bashe edame bede
#ag ndashte bashe edame nadee
#farsi----> englisish?


text=f'''

-----plutus--------
product name : {name}
product code : {code}

total price : {price*0.7}


------
'''

print(text)







#-------------------inja ideal tarin ja

def persian_digit_to_english_digit(persian_numb):
    new_numb=[]
    
    if persian_numb.isdigit():
        
        for digit in persian_numb:
            if digit=='۰':
                new_numb.append('0')
                
            elif digit=='۱':
                new_numb.append('1')
                
            elif digit=='۲':
                new_numb.append('2')
                
            elif digit=='۳':
                new_numb.append('3')
                
            elif digit=='۴':
                new_numb.append('4')
                
            elif digit=='۵':
                new_numb.append('5')
                
            elif digit=='۶':
                new_numb.append('6')
                
            elif digit=='۷':
                new_numb.append('7')
                
            elif digit=='۸':
                new_numb.append('8')
                
            elif digit=='۹':
                new_numb.append('9')
                
        khali=''
        
        newnumb=khali.join(new_numb)
        
        
        english_numb=float(newnumb)
        
        #print(english_numb)

        return english_numb

    else:
        return None
    
    
    
    
    
name=input('name mahsooL:')
code=input('code mahsool')

price=input('code mahsool')

new_price=persian_digit_to_english_digit(price)

if price==None:
    print('lotfan adad vared konid')

text=f'''

-----plutus--------
product name : {name}
product code : {code}

total price : {new_price*0.7}


------
'''

print(text)

#-----
#----10000


phone_number=input('salam shoamr emobileto begoo:')


new_number=persian_digit_to_english_digit(phone_number)



#----------------------------------------------------


#------ 1000

phone_number=input('shoamreye tamaseto begooo :')

new_phone_number=[]
if phone_number.isdigit():
    for digit in phone_number:
        
        if digit=='۰':
            new_phone_number.append('0')
            
        #elif --->1
        
    #-->2
    #......
    
    
    
    #new phoen number --->
    
            




#--> sms --> englisi




'''

tamrin jalase 3





'''

'''

fibonachi


donbale ha -->


1 3 5 7 9 11 13 15 ,..... donbale
adadi


1 2 4 8 16 28 ,...... --> n

fibonachi

0 1 1 2 3 5 8 13 

'''



for i in range(0,10):
    print(i)



for i in range(0,10,2):
    print(i)
'''
0
2
4
6
8
'''




for i in range(0,10):
    print(i)


for i in range(0,10):
    print(i,end=' ')




for i in range(0,10):
    print(i)


'''


0 
1
2
3
5
8
13
,.....


'''




#print
a=0
b=1
c=1


print(a)
print(b)
print(c)


d=c+b
print(d)

e=d+c
print(e)


#-----------------
a=0
b=1


n=10

for i in range(n):
    print(a)
    a,b=b,a+b


#i-->0 ---> print(0)  --->0  a=1 , b=1
#i-->1 ---> print(1) --->1   a=1  ,b=2
#i--->2 -->print(1) --->1   a=2 , b=3
#



n=int(input('salam y adad bede behet fibonachi ro bdm'))
a=0
b=1
for i in range(n):
    print(a)
    a,b=b,a+b




def fibonachi(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        a,b=b,a+b
      
        
      
def fibonacci_recursive(n):
    if n<=0:
        return 0
    
    elif n==1:
        return 1
    
    else:
        return fibonacci_recursive(n-1) +fibonacci_recursive(n-2)
    
    
    
#jomle he ro mdie

fibonacci_recursive(0)
fibonacci_recursive(1)
fibonacci_recursive(2)

fibonacci_recursive(3)

n=10
for i in range(n):
    print(fibonacci_recursive(i))
    
#==================================


        
      


'''

Tamrine 2





'''

#1 2 3 4 5 6 7 8 9 10
for i in range(1,11):
    print(i)


# %2 

#%2 -->0 zoj
#dfard


for i in range(1,11):
    #zoje
    if i%2==0:
        print(i+5)
        
    else:
        print(i*5)
'''
5
7
15
9
25
11
35
13
45
15

'''



#-----------
reshte=input('yek reshte bede behem:')

len(reshte)
#a l i p i l e h v a r

if len(reshte)%2==0:
    #nimeye avalesho namayesh bede
    print(reshte[0:len(reshte)/2])
else:
    #print(reshte[len(reshte)/2:len(reshte)])
    print(reshte[int(len(reshte)/2):])
    #niemye dovom



#shart
'''


2 ta reshte
agar reshteye 1 dar rehsteye 2 bashad ---> reshteye1 ro hazf kon az reshte 2

age na -> reshte ye 1 b ebteda o entehash ezaf kon




'''
reshte1='ali'
reshte2='alipilehvar'


reshte1='ali'
reshte2='pilhevar'


if reshte1 in reshte2:
    #hast
    #hazf konam
    khoroji=reshte2.replace(reshte1,'')
    

else:
    khoroji=reshte1 + reshte2 + reshte1
    #nist

print(khoroji)




def hazfe_2(reshte1,reshte2):
    if reshte1 in reshte2:
        #hast
        #hazf konam
        khoroji=reshte2.replace(reshte1,'')
        

    else:
        khoroji=reshte1 + reshte2 + reshte1
        
    #print(khoroji)
    return khoroji



new_zarf=hazfe_2('ali','alipilehvar')

new_zarf=hazfe_2('ali','pilehvar')


#----------------

'''


D1={'a':1,'b:3,c:2}
D2={'a'"2" , b:3, c:1}


new_dic={'b':3}


'''


D1={'a':1,'b':3,'c':2}
D2={'a':2,'b':3,'c':1}




for key in D1:
    if key in D2 and D1[key]==D2[key]:
        
        #key --> a , b , c--> tekrar shode
        #D1[key] --> D2[key] -->value
        
        new_dsict={key :D1[key] }
            

new_dsict
#{'b': 3}



common_items={key :D1[key] for key in D1 if key in D2 and D1[key]==D2[key] }




#_--------------------------------
a=[10,20,30,30,40,50]

#tekrario--> set

b=set(a)
print(b)


#-----
'''


2 ta list dari

fght anasere monhaser be fardeshono


1-->tekrari dare

2-->khdoesh tekrari ddare




'''

list1=[1,2,2,3,4,5,6]
list2=[6,7,7,8]

#-->1,2,3,4,5,6,7,8



list1.extend(list2)

print(list1) #[1, 2, 2, 3, 4, 5, 6, 6, 7, 7, 8]

print(set(list1))
#{1, 2, 3, 4, 5, 6, 7, 8}







#-----------------------------

files=['new.jpg','prog.exe','lib.gif','yechizi.mov']

#-->{'jpg','exe','gif'}

files=['new.jpg','prog.exe','lib.gif','yechizi.mov','myfile.py.exe']

mylist=[]

for file in files:
    
    new_file=file.split('.')
    
    #new_file[1] #dovomin idnex--->? 
    
    if len(new_file)>2:
        mylist.append(''.join(new_file[1:]))
        
    else:
        mylist.append(new_file[1])
    
    #print(new_file[1])
    
    

print(mylist)


print(set(mylist))
#{'gif', 'jpg', 'mov', 'exe'}




files=['new.jpg','prog.exe','lib.gif','yechizi.mov','myfile.py.exe']

#-->{'jpg','exe','gif'}

mylist=[]
for file in files:
    file_index=file.find('.')
    mylist.append(file[file_index+1:])
    
   
print(mylist)
#['jpg', 'exe', 'gif', 'mov']

print(set(mylist)) 
#{'gif', 'jpg', 'mov', 'exe'}



#-------------------------------------

#-------------------------------------


'''
reshte az virid daryaft konad

karacterh haye ba mogheiate indexe zoj ro ahzf kone




'''


s='alipilehvar'
#l p l h a

def deleven(s):
    s=(s[1::+2])
    print(s)
    
    

s[2:5] #2 3 4

s[1::2]
#------------------------
reshte=input('yek reshte')
dovom=int(input('adad begoo:'))
sevom=int(input('adad begoo:'))


hazfi=reshte[dovom:sevom+1]

myfinal=reshte.replace(hazfi,'')




def hazf_kone(reshte,dovom,sevom):
    hazfi=reshte[dovom:sevom+1]

    myfinal=reshte.replace(hazfi,'')
    
    #print(myfinal)
    return myfinal





#ta zamani ke-->while true



mynumbers=[]

while True:
    
    vorodi=input('adad bede:')
    
    if vorodi=='exit':
        break
    
    else:
        mynumbers.append(vorodi)
        
        
        
print(mynumbers)





#-----------------------------


mynumbers=[]
lenmynumb=[]

while True:
    
    vorodi=input('adad bede:')
    
    if vorodi=='exit':
        break
    
    else:
        
        mynumbers.append(vorodi)
        lenmynumb.append(len(vorodi))
        

print(mynumbers)
print(lenmynumb)



max(lenmynumb)



longest=''

for item in mynumbers:
    if len(item) > len(longest):
        
        longest=item
        
        
print(longest)
    

max(mynumbers,key=len)



def nahaee():
    mynumbers=[]
    lenmynumb=[]
    while True:
        vorodi=input('adad bede:')
        if vorodi=='exit':
            break
        
        else:
            
            mynumbers.append(vorodi)
            lenmynumb.append(len(vorodi))
    longest=''

    for item in mynumbers:
        if len(item) > len(longest):
            
            longest=item
            
    print(longest)
    
    return longest



    

            




#--------------
reeshte=input('yek chizi bede')

if reeshte.isdigit():
    a=int(reeshte)
    
else:
    #----
    pass



    
    
    
#-------------------

def calculator():
        
    while True:

        numb1=input('adade aval ro bedid:')
        numb2=input('adade dovom ro bedid:')
        amalgar=input('amalgar ro bedid')
        
        if numb1=='exit':
            break
        
        else:
            if amalgar=='jam':
                javab=float(numb1)+float(numb2)
                return javab
            
            elif amalgar=='tafrigh':
                javab=float(numb1)-float(numb2)
                return javab
            
            elif amalgar=='zarb':
                javab=float(numb1)*float(numb2)
                return javab
                
                
            elif amalgar=='tavan':
                javab=float(numb1)**float(numb2)
                return javab
            
            elif amalgar=='taghsim':
                if numb2==0:
                    print('division on 0 is infinit')
                    return None

                else:
                    javab=float(numb1)/float(numb2)
                    return javab
                
                
        


