'''Identifiers 
     Names in python programmes are called Identifiers. 
     Name can be variable name, class name or method name
    Rules to define Identifiers in Python:-
       Only Allowed values are
           alphabet symbols (upper case and lower case) a to z or A to Z
           digits (0 to 9)
           underscore (_)
        Identifiers should not start with digits
        Python is case sensitive language
           total =10 and TOTAL =10  both are different
        Keywords are not allowed to used as Identifiers
        No length limit for identifiers 
        If the identifier starts with underscore(_) symbol then it is private
        If identifiers starts with 2 underscore(__) symbol then it is strongly private
        If identifier starts and ends with 2 underscore (__main__)symbol 
        then it is language specific identifier, special variable defined by python itself 

'''

# Implementation of Identifier rules
# Remove comment one by one and check
cash=10
# ca$h = 10   # error
cas_h=10
total123 = 10
# 123total =10 # error
# True = 12 # error
# False = 0 # error
umbrella = 'rain'
print(umbrella)
test_case_001 = 12 # error
print(test_case_001)