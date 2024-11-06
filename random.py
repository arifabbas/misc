

user_status={'arif':'active', 'abbas':'active', 'mishra':'inactive'}
for user,status in user_status.copy().items():
    if status=='inactive':
        del user_status[user]
print(user_status)

user_status1={'arif':'active', 'abbas':'active', 'mishra':'inactive'}
new_user_status={}

for user,status in user_status1.items():
    if status=='inactive':
        new_user_status[user]=status;
print(new_user_status)



print("-----------------")
user_status1={'arif':'active', 'abbas':'active', 'mishra':'inactive'}

for i in user_status1:
    print(i)

print("-----------------")

print(range(2,10))

for n in range(2,2):
    print(n);

dict={"name" : "arif","age" :30}
print(dict)


def key_func(**keyword):
    for kw in keyword:
        print(kw,":",keyword[kw]);
key_func(name="Arif",age=30);


list_num=[1,2,3,4,5,6,6,77,88,8]
print(list_num)

tuple_num=(1,2,3,4,5,6,6,77,88,8)
print(tuple_num)

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))

print(concat("earth", "mars", "venus", sep="."))

