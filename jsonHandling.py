import json

mydict={}

with open('E:/DevGod/Python God Mode/MyPython/Programming/file.json', 'r' , encoding="utf-8") as f:
    #for loading json from a file using load()
    print(json.load(f))
    
    # f.seek(0)
    # newdict=json.load(f)

    # print("My New dictionary is Newdict=",newdict)

    string= str("""{"car":"TATA", "price": 200000}""")
    print(string)
    #loading json from a string using loads()
    mydict= json.loads(string)
    
    # print(mydict)



    #print(type(x))
    #print(type(json.load(f)))
    #mydict=json.load(f)


print("My dictionary is mydict=",mydict)

#converting mydict to mudictstr using dumps()
mydictstr=json.dumps(mydict)
print("MyDict in string format=",mydictstr)

#now creating a new json file and dump the string using dump()

with open('E:/DevGod/Python God Mode/MyPython/Programming/newfile.json', 'w' , encoding="utf-8") as nf:
    json.dump(mydict,nf)
