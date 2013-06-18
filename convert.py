#convert out illegal XML UTF characters
#credit to Jason from stackoverflow.com

import fileinput
import sys
def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

        
replaceAll("CCC dso 1.xml","#","")
replaceAll("CCC dso 1.xml","_","")
replaceAll("CCC dso 1.xml","ISBN/ISSN/HBS","ISBNISSNHBS")
replaceAll("CCC dso 1.xml","Book/JournalTitle","BookJournalTitle")
replaceAll("CCC dso 1.xml","ISBN/ISSN/HBS","ISBNISSNHBS")
replaceAll("CCC dso 1.xml","Volume/IssueofJournal","VolumeIssueofJournal")
replaceAll("CCC dso 1.xml","Author/EditorofBook","AuthorEditorofBook")

