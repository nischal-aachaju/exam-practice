
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



with open("a.txt","r") as f1:
    with open("b.txt","w") as f2:
        while True:
            word=f1.readline()
            if word=="":
                break
            f2.write(word)

# with open("a.txt","r",encoding="UTF8")  as f1 :
#     with open("z.txt","w") as f2:
#         for line in f1:
#             print(f1)
#             f2.write(line)
