#convert out illegal XML UTF characters
#credit to Jason from stackoverflow.com

import fileinput
import sys
def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

        
replaceAll("DSO.xml","#","")
replaceAll("DSO.xml","_","")
replaceAll("DSO.xml","ISBN/ISSN/HBS","ISBNISSNHBS")
replaceAll("DSO.xml","Book/JournalTitle","BookJournalTitle")
replaceAll("DSO.xml","ISBN/ISSN/HBS","ISBNISSNHBS")
replaceAll("DSO.xml","Volume/IssueofJournal","VolumeIssueofJournal")
replaceAll("DSO.xml","Author/EditorofBook","AuthorEditorofBook")

