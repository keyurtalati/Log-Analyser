import re
from termcolor import colored
def search_function(stringtosearch):
    with open('Server_Log.txt', "r") as fh:
        fstring=fh.readlines()
    linenumber=0
    result=[]
    extractword=[]
    for line in fstring:
        linenumber=linenumber+1
        word = re.search(stringtosearch, line)
        if(word):
            i=fstring[linenumber-1]
            extractword.append(i)
    ip=[]
    for i in extractword:
        words = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', i)
        ip.append(words.group())
    dictOfElements = dict()
    for element in ip:
        if element in dictOfElements:
            dictOfElements[element] += 1
        else:
            dictOfElements[element] = 1
    dictOfElements = {key: value for key, value in dictOfElements.items() if value > 0}
    for key, value in dictOfElements.items():
        print("\t",colored(key,"red"), ' :: ', colored(value,"yellow"))

with open('./Server_Log.txt', "r") as fh:
    fstring=fh.readlines()
lst=[]
for line in fstring:
    word = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line)
    word=word.group()
    lst.append(word)
dictOfElems = dict()
for elem in lst:
    if elem in dictOfElems:
        dictOfElems[elem] += 1
    else:
        dictOfElems[elem] = 1
dictOfElems = {key: value for key, value in dictOfElems.items() if value > 0}
total=0
for key, value in dictOfElems.items():
        total=total+value
for key, value in dictOfElems.items():  
        per=value/total
        print(colored(key,"red") , ' : ', colored(value,"green"),' : ',colored(per*100,"yellow") ,colored('%',"yellow")) 

print("")
print(" 1 : SQL Injection")
print(" 2 : Directory traversal attack")
print(" 3 : Cross site scripting (XSS)")
print(" 4 : Password finding attempt")
choise=int(input(colored("\nEnter your choice : ","blue")))
if(choise==1):
    print("\nOutput for SQL Injection attacks are as follow...\n")
    print("sleep based attacks")
    search_function("sleep")
    print("select based attacks")
    search_function("select")
if(choise==2):
    print("\nOutput for directory traversal attacks are as follow...\n")
    search_function("../../../")
if(choise==3):
    print("\nOutput for XSS attacks are as follow...\n")
    print("Alert based XSS")
    search_function("alert")
    print("Prompt based XSS")
    search_function("prompt")
if(choise==4):
    print("\nOutput for password finding attacks are as follow...\n")
    search_function("etc/passwd")