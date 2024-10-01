# pre defined function



'''
a = 2
b = 5
c = sum((a,b))232
print (c)
'''

# user defined function


def M() :
    print ("satya sanatan dharam ki jai")
print (M())    



def a (a,b):
    ''' yaha par likha hua gyan comment nahi docstrings hota hai '''
    average = (a+b)/2
    return average
b = a(20,56)
print(b)
print(a.__doc__)    