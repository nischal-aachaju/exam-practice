
# with open("a.txt","r") as f1:
#     with open("d.txt","w") as f2:
#         for line in f1:
#             f2.write(line)

# with open("a.txt","r") as f_a:
#     with open("b.txt","w") as f_b:
#         while True:
#             text=f_a.readline()
#             f_b.write(text)
#             print(text)
#             if text=="":
#                 break



# with open("a.txt","r") as f1:
#     with open("b.txt","w") as f2:
#         while True:
#             word=f1.readline()
#             if word=="":
#                 break
#             f2.write(word)

# with open("a.txt","r",encoding="UTF8")  as f1 :
#     with open("z.txt","w") as f2:
#         for line in f1:
#             print(f1)
#             f2.write(line)


# with open("story.txt","r") as f:
#     counter=0
#     while True:
#         if f.readline()=="":
#             print(f"total count:{counter}")
#             break
#         counter+=1

# with open("number.txt","r") as f1:
#     with open("square.txt","w") as f2:
#         while True:
#             line=f1.readline()
#             if line=="":
#                 break
#             num=int(line)
#             square=num*num
#             square=str(square)+"\n"
#             f2.write(square)


with open("story.txt","r") as f1:
    with open("u.txt","w") as f2:
        while True:
            line=f1.readline()
            if line=="":
                break
            f2.write(line.upper())
 