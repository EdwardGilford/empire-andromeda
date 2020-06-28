#Program to convert between the long html link to an icon (for credits, dice, etc) on the spreadsheet and a nice little latex-y shortcut

import pandas as pd

naturalWords = ["credit","die","point","unit",]

typedWords = [";" + naturalWord for naturalWord in naturalWords]
htmlWords =['<img src="C:\\Users\\edwar\\OneDrive\\Documents\\Rook\cards\\' + naturalWord +'.png" width="15" height="15">' for naturalWord in naturalWords]

def conversion(text):
    for i in range(len(typedWords)):
        text = text.replace(typedWords[i], htmlWords[i])
    return text

df = pd.read_csv('ea_card_for_edit.csv')
df['ability'] = df['ability'].map(conversion)

df.to_csv('ea_card_for_nandeck.csv')
input("Done")
