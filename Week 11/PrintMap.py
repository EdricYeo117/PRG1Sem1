map =[['T', ' ', ' ', ' ', 'T'],[' ', 'P', ' ', ' ', ' '],[' ', ' ', ' ', 'T', ' '],[' ', 'T', ' ', ' ', ' ']]

for rows in map:
    line1 = "+"
    line2 = "|"
    for columns in rows:
        line1 += "---+"
        line2 += (" " + columns + " |")
    print(line1+"\n"+line2)
print(line1)

