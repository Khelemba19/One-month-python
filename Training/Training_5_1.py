#creating a new file and adding data to it
import os

#with open("practice.txt", "w") as f:
    #f.write("Hi everyone \nWe are learning File I/O \nUsing Java \nI like programming in Java")


#replacing all the word "java" with "python"
with open ("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python") 
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)


#searching if it has the word "learning"
def check():
    word = str(input("Enter Word: "))

    with open("practice.txt", "r") as f:
        datas = f.read()
        if (word in datas):
            print("found")
        else:
            print("not found")

check()


#to find in which line
def checkline():
    word = "learning"
    line = 1
    with open("practice.txt", "r") as f:
        while True:
            data = f.readline()
            if (word in data):
                print("found in", line)
            line += 1
    return -1
    
checkline()


         
 

