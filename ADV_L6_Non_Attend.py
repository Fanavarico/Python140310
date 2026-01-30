
"""
Created on Mon Mar 17 20:12:31 2025

@author: apm

In The Name of gOD



ADVL6_Non_Attend



"""


'''

strategy 1---> psudocode az bala b paeen 


strategy2----> functions 


strategy 3---> class




---------functions-------------

vorodi ----> BOX ---> Khorojii

vorodi --- BODY- ---> KHOORJI

ba vorodi , ba khoroji
b vorodi , bdone khoroji
bdone vorodi, ba khoroji
bdoen vorodi , bdone khoroji




#print, return 

#**ghavanini hast k shjoam bayad rayat konu
#name baraye yek variable bzari

def name(input1,input2,input3,....):
    
    body calculation
    
    #print()
    
    return output1,output2,output3,....

'''


def add(a,b):
    c=a+b
    return c



zarf=add(10,20)



def add(a,b):
    c=a+b
    print(c)
    
add(10,20) #30

zarf=add(10,20) #NONE







#-------------------------
#name
#esme vorodi ha
#KJhode tabe tozihat dashte bashe



def add(a,b):
    c=a+b
    return c 



def add(number1,number2):
    answer=number1+number2
    
    
    
    
    return answer




#-------------
#esme
#add()




def add(number1,number2):
    '''
    this fucntion is for adding two nuber together

    '''
    
    
    
    answer=number1+number2
    
    
    
    
    return answer



#add()






def add(number1,number2):
    '''

    Parameters
    ----------
    number1 : float
        first number.
    number2 : float
        second number.

    Returns
    -------
    answer : float
        this is addition odf nubner1 to number2.

    '''


    
    answer=number1+number2
    
    
    
    
    return answer



add()

#zaroorate zihba nevisi
#esdmse khana




#traqsnlate_persian_text_TO_



#-------------

#tabe nevisi
#2 marhalas

#marhale 1 ---> misazish sakhtaresho (run nmishe) shenakhte mishe b python


#marhale 2 --> usage , estefade hast --> call , seda koni 




def add(a,b):
    c=a+b
    return c

#etefaghi nmniofte




add(4,5)

#ag khoroji ndre print dre , zarf nmizari --> trabe ha rare


#return

zarf=add(4,5)

#print
#for
#VARIABLE

#a=10
#b=30
#b=a


#step1 --> run mikoni sakhtareto -->etefaghi nmiofte
#stepe 2 zarf ro mikhoen zarf misaze va mosavi gharr mide

#bad esme tabe at ro mikhone va ta b paranetz nareside fek mikoen yek zarfe digar hast
#b paranetz mirese python mige ee in k functione
#bezar beram bala check konm bnbinm vojod dre ya na
#ag mndsht error mide

zarf=tafrigh(5,6)
#NameError: name 'tafrigh' is not defined

#vase hamine ma ghabl az seda zadane tabe miaym m isazimesh va
#badesh call mikonim



#hala k rft bala check krd did vojod dare tabe
#negah mikone k tabeye ma chanta vorodi dare
#negah mikone chanta vorodi dre
#miad check mikone k b andazeye doros vorodi dadim ya na
#ag kam bdim error mide
#ag ziad bdim error mide


zarf=add(10,20,30)
#TypeError: add() takes 2 positional arguments but 3 were given

zarf=add(10)
#TypeError: add() missing 1 required positional argument: 'b'

#agar 2 ta dade bashi vorodie tabe ro ba vorodie to yeksan migire
#a=10
#b=20

#body va dakhele tabe ro run mikone
#tamaammm

#vaghty b return mirrese adadde 30 ro barmidri barmigrdone

#koja? jaee k sedash zadi
#koja sedash zadi? jkoloye yek zarf

zarf=add(10,20)
zarf=30

#a , b , c --> 3 ta zarfi bood k bsoorate movaghat sakhte
#vaghty return mikone
#tamam ein se zarf ro mishkone
#yani vojode khareji ndrn fght movaghat bodan
#k karaye tooye tabe ro bokonan
#pas fght tooye tabe shenakhte shdoe hastan
#local


#birone tabe ghabele dastsressis nis







def add(a,b):
    c=a+b
    return c




d=add(10,40)

#a=10 hazf
#b=40 hazf
#c=10+40=50 hazf

#d=50

print(a) #NameError: name 'a' is not defined
print(b) #NameError: name 'b' is not defined
print(c) #NameError: name 'c' is not defined


#-------------



c=50
def add(a,b):
    c=a+b
    return c



d=add(100,50)

print(c)


#oonae k vojod ndrno hazf mikone
#onae k vojod daran---> b halat eghabl barmigrdone


#b yek variabl dastresi peyda konm birone tabe


#globalesh kon

def add(a,b):
    global c
    c=a+b
    return c

d=add(10,20)


#nisan hazf mikone ( zarfa mishkone)
#onaee k already hast , mizare adsade ghabli
#onae k globalan ro hazf nmikone

#-----------------------------------------------


#f=m*a


def newton(mass,acc):   
    force=mass*acc
    return force



zarf2=newton(10,20)
    
#zarf2=200


zarf2=newton(10)
#TypeError: newton() missing 1 required positional argument: 'acc'

#agha man mikham default --> pish farz bzarm
#begam agah amishe trf hamishe 2 ta vorodie
#ama y vorodi optional bashe
#y vorodi ejbari

#ooni k optionalesh koni 
#too ddele tabat ch adadi bzri jash??



#ooni k mikhay default , = bzar

def newton(mass,acc=9.8):   
    force=mass*acc
    return force


newton(10,20) #200

newton(10) #error nmide
#98

#-----------

def newton(mass,acc):   
    force=mass*acc
    return force



newton(10,20)


a=10
b=20
newton(a,b)


a=10
print(a)


newton(10,20)


newton(mass=10,acc=20) #200

#damet garm


#aya man mitonm yeseri az argument (input)
#yeserisho bgm fght adad bzn
#yeserisho bgm na fght bayad esm bzni
#bale python hame kar mitoni koni



def newton(*,mass,acc):   
    force=mass*acc
    return force


newton(10,20)
#TypeError: newton() takes 0 positional arguments but 2 were given

#bad az * , jahr arg miad , yani elzamie esmesh

newton(mass=10,acc=20)





def newton(mass,acc,/):
    force=mass*acc
    return force

#harchi ghabl az / biad
#yani fgght adad bvayad bzni



newton(10,20)

newton(mass=10,acc=20)




#bade * hatman esmeshono bayad bzni
#ghable / bayad fgth adad bzni




def myfunc(a,b,c,d):
    f=a*b*c*d
    return f



myfunc(10,20,30,40)
myfunc(a=10,b=20,c=30,d=40)





def myfunc(a,b,/,*,c,d):
    f=a*b*c*d
    return f

myfunc(10,20,30,40) #errorr
myfunc(a=10,b=20,c=30,d=40) #error

myfunc(10,20,c=30,d=40)




#------------

def myfunc(a,b,c,d,e,f,g,h,i,j,k,l,m,n,p):
    pass


def myfunc(a):
    '''
    
    a--> list
    '''
    
    c= a[0] + a[1]
    return c 

#myfunc(1)


myfunc([10,20,30,40,50,60]) #30





#---------

def karmandan():
    
    pass



def moshtarian():
    pass


def modiran():
    pass

def beyne_shobe():
    pass


#4 ta hamzaman rooye server rune

#script dari har 4 ytabe dare run mishe ok?


#yhek frdi dar ghesmate karmandan error bokhore
#kole barname stop mishe




a=10
b=20

c=a+b[0] #yk dastore k error dre

print('salam')

#harjaee error bashe dar code
#stop mishe barename



# 4 ta tabe dari

#error mokene pish 





#man k midonm momkene codam error dashte abshge

#erroro hazf konam

#ino agha anjam bde
#ta zamani k error ndsht

#error didi , torokhodaaaaaaaaa error nshon nde 
#(yani barnameye maro stop nakon)
#fgth oon tike ro ejra nkon 






def karmandan():
    try:
        a=10
        b=20
        c=a+b[0]
        
        print('karmande aziz mojodi:')
        print(c)
        
        pass
    
    except Exception:
        
        print('unexpected error happen')
        

id_dvlps='@apmaa'

def karmandan():
    try:
        a=10
        b=20
        c=a+b[0]
        
        print('karmande aziz mojodi:')
        print(c)
        
        pass
    
    except Exception:
        
        print('unexpected error happen')
        #telegram.send_message('unexpected error')
        
        #telegram.bot_send(id_dvlps,'errori pish omde')
        
        
        
        
def karmandan():
    try:
        a=10
        b=20
        c=a+b[0]
        
        print('karmande aziz mojodi:')
        print(c)
        
        pass
    
    except Exception as e:
        
        print('unexpected error happen')
        #telegram.send_message('unexpected error')
        
        #telegram.bot_send(id_dvlps,'errori pish omde')
        #telegram.bot_send(id_dvlps,f'errori pish amade : {e}')
             
        
        


def moshtarian():
    print('moshtarie aziz....')
    pass


def modiran():
    print('modire aziz')
    pass

def beyne_shobe():
    pass


#mazayaye 1--->
#error pish baidkole barename nemikhabe

#mazaye 2--> ag error pish omd b taraf naamayehs mdie mige error

#mazaye 3 --> mitonim error ro bfrsim baraye khodemon


#-----------------------------------------
#-----------------------------------------

'''

strategy 1 ---> psudocode



strategy2 ---> functions


strategy 3 ----> class



'''





#bank bia besazim

def create_account(name,initial):
    global balance
    balance=initial
    print('sakhte shod')
    
    
    
def show_balance():
    global balance
    print(balance)
    
    
    
def deposition(amount):
    global balance
    balance=amount+balance
    
    
def atm(amount):
    global balance
    balance=amount-balance

#too tabeat agar errror ham bashe 
#ejra mishe



create_account('ali', 400)

show_balance() #NameError: name 'balance' is not defined



create_account('mohsen', 200)
show_balance() 


#shakhsi saazi nmitoni koni
#





'''
dar bazi az application ha , karbordhaaa


1 moshkele bozorg---> tabe ha bveham marbotan ama
avriabl hjja local hastan 



moshkele 2
shakhsi sazi nmishe

to yejahaee niaz dari k object dashte bashi

yekseri shey mikhay az y type


yek sewri msohtai az ye bank
yekseri danesh amooz dari az yek madrese
yekseri varezeshkar az yek varzxesh]]
    
    
    
yek seri CHIZZZ dari az yek Type chizz




yekseri safe dari az yek application



az ychi (type,class) -->bekani besazi --> object



function --- class


'''


def add(a,b):
    global c
    c=a+b
    return c


zarf=add(10,20) 

#na a
#na b
#na c

#local hastan



def tafrigh(z,y):
    
    d=z+y+c
    return d


zarf2=tafrigh(10,20)
#NameError: name 'c' is not defined



'''


CLASS





C
C++


syntax


printf
cout

class




class------


variables ---> attributes,property
Function ---> methods



'''

def bankk():
    balance=100
    return balance
    

a=bankk()




class BANK:
    balance=100
    
    


a=BANK()


#khoroji ee nmide


#to dari yekobject az yekj class misazi

#attributes, methods

#baraye dastressi b ina
#bayad aval yek object bsazi


#zarf = class()


#zarf.attribute
#zarf.function()








class BANK:
    balance=100
    
    


a=BANK()

zarf=a.balance




#------------------------------------------
#infrustructure---> zirsakht
#real bank benevisim 
#website, 
#narm afzar
#narm afzar goshi, laptob ,....


#real world bank management system --> infrsutructure




class BANK:
    balance=100
    
    
a1=BANK()
a2=BANK()
a3=BANK()


a1.balance
a2.balance
a3.balance



#migam ahgha ag man bekham yek 

#yek account besazi --> nam , sen , mojodie avalie

a1=BANK()

#a1=BANK(NAME,age, ....)



#class BANK(name,age,...)
    


class BANK:
    #chizaee k dos dari yek frd vaghty obejct msiaze bayad
    #vared kone ro bad az self tooye init briz
    
    def __init__(self,name,age,initial_balance):
        pass




a1=BANK()
#TypeError: BANK.__init__() missing 3 required positional arguments: 'name', 'age', and 'initial_balance'


a1=BANK('ali',30,3000)

a1.name #AttributeError: 'BANK' object has no attribute 'name'
a1.age #AttributeError: 'BANK' object has no attribute 'age'


# def __init__(self,name,age,initial_balance): --> fght
#mige k in se ta vorodi ro bgir
#jaee zkahir nmikone


#self --> yek khonas koli ghafase dre


#har ghasfase ye esm dre


#self.ali

#yek ghafase e bname ali hast tooye self (khonate)

#pas ag mikhay zakhire koni chizio

#tooye yek ghafase az in khoen az in self



class BANK:
    #chizaee k dos dari yek frd vaghty obejct msiaze bayad
    #vared kone ro bad az self tooye init briz
    
    def __init__(self,name,age,initial_balance):
        self.name_kamel=name
        self.sen=age
        self.balance=initial_balance

#agha ag yeki obejct khast bsaze
#hatman azash name, age , initial_balance bekha


#vorodi ee k grfti esmehs name
#tooye zarfe name harchi has
#beriz too ye ghafase ye self, k esmesh hast name_kamel



#age roi bgir briz tooye sen

a1=BANK('ali',30,3000)

#name
#zkahire
a1.name #AttributeError: 'BANK' object has no attribute 'name'

a1.name_kamel #'ali'

a1.age

a1.sen



class BANK:
    #chizaee k dos dari yek frd vaghty obejct msiaze bayad
    #vared kone ro bad az self tooye init briz
    
    def __init__(self,name,age,initial_balance):
        self.name_kamel=name
        self.sen=age
        self.balance=initial_balance
        
    #har tabe msiazi self ro bzar
    def welcome(self):
        print('salam khosh amadid ', self.name_kamel)
        
        
    
a1=BANK('ali',30,1000)
a1.name_kamel
a1.welcome #na attributes k nis function ()
a1.welcome()
#salam khosh amadid  ali
#moshkele yek hal shod 
#Man alan mitonm koli tabe benevuisam ba estefade az self
#koel in variable haro beham vasl konam



a2=BANK('vahid',40,100000)
a2.name_kamel  
a2.welcome()   
#salam khosh amadid  vahid
#shakhsi sazi konm




#b hadafam residasm




#-----------------------

#deposition()
#atm

#show balance



#show_balance --> mojodisho trf mikhad begire

#show_balance()








class BANK:
    
    def __init__(self,name,age,initial):
        
        self.name=name
        self.age=age
        self.balance=initial
        
        
    def welcome(self):
        print('salam khosh amadid moshtarie aziz ', self.name)
        
    
    def show_balance(self):
        print('mojodie shoma hast: ', self.balance)
        
        
    def deposit(self,amount):
        
        self.balance= self.balance+ amount
        
        print('ba moafaghiat anjam shod')
        
        print('mojodie shoma : ', self.balance)
        
        
    def atm(self,amount):
        
        self.balance=self.balance-amount
        
        print('bardasht ba moafaghiat anajam shod')
        
        print('mojodie shoma: ', self.balance)
        
    
    
    
    
#a1=BANK(ALI,30,1000)

#a1.welcome()

#a1.show_balance()


#deposit(4000)

#atm(3000)
    

#object assignment---------
a1=BANK('ali',30,1000)

#attributes-----------
a1.name #ali
a1.age #30


#methods-------()
a1.welcome()
#salam khosh amadid moshtarie aziz  ali


a1.show_balance()
#mojodie shoma hast:  1000

a1.deposit(2000)


a1.show_balance()
#mojodie shoma hast:  3000

a1.atm(1000)
#bardasht ba moafaghiat anajam shod
#mojodie shoma:  2000

a1.show_balance()
#mojodie shoma hast:  2000




a2=BANK('vahid',50,100000000)
a2.name

a2.welcome()
#salam khosh amadid moshtarie aziz  vahid

a1.welcome()
#salam khosh amadid moshtarie aziz  ali


a2.show_balance()
#100000000


a1.show_balance()

#2000


a2.deposit(4323453244234523)
#mojodie shoma :  4323453344234523
a2.atm(10000)
#mojodie shoma:  4323453344224523
a2.show_balance()
#mojodie shoma hast:  4323453344224523


a1.show_balance()
#mojodie shoma hast:  2000



#-----------------------




#def --> return daran

#frotn ----> 
#name , age , 5000

a1=BANK()

#fastapi , django


#python --- > html , dart , c++ qt

#a1=BANK(inja , senesho , )


#click mizane rooye welcome


#dokmas


#front 

#if user.clicked.welcome_button --> 

#a1.welcome() -->text return

#zarf=a1.welcome()


#dart , 


#div< dart , colour : pink , nackground=black


#--------------
#dokme --> mojodii


#if user.clicked.mojodi_button --> 
#zarf_jadid= a1.show_balance()


#divdiv < red , green ,..... ->



class BANK:
    
    #shoamre meli , name pedar , .......
    
    def __init__(self,name,age,initial):
        
        self.name=name
        self.age=age
        self.balance=initial
        
        
        #------ vorodi zakhire
        
        self.bank_name='PLUTUS'
        
        #numpy
        
        #Numpy.random.uinifrom(10000,1000000)
        
        #self.bank_card=.....
        
        
        
    def welcome(self):
        text=f'salam khosh amadid moshtarie aziz {self.name}'
        return text
        
    
    def show_balance(self):
        return self.balance
        
        
    def deposit(self,amount):
        
        self.balance= self.balance+ amount
        
        print('ba moafaghiat anjam shod')
        
        print('mojodie shoma : ', self.balance)
        
        
    def atm(self,amount):
        
        self.balance=self.balance-amount
        
        print('bardasht ba moafaghiat anajam shod')
        
        print('mojodie shoma: ', self.balance)
        
    


#===============================================
class BANK:
    
    def __init__(self,name,age,initial):
        self.name=name
        self.age=age
        self.balance=initial
         
    def welcome(self):
        print('salam khosh amadid moshtarie aziz ', self.name)
        
    def show_balance(self):
        print('mojodie shoma hast: ', self.balance)
           
    def deposit(self,amount):
        self.balance= self.balance+ amount
        print('ba moafaghiat anjam shod')
        print('mojodie shoma : ', self.balance)
        
        
    def atm(self,amount):
        self.balance=self.balance-amount
        print('bardasht ba moafaghiat anajam shod')
        print('mojodie shoma: ', self.balance)
        


#codeeto sakhti bor obugesho dr biar
#real
#omdm donyaye vaghei

a1=BANK('ali',40,4000)
a1.welcome()
a1.show_balance()
a1.deposit(1000) #5000
a1.atm(2000) #3000

a1.show_balance()


a1.atm(10000) #-7000

a1.atm(1000000000) #mojodie shoma:  -1000007000



class BANK:
    
    def __init__(self,name,age,initial):
        self.name=name
        self.age=age
        self.balance=initial
         
    def welcome(self):
        print('salam khosh amadid moshtarie aziz ', self.name)
        
    def show_balance(self):
        if self.balance >100:
        
            self.balance=self.balance - 100
            
            print('mojodie shoma hast: ', self.balance)
        else:
            print('shjoma mojodie moshahedeye mojodi ham nadari')
           
        
        
    def deposit(self,amount):
        #saghf 
        self.balance= self.balance+ amount
        print('ba moafaghiat anjam shod')
        print('mojodie shoma : ', self.balance)
        
        
    def atm(self,amount):
        if amount < self.balance:
            self.balance=self.balance-amount
            print('bardasht ba moafaghiat anajam shod')
            print('mojodie shoma: ', self.balance)
            
        else:
            print('mojodie shoma kafi nemibashad')
        
        
a1=BANK('ali',30,1000)

a1.show_balance()

a1.deposit(2000)   

a1.atm(10000)
#mojodie shoma kafi nemibashad

a1.atm(2800)

a1.atm(50)


a1.show_balance()
#shjoma mojodie moshahedeye mojodi ham nadari




#-------PISHRAFT DARE

#TABE HAYE JADID EZAFE KONI


#history 
#SEDASH KONI --> tarakonesh haro neshoon bde

#yek tabe benvisi k jam kone
#chghd bardahst shdoe
#chghd vriz shide
#.......




class BANK:
    
    def __init__(self,name,age,initial):
        self.name=name
        self.age=age
        self.balance=initial
        self.history_list=[]
         
    def welcome(self):
        print('salam khosh amadid moshtarie aziz ', self.name)
        
    def show_balance(self):
        if self.balance >100:
        
            self.balance=self.balance - 100
            
            print('mojodie shoma hast: ', self.balance)
        else:
            print('shjoma mojodie moshahedeye mojodi ham nadari')
           
        
        
    def deposit(self,amount):
        self.history_list.append(amount)
        
        #saghf 
        self.balance= self.balance+ amount
        print('ba moafaghiat anjam shod')
        print('mojodie shoma : ', self.balance)
        
        
    def atm(self,amount):
        if amount < self.balance:
            self.history_list.append(-amount)
            
            self.balance=self.balance-amount
            print('bardasht ba moafaghiat anajam shod')
            print('mojodie shoma: ', self.balance)
            
        else:
            print('mojodie shoma kafi nemibashad')
        
        
        

    def history(self):
        
        print('-------------')
        print('-----trakonesh ha-----')
        
        for i in self.history_list:
            print(i)
            print('-----')
            
    def advanced_history(self):
        
        if self.balance>500:
            self.balance=self.balance-500
            
            print('-----------------------')
            print('-----trakonesh ha-----')
            print('-----------------------')
            
            for i in self.history_list:
                
                if i<0:
                    print('Bardasht : ', i)
                else:
                    print('Variz : ',i)
                
                print('-----')
                
                
        else:
            print('shoma mojojodoie moshahede tarakonesh ra nadarid')
            
            
            
        




#a1.history()


a1=BANK('ali',30,1000)

a1.show_balance()

a1.deposit(2000)   


a1.atm(1000)
a1.atm(200)


a1.deposit(3000)   

a1.deposit(4000)   

a1.deposit(5000)   



a1.atm(2000)



a1.history()

a1.advanced_history()


#yek class jadid besazi k class ghablio
#tabe hasho dashte bashe----> ers bari


#inheretence--->



#yek hesabe arzi (dollar)

#class-->tamam evzihegi haye clas ghablio dahste bashe +
#koli tabe jadid bzari



#TOOYE PARANTEZ oon clas


#class CURRENCY_BANK

#a1=BANK()
#a1=CURRENCY_BANK() --> na tanha tamam etavabe ye BANK , tabne haye jadid ham dare

#esmesho bnvisi too partanetz bnvisi BANK



#a1=CURREENCY_BANK()
#DASTE KHDOETE AMA HAVASET BAZSHE

#in gharrae tamame tabe haye bank ro dahste bashe
#pas htaman bayad vorodishash vorodi haye bANK ro dashte abshe



class CURRENCY_BANK(BANK):
    
    #hatman bayad bgiireeeeee
   # def __init__(self,name,age,initial)
   
   def __init__(self,name,age,initial,currency_id):
       #3 taro zakhire jadid zakhire
       super().__init__(name,age,initial)
       
       self.currency_id=currency_id
       
       
       
a1=CURRENCY_BANK('ali', 40, 1000, 1234)
      

a1.currency_id

a1.welcome() #salam khosh amadid moshtarie aziz  ali
a1.show_balance() #mojodie shoma hast:  900


     

    


class CURRENCY_BANK(BANK):
    
    #hatman bayad bgiireeeeee
   # def __init__(self,name,age,initial)
   
   def __init__(self,name,age,initial,currency_id):
       #3 taro zakhire jadid zakhire
       super().__init__(name,age,initial)
       
       self.currency_id=currency_id
       
       self.currency_balance=0
       
       
   def welcome_english(self):
       print('welcome to our bank dear, ', self.name)
       
       
       
     
   def exchange(self,tooman_amount):
       
       if self.balance > tooman_amount:
       
           self.balance = self.balance - tooman_amount
           
           dollar_amount = tooman_amount /95000
           
           self.currency_balance = self.currency_balance + dollar_amount
           
           print('finish...')
           
           print('Rial account : ', self.balance)
           print('Currency account :' , self.currency_balance)
           
       else:
           print('not enough balance')
            
       
       
       
b=BANK('ali',30,1000)     
type(b)
b.welcome_english()  
#AttributeError: 'BANK' object has no attribute 'welcome_english'





       
       
a1=CURRENCY_BANK('ali', 40, 1000, 1234)
     
#----bank

type(a1) # __main__.CURRENCY_BANK

a1.show_balance() #mojodie shoma hast:  900

a1.deposit(200000) #mojodie shoma :  200900


a1.deposit(100000) 
#mojodie shoma :  300900

a1.show_balance()

a1.atm(800)
#mojodie shoma:  300000



#---------------
a1.welcome_english()
#welcome to our bank dear,  ali

a1.exchange(200000)


#100 000

#2.2

'''
Rial account :  100000
Currency account : 2.1052631578947367

'''




        
        
