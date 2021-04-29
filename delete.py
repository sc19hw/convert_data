import sys
import string
import os
import re

string = open("C:/Users/hxw20/Desktop/2121/EnglishEP.txt", "r+", encoding='utf-8').read()
new_str = re.sub('[^a-zA-Z0-9",\n\.]', ' ', string)
open("C:/Users/hxw20/Desktop/2121/EnglishPK.txt", 'w+', encoding='utf-8').write(new_str)