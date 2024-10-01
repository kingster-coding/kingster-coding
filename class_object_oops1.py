# class and object

class details:
    def __init__(self,full_name,stu_id,age,number):

        self.full_name = full_name
        self.stu_id = stu_id
        self.age = age
        self.number = number

mayank =  details("mayank vajpayee","B2292R10400156",21,6269975825)
print(mayank.full_name,mayank.stu_id) 




class phone_specification:
    def __init__(self,brand,model,ram,internal,price):

        self.brand = brand
        self.model = model
        self.ram = ram
        self.internal = internal
        self.price = price

info = phone_specification("acer","ryzen 5",16,528,50000)
print(info.price,info.ram)


        
