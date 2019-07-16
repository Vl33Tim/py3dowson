# generator of heroes, atributes

attrbutes = 30
health = 0
strengh = 0
intelegence = 0 
agility = 0

rules = ("""

        Welcome to Generator of heroes
        chose attribute

        0 - exit
        1 - health
        2 - strenght
        3 - intelegence
        4 - agility
        5 - show state

    
""")
print(rules)
menu = input("\tMake your choice \n\t")

while menu != "0":
    decision = 1
    if menu == "1":
        while decision != 0:
            decision = int(input("\tEnter number of health 'b'-back to previous menu\n\t"))
            if 30 < (health + decision) < 0  or (attrbutes - decision) < 0 :
                print("\tIt's incorrect number, must be >0 and <=30\n\t")
            elif decision == 0:
                print("\tBack to previous menu\n\t")
            else:
                health += decision
                attrbutes -= decision
                print("\tHealth now is {}  {}\n".format(health,"#"*health))
                print("\t{} free point left".format(attrbutes))
            
    elif menu == "2":
        while decision != 0:
            decision = int(input("\tEnter number of strenght 'b'-back to previous menu\n\t"))
            if 30 < (strengh + decision) < 0  or attrbutes - decision < 0 :
                print("\tIt's incorrect number, must be >0 and <=30\n\t")
            elif decision == 0:
                print("\tBack to previous menu\n\t")
            else:
                strengh += decision
                attrbutes -= decision
                print("\tHealth now is {}  {}\n\t".format(strengh,"#"*strengh))
                print("\t{} free point left\t".format(attrbutes))
    elif menu == "3":
        while decision != 0:
            decision = int(input("\tEnter number of intelegence 'b'-back to previous menu\n\t"))
            if 30 < (intelegence + decision) < 0  or attrbutes - decision < 0 :
                print("\tIt's incorrect number, must be >0 and <=30\n\t")
            elif decision == 0:
                print("\tBack to previous menu\n\t")
            else:
                intelegence += decision
                attrbutes -= decision
                print("\tIntelegence now is {}  {}\n\t".format(intelegence,"#"*intelegence))
                print("\t{} free point left\t".format(attrbutes))
    elif menu == "4":
        while decision != 0:
            decision = int(input("enter number of agility 'b'-back to previous menu\n\t"))
            if 30 < (agility + decision) < 0  or attrbutes - decision < 0 :
                print("\tIt's incorrect number, must be >0 and <=30\n\t")
            elif decision == 0:
                print("\tBack to previous menu\n")
            else:
                agility += decision
                attrbutes -= decision
                print("\tHealth now is {}  {}\n".format(agility,"#"*agility))
                print("\t{} free point left".format(attrbutes))
    elif menu == "5":
        print("\tHealth now is {}  {}\n".format(health,"#"*health))
        print("\tStrenght now is {}  {}\n".format(strengh,"#"*strengh))
        print("\tIntelegence now is {}  {}\n".format(intelegence,"#"*intelegence))
        print("\tHealth now is {}  {}\n".format(agility,"#"*agility))
        print("\t{} free point left".format(attrbutes))
    print(rules)
    menu = input("\tMake your choice\n\t")