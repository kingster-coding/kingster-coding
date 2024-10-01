dictionary = {"mayank":"programmer","deepanshu":"youtuber","abhay":"thekedar","naino":{"work":"girlfriend","age":24,"place":"mera dill","fav food":"ramen","mentality":"nibbi"}}

print (dictionary)
print (type(dictionary))
print (dictionary["naino"])
print (dictionary ["mayank"])

dictionary ["pathary"] = "londiyabaaz"
print (dictionary)
print (dictionary ["pathary"])
del dictionary["abhay"]
print (dictionary)


# create a dictionary using python where we can take input from the user?

prac = {"a":"apple","b":"ball","c":"cat","d":"dog"}

#i = input("enter a word:-")
#print(prac[i])



d = {"a":1,"b":2,"c":3,"d":4}
print (d)
print (type(d))

z = input("enter the word")
print (d[z])