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

applicant = { "name": "Priya", 
             "skills":["Java", "SQL"],
             "experience_years": 1
             } 

required_skills = {"Python", "Java"} 

# for skill in applicant["skills"]:
#     if skill in required_skills:
#         if applicant["experience_years"]>= 2:
#             print(f"{applicant["name"]} is qualifued")
#         else:
#             print(f"{applicant["name"]} is not qualfyed")


has_requierd_skill=len(set(applicant["skills"]).intersection(required_skills))>0
has_experiences=applicant["experience_years"]>=2

if has_experiences and has_requierd_skill:
    print(f"{applicant['name']} is qualidied")

else:
    print(f"{applicant['name']} is no qualidied")