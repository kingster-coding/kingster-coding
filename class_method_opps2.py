# class and object

class details:
    def __init__(self,full_name,stu_id,age,number):

        self.full_name = full_name
        self.stu_id = stu_id
        self.age = age
        self.number = number

    @classmethod

    def add(cls,address):
        cls.address = address

mayank =  details("mayank vajpayee","B2292R10400156",21,6269975825)

'''details.add("nagod")
print(details.address)'''
print(mayank.full_name,mayank.stu_id) 

mayank.add("nagod")
print("mayank")


