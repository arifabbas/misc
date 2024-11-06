from xml.dom.expatbuilder import TEXT_NODE
import xml.dom.minidom

#parser= xml.dom.minidom.parse("C:/Users/pc969706/Desktop/Python/Programming/aci.xml")

parser= xml.dom.minidom.parse("C:/Users/pc969706/Desktop/Python/Programming/filexml.xml")


print(parser.nodeName)
print(parser.firstChild.tagName)


print(parser.getElementsByTagName("to"))
to= parser.getElementsByTagName("to")


for i in to:
    print(i.firstChild.nodeValue)
    if i.hasChildNodes:
        j=i.childNodes
    for k in j:
        if k.nodeType == k.TEXT_NODE:
            print(k.nodeValue)


print(parser.getElementsByTagName("note"))

pl=parser.firstChild.childNodes
for i in pl:
    print(i.nodeName)

# fvtenants= parser.getElementsByTagName("fvTenant")
# print(fvtenants.length)
# print("lCOwn","\t","Name","\t","ModTS")
# for fvtenant in fvtenants:
#     print(fvtenant.getAttribute('lcOwn'),"\t",fvtenant.getAttribute('name'),"\t",fvtenant.getAttribute('modTs'))

parser.unlink()