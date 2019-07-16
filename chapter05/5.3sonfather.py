# father son dictionary founding   

mans = {'John':'Samuel','Vasiliy':'Petr','Vladislav':'Uriy','Nikolai':'Andrei'}
rules = ("""

        Welcome to Generator of heroes
        chose attribute

        0 - exit
        1 - show all names
        2 - add couple
        3 - remove couple
        4 - change name
        5 - change father name
        6 - show cople
    
""")
show = 1
add  = 2
remove = 3
change_name = 4
change_ftname = 5
show_1=6
#enter = input('Type name of son\n')
#output = mans.get(enter,"Not founded")
print(rules)

menu = int(input("Make your choice\t"))
while menu != 0:
    if menu == show:
        print(mans)
    elif menu == add:
        name = input("Enter name that you want add\t")
        fathr_name = input("Enter father name you want add\t")
        mans.update({name:fathr_name})
    elif menu == remove:
        name = input("Enter the name wich you want to delete\t")
        mans.pop(name)
    elif menu == change_name:
        old_name = input("Enter the old name\t")
        name = input("Enter the new name\t")
        mans[name] = mans.pop(old_name)
    elif menu == change_ftname:
        old_ftname = input("Enter the old father name \t")
        name = input("Enter new father name\t")
        mans[old_ftname] = name
    elif menu == show_1:
        enter = input("Enter name \t")
        output = mans.get(enter,"Not founded")
        print("\t",mans.get(enter,"Not founded"))
    print(rules)
    menu = int(input("Make your choice\t"))