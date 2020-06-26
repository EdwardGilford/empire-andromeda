#Program to convert between the long html link to an icon (for credits, dice, etc) on the spreadsheet and a nice little latex-y shortcut
#unfinished

import csv

naturalWords = ["credit","dice"]

typedWord = ["\\" + naturalWord for naturalWord in naturalWords]
htmlWord =['<img src="C:\\Users\\edwar\\OneDrive\\Documents\\Rook\cards\\\\' + naturalWord +'.png" width="15" height="15">' for naturalWord in naturalWords]


with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
     for row in reader:
         print(row['first_name'], row['last_name'])
