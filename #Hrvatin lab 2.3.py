#Hrvatin lab 2.3.py
#Period 8

print("Task 1")
name =input("Please enter you first and last name\n")
space =name.find(" ")
fname =name[0:space]
lname = name[space+1 :len(name)]
print(fname.title(),lname.title())

difname =name .upper()
newfname =difname[0].lower()+difname[1:space+1]
newlname =difname[space+1].lower()+difname[space+2:len(difname)]

print(newfname,newlname,"\n\n", sep="")

print("Task 2")
phrase =("Once you start down the dark path,"+\
        "forever will it dominate your destiny")

newphrase =phrase.upper()\
.replace("A","1")\
.replace("E","2")\
.replace("I","3")\
.replace("O","4")\
.replace("U","5")

print(newphrase,"\n\n")


print("Task 3")

thirds =(int)(len(phrase)/3)
phr1 =phrase[0:thirds]
phr2 =phrase[thirds+1:thirds*2]
phr3 =phrase[thirds*2+1:thirds*3]

print(phr2,"\n",phr3,"\n",phr1,"\n\n",sep="")

print("Task 4")

number =(input("Please enter five digits\n"))

print((int)(number[0])+(int)(number[1])+(int)(number[2])+(int)(number[3])+(int)(number[4]),"\n\n")

print("Task 5")

phrase2 ="Why, you stuck-up half-witted scruffy-looking nerf herder."

print(phrase2[0:len(phrase2):2])
#idk how to do reverse
print(phrase2[-len(phrase2):len(phrase):2])
