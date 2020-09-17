#Program to convert between the long html link to an icon (for credits, dice, etc) on the spreadsheet and a nice little latex-y shortcut

import pandas as pd

directory = "D:\\Documents\\empire-andromeda\\Cards\\Images\\"

naturalWords = ["credit","die","point","unit",]

typedWords = [";" + naturalWord for naturalWord in naturalWords]
htmlWords =['<img src="' + directory + naturalWord +'.png" width="15" height="15">' for naturalWord in naturalWords]

def conversion(text):
    for i in range(len(typedWords)):
        text = text.replace(typedWords[i], htmlWords[i])
    return text

df = pd.read_csv('tim_plan_cards.csv')
df['ability'] = df['ability'].map(conversion)

df.to_csv('tim_card_for_nandeck.csv')
input("Done")
