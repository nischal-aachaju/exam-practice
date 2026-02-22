

# # items=["sql","123","python"]
# # fltr=list(filter(lambda x:x.isalpha(),items))
# # print(fltr)

# # products = [
# #  {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
# #  {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock':False}]  

# # is_instock=list(filter(lambda item:item["instock"]==True,products))
# # print(is_instock)
# # from random import randint

# # quiz=[
# #     {"qn":"question",
# #      "option":["A","B","C","D"],
# #      "ans":"B"},
    
# #     {"qn":"question",
# #      "option":["A","B","C","D"],
# #      "ans":"B"},
    
# #         {"qn":"question",
# #      "option":["A","B","C","D"],
# #      "ans":"B"},
# # ]

# # for q in quiz:
# #     for k,v in q.items():
# #         print(k,v)

# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     return a/b

# def inputs():
#     num1=int(input("Enter first num: "))
#     num2=int(input("Enter second num: "))
#     return num1,num2
# print('''
# 1 )add
# 2 )sub
# 3 ) mul
# 4 ) divide
# 5 )Exit  
#       ''')
# while True:
#     operation=input("Enter operation: ")[:1]

#     if operation=="1":
#         num1,num2=inputs()
#         print(add(num1,num2))

#     elif operation=="2":
#         num1,num2=inputs()
#         print(sub(num1,num2))

#     elif operation=="3":
#         num1,num2=inputs()
#         print(mul(num1,num2))
#     elif operation=="4":
#         num1,num2=inputs()
#         print(div(num1,num2))
#     elif operation=="5":
#         print("Exit....")
#         break
#     else:
#         print("invalid input")

# def remove_at_idx(lst,idx):

#     lst.pop(idx)
#     return lst

# lst=[1,2,3]
# print(remove_at_idx(lst,2))


# def vote (age):
#     if age<18:
#         raise ValueError("not eligible: Must be 18 or older")

#     else:
#         print("Can vote")

# try:
#     test_age=int(input("Enter age: "))
#     vote(test_age)
# except ValueError as e:
#     print(e)

# a=5
# b=4
# c=a/b
# print(type(c))

# numbers = ["t", "jk", 'jh', "y"]
# new_list = sorted(numbers)

# print(new_list)

# print(numbers)

# text = 1
# print(id(text))

# text = text + 1
# print(text)
# print(id(text))

t = ([1, 2], 3)
print(id(t))
t[0].append(4)
print(id(t))

a=[1,1,2,2,2,3]
a.remove(2)
print(a)
b=(1,2,2,3)
c=b.count(2)
print(c)