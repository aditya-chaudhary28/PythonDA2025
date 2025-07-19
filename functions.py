def greet():
    print("Hello Everyone")
    
greet()
greet()
greet()
greet()

print([greet()for i in range(10)])



g_var=10
def scope():
    l_var=5
    print(g_var,l_var)
    
scope()


# Input from users
n="Enter Your Name"
def hi(n):
    print("Hello, ",n)
    
hi("Aditya")

print("*"*50)
# Passing The Parameter
def subm(a=0,b=0):
    return a+b
    
subm(2,1)
subm(4,5)
var=subm(4,5)
print(var*2)


# Calling Different Functions
lst=[1,2,3,4,5]
def sq(lst):
    return[i**2 for i in lst]
print(sq(lst))