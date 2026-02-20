# # # a=list(range(20,10,-2))
# # # print(a)

# # # a=2
# # # b=4
# # # b/=a
# # # print(b)

# # name=" Laxmi deptoka "
# # name=name.lower().strip()
# # name=name.split()
# # user_name="_".join(name)

# # print(user_name)

# # password="passion"
# # password=password.lower()
# # le={"a":"","s":""}
# # translator=str.maketrans("aeios","@3!0$")
# # # translator=str.maketrans(le)
# # secret_password=password.translate(translator)+"0##9"
# # print(secret_password)

# # word="I love south indian movie"
# # word_list=word.title().split()
# # word_list_rev=word_list[::-1]
# # word_rev=" ".join(word_list_rev)
# # print(word_rev)

# # # num=int(input("Enter number: "))
# # num=1
# # if num %2==0: 
# #     print("then number is even")
# # else :
# #     print("The number is odd")

# # # char=input("Enter char:")
# # char="a"
# # char=char[:1].lower()
# # print(char)
# # vowel=["a","e","i","o","u"]
# # if char in vowel:
# #     print("Vowel")
# # else:
# #     print("Consonent")
    
    
# # months = {
# #     1: "January",
# #     2: "February",
# #     3: "March",
# #     4: "April",
# #     5: "May",
# #     6: "June",
# #     7: "July",
# #     8: "August",
# #     9: "September",
# #     10: "October",
# #     11: "November",
# #     12: "December"
# # }

# # num=int(input("Enter number betn 1 to 12: "))
# # if num >0 and num <=12:
# #     print(f"Month: {months[num]}")
# # else:
# #     print("Invalid number")
# # from random import randint

# # snapple={

# # 0 :'Flamingos turn pink from eating shrimp.',
# # 1 : "The only food that doesn't spoil is honey.",
# # 2 : 'Shrimp can only swim backwards.',
# # 3 : "A taste bud's life span is about 10 days.",
# # 4 : 'It is impossible to sneeze while sleeping.',
# # 5 : 'It is illegal to sing off-key in North Carolina.'
# # }

# # num=randint(0,5)
# # print(snapple[num])

# # words=["ram","shyam","hari","rameshor"]
# # word_len=[]
# # for word in words:
# #     word_len.append(len(word))
# # print(word_len)

# # Ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
# # content_rating={}

# # for rating in Ratings:
# #     if rating in content_rating:
# #         content_rating[rating]+=1
# #     else:
# #         content_rating[rating]=1
# # print(content_rating)

# from random import randint
# random_num=randint(1,50)
# attemp=7
# while True:
#     # num=int(input("Enter number: "))
#     num=4
#     if num==random_num:
#         print("Correct")
        
#         print(f"you correct in {7-attemp}")
#         attemp=attemp-1
#         break
#     elif attemp==0:
#         print("You lose")
#         print(f"{attemp} attemp left")
        
#         break
    
#     elif num>random_num:
        
#         print("hint: try low value")
#         print("attemp left",attemp,"attemp")
#         attemp=attemp-1
#     elif num<random_num:
        
#         print("hint:try high value")
#         print("attemp left",attemp,"attemp")
#         attemp=attemp-1

# num=2
# for i in range(1,11):
#     print(f"{num} x {i} ={num*i}")
    
# students = [

#     {"name": "ram", "math_grade": 43},

#     {"name": "hari", "math_grade": 70},

#     {"name": "sita", "math_grade": 90}

# ] 

# for student in students:
#     if student["math_grade"]>=70:
#         print(f"{student["name"]} is accepted")
        
#     else:
#        print(f"{student["name"]} is rejected")
        
 
# lst1=[1,2,3,4,5] 
# lst2= [3,4,5,6,7]
# common_num=[]
# for i in lst1:
#     if i in lst2:
#         common_num.append(i)
# print(common_num)


# lst=[1,2,3,4] 
# print(lst[:2],lst[3:])
# l=[1,2,3,4]
# l.pop(2)
# l.insert(1,"a")
# print(l)


# sum=0
# while True:
#     # num=int(input("Enter positive number only: "))
#     num=0
#     if num <0:
#         continue
#     elif num ==0:
#         print(f"Total:{sum}")
#         break
#     else:
#         sum+=num
        
# total=0
# counter=1
# while counter<=50:
#     total+=counter
#     counter+=1
# print(total)

# vowel=["a","e","i","o","u"]
# vowel_found={*()}
# number_of_vowel=0
# word="AEwerzdfIerthOUUUU".lower()

# for i in word:
#     if i in vowel:
#         if i not in vowel_found:
#             number_of_vowel+=1
#         vowel_found.add(i)

# print(number_of_vowel) 


# word="hello my name is nischal".lower()
# vowel=["a","e","i","o","u"]
# vowel_found={*()}
# for i in word:
#     if i in vowel:
#         vowel_found.add(i)
        
# print(len(vowel_found))


num=int(input("Enter number: "))

if (num//2)*2==num:
    print("even")
else:
    print("odd")