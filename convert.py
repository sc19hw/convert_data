import sys
import string
import os

with open("C:/Users/hxw20/Desktop/2121/EnglishEP.txt","r+", encoding='utf-8') as file:
    for line in file.readlines():
        line=line.replace('"',"")
        line=line.replace('“',"")
        line=line.replace(',',"")
        line=line.strip('\n')
        line=line.replace("<p>",'"')
        line=line.replace("</p>",'"')
        if line.find("<doc") != -1 :
            file.write("")
        elif line.find("</doc>") != -1 :
            file.write("")
        elif line.find('"') != -1 :
            file.write(line+",Pakistan"+'\n')
        elif line.find('\n') :
            file.write("")
        else:
            line = '"' + line + '"'
            file.write(line+",Pakistan"+'\n')
file.close()