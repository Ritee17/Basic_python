# create first dictionary name 'ASC_Value'in pyhton using loop  in which keys are alphabets (lower case letters) and values are their corresponding ASCII code print the final  dictionary items in seperated lines. Also read your first nameand calculate your ASCII score(add ASCII code of each characted or your name ) using that dictionary ASC_Value
f = open("DATA.txt", "r")
data = f.readlines()
word = 0
print(f"There are {len (data)} lines in the file")
for Word in data:
    wordlist = Word.split(" ")
    word += len(wordlist)
print(f"There are {word} words in the file")
f.close()

f = open("DATA.txt", "r")
data1 = f.read()
alpha = 0
dig = 0
for i in list(data1):
    if i.isalpha():
        alpha += 1
    elif i.isnumeric():
        dig += 1
print(f"There are {alpha} alphabets in the line.")
print(f"Ther are {dig} digits in the file.")