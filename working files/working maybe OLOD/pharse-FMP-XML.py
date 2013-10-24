#{http://www.filemaker.com/fmpxmlresult}ERRORCODE - 0
#{http://www.filemaker.com/fmpxmlresult}PRODUCT -   1
#{http://www.filemaker.com/fmpxmlresult}DATABASE -  2
#{http://www.filemaker.com/fmpxmlresult}METADATA -  3
#{http://www.filemaker.com/fmpxmlresult}RESULTSET - 4

##from xml.dom import minidom
##xmldoc = minidom.parse('DSO.xml')
##itemlist = xmldoc.getElementsByTagName('ROW')
##print len(itemlist)
##name = itemlist[0].firstChild.nodeValue
##
##
##for s in name:
##    name = itemlist[2].firstChild.nodeValue.data
##    print name
import xml.etree.ElementTree as ET
tree = ET.parse('DSO.xml')
root = tree.getroot()
thing = tree
##print root.text
##for child in root:
##    print child.tag, child.attrib
#print root[3][5].text

record-num = 3
##Catalog API vars

#searchworksV2
ProductStr = 'none'
Stdnum = root[record-num][9].text
title = root[record-num][4].text
publiserName = root[record-num][13].text

#Quickprice
productStr = 'None'
cccWorkInst = 'None'
publicationYear = root[record-num][12].text
numCopies = root[record-num][7].text
numPages = root[record-num][19].text
entireBook = 'N/A'
print (productStr  cccWorkInst)
##Academic API

#create order header
prdAbrv = 'none'
edInstitution = root[record-num][15].text
courseName = root[record-num][5].text
startOfTerm = root[record-num][6].text
instructorName = root[record-num][8].text
courseNumber = root[record-num][5].text
acctRefNum = '14 + 1 combined to string'
enteredBy = root[record-num][20].text
custRefNum = root[record-num][16].text

#create order detail
cccWorkInst = 'none'
publicationYear = root[record-num][12].text
numCopiesStudents = root[record-num][7].text
numPages = root[record-num][17].text
fromPage = "str split from 'page numbers used'/root[record-num][11] "
toPage = "str split from 'page numbers used'/root[record-num][11] "
Stdnum = root[record-num][9].text
title = root[record-num][4].text
publisherName = root[record-num][13].text
author = 'see logic for this'
dateOfIssue = root[record-num][12].text
volume = root[record-num][18].text
edition = 'N/A'
chapterArticle = root[record-num][1].text
customerRefNum = 'none'









print Stdnum



























