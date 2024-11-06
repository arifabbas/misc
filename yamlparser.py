import yaml
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

stream1= open("C:/Users/pc969706/Desktop/Python/Programming/fileyaml.yaml", 'r', encoding="utf-8")
myYaml=yaml.load(stream1,Loader)

for key,value in myYaml.items():
    print (key + " : " + str(value))



stream2= open("C:/Users/pc969706/Desktop/Python/Programming/mulitpleFiles.yaml", 'r', encoding="utf-8")
documents=yaml.load_all(stream2,Loader)


for doc in documents:
    print("New Document")
    for key,value in doc.items():
        print (key + " : " + str(value))

