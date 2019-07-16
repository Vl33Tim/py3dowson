#Текст наоборот||торобоан тскеТ

invert = "" 
org_str = input("Введите слово: ")
length = len(org_str)
for i in range (0, (length )):
    invert += org_str[length - i - 1 :length - i]#срез строки по 1-му символу начиная с последнего символа
print(invert)
    
