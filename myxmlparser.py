from xml.dom.expatbuilder import TEXT_NODE
import xml.dom.minidom

parser= xml.dom.minidom.parse("E:/DevGod/Python God Mode/MyPython/Programming/filexml.xml")
print(parser.nodeName) #nodeName for parsed xml is document
print(parser.firstChild.tagName)#first Child is the parent Node
i=parser.firstChild.childNodes 
print(i) #new line char is also a child node
for j in i:
    print(j.nodeName,j.nodeValue) #nodeName for Element is Tag Name , Node Value for Element is None
#Also, Node Name for Text Node is text and Node Value is String



print(parser.getElementsByTagName("to"))
to= parser.getElementsByTagName("to")


for i in to:
    #print(i.firstChild.nodeValue)
    if i.hasChildNodes:
        j=i.childNodes
        print(j)
        for k in j:
            # if k.nodeType == k.TEXT_NODE:
            print(k.nodeName,k.nodeValue) #nodeName for Element is Tag Name , Node Value for Element is None
#Also, Node Name for Text Node is text and Node Value is String


print(parser.getElementsByTagName("note"))

print(parser.firstChild.childNodes.length) # New line character is also treated as a childNode


parser1=xml.dom.minidom.parse("E:/DevGod/Python God Mode/MyPython/Programming/aci.xml")
fvtenants= parser1.getElementsByTagName("fvTenant") #list of all found elements
print(fvtenants.length)
print("lCOwn","\t","Name","\t","ModTS")
for fvtenant in fvtenants:
    print(fvtenant.getAttribute('lcOwn'),"\t",fvtenant.getAttribute('name'),"\t",fvtenant.getAttribute('modTs')) # Tag with Attributes Values

parser.unlink()
parser1.unlink()