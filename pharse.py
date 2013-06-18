#{http://www.filemaker.com/fmpxmlresult}ERRORCODE - 0
#{http://www.filemaker.com/fmpxmlresult}PRODUCT -   1
#{http://www.filemaker.com/fmpxmlresult}DATABASE -  2
#{http://www.filemaker.com/fmpxmlresult}METADATA -  3
#{http://www.filemaker.com/fmpxmlresult}RESULTSET - 4

from xml.dom import minidom
xmldoc = minidom.parse('CCC dso 1.xml')
itemlist = xmldoc.getElementsByTagName('ROW')
childs = itemlist[0].childNodes


for child in childs :
    if child.childNode == []:
        print child.nodeValue





print len(itemlist)
print itemlist[0].attributes['course'].value
for s in itemlist:
    print s.attributes['course'].value

print ('git test ')
