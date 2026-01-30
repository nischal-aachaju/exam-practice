
# name=input("Enter name")
# name=name.lower()
# name=name.strip()
# name=name.split()
# name="_".join(name)
# print(name)


# password=input("Enter password: ")
# # password="Passion"
# password=password.lower()
# clean={"a":"@","e":"3","i":"!","o":"0","s":"$"}
# translator=str.maketrans(clean)
# strong_passord=password.translate(translator)
# strong_passord=strong_passord+"0##9"
# print(strong_passord)

# num=input("Enter number")

# num="+977  9849-241-223"
# clean={"-":"",",":"","+":""," ":""}

# a=str.maketrans(clean)
# num="+"+num.translate(a)
# print(num)


# word="joNH ceNA"
# word=word.title()

# print(word.title())



# word=" I love south indian movies"
# word=word.strip()
# word=word.split()

# rev_word=word[-1::-1]
# rev_word=" ".join(rev_word)
# rev_word=rev_word.title()
# print(rev_word)


# c=5
# b=2

# # c=c//b
# c//=b

# print(c)

# print(type(6//2))

# print(type(3+3.0))



# dict={
#     "hello":"oii",
#     "ng":"dfg"}  
# print("oii" in dict) #output=?

# a=6
# b=2

# c=a/b
# print(type(c))


# a = [1,2,3]
# b = a
# print(a is b) # 
# a = [1,2,3]
# b = [1,2,3]
# print(a is b) # output=?
# print(a==b) # optput=?

# a={*()}
# a.add("A")
# print(a)

# print(type(a))


# months = {
# 1: "January",
# 2: "February",
# 3: "March",
# 4: "April",
# 5: "May",
# 6: "June",
# 7: "July",
# 8: "August",
# 9: "September",
# 10: "October",
# 11: "November",
# 12: "December"
# }


# try:
    
#     num=int(input("enter num: "))
#     if num in months:
#         print(f"The month is {months[num]}")

#     else :
#         print(f"enter between 1 to 12")
        
# except ValueError:
#     print("Please enter num")



# ismember=(input("do you have membership card?(y/n) "))
# print(ismember)
# num=True
# print(type(num))


# marks = int(input("Enter student's marks: "))
# if marks >= 90 and marks<= 100:
#     grade = "A+"
# elif marks >= 80 and marks <= 89:
#     grade = "A"
# elif marks >= 70 and marks <= 79:
#     grade = "B+"
# elif marks >= 60 and marks <= 69:
#     grade = "B"
# elif marks >= 50 and marks <= 59:
#     grade = "C"
# elif marks >= 40 and marks <= 49:
#     grade = "D"
# elif marks < 40:
#     grade ="E"
# else:
#     grade = "Invalid marks"
# print(f"Marks: {marks}")
# print(f"Grade: {grade}")




# num1=4
# num2=4
# num3=3
# if(num1 ==num2 ==num3 ):
#     print("all are equal")

# elif num1!=num2 and num1!=num3 and num2!=num3:
#     print("all are different") 
    

# else :
#     print("two are equall")
    
    
# import turtle

# t = turtle.Turtle()
# t.speed(1) # Set drawing speed (0 is fastest, 1 is slowest)

# # Set multiple pen properties at once
# t.pen(pencolor="red", pensize=5, fillcolor="blue")

# t.forward(200)
# t.left(90)
# t.forward(100)

# # Lift the pen, move without drawing, then put it down
# t.penup()
# t.forward(50)
# t.pendown()

# # Change color and continue drawing
# t.pencolor("green")
# t.forward(100)

# turtle.done() # Keep the window open until clicked


# from random import randint

import random 


num=random.randint(0,4)

print(num)