a= input("what year were you born?")

b= input("what year is it now?")

c= int(b)-int(a)

print (f"you are",c,"years old")



def age(a,b):
    c= int(b)-int(a)
    return c

print(age(1990,2020))