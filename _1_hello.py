for x in range (0,11):
    print(x)
  
  

for x in range (5):
    for y in range(x+1):
        print('* ',end='')
    print()

for i in range (6):
    for x in range(i):
        print('& ',end='')
    print()

dic ={
    'a'  : "ABCD",
    'dollar': 78,
    'pound' : 73,
    'uros'  : 86,
    'country' : {'u.s' : 'United nation',
                 'u.k' : 'united Kingdom'}
}



print(dic.get('a'))


print('\n\nfunction \n')


def sq(n):
    return (n**2)
obj = sq(2)
print(f'ans is : {obj}')



def l(string):
    return len(string)
print(f'length of python is ',{l('python')})



# adding 2 in array

def add(list):
    arr=[]
    for i in list:
        arr.append(2+i)
    return arr
listt=[2,4,6,8,10]
final = add(listt)
print(final)

adding = lambda a,b : a+b


print(adding(10,40))



def fun1():
    string = 'ttt'

    def fun2():
        print(string)

    fun2()
fun1()



# date and time 

import time

print(time.localtime(time.time()))






# swaping variables 

a = 10
b = 20
print (f'{a} and {b}')

c = a
a = b
b = c 

print (f'{a} and {b}')

print (" swaping variables 2nd method")

a = 10
b = 20
print (f'{a} and {b}')

a = a+b 
b = a-b
a = a-b
print (f'{a} and {b}')


