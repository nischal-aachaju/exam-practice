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