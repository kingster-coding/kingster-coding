  # global variable

a = ("mayank")
def vajpayee():
    print (a)

vajpayee ()

print (a)

# local variable

def b():
    c = ("aloo")
    print (c)

b()


# local and global variable

z = (" this is real global variable ")

def x():
    global v
    v = ("bech ke chacha hai")
    z = ("the is local wale chacha")
    print(z)
    print(v)

x()
print(z)
print(v)








