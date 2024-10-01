''' map wo function hai jisko use karke hum kise bhi function ke elements ke upar apply kar sakte hai'''

number = ["1","2","3","4","5",
          "6","7","8","9","10"]
'''
print (type(number))
print (number)'''

'''numbers = list(map(int,number))

print (numbers)'''

'''
a = [5,6,6,8,9,78,4,5,5]

add = list(map(lambda a: a+1,a))
print (add)
'''


#  reduce
from functools import reduce


list = [1,2,3,4,5]
add = reduce(lambda a,b: a*b,list)
print (add)
