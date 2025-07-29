# Find the number of occurence of each character in a string
txt = input("Enter a string: ")
char_count = {}
txt = txt.replace(" ","")
i = 0
for i in txt:
    if (i not in char_count):
        char_count[i]=1
    else:
        char_count[i]+=1

print(char_count)