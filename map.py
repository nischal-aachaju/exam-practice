# lst=[1,2,3,4,5,6]

# sq_lst=list(map(lambda x:x*x , lst))
# print(sq_lst)

# sq_lst=[]
# for i in range(1,31):
#     sq_lst.append(i*i)
# sq_first=sq_lst[:5]
# sq_last=sq_lst[-5:]
# print(sq_first)
# print(sq_last)

# color= ["Black", "Red", "Maroon", "Yellow"]
# color_code= ["#000000", "#FF0000","#800000", "#FFFF00"]

# json_output=[]  

# for i in range(len(color)):
#     json_output.append({"color":color[i],"color_code":color_code[i]})
    
# print(json_output)

# Data = [{"V":"S001"}, 
#         {"V": "S002"}, 
#         {"VI": "S001"}, 
#         {"VI": "S005"},
#         {"VII":"S005"}, 
#         {"V":"S009"},
#         {"VIII":"S007"}]

# data_set={*()}
# for i in Data:
#     for j in i.values():
#         data_set.add(j)
# print(data_set)

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}

# merge_dict={}
# for i in dic1.keys():
#     merge_dict[i]=dic1[i]

# for i in dic2.keys():
#     merge_dict[i]=dic2[i]

# for i in dic3.keys():
#     merge_dict[i]=dic3[i]

# print(merge_dict)

dic={ 2: 20, 3: 30, 6: 60, 4: 40,1: 10, 5: 50}

ass_dict=dict(sorted(dic.items(),key=lambda i:i[1],reverse=True))
print(ass_dict)

a=(1,2),(2,4)
print(dict(a))