# a=list(range(20,10,-2))
# print(a)

# a=2
# b=4
# b/=a
# print(b)

name=" Laxmi deptoka "
name=name.lower().strip()
name=name.split()
user_name="_".join(name)

print(user_name)

password="passion"
password=password.lower()
le={"a":"","s":""}
translator=str.maketrans("aeios","@3!0$")
# translator=str.maketrans(le)
secret_password=password.translate(translator)+"0##9"
print(secret_password)

word="I love south indian movie"
word_list=word.title().split()
word_list_rev=word_list[::-1]
word_rev=" ".join(word_list_rev)
print(word_rev)