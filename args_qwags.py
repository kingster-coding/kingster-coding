def mayank(*args,**kwargs):
    for arg in args:
        print(arg)
    for b in kwargs:
        print (b,kwargs[b])    
mayank(1,2,3,4,5,6,7,8,9,a=2)

# args bina variable ko add kiye infinite value ko store kar sakta hai 
# kwargs ki madad se arqs ke andar hum alag se varible bhi store kar sakte hai