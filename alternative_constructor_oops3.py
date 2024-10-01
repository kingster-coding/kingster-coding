class Info:
    def __init__(self,name,stu_id,number,):
        
        self.name = name
        self.stu_id = stu_id
        self.number = number


    def information(self):
        return f"name is {self.name},student id is {self.stu_id},number is {self.number}"


    @classmethod
    def spliting(cls,string):
        new = string.split(" , ")
        print(new)

mayank = Info("mayank",234,4885) 

print(mayank.information())

Info.spliting("kingster,22,44366")
