# Items = [3,5,7,9,11,13]

# idx4=Items.pop(3)
# print(Items,idx4)
# Items.insert(1,idx4)
# print(Items)
# Items.append(idx4)
# print(Items)

# first_set = {23, 42, 65, 57, 78, 83, 29} 
# second_set = {57,83, 29, 67, 73, 43, 48}

# intersec=first_set.intersection(second_set)
# print(intersec)

# first_set=first_set.difference(intersec)
# print(first_set)


# month = {'jan': 47, 'feb': 52, 'march': 47,
#          'April': 44, 'May': 52, 'June':53, 
#          'july': 54, 'Aug': 44, 'Sept': 54}


# lst=list(set(month.values()))

# # lst={*()}
# # for i in month.values():
# #     lst.add(i)

# # lst=list(lst)
# print(lst)


# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
# tuple_list=tuple(set(sample_list))
# max_num=max(tuple_list)
# min_num=min(tuple_list)
# print("max num:",max_num)
# print("min num:",min_num)
# print(tuple_list)

# applicant = { "name": "Priya", 
#              "skills":["Java", "SQL"],
#              "experience_years": 1
#              } 

# required_skills = {"Python", "Java"} 

# for skill in applicant["skills"]:
#     if skill in required_skills:
#         if applicant["experience_years"]>= 2:
#             print(f"{applicant["name"]} is qualifued")
#         else:
#             print(f"{applicant["name"]} is not qualfyed")


# has_requierd_skill=len(set(applicant["skills"]).intersection(required_skills))>0
# has_experiences=applicant["experience_years"]>=2

# if has_experiences and has_requierd_skill:
#     print(f"{applicant['name']} is qualidied")

# else:
#     print(f"{applicant['name']} is no qualidied")


# banned_list={"scissors", "knife","lighter"}

# bag_weight=float(input("Enter bag weight (kg only): "))
# bag_items=input("Enter items which are in bag : ")
# bag_items=bag_items.lower().strip().split()

# is_bag_weight_satisfied=bag_weight<=7
# is_bag_items_safe=len(set(bag_items).intersection(banned_list))==0

# if is_bag_items_safe and is_bag_weight_satisfied:
#     print("Bag accepted")

# else :
#     print("Bag not allowed")

# group_A = {"Alice", "Bob", "Charlie", "David"}
# group_B = {"Eve", "Frank", "Charlie", "Grace"}

# if group_A.isdisjoint(group_B):
#     print("Groups are OK – no overlap.")
# else:
#     print("warning: Groups share at least one student!")


# sample_dict = {
#     'emp1':{'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name':'Shyam', 'salary': 500}
# }

# for key,Value in sample_dict.items():
#     if "Shyam" in Value["name"]:
#             Value["salary"]=8500

# print(sample_dict)


# b=2000
# a=2000

# print(b is a)
# c=[1,2,3]
# d=[1,2,3]

# print(c is d)


# a=5

# if (a & 1)==0:
#     print("even")
# else:
#     print("odd")
    
    
# a=2
# b=1
# print(a,b)
# # a=a-b
# # b=b+a
# # a=a+b

# # print(a,b)

# a=a^b
# b=a^b
# a=a^b

# print(a,b)


# a=14>>1
# print(a)

# print(~(-19))
# std={}
# for i in range(3):
#     name=input("Enter name:")
#     if name not in std:
#         contact=input("Enter number:")
#         std[name]=contact
# # print(std)


# i=2

# while i<5:

#     i=i+1

#     print(i)

#     i=i+1

# print(i)





# Ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']

# content_ratings={}

# for rating in Ratings:
#     if rating in content_ratings:
#         content_ratings[rating]+=1
#     else:
#         content_ratings[rating]=1
# print(content_ratings)

# sum=0

# i=2

# while i<5:

#     i=i+1

#     sum=sum-2

#     print(i)

# print(sum)

# a=[3,5,7,9] 

# sum=0

# i=2

# while i<len(a)-1:

#     i=i+1

#     sum=sum+a[3]

# print(sum)
# a=[3,5,7,9] 

# sum=0

# i=0

# while i<2:

#     if i==2:

#         sum=sum+a[i]

#         i=i+1

#         continue

#     sum=sum+a[i]

#     i=i+1

# print(sum)
# sum=0

# i=5

# while i!=0:

#     if i==2:

#         sum=sum+1

#         i=i-1

#         continue

#     i=i-1

# # print(sum)  
# a=[13,17,15,19]

# sum=0

# i=3

# while i!=0:

#     sum=sum+a[i]

#     i=i-1

# print(sum)

# i = 1

# while True:

#     if i%7 == 0:

#         break

#     print(i)

#     i += 1


# i = 1

# while True:

#     if i%2 == 0:

#         break

#     print(i)

#     i += 2

# i = 0  

# while i < 5:  

#     print(i)  

#     i += 1  

#     if i == 3:  

#         break  

#     else:  

#         print(45)

# var1 = -2

# var2 = 0

# while var1 != 0:

#     var1 = var1 + 1

#     var2 = var2 - 1

# print("var1: " + str(var1) + " var2 " + str(var2))
# n = 10

# answer = 1

# while n > 0:

#     answer = answer + n

#     n = n - 1

# print(answer)


# quiz = {
#     "q1":{
#         "question":"CPU stands for",
#         "options":{"A":"Central Processing Unit","B":"Center Process Unit","C":"Central Protocol Unit"},
#         "answer":"A"
#     },

#     "q2":{
#         "question":"RAM stands for",
#         "options":{"A":"Random Access Memory","B":"Read Access Memory","C":"Run Access Memory"},
#         "answer":"A"
#     },

#     "q3":{
#         "question":"ROM stands for",
#         "options":{"A":"Read Only Memory","B":"Run Only Memory","C":"Random Only Memory"},
#         "answer":"A"
#     },

#     "q4":{
#         "question":"Which is an input device?",
#         "options":{"A":"Monitor","B":"Keyboard","C":"Speaker"},
#         "answer":"B"
#     },

#     "q5":{
#         "question":"Which is an output device?",
#         "options":{"A":"Printer","B":"Mouse","C":"Scanner"},
#         "answer":"A"
#     },

#     "q6":{
#         "question":"Which language is used for web page structure?",
#         "options":{"A":"Python","B":"HTML","C":"C++"},
#         "answer":"B"
#     },

#     "q7":{
#         "question":"Python is which type of language?",
#         "options":{"A":"Low level","B":"High level","C":"Machine level"},
#         "answer":"B"
#     },

#     "q8":{
#         "question":"Which operator is bitwise AND?",
#         "options":{"A":"&","B":"|","C":"^"},
#         "answer":"A"
#     },

#     "q9":{
#         "question":"Which data type is immutable in Python?",
#         "options":{"A":"List","B":"Dictionary","C":"Tuple"},
#         "answer":"C"
#     },

#     "q10":{
#         "question":"Which keyword is used to define function in Python?",
#         "options":{"A":"func","B":"define","C":"def"},
#         "answer":"C"
#     }
# }

# score=0

# for value in quiz.values():
#     print(f"question: {value["question"]}")
#     for i,j in value["options"].items():
#         print(i,":",j)
#     chooes=input("Chooes: ").upper()
#     if chooes == value["answer"]:
#         print("right")
#         score+=1
#         print(f"score={score}")
#     else:
#         print("Wrong")
#         score-=1
#         print(f"score={score}")
    
#---binary searching

# def binary_searching(arr,target):
#     low=0
#     high=len(arr)-1
#     while low < high:
#         mid=(low+high)//2
#         if arr[mid]==target:
#             print(mid)
            
#         elif target>mid:
#             low=mid+1

#         else:
#             print("sfd")
    

# arr=list(range(1,101))
# # print(arr)
# target=int(input("Enter target: "))
# binary_searching(arr,target)

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid

#         elif arr[mid] < target:
#             low = mid + 1

#         else:
#             high = mid - 1

#     return -1

# arr = [1, 3, 5, 7, 9, 11, 13]
# target = 7

# result = binary_search(arr, target)

# if result != -1:
#     print("Element found at index:", result)
# else:
#     print("Element not found")


# linear searching

# lst=list(range(1,11))
# target=6
# idx=0
# for i in lst:
#     if target==i:
#         print(f"Target found in {idx} index")
#         break
#     idx+=1

#Binary searching


# def binary_searching(lst,target):   
#     low=0
#     high=len(lst)-1 
#     while low <= high:
#         mid=(low+high)//2
#         if lst[mid]==target:
#             print(f"Target found in {mid} index")
#             break   
#         elif lst[mid] < target:
#             low=mid+1
#         else:
#             high=mid-1        
#     else:
#         print("Not found")
        
# binary_searching(list(range(1,21)),16)

# from math import ceil, floor


# a=7.8
# print(floor(a))


# def he():
    
#     a=5
#     def hee():
#         nonlocal a
#         b=5
#         print(a,b)
#     hee()

# he()

#-------------- lambda function-----------
# sum=lambda x,y:x+y
# print(sum(2,4))


# square =lambda x:x*x
# print(square(3))

# num= lambda x:x%2==0

# even=num(7)
# print(even)
# if even:
#     print("even")
# else :
#     print("odd")


# nam="nischalShrestha"
# len_name= lambda name:len(name)
# print(len_name(nam))

# x=2
# y=3
# z=4
# max_num= lambda x,y,z:max(x,y,z)
# print(max_num(x,y,z))

'''2. You are managing an e-commerce inventory database. Given a list of product
dictionaries, write a Python program using a filter() and lambda function to
extract and display only the products that are currently in stock (instock: True)
products = [
 {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
 {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock':
False}
]'''


# products = [
#  {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
#  {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock':False},
#  {'id': 3, 'name': 'PC', 'category': 'electronics', 'price': 1500, 'instock':True},
#  ]

# in_stock=list(filter(lambda x:x["instock"]==True,products ))
# print(in_stock)


"""3. Given a list of course dictionaries, write a Python program using a lambda function
to filter and display only those courses that belong to the 'history' genre.
course = [ {'title': 'Ancient Civilizations', 'genre': 'history'}, {'title': 'Corporate
Finance', 'genre': 'commerce'}, {'title': 'Modern World History', 'genre': 'history'} ]
    """
# courses = [ {'title': 'Ancient Civilizations', 'genre': 'history'},
#           {'title': 'CorporateFinance', 'genre': 'commerce'}, 
#           {'title': 'Modern World History', 'genre': 'history'} ]

# course_genre_history=list(filter(lambda course:course["genre"]=="history",courses))
# print(course_genre_history)

'''
4. You have a list of blacklisted domains. Write a Python program using a lambda
function to filter a list of emails and return only the ones that are considered spam
those that match any domain in the blacklist.
emails = ['ram.sharma@gmail.com', 'spam@hooya.com', 'virus@malware.net',
‘shyam.kumar@workcorp.com’]
blacklist = ('@hooya.com', '@malware.net')
'''

# emails = ['ram.sharma@gmail.com',
#           'spam@hooya.com', 
#           'virus@malware.net',
#           'shyam.kumar@workcorp.com']

# blacklist = ('@hooya.com', '@malware.net')

# spam_email=list(filter(lambda email:(blacklist[0] in email) or (blacklist[1] in email),emails))

# print(spam_email)

'''5. Applying a 20% discount to all items in a shopping cart:
price = [100, 50, 200, 75] implement using lambda function'''

# price = [100, 50, 200, 75]

# price_d=list(map(lambda x:int(x-x*0.2) ,price))

# print(price_d)

'''
6. Create a function, skip_two that takes a list as input, and returns a list that: Starts
with the second element of the input. While skipping every two elements. Does
not keep any element whose index is greater than 11
'''




# lst=["Nischal","Nirjal","samir","Anurag","Norman","1","2","3","4","5","6","7","8","9"]

# def skip_two(lst):
#     new_list=[]
#     for i in range(1,11):
#         new_list.append(lst[i])
#     return new_list
# print(skip_two(lst))

"""7. Create a function, remove_at_idx, with the following features:
 Takes a list as its first argument.
 Takes a positive index as its second argument.
 Removes the element at the given index and decreases the index of all
subsequent elements by one.
 Returns a new list
    """
# lst=["Nischal","Nirjal","samir","Anurag","Norman","1","2","3","4","5","6","7","8","9"]  

# def remove_at_idx (lst,idx):
#     new_lst=lst.copy()
#     new_lst.pop(idx)
#     return new_lst
# idx=2
# print(lst)
# print(remove_at_idx(lst,idx))

# lst=[4,2,6,2,8,9,4,2]

# def he(l):
#     return l+1

# a=list(map(he,lst))
# print(a)


# try:
#     num =int(input("Enter a number: "))

#     result=100/num

#     print(f" Result : {result}")
    
# except ValueError:
#     print("value must be number")

# except ZeroDivisionError:
#     print("can't divied by zero")

# except KeyboardInterrupt:
#     print(" keyboard interrupt")

# except Exception:
#     print("Some went wrong")

