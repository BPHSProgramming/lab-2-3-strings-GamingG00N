#Hrvatin lab 2.3.py
#Period 8

print("Task 1")
name =input("Please enter you first and last name\n")
space =name.find(" ")
fname =name[0:space]
lname = name[space+1 :len(name)]
print(fname.title(),lname.title())

difname =name .upper()
lowerfname =difname[0].lower()
upperfname =difname[1:space+1]
lowerlname =difname[space+1].lower()
upperlname =difname[space+2:len(difname)]

print(lowerfname,upperfname,lowerlname,upperlname,"\n\n\n", sep="")

phrase =("Once you start down the dark path,"+\
        "forever will it dominate your destiny")

newphrase =phrase.upper()
newestphrase =newphrase.replace("1","1"),newphrase.replace("e","2"),newphrase.replace("i","3"),newphrase.replace("o","4"),newphrase.replace("u","5")

print(newestphrase)
#i have no clue what im doing