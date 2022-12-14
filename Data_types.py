'''
Data types in Python
    Python is dynamically typed programming language i.e. no need to declare data type for variables
    In Python range, size, maxi or mini etc are not present. 
    In Python everything is object i.e. range, size, maxi or mini concept are not present
int data type
    It takes integer type of values without decimals
float data type
    It takes only decimal values
string data type
    It takes any string of characters
    String are enclosed with single,double or triple inverted commas  
boolean data type
    It is used for logical type data. The only allowed value for bool type are True and False
    T of True and F of False are compulsorily of capital letters
complex data type
    It takes only complex values whose one part is real and one part is imaginary
 Examples of all data type
'''
a=10
type(a) # class ‘int’

b=12.45
type(b) # class ‘float’

c="Python class"
type(c) # class ‘string’

a=10
b=20

a>b # ‘False’
type(a>b) # class ‘bool’ 

a<b # True 
type(a<b) # class ‘bool’

x= 10+20j
y= 20+30j
z= x+y 
print(z) # 30+50j
type(z) # class ‘complex’

s='''Have you completed your "previous tasks" ''' 
print(s)  # 'Have you completed your "previous tasks" '
